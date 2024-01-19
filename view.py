from datetime import datetime

class View:

    def show_menu(self):
        self.show_message("\nМеню:")
        self.show_message("1. Додати рядок")
        self.show_message("2. Показати таблицю")
        self.show_message("3. Редагувати рядок")
        self.show_message("4. Видалити рядок")
        self.show_message("5. Вихід")
        choice = input("Виберіть пункт: ")
        return choice

    def show_tables(self):
        self.show_message("\nТаблиці:")
        self.show_message("1. Patient (пацієнт)")
        self.show_message("2. Medicine (ліки)")
        self.show_message("3. Medical record (запис пацієнта)")
        self.show_message("4. Medical worker (лікар)")
        self.show_message("5. Worker record (лікар-запис)")
        self.show_message("6. Повернутися до меню")
        table = input("Оберіть потрібну таблицю: ")
        return table

    def show_patients(self, patients):
        print("\nPatients:")
        for patient in patients:
            print(f"ID: {patient[0]}, Name: {patient[1]}, Birthday: {patient[2]}, Address: {patient[3]}")

    def show_medicines(self, medicines):
        print("\nMedicines:")
        for medicine in medicines:
            print(f"ID: {medicine[0]}, Patient ID: {medicine[1]}, Name: {medicine[2]}, Dosage: {medicine[3]}")

    def show_medical_records(self, medical_records):
        print("\nMedical records:")
        for medical_record in medical_records:
            print(f"ID: {medical_record[0]}, Patient ID: {medical_record[1]}, Date: {medical_record[2]}, Symptoms: {medical_record[3]}, Diagnosis: {medical_record[4]}")

    def show_medical_workers(self, medical_workers):
        print("\nMedical workers:")
        for medical_worker in medical_workers:
            print(f"ID: {medical_worker[0]}, Name: {medical_worker[1]}, Speciality: {medical_worker[2]}")

    def show_workers_records(self, workers_records):
        print("\nWorkers records:")
        for worker_record in workers_records:
            print(f"ID: {worker_record[0]}, Worker ID: {worker_record[1]}, Record ID: {worker_record[2]}")

    def get_patient_input(self):
        while True:
            try:
                name = input("Enter patient name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                date = input("Enter birthday (YYYY-MM-DD): ")
                birthday = datetime.strptime(date, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        while True:
            try:
                address = input("Enter patient address: ")
                if address.strip():
                    break
                else:
                    print("Address cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return name, birthday, address

    def get_medicine_input(self):
        while True:
            try:
                patient_id = int(input("Enter patient ID: "))
                break
            except ValueError:
                print("Patient ID must be a number.")
        while True:
            try:
                name = input("Enter medicine name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                dosage = input("Enter medicine dosage: ")
                if dosage.strip():
                    break
                else:
                    print("Dosage cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return patient_id, name, dosage

    def get_medical_record_input(self):
        while True:
            try:
                patient_id = int(input("Enter patient ID: "))
                break
            except ValueError:
                print("Patient ID must be a number.")
        while True:
            try:
                date_input = input("Enter date (YYYY-MM-DD): ")
                date = datetime.strptime(date_input, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        while True:
            try:
                symptoms = input("Enter medical record symptoms: ")
                if symptoms.strip():
                    break
                else:
                    print("Symptoms cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                diagnosis = input("Enter medical record diagnosis: ")
                if diagnosis.strip():
                    break
                else:
                    print("Diagnosis cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return patient_id, date, symptoms, diagnosis

    def get_medical_worker_input(self):
        while True:
            try:
                worker_id = int(input("Enter worker ID: "))
                break
            except ValueError:
                print("Worker ID must be a number.")
        while True:
            try:
                name = input("Enter medical worker name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                speciality = input("Enter medical worker speciality: ")
                if speciality.strip():
                    break
                else:
                    print("Speciality cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return worker_id, name, speciality

    def get_worker_record_input(self):
        while True:
            try:
                worker_id = int(input("Enter worker ID: "))
                break
            except ValueError:
                print("Worker ID must be a number.")
        while True:
            try:
                record_id = int(input("Enter record ID: "))
                break
            except ValueError:
                print("Record ID must be a number.")
        return worker_id, record_id

    def get_id(self):
        while True:
            try:
                id = int(input("Enter ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def show_message(self, message):
        print(message)