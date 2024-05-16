from django.db import models

# Create your models here.

class BaseModel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Monoambiente(BaseModel):
    # Otros campos específicos para un monoambiente podrían ir aquí

    def __str__(self):
        return f"Monoambiente: {self.name}"

class UnDormitorio(BaseModel):
    # Otros campos específicos para un departamento de un dormitorio podrían ir aquí

    def __str__(self):
        return f"Un dormitorio: {self.name}"

class DosDormitorios(BaseModel):
    # Otros campos específicos para un departamento de dos dormitorios podrían ir aquí

    def __str__(self):
        return f"Dos dormitorios: {self.name}"
