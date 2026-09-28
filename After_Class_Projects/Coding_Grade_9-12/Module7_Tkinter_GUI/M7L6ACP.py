# Module 7 Lesson 6 ACP: Stationery Order Management App
# A complete stationery ordering application with Canvas background, themed ttk widgets,
# row generation via enumerate(), ternary currency switching, and input validation via .isdigit().

import os
import tkinter as tk
from tkinter import ttk, messagebox


class StationeryOrderManagement:
    """Class representing the Stationery Order Management Application."""

    def __init__(self, root):
        self.root = root
        self.root.title("Stationery Order Management App")

        # Store stationery items and their base prices in USD
        self.stationery_items = {
            "NOTEBOOK": 3,
            "PENCIL PACK": 2,
            "PEN SET": 4,
            "ERASER": 1,
            "GEOMETRY BOX": 6,
            "COLOUR PENCILS": 5
        }
        self.exchange_rate = 82  # Exchange rate for USD to INR

        # Set up the Canvas background before placing widgets
        self.setup_background(root)

        # Create a themed frame to hold all interface widgets in the center
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Heading label
        ttk.Label(
            frame,
            text="Stationery Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        # Store references to labels and Entry widgets
        self.item_labels = {}
        self.item_quantities = {}

        # Create one row for every stationery item using enumerate(..., start=1)
        for index, (item, price) in enumerate(self.stationery_items.items(), start=1):
            item_label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12)
            )
            item_label.grid(row=index, column=0, padx=10, pady=5, sticky="w")
            self.item_labels[item] = item_label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=index, column=1, padx=10, pady=5)
            self.item_quantities[item] = quantity_entry

        # Variable for storing the selected currency
        self.currency_var = tk.StringVar()
        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(row=len(self.stationery_items) + 1, column=0, padx=10, pady=5, sticky="w")

        # Currency selection dropdown
        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("USD", "INR")
        )
        currency_dropdown.grid(
            row=len(self.stationery_items) + 1,
            column=1,
            padx=10,
            pady=5
        )
        # Select USD as the default currency
        currency_dropdown.current(0)

        # Update prices whenever the currency changes
        self.currency_var.trace("w", self.update_item_prices)

        # Button to place the stationery order
        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )
        order_button.grid(
            row=len(self.stationery_items) + 2,
            columnspan=3,
            padx=10,
            pady=10
        )

    def setup_background(self, root):
        """Set up the Canvas background image and preserve its reference."""
        background_width = 800
        background_height = 600
        canvas = tk.Canvas(root, width=background_width, height=background_height)
        canvas.pack(fill="both", expand=True)

        bg_path = os.path.join(os.path.dirname(__file__), "background.png")
        if not os.path.exists(bg_path):
            bg_path = "background.png"

        original_image = tk.PhotoImage(file=bg_path)
        x_sub = max(1, original_image.width() // background_width)
        y_sub = max(1, original_image.height() // background_height)
        background_image = original_image.subsample(x_sub, y_sub)

        canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        # Keep a reference to prevent garbage collection
        canvas.image = background_image

    def update_item_prices(self, *args):
        """Update item prices according to the selected currency."""
        currency = self.currency_var.get()
        # Pick values using the ternary operator
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, label in self.item_labels.items():
            price = self.stationery_items[item] * rate
            label.config(text=f"{item} ({symbol}{price}):")

    def place_order(self):
        """Read quantities, validate input with .isdigit(), and place the order."""
        total_cost = 0
        order_summary = "Stationery Order Summary:\n"
        currency = self.currency_var.get()
        # Pick values using the ternary operator
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, entry in self.item_quantities.items():
            quantity = entry.get()
            # Validate that the quantity contains digits
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.stationery_items[item] * rate
                cost = quantity * price
                total_cost += cost
                if quantity > 0:
                    order_summary += (
                        f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
                    )

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one stationery item.")


# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = StationeryOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()
