from tkinter import *
import sqlite3

# Functions -----------------------------------


def patient():
    patient_root = Tk()
    patient_root.title('Patient Database')
    patient_root.geometry("900x900")
    patient_root.config(bg="lightyellow")

    # Ensure the table exists
    conn = sqlite3.connect('Patient.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Patient (
                    Patient_Name TEXT,
                    Sex TEXT,
                    Date_Of_Birth TEXT,
                    Age INTEGER,
                    Address TEXT,
                    Contact_No TEXT,
                    Doctor TEXT,
                    Nurses INTEGER,
                    Medication_Operation TEXT,
                    Date_admitted TEXT
                )''')
    conn.commit()
    conn.close()

    def edit():
        editor = Tk()
        editor.title('Update Patient Data')
        editor.geometry("500x500")
        editor.config(bg="lightyellow")

        conn = sqlite3.connect('Patient.db')
        c = conn.cursor()

        record_id = delete_box.get()

        if not record_id.isdigit():
            error_label = Label(
                editor, text="Please enter a valid patient ID number.", bg="lightyellow", font=("Arial Black", 12, "bold"))
            error_label.grid(row=0, column=0, columnspan=2)
            return

        c.execute("SELECT * FROM Patient WHERE oid=?", (record_id,))
        record = c.fetchone()

        if not record:
            error_label = Label(editor, text="Patient record not found!",
                                bg="lightyellow", font=("Arial Black", 12, "bold"))
            error_label.grid(row=0, column=0, columnspan=2)
            return

        # Create entry widgets for all fields
        fields = [
            ("Patient Name", record[0]),
            ("Sex", record[1]),
            ("Date Of Birth", record[2]),
            ("Age", record[3]),
            ("Address", record[4]),
            ("Contact No.", record[5]),
            ("Doctor", record[6]),
            ("No. Of Nurses", record[7]),
            ("Medication/Operation", record[8]),
            ("Date Admitted", record[9]),
        ]

        entries = []
        for i, (label, value) in enumerate(fields):
            Label(editor, text=label, bg="lightyellow",
                  font=("Arial Black", 12, "bold")).grid(row=i, column=0, padx=10, pady=5)
            entry = Entry(editor, width=30)
            entry.grid(row=i, column=1, pady=5)
            entry.insert(0, value)
            entries.append(entry)

        def save_update():
            updated_data = [entry.get() for entry in entries]
            c.execute('''UPDATE Patient SET
                            Patient_Name = ?, Sex = ?, Date_Of_Birth = ?, Age = ?, Address = ?, Contact_No = ?, Doctor = ?, Nurses = ?, Medication_Operation = ?, Date_admitted = ? 
                          WHERE oid = ?''', (*updated_data, record_id))
            conn.commit()
            conn.close()
            editor.destroy()
            query()

        Button(editor, text="Save Changes", command=save_update, bg="yellow",
               font=("Arial Black", 12, "bold")).grid(row=len(fields), column=0, columnspan=2, pady=20, ipadx=20)

        editor.mainloop()

    def submit():
        conn = sqlite3.connect('Patient.db')
        c = conn.cursor()

        c.execute("INSERT INTO Patient VALUES (:Patient_Name, :Sex, :Date_Of_Birth, :Age, :Address, :Contact_No, :Doctor, :Nurses, :Medication_Operation, :Date_admitted)",
                  {
                      'Patient_Name': Patient_Name.get(),
                      'Sex': Sex.get(),
                      'Date_Of_Birth': Date_Of_Birth.get(),
                      'Age': Age.get(),
                      'Address': Address.get(),
                      'Contact_No': Contact_No.get(),
                      'Doctor': Doctor.get(),
                      'Nurses': Nurses.get(),
                      'Medication_Operation': Medication_Operation.get(),
                      'Date_admitted': Date_admitted.get(),
                  })

        conn.commit()
        conn.close()

        # Clear the text boxes
        Patient_Name.delete(0, END)
        Sex.delete(0, END)
        Date_Of_Birth.delete(0, END)
        Age.delete(0, END)
        Address.delete(0, END)
        Contact_No.delete(0, END)
        Doctor.delete(0, END)
        Nurses.delete(0, END)
        Medication_Operation.delete(0, END)
        Date_admitted.delete(0, END)

    def query():
        conn = sqlite3.connect("Patient.db")
        c = conn.cursor()
        c.execute("SELECT *, oid FROM Patient")
        records = c.fetchall()
        conn.close()

        # Clear previous records in the query box
        query_text.config(state=NORMAL)
        query_text.delete(1.0, END)

        print_records = ""
        for record in records:
            print_records += f"⚕️Patient Name: {record[0]}\nSex: {record[1]}\nDate Of Birth: {record[2]}\nAge: {record[3]}\nAddress: {record[4]}\nContact No.: {record[5]}\nDoctor: {record[6]}\nNurses: {record[7]}\nMedication: {record[8]}\nDate Admitted: {record[9]}\nPatient ID: {record[10]}\n\n-------------------------------------------------------------------------\n\n\n"
        query_text.insert(END, print_records)
        query_text.config(state=DISABLED)

    def delete():
        conn = sqlite3.connect('Patient.db')
        c = conn.cursor()
        c.execute("DELETE FROM Patient WHERE oid=?", (delete_box.get(),))
        conn.commit()
        conn.close()
        delete_box.delete(0, END)
        query()

    # Entries and Labels -----------------------------------

    labels = [
        "Patient Name", "Sex", "Date Of Birth", "Age",
        "Address", "Contact#", "Doctor", "No. Of Nurses",
        "Medication/Operation", "Date Admitted"
    ]
    entries = [Entry(patient_root, width=30) for _ in labels]

    for i, (label, entry) in enumerate(zip(labels, entries)):
        Label(patient_root, text=label, bg="lightyellow", font=("Arial Black", 12, "bold")).grid(
            row=i % 5, column=(i // 5) * 2, padx=10, pady=5)
        entry.grid(row=i % 5, column=(i // 5) * 2 + 1, padx=10, pady=5)

    Patient_Name, Sex, Date_Of_Birth, Age, Address, Contact_No, Doctor, Nurses, Medication_Operation, Date_admitted = entries

    # Buttons -----------------------------------

    Button(patient_root, text="Add Patient", command=submit, bg="Skyblue", font=("Arial Black", 12, "bold")).grid(
        row=5, column=0, columnspan=2, pady=10, ipadx=20)
    Button(patient_root, text="Show Patients", command=query, bg="LightPink", font=("Arial Black", 12, "bold")).grid(
        row=6, column=0, columnspan=2, pady=10, ipadx=20)
    Button(patient_root, text="Delete Patient", command=delete, bg="Lightgreen", font=("Arial Black", 12, "bold")).grid(
        row=7, column=0, columnspan=2, pady=10, ipadx=20)
    Button(patient_root, text="Edit Patient Data", command=edit, bg="Orange", font=("Arial Black", 12, "bold")).grid(
        row=8, column=0, columnspan=2, pady=10, ipadx=20)

    delete_box = Entry(patient_root, width=30)
    delete_box.grid(row=9, column=1, padx=20, pady=10)
    Label(patient_root, text="Select Patient No.", bg="lightyellow", font=("Arial Black", 12, "bold")).grid(
        row=9, column=0, padx=10, pady=10)

    query_text = Text(patient_root, height=15, width=50, wrap=WORD, font=("Arial", 10, "bold"), state=DISABLED)
    query_text.grid(row=10, column=0, columnspan=4, padx=20, pady=10)

    patient_root.mainloop()


# Homepage -----------------------------------------------------------
root = Tk()
root.title("Hospital Management System")
root.geometry("400x400")
root.config(bg="lightblue")

Label(root, text="Welcome to Hospital Management", bg="lightblue", font=("Arial Black", 14, "bold")).pack(pady=50)

Button(root, text="Patient", command=patient, bg="green", font=("Arial", 12, "bold"), width=15).pack(pady=10)
Button(root, text="Exit", command=root.destroy, bg="red", font=("Arial", 12, "bold"), width=15).pack(pady=10)


root.mainloop()
