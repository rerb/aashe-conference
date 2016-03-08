from feincms.module.page.models import Page
from django.utils.translation import ugettext_lazy as _

from types.master_slider import MainSlider, SliderImage
from feincms.content.raw.models import RawContent
from feincms.content.video.models import VideoContent
from gallery.models import GalleryContent
from types.logo_ticker import LogoTicker, SponsorLogo
# from types.parallax_box import ParallaxBox
from feincms.content.richtext.models import RichTextContent

import os


Page.register_templates({
    'title': _('Home Page'),
    'path': 'page_layout_templates/home_page.html',
    'regions': (
        ('main_slider', _('Main Slider')),
        ('call-to-action', _('Call To Action Bar')),
        ('about', _('About')),
        ('parallax', _('Parallax Box')),
        ('sponsors', _('Sponsors')),
        ('footer', _('Footer')),
    )
})

if os.environ.get('CMS', False):
    Page.create_content_type(MainSlider, regions='main_slider')
    Page.create_content_type(RawContent)
    Page.create_content_type(GalleryContent)
    Page.create_content_type(VideoContent)
    Page.create_content_type(LogoTicker, regions='sponsors')
    # Page.create_content_type(ParallaxBox)
    Page.create_content_type(RichTextContent)
