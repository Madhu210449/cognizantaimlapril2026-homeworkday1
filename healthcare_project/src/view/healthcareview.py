import typing
class HealthcareView:
    """
    Handles console interaction and display logic.
    """

    def display_header(self) -> None:
        print("\n🏥 HEALTHCARE MANAGEMENT SYSTEM\n")

    def show_doctors(self, doctors) -> None:
        print("Doctors:")
        for doctor in doctors:
            print(" -", doctor)

    def show_mapping(self, patient_name: str, disease: str, doctor_name: str | None) -> None:
        if doctor_name:
            print(f" {patient_name} ({disease}) ➜ {doctor_name}")
        else:
            print(f" {patient_name} ({disease}) ➜ No doctor available")
