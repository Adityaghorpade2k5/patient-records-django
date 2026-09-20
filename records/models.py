from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from django.urls import reverse


class Patient(models.Model):
    """One row per patient registered at the clinic."""

    class Gender(models.TextChoices):
        FEMALE = "F", "Female"
        MALE = "M", "Male"
        OTHER = "O", "Other"

    class Status(models.TextChoices):
        ADMITTED = "AD", "Admitted"
        OUTPATIENT = "OP", "Outpatient"
        DISCHARGED = "DC", "Discharged"

    BLOOD_GROUPS = [
        ("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"),
        ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-"),
    ]

    registration_no = models.CharField(
        max_length=12,
        unique=True,
        help_text="Clinic registration number, e.g. PT-00142",
        validators=[
            RegexValidator(
                r"^[A-Za-z0-9\-]+$",
                "Use letters, digits and hyphens only.",
            )
        ],
    )
    full_name = models.CharField(max_length=120)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)]
    )
    gender = models.CharField(max_length=1, choices=Gender.choices)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS, blank=True)
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r"^\d{10}$", "Enter a 10-digit mobile number.")],
    )
    diagnosis = models.CharField(max_length=200)
    consulting_doctor = models.CharField(max_length=120)
    admitted_on = models.DateField()
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.OUTPATIENT
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-admitted_on", "full_name"]
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return f"{self.registration_no} — {self.full_name}"

    def get_absolute_url(self):
        return reverse("patient_detail", args=[self.pk])
