# If you are reading this... EASTER EGG!!!!!
# Yumin1004 (c) 2026
# Use this file if you are not sure if that main file is functionable!

try:
  import tkinter as tk
  import time
except:
  print("It seems needed package(s) are missing or corrupted. Executing automatic installer.")
  import subprocess
  subprocess.run(['pip3', 'install', 'tkinter', 'time'])

try:
  from m import MEP, Sequencer
except:
  print("FATAL ERROR: MISSING MAIN FILE!!!\nMake sure you installed full package!")
  exit(1)

class MouseTester:
  def __init__(self, root):
    self.root = root

    self.mouse_x = 0
    self.mouse_y = 0
    self.last_x = None
    self.last_y = None
    self.dragging = False
    self.mep = MEP()
    self.seq = Sequencer(self.mep)

    self.position_label = tk.Label(
      root,
      text="Mouse: (0, 0)",
      font=("Consolas", 16)
    )
    self.position_label.pack(pady=10)

    self.state_label = tk.Label(
      root,
      text="State: Nothing",
      font=("Consolas", 14)
    )
    self.state_label.pack()

    self.canvas = tk.Canvas(
      root,
      width=700,
      height=400,
      bg="white"
    )
    self.canvas.pack(padx=10, pady=10)

    buttons = tk.Frame(root)
    buttons.pack(pady=5)

    tk.Button(
      buttons,
      text="START SEQUENCE",
      command=self.start_sequence,
      width=18
    ).pack(
      side=tk.LEFT,
      padx=5
    )

    tk.Button(
      buttons,
      text="ABORT",
      command=self.abort,
      width=12,
      bg="red",
      fg="white"
    ).pack(
      side=tk.LEFT,
      padx=5
    )

    self.log = tk.Text(
      root,
      width=80,
      height=10,
      font=("Consolas", 10)
    )
    self.log.pack(padx=10, pady=10)

    # Mouse events
    self.canvas.bind("<Motion>", self.motion)
    self.canvas.bind("<ButtonPress-1>", self.press)
    self.canvas.bind("<ButtonRelease-1>", self.release)
    self.canvas.bind("<B1-Motion>", self.drag)
    self.root.bind("<Escape>", lambda event: self.abort())

  def log_event(self, text):
    timestamp = time.perf_counter()

    self.log.insert(
      tk.END,
      f"{timestamp:.6f}  {text}\n"
    )

    self.log.see(tk.END)

  def draw_trail(self, x, y):
    if self.last_x is not None and self.last_y is not None:
      self.canvas.create_line(
        self.last_x,
        self.last_y,
        x,
        y,
        width=3
      )

    self.last_x = x
    self.last_y = y

  def motion(self, event):
    self.mouse_x = event.x
    self.mouse_y = event.y

    self.position_label.config(
      text=f"Mouse: ({event.x}, {event.y})"
    )

    if not self.dragging:
      self.state_label.config(
        text="State: Moving"
      )

    # Only draw trail while dragging
    if self.dragging:
      self.draw_trail(event.x, event.y)

  def press(self, event):
    self.dragging = True

    self.last_x = event.x
    self.last_y = event.y

    self.state_label.config(
      text="State: LEFT BUTTON DOWN"
    )

    self.log_event(
      f"CLICK DOWN   window=({event.x}, {event.y})"
    )

  def release(self, event):
    self.dragging = False

    self.draw_trail(event.x, event.y)

    self.state_label.config(
      text="State: LEFT BUTTON RELEASED"
    )

    self.log_event(
      f"CLICK UP     window=({event.x}, {event.y})"
    )

    self.last_x = None
    self.last_y = None

  def drag(self, event):
    self.mouse_x = event.x
    self.mouse_y = event.y

    self.position_label.config(
      text=f"Mouse: ({event.x}, {event.y})"
    )

    self.state_label.config(
      text="State: DRAGGING"
    )

    self.draw_trail(event.x, event.y)

    self.log_event(
      f"DRAG         window=({event.x}, {event.y})"
    )

  def start_sequence(self):
    sequence = [
      ("v", 600, 500, 40),
      ("i", 650, 450, 50),
      ("h", 600, 500),
      ("l", 650, 400),
    ]

    started = self.seq.play(
      sequence,
      delay=0.018
    )

    if not started:
      self.state_label.config(
        text="State: SEQUENCE ALREADY RUNNING"
      )

      self.log_event(
        "SEQUENCE ALREADY RUNNING"
      )

      return

    self.state_label.config(
      text="State: SEQUENCE RUNNING"
    )

    self.log_event(
      "SEQUENCE START delay=0.018"
    )

  def abort(self):
    self.seq.stop()

    self.state_label.config(
      text="State: ABORTED"
    )

    self.log_event(
      "!!! ABORT !!!"
    )

  def close(self):
    self.seq.stop()
    self.root.destroy()


root = tk.Tk()
root.title("Mouse Input Laboratory")
root.geometry("850x700")

app = MouseTester(root)

root.protocol("WM_DELETE_WINDOW", app.close)

root.mainloop()
