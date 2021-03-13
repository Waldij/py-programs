from tkinter import *
root = Tk()

def Hello():
	print("Hello")

btn = Button(root,                  
             text="Click me",       
             width=30,height=5,     
             bg="white",fg="black")

btn.bind("<Button-1>", Hello)
btn.pack() 
root.mainloop()