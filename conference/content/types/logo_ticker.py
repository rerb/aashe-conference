from django.db import models
from django.template.loader import render_to_string
from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey


class LogoTicker(models.Model):
    images = models.ForeignKey('LogoCollection')

    class Meta:
        abstract = True
        verbose_name = "Logo Image Ticker"

    def render(self, **kwargs):
        images = self.images.images.select_related()
        return render_to_string('logo_ticker/logo_ticker.html', {
            'images': images,
        })


class LogoCollection(models.Model):
    name = models.TextField(max_length=25)
    images = models.ManyToManyField('SponsorLogo')

    class Meta:
        verbose_name = "Logo Collection"

    def __unicode__(self):
        return u'%s' % self.name


class SponsorLogo(models.Model):
    name = models.TextField(max_length=255, verbose_name="Sponsor Name")
    image = MediaFileForeignKey(MediaFile, related_name='+',
                                limit_choices_to={'type': 'image'},
                                verbose_name="Logo Image")
    url = models.URLField()

    class Meta:
        verbose_name = 'Sponsor Logo'
        verbose_name_plural = 'Sponsor Logos'

    def __unicode__(self):
        return u'%s' % self.image
