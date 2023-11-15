import tkinter as tk
import win32gui
import win32con
from tkinter import messagebox
from ctypes import windll
import datetime

root = tk.Tk()
root.title("我的代办")
root.geometry("400x500")
root.overrideredirect(False)  # 隐藏窗口边框
root.attributes("-alpha", 0.8)  # 设置窗口透明度

def add_task():
    task = entry.get() + '    ' +str(datetime.datetime.now())[:19]
    if task:
        listbox.insert(tk.END, task)
        save_tasks(True)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("警告", "请输入任务！")

def delete_task():
    try:
        index = listbox.curselection()[0]
        save_tasks(True)
        listbox.delete(index)
    except IndexError:
        pass

def clear_tasks():
    listbox.delete(0, tk.END)

def save_tasks(not_show=False):
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    if not_show == False:
        messagebox.showinfo("提示", "任务已保存！")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def set_window_topmost():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

def set_window_top_not_most():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

def set_window_not_top():
    root.after(100, set_window_top_not_most)  # 设置窗口置顶

def set_window_top():
    root.after(100, set_window_topmost)  # 设置窗口置顶

def hide_tabbar_icon():
    hwnd = win32gui.GetForegroundWindow()

    # 获取窗口扩展样式
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)

    # 隐藏任务栏图标
    style |= win32con.WS_EX_TOOLWINDOW
    style &= ~win32con.WS_EX_APPWINDOW

    # 更新窗口扩展样式
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, style)

    # 刷新窗口
    win32gui.SetWindowPos(hwnd, -1, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOSIZE)

def reset_window(root):
    # 销毁当前窗口
    root.destroy()

    # 在新窗口中添加组件和设置样式
    root = tk.Tk()
    root.title("我的代办")
    root.geometry("400x500")
    root.overrideredirect(False)  # 隐藏窗口边框
    root.attributes("-alpha", 0.8)  # 设置窗口透明度


    frame = tk.Frame(root)
    frame.pack(pady=20)

    listbox = tk.Listbox(frame, width=40, height=10)
    listbox = tk.Listbox(frame, width=40, height=10)

    # 设置Listbox的背景颜色
    listbox.configure(bg='lightgray')

    # 设置Listbox中选项的样式
    listbox.configure(font=('Arial', 15))

    # 设置Listbox的边框样式
    listbox.configure(borderwidth=2, relief=tk.SOLID)

    # 设置Listbox的滚动条样式
    scrollbar = tk.Scrollbar(frame, command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox.pack(side=tk.LEFT, fill=tk.BOTH)
    listbox.configure(yscrollcommand=scrollbar.set)


    entry = tk.Entry(root, font=("Helvetica", 12))
    entry.pack(pady=20)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    add_button = tk.Button(button_frame, text="添加任务", command=add_task)
    add_button.grid(row=0, column=0)

    delete_button = tk.Button(button_frame, text="删除任务", command=delete_task)
    delete_button.grid(row=0, column=1)

    clear_button = tk.Button(button_frame, text="清空任务", command=clear_tasks)
    clear_button.grid(row=0, column=2)

    button_frame2 = tk.Frame(root)
    button_frame2.pack(pady=20)

    save_button = tk.Button(button_frame2, text="保存任务", command=save_tasks)
    save_button.grid(row=1, column=0)

    load_button = tk.Button(button_frame2, text="加载任务", command=load_tasks)
    load_button.grid(row=1, column=1)

    up_button = tk.Button(button_frame2, text= "置顶",command = set_window_top)
    up_button.grid(row=1, column=2)

    up_button = tk.Button(button_frame2, text= "取消置顶",command = set_window_not_top)
    up_button.grid(row=1, column=3)

    up_button = tk.Button(button_frame2, text= "隐藏桌面图标",command = hide_tabbar_icon)
    up_button.grid(row=1, column=4)

    load_tasks()



frame = tk.Frame(root)
frame.pack(pady=20)

listbox = tk.Listbox(frame, width=40, height=10)
listbox = tk.Listbox(frame, width=40, height=10)

# 设置Listbox的背景颜色
listbox.configure(bg='lightgray')

# 设置Listbox中选项的样式
listbox.configure(font=('Arial', 15))

# 设置Listbox的边框样式
listbox.configure(borderwidth=2, relief=tk.SOLID)

# 设置Listbox的滚动条样式
scrollbar = tk.Scrollbar(frame, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.pack(side=tk.LEFT, fill=tk.BOTH)
listbox.configure(yscrollcommand=scrollbar.set)


entry = tk.Entry(root, font=("Helvetica", 12))
entry.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

add_button = tk.Button(button_frame, text="添加任务", command=add_task)
add_button.grid(row=0, column=0)

delete_button = tk.Button(button_frame, text="删除任务", command=delete_task)
delete_button.grid(row=0, column=1)

clear_button = tk.Button(button_frame, text="清空任务", command=clear_tasks)
clear_button.grid(row=0, column=2)

button_frame2 = tk.Frame(root)
button_frame2.pack(pady=20)

save_button = tk.Button(button_frame2, text="保存任务", command=save_tasks)
save_button.grid(row=1, column=0)

load_button = tk.Button(button_frame2, text="加载任务", command=load_tasks)
load_button.grid(row=1, column=1)

up_button = tk.Button(button_frame2, text= "隐藏桌面图标",command = hide_tabbar_icon)
up_button.grid(row=1, column=2)

load_tasks()



root.mainloop()
