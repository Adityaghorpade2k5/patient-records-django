from django.contrib import admin

from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "registration_no",
        "full_name",
        "age",
        "consulting_doctor",
        "status",
        "admitted_on",
    )
    list_filter = ("status", "gender", "blood_group")
    search_fields = ("registration_no", "full_name", "diagnosis", "consulting_doctor")
    date_hierarchy = "admitted_on"
