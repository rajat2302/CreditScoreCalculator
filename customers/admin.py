from django.contrib import admin
from .models import Footprint,CreditScore,Profile
# Register your models here.
class FootprintAdmin(admin.ModelAdmin):
    pass

class CreditScoreAdmin(admin.ModelAdmin):
    pass

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Footprint, FootprintAdmin)
admin.site.register(CreditScore, CreditScoreAdmin)


