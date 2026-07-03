# 🏥 Hospital Patient Management System

A RESTful Hospital Patient Management System built using **FastAPI** and **Pydantic**. This project provides APIs to manage patient records with input validation, JSON-based data storage, and CRUD operations.

---

# 📌 Features

- 🚀 FastAPI REST API
- ➕ Add New Patient
- 📋 View All Patients
- 🔍 Search Patient by ID
- ✏️ Update Patient Details
- ❌ Delete Patient
- 📊 BMI Calculation
- 📈 Automatic Health Verdict
- ✅ Pydantic Validation
- 📂 JSON File Storage
- 📖 Interactive Swagger Documentation

---

# 🛠️ Tech Stack

### Backend

- FastAPI
- Uvicorn

### Validation

- Pydantic

### Data Storage

- JSON

### Language

- Python

### Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
Hospital_Patient_Management_System/
│
├── app/
│   ├── routes/
│   │   └── patient.py
│   │
│   ├── database.py
│   ├── models.py
│   └── main.py
│
├── data/
│   └── patients.json
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📋 Patient Information

Each patient record stores:

- Patient ID
- Name
- Age
- Gender
- Height
- Weight
- City
- Contact Details (if applicable)

Computed Information:

- BMI
- Health Verdict

---

# 🚀 API Endpoints

## Get All Patients

```http
GET /patients
```

Returns all patient records.

---

## Get Patient By ID

```http
GET /patient/{patient_id}
```

Returns a single patient record.

---

## Add New Patient

```http
POST /patient
```

Example Request

```json
{
    "id": "P101",
    "name": "John Doe",
    "age": 28,
    "gender": "Male",
    "height": 1.75,
    "weight": 72
}
```

---

## Update Patient

```http
PUT /patient/{patient_id}
```

Updates an existing patient.

---

## Delete Patient

```http
DELETE /patient/{patient_id}
```

Deletes the patient record.

---

# 📊 BMI Calculation

BMI is calculated automatically using:

```text
BMI = Weight / Height²
```

---

# 🩺 Health Verdict

Based on BMI, the application automatically categorizes the patient into health categories such as:

- Underweight
- Normal Weight
- Overweight
- Obese

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/rajputmanu2024-tech/Hospital_Patient_Management_System.git
```

Move into the project directory

```bash
cd Hospital_Patient_Management_System
```

Create a virtual environment

```bash
python -m venv myenv
```

Activate the virtual environment

Windows

```bash
myenv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```


# 🔮 Future Improvements

- SQLite / PostgreSQL Database
- JWT Authentication
- Search by Name
- Pagination
- Appointment Management
- Doctor Management
- Medical History
- Prescription Module
- Docker Support
- Deployment on Render

---

# 👨‍💻 Author

**Manu Rajput**

GitHub:

https://github.com/rajputmanu2024-tech

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.