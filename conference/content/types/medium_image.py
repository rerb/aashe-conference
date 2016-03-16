from django.db import models
from django.template.loader import render_to_string
from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey


class MediumImage(models.Model):
    image = MediaFileForeignKey(MediaFile, related_name='+', limit_choices_to={'type': 'image'})

    class Meta:
        abstract = True
        verbose_name = "Medium Image"

    def render(self, **kwargs):
        return render_to_string('medium_image/medium_image.html', {
            'image': self.image,
        })
