import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from tkinter.constants import *
from tkinter import messagebox
import json
from tkinter.scrolledtext import ScrolledText

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.title('To-Do List')
root.geometry('520x440+520+100')
root.resizable(width=False, height=False)
icon = ImageTk.PhotoImage(file='Mans icon.png')
root.iconphoto(False, icon)



JSON_FILE = "tasks.json"

def load_tasks():
    try:
        with open(JSON_FILE, "r") as f:
            global tasks
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
        view_task()
    return tasks


def save_tasks(tasks):
    '''
    This function opens a file in write mode.
    :param tasks: name of file to be written
    :return:
    '''
    with open(JSON_FILE, "w") as f:
        json.dump(tasks, f, indent=3)

def edit_task():
    selected_index = task_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        description = description_entry.get()
        due_date = due_date_entry.get()
        priority = priority_entry.get()

        if description != "" and due_date != "":
            tasks = load_tasks()
            tasks[selected_index]["description"] = description
            tasks[selected_index]["due_date"] = due_date
            tasks[selected_index]["priority"] = priority
            save_tasks(tasks)
            view_task()

            description_entry.delete(0, "end")
            due_date_entry.delete(0, "end")
            priority_entry.delete(0, "end")
        else:
            messagebox.showwarning("Fill the all details.")
    else:
        messagebox.showerror("Error")

def add_task():
    '''
    This function takes user input from user then adds to the list box and save the tasks to json file [tasks].
     It first checks if there is data entered in the list box. If no data is entered it returns a warning.
    :return:
    '''
    description = description_entry.get()
    due_date = due_date_entry.get()
    priority = priority_entry.get()
    if description != "" and due_date != "":

        task = {"description": description,
                "due_date": due_date,
                "priority": priority}


        task_list.insert(END, f"{task['description']} - Due Date: {task['due_date']} - Priority: {task['priority']}")
        description_entry.delete(0, "end")
        due_date_entry.delete(0, "end")
        priority_entry.delete(0, "end")
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
    else:
        messagebox.showwarning("warning", "Please fill in all details.")


def deleteTask():
    '''
    This function deletes takes highlited by the cursor if no selection it returns an index error
    :return:
    '''
    try:
        selected_index = task_list.curselection()[0]
        task_list.delete(selected_index)
        tasks = load_tasks()
        tasks.pop(selected_index)
        save_tasks(tasks)
    except IndexError:
        pass


def view_task():
    # clear the task_list widget
    task_list.delete(0, "end")


    tasks = load_tasks()
    for task in tasks:
        task_list.insert(tk.END,
                         f"{task['description']} - Due Date: {task['due_date']} - Priority: {task['priority']}")

tasks = load_tasks()
def search():
    # clear the task_list widget
    task_list.delete(0, "end")

    tasks = load_tasks()
    search_text = description_entry.get()
    for task in tasks:
        if task["description"] == search_text:
            task_list.insert(tk.END, f"{task['description']} - Due Date: {task['due_date']} - Priority: {task['priority']}")


def completed():
    try:
        complete=task_list.curselection()
        temp=complete[0]
        #store the text of selected item in a string
        temp_marked=task_list.get(complete)
        #update it
        temp_marked=temp_marked+" ✔"
        #delete it then insert it
        task_list.delete(temp)
        task_list.insert(temp,temp_marked)
    except IndexError:
        messagebox.showerror("Error", "No task selected")


# add a frame for our widgets
widget_frame = customtkinter.CTkFrame(root, corner_radius=10, width=510)
widget_frame.pack(pady=10, padx=10)

# resize the logo and display the logo on the frame.
group7_img = Image.open('group07.png')
resized = group7_img.resize((180, 160), Image.Resampling.LANCZOS)
group7_logo = ImageTk.PhotoImage(resized)
group7_label = tk.Label(widget_frame, image=group7_logo, bg='#222222')
group7_label.grid(row=0, rowspan=2, column=2)

# User input entry boxes and labels
description_label = customtkinter.CTkLabel(widget_frame, corner_radius=10, text='Description')
description_label.grid(row=0, column=0, padx=10, pady=10)

description_entry = customtkinter.CTkEntry(widget_frame, width=210, placeholder_text='Enter task', border_width=1)
description_entry.grid(row=0, column=1)

due_date_label = customtkinter.CTkLabel(widget_frame, corner_radius=10, text='Due Date')
due_date_label.grid(row=1, column=0, padx=10, pady=10)

due_date_entry = customtkinter.CTkEntry(widget_frame, width=210, placeholder_text='DD/MM/YYYY', border_width=1)
due_date_entry.grid(row=1, column=1, padx=10,pady=10)

priority_label = customtkinter.CTkLabel(widget_frame, corner_radius=10, text='Priority')
priority_label.grid(row=2, column=0, padx=10, pady=10)

priority_entry = customtkinter.CTkEntry(widget_frame, width=210, placeholder_text='High-Medium-Low', border_width=1)
priority_entry.grid(row=2, column=1, padx=10, pady=10)

# buttons to select operation
add_button = customtkinter.CTkButton(widget_frame, text='Add Task', command=add_task)
add_button.grid(row=2, column=2, padx=10, pady=10)

edit_button = customtkinter.CTkButton(widget_frame, text='Edit Task', command=lambda: save_tasks(tasks))
edit_button.grid(row=3, column=2, padx=10, pady=10)

view_button = customtkinter.CTkButton(widget_frame, text= 'View All Tasks', command=lambda: view_task())
view_button.grid(row=4, column=2, padx=10, pady=10)

complete_button = customtkinter.CTkButton(widget_frame, text= 'Complete', command=lambda: completed())
complete_button.grid(row=5, column=2, padx=10, pady=10)

delete_button = customtkinter.CTkButton(widget_frame, text= 'Delete Task', command=deleteTask)
delete_button.grid(row=6, column=2, padx=15, pady=10)

search_button = customtkinter.CTkButton(widget_frame, text='Search Task', command=search)
search_button.grid(row=7, column=2, padx=15, pady=10)

edit_button = customtkinter.CTkButton(widget_frame, text='Edit Task', command=edit_task)
edit_button.grid(row=3, column=2, padx=10, pady=10)

# listbox to display tasks
task_list = tk.Listbox(widget_frame, height=17, bg='#222222', fg='silver',
                       width=65,
                       borderwidth=1,
                       bd=0,
                       relief=SUNKEN,
                       highlightthickness=0,
                       selectbackground='#222222',
                       activestyle='none',
                       selectmode=MULTIPLE)
task_list.place(x=10, y=250)
text_scroll = tk.Scrollbar(task_list, borderwidth=1, activebackground='#222222')
text_scroll.place(x=370, height=263)

# configure the scrollbar to scroll the text widget
text_scroll.config(command=task_list.yview)



root.mainloop()