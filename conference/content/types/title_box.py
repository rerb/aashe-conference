from django.db import models
from django.template.loader import render_to_string
from feincms.content.richtext.models import RichTextField
from django.utils.safestring import mark_safe


class TitleBox(models.Model):
    textbox = RichTextField()

    class Meta:
        abstract = True
        verbose_name = 'Title Box'

    def render(self, **kwargs):
        return render_to_string('title_box/title_box.html', {
            'textbox': mark_safe(self.textbox),
        })
