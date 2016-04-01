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
            'textbox': mark_safe(self.header_box.content),
        })


class HeaderBoxContent(models.Model):
    name = models.TextField(max_length=25)
    content = RichTextField()

    class Meta:
        verbose_name = "Header Box Content"

    def __unicode__(self):
        return u'%s' % self.name
