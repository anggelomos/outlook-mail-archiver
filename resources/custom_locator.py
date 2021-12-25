class Locator:
    def __init__(self, by: str, value: str):
        self.by = by
        self.value = value

    def __str__(self):
        return f"Locator(by: {self.by}, value: {self.value})"

    def __repr__(self):
        return f"Locator(by: {self.by}, value: {self.value})"
