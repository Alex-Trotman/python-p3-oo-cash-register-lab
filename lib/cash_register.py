#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0, items=None):
        self.discount = discount
        self.total = total
        # Initialize items as an empty list if none is provided
        self.items = [] if items is None else items
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        # Append just the title for each quantity of the item added
        for _ in range(quantity):
            self.items.append(title)  # Only append the title string
        self.last_transaction_amount = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            # Determine if the total is an integer and format accordingly
            if self.total.is_integer():
                formatted_total = f"${int(self.total)}"
            else:
                formatted_total = f"${self.total:.2f}"
            print(f"After the discount, the total comes to {formatted_total}.")
            return f"After the discount, the total comes to {formatted_total}."
        else:
            print("There is no discount to apply.")
            return "There is no discount to apply."

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        # Remove the last item based on the title; adjust logic if needed for multiple quantities
        if self.items:
            self.items.pop()
        self.last_transaction_amount = 0
        # Reset total if items list is empty
        if not self.items:
            self.total = 0.0
