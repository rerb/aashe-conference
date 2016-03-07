from django.db import models
from django.template.loader import render_to_string
from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey


class LogoTicker(models.Model):
    images = models.ManyToManyField('SponsorLogo')

    class Meta:
        abstract = True

    def render(self, **kwargs):
        images = self.images.select_related()
        return render_to_string('logo_ticker/logo_ticker.html', {
            'images': images,
        })


class SponsorLogo(models.Model):
    name = models.TextField(max_length=255)
    image = MediaFileForeignKey(MediaFile, related_name='+', limit_choices_to={'type': 'image'})
    url = models.TextField(max_length=255)

    class Meta:
        verbose_name = 'Sponsor Logo'
        verbose_name_plural = 'Sponsor Logos'

    def __unicode__(self):
        return u'%s' % self.image
