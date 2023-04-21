from tkinter import *
root = Tk()#first two line is needed for all the gui project
root.title('My Menu app')#logo title
root.iconbitmap('camera.svg')#logo add
root.geometry('500x500')#size

product=[
    ('Microsoft surface','Microsoft surface'),
    ('pixel','pixel'),
    ('asus rog','asus rog'),
    ('Macbook pro','Macbook pro'),
    ('Hp probook','Hp probook'),
    ('Lenovo','Lenovo')
]
choice = StringVar()
choice.set('Microsoft surface')
for text,mode in product:
    Radiobutton(root,text=text,variable=choice,value=mode).pack(anchor='w')

def click(value):
    my_label= Label(root,text=value).pack()

my_button=Button(root,text='Buy Now!',command=lambda :click(choice.get())).pack()
root.mainloop()