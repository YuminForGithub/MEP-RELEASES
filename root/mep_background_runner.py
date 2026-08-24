# Change hotkey in CONFIG when comment says It is ok to change.
# I used ChatGPT Codex to work with, but after just 2 works of this, We had to upgrade my plan from free to more complicated...

"""
## MEP RELEASE: v1.0.2 "Alpha" [2020 - 2024 update!]
Module (or Alternate runner) `mep_background_runner(.py)` is alternate module to run `MEP RELEASE 1 Prototype` directly. Please use this module in right usage following:

Usage:
  - `main()`
  Runs main thread. It will work outside the program.

  - `Config`
  Config modifier.

End of Usage.

  LIST OF `Config`
    - `resetAll()`
    Resets all config.

    - `ChangeConfig`
    Config changer, From here please read README.py (soon be updated)

Change Configs:
  Change configs in `CONFIGS` row of this module file.
  But some of configs are limited to change, Or changing it even breaks full code.
  So please be careful and read the Important information carefully.
  If you know how to modify in module range, Please use `...Config.ChangeConfig` to modify in long-range.

* `...` : means `mep_background_runner.` to be make information shorter. So `...main()` means `mep_background_runner.main()`.
"""

import atexit # So, What even is this?
import ctypes # Uhh
import signal # Never heard of this
import sys
import threading
import psutil
from ctypes import wintypes
import webbrowser

import pyautogui as pgu # Firing spells here. Pyautogui gave me mouse movement very freely moved by a program. I like it

from m import MEP # If you are getting error HERE, Be sure this file is in same folder as m.py

if __name__ != "__main__":
  print("INFO: Detected this is running in module or etc, unmain status. Are you running in modules?")

current_battery = psutil.sensors_battery()

if current_battery is not None:
  percent = current_battery.percent

  if not current_battery.power_plugged:

    if percent <= 10:
      input(
        "WARNING: CURRENT BATTERY IS SUPER LOW AND MAY "
        "LEAD TO SHUT OFF COMPUTER WHILE RUNNING.\n"
        "PLEASE BE SUPER SURE YOU CAN RUN THIS WHILE LOW BATTERY!\n"
        "Press Enter after understanding and confirming, "
        "or close this program with Ctrl+C."
      )

    elif percent < 12:
      input(
        "WARNING: CURRENT BATTERY IS FATALLY LOW AND MAY "
        "LEAD TO SHUT OFF COMPUTER WHILE RUNNING.\n"
        "Press Enter after understanding!"
      )

    elif percent < 15:
      print(
        "WARNING: CURRENT BATTERY IS LOW AND MAY LEAD "
        "TO SHUT OFF COMPUTER WHILE RUNNING."
      )


# ============================================================
# CONFIG
# ============================================================

# 𝗜𝗺𝗽𝗼𝗿𝘁𝗮𝗻𝘁:⁡ 𝘿𝙊 𝙉𝙊𝙏 𝘾𝙃𝘼𝙉𝙂𝙀 𝙏𝙃𝙀 𝘾𝙊𝘿𝙀 𝙊𝙐𝙏𝙎𝙄𝘿𝙀 𝘾𝙊𝙈𝙈𝙀𝙉𝙏 𝙎𝘼𝙔𝙄𝙉𝙂 𝙄𝙏 𝙄𝙎 𝙎𝘼𝙁𝙀 𝙏𝙊 𝘾𝙃𝘼𝙉𝙂𝙀!

SPELL_HOTKEYS = { # SAFE TO CHANGE.
  # USAGE: "(hotkey)": "(spell to use)", ... end: no comma.
  # SYMBOLS [i: I, e: -, v: V, u: Up-V, l: lightning, h: heart, spiral: (same)]
  "1":  "i",
  "2":  "e",
  "3": "v",
  "4": "u",
  "5":  "l",
  "6":  "h",
  "7": "spiral",
  "8": "circle"
}

ABORT_HOTKEY = "9" # ⁡⁣⁢⁣⁡⁣⁢SAFE TO CHANGE.⁡ (Please be sure remember this hotkey when changing for emergency reasons.)
QUIT_HOTKEY = "0" # SAFE TO CHANGE.

# Coordinates for each spell.
# Change these whenever you want. ⁡⁣⁢SAFE TO CHANGE.
SPELLS = {
  # USAGE: "(symbol)": (x, y, l)
  # WARNING: Variable 'l'(right-side) should be used at v, u, i, e and nothing else or code will break!
  "v": (600, 500, 80),
  "u": (600, 500, 80),
  "i": (600, 500, 80),
  "e": (600, 500, 80),
  "l": (600, 500),
  "h": (600, 500),
  "spiral": (600, 500),
  "circle": (600, 500)
}

