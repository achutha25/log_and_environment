class Calculation:
    def __init__(self, a: float, b: float, result: float, operation: str):
        self.a = a
        self.b = b
        self.result = result
        self.operation = operation

    def __repr__(self):
        return f"{self.a} {self.operation} {self.b} = {self.result}"

