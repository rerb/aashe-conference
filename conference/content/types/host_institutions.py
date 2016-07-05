from django.db import models
from django.template.loader import render_to_string
from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey


class HostInstitutionBlock(models.Model):
    images = models.ForeignKey('HostInstitutionLogoCollection')

    class Meta:
        abstract = True
        verbose_name = "Host Institutions Block"

    def render(self, **kwargs):
        images = self.images.images.select_related()
        logos = []
        for image in images:
            logo = render_to_string('host_institutions/' + self.images.level.lower() + '.html', {
                'image': image,
            })
            logos.append(logo)
        return render_to_string('host_institutions/host_institutions_block.html', {
            'level': self.images.level,
            'logos': logos,
        })


class HostInstitutionLogoCollection(models.Model):
    LEVEL_CHOICES = [
        ('Platinum', 'Platinum'),
        ('Silver', 'Silver'),
        ('Bronze', 'Bronze'),
        ('Friend', 'Friend'),
        ('Master', 'Master Host'),
        ('Regional', 'Regional Host'),
        ('Supporting', 'Supporting Host'),
    ]

    name = models.TextField(max_length=25)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=1028, verbose_name="Host/Sponsor Level")
    images = models.ManyToManyField('HostInstitutionLogo', blank=True)

    class Meta:
        verbose_name = "Host Institution/Sponsor Logo Collection"

    def __unicode__(self):
        return u'%s' % self.name


class HostInstitutionLogo(models.Model):
    name = models.TextField(max_length=255, verbose_name="Sponsor Name")
    image = MediaFileForeignKey(MediaFile, related_name='+',
                                limit_choices_to={'type': 'image'},
                                verbose_name="Logo Image", blank=True)
    url = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Host Institution/Sponsor Logo"
        verbose_name_plural = "Host Institution/Sponsor Logos"

    def __unicode__(self):
        return u'%s' % self.image
