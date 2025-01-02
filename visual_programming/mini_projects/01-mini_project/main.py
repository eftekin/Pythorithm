import tkinter as tk
from tkinter import filedialog, messagebox

import pandas as pd

# Main application window
root = tk.Tk()
root.title("Halic University - GPA & Ranking")
root.geometry("400x300")
root.resizable(False, False)
root.attributes("-fullscreen", False)

# Variables
student_data = None
entry_id = tk.Entry(root)
name_label = None
gpa_label = None
rank_label = None


# Functions
def browse_file():
    global student_data
    try:
        # Open file dialog to select an Excel file
        filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if filepath:
            # Read the Excel file into a DataFrame
            student_data = pd.read_excel(filepath)
            # GPA calculation using subject coefficients
            coefficients = {
                "Physics": 0.25,
                "Calculus": 0.25,
                "Advanced Programming": 0.30,
                "Chemistry": 0.20,
            }
            student_data["GPA"] = (
                student_data["Physics"] * coefficients["Physics"]
                + student_data["Calculus"] * coefficients["Calculus"]
                + student_data["Advanced Programming"]
                * coefficients["Advanced Programming"]
                + student_data["Chemistry"] * coefficients["Chemistry"]
            )
            # Assign ranks based on GPA, highest GPA gets rank 1
            student_data["Rank"] = student_data["GPA"].rank(ascending=False).astype(int)
            student_data.sort_values("GPA", ascending=False, inplace=True)
            student_data.reset_index(drop=True, inplace=True)
            messagebox.showinfo("Success", "File loaded successfully!")
        else:
            messagebox.showwarning("Warning", "No file selected!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load the file: {e}")


def display_info():
    if student_data is None:
        messagebox.showwarning("Warning", "Please load a file first!")
        return

    try:
        # Get student ID from input and find corresponding record
        student_id = int(entry_id.get())
        student = student_data.loc[student_data["ID"] == student_id]
        if student.empty:
            raise ValueError("Student ID not found!")

        # Display the student's name, GPA, and rank
        name_label.config(
            text=f"{student['Name'].values[0]} {student['Surname'].values[0]}"
        )
        gpa_label.config(text=f"{student['GPA'].values[0]:.2f}")
        rank_label.config(text=f"{student['Rank'].values[0]}")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def export_file():
    if student_data is None:
        messagebox.showwarning("Warning", "Please load a file first!")
        return

    try:
        # Get student ID from input and find corresponding record
        student_id = int(entry_id.get())
        student = student_data.loc[student_data["ID"] == student_id]
        if student.empty:
            raise ValueError("Student ID not found!")

        # Get the selected file format for export
        selected_format = file_format.get()
        filename = f"{student_id}_{student['Name'].values[0]}_{student['Surname'].values[0]}.{selected_format}"

        # Export to text file
        if selected_format == "txt":
            with open(filename, "w") as file:
                file.write(
                    f"Name: {student['Name'].values[0]} {student['Surname'].values[0]}\n"
                )
                file.write(f"GPA: {student['GPA'].values[0]:.2f}\n")
                file.write(f"Rank: {student['Rank'].values[0]}\n")

        # Export to Excel file, merge Name and Surname columns and select relevant columns
        elif selected_format == "xls":
            # Create a new DataFrame with merged Name and Surname columns
            student["Full Name"] = student["Name"] + " " + student["Surname"]
            student_info = student[["Full Name", "GPA", "Rank"]]
            student_info.to_excel(filename, index=False, engine="openpyxl")

        else:
            raise ValueError("Unsupported file format selected!")

        messagebox.showinfo("Success", f"File exported successfully as {filename}!")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def clear_info():
    # Clear the displayed information and input fields
    name_label.config(text="")
    gpa_label.config(text="")
    rank_label.config(text="")
    entry_id.delete(0, tk.END)


# GUI Layout
tk.Label(root, text="Student GPA and Ranking", font=("Arial", 14, "bold")).grid(
    row=0, column=0, columnspan=2, pady=10
)

tk.Label(root, text="Open file:", font=("Arial", 12)).grid(
    row=1, column=0, sticky="w", padx=10, pady=5
)
tk.Button(root, text="Browse", command=browse_file).grid(
    row=1, column=1, sticky="w", padx=10
)

tk.Label(root, text="ID:", font=("Arial", 12)).grid(
    row=2, column=0, sticky="w", padx=10, pady=5
)
entry_id.grid(row=2, column=1, sticky="w", padx=10, pady=5)

tk.Label(root, text="Name Surname:", font=("Arial", 12)).grid(
    row=3, column=0, sticky="w", padx=10, pady=5
)
name_label = tk.Label(root, text="", anchor="w", width=30)
name_label.grid(row=3, column=1, sticky="w", padx=10, pady=5)

tk.Label(root, text="GPA:", font=("Arial", 12)).grid(
    row=4, column=0, sticky="w", padx=10, pady=5
)
gpa_label = tk.Label(root, text="", anchor="w", width=30)
gpa_label.grid(row=4, column=1, sticky="w", padx=10, pady=5)

tk.Label(root, text="Rank:", font=("Arial", 12)).grid(
    row=5, column=0, sticky="w", padx=10, pady=5
)
rank_label = tk.Label(root, text="", anchor="w", width=30)
rank_label.grid(row=5, column=1, sticky="w", padx=10, pady=5)

tk.Label(root, text="Please select file type:", font=("Arial", 12)).grid(
    row=6, column=0, sticky="w", padx=10, pady=5
)
file_format = tk.StringVar(value="txt")
file_type_combobox = tk.OptionMenu(root, file_format, "txt", "xls")
file_type_combobox.grid(row=6, column=1, sticky="w", padx=10, pady=5)

# Frame for buttons to align them closer
button_frame = tk.Frame(root)
button_frame.grid(row=7, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Display", command=display_info).grid(
    row=0, column=0, padx=5
)
tk.Button(button_frame, text="Export", command=export_file).grid(
    row=0, column=1, padx=5
)
tk.Button(button_frame, text="Clear", command=clear_info).grid(row=0, column=2, padx=5)

# Run the application
root.mainloop()
