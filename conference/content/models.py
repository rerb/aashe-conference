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
from types.news_link_pane import NewsLinkPane
from types.keynote import TwoColumnKeynote
from types.title_box import TitleBox
from types.header_box import HeaderBox
from types.pricing_table import PricingTable
from django.template.defaulttags import register


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
        'path': 'page_layout_templates/topic_page.html',
        'regions': (
            ('header_block', _('Header Block')),
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
            ('header_block', _('Header Block')),
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
            ('header_block', _('Header Block')),
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
        'title': _('Two-Column Content Page'),
        'path': 'page_layout_templates/simple_page.html',
        'regions': (
            ('header_block', _('Header Block')),
            ('title_banner', _('Title Banner')),
            ('content', _('Two-Column Content')),
            ('call_to_action', _('Call To Action Bar')),
            ('sponsors', _('Sponsors')),
        )},
    {
        'title': _('Flickr Gallery Page'),
        'path': 'page_layout_templates/flickr_gallery.html',
        'regions': (
            ('header_block', _('Header Block')),
            ('title_banner', _('Title Banner')),
            ('flickr_gallery', _('Flickr Gallery')),
            ('sponsors', _('Sponsors')),
        )},
    {
        'title': _('Rich Text Page'),
        'path': 'page_layout_templates/plain_text_page.html',
        'regions': (
            ('header_block', _('Header Block')),
            ('title_banner', _('Title Banner')),
            ('rich_text_content', _('Content')),
            ('sponsors', _('Sponsors')),
        )},
    {
        'title': _('Video Gallery Page'),
        'path': 'page_layout_templates/video_gallery.html',
        'regions': (
            ('header_block', _('Header Block')),
            ('title_banner', _('Title Banner')),
            ('videos', _('Videos')),
            ('sponsors', _('Sponsors')),
        )},
)


"""
    Register content types for page creation interface
"""
if os.environ.get('CMS', False):
    Page.create_content_type(MainSlider, regions=('main_slider',))
    Page.create_content_type(GalleryContent, regions=('about', 'content', 'main_content', 'additional_content',))
    Page.create_content_type(VideoContent, regions=('about', 'content', 'main_content', 'additional_content', 'videos',))
    Page.create_content_type(LogoTicker, regions=('sponsors',))
    # Page.create_content_type(ParallaxBox, regions=('parallax_box_1', 'parallax_box_2', 'parallax',))
    Page.create_content_type(RichTextContent,
                             regions=('about', 'content', 'main_content', 'additional_content',
                                      'rich-text-left-column', 'rich_text_content',))
    Page.create_content_type(CallToAction, regions='call_to_action')
    Page.create_content_type(SingleButton)
    Page.create_content_type(DoubleButton)
    Page.create_content_type(SingleImageBanner, regions=('title_banner', 'call_to_action'))
    Page.create_content_type(MediumImage,
                             regions=('about', 'content', 'main_content', 'additional_content',
                                      'medium-image-right-column',))
    Page.create_content_type(LargeImage,
                             regions=('about', 'content', 'main_content', 'additional_content', 'large_image'))

    Page.create_content_type(TwoColumnKeynote, regions=('about', 'content', 'main_content', 'additional_content',))
    Page.create_content_type(TitleBox)
    Page.create_content_type(RawContent, regions=('flickr_gallery',))

    Page.create_content_type(FeaturedImageLinkPane, regions='featured')
    Page.create_content_type(NewsLinkPane, regions=('featured',))

    Page.create_content_type(HeaderBox, regions=('header_block',))
    Page.create_content_type(PricingTable, regions=('pricing_table', 'about'))

"""
    Register page extension modules
"""
Page.register_extensions(
    'feincms.module.page.extensions.navigation',
)
