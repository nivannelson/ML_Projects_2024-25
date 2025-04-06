import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Vehicle:
    def __init__(self, engine_no, model, v_type, mileage, vendor, reg_no, owner):
        self.engine_no = engine_no
        self.model = model
        self.v_type = v_type
        self.mileage = mileage
        self.vendor = vendor
        self.reg_no = reg_no
        self.owner = owner

    def to_tuple(self):
        return (self.engine_no, self.model, self.v_type, self.mileage, self.vendor, self.reg_no, self.owner)

class VehicleManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Management System")
        self.vehicles = []
        self.load_data()

        # UI Components
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        ttk.Label(self.root, text="Vehicle Management System", font=("Arial", 16, "bold")).pack(pady=10)

        # Entry Fields
        frame = ttk.Frame(self.root)
        frame.pack(pady=5)
        labels = ["Engine No:", "Model:", "Type:", "Mileage:", "Vendor:", "Reg No:", "Owner:"]
        self.entries = {}

        for i, label in enumerate(labels):
            ttk.Label(frame, text=label).grid(row=i, column=0, padx=5, pady=2)
            entry = ttk.Entry(frame)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.entries[label] = entry

        # Buttons
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Add Vehicle", command=self.add_vehicle).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_vehicle).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Modify", command=self.modify_vehicle).grid(row=0, column=2, padx=5)
        ttk.Button(btn_frame, text="Sort by Mileage", command=self.sort_by_mileage).grid(row=0, column=3, padx=5)
        ttk.Button(btn_frame, text="Export PDF", command=self.export_pdf).grid(row=0, column=4, padx=5)

        # Treeview for displaying vehicles
        columns = ("Engine No", "Model", "Type", "Mileage", "Vendor", "Reg No", "Owner")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(pady=10)

        # Load existing data
        self.update_table()

    def add_vehicle(self):
        values = [self.entries[label].get() for label in self.entries]
        if any(val == "" for val in values):
            messagebox.showwarning("Warning", "All fields are required!")
            return

        vehicle = Vehicle(*values)
        self.vehicles.append(vehicle)
        self.update_table()
        self.save_data()
        messagebox.showinfo("Success", "Vehicle added successfully!")

    def delete_vehicle(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select a vehicle to delete.")
            return
        
        reg_no = self.tree.item(selected_item)["values"][5]  # Get Reg No from table
        self.vehicles = [v for v in self.vehicles if v.reg_no != reg_no]
        self.update_table()
        self.save_data()
        messagebox.showinfo("Success", "Vehicle deleted successfully!")

    def modify_vehicle(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select a vehicle to modify.")
            return

        reg_no = self.tree.item(selected_item)["values"][5]
        for v in self.vehicles:
            if v.reg_no == reg_no:
                values = [self.entries[label].get() for label in self.entries]
                if any(val == "" for val in values):
                    messagebox.showwarning("Warning", "All fields are required!")
                    return
                
                v.engine_no, v.model, v.v_type, v.mileage, v.vendor, v.reg_no, v.owner = values
                break

        self.update_table()
        self.save_data()
        messagebox.showinfo("Success", "Vehicle modified successfully!")

    def sort_by_mileage(self):
        self.vehicles.sort(key=lambda x: float(x.mileage), reverse=True)
        self.update_table()

    def update_table(self):
        self.tree.delete(*self.tree.get_children())
        for v in self.vehicles:
            self.tree.insert("", "end", values=v.to_tuple())

    def save_data(self):
        with open("vehicles.pkl", "wb") as f:
            pickle.dump(self.vehicles, f)

    def load_data(self):
        try:
            with open("vehicles.pkl", "rb") as f:
                self.vehicles = pickle.load(f)
        except FileNotFoundError:
            self.vehicles = []

    def export_pdf(self):
        filtered_vehicles = [v.to_tuple() for v in self.vehicles]
        if not filtered_vehicles:
            messagebox.showwarning("Warning", "No vehicles to export.")
            return
        
        pdf_file = "vehicles_report.pdf"
        pdf = canvas.Canvas(pdf_file, pagesize=letter)
        pdf.setFont("Helvetica", 12)
        pdf.drawString(100, 750, "Vehicle Management Report")

        y = 720
        for v in filtered_vehicles:
            pdf.drawString(100, y, f"{v}")
            y -= 20

        pdf.save()
        messagebox.showinfo("Success", f"Report saved as {pdf_file}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleManagerApp(root)
    root.mainloop()
