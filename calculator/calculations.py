# pylint: disable=C0304, C0115, R0903

from calculator.calculation import Calculation

class Calculator:
    history = []

    @s

    @staticmethod
    def multiply(a: float, b: float) -> float:
        result = a * b
        Calculator.history.append(Calculation(a, b, result, "multiply"))
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        Calculator.history.append(Calculation(a, b, result, "divide"))
        return result

    @classmethod
    def get_history(cls):
        return cls.hi
