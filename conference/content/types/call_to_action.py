from django.db import models
from django.template.loader import render_to_string
from feincms.content.richtext.models import RichTextField
from django.utils.safestring import mark_safe


class CallToAction(models.Model):
    textbox = RichTextField()
    link = models.TextField(max_length=255)
    button_text = models.TextField(max_length=20)

    class Meta:
        abstract = True
        verbose_name = "Call To Action Bar"

    def make_email_links(self, text_block):
        words = [word if '@' not in word
                 else '<a href="mailto:{0}">{0}</a>'.format(word)
                 for word in text_block.split(" ")]
        return " ".join(words)

    def render(self, **kwargs):
        return render_to_string('call_to_action/call_to_action.html', {
            'textbox': mark_safe(self.make_email_links(self.textbox)),
            'link': self.link,
            'button_text': self.button_text,
        })
