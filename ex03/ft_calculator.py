class calculator:
    """Define a calculator """

    def __init__(self, vector):
        """Initialize calculator with a vector"""
        self.vector = vector

    def __add__(self, object) -> None:
        """addition operator overloading"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """multiplication operator overloading"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """subtraction operator overloading"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """division operator overloading"""
        if object == 0:
            print("Error: division by zero")
            return
        self.vector = [x / object for x in self.vector]
        print(self.vector)
