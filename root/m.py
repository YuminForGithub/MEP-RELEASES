# A longest file in MEP!

print("Please wait while we load our modules...")

import pyautogui as pgu
import threading


# ============================================================
# MEP
# Momo Explosion Project
# Macro / TAS Controller
# ============================================================

print(
  "\nHello from Yumin1004. (c) Made in Korea 2026\n"
  "MEP(Momo Explosion Project) Subprocessor ||| "
  "Version = Release 1 (Build: ALPHA SLOWY)\n"
  """
MEP is the project to Speedrun the game `Magic Cat Academy`
as TAS (Tool-assisted Speedrun) using Python.

Current speedrun record (Any%, Glitchless, Without TAS)
is 4m 34s 917ms by Voulu.
(Based on www.speedrun.com, 18 August 2026)

Mission: 4m 34s or lower

(Creator note: Help me)
"""
)


# ============================================================
# ABORT CONTROLLER
# ============================================================

class AbortController:
  def __init__(self):
    self.abort_event = threading.Event()

  def abort(self):
    """Emergency stop."""
    self.abort_event.set()

    # Release mouse button in case a gesture was interrupted.
    pgu.mouseUp()

  def reset(self):
    """Allow macros to run again."""
    self.abort_event.clear()

  def check(self):
    """Return True if an abort has been requested."""
    return self.abort_event.is_set()

  def wait(self, duration: float | int):
    """
    Wait for a duration.

    Returns:
      True  → aborted during the wait
      False → wait completed normally
    """
    return self.abort_event.wait(duration)

print(" --- Loading --- ")
# ============================================================
# DRAWER
# ============================================================

