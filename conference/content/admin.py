from django.contrib import admin

from types.master_slider import SliderImage
from types.logo_ticker import SponsorLogo, LogoCollection
from types.header_box import HeaderBoxContent
from types.pricing_table import RegistrationLevel, Deadline
from types.host_institutions import HostInstitutionLogo, \
    HostInstitutionLogoCollection
from types.faq import FAQ, FAQCollection


class RegistrationLevelAdmin(admin.ModelAdmin):
    model = RegistrationLevel
    list_display = ('level_name', 'order')
    list_editable = ('order',)


class DeadlineAdmin(admin.ModelAdmin):
    model = RegistrationLevel
    list_display = ('deadline', 'order')
    list_editable = ('order',)


admin.site.register(SponsorLogo)
admin.site.register(SliderImage)
admin.site.register(LogoCollection)
admin.site.register(HeaderBoxContent)
admin.site.register(RegistrationLevel, RegistrationLevelAdmin)
admin.site.register(Deadline, DeadlineAdmin)
admin.site.register(HostInstitutionLogo)
admin.site.register(HostInstitutionLogoCollection)
admin.site.register(FAQ)
admin.site.register(FAQCollection)
