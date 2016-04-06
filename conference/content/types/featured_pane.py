from django.db import models
from django.template.loader import render_to_string


class FeaturedPane(models.Model):
    ICON_CHOICES = [
        ('badge', 'Badge'),
        ('bubbles', 'Bubbles'),
        ('note', 'Note'),
        ('briefcase', 'Briefcase'),
    ]

    icon = models.CharField(choices=ICON_CHOICES, max_length=10)
    title = models.TextField(max_length=64)
    text_block = models.TextField(max_length=256)

    class Meta:
        abstract = True
        verbose_name = "Featured Pane"

    def render(self, **kwargs):
        return render_to_string('featured_pane/featured_pane.html', {
            'icon': 'icon-' + self.icon,
            'title': self.title,
            'text_block': self.text_block,
        })
