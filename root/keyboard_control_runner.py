import signal
import sys
import threading
import tkinter as tk
from tkinter import messagebox

import pyautogui as pgu

from m import AbortController, Drawer, KeyboardMacro, MEP


ALLOWED_KEYS = {
  "left",
  "right",
  "up",
  "down",
  "w",
  "a",
  "s",
  "d",
  "space",
  "enter",
  "shift",
  "ctrl",
  "alt",
}

RELEASE_KEYS = sorted(ALLOWED_KEYS | {"win"})


class KeyboardRunner:
  def __init__(self, root):
    self.root = root
    self.mep = MEP()
    self.abort = self.mep.abort
    self.keyboard = self.mep.keyboard
    self.drawer = self.mep.drawer
    self.worker = None
    self.lock = threading.Lock()
    self.closed = False

    self._check_api()

    pgu.FAILSAFE = True
    pgu.PAUSE = 0.03

    self.status = tk.StringVar(value="Ready")
    self.keys_text = tk.StringVar(value="left right up down w a s d")

    self.root.title("MEP Keyboard Runner")
    self.root.geometry("640x360")
    self.root.protocol("WM_DELETE_WINDOW", self.close)
    self.root.bind_all("<Escape>", lambda _event: self.abort_now("Escape"))
    self.root.bind_all("<Control-c>", lambda _event: self.abort_now("Ctrl+C"))

    self._build_ui()
    self._install_signals()

  def _check_api(self):
    if not isinstance(self.abort, AbortController):
      raise TypeError("MEP.abort is not an AbortController")

    if not isinstance(self.keyboard, KeyboardMacro):
      raise TypeError("MEP.keyboard is not a KeyboardMacro")

    if not isinstance(self.drawer, Drawer):
      raise TypeError("MEP.drawer is not a Drawer")

  def _build_ui(self):
    top = tk.Frame(self.root)
    top.pack(fill=tk.X, padx=12, pady=12)

    tk.Label(top, text="Keys").pack(side=tk.LEFT)

    tk.Entry(top, textvariable=self.keys_text).pack(
      side=tk.LEFT,
      fill=tk.X,
      expand=True,
      padx=8,
    )

    tk.Button(top, text="Run", command=self.run).pack(side=tk.LEFT)

    tk.Button(
      top,
      text="ABORT",
      command=lambda: self.abort_now("button"),
      bg="#b00020",
      fg="white",
    ).pack(side=tk.LEFT, padx=(8, 0))

    tk.Label(self.root, textvariable=self.status, anchor="w").pack(
      fill=tk.X,
      padx=12,
    )

    self.target = tk.Text(self.root, height=8)
    self.target.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)
    self.target.insert(
      tk.END,
      "This box is the safe keyboard target.\n"
      "Allowed keys: "
      + " ".join(sorted(ALLOWED_KEYS))
      + "\nAbort: Escape, Ctrl+C, ABORT, close window, or terminal interrupt.\n",
    )
    self.target.focus_set()

    self.log = tk.Text(self.root, height=5, state=tk.DISABLED)
    self.log.pack(fill=tk.BOTH, expand=False, padx=12, pady=(0, 12))

  def _install_signals(self):
    for name in ("SIGINT", "SIGTERM"):
      signum = getattr(signal, name, None)

      if signum is None:
        continue

      try:
        signal.signal(
          signum,
          lambda _signum, _frame, source=name: self.abort_now(source),
        )
      except (OSError, ValueError):
        pass

  def parse_keys(self):
    keys = [key.lower() for key in self.keys_text.get().split()]
    bad = [key for key in keys if key not in ALLOWED_KEYS]

    if bad:
      raise ValueError("Not allowed: " + ", ".join(bad))

    if not keys:
      raise ValueError("Enter at least one key.")

    return keys

  def run(self):
    with self.lock:
      if self.worker and self.worker.is_alive():
        self.log_safe("Already running.")
        return

      try:
        keys = self.parse_keys()
      except ValueError as exc:
        messagebox.showerror("Key sequence", str(exc))
        return

      self.mep.start()
      self.target.focus_force()
      self.set_status("Running: " + " ".join(keys))

      self.worker = threading.Thread(
        target=self.run_worker,
        args=(keys,),
        daemon=True,
      )
      self.worker.start()

  def run_worker(self, keys):
    message = "Finished."

    try:
      if self.abort.wait(0.4):
        message = "Aborted before first key."
        return

      for key in keys:
        if self.abort.check():
          message = "Aborted."
          return

        ok = self.keyboard.press(key, duration=0.08)

        if not ok:
          message = "Aborted during key press."
          return

        if self.abort.wait(0.12):
          message = "Aborted between keys."
          return
    except pgu.FailSafeException:
      message = "Aborted by PyAutoGUI failsafe."
      self.mep.stop()
    except Exception as exc:
      message = "Error: " + str(exc)
      self.mep.stop()
    finally:
      self.cleanup_inputs()
      self.after_ui(self.worker_finished, message)

  def cleanup_inputs(self):
    self.drawer.end()

    for key in RELEASE_KEYS:
      self.keyboard.release(key)

  def abort_now(self, source):
    self.mep.stop()
    self.cleanup_inputs()
    self.set_status("Aborted by " + source + ".")

  def close(self):
    self.closed = True
    self.abort_now("window close")
    self.root.after(100, self.root.destroy)

  def worker_finished(self, message):
    self.set_status(message)

    with self.lock:
      self.worker = None

  def after_ui(self, callback, *args):
    try:
      self.root.after(0, callback, *args)
    except (RuntimeError, tk.TclError):
      pass

  def set_status(self, message):
    if self.closed:
      return

    self.status.set(message)
    self.log_safe(message)

  def log_safe(self, message):
    if self.closed:
      return

    self.log.configure(state=tk.NORMAL)
    self.log.insert(tk.END, message + "\n")
    self.log.see(tk.END)
    self.log.configure(state=tk.DISABLED)


if __name__ == "__main__":
  app_root = tk.Tk()
  app = KeyboardRunner(app_root)

  try:
    app_root.mainloop()
  finally:
    try:
      app.abort_now("main exit")
    except tk.TclError:
      pass

  sys.exit(0)
