from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PatientForm
from .models import Patient


def patient_list(request):
    """READ — list every patient, with optional search and status filter."""
    patients = Patient.objects.all()

    query = request.GET.get("q", "").strip()
    if query:
        patients = patients.filter(
            Q(full_name__icontains=query)
            | Q(registration_no__icontains=query)
            | Q(diagnosis__icontains=query)
            | Q(consulting_doctor__icontains=query)
        )

    status = request.GET.get("status", "")
    if status:
        patients = patients.filter(status=status)

    context = {
        "patients": patients,
        "query": query,
        "status": status,
        "status_choices": Patient.Status.choices,
        "total": Patient.objects.count(),
        "admitted": Patient.objects.filter(status=Patient.Status.ADMITTED).count(),
    }
    return render(request, "records/patient_list.html", context)


def patient_detail(request, pk):
    """READ — one patient's full record."""
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, "records/patient_detail.html", {"patient": patient})


def patient_create(request):
    """CREATE — register a new patient."""
    form = PatientForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        patient = form.save()
        messages.success(request, f"Registered {patient.full_name}.")
        return redirect("patient_detail", pk=patient.pk)

    return render(
        request,
        "records/patient_form.html",
        {"form": form, "heading": "Register a patient", "submit_label": "Save patient"},
    )


def patient_update(request, pk):
    """UPDATE — edit an existing record."""
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientForm(request.POST or None, instance=patient)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"Updated {patient.full_name}.")
        return redirect("patient_detail", pk=patient.pk)

    return render(
        request,
        "records/patient_form.html",
        {
            "form": form,
            "patient": patient,
            "heading": f"Edit {patient.full_name}",
            "submit_label": "Save changes",
        },
    )


def patient_delete(request, pk):
    """DELETE — remove a record after confirmation."""
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        name = patient.full_name
        patient.delete()
        messages.success(request, f"Deleted the record for {name}.")
        return redirect("patient_list")

    return render(request, "records/patient_confirm_delete.html", {"patient": patient})
