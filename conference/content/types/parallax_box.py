from django.db import models
from django.template.loader import render_to_string
from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey


class ParallaxBox(models.Model):
    image = MediaFileForeignKey(MediaFile, related_name='+', limit_choices_to={'type': 'image'})
    text_content = models.TextField()

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('parallax_box/parallax_box.html', {
            'image': self.image,
            'text_content': self.text_content,
        })
