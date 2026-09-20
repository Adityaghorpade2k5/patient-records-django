"""Load a handful of sample patients so the register isn't empty for screenshots."""
from datetime import date

from django.core.management.base import BaseCommand

from records.models import Patient

SAMPLE = [
    ("PT-00101", "Sunita Deshmukh", 54, "F", "B+", "9822011223",
     "Type 2 diabetes mellitus", "Dr. A. Kulkarni", date(2026, 9, 3), "OP"),
    ("PT-00102", "Rahul Jadhav", 31, "M", "O+", "9890044556",
     "Bronchial asthma", "Dr. M. Patil", date(2026, 9, 8), "AD"),
    ("PT-00103", "Fatima Shaikh", 67, "F", "A-", "9766012398",
     "Hypertension with CKD stage 2", "Dr. S. Rane", date(2026, 9, 11), "AD"),
    ("PT-00104", "Omkar Bhosale", 8, "M", "AB+", "9004556677",
     "Acute gastroenteritis", "Dr. P. Nadkarni", date(2026, 9, 14), "DC"),
    ("PT-00105", "Neha Kulkarni", 26, "F", "O-", "9923311447",
     "Iron deficiency anaemia", "Dr. A. Kulkarni", date(2026, 9, 16), "OP"),
    ("PT-00106", "Ganesh Pawar", 45, "M", "B-", "9850077889",
     "Post-operative wound review", "Dr. S. Rane", date(2026, 9, 18), "AD"),
]


class Command(BaseCommand):
    help = "Insert sample patient records (skips any registration number already present)."

    def handle(self, *args, **options):
        created = 0
        for row in SAMPLE:
            reg, name, age, gender, blood, phone, dx, doctor, admitted, status = row
            _, was_created = Patient.objects.get_or_create(
                registration_no=reg,
                defaults={
                    "full_name": name,
                    "age": age,
                    "gender": gender,
                    "blood_group": blood,
                    "phone": phone,
                    "diagnosis": dx,
                    "consulting_doctor": doctor,
                    "admitted_on": admitted,
                    "status": status,
                },
            )
            created += was_created
        self.stdout.write(self.style.SUCCESS(f"Added {created} sample patient(s)."))