pgu.PAUSE = 0.015 # Safe to change. Delay every spell drawing steps, Do not go lower than 0.014.
SPELL_DURATION = 0.075 # Safe to change, but putting lower than default may cause to web cannot interact with mouse.
SEQUENCE_DELAY = 0.018 # Safe to change. Delay every sequence of spell. Do not go lower than 0.0156.

RELEASE_KEYS = [ # Do not change this.
  "left", "right", "up", "down",
  "w", "a", "s", "d",
  "space", "enter",
  "shift", "ctrl", "alt", "win",
]

# ============================================================
# UPDATED FEATURE: Change configs in module runner!
# ============================================================

class Configs:
  def resetAll(self):
    global SPELLS, SPELL_DURATION, SEQUENCE_DELAY, ABORT_HOTKEY, QUIT_HOTKEY, SPELL_HOTKEYS
    SPELLS = {
      "v": (600, 500, 80),
      "u": (600, 500, 80),
      "i": (600, 500, 80),
      "e": (600, 500, 80),
      "l": (600, 500),
      "h": (600, 500),
    }
    SPELL_HOTKEYS = {
      "1":  "i",
      "2":  "e",
      "3": "v",
      "4": "u",
      "5":  "l",
      "6":  "h",
      "7": "spiral"
    }
    ABORT_HOTKEY = "8"
    QUIT_HOTKEY = "9"
    SPELL_DURATION = 0.11
    SEQUENCE_DELAY = 0.018
    pgu.PAUSE = 0.016

  class ChangeConfigs:
    class Spells:
      global SPELLS, SPELL_DURATION, SEQUENCE_DELAY
      def changeSpellConfigs(self, target: dict):
        """
        Args:
          target: dict
            v, u, i, e: (x, y, l)
            Like: "v": (x, y, l), "u" ... "e": (x, y, l)
            left-side l and h does not need right-side l
        """
        global SPELLS
        SPELLS = target

      def changePause(self, to: float):
        pgu.PAUSE = to

      def changeDuration(self, to: float):
        global SPELL_DURATION
        SPELL_DURATION = to

      def changeDelay(self, to: float):
        global SEQUENCE_DELAY
        SEQUENCE_DELAY = to

    def changeHotkey(self, target: dict):
      global SPELL_HOTKEYS
      SPELL_HOTKEYS = target

    def abortHotkey(self, to: str):
      global ABORT_HOTKEY
      ABORT_HOTKEY = to

    def quitHotkey(self, to: str):
      global QUIT_HOTKEY
      QUIT_HOTKEY = to
      

# ============================================================
# WINDOWS GLOBAL HOTKEYS
# CRITICAL FOR CHANGING ANY.
# ============================================================

WM_HOTKEY = 0x0312

MOD_ALT = 0x0001
MOD_CONTROL = 0x0002
MOD_SHIFT = 0x0004
MOD_WIN = 0x0008
MOD_NOREPEAT = 0x4000

HOTKEY_RUN_BASE = 100
HOTKEY_ABORT = 200
HOTKEY_QUIT = 201

MODIFIERS = {
  "alt": MOD_ALT,
  "ctrl": MOD_CONTROL,
  "control": MOD_CONTROL,
  "shift": MOD_SHIFT,
  "win": MOD_WIN,
  "windows": MOD_WIN,
  "cmd": MOD_WIN,
}

KEY_CODES = {
  "esc": 0x1B,
  "escape": 0x1B,
  "space": 0x20,
  "enter": 0x0D,
  "return": 0x0D,
  "tab": 0x09,
  "backspace": 0x08,
  "delete": 0x2E,
  "insert": 0x2D,
  "home": 0x24,
  "end": 0x23,
  "pageup": 0x21,
  "pagedown": 0x22,
  "left": 0x25,
  "up": 0x26,
  "right": 0x27,
  "down": 0x28,
}

for index in range(1, 25):
  KEY_CODES[f"f{index}"] = 0x6F + index

for code in range(ord("a"), ord("z") + 1):
  KEY_CODES[chr(code)] = code

for code in range(ord("0"), ord("9") + 1):
  KEY_CODES[chr(code)] = code


user32 = ctypes.WinDLL(
  "user32",
  use_last_error=True
)

user32.RegisterHotKey.argtypes = [
  wintypes.HWND,
  ctypes.c_int,
  wintypes.UINT,
  wintypes.UINT,
]

user32.RegisterHotKey.restype = wintypes.BOOL

