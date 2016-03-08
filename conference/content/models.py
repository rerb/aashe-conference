from feincms.module.page.models import Page
from django.utils.translation import ugettext_lazy as _

from types.master_slider import MainSlider, SliderImage
from feincms.content.raw.models import RawContent
from feincms.content.video.models import VideoContent
from gallery.models import GalleryContent
from types.logo_ticker import LogoTicker, SponsorLogo
from types.parallax_box import ParallaxBox

import os


Page.register_templates({
    'title': _('Home Page'),
    'path': 'page_layout_templates/home_page.html',
    'regions': (
        ('masterslider', _('Master Slider')),
        ('call-to-action', _('Call To Action Bar')),
        ('about', _('About')),
        ('parallax', _('Parallax Box')),
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
    # Page.create_content_type(ParallaxBox)
