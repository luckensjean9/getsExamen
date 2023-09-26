from django.contrib import admin
from .models import (
    Etudiant,
    Programme,
    Projet,
    Matiere,
    ProgrammeMatiere
)

admin.site.site_header = "GEST EXAMEN"
admin.site.site_title = "Matrix509"

admin.site.register(Etudiant)
admin.site.register(Programme)
admin.site.register(Projet)
admin.site.register(Matiere)
admin.site.register(ProgrammeMatiere)


# Register your models here.
