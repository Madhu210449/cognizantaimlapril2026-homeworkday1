import typing
class Patient:
    """
    Patient model representing users seeking treatment.
    """

    def __init__(self, patient_id: int, name: str, disease: str):
        self.patient_id: int = patient_id
        self.name: str = name
        self.disease: str = disease

    def __str__(self) -> str:
        return f"{self.name} ({self.disease})"
