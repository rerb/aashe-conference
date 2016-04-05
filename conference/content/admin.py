from django.contrib import admin

from types.master_slider import SliderImage
from types.logo_ticker import SponsorLogo, LogoCollection
from types.header_box import HeaderBoxContent
from types.pricing_table import RegistrationLevel, Benefit

admin.site.register(SponsorLogo)
admin.site.register(SliderImage)
admin.site.register(LogoCollection)
admin.site.register(HeaderBoxContent)
admin.site.register(RegistrationLevel)
admin.site.register(Benefit)
