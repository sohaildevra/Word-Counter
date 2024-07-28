import tkinter as tk
from tkinter import scrolledtext

def get_text(root,labelword):
   text = scrolled_text.get("1.0", tk.END)
   words=0
   if text!="":
      for i in range(0,len(text)):
         if text[i].isspace() and text[i-1].isspace()==False:
            words+=1
   labelword.config(text = f"Words: {words}")   

root = tk.Tk()
root.geometry("720x300")
root.resizable(False,False)
root.title("Retrieving Text from a ScrolledText Widget in Tkinter ")

label = tk.Label(root,text="Enter the String", font=("Arial",20),fg="green")
label.pack()

scrolled_text = scrolledtext.ScrolledText(root, width=40, height=10)
scrolled_text.pack()

labelword = tk.Label(root,text="", font=("Arial",20))
labelword.pack()

button = tk.Button(root, text="Get Text", font=("Arial",20),fg="green", command=lambda: get_text(root,labelword))
button.pack()

root.mainloop()
