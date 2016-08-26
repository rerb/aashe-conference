from django.db import models
from django.template.loader import render_to_string
from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey
from django.utils.safestring import mark_safe


class NewsLinkPane(models.Model):
    image = MediaFileForeignKey(
        MediaFile, related_name='+', limit_choices_to={'type': 'image'})
    title = models.TextField(max_length=32)
    text_block = models.TextField(max_length=100)
    url = models.TextField(max_length=255)

    class Meta:
        abstract = True
        verbose_name = "News Link Pane"

    def make_email_links(self, text_block):
        words = [word if '@' not in word
                 else '<a href="mailto:{0}">{0}</a>'.format(word)
                 for word in text_block.split(" ")]
        return " ".join(words)

    def render(self, **kwargs):
        return render_to_string('news_link_pane/news_link_pane.html', {
            'image': self.image,
            'title': self.title,
            'text_block': mark_safe(self.make_email_links(self.text_block)),
            'link_url': self.url,
        })
