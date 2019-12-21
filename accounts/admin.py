from django.contrib import admin
from .models import ContractorProfile, PublicProfile, Feedback, RoadProfile
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.
admin.site.register(ContractorProfile)
admin.site.register(PublicProfile)
admin.site.register(Feedback)
admin.site.register(RoadProfile)