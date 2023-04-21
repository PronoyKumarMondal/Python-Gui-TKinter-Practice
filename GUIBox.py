from tkinter import *
root = Tk()#first two line is needed for all the gui project
root.title('My Box gui')#logo title
root.iconbitmap('camera.svg')#logo add
root.geometry('500x500')#size
#showing label/printing thing
my_label= Label(root,text='Hello Deadhead!')
my_label2=Label(root,text='How are you doing today!')
#griding the message
my_label.grid(row=0,column=0)
my_label.grid(row=0,column=1)
my_label.pack()#packing /endling
my_label2.pack()
def myclick():
    my_label=Label(root,text='Welcome to DeadHead '+e.get(),fg='red').pack()#fg - foreground,bg-background ,e.get()- means getting the string we write the entrybox
    e.delete(0, END)#after clicking 1 time the value is clear
mybutton=Button(root,text='Hey click this',command=myclick,fg='white',bg='black',padx=30,pady=30)#clicking button,padx-padding sizing the button
mybutton.pack()
e=Entry(root,width=50,fg='red')#entry box
e.pack()

#radiobutton
q=IntVar()
q.get()
q.set('2')
def click(value):
    my_label3=Label(root,text=value).pack()
Radiobutton(root,text='option1',variable=q ,value=1).pack(anchor='w')
Radiobutton(root,text='option2',variable=q ,value=2).pack(anchor='w')
my_label3=Label(root,text=q.get()).pack(anchor='w')
mybutton1= Button(root,text='submit',command=lambda :click(q.get())).pack(anchor='w')


root.mainloop()




