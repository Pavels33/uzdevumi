import tkinter as tk

window = tk.Tk()

label = tk.Label(
 text = "Sveiki! Sveiki! Sveiki!",
 foreground = "white",
 background = "green"
 )
label1 = tk.Label(
  text = "hey hey",
 foreground = "blue",
 background = "red",
 width = 12,
 height = 15
 )
label.pack()
label1.pack()

window.mainloop()