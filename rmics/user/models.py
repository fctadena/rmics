from django.db import models
from django.contrib.auth.models import User
from ams.models import PlantAssignment

# Create your models here.


class CustomUserProfile(models.Model):
    # User Basic Info
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Profile Picture
    profile_picture = models.ImageField(upload_to='pics', default='smcrmi_logo_1.jpg')
    
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

    
    
    plant_assignment = models.ForeignKey(PlantAssignment, on_delete=models.SET_NULL, null=True, blank=True)
    
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




class Reward(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    awardee = models.ManyToManyField(User, verbose_name='awardee')
    certificate = models.FileField(upload_to='certificates/', max_length=100, verbose_name='certificate', default='smcrmi_logo_1.jpg')


    def __str__(self):
        awardee_names = ', '.join(str(user) for user in self.awardee.all())
        return f"{awardee_names} - {self.title}"
