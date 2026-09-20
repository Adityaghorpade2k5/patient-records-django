from django import forms

from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "registration_no",
            "full_name",
            "age",
            "gender",
            "blood_group",
            "phone",
            "diagnosis",
            "consulting_doctor",
            "admitted_on",
            "status",
            "notes",
        ]
        widgets = {
            "registration_no": forms.TextInput(attrs={"placeholder": "PT-00142"}),
            "full_name": forms.TextInput(attrs={"placeholder": "Sunita Deshmukh"}),
            "phone": forms.TextInput(attrs={"placeholder": "9822011223"}),
            "diagnosis": forms.TextInput(attrs={"placeholder": "Type 2 diabetes mellitus"}),
            "consulting_doctor": forms.TextInput(attrs={"placeholder": "Dr. A. Kulkarni"}),
            "admitted_on": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }

    def clean_registration_no(self):
        return self.cleaned_data["registration_no"].strip().upper()

    def clean_full_name(self):
        return self.cleaned_data["full_name"].strip()