class Drawer:
  def __init__(self, abort: AbortController, deletePause: bool = False):
    self.abort = abort
    if deletePause:
      pgu.PAUSE = 0.01
    self.r = 0


  def wait(self, duration: float | int):
    """Non-blocking-to-the-controller wait."""
    return self.abort.wait(duration)

  def check_abort(self):
    """Check whether drawing should stop."""
    if self.abort.check():
      pgu.mouseUp()
      return True

    return False

  def move_to(
    self,
    x: int | float,
    y: int | float,
    duration: float | int = 0
  ):
    """
    Move mouse while respecting the abort mechanism.
    """
    if self.check_abort():
      return False

    pgu.moveTo(
      x,
      y,
      duration=duration
    )

    return not self.check_abort()

  def start(self, x, y):
    """Move to start point and press mouse."""
    if self.check_abort():
      return False

    pgu.moveTo(x, y)
    pgu.mouseDown()

    return True

  def end(self):
    """Release mouse."""
    pgu.mouseUp()

  def test_wait(self, test):
    """Wait 2 seconds when test mode is enabled."""
    if test:
      return not self.wait(2)

    return True

  # ----------------------------------------------------------
  # FROM HERE IS A SPELL DRAWER.
  #   Note: Enhance if you want. Pleasure!
  # (Be sure changing mep_background_runnder too)
  # I
  # ----------------------------------------------------------

  def i(
    self,
    sx: int,
    sy: int,
    d: int,
    dur: float | int = 0.1,
    test: bool = False
  ):
    if d <= 0:
      raise ValueError(
        "Distance cannot be negative or 0"
      )

    if not self.test_wait(test):
      return False

    if not self.start(sx, sy):
      return False

    if not self.move_to(
      sx,
      sy + d,
      duration=dur
    ):
      self.end()
      return False
    if not self.move_to(
          sx + 7,
          sy + (d*2),
          duration=dur
        ):
          self.end()
          return False

    self.end()
    return True

  # ----------------------------------------------------------
  # E / horizontal line
  # ----------------------------------------------------------

  def e(
    self,
    sx: int,
    sy: int,
    d: int,
    dur: float | int = 0.1,
    test: bool = False
  ):
    if d <= 0:
      raise ValueError(
        "Distance cannot be negative or 0"
      )

    if not self.test_wait(test):
      return False

    if not self.start(sx, sy):
      return False

    if not self.move_to(
      sx + d,
      sy,
      duration=dur
    ):
      self.end()
      return False
    if not self.move_to(
          sx + (d * 2),
          sy + 7,
          duration=dur
        ):
          self.end()
          return False

    self.end()
    return True

  # ----------------------------------------------------------
  # V
  # ----------------------------------------------------------

  def v(
    self,
    sx: int,
    sy: int,
    d: int,
    dur: float | int = 0.1,
    test: bool = False
  ):
    if d <= 0:
      raise ValueError(
        "Distance in V or Up-V function "
        "cannot be negative or 0"
      )

    if not self.test_wait(test):
      return False

    if not self.start(sx, sy):
      return False

    half = dur / 1.4

    if not self.move_to(
      sx + d,
      sy - d,
      duration=half
    ):
      self.end()
      return False

    if not self.move_to(
      sx + d * 2,
      sy + d,
      duration=half
    ):
      self.end()
      return False

    self.end()
    return True

  # ----------------------------------------------------------
  # UP-V
  # ----------------------------------------------------------

  def up_v(
    self,
    sx: int,
    sy: int,
    d: int,
    dur: float | int = 0.1,
    test: bool = False
  ):
    if d <= 0:
      raise ValueError(
        "Distance in V or Up-V function "
        "cannot be negative or 0"
      )

    if not self.test_wait(test):
      return False

    if not self.start(sx, sy):
      return False

    half = dur / 1.4

    if not self.move_to(
      sx + d,
      sy + d,
      duration=half
    ):
      self.end()
      return False

    if not self.move_to(
      sx + d * 2,
      sy - d,
      duration=half
    ):
      self.end()
      return False

    self.end()
    return True

  # ----------------------------------------------------------
  # HEART
  # ----------------------------------------------------------

  def h(
    self,
    sx: int,
    sy: int,
    dur: float | int = 0.1,
    divider: int = 1,
    test: bool = False
  ):
    if divider <= 0:
      raise ValueError(
        "Divider cannot be negative or 0"
      )

    coordinates = [
      (0, 50),
      (-30, 25),
      (-50, 0),
      (-50, -25),
      (-35, -45),
      (-15, -45),
      (0, -25),
      (15, -45),
      (35, -45),
      (50, -25),
      (50, 0),
      (30, 25),
      (0, 50)
    ]

    if not self.test_wait(test):
      return False

    first_x = sx + coordinates[0][0] // divider
    first_y = sy + coordinates[0][1] // divider

    if not self.start(first_x, first_y):
      return False

    segment_dur = dur / (len(coordinates) - 1)

    for x, y in coordinates[1:]:

      if self.check_abort():
        self.end()
        return False

      target_x = sx + x // divider
      target_y = sy + y // divider

      if not self.move_to(
        target_x,
        target_y,
        duration=segment_dur
      ):
        self.end()
        return False

    self.end()
    return True
  # ----------------------------------------------------------
  # LIGHTNING
  # ----------------------------------------------------------

  def l(
    self,
    sx: int,
    sy: int,
    dur: float | int = 0.1,
    divider: int = 1,
    test: bool = False
  ):
    if divider <= 0:
      raise ValueError(
        "Divider cannot be negative or 0"
      )

    coordinates = [
      (60, -100),
      (0, 0),
      (60, 0),
      (0, 100)
    ]

    if not self.test_wait(test):
      return False

    first_x = sx + coordinates[0][0] // divider
    first_y = sy + coordinates[0][1] // divider

    if not self.start(first_x, first_y):
      return False

    segment_dur = dur / (len(coordinates) - 1)

    for x, y in coordinates[1:]:

      if self.check_abort():
        self.end()
        return False

      target_x = sx + x // divider
      target_y = sy + y // divider

      if not self.move_to(
        target_x,
        target_y,
        duration=segment_dur
      ):
        self.end()
        return False

    self.end()
    return True

# ============================================================
# KEYBOARD MACRO
# ============================================================

