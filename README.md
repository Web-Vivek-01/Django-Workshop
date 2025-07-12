<h1 align="center">🚀 Django Workshop Project</h1>

<p align="center">
  Build your first Django REST API with CRUD operations: GET, POST, PUT, DELETE (by ID and by Email)!
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-4.x-green?style=flat&logo=django">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python">
  <img src="https://img.shields.io/badge/REST%20API-CRUD-orange?style=flat">
</p>

---

## 📚 Overview

This project teaches you how to build a simple Django REST API with full CRUD functionality including deleting by email input!
<br><br>"LMS is the project name, whereas Courses is the app name."<br>
<img src="images/LMS User.png" alt="Main LMS User" width="800"/>
---
## 📬 API Endpoints & Embedded Screenshots ( POSTMAN )

### 🔹 GET API – `http://127.0.0.1:8000/getAllUser`

> ✅ Fetch all records

<img src="images/ex - get api.png" alt="GET API" width="800"/>

---

### 🔹 POST API – `http://127.0.0.1:8000/signup/`

> ➕ Add a new record

<img src="images/ex - post api.png" alt="POST API" width="800"/>

---

### 🔹 PUT API – `http://127.0.0.1:8000/updateEmail/`

> ✏️ Update existing record by Email ID

<img src="images/ex - put api.png" alt="PUT API" width="800"/>

---

### 🔹 DELETE API (by number in url bar) – `http://127.0.0.1:8000/deleteUser/<number>`

> ❌ Delete record using number in URL Add bar  

<img src="images/ex - delete api (url).png" alt="DELETE API by number" width="800"/>

---

### 🔹 DELETE API (by Email Input) – `http://127.0.0.1:8000/deleteUserByEmail/`

> ❌ Delete record using email input in body

<img src="images/ex  - delete api using email input.png" alt="DELETE API by Email" width="800"/>

## ⚙️ Project Setup

```bash
git clone https://github.com/Web-Vivek-01/Django-Workshop.git
cd Django-Workshop

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py createsuperuser
    #username
    #email
    #password

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
