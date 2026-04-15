from typing import Final

class Doctor:
    """
    Doctor model representing healthcare practitioners.
    """

    def __init__(self, doctor_id: int, name: str, specialization: str):
        self.doctor_id: Final[int] = doctor_id
        self.name: str = name
        self.specialization: str = specialization

    def __str__(self) -> str:
        return f"{self.name} ({self.specialization})"