from abc import ABC, abstractmethod
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


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order: Order):
        ...



class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code: str) -> None:
        self.security_code = security_code

    def pay(self, order: Order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code: str) -> None:
        self.security_code = security_code

    def pay(self, order:Order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address: str) -> None:
        self.email_address = email_address

    def pay(self, order: Order):
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor("my@email.com")
processor.pay(order)