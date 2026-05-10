from dataclasses import dataclass, asdict

@dataclass
class Bug:
    id: int
    title: str
    severity: int
    status: str
    team: str

b = Bug(id = 1, title= "Test", severity= 5, status= "open", team= "mobile")
print(b)
print(b.title)
print(b.severity)