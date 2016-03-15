from django.db import models
from django.template.loader import render_to_string
from feincms.content.richtext.models import RichTextField


class CallToAction(models.Model):
    textbox = RichTextField()
    link = models.URLField()
    button_text = models.TextField(max_length=20)

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('call_to_action/call_to_action.html', {
            'textbox': self.textbox,
            'link': self.link,
            'button_text': self.button_text,
        })
