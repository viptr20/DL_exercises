class Value():

    def __init__(self, data: float):
        self.data = float(data)

    def __add__(self, other: "Value") -> "Value":
        return Value(self.data + other.data)

    def __repr__(self) -> str:
        return f"Value(data={self.data})"