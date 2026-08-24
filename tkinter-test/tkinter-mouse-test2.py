# Origin tkinter file from tkinter-mouse-test3.py

import tkinter as tk
import time


class MouseTester:
  def __init__(self, root):
    self.root = root

    self.mouse_x = 0
    self.mouse_y = 0
    self.dragging = False

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

  def log_event(self, text):
    timestamp = time.perf_counter()
    self.log.insert(
      tk.END,
      f"{timestamp:.6f}  {text}\n"
    )
    self.log.see(tk.END)

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

  def press(self, event):
    self.dragging = True

    self.state_label.config(
      text="State: LEFT BUTTON DOWN"
    )

    self.log_event(
      f"CLICK DOWN   window=({event.x}, {event.y})"
    )

  def release(self, event):
    self.dragging = False

    self.state_label.config(
      text="State: LEFT BUTTON RELEASED"
    )

    self.log_event(
      f"CLICK UP     window=({event.x}, {event.y})"
    )

  def drag(self, event):
    self.mouse_x = event.x
    self.mouse_y = event.y

    self.position_label.config(
      text=f"Mouse: ({event.x}, {event.y})"
    )

    self.state_label.config(
      text="State: DRAGGING"
    )

    self.log_event(
      f"DRAG         window=({event.x}, {event.y})"
    )


root = tk.Tk()
root.title("Mouse Input Laboratory")
root.geometry("850x700")

app = MouseTester(root)

root.mainloop()