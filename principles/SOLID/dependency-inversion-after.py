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


class Authenticator(ABC):

    @abstractmethod
    def is_authorized(self) -> bool:
        ...


class SMSAuthenticator(Authenticator):

    def __init__(self):
        self.authorized = False

    def verify_code(self, code: str):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized

class AuthorizerGoogle(Authenticator):

    def __init__(self):
        self.authorized = False

    def verify_code(self, code: str):
        print(f"Verifying Google auth code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class AuthorizerRobot(Authenticator):

    def __init__(self):
        self.authorized = False

    def not_a_robot(self):
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order: Order):
        ...


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code: str, authorizer: Authenticator) -> None:
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order: Order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code: str) -> None:
        self.security_code = security_code

    def pay(self, order: Order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address: str, authorizer: Authenticator) -> None:
        self.email_address = email_address
        self.authorizer = authorizer


    def pay(self, order: Order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = AuthorizerRobot()
authorizer.not_a_robot()
processor = DebitPaymentProcessor("2349875", authorizer)
processor.pay(order)