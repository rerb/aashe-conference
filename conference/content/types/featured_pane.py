from django.db import models
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class FeaturedPane(models.Model):
    ICON_CHOICES = [
        ('icon-badge', 'Badge'),
        ('icon-bubbles', 'Bubbles'),
        ('icon-note', 'Note'),
        ('icon-briefcase', 'Briefcase'),
        ('icon-communication-096', 'Communication 096'),
        ('icon-hotel-restaurant-002', 'Hotel-Restaurant 002'),
        ('icon-education-092', 'Education 092'),
        ('icon-education-086', 'Education 086'),
        ('icon-communication-171', 'Communication 171'),
        ('icon-education-007', 'Education 007'),
        ('icon-communication-057', 'Communication 057'),
        ('fa fa-recycle', 'Recycle'),
        ('icon-education-197', 'Education 197'),
        ('icon-education-192', 'Education 192'),
        ('icon-finance-053', 'Finance 053'),
        ('icon-finance-105', 'Finance 105'),
        ('icon-communication-168', 'Communication 168'),
        ('icon-travel-021', 'Travel 021'),
        ('icon-travel-014', 'Travel 014'),
        ('icon-travel-079', 'Travel 079'),
        ('icon-travel-056', 'Travel 056'),
        ('icon-education-064', 'Education 064'),
        ('icon-education-127', 'Education 127'),
        ('icon-communication-023', 'Communication 023'),
        ('icon-communication-076', 'Communication 076'),
        ('icon-travel-150', 'Travel 150'),
        ('icon-communication-055', 'Communication 055'),
        ('icon-communication-109', 'Communication 109'),
        ('icon-electronics-097', 'Electronics 097'),
        ('icon-weather-001', 'Weather 001'),
        ('icon-communication-082', 'Communication 082'),
    ]

    icon = models.CharField(choices=ICON_CHOICES, max_length=1028, verbose_name="Select Icon")
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
            'icon': self.icon,
            'title': self.title,
            'text_block': mark_safe(self.make_email_links(self.text_block)),
            'button_url': self.button_url,
        })
