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

class Work:
    name: str
    salary: int
    responsibilities: str

    def __init__(self, name: str, salary: int, responsibilities: str) -> None:
        self.name = name
        self.salary = salary
        self.responsibilities = responsibilities

    def get_name(self) -> str:
        return self.name

    def get_salary(self) -> int:
        return self.salary

    def get_responsibilities(self) -> str:
        return self.responsibilities

member = Member("Test", 19)
