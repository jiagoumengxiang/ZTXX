'''
Created on 2012-7-6

@author: kingcc
'''
from tkinter import *
from tkinter import ttk
import AddTaskForm

root=Tk();
root.geometry('280x54-10-10');
root.resizable(FALSE,FALSE);
root.title("战拖新星");
root.overrideredirect(TRUE);
mainFrame=ttk.Frame(root);
mainFrame.grid(column=0,row=0,sticky=(N,W,E,S));


#发现敌人按钮
def AddTask():
    AddTaskForm.Show(root);
    pass;
#显示任务
def ShowTask():
    pass


modBtn=ttk.Button(mainFrame,text="谋略");
modBtn.grid(column=0,row=0);

coinLb=ttk.Label(mainFrame,text="N:0    P:0    T:0    ");
coinLb.grid(column=1,row=0);

addBtn=ttk.Button(mainFrame,text="发现敌人",command=AddTask);
addBtn.grid(column=2,row=0);

configBtn=ttk.Button(mainFrame,text="休整");
configBtn.grid(column=0,row=2);

hpLb=ttk.Label(mainFrame,text="N:0    P:0    T:0    ");
hpLb.grid(column=1,row=2);

delBtn=ttk.Button(mainFrame,text="消灭敌人");
delBtn.grid(column=2,row=2);

root.mainloop();
