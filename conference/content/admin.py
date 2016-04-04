from django.contrib import admin

from types.master_slider import SliderImage
from types.logo_ticker import SponsorLogo, LogoCollection
from types.header_box import HeaderBoxContent

admin.site.register(SponsorLogo)
admin.site.register(SliderImage)
admin.site.register(LogoCollection)
admin.site.register(HeaderBoxContent)
