import tkinter

window = tkinter.Tk()

window.title("I am Window")
window.geometry("640x400+100+100")
window.resizable(False, False)

count = 0
def count_up():
    global count
    count += 1
    label.config(text=str(count))

label=tkinter.Label(window, text="0", width=10, height=5, fg="red", relief="solid")
label.pack()

button = tkinter.Button(window, overrelief="solid", width = 15, command=count_up, repeatdelay=10000, repeatinterval=100)
button.pack()

window.mainloop()