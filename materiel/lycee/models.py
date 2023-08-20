from django.db import models


# Create your models here.
class Enseignant(models.Model):
    nom = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    prenom = models.CharField(
        max_length=50,
        blank=False,
        null=False

    )

    def __str__(self):
        return self.nom + " " + self.prenom

class Budget(models.Model):
    TYPE_CHOICES = (
        ('budget_courant', 'Budget Courant'),
        ('budget_projet', 'Budget de Projet'),
        ('budget_financement_exceptionnel', 'Financement Exceptionnel')
    )

    type_budget = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.type_budget


class Responsable(models.Model):
    TYPE_CHOICES = (
        ("le lycee", "le lycee"),
        ('le mandant', 'le demandeur'),
        ('proprietaire', 'le propriètaire')
    )
    type_responsable = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.type_responsable


class Salle(models.Model):
    TYPE_CHOICES = (
        ('001', '001'),
        ('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'),
        ('201', '201'), ('202', '202'), ('203', '203'), ('204', '204'), ('205', '205'),
        ('301', '301'), ('302', '302'), ('303', '303'), ('304', '304'), ('305', '305'),
    )

    numero = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.numero


class Materiel(models.Model):
    TYPE_CHOICES = (
        ('smartphone', 'Smartphone'),
        ('tablette', 'Tablette'),
        ('ecran', 'Écran'),
        ('video_projecteur', 'Vidéo-projecteur'),
        ('pointeur_laser', 'Pointeur Laser'),
        # Ajoutez d'autres types de matériels si nécessaire
    )

    type_materiel = models.CharField(max_length=50, choices=TYPE_CHOICES)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE, related_name='materiels_responsables')
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='materiels_responsable')
    salle_actuelle = models.ForeignKey(Salle, on_delete=models.CASCADE, default='001')

    def __str__(self):
        return self.type_materiel


class Accessoire(models.Model):
    TYPE_CHOICES = (
        ('chargeur', 'Chargeur'),
        ('cable_usb', 'Cable USB'),
        ('cable_alimentation', 'Câble alimentation'),
        ('cable_hdmi', 'Cable HDMI'),
        ('piles', 'Piles'),
    )
    nom = models.CharField(max_length=50, choices=TYPE_CHOICES)
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)


class Emprunt(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    date_emprunt = models.DateField()
    date_retour = models.DateField()
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    object = models.TextField(max_length=255)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    passassion = models.BooleanField()

    def __str__(self):
        return str(self.id)


class Passassion(models.Model):
    donneur = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name="enseignant_donneur")
    receveur = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name="enseignant_receveur")
    date = models.DateField()
    lieu = models.ForeignKey(Salle, on_delete=models.CASCADE)
    objectif = models.TextField(max_length=255)
    emprunt = models.ForeignKey(Emprunt, on_delete=models.CASCADE, related_name="emprunt_lier")
