# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from tkinter import  *
import  os
import shutil
from tkinter import messagebox
root=Tk()
def compare_file(file1,file2):
    f1 = open(file1,'r')
    f2 = open(file2,'r')
    count = 0
    diff = []
    for line1 in f1:
        line2 = f2.readline()
        count +=1
        if line1 != line2:
            diff.append(count)
    f1.close()
    f2.close()
    return diff

def allrenew():
    c2=listfile.get(0,listfile.size())
    for i in c2:
        text=str(i).split(",")
        print(str(i))
        if len(text)!=3:
            messagebox.showerror(title="error",message="格式错误")
        filepath1=text[1].strip()
        filepath2=text[2].strip()
        if os.path.isfile(filepath1) and os.path.isfile(filepath2):
            differ=compare_file(filepath1,filepath2)
            if differ==0:
                pass
            else:
                time1=os.path.getmtime(filepath1)
                time2=os.path.getmtime(filepath2)
                if time1>time2:
                    shutil.copyfile(filepath1,filepath2)
                else:
                    shutil.copyfile(filepath2,filepath1)

def renew(i):
    text = str(i).split(",")
    print(str(i))
    if len(text) != 3:
        messagebox.showerror(title="error", message="格式错误")
    filepath1 = text[1].strip()
    filepath2 = text[2].strip()
    if os.path.isfile(filepath1) and os.path.isfile(filepath2):
        differ = compare_file(filepath1, filepath2)
        if differ == 0:
            pass
        else:
            time1 = os.path.getmtime(filepath1)
            time2 = os.path.getmtime(filepath2)
            if time1 > time2:
                shutil.copyfile(filepath1, filepath2)
            else:
                shutil.copyfile(filepath2, filepath1)

def input():
    str=var.get().strip()
    listfile.insert(0,str)
    file = open("log.txt", mode='w')
    file.writelines(str)

def close():
    file = open("log.txt", mode='w')
    file.truncate()
    for t in listfile.get(0,listfile.size()):
        file.writelines(str(t).strip()+"\n")
    root.destroy()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root.geometry("717x426")
    root.protocol("WM_DELETE_WINDOW",close)
    listfile=Listbox(root,width=100,height=15)
    file=open("log.txt",mode='r')

    for t in file:
        listfile.insert(0,t)

    file.close()
    var = StringVar()
    var.set("")
    entry = Entry(root, textvariable=var,width=100)
    entry.pack()

    A=Button(root,
             text="添加",
             command=input)

    B=Button(root,
             text="删除",
             command=lambda x=listfile:x.delete(ACTIVE) )

    C=Button(root,
             text="更新所有",
             command=allrenew)

    D=Button(root,text="更新",command=lambda :renew(listfile.get(listfile.curselection())))

    sb=Scrollbar(root)
    sb.pack(side=RIGHT,fill=Y)
    sb.config(command=listfile.yview)
    listfile.pack()
    A.pack()
    B.pack()
    C.pack()
    D.pack()
    mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
