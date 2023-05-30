import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
from get_fb_posts import get_fb_posts


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    input_file_var.set(file_path)

def save_file_dialog():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                             filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    return file_path


def update_progress(value):
    progress_bar["value"] = value
    root.update_idletasks()

def run_function():
    input_file = input_file_var.get()
    username = username_var.get()
    password = password_var.get()
    param1 = int(param1_var.get())
    param2 = int(param2_var.get())

    input_data = pd.read_excel(input_file)
    
    def float_to_int(x):
        if isinstance(x, float):
            return int(x)
        return x
    
    input_data['id'] = input_data['id'].apply(float_to_int)
    input_strings = input_data['id'].astype(str).tolist()
    
    if username and password:
        cred = (username, password)
    else:
        cred = ("","")

    sorted_df = get_fb_posts(input_strings, param1, param2, cred, progress_callback=update_progress)

    # Call the save_file_dialog function to get the file path
    full_file_path = save_file_dialog()

    # Check if a file path was provided (the user didn't cancel the dialog)
    if full_file_path:
        # Save the DataFrame to the selected file path
        sorted_df.to_excel(full_file_path, index=False, engine='openpyxl')
        # Show a pop-up message that the process is complete
        messagebox.showinfo("Process Complete","File Created Successfully!")
    else:
        print("File save was canceled.")


root = tk.Tk()
root.title("Fetch Facebook Posts")

input_file_var = tk.StringVar()
username_var = tk.StringVar()
password_var = tk.StringVar()
param1_var = tk.IntVar()
param2_var = tk.IntVar()

tk.Label(root, text="Input File:").grid(row=0, column=0, sticky=tk.W)
tk.Entry(root, textvariable=input_file_var, width=50).grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2)

# Username input field
tk.Label(root, text="Username:").grid(row=1, column=0, sticky=tk.W)
tk.Entry(root, textvariable=username_var).grid(row=1, column=1)

# Password input field
tk.Label(root, text="Password:").grid(row=2, column=0, sticky=tk.W)
tk.Entry(root, textvariable=password_var, show="*").grid(row=2, column=1)

tk.Label(root, text="Pages to Scroll Through:").grid(row=3, column=0, sticky=tk.W)
tk.Entry(root, textvariable=param1_var).grid(row=3, column=1)

tk.Label(root, text="Posts per Scroll:").grid(row=4, column=0, sticky=tk.W)
tk.Entry(root, textvariable=param2_var).grid(row=4, column=1)

tk.Button(root, text="Generate File", command=run_function).grid(row=5, column=1)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.grid(row=6, column=1, pady=10)


root.mainloop()