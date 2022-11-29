from django.db import models

# Create your models here.
class Category(models.Model):
    label = models.CharField(max_length=20, verbose_name="label")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.label)


class Livre(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="livre",
                                 verbose_name="Project's category")
    titre = models.CharField(max_length=50)
    auteur = models.CharField(max_length=50)
    nombreDePage = models.IntegerField()
    description = models.TextField(blank=True)
    prix = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.nom)