user32.UnregisterHotKey.argtypes = [
  wintypes.HWND,
  ctypes.c_int,
]

user32.UnregisterHotKey.restype = wintypes.BOOL

user32.GetMessageW.argtypes = [
  ctypes.POINTER(wintypes.MSG),
  wintypes.HWND,
  wintypes.UINT,
  wintypes.UINT,
]

user32.GetMessageW.restype = wintypes.BOOL


def parse_hotkey(hotkey):
  modifiers = MOD_NOREPEAT
  key = None

  for raw_part in hotkey.lower().replace(" ", "").split("+"):
    if not raw_part:
      continue

    if raw_part in MODIFIERS:
      modifiers |= MODIFIERS[raw_part]

    elif raw_part in KEY_CODES:
      if key is not None:
        raise ValueError(
          f"Hotkey has more than one main key: {hotkey}"
        )

      key = KEY_CODES[raw_part]

    else:
      raise ValueError(
        f"Unknown hotkey part: {raw_part}"
      )

  if key is None:
    raise ValueError(
      f"Hotkey needs a main key: {hotkey}"
    )

  return modifiers, key


def register_hotkey(hotkey_id, hotkey):
  modifiers, key = parse_hotkey(hotkey)

  if user32.RegisterHotKey(
    None,
    hotkey_id,
    modifiers,
    key
  ):
    return

  error = ctypes.get_last_error()

  raise OSError(
    error,
    f"Could not bind {hotkey!r}. "
    "Another app may already use it."
  )


def unregister_hotkey(hotkey_id):
  user32.UnregisterHotKey(
    None,
    hotkey_id
  )


# ============================================================
# MEP BACKGROUND RUNNER (CORE SYSTEM)
# SAFE THINGS CAN BE CHANGED OR ENHANCED.
# BUT CHANGING CORE MAY RESULT TO ERROR.
# ============================================================

class MEPBackgroundRunner:

  def __init__(self):
    self.mep = MEP()
    self.lock = threading.Lock()
    self.exiting = False

    pgu.FAILSAFE = True

  # ----------------------------------------------------------
  # FIRE SPELL
  # Update if you want. Pleasure!
  # ----------------------------------------------------------

  def fire_spell(self, spell):
    with self.lock:

      if self.exiting:
        return

      # Stop an old spell first. Stops thread bomb when spamming `spells` or in some reasons, A `fork bomb.`
      self.mep.stop()
      self.mep.start()

      try:

        if spell == "v":
          x, y, d = SPELLS["v"]

          self.mep.drawer.v(
            x,
            y,
            d,
            dur=SPELL_DURATION
          )

        elif spell == "u":
          x, y, d = SPELLS["u"]

          self.mep.drawer.up_v(
            x,
            y,
            d,
            dur=SPELL_DURATION
          )

        elif spell == "i":
          x, y, d = SPELLS["i"]

          self.mep.drawer.i(
            x,
            y,
            d,
            dur=SPELL_DURATION
          )

        elif spell == "e":
          x, y, d = SPELLS["e"]

          self.mep.drawer.e(
            x,
            y,
            d,
            dur=SPELL_DURATION
          )

        elif spell == "l":
          x, y = SPELLS["l"]

          self.mep.drawer.l(
            x,
            y,
            dur=SPELL_DURATION
          )

        elif spell == "h":
          x, y = SPELLS["h"]

          self.mep.drawer.h(
            x,
            y,
            dur=SPELL_DURATION
          )

        elif spell == "spiral":
          x, y = SPELLS["spiral"]

          self.mep.drawer.spiral(
            x,
            y,
            dur=SPELL_DURATION,
            divider=0.3
          )

        elif spell == "circle":
          x, y = SPELLS["circle"]

          self.mep.drawer.circle(
            x,
            y,
            dur=SPELL_DURATION,
            divider=0.3
          )

        else:
          raise ValueError(
            f"Unknown spell: {spell}"
          )

      except pgu.FailSafeException:
        print(
          f"PyAutoGUI failsafe activated "
          f"during {spell.upper()}."
        )

      except Exception as error:
        print(
          f"Error firing {spell.upper()}: {error}"
        )

      finally:
        self.cleanup_inputs()

  # ----------------------------------------------------------
  # THREAD (Lowering the spell's duration as possible)
  # ----------------------------------------------------------

  def fire_spell_thread(self, spell):
    threading.Thread(
      target=self.fire_spell,
      args=(spell,),
      daemon=True
    ).start()

  # ----------------------------------------------------------
  # ABORT (Emergency Usage)
  # ----------------------------------------------------------

  def abort_now(self):
    self.mep.stop()
    self.cleanup_inputs()

    print("MEP ABORTED.")

  # ----------------------------------------------------------
  # CLEANUP
  # ----------------------------------------------------------

  def cleanup_inputs(self):
    try:
      self.mep.drawer.end()
    except Exception:
      pgu.mouseUp()

    for key in RELEASE_KEYS:
      try:
        self.mep.keyboard.release(key)
      except Exception:
        pass

  # ----------------------------------------------------------
  # RUN
  # ----------------------------------------------------------

  def run(self):

    registered = []

    try:

      # Register spell hotkeys.
      for index, (hotkey, spell) in enumerate(
        SPELL_HOTKEYS.items()
      ):
        hotkey_id = HOTKEY_RUN_BASE + index

        register_hotkey(
          hotkey_id,
          hotkey
        )

        registered.append(hotkey_id)

      # Abort.
      register_hotkey(
        HOTKEY_ABORT,
        ABORT_HOTKEY
      )

      registered.append(
        HOTKEY_ABORT
      )

      # Quit.
      register_hotkey(
        HOTKEY_QUIT,
        QUIT_HOTKEY
      )

      registered.append(
        HOTKEY_QUIT
      )

      print()
      print("================================")
      print(" MEP BACKGROUND SPELL RUNNER")
      print("================================")

      for hotkey, spell in SPELL_HOTKEYS.items():
        print(
          f"{hotkey:>8} → {spell.upper()}"
        )

      print(
        f"{ABORT_HOTKEY:>8} → ABORT"
      )

      print(
        f"{QUIT_HOTKEY:>8} → QUIT"
      )

      print()
      print("Runner is active.")
      print(
        "PyAutoGUI failsafe: move mouse "
        "to a screen corner."
      )

      msg = wintypes.MSG()

      while not self.exiting:

        result = user32.GetMessageW(
          ctypes.byref(msg),
          None,
          0,
          0
        )

        if result == 0:
          break

        if result == -1:
          raise ctypes.WinError(
            ctypes.get_last_error()
          )

        if msg.message != WM_HOTKEY:
          continue

        hotkey_id = int(msg.wParam)

        # Spell hotkeys
        for index, spell in enumerate(
          SPELL_HOTKEYS.values()
        ):
          if hotkey_id == HOTKEY_RUN_BASE + index:

            print(
              f"FIRE: {spell.upper()}"
            )

            self.fire_spell_thread(
              spell
            )

            break

        # Abort
        if hotkey_id == HOTKEY_ABORT:
          self.abort_now()

        # Quit
        elif hotkey_id == HOTKEY_QUIT:
          self.exiting = True

    finally:

      self.exiting = True
      self.mep.stop()
      self.cleanup_inputs()

      for hotkey_id in registered:
        unregister_hotkey(
          hotkey_id
        )


