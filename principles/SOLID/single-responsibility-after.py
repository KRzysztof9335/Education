from typing import List

class Order:

    def __init__(self):
        self.items: List[str] = []
        self.quantities: List[int] = []
        self.prices: List[float] = []
        self.status = "open"

    def add_item(self, name: str, quantity: int, price: float):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor:
    def pay_debit(self, order: Order, security_code: str):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

    def pay_credit(self, order: Order, security_code: str):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaymentProcessor()
processor.pay_debit(order, "0372846")