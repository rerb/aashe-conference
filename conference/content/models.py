from feincms.module.page.models import Page
from django.utils.translation import ugettext_lazy as _
import os

"""
    Import built-in FeinCMS content type models
"""
from feincms.content.raw.models import RawContent
from feincms.content.video.models import VideoContent
from feincms.content.richtext.models import RichTextContent
from gallery.models import GalleryContent

"""
    Import custom content type models
"""
from types.master_slider import MainSlider, SliderImage
from types.logo_ticker import LogoTicker, SponsorLogo
# from types.parallax_box import ParallaxBox
from types.call_to_action import CallToAction
from types.buttons import SingleButton, DoubleButton
from types.single_image_banner import SingleImageBanner


"""
    Register page layout templates
"""
Page.register_templates({
    'title': _('Home Page'),
    'path': 'page_layout_templates/home_page.html',
    'regions': (
        ('main_slider', _('Main Slider')),
        ('call_to_action', _('Call To Action Bar')),
        ('about', _('About')),
        ('parallax', _('Parallax Box')),
        ('sponsors', _('Sponsors')),
        ('footer', _('Footer')),
    )
})


"""
    Register content types for page creation interface
"""
if os.environ.get('CMS', False):
    Page.create_content_type(MainSlider, regions='main_slider')
    Page.create_content_type(RawContent)
    Page.create_content_type(GalleryContent)
    Page.create_content_type(VideoContent)
    Page.create_content_type(LogoTicker, regions='sponsors')
    # Page.create_content_type(ParallaxBox)
    Page.create_content_type(RichTextContent)
    Page.create_content_type(CallToAction, regions='call_to_action')
    Page.create_content_type(SingleButton)
    Page.create_content_type(DoubleButton)
    Page.create_content_type(SingleImageBanner)


"""
    Register page extension modules
"""
Page.register_extensions(
    'feincms.module.page.extensions.navigation',
)
