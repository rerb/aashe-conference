from django.db import models
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from feincms.content.richtext.models import RichTextField


class GalleryBlock(models.Model):
    title_block = RichTextField(verbose_name="Title Text Block")
    flickr_embed_code = models.TextField(verbose_name="Full Flickr Embed Code (remember to modify height & width)")
    youtube_url = models.TextField(blank=True, verbose_name="Youtube Video URL")
    no_youtube_message = models.TextField(blank=True, verbose_name="Optional Message if No Youtube Video")

    class Meta:
        abstract = True
        verbose_name = "Gallery Block"

    def render(self, **kwargs):
        return render_to_string('gallery_block/gallery_block.html', {
            'title_block': mark_safe(self.title_block),
            'flickr_embed_code': mark_safe(self.flickr_embed_code),
            'youtube_url': self.youtube_url,
            'no_youtube_message': self.no_youtube_message,
        })
