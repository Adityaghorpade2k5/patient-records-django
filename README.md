# Patient Records — Django CRUD Project

**Course:** AAI Lab — CCA1
**Project title:** Patient Records — a clinic register with full CRUD

A Django web application to register patients and manage their records. It covers
all four CRUD operations, plus search and filtering.

| Operation | Where it happens | URL |
|---|---|---|
| Create | Register a patient form | `/patients/new/` |
| Read | Register list + case sheet | `/` and `/patients/<id>/` |
| Update | Edit record form | `/patients/<id>/edit/` |
| Delete | Confirm-and-delete page | `/patients/<id>/delete/` |

Extras: keyword search across name / registration number / diagnosis / doctor,
status filter, Django admin, form validation, and five automated tests.

---

## Run it locally

```bash
# 1. create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 2. install Django
pip install -r requirements.txt

# 3. set up the database
python manage.py migrate

# 4. load sample patients (nice for screenshots)
python manage.py seed

# 5. optional: admin login
python manage.py createsuperuser

# 6. start the server
python manage.py runserver
```

Open http://127.0.0.1:8000/ — admin is at http://127.0.0.1:8000/admin/

Run the tests with `python manage.py test`.

---

## Project structure

```
patient-records-django/
├── manage.py
├── requirements.txt
├── config/                  # project settings, root URLconf, WSGI/ASGI
│   ├── settings.py
│   └── urls.py
└── records/                 # the app
    ├── models.py            # Patient model
    ├── forms.py             # PatientForm (ModelForm + validation)
    ├── views.py             # the five CRUD views
    ├── urls.py              # app URL patterns
    ├── admin.py             # admin registration
    ├── tests.py             # create / read / update / delete / search tests
    ├── management/commands/seed.py
    └── templates/records/   # base, list, detail, form, confirm_delete
```

## The model

`Patient` fields: registration number (unique), full name, age, gender,
blood group, phone, diagnosis, consulting doctor, admitted-on date, status
(Admitted / Outpatient / Discharged), notes, created-at, updated-at.

Validation: 10-digit phone, age 0–120, registration number letters/digits/hyphens
only and auto-uppercased, uniqueness enforced at both form and database level.

---

## Push to GitHub

```bash
git init
git add .
git commit -m "Django CRUD project: patient records"
git branch -M main
git remote add origin https://github.com/<your-username>/patient-records-django.git
git push -u origin main
```

Then add your partner: repo **Settings → Collaborators → Add people**, so both
names are on the project.

---

## Team

- Aditya Ghorpade
- (partner name)
