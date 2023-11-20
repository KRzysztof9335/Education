# SOLID

## S - Single responsibility

Function, class, method should have just one responsibility to change.
Thanks to it is also easier to write tests.

## O - Open, close

Code should be open for being extended but closed for modification.
Imagine you need to add new type of payment method. Instead of doing if statements, use 'Abstract class' with abstract methods. Each subclass will derive from it defining its own implementation of payment

## L - Liskov substitution

If we have subclass of abstract class then you should be able to replace any object without altering the correctness of the program

In example let's add new payment method which do not rely on security code, instead it relies on email address. Method in abstract class expects 'security_code' but got email which is an error.

There are two ways to fix it: move code or email address to constructor of specific payment method.

## I - Interface segregation

Better to have several interfaces instead of one general.

## D - Dependency Inversion

What if we would like to add new type of authorizer? Might be a bit problem. Instead use 'Dependency inversion' pattern which is 'Dependency injection' with 'Abstract Base Class'. So, provide function with just abstract object that will have specific method.
