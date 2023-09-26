from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Etudiant,
    Programme,
    Projet,
    Matiere,
    ProgrammeMatiere
)


# Create your views here.
def list(request):
    return render(request, 'list.html')

@login_required
def lister(request):
    lister_etudiant = Etudiant.objects.all()
    lister_programme = Programme.objects.all()
    lister_projet = Projet.objects.all()
    lister_matiere = Matiere.objects.all()
    lister_programme_matiere = ProgrammeMatiere.objects.all()

    context = {
        'lister_etudiant':lister_etudiant,
        'lister_programme':lister_programme,
        'lister_projet':lister_projet,
        'lister_matiere':lister_matiere,
        'lister_programme_matiere':lister_programme_matiere,
    }
    return render(request, 'lister.html', context)
