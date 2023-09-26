from django.db import models

# Create your models here.

class Etudiant(models.Model):
    idEtudiant = models.CharField(max_length=100, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    origineScolaire = models.CharField(max_length=100)

    def __str__(self):
        return self.idEtudiant 

class Programme(models.Model):
    idProgramme = models.CharField(max_length=100, unique=True)
    idEtudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=100)
    annee = models.CharField(max_length=100)
    
    def __str__(self):
        return self.idProgramme 


class Projet(models.Model):
    idProjet = models.CharField(max_length=100, unique=True)
    idEtudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=100)
    
    def __str__(self):
        return self.idProjet


class Matiere(models.Model):
    idMatiere = models.CharField(max_length=100, unique=True)
    idEtudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    idProjet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    objectif = models.CharField(max_length=100)
    
    def __str__(self):
        return self.idMatiere


class ProgrammeMatiere(models.Model):
    idProgrammeMatiere = models.CharField(max_length=100, unique=True)
    idProgramme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    idMatiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.idProgrammeMatiere 