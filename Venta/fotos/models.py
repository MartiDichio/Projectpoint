from django.db import models

# Create your models here.

class BaseModel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Monoambiente(BaseModel):
    

    def __str__(self):
        return f"Monoambiente: {self.name}"

class UnDormitorio(BaseModel):
    

    def __str__(self):
        return f"Un dormitorio: {self.name}"

class DosDormitorios(BaseModel):
    

    def __str__(self):
        return f"Dos dormitorios: {self.name}"