# ============================================================
# MAIN
# ============================================================

def main(redirect_now: bool = False):
  """
  Runs main system.
  Args:
    redirect_now: Redirects browser to halloween 2016 (google doodle, MCA1) instantly

  Raises:
    RuntimeError: When platform is not Windows (`sys.platform != win32`)
  """
  if sys.platform != "win32":
    raise RuntimeError(
      "This runner requires Windows."
      # You are probably running this program in windows, right?
    )

  runner = MEPBackgroundRunner()

  atexit.register(
    runner.cleanup_inputs
  )

  def handle_signal(
    _signum,
    _frame
  ):
    runner.exiting = True
    runner.mep.stop()
    runner.cleanup_inputs()
    raise KeyboardInterrupt

  signal.signal(
    signal.SIGINT,
    handle_signal
  )

  if hasattr(signal, "SIGTERM"):
    signal.signal(
      signal.SIGTERM,
      handle_signal
    )

  if redirect_now:
    openversion = int(input("""\
Which doodle to open?
1: Halloween 2016, 2: Halloween 2020, 3: Halloween 2024.
(Note: 2020-2024 needs spell `spiral`. It is neccessary, but 2016 will not work with spiral.)
>> """))
    match openversion:
      case 1:
        link = "https://www.google.com/logos/2016/halloween16/halloween16.html"
      case 2:
        link = "https://www.google.com/logos/2020/halloween20/rc1/halloween20.html"
      case 3:
        link = "https://www.google.com/logos/2024/halloween24/rc3/halloween24.html?hl=en&origin=www.google.com"
      case _:
        print("""\
ERROR: Bad version information
Provide 1, 2, or 3 while try of redirect doodle.""")
        exit(9)
    webbrowser.open(link)
  
  runner.run()


if __name__ == "__main__":
  main() # Main object

# I pronounce you are a programmer!