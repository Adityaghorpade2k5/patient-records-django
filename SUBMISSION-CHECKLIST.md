# Submission checklist — AAI Lab CCA1

Deadline: 21–22 Sept 2026. Group of 2.

## 1. Get it running (≈10 minutes)
- [ ] `python -m venv venv` and activate it
- [ ] `pip install -r requirements.txt`
- [ ] `python manage.py migrate`
- [ ] `python manage.py seed` — gives you six patients so screens aren't empty
- [ ] `python manage.py createsuperuser` — for the admin screenshot
- [ ] `python manage.py runserver`

## 2. Screenshots to take (this is what the PDF is graded on)
1. **Register / list page** at `/` — shows READ, with the sample data visible
2. **Search in action** — type `asthma` in the search box, screenshot the result
3. **Register a patient form** at `/patients/new/` — filled in, before saving
4. **Validation error** — submit the form with a 5-digit phone number; screenshot the red error
5. **Case sheet** at `/patients/<id>/` — shows a single record, plus the success banner after saving
6. **Edit form** at `/patients/<id>/edit/` — pre-filled with existing data (UPDATE)
7. **Delete confirmation** at `/patients/<id>/delete/` (DELETE)
8. **Django admin** at `/admin/` — patient list with filters
9. **Terminal running `python manage.py test`** — 5 tests, OK
10. **GitHub repo page** — file tree and commit history

## 3. Canva PDF layout
- Cover: project title, both names, PRNs, class, subject, date
- Slide: problem statement and objective (2–3 lines)
- Slide: tech stack — Python, Django, SQLite, HTML/CSS
- Slide: the `Patient` model — table of field names, types, validation
- Slide: URL routing table (the CRUD table from the README)
- Slides: the screenshots above, one CRUD operation per page, captioned
- Slide: GitHub link, printed in full as text as well as linked
- Slide: conclusion and what each member did

## 4. Submit
- [ ] Push code to GitHub, add your partner as a collaborator
- [ ] Export the Canva file as PDF, name it `AAI_CCA1_<RollNo1>_<RollNo2>.pdf`
- [ ] Upload the PDF to the Project PDFs OneDrive folder
- [ ] Reply to the mail with: project title + GitHub link + both names
