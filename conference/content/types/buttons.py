from django.db import models
from django.template.loader import render_to_string


class SingleButton(models.Model):
    button_url = models.TextField(max_length=255)
    button_text = models.TextField(max_length=15)

    def render(self, **kwargs):
        return render_to_string('buttons/single_button.html', {
            'button_url': self.button_url,
            'button_text': self.button_text,
        })

    class Meta:
        abstract = True
        verbose_name = "Single Link Button"

    def __unicode__(self):
        return u'%s' % self.button_text


class DoubleButton(models.Model):
    button_url_1 = models.TextField(max_length=255)
    button_text_1 = models.TextField(max_length=15)
    button_url_2 = models.TextField(max_length=255)
    button_text_2 = models.TextField(max_length=15)

    def render(self, **kwargs):
        return render_to_string('buttons/double_button.html', {
            'button_url_1': self.button_url_1,
            'button_text_1': self.button_text_1,
            'button_url_2': self.button_url_2,
            'button_text_2': self.button_text_2,
        })

    class Meta:
        abstract = True
        verbose_name = "Double Link Button"

    def __unicode__(self):
        return u'%s' % self.button_text_1 + '&' + self.button_text_2
