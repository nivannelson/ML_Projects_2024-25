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

    def __str__(self):
        return f"{self.reg_no}: {self.model} ({self.v_type}) - {self.mileage} kmpl"

class VehicleCollection:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def delete_vehicle(self, reg_no):
        self.vehicles = [v for v in self.vehicles if v.reg_no != reg_no]

    def modify_vehicle(self, reg_no, **updates):
        for v in self.vehicles:
            if v.reg_no == reg_no:
                for key, value in updates.items():
                    setattr(v, key, value)

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the collection.")
            return
        for v in self.vehicles:
            print(v)

    def sort_by_mileage(self):
        self.vehicles.sort(key=lambda x: x.mileage, reverse=True)

    def save_to_file(self, filename="vehicles.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self.vehicles, f)
        print("Data saved successfully.")

    def load_from_file(self, filename="vehicles.pkl"):
        try:
            with open(filename, "rb") as f:
                self.vehicles = pickle.load(f)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")

    def filter_and_export(self, attribute, value, output_file="filtered_report.pdf"):
        filtered_vehicles = [v for v in self.vehicles if getattr(v, attribute, None) == value]

        if not filtered_vehicles:
            print(f"No vehicles found with {attribute} = {value}")
            return
        
        pdf = canvas.Canvas(output_file, pagesize=letter)
        pdf.setFont("Helvetica", 12)
        pdf.drawString(100, 750, f"Filtered Vehicles by {attribute} = {value}")

        y = 720
        for v in filtered_vehicles:
            pdf.drawString(100, y, str(v))
            y -= 20

        pdf.save()
        print(f"Report saved as {output_file}")

# Example Usage
if __name__ == "__main__":
    vc = VehicleCollection()

    # Adding sample vehicles
    vc.add_vehicle(Vehicle("ENG001", "Tesla Model S", "Electric", 400, "Tesla", "REG123", "John Doe"))
    vc.add_vehicle(Vehicle("ENG002", "Toyota Prius", "Hybrid", 350, "Toyota", "REG456", "Jane Doe"))
    vc.add_vehicle(Vehicle("ENG003", "Honda Civic", "Petrol", 250, "Honda", "REG789", "Alice"))

    print("\n--- Display Vehicles ---")
    vc.display_vehicles()

    print("\n--- Sorted by Mileage ---")
    vc.sort_by_mileage()
    vc.display_vehicles()

    print("\n--- Modify Vehicle (REG456) ---")
    vc.modify_vehicle("REG456", mileage=360)
    vc.display_vehicles()

    print("\n--- Save and Load Data ---")
    vc.save_to_file()
    vc.load_from_file()

    print("\n--- Delete Vehicle (REG789) ---")
    vc.delete_vehicle("REG789")
    vc.display_vehicles()

    print("\n--- Exporting Filtered Report (Electric Vehicles) ---")
    vc.filter_and_export("v_type", "Electric")
