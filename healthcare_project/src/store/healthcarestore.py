from typing import List, Optional
from faker import Faker
from models.doctor import Doctor
from models.patient import Patient

fake = Faker()

class HealthcareStore:
    """
    Handles business logic and data storage.
    """

    def __init__(self):
        self.doctors: List[Doctor] = []
        self.patients: List[Patient] = []

    def generate_doctors(self, count: int = 5) -> None:
        specializations = ["Cardiology", "Neurology", "Dermatology", "Orthopedic"]

        for i in range(count):
            self.doctors.append(
                Doctor(
                    doctor_id=i + 1,
                    name=fake.name(),
                    specialization=fake.random_element(specializations)
                )
            )

    def generate_patients(self, count: int = 5) -> None:
        diseases = ["Cardiology", "Neurology", "Dermatology", "Orthopedic"]

        for i in range(count):
            self.patients.append(
                Patient(
                    patient_id=i + 1,
                    name=fake.name(),
                    disease=fake.random_element(diseases)
                )
            )

    def map_patient_to_doctor(self, disease: str) -> Optional[Doctor]:
        for doctor in self.doctors:
            if doctor.specialization.lower() == disease.lower():
                return doctor
        return None