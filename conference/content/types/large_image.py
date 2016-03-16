from django.db import models
from django.template.loader import render_to_string
from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey


class LargeImage(models.Model):
    image = MediaFileForeignKey(MediaFile, related_name='+', limit_choices_to={'type': 'image'})

    class Meta:
        abstract = True
        verbose_name = "Large Image"

    def render(self, **kwargs):
        return render_to_string('images/large_image.html', {
            'image': self.image,
        })
