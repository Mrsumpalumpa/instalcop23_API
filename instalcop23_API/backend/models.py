from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    code = models.CharField(max_length=100, unique=True)
    project_name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="projects")
    start_date = models.DateField()
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.project_name}"



