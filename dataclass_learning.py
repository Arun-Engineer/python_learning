from dataclasses import dataclass

@dataclass
class Bug:
    id: int
    title: str
    severity: int = 1
    status: str = "open"
    team: str = "unassigned"

bug = Bug(id = 1, title= "Login Broken", severity= 5, status= "open", team= "mobile")
bug = Bug(id = 2, title= "Typo")
