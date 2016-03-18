from django.db import models
from django.template.loader import render_to_string
from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey


class NewsLinkPane(models.Model):
    image = MediaFileForeignKey(MediaFile, related_name='+', limit_choices_to={'type': 'image'})
    title = models.TextField(max_length=32)
    text_block = models.TextField(max_length=100)
    url = models.URLField()

    class Meta:
        abstract = True
        verbose_name = "News Link Pane"

    def render(self, **kwargs):
        return render_to_string('news_link_pane/news_link_pane.html', {
            'image': self.image,
            'title': self.title,
            'text_block': self.text_block,
            'link_url': self.url,
        })
