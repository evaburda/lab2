from db import Base, Session, engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Date

s = Session()


class Patient(Base):
    __tablename__ = 'Patient'
    Patient_ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Birthday = Column(Date)
    Address = Column(String)

    medicine = relationship("Medicine")
    medical_record = relationship("Medical_Record")

    def __init__(self, patient_id, name, birthday, address):
        self.Patient_ID = patient_id
        self.Name = name
        self.Birthday = birthday
        self.Address = address

    def __repr__(self):
        return f"<Patients(patient_id={self.Patient_ID}, name={self.Name}, birthday={self.Birthday}, address={self.Address})>"


class Medicine(Base):
    __tablename__ = 'Medicine'
    Medicine_ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Dosage = Column(String)

    Patient_ID = Column(Integer, ForeignKey('Patient.Patient_ID'))

    def __init__(self, medicine_id, patient_id, name, dosage):
        self.Medicine_ID = medicine_id
        self.Patient_ID = patient_id
        self.Name = name
        self.Dosage = dosage

    def __repr__(self):
        return f"<Medicines(medicine_id={self.Medicine_ID}, patient_id={self.Patient_ID}, name={self.Name}, dosage={self.Dosage})>"

class Medical_Record(Base):
    __tablename__ = 'Medical_Record'
    Record_ID = Column(Integer, primary_key=True)
    Date = Column(Date)
    Symptoms = Column(String)
    Diagnosis = Column(String)

    Patient_ID = Column(Integer, ForeignKey('Patient.Patient_ID'))

    worker_record = relationship("Worker_Record")

    def __init__(self, record_id, patient_id, date, symptoms, diagnosis):
        self.Record_ID = record_id
        self.Patient_ID = patient_id
        self.Date = date
        self.Symptoms = symptoms
        self.Diagnosis = diagnosis

    def __repr__(self):
        return f"<Medical_Records(record_id={self.Record_ID}, patient_id={self.Patient_ID}, date={self.Date}, symptoms={self.Symptoms}, diagnosis={self.Diagnosis})>"


class Medical_Worker(Base):
    __tablename__ = 'Medical_Worker'
    Worker_ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Speciality = Column(String)

    worker_record = relationship("Worker_Record")

    def __init__(self, worker_id, name, speciality):
        self.Worker_ID = worker_id
        self.Name = name
        self.Speciality = speciality

    def __repr__(self):
        return f"<Medical_Worker(worker_id={self.Worker_ID}, name={self.Name}, speciality={self.Speciality})>"


class Worker_Record(Base):
    __tablename__ = 'Worker_Record'
    Tab_ID = Column(Integer, primary_key=True)

    Worker_ID = Column(Integer, ForeignKey('Medical_Worker.Worker_ID'))
    Record_ID = Column(Integer, ForeignKey('Medical_Record.Record_ID'))

    def __init__(self, tab_id, worker_id, record_id):
        self.Tab_ID = tab_id
        self.Worker_ID = worker_id
        self.Record_ID = record_id

    def __repr__(self):
        return f"<Worker_Record(tab_id={self.Tab_ID}, worker_id={self.Worker_ID}, record_id={self.Record_ID})>"

class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    def insert_patient(self, patient_id: int, name: str, birthday: Date, address: str) -> None:
        patient = Patient(patient_id=patient_id, name=name, birthday=birthday, address=address)
        s.add(patient)
        s.commit()

    def insert_medicine(self, medicine_id: int, patient_id: int, name: str, dosage: str) -> None:
        medicine = Medicine(medicine_id=medicine_id, patient_id=patient_id, name=name, dosage=dosage)
        s.add(medicine)
        s.commit()

    def insert_medical_record(self, record_id: int, patient_id: int, date: Date, symptoms: str, diagnosis: str) -> None:
        medical_record = Medical_Record(record_id=record_id, patient_id=patient_id, date=date, symptoms=symptoms, diagnosis=diagnosis)
        s.add(medical_record)
        s.commit()

    def insert_medical_worker(self, worker_id: int, name: str, speciality: str) -> None:
        medical_worker = Medical_Worker(worker_id=worker_id, name=name, speciality=speciality)
        s.add(medical_worker)
        s.commit()

    def insert_worker_record(self, tab_id: int, worker_id: int, record_id: int) -> None:
        worker_record = Worker_Record(tab_id=tab_id, worker_id=worker_id, record_id=record_id)
        s.add(worker_record)
        s.commit()

    def show_patients(self):
        return s.query(Patient.Patient_ID, Patient.Name, Patient.Birthday, Patient.Address).all()

    def show_medicines(self):
        return s.query(Medicine.Medicine_ID, Medicine.Patient_ID, Medicine.Name, Medicine.Dosage).all()

    def show_medical_records(self):
        return s.query(Medical_Record.Record_ID, Medical_Record.Patient_ID, Medical_Record.Date, Medical_Record.Symptoms, Medical_Record.Diagnosis).all()

    def show_medical_workers(self):
        return s.query(Medical_Worker.Worker_ID, Medical_Worker.Name, Medical_Worker.Speciality).all()

    def show_workers_records(self):
        return s.query(Worker_Record.Tab_ID, Worker_Record.Worker_ID, Worker_Record.Record_ID).all()

    def update_patient(self, name: str, birthday: Date, address: str, patient_id: int) -> None:
        s.query(Patient).filter_by(Patient_ID=patient_id).update({Patient.Name: name, Patient.Birthday: birthday, Patient.Address: address})
        s.commit()

    def update_medicine(self, patient_id: int, name: str, dosage: str, medicine_id: int) -> None:
        s.query(Medicine).filter_by(Medicine_ID=medicine_id).update({Medicine.Patient_ID: patient_id, Medicine.Name: name, Medicine.Dosage: dosage})
        s.commit()

    def update_medical_record(self, patient_id: int, date: Date, symptoms: str, diagnosis: str, record_id: int) -> None:
        s.query(Medical_Record).filter_by(Record_ID=record_id).update({Medical_Record.Patient_ID: patient_id, Medical_Record.Date: date, Medical_Record.Symptoms: symptoms, Medical_Record.Diagnosis: diagnosis})
        s.commit()

    def update_medical_worker(self, name: str, speciality: str, worker_id: int) -> None:
        s.query(Medical_Worker).filter_by(Worker_ID=worker_id).update({Medical_Worker.Name: name, Medical_Worker.Speciality: speciality})
        s.commit()

    def update_worker_record(self, worker_id: int, record_id: int, tab_id: int) -> None:
        s.query(Worker_Record).filter_by(Tab_ID=tab_id).update({Worker_Record.Worker_ID: worker_id, Worker_Record.Record_ID: record_id})
        s.commit()

    def delete_patient(self, patient_id) -> None:
        patient = s.query(Patient).filter_by(Patient_ID=patient_id).one()
        s.delete(patient)
        s.commit()

    def delete_medicine(self, medicine_id) -> None:
        medicine = s.query(Medicine).filter_by(Medicine_ID=medicine_id).one()
        s.delete(medicine)
        s.commit()

    def delete_medical_record(self, record_id) -> None:
        medical_record = s.query(Medical_Record).filter_by(Record_ID=record_id).one()
        s.delete(medical_record)
        s.commit()

    def delete_medical_worker(self, worker_id) -> None:
        medical_worker = s.query(Medical_Worker).filter_by(Worker_ID=worker_id).one()
        s.delete(medical_worker)
        s.commit()

    def delete_worker_record(self, tab_id) -> None:
        worker_record = s.query(Worker_Record).filter_by(Tab_ID=tab_id).one()
        s.delete(worker_record)
        s.commit()


