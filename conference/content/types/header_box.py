from django.db import models
from django.template.loader import render_to_string
from feincms.content.richtext.models import RichTextField
from django.utils.safestring import mark_safe


class HeaderBox(models.Model):
    header_box = models.ForeignKey('HeaderBoxContent')

    class Meta:
        abstract = True
        verbose_name = "Header Box"

    def render(self, **kwargs):
        return render_to_string('header_box/header_box.html', {
            'header_box_title': self.header_box.title,
            'header_box_line_1': self.header_box.text_line_1,
            'header_box_line_2': self.header_box.text_line_2,
        })


class HeaderBoxContent(models.Model):
    name = models.TextField(max_length=25)
    title = models.TextField(max_length=128)
    text_line_1 = models.TextField(max_length=128)
    text_line_2 = models.TextField(max_length=128)

    class Meta:
        verbose_name = "Header Box Content"

    def __unicode__(self):
        return u'%s' % self.name
