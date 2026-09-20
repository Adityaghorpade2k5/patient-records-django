from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Patient


class PatientCrudTests(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            registration_no="PT-00001",
            full_name="Sunita Deshmukh",
            age=54,
            gender="F",
            blood_group="B+",
            phone="9822011223",
            diagnosis="Type 2 diabetes mellitus",
            consulting_doctor="Dr. A. Kulkarni",
            admitted_on=date(2026, 9, 10),
            status="OP",
        )

    def test_list_shows_patient(self):
        response = self.client.get(reverse("patient_list"))
        self.assertContains(response, "Sunita Deshmukh")

    def test_create(self):
        self.client.post(
            reverse("patient_create"),
            {
                "registration_no": "PT-00002",
                "full_name": "Rahul Jadhav",
                "age": 31,
                "gender": "M",
                "blood_group": "O+",
                "phone": "9890011223",
                "diagnosis": "Asthma",
                "consulting_doctor": "Dr. M. Patil",
                "admitted_on": "2026-09-15",
                "status": "AD",
                "notes": "",
            },
        )
        self.assertEqual(Patient.objects.count(), 2)

    def test_update(self):
        self.client.post(
            reverse("patient_update", args=[self.patient.pk]),
            {
                "registration_no": "PT-00001",
                "full_name": "Sunita Deshmukh",
                "age": 55,
                "gender": "F",
                "blood_group": "B+",
                "phone": "9822011223",
                "diagnosis": "Type 2 diabetes mellitus",
                "consulting_doctor": "Dr. A. Kulkarni",
                "admitted_on": "2026-09-10",
                "status": "DC",
                "notes": "",
            },
        )
        self.patient.refresh_from_db()
        self.assertEqual(self.patient.age, 55)
        self.assertEqual(self.patient.status, "DC")

    def test_delete(self):
        self.client.post(reverse("patient_delete", args=[self.patient.pk]))
        self.assertEqual(Patient.objects.count(), 0)

    def test_search(self):
        response = self.client.get(reverse("patient_list"), {"q": "diabetes"})
        self.assertContains(response, "Sunita Deshmukh")
