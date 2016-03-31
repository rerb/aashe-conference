from django.db import models
from django.template.loader import render_to_string
from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey
from feincms.content.richtext.models import RichTextField


class TwoColumnKeynote(models.Model):
    ORIENTATIONS = (
        ('Left', 'Image Left'),
        ('Right', 'Image Right'),
    )

    image = MediaFileForeignKey(MediaFile, related_name='+', limit_choices_to={'type': 'image'})
    text_block = RichTextField()
    orientation = models.CharField(max_length=5, choices=ORIENTATIONS)

    class Meta:
        abstract = True
        verbose_name = "Two Column Keynote"

    def render(self, **kwargs):

        if self.orientation == 'Left':
            template = 'keynote/keynote_right.html'
        else:
            template = 'keynote/keynote_left.html'

        return render_to_string(template, {
            'image': self.image,
            'text_block': self.text_block,
        })
