# Module 7 Lesson 6 Activity 1: Restaurant Management System
# Build a complete desktop restaurant ordering interface with Canvas background,
# ttk themed widgets, enumerate() loop, ternary currency conversion, and .isdigit() input validation.

import os
import tkinter as tk
from tkinter import ttk, messagebox


class RestaurantOrderManagement:
    """Class representing the Restaurant Order Management Application."""

    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")

        # Menu items and base prices in USD
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }
        self.exchange_rate = 82  # USD to INR conversion rate

        # Set up the Canvas background before placing interface widgets
        self.setup_background(root)

        # Create a themed frame to hold all interface widgets in the center
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Heading label
        ttk.Label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels = {}      # References to item price labels
        self.menu_quantities = {}  # References to quantity Entry widgets

        # Create one row for each menu item using enumerate(..., start=1)
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12)
            )
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        # Currency selection dropdown with StringVar and Combobox
        self.currency_var = tk.StringVar()
        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(row=len(self.menu_items) + 1, column=0, padx=10, pady=5, sticky="w")

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("USD", "INR")
        )
        currency_dropdown.grid(
            row=len(self.menu_items) + 1,
            column=1,
            padx=10,
            pady=5
        )
        currency_dropdown.current(0)  # Default selection: USD

        # Update menu prices dynamically whenever currency changes
        self.currency_var.trace("w", self.update_menu_prices)

        # Place Order button
        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )
        order_button.grid(
            row=len(self.menu_items) + 2,
            columnspan=3,
            padx=10,
            pady=10
        )

    def setup_background(self, root):
        """Draw a background image onto a Canvas widget and preserve its reference."""
        bg_width, bg_height = 800, 600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack(fill="both", expand=True)

        bg_path = os.path.join(os.path.dirname(__file__), "background.png")
        if not os.path.exists(bg_path):
            bg_path = "background.png"

        original_image = tk.PhotoImage(file=bg_path)
        # Subsample to fit if image exceeds canvas size
        x_sub = max(1, original_image.width() // bg_width)
        y_sub = max(1, original_image.height() // bg_height)
        background_image = original_image.subsample(x_sub, y_sub)

        canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        # Store reference on canvas object to prevent garbage collection
        canvas.image = background_image

    def update_menu_prices(self, *args):
        """Update price labels according to the selected currency using a ternary operator."""
        currency = self.currency_var.get()
        # Ternary operator to select symbol and rate in one line each
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price}):")

    def place_order(self):
        """Validate entered quantities using .isdigit() and calculate total cost."""
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            # Validate input using .isdigit() before conversion
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
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
            messagebox.showerror("Error", "Please order at least one item.")


# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()
