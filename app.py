import instaloader
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox


win = tk.Tk()
win.title("Best instagram Image Downloader")

def imgDownload():
  ig = instaloader.Instaloader()
  profile = entry.get()
  ig.download_profile(profile, profile_pic_only=True)
  messagebox.showinfo("status", "image Downloaded seccessfully")

img = Image.open("ig.jpg")
img = img.resize((200, 150), Image.ANTIALIAS)
resized_img = ImageTk.PhotoImage(img)

title = tk.Label(win, text="instagram Image Downloader",
  font=("times", 24, "bold"))

title.grid(row=0, column=0, columnspan=5, padx=30, pady=10)

image = tk.Label(win, image=resized_img)
image.grid(row=2, column=0, columnspan=5, pady=20)

label1 = tk.Label(win, text="enter username:", font=("Arial", 16))
label1.grid(row=3, column=0)

entry = tk.Entry(win, width=50)
entry.grid(row=3, column=1, columnspan=3)

btn = tk.Button(win, text="Download", command=imgDownload)
btn.grid(row=4, column=0, columnspan=5, pady=10)

win.mainloop()