from django.db import models
from django.template.loader import render_to_string
from feincms.module.medialibrary.models import MediaFile
from feincms.content.raw.models import RawContent
from feincms.module.medialibrary.fields import MediaFileForeignKey


class MainSlider(models.Model):
    images = models.ManyToManyField('SliderImage')

    class Meta:
        abstract = True

    def render(self, **kwargs):
        images = self.images.select_related.all()
        slider_elements = self.get_slider_elements(images)
        return render_to_string('main_slider/main_slider.html', {
            'slider_elements': slider_elements,
        })

    def get_slider_elements(self, images):
        elements = ''
        for image in images:
            element = render_to_string('main_slider/slider_element.html', {
                'image': image.image,
                'text_block': image.text_block,
            })
            elements += element
        return elements


class SliderImage(models.Model):
    image = MediaFileForeignKey(MediaFile, limit_choices_to={'type': 'image'})
    text_block = models.TextField(RawContent)

    class Meta:
        verbose_name = 'Image for master slider'
        verbose_name_plural = 'Images for master slider'

    def __unicode__(self):
        return u'%s' % self.image
