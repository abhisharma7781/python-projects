import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Function to add task
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete selected task
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Entry widget to enter tasks
entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=10)

# Add Task button
button_add_task = tk.Button(root, text="Add Task", width=20, command=add_task)
button_add_task.pack(pady=10)

# Listbox to display tasks
listbox_tasks = tk.Listbox(root, width=30, height=10)
listbox_tasks.pack(pady=10)

# Delete Task button
button_delete_task = tk.Button(root, text="Delete Task", width=20, command=delete_task)
button_delete_task.pack(pady=10)

# Run the application
root.mainloop()
