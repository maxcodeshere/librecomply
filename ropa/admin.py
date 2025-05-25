from django.contrib import admin
from .models import Organization, ProcessingActivity, DataSubjectCategory, DataCategory, ProcessingAsset, ProcessingAssetLocation
# Register your models here.
admin.site.register(Organization)
admin.site.register(ProcessingActivity)
admin.site.register(DataSubjectCategory)
admin.site.register(DataCategory)
admin.site.register(ProcessingAsset)
admin.site.register(ProcessingAssetLocation)