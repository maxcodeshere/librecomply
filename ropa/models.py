from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
# Model for an organzination
class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    country = CountryField(blank_label="(select country)")
    data_protection_officer = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Model for data subject categories
class DataSubjectCategory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Model for data categories
class DataCategory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Model for Asset Locations
class ProcessingAssetLocation(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    country = CountryField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='asset_locations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Model for Assets used in processing
class ProcessingAsset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.ForeignKey(ProcessingAssetLocation, on_delete=models.SET_NULL, blank=True, null=True, related_name='assets')
    asset_type = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='assets')
    owner = models.CharField(max_length=255, blank=True, null=True)
    lifecycle_status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Model for the Register of Processing Activities (ROPA)
class ProcessingActivity(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='processing_activities')
    name = models.CharField(max_length=255)
    purpose = models.TextField()
    data_subject_categories = models.ManyToManyField(DataSubjectCategory, related_name='processing_activities')
    data_categories = models.ManyToManyField(DataCategory, help_text="List of data categories (e.g. name, email, health data, etc.)")
    assets = models.ManyToManyField(ProcessingAsset, related_name='processing_activities', blank=True)
    recipients = models.TextField(blank=True, null=True)
    third_country_transfers = models.TextField(blank=True, null=True)
    retention_period = models.CharField(max_length=255, blank=True, null=True)
    security_measures = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
