import tkinter as tk
window=tk.Tk()
def click():
    print("Hello cse7 students")
button=tk.Button(window,text="click me",command="click me")
button.pack()
window.mainloop()
