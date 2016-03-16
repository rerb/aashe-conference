from django.db import models
from django.template.loader import render_to_string
from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey


class SingleImageBanner(models.Model):
    image = MediaFileForeignKey(MediaFile, related_name='+', limit_choices_to={'type': 'image'})
    text_header = models.TextField(max_length=15)
    text_block = models.TextField(max_length=35)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('single_image_banner/single_image_banner.html', {
            'image': self.image,
            'text_header': self.text_header,
            'text_block': self.text_block,
        })
