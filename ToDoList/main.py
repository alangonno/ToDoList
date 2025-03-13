import tkinter as tk
def remove(a, b, c):
        a.destroy()
        b.destroy()
        c.destroy()
        
def new_to_do():
        text = box.get()
        
        if text.strip():
                task_frame = tk.Frame(root)
                task_frame.pack(anchor='w', padx=20, pady=5)

                activie = tk.Label(task_frame, text=text, font=('Arial', 10))
                activie.pack(side='left')

                do = tk.Button(task_frame, text='Finished', command=lambda:remove(do, activie, task_frame))
                do.pack(side='right', padx=50)



root = tk.Tk()
root.geometry('700x700')

maintext = tk.Label(root, text='To Do List', font=('Arial Black', 30))
maintext.pack(padx=20, pady=20)

box = tk.Entry(root, width=100)
box.pack()

send = tk.Button(root, text='Send', command=new_to_do, width=10, height=1)
send.pack(padx=20, pady=10)

root.mainloop()