from django.contrib import admin

from types.master_slider import SliderImage
from types.logo_ticker import SponsorLogo
from feincms.module.medialibrary.models import MediaFile


admin.site.register(SponsorLogo)
admin.site.register(SliderImage)
