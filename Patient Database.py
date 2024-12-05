
from tkinter import *
import sqlite3

# Functions -----------------------------------

def edit():
    editor = Tk()
    editor.title('Update Patient Data')
    editor.geometry("500x500")
    editor.config(bg = "lightyellow")

    conn = sqlite3.connect('F:/Final_Database_Python/Patient.db')
    c = conn.cursor()

    record_id = delete_box.get()

    if not record_id.isdigit():
        error_label = Label(editor, text="Please enter a valid patient ID number.", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
        error_label.grid(row=0, column=0, columnspan=2)
        return

    c.execute("SELECT * FROM Patient WHERE oid=?", (record_id,))
    record = c.fetchone()

    if not record:
        error_label = Label(editor, text="Patient record not found!", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
        error_label.grid(row=0, column=0, columnspan=2)
        return
    
    # Patient Name Entry and Label
    Patient_Name_editor = Entry(editor, width=30)
    Patient_Name_editor.grid(row=0, column=1, pady=(10, 0))
    Patient_Name_editor.insert(0, record[0])  # Patient Name

    Patient_Name_label = Label(editor, text="Patient Name", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
    Patient_Name_label.grid(row=0, column=0, padx=10, pady=(10, 0))

    # Sex Entry and Label
    Sex_editor = Entry(editor, width=30)
    Sex_editor.grid(row=1, column=1, pady=(10, 0))
    Sex_editor.insert(0, record[1])  # Sex

    Sex_label = Label(editor, text="Sex", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
    Sex_label.grid(row=1, column=0, padx=10, pady=(10, 0))

    # Date Of Birth Entry and Label
    Date_Of_Birth_editor = Entry(editor, width=30)
    Date_Of_Birth_editor.grid(row=2, column=1, pady=(10, 0))
    Date_Of_Birth_editor.insert(0, record[2])  # Date Of Birth

    Date_Of_Birth_label = Label(editor, text="Date Of Birth", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
    Date_Of_Birth_label.grid(row=2, column=0, padx=10, pady=(10, 0))

    # Age Registered Entry and Label
    Age_editor = Entry(editor, width=30)
    Age_editor.grid(row=3, column=1, pady=(10, 0))
    Age_editor.insert(0, record[3])  # Age

    Age_label = Label(editor, text="Age", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
    Age_label.grid(row=3, column=0, padx=10, pady=(10, 0))

    # Address Entry and Label
    Address_editor = Entry(editor, width=30)
    Address_editor.grid(row=4, column=1, pady=(10, 0))
    Address_editor.insert(0, record[4])  # Address

    Address_label = Label(editor, text="Address", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
    Address_label.grid(row=4, column=0, padx=10, pady=(10, 0))

    # Contact Number Entry and Label
    Contact_No_editor = Entry(editor, width=30)
    Contact_No_editor.grid(row=5, column=1, pady=(10, 0))
    Contact_No_editor.insert(0, record[5])  # Contact Number

    Contact_No_label = Label(editor, text="Contact No.", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
    Contact_No_label.grid(row=5, column=0, padx=10, pady=(10, 0))

    #Doctor Entry and Label
    Doctor_editor = Entry(editor, width=30)
    Doctor_editor.grid(row=6, column=1, pady=(10, 0))
    Doctor_editor.insert(0, record[6])  # Doctor

    Doctor_label = Label(editor, text="Doctor", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
    Doctor_label.grid(row=6, column=0, padx=10, pady=(10, 0))

    # Nurses Entry and Label
    Nurses_editor = Entry(editor, width=30)
    Nurses_editor.grid(row=7, column=1, pady=(10, 0))
    Nurses_editor.insert(0, record[7])  # Nurses

    Nurses_label = Label(editor, text="No. Of Nurses", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
    Nurses_label.grid(row=7, column=0, padx=10, pady=(10, 0))

    # Medication/Operation Entry and Label
    Medication_Operation_editor = Entry(editor, width=30)
    Medication_Operation_editor.grid(row=8, column=1, pady=(10, 0))
    Medication_Operation_editor.insert(0, record[8])  # Medication/Operation

    Medication_Operation_label = Label(editor, text="Medication/Operation", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
    Medication_Operation_label.grid(row=8, column=0, padx=10, pady=(10, 0))

    # Nurses Entry and Label
    Date_admitted_editor = Entry(editor, width=30)
    Date_admitted_editor.grid(row=9, column=1, pady=(10, 0))
    Date_admitted_editor.insert(0, record[9])  # Date Admitted

    Date_admitted_label = Label(editor, text="Date Admitted", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
    Date_admitted_label.grid(row=9, column=0, padx=10, pady=(10, 0))

    def save_update():
        updated_Patient_Name = Patient_Name_editor.get()
        updated_Sex = Sex_editor.get()
        updated_Date_Of_Birth = Date_Of_Birth_editor.get()
        updated_Age = Age_editor.get()
        updated_Address = Address_editor.get()
        updated_Contact_No = Contact_No_editor.get()
        updated_Doctor = Doctor_editor.get()
        updated_Nurses = Nurses_editor.get()
        updated_Medication_Operation = Medication_Operation_editor.get()
        updated_Date_admitted = Date_admitted_editor.get()

        c.execute('''UPDATE Patient SET
                        Patient_Name = ?, Sex = ?, Date_Of_Birth = ?, Age = ?, Address = ?, Contact_No = ?, Doctor = ?, Nurses = ?, Medication_Operation = ?, Date_admitted = ?     WHERE oid = ?''', 
                  (updated_Patient_Name, updated_Sex, updated_Date_Of_Birth, updated_Age, updated_Address, updated_Contact_No, updated_Doctor, updated_Nurses, updated_Medication_Operation, updated_Date_admitted, record_id))

        conn.commit()
        conn.close()

        editor.destroy()

        query()

    save_btn = Button(editor, text="Save Changes", command=save_update, bg="yellow", font = ("Arial Black", 12, "bold"))
    save_btn.grid(row=11, column=0, columnspan=2, pady=20, padx=10, ipadx=20)

    editor.mainloop()

     

    

def submit():
    conn = sqlite3.connect('F:/Final_Database_Python/Patient.db')
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
    conn = sqlite3.connect('F:/Final_Database_Python/Patient.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM Patient")
    records = c.fetchall()
    conn.close()

    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) >= 30:
            widget.grid_forget()

    print_records = ''
    for record in records:
        print_records += f" \n --------------- PATIENT RECORDS --------------- \n\n Patient Name : {record[0]} \n Sex : {record[1]} \n Date Of Birth : {record[2]} \n Age : {record[3]} \n Address : {record[4]} \n Contact# : {record[5]} \n Doctor: {record[6]} \n No. Of Nurses: {record[7]} \n Medication/Operation: {record[8]} \n Date Admitted: {record[9]} \n Patient ID: {record[10]}\n\n-------------------------------------------------------------------------------------------\n\n"

    query_label = Label(root, text=print_records, bg = "lightyellow", font = ("Arial Black", 12, "bold"))
    query_label.grid(row=30, column=0, columnspan=2)
    

def delete():
    conn = sqlite3.connect('F:/Final_Database_Python/Patient.db')
    c = conn.cursor()
    c.execute("DELETE FROM Patient WHERE oid=?", (delete_box.get(),))
    conn.commit()

    delete_box.delete(0, END)

    conn.close()

    query()


root = Tk() 
root.title('Patient Database')
root.geometry("900x900")
root.config(bg = "lightyellow")

# Entry -----------------------------------

Patient_Name = Entry(root, width=30)
Patient_Name.grid(row=0, column=1, padx=20)

Sex = Entry(root, width=30)
Sex.grid(row=1, column=1, padx=20)

Date_Of_Birth = Entry(root, width=30)
Date_Of_Birth.grid(row=2, column=1, padx=20)

Age = Entry(root, width=30)
Age.grid(row=3, column=1, padx=20)

Address = Entry(root, width=30)
Address.grid(row=4, column=1, padx=20)

Contact_No = Entry(root, width=30)
Contact_No.grid(row=5, column=1, padx=20)

Doctor = Entry(root, width=30)
Doctor.grid(row=0, column=3, padx=20)

Nurses = Entry(root, width=30)
Nurses.grid(row=1, column=3, padx=20)

Medication_Operation = Entry(root, width=30)
Medication_Operation.grid(row=2, column=3, padx=20)

Date_admitted = Entry(root, width=30)
Date_admitted.grid(row=3, column=3, padx=20)

# Label -----------------------------------

Patient_Name_label = Label(root, text="Patient Name", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
Patient_Name_label.grid(row=0, column=0)

Sex_label = Label(root, text="Sex", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
Sex_label.grid(row=1, column=0)

Date_Of_Birth_label = Label(root, text="Date Of Birth", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
Date_Of_Birth_label.grid(row=2, column=0)

Age_label = Label(root, text="Age", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
Age_label.grid(row=3, column=0)

Address_label = Label(root, text="Address", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
Address_label.grid(row=4, column=0)

Contact_No_label = Label(root, text="Contact#", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
Contact_No_label.grid(row=5, column=0)

Doctor_label = Label(root, text="Doctor", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
Doctor_label.grid(row=0, column=2)

Nurses_label = Label(root, text="No. Of Nurses", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
Nurses_label.grid(row=1, column=2)

Medication_Operation_label = Label(root, text="Medication/Operation", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
Medication_Operation_label.grid(row=2, column=2)

Date_admitted_label = Label(root, text="Date Admitted", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
Date_admitted_label.grid(row=3, column=2)

# Delete Entry and Label -----------------------------------

delete_box = Entry(root, width=30)
delete_box.grid(row=10, column=1, padx=30)

delete_box_label = Label(root, text="Select Patient No.", bg = "lightyellow", font = ("Arial Black", 12, "bold"))
delete_box_label.grid(row=10, column=0)

# Add Patient, Show Patients, Delete Patient, and Update Patient Record Button -----------------------------------

submit_btn = Button(root, text="Add Patient", command=submit, bg="Skyblue", font = ("Arial Black", 12, "bold"))
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=20)

query_btn = Button(root, text="Show Patients", command=query, bg="LightPink", font = ("Arial Black", 12, "bold"))
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=20)

delete_btn = Button(root, text="Delete Patient", command=delete, bg="Lightgreen", font = ("Arial Black", 12, "bold"))
delete_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=20)

update_btn = Button(root, text="Edit Patient Data", command=edit, bg="Orange", font = ("Arial Black", 12, "bold"))
update_btn.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=20)


root.mainloop()
