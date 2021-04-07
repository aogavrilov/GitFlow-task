class Member:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_age(self) -> int:
        return self.age

    def get_name(self) -> str:
        return self.name


member = Member("Test", 19)