class KeyboardMacro:
  def __init__(self, abort):
    self.abort = abort

  def check_abort(self):
    return self.abort.check()

  def press(
    self,
    key: str,
    duration: float | int = 0.05
  ):
    """Hold a key for a specific amount of time."""

    if self.check_abort():
      return False

    pgu.keyDown(key)

    # Wait, but wake immediately if aborted.
    if self.abort.wait(duration):
      pgu.keyUp(key)
      return False

    pgu.keyUp(key)

    return True

  def tap(self, key: str):
    """Quickly press a key."""

    if self.check_abort():
      return False

    pgu.press(key)
    return True

  def release(self, key: str):
    """Release a key safely."""
    pgu.keyUp(key)

  def sequence(
    self,
    keys: list[str],
    delay: float | int = 0.05
  ):
    """Press a sequence of keys."""

    for key in keys:

      if self.check_abort():
        return False

      if not self.tap(key):
        return False

      if self.abort.wait(delay):
        return False

    return True

# ============================================================
# MEP CONTROLLER
# ============================================================

class MEP:
  def __init__(self):
    self.abort = AbortController()

    self.drawer = Drawer(
      self.abort
    )

    self.keyboard = KeyboardMacro(
      self.abort
    )

  def start(self):
    self.abort.reset()

  def stop(self):
    self.abort.abort()

  def aborted(self):
    return self.abort.check()

class Sequencer:
  def __init__(self, mep = None):
    self.mep = mep or MEP()
    self.worker = None
    self.last_result = None
    self.last_error = None

  def play(self, sequence, delay = 0.01):
    if delay < 0:
      raise ValueError(
        "Delay cannot be negative"
      )

    if self.worker and self.worker.is_alive():
      return False

    self.mep.start()

    self.last_result = None
    self.last_error = None

    self.worker = threading.Thread(
      target=self._worker,
      args=(list(sequence), delay),
      daemon=True
    )

    self.worker.start()

    return True

  def _worker(self, sequence, delay):
    try:
      self.last_result = self._run(
        sequence,
        delay
      )

    except Exception as error:
      self.last_error = error
      self.mep.stop()
      raise

  def _run(self, sequence, delay):
    old_pause = pgu.PAUSE
    pgu.PAUSE = 0.018

    try:
      for index, command in enumerate(sequence):
        if self.mep.aborted():
          return False

        if not self._play_command(command):
          return False

        if index < len(sequence) - 1:
          if self.mep.abort.wait(delay):
            return False

      return True

    finally:
      self.mep.drawer.end()
      pgu.PAUSE = old_pause

  def _play_command(self, command):
    if self.mep.aborted():
      return False

    spell = command[0]

    if spell == "i":
      _, x, y, d = command
      if not self.mep.drawer.i(x, y, d, dur=0):
        return False

    elif spell == "e":
      _, x, y, d = command
      if not self.mep.drawer.e(x, y, d, dur=0):
        return False

    elif spell == "v":
      _, x, y, d = command
      if not self.mep.drawer.v(x, y, d, dur=0):
        return False

    elif spell == "u":
      _, x, y, d = command
      if not self.mep.drawer.up_v(x, y, d, dur=0):
        return False

    elif spell == "h":
      _, x, y = command
      if not self.mep.drawer.h(x, y, dur=0):
        return False

    elif spell == "l":
      _, x, y = command
      if not self.mep.drawer.l(x, y, dur=0):
        return False

    else:
      raise ValueError(
        f"Unknown spell: {spell}"
      )

    return True

  def wait(self):
    if self.worker:
      self.worker.join()

    if self.last_error:
      raise self.last_error

    return self.last_result

  def stop(self):
    self.mep.stop()
    self.mep.drawer.end()

if __name__ == "__main__":
  print("It seems you are currently running at the function file!\nPlease open at keyboard_control_runner.py.")
  if input("...Or run in current file [y/... ?] ").lower() == "y":
    try:
      import mep_background_runner
      mep_background_runner.main()
    except:
      print("ERROR while: Getting module and running it. Be sure mep_background_runner.py is same directory as this file.")
    else:
      print("Sucessfuly ran runner!")
    finally:
      print("FINISHED OPENING RUNNER.")
else:
  print("\nFinished Loading Modules!")
