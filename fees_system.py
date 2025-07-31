import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# --- 1. Database Manager Class ---
class DatabaseManager:
    def __init__(self, db_name="fees_management.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        # Students Table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                standard TEXT,
                contact_number TEXT,
                email TEXT
            )
        ''')
        # Courses Table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT NOT NULL UNIQUE,
                fees REAL NOT NULL
            )
        ''')
        # Payments Table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                course_id INTEGER,
                amount_paid REAL NOT NULL,
                payment_date TEXT NOT NULL,
                due_date TEXT,
                status TEXT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students(student_id),
                FOREIGN KEY (course_id) REFERENCES courses(course_id)
            )
        ''')
        self.conn.commit()

    # --- Student Operations ---
    def add_student(self, name, standard, contact_number, email):
        try:
            self.cursor.execute("INSERT INTO students (name, standard, contact_number, email) VALUES (?, ?, ?, ?)",
                                (name, standard, contact_number, email))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error adding student: {e}")
            return False

    def get_all_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def get_student_by_id(self, student_id):
        self.cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
        return self.cursor.fetchone()

    def update_student(self, student_id, name, standard, contact_number, email):
        try:
            self.cursor.execute("UPDATE students SET name=?, standard=?, contact_number=?, email=? WHERE student_id=?",
                                (name, standard, contact_number, email, student_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error updating student: {e}")
            return False

    def delete_student(self, student_id):
        try:
            # Also delete related payments to maintain data integrity
            self.cursor.execute("DELETE FROM payments WHERE student_id=?", (student_id,))
            self.cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error deleting student: {e}")
            return False

    # --- Course Operations ---
    def add_course(self, course_name, fees):
        try:
            self.cursor.execute("INSERT INTO courses (course_name, fees) VALUES (?, ?)", (course_name, fees))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            messagebox.showwarning("Duplicate Entry", "Course with this name already exists.")
            return False
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error adding course: {e}")
            return False

    def get_all_courses(self):
        self.cursor.execute("SELECT * FROM courses")
        return self.cursor.fetchall()

    def get_course_by_id(self, course_id):
        self.cursor.execute("SELECT * FROM courses WHERE course_id=?", (course_id,))
        return self.cursor.fetchone()

    def update_course(self, course_id, course_name, fees):
        try:
            self.cursor.execute("UPDATE courses SET course_name=?, fees=? WHERE course_id=?",
                                (course_name, fees, course_id))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            messagebox.showwarning("Duplicate Entry", "Course with this name already exists.")
            return False
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error updating course: {e}")
            return False

    def delete_course(self, course_id):
        try:
            # Prevent deletion if there are payments associated with this course
            self.cursor.execute("SELECT COUNT(*) FROM payments WHERE course_id=?", (course_id,))
            if self.cursor.fetchone()[0] > 0:
                messagebox.showwarning("Deletion Blocked", "Cannot delete course with existing payments.")
                return False

            self.cursor.execute("DELETE FROM courses WHERE course_id=?", (course_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error deleting course: {e}")
            return False

    # --- Payment Operations ---
    def record_payment(self, student_id, course_id, amount_paid, payment_date, due_date, status):
        try:
            self.cursor.execute("INSERT INTO payments (student_id, course_id, amount_paid, payment_date, due_date, status) VALUES (?, ?, ?, ?, ?, ?)",
                                (student_id, course_id, amount_paid, payment_date, due_date, status))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error recording payment: {e}")
            return False

    def get_payments_by_student(self, student_id):
        self.cursor.execute("""
            SELECT p.payment_id, s.name, c.course_name, p.amount_paid, p.payment_date, p.due_date, p.status
            FROM payments p
            JOIN students s ON p.student_id = s.student_id
            JOIN courses c ON p.course_id = c.course_id
            WHERE p.student_id = ?
        """, (student_id,))
        return self.cursor.fetchall()

    def get_all_payments(self):
        self.cursor.execute("""
            SELECT p.payment_id, s.name, c.course_name, p.amount_paid, p.payment_date, p.due_date, p.status
            FROM payments p
            JOIN students s ON p.student_id = s.student_id
            JOIN courses c ON p.course_id = c.course_id
        """)
        return self.cursor.fetchall()

    def update_payment(self, payment_id, student_id, course_id, amount_paid, payment_date, due_date, status):
        try:
            self.cursor.execute("UPDATE payments SET student_id=?, course_id=?, amount_paid=?, payment_date=?, due_date=?, status=? WHERE payment_id=?",
                                (student_id, course_id, amount_paid, payment_date, due_date, status, payment_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error updating payment: {e}")
            return False

    def delete_payment(self, payment_id):
        try:
            self.cursor.execute("DELETE FROM payments WHERE payment_id=?", (payment_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error deleting payment: {e}")
            return False

    # --- Reporting ---
    def get_total_fees_collected(self):
        self.cursor.execute("SELECT SUM(amount_paid) FROM payments")
        return self.cursor.fetchone()[0] or 0.0

    def get_outstanding_fees(self):
        # This is a bit more complex, requires calculating for each student/course combination
        # For simplicity, let's assume it's the sum of fees for courses that are "Due"
        # A more robust calculation would involve total course fees - total paid
        self.cursor.execute("""
            SELECT SUM(c.fees - IFNULL((SELECT SUM(p.amount_paid) FROM payments p WHERE p.student_id = s.student_id AND p.course_id = c.course_id), 0))
            FROM students s
            JOIN courses c ON 1
            WHERE c.fees > IFNULL((SELECT SUM(p.amount_paid) FROM payments p WHERE p.student_id = s.student_id AND p.course_id = c.course_id), 0)
        """)
        return self.cursor.fetchone()[0] or 0.0

    def close(self):
        self.conn.close()

# --- 2. GUI Application Class ---
class FeesManagementApp:
    def __init__(self, master):
        self.master = master
        master.title("Fees Management System")
        master.geometry("1200x700")

        self.db = DatabaseManager()

        # Create Notebook (tabs)
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Tabs
        self.student_tab = ttk.Frame(self.notebook)
        self.course_tab = ttk.Frame(self.notebook)
        self.payment_tab = ttk.Frame(self.notebook)
        self.report_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.student_tab, text="Students")
        self.notebook.add(self.course_tab, text="Courses")
        self.notebook.add(self.payment_tab, text="Payments")
        self.notebook.add(self.report_tab, text="Reports")

        self._setup_student_tab()
        self._setup_course_tab()
        self._setup_payment_tab()
        self._setup_report_tab()

        # Load initial data
        self._load_students_into_treeview()
        self._load_courses_into_treeview()
        self._load_payments_into_treeview()

    def _setup_student_tab(self):
        # Input Frame
        input_frame = ttk.LabelFrame(self.student_tab, text="Student Details", padding="10")
        input_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(input_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.student_id_entry = ttk.Entry(input_frame, state='readonly') # Read-only for display
        self.student_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(input_frame, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.student_name_entry = ttk.Entry(input_frame)
        self.student_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(input_frame, text="Standard:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.student_standard_entry = ttk.Entry(input_frame)
        self.student_standard_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(input_frame, text="Contact:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.student_contact_entry = ttk.Entry(input_frame)
        self.student_contact_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(input_frame, text="Email:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.student_email_entry = ttk.Entry(input_frame)
        self.student_email_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        input_frame.columnconfigure(1, weight=1) # Allow entry fields to expand

        # Buttons
        button_frame = ttk.LabelFrame(self.student_tab, text="Actions", padding="10")
        button_frame.pack(padx=10, pady=5, fill="x")

        ttk.Button(button_frame, text="Add Student", command=self._add_student).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(button_frame, text="Update Student", command=self._update_student).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(button_frame, text="Delete Student", command=self._delete_student).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(button_frame, text="Clear Fields", command=self._clear_student_fields).grid(row=0, column=3, padx=5, pady=5)

        # Treeview for displaying students
        self.student_tree = ttk.Treeview(self.student_tab, columns=("ID", "Name", "Standard", "Contact", "Email"), show="headings")
        self.student_tree.heading("ID", text="ID")
        self.student_tree.heading("Name", text="Name")
        self.student_tree.heading("Standard", text="Standard")
        self.student_tree.heading("Contact", text="Contact")
        self.student_tree.heading("Email", text="Email")

        self.student_tree.column("ID", width=50, anchor="center")
        self.student_tree.column("Name", width=150)
        self.student_tree.column("Standard", width=100)
        self.student_tree.column("Contact", width=100)
        self.student_tree.column("Email", width=200)

        self.student_tree.pack(padx=10, pady=10, expand=True, fill="both")
        self.student_tree.bind("<ButtonRelease-1>", self._on_student_select)

        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(self.student_tree, orient="vertical", command=self.student_tree.yview)
        self.student_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def _load_students_into_treeview(self):
        for item in self.student_tree.get_children():
            self.student_tree.delete(item)
        students = self.db.get_all_students()
        for student in students:
            self.student_tree.insert("", "end", values=student)

    def _add_student(self):
        name = self.student_name_entry.get().strip()
        standard = self.student_standard_entry.get().strip()
        contact = self.student_contact_entry.get().strip()
        email = self.student_email_entry.get().strip()

        if not name:
            messagebox.showwarning("Input Error", "Student Name is required.")
            return

        if self.db.add_student(name, standard, contact, email):
            messagebox.showinfo("Success", "Student added successfully.")
            self._clear_student_fields()
            self._load_students_into_treeview()
            self._update_payment_student_dropdown() # Update student dropdown in payments tab

    def _update_student(self):
        student_id_str = self.student_id_entry.get().strip()
        if not student_id_str:
            messagebox.showwarning("Selection Error", "Please select a student to update.")
            return
        try:
            student_id = int(student_id_str)
        except ValueError:
            messagebox.showerror("Invalid Input", "Invalid Student ID.")
            return

        name = self.student_name_entry.get().strip()
        standard = self.student_standard_entry.get().strip()
        contact = self.student_contact_entry.get().strip()
        email = self.student_email_entry.get().strip()

        if not name:
            messagebox.showwarning("Input Error", "Student Name is required.")
            return

        if self.db.update_student(student_id, name, standard, contact, email):
            messagebox.showinfo("Success", "Student updated successfully.")
            self._clear_student_fields()
            self._load_students_into_treeview()
            self._update_payment_student_dropdown()

    def _delete_student(self):
        selected_item = self.student_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a student to delete.")
            return

        student_id = self.student_tree.item(selected_item, 'values')[0]

        if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete student ID {student_id}? This will also delete all associated payments."):
            if self.db.delete_student(student_id):
                messagebox.showinfo("Success", "Student deleted successfully.")
                self._clear_student_fields()
                self._load_students_into_treeview()
                self._load_payments_into_treeview() # Payments might have been deleted
                self._update_payment_student_dropdown()

    def _on_student_select(self, event):
        selected_item = self.student_tree.selection()
        if selected_item:
            values = self.student_tree.item(selected_item, 'values')
            self.student_id_entry.config(state='normal')
            self.student_id_entry.delete(0, tk.END)
            self.student_id_entry.insert(0, values[0])
            self.student_id_entry.config(state='readonly')

            self.student_name_entry.delete(0, tk.END)
            self.student_name_entry.insert(0, values[1])

            self.student_standard_entry.delete(0, tk.END)
            self.student_standard_entry.insert(0, values[2])

            self.student_contact_entry.delete(0, tk.END)
            self.student_contact_entry.insert(0, values[3])

            self.student_email_entry.delete(0, tk.END)
            self.student_email_entry.insert(0, values[4])
        else:
            self._clear_student_fields()

    def _clear_student_fields(self):
        self.student_id_entry.config(state='normal')
        self.student_id_entry.delete(0, tk.END)
        self.student_id_entry.config(state='readonly')
        self.student_name_entry.delete(0, tk.END)
        self.student_standard_entry.delete(0, tk.END)
        self.student_contact_entry.delete(0, tk.END)
        self.student_email_entry.delete(0, tk.END)
        self.student_tree.selection_remove(self.student_tree.selection()) # Deselect

    # --- Course Tab Functions ---
    def _setup_course_tab(self):
        input_frame = ttk.LabelFrame(self.course_tab, text="Course Details", padding="10")
        input_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(input_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.course_id_entry = ttk.Entry(input_frame, state='readonly')
        self.course_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(input_frame, text="Course Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.course_name_entry = ttk.Entry(input_frame)
        self.course_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(input_frame, text="Fees:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.course_fees_entry = ttk.Entry(input_frame)
        self.course_fees_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        input_frame.columnconfigure(1, weight=1)

        button_frame = ttk.LabelFrame(self.course_tab, text="Actions", padding="10")
        button_frame.pack(padx=10, pady=5, fill="x")

        ttk.Button(button_frame, text="Add Course", command=self._add_course).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(button_frame, text="Update Course", command=self._update_course).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(button_frame, text="Delete Course", command=self._delete_course).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(button_frame, text="Clear Fields", command=self._clear_course_fields).grid(row=0, column=3, padx=5, pady=5)

        self.course_tree = ttk.Treeview(self.course_tab, columns=("ID", "Name", "Fees"), show="headings")
        self.course_tree.heading("ID", text="ID")
        self.course_tree.heading("Name", text="Course Name")
        self.course_tree.heading("Fees", text="Fees")

        self.course_tree.column("ID", width=50, anchor="center")
        self.course_tree.column("Name", width=200)
        self.course_tree.column("Fees", width=100, anchor="e")

        self.course_tree.pack(padx=10, pady=10, expand=True, fill="both")
        self.course_tree.bind("<ButtonRelease-1>", self._on_course_select)

        scrollbar = ttk.Scrollbar(self.course_tree, orient="vertical", command=self.course_tree.yview)
        self.course_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def _load_courses_into_treeview(self):
        for item in self.course_tree.get_children():
            self.course_tree.delete(item)
        courses = self.db.get_all_courses()
        for course in courses:
            self.course_tree.insert("", "end", values=course)

    def _add_course(self):
        course_name = self.course_name_entry.get().strip()
        fees_str = self.course_fees_entry.get().strip()

        if not course_name or not fees_str:
            messagebox.showwarning("Input Error", "Course Name and Fees are required.")
            return
        try:
            fees = float(fees_str)
            if fees < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Fees must be a positive number.")
            return

        if self.db.add_course(course_name, fees):
            messagebox.showinfo("Success", "Course added successfully.")
            self._clear_course_fields()
            self._load_courses_into_treeview()
            self._update_payment_course_dropdown() # Update course dropdown in payments tab

    def _update_course(self):
        course_id_str = self.course_id_entry.get().strip()
        if not course_id_str:
            messagebox.showwarning("Selection Error", "Please select a course to update.")
            return
        try:
            course_id = int(course_id_str)
        except ValueError:
            messagebox.showerror("Invalid Input", "Invalid Course ID.")
            return

        course_name = self.course_name_entry.get().strip()
        fees_str = self.course_fees_entry.get().strip()

        if not course_name or not fees_str:
            messagebox.showwarning("Input Error", "Course Name and Fees are required.")
            return
        try:
            fees = float(fees_str)
            if fees < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Fees must be a positive number.")
            return

        if self.db.update_course(course_id, course_name, fees):
            messagebox.showinfo("Success", "Course updated successfully.")
            self._clear_course_fields()
            self._load_courses_into_treeview()
            self._update_payment_course_dropdown()

    def _delete_course(self):
        selected_item = self.course_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a course to delete.")
            return

        course_id = self.course_tree.item(selected_item, 'values')[0]

        if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete course ID {course_id}?"):
            if self.db.delete_course(course_id):
                messagebox.showinfo("Success", "Course deleted successfully.")
                self._clear_course_fields()
                self._load_courses_into_treeview()
                self._update_payment_course_dropdown()

    def _on_course_select(self, event):
        selected_item = self.course_tree.selection()
        if selected_item:
            values = self.course_tree.item(selected_item, 'values')
            self.course_id_entry.config(state='normal')
            self.course_id_entry.delete(0, tk.END)
            self.course_id_entry.insert(0, values[0])
            self.course_id_entry.config(state='readonly')

            self.course_name_entry.delete(0, tk.END)
            self.course_name_entry.insert(0, values[1])

            self.course_fees_entry.delete(0, tk.END)
            self.course_fees_entry.insert(0, values[2])
        else:
            self._clear_course_fields()

    def _clear_course_fields(self):
        self.course_id_entry.config(state='normal')
        self.course_id_entry.delete(0, tk.END)
        self.course_id_entry.config(state='readonly')
        self.course_name_entry.delete(0, tk.END)
        self.course_fees_entry.delete(0, tk.END)
        self.course_tree.selection_remove(self.course_tree.selection())

    # --- Payment Tab Functions ---
    def _setup_payment_tab(self):
        input_frame = ttk.LabelFrame(self.payment_tab, text="Payment Details", padding="10")
        input_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(input_frame, text="Payment ID:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.payment_id_entry = ttk.Entry(input_frame, state='readonly')
        self.payment_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(input_frame, text="Student:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.payment_student_combobox = ttk.Combobox(input_frame, state="readonly")
        self.payment_student_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.payment_student_combobox.bind("<<ComboboxSelected>>", self._on_payment_student_selected)

        ttk.Label(input_frame, text="Course:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.payment_course_combobox = ttk.Combobox(input_frame, state="readonly")
        self.payment_course_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.payment_course_combobox.bind("<<ComboboxSelected>>", self._on_payment_course_selected)

        ttk.Label(input_frame, text="Amount Paid:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.payment_amount_entry = ttk.Entry(input_frame)
        self.payment_amount_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(input_frame, text="Payment Date (YYYY-MM-DD):").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.payment_date_entry = ttk.Entry(input_frame)
        self.payment_date_entry.insert(0, datetime.now().strftime("%Y-%m-%d")) # Default to today
        self.payment_date_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(input_frame, text="Due Date (YYYY-MM-DD):").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.payment_due_date_entry = ttk.Entry(input_frame)
        self.payment_due_date_entry.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(input_frame, text="Status:").grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.payment_status_combobox = ttk.Combobox(input_frame, values=["Paid", "Partial", "Due"], state="readonly")
        self.payment_status_combobox.set("Paid") # Default status
        self.payment_status_combobox.grid(row=6, column=1, padx=5, pady=5, sticky="ew")
        input_frame.columnconfigure(1, weight=1)

        button_frame = ttk.LabelFrame(self.payment_tab, text="Actions", padding="10")
        button_frame.pack(padx=10, pady=5, fill="x")

        ttk.Button(button_frame, text="Record Payment", command=self._record_payment).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(button_frame, text="Update Payment", command=self._update_payment).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(button_frame, text="Delete Payment", command=self._delete_payment).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(button_frame, text="Clear Fields", command=self._clear_payment_fields).grid(row=0, column=3, padx=5, pady=5)

        self.payment_tree = ttk.Treeview(self.payment_tab, columns=("ID", "Student", "Course", "Amount Paid", "Payment Date", "Due Date", "Status"), show="headings")
        self.payment_tree.heading("ID", text="ID")
        self.payment_tree.heading("Student", text="Student")
        self.payment_tree.heading("Course", text="Course")
        self.payment_tree.heading("Amount Paid", text="Amount Paid")
        self.payment_tree.heading("Payment Date", text="Payment Date")
        self.payment_tree.heading("Due Date", text="Due Date")
        self.payment_tree.heading("Status", text="Status")

        self.payment_tree.column("ID", width=50, anchor="center")
        self.payment_tree.column("Student", width=120)
        self.payment_tree.column("Course", width=120)
        self.payment_tree.column("Amount Paid", width=100, anchor="e")
        self.payment_tree.column("Payment Date", width=100, anchor="center")
        self.payment_tree.column("Due Date", width=100, anchor="center")
        self.payment_tree.column("Status", width=80, anchor="center")

        self.payment_tree.pack(padx=10, pady=10, expand=True, fill="both")
        self.payment_tree.bind("<ButtonRelease-1>", self._on_payment_select)

        scrollbar = ttk.Scrollbar(self.payment_tree, orient="vertical", command=self.payment_tree.yview)
        self.payment_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self._update_payment_student_dropdown()
        self._update_payment_course_dropdown()

    def _update_payment_student_dropdown(self):
        students = self.db.get_all_students()
        student_names = [f"{s[0]} - {s[1]}" for s in students] # "ID - Name"
        self.payment_student_combobox['values'] = student_names
        self.student_data_map = {f"{s[0]} - {s[1]}": s[0] for s in students} # Map combo display to ID

    def _update_payment_course_dropdown(self):
        courses = self.db.get_all_courses()
        course_names = [f"{c[0]} - {c[1]} (Rs. {c[2]:.2f})" for c in courses] # "ID - Name (Fees)"
        self.payment_course_combobox['values'] = course_names
        self.course_data_map = {f"{c[0]} - {c[1]} (Rs. {c[2]:.2f})": c[0] for c in courses} # Map combo display to ID
        self.course_fees_map = {c[0]: c[2] for c in courses} # Map course ID to fees

    def _on_payment_student_selected(self, event):
        selected_student_display = self.payment_student_combobox.get()
        student_id = self.student_data_map.get(selected_student_display)
        # Optionally, load student's previous payments here if needed
        if student_id:
            self._load_payments_into_treeview(student_id)
        else:
            self._load_payments_into_treeview() # Load all if no student selected

    def _on_payment_course_selected(self, event):
        selected_course_display = self.payment_course_combobox.get()
        course_id = self.course_data_map.get(selected_course_display)
        if course_id and self.payment_amount_entry.get().strip() == '': # Auto-fill amount if empty
            total_fees = self.course_fees_map.get(course_id)
            if total_fees is not None:
                self.payment_amount_entry.delete(0, tk.END)
                self.payment_amount_entry.insert(0, str(total_fees))


    def _load_payments_into_treeview(self, student_id=None):
        for item in self.payment_tree.get_children():
            self.payment_tree.delete(item)
        if student_id:
            payments = self.db.get_payments_by_student(student_id)
        else:
            payments = self.db.get_all_payments()
        for payment in payments:
            self.payment_tree.insert("", "end", values=payment)

    def _record_payment(self):
        selected_student_display = self.payment_student_combobox.get()
        student_id = self.student_data_map.get(selected_student_display)

        selected_course_display = self.payment_course_combobox.get()
        course_id = self.course_data_map.get(selected_course_display)

        amount_paid_str = self.payment_amount_entry.get().strip()
        payment_date = self.payment_date_entry.get().strip()
        due_date = self.payment_due_date_entry.get().strip()
        status = self.payment_status_combobox.get().strip()

        if not all([student_id, course_id, amount_paid_str, payment_date, status]):
            messagebox.showwarning("Input Error", "All fields except 'Due Date' are required.")
            return

        try:
            amount_paid = float(amount_paid_str)
            if amount_paid < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount Paid must be a positive number.")
            return

        try:
            datetime.strptime(payment_date, "%Y-%m-%d")
            if due_date:
                datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Date format must be YYYY-MM-DD.")
            return

        if self.db.record_payment(student_id, course_id, amount_paid, payment_date, due_date, status):
            messagebox.showinfo("Success", "Payment recorded successfully.")
            self._clear_payment_fields()
            self._load_payments_into_treeview()

    def _update_payment(self):
        payment_id_str = self.payment_id_entry.get().strip()
        if not payment_id_str:
            messagebox.showwarning("Selection Error", "Please select a payment to update.")
            return
        try:
            payment_id = int(payment_id_str)
        except ValueError:
            messagebox.showerror("Invalid Input", "Invalid Payment ID.")
            return

        selected_student_display = self.payment_student_combobox.get()
        student_id = self.student_data_map.get(selected_student_display)

        selected_course_display = self.payment_course_combobox.get()
        course_id = self.course_data_map.get(selected_course_display)

        amount_paid_str = self.payment_amount_entry.get().strip()
        payment_date = self.payment_date_entry.get().strip()
        due_date = self.payment_due_date_entry.get().strip()
        status = self.payment_status_combobox.get().strip()

        if not all([student_id, course_id, amount_paid_str, payment_date, status]):
            messagebox.showwarning("Input Error", "All fields except 'Due Date' are required.")
            return

        try:
            amount_paid = float(amount_paid_str)
            if amount_paid < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount Paid must be a positive number.")
            return

        try:
            datetime.strptime(payment_date, "%Y-%m-%d")
            if due_date:
                datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Date format must be YYYY-MM-DD.")
            return

        if self.db.update_payment(payment_id, student_id, course_id, amount_paid, payment_date, due_date, status):
            messagebox.showinfo("Success", "Payment updated successfully.")
            self._clear_payment_fields()
            self._load_payments_into_treeview()


    def _delete_payment(self):
        selected_item = self.payment_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a payment to delete.")
            return

        payment_id = self.payment_tree.item(selected_item, 'values')[0]

        if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete payment ID {payment_id}?"):
            if self.db.delete_payment(payment_id):
                messagebox.showinfo("Success", "Payment deleted successfully.")
                self._clear_payment_fields()
                self._load_payments_into_treeview()

    def _on_payment_select(self, event):
        selected_item = self.payment_tree.selection()
        if selected_item:
            values = self.payment_tree.item(selected_item, 'values')
            self.payment_id_entry.config(state='normal')
            self.payment_id_entry.delete(0, tk.END)
            self.payment_id_entry.insert(0, values[0])
            self.payment_id_entry.config(state='readonly')

            # Populate student and course comboboxes
            student_name = values[1]
            course_name = values[2]
            
            # Find the full display string for the comboboxes based on name (less robust, but works for simple case)
            # A more robust solution would be to store IDs in treeview or fetch from DB by name
            for key, val_id in self.student_data_map.items():
                if student_name in key: # Check if the name part is in the key
                    self.payment_student_combobox.set(key)
                    break
            
            for key, val_id in self.course_data_map.items():
                if course_name in key: # Check if the name part is in the key
                    self.payment_course_combobox.set(key)
                    break

            self.payment_amount_entry.delete(0, tk.END)
            self.payment_amount_entry.insert(0, values[3])

            self.payment_date_entry.delete(0, tk.END)
            self.payment_date_entry.insert(0, values[4])

            self.payment_due_date_entry.delete(0, tk.END)
            self.payment_due_date_entry.insert(0, values[5])

            self.payment_status_combobox.set(values[6])
        else:
            self._clear_payment_fields()

    def _clear_payment_fields(self):
        self.payment_id_entry.config(state='normal')
        self.payment_id_entry.delete(0, tk.END)
        self.payment_id_entry.config(state='readonly')
        self.payment_student_combobox.set("")
        self.payment_course_combobox.set("")
        self.payment_amount_entry.delete(0, tk.END)
        self.payment_date_entry.delete(0, tk.END)
        self.payment_date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.payment_due_date_entry.delete(0, tk.END)
        self.payment_status_combobox.set("Paid")
        self.payment_tree.selection_remove(self.payment_tree.selection())

    # --- Report Tab Functions ---
    def _setup_report_tab(self):
        report_frame = ttk.LabelFrame(self.report_tab, text="Financial Reports", padding="10")
        report_frame.pack(padx=10, pady=10, fill="x")

        ttk.Button(report_frame, text="Generate Summary Report", command=self._generate_summary_report).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(report_frame, text="Show All Payments", command=lambda: self._load_payments_into_treeview()).grid(row=0, column=1, padx=5, pady=5)

        self.report_text = tk.Text(self.report_tab, height=15, wrap="word")
        self.report_text.pack(padx=10, pady=10, expand=True, fill="both")

    def _generate_summary_report(self):
        total_collected = self.db.get_total_fees_collected()
        outstanding_fees = self.db.get_outstanding_fees()

        report = f"--- Fees Summary Report ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n\n"
        report += f"Total Fees Collected: Rs. {total_collected:.2f}\n"
        report += f"Estimated Outstanding Fees: Rs. {outstanding_fees:.2f}\n\n"
        report += "Note: Outstanding fees calculation is a simplified sum of (Course Fees - Paid) for each course where fees are still due. A more complex calculation would involve tracking remaining balance per student per course.\n"

        self.report_text.delete(1.0, tk.END)
        self.report_text.insert(tk.END, report)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.db.close()
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FeesManagementApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing) # Handle window close
    root.mainloop()