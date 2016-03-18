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
from gallery import specs
from types.master_slider import MainSlider, SliderImage
from types.logo_ticker import LogoTicker, SponsorLogo
# from types.parallax_box import ParallaxBox
from types.call_to_action import CallToAction
from types.buttons import SingleButton, DoubleButton
from types.single_image_banner import SingleImageBanner
from types.featured_image_link_pane import FeaturedImageLinkPane
from types.medium_image import MediumImage
from types.large_image import LargeImage


"""
    Must manually define available gallery types from feincms_gallery,
    they are not made available automatically for some reason
"""
GALLERY_TYPES = [
    specs.ClassicLightbox,
]
GALLERY_TYPES[0].columns = 5


"""
    Register page layout templates
"""
Page.register_templates(
    {
        'title': _('Topic Page'),
        'path': 'page_layout_templates/Topic_page.html',
        'regions': (
            ('title_banner', _('Title Banner')),
            ('featured', _('Featured')),
            ('main_content', _('Main Content')),
            ('parallax_box', _('Parallax Box')),
            ('additional_content', _('Additional Content')),
            ('sponsors', _('Sponsors')),
        )},
    {
        'title': _('Detail Page'),
        'path': 'page_layout_templates/detail_page.html',
        'regions': (
            ('call_to_action', _('Parallax Box')),
            ('rich-text-left-column', _('Left Column Text Block')),
            ('medium-image-right-column', _('Right Column Image')),
            ('featured', _('Featured')),
            ('main_content', _('Main Content')),
            ('call_to_action', _('Parallax Box')),
            ('additional_content', _('Additional Content')),
            ('sponsors', _('Sponsors')),
        )},
    {
        'title': _('Home Page'),
        'path': 'page_layout_templates/home_page.html',
        'regions': (
            ('main_slider', _('Main Slider')),
            ('call_to_action', _('Call To Action Bar')),
            ('rich-text-left-column', _('Left Column Text Block')),
            ('medium-image-right-column', _('Right Column Image')),
            ('parallax_box_1', _('Parallax Box 1')),
            ('about', _('About')),
            ('parallax_box_2', _('Parallax Box 2')),
            ('featured', _('Featured')),
            ('sponsors', _('Sponsors')),
        )},
    {
        'title': _('Test Page'),
        'path': 'page_layout_templates/test_layout.html',
        'regions': (
            ('main_slider', _('Main Slider')),
            ('call_to_action', _('Call To Action Bar')),
            ('large_image', _('Large Image')),
            ('featured', _('Featured')),
            ('rich-text-left-column', _('Left Column Text Block')),
            ('medium-image-right-column', _('Right Column Image')),
            ('about', _('About')),
            ('parallax', _('Parallax Box')),
            ('sponsors', _('Sponsors')),
        )},
)


"""
    Register content types for page creation interface
"""
if os.environ.get('CMS', False):
    Page.create_content_type(MainSlider, regions='main_slider')
    # Page.create_content_type(RawContent)
    Page.create_content_type(GalleryContent)
    Page.create_content_type(VideoContent)
    Page.create_content_type(LogoTicker, regions='sponsors')
    # Page.create_content_type(ParallaxBox)
    Page.create_content_type(RichTextContent)
    Page.create_content_type(CallToAction, regions='call_to_action')
    Page.create_content_type(SingleButton)
    Page.create_content_type(DoubleButton)
    Page.create_content_type(SingleImageBanner)
    Page.create_content_type(FeaturedImageLinkPane, regions='featured')
    Page.create_content_type(MediumImage)
    Page.create_content_type(LargeImage)


"""
    Register page extension modules
"""
Page.register_extensions(
    'feincms.module.page.extensions.navigation',
)
