from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CustomUserProfile(models.Model):
    # User Basic Info
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Profile Picture
    profile_picture = models.ImageField(upload_to='pics', default='D:\Legacy Projects\rmics\rmics\media\smcrmi_logo_1.jpg')

    # Position Choices
    POSITION_CHOICES = [
        ('Operations Analyst', 'Operations Analyst'),
        ('Material Custodian', 'Material Custodian'),
        ('Maintenance Planner', 'Maintenance Planner'),
        ('Supervisor', 'Supervisor'),
        ('Engineering Head', 'Engineering Head'),
        ('Area Engineering Head', 'Area Engineering Head'),
        ('National Operations Manager', 'National Operations Manager'),
        ('General Manager', 'General Manager'),
    ]
    position = models.CharField(max_length=100, choices=POSITION_CHOICES, blank=True, null=True)

    # Profession Choices
    PROFESSION_CHOICES = [
        ('Electrical Engineer', 'Electrical Engineer'),
        ('Mechanical Engineer', 'Mechanical Engineer'),
        ('Civil Engineer', 'Civil Engineer'),
        ('Electronics Engineer', 'Electronics Engineer'),
        ('National Certificate', 'National Certificate'),
    ]
    profession = models.CharField(max_length=100, choices=PROFESSION_CHOICES, blank=True, null=True)

    # Plant Assignment Choices
    PLANT_ASSIGNMENT_CHOICES = [
        ('National Office - Pasig', 'National Office - Pasig'),
        ('BMEG-Bataan 1', 'BMEG-Bataan 1'),
        ('BMEG-Bataan 2', 'BMEG-Bataan 2'),
        ('BMEG-Echague', 'BMEG-Echague'),
        ('BMEG-Leganes', 'BMEG-Leganes'),
        ('BMEG-Ormoc', 'BMEG-Ormoc'),
        ('BMEG-Pavia', 'BMEG-Pavia'),
        ('BMEG-San Ildefonso', 'BMEG-San Ildefonso'),
        ('BMEG-Sta. Cruz', 'BMEG-Sta. Cruz'),
        ('BMEG-Tagoloan', 'BMEG-Tagoloan'),
        ('BMEG-Tarlac', 'BMEG-Tarlac'),
        ('BMEG-Pangasinan', 'BMEG-Pangasinan'),
        ('Mills-Mabini 1', 'Mills-Mabini 1'),
        ('Mills-Mabini 2', 'Mills-Mabini 2'),
        ('Mills-Tabangao', 'Mills-Tabangao'),
        ('BMEG-Mandaue', 'BMEG-Mandaue'),
        ('Mills-Mabini Premix', 'Mills-Mabini Premix'),
        ('Monterey-Sumilao', 'Monterey-Sumilao'),
    ]
    plant_assignment = models.CharField(max_length=100, choices=PLANT_ASSIGNMENT_CHOICES, blank=True, null=True)

    # Area Assignment Choices
    AREA_ASSIGNMENT_CHOICES = [
        ('Plant', 'Plant'),
        ('Area', 'Area'),
        ('Regional', 'Regional'),
        ('National', 'National'),
        ('Functional', 'Functional'),
    ]
    area_assignment = models.CharField(max_length=100, choices=AREA_ASSIGNMENT_CHOICES, blank=True, null=True)

    # Business Unit Choices
    BUSINESS_UNIT_CHOICES = [
        ('SMFI Feeds', 'SMFI Feeds'),
        ('SMFI Flour', 'SMFI Flour'),
        ('SMB Beer', 'SMB Beer'),
    ]
    business_unit = models.CharField(max_length=100, choices=BUSINESS_UNIT_CHOICES, blank=True, null=True)

    # Motto
    motto = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username  




    