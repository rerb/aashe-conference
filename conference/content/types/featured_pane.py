from django.db import models
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class FeaturedPane(models.Model):
    ICON_CHOICES = [
        ('badge', 'Badge'),
        ('bubbles', 'Bubbles'),
        ('note', 'Note'),
        ('briefcase', 'Briefcase'),
    ]

    icon = models.CharField(choices=ICON_CHOICES, max_length=10, verbose_name="Select Icon")
    title = models.TextField(max_length=64, verbose_name="Title")
    text_block = models.TextField(max_length=256, verbose_name="Text Block")
    button_url = models.TextField(max_length=255, blank=True, verbose_name="Button URL (optional)")
    button_text = models.TextField(blank=True, max_length=32, verbose_name="Button Text")

    class Meta:
        abstract = True
        verbose_name = "Featured Pane"

    def make_email_links(self, text_block):
        words = [word if '@' not in word else '<a href="mailto:{0}">{0}</a>'.format(word)
                 for word in text_block.split(" ")]
        return " ".join(words)

    def render(self, **kwargs):
        return render_to_string('featured_pane/featured_pane.html', {
            'icon': 'icon-' + self.icon,
            'title': self.title,
            'text_block': mark_safe(self.make_email_links(self.text_block)),
            'button_url': self.button_url,
        })
