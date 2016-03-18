from django.db import models
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey


class MainSlider(models.Model):
    images = models.ManyToManyField('SliderImage')

    class Meta:
        abstract = True
        verbose_name = "Main Slider"

    def render(self, **kwargs):
        images = self.images.select_related()
        slider_elements = self.get_slider_elements(images)
        return render_to_string('main_slider/main_slider.html', {
            'slider_elements': mark_safe(slider_elements),
        })

    def get_slider_elements(self, images):
        elements = ''
        for image in images:
            element = render_to_string('main_slider/slider_element.html', {
                'image': image.image,
                'text_header_line_1': image.text_header_line_1,
                'text_header_line_2': image.text_header_line_2,
                'text_block': image.text_block,
                'button_link_1': image.button_link_1,
                'button_text_1': image.button_text_1,
                'button_link_2': image.button_link_2,
                'button_text_2': image.button_text_2,
            })
            elements += element
        return elements


class SliderImage(models.Model):
    image = MediaFileForeignKey(MediaFile, related_name='+',
                                limit_choices_to={'type': 'image'})
    text_header_line_1 = models.TextField(max_length=15)
    text_header_line_2 = models.TextField(max_length=25)
    text_block = models.TextField(max_length=150)
    button_link_1 = models.URLField(blank=True)
    button_text_1 = models.TextField(blank=True, max_length=15)
    button_link_2 = models.URLField(blank=True)
    button_text_2 = models.TextField(blank=True, max_length=15)

    class Meta:
        verbose_name = 'Image for master slider'
        verbose_name_plural = 'Images for master slider'

    def __unicode__(self):
        return u'%s' % self.image
