from feincms.module.page.models import Page
from django.utils.translation import ugettext_lazy as _

from types.master_slider import MainSlider, SliderImage
from feincms.content.raw.models import RawContent
from feincms.content.video.models import VideoContent
from gallery.models import GalleryContent
from types.logo_ticker import LogoTicker, SponsorLogo

import os


Page.register_templates({
    'title': _('Home Page'),
    'path': 'base.html',
    'regions': (
        ('masterslider', _('Master Slider')),
        ('call-to-action', _('Call to action bar')),
        ('about-info', _('About info')),
        ('parallax-quote', _('Parallax Quote')),
        ('services', _('Services Area')),
        ('team', _('Team')),
        ('testimonials', _('Testimonials')),
        ('sponsors', _('Sponsors')),
        ('footer', _('Footer')),
    )
})

if os.environ.get('CMS', False):
    Page.create_content_type(MainSlider)
    Page.create_content_type(RawContent)
    Page.create_content_type(GalleryContent)
    Page.create_content_type(VideoContent)
    Page.create_content_type(LogoTicker)
