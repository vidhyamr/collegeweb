from django.db import models

# Create your models here.
class FormEntry(models.Model):
    main_dropdown=models.CharField(max_length=100)
    sub_dropdown_1=models.CharField(max_length=100)