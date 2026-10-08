class Expense:
    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"Expense: {self.name}, Category: {self.category}, Amount: ${self.amount:.2f}"

    # Add this line so lists know how to display it:
    def __repr__(self):
        return self.__str__()