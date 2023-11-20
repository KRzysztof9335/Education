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

    @abstractmethod
    def auth_sms(self, code: str):
        pass



class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code: str) -> None:
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code: str):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order: Order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code: str) -> None:
        self.security_code = security_code

    def auth_sms(self, code: str):
        raise Exception("Credit card payments don't support SMS code authorization.")

    def pay(self, order: Order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address: str) -> None:
        self.email_address = email_address
        self.verified = False

    def auth_sms(self, code: str):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order: Order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = DebitPaymentProcessor("2349875")
processor.auth_sms("465839")
processor.pay(order)