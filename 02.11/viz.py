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
 background = "red"
 )
label.pack()
label1.pack()

window.mainloop()