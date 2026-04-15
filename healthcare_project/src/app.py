from store.healthcarestore import HealthcareStore
from view.healthcareview import HealthcareView

def main() -> None:
    store = HealthcareStore()
    view = HealthcareView()

    store.generate_doctors()
    store.generate_patients()

    view.display_header()
    view.show_doctors(store.doctors)

    print("\nPatient → Doctor Mapping:")
    for patient in store.patients:
        doctor = store.map_patient_to_doctor(patient.disease)
        view.show_mapping(
            patient.name,
            patient.disease,
            doctor.name if doctor else None
        )

if __name__ == "__main__":
    main()
