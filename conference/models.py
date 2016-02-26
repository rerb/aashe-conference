from django.utils.translation import ugettext_lazy as _

from django.db import models
from django import forms
from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent


# class SponsorLogo(models.Model):
#     content = models.ForeignKey('gallery.Album')
#
#     class Meta:
#         abstract = True
#
#     @property
#     def media(self):
#         return forms.Media(
#             css={'all': ('aashe_theme/css/aashe_unify.css',), },
#             js=('aashe_theme/unify/js/plugins/master-slider/masterslider/masterslider.min.js')
#         )
#
#     def render(self, **kwargs):
#         return render_to_string('')
#
Page.register_templates({
    'title': _('Home Page'),
    'path': 'home.html',
    'regions': (
        ('about_info', _('About text content area')),
    )
})
#
# Page.create_content_type(RichTextContent)
# Page.create_content_type(SponsorLogo)
