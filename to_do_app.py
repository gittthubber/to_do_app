import tkinter as tk
from tkinter import ttk, messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestore di To-Do List")
        self.root.geometry("500x450")

        self.tasks = []
        self.load_tasks()

        self.create_widgets()
        self.style_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=10)

        self.label_listbox = ttk.Label(self.frame, text="Le tue attività:")
        self.label_listbox.pack()

        self.task_listbox = tk.Listbox(
            self.frame,
            width=50,
            height=15,
            bd=0,
            selectbackground="gray",
            activestyle="none",
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = ttk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry_frame = ttk.Frame(self.root)
        self.entry_frame.pack(pady=20)

        self.label_entry = ttk.Label(self.entry_frame, text="Inserisci una nuova attività:")
        self.label_entry.pack()

        self.entry = ttk.Entry(
            self.entry_frame,
            font=("Helvetica", 18),
            width=30
        )
        self.entry.pack()

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(pady=20)

        self.add_task_button = ttk.Button(
            self.button_frame,
            text="Aggiungi Attività",
            command=self.add_task,
        )
        self.add_task_button.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=5)

        self.delete_task_button = ttk.Button(
            self.button_frame,
            text="Rimuovi Attività",
            command=self.delete_task,
        )
        self.delete_task_button.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=5)

        self.save_tasks_button = ttk.Button(
            self.root,
            text="Salva Attività",
            command=self.save_tasks,
        )
        self.save_tasks_button.pack(pady=20)

        self.update_task_listbox()

    def style_widgets(self):
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        style.configure("TEntry", font=("Helvetica", 18))
        style.configure("TLabel", font=("Helvetica", 14), padding=5)
        style.configure("TFrame", padding=10)
        style.configure("TScrollbar", troughcolor="gray")

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry.delete(0, tk.END)
            self.entry.focus()  # Torna sul campo di input
        else:
            messagebox.showwarning("Attenzione", "Inserisci un'attività")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Attenzione", "Seleziona un'attività")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
        messagebox.showinfo("Informazione", "Attività salvate")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                self.tasks = f.read().splitlines()
        except FileNotFoundError:
            self.tasks = []

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
