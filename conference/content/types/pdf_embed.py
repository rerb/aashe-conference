from django.db import models
from django.template.loader import render_to_string


class PDFEmbed(models.Model):
    name = models.CharField(max_length=255)
    pdf_file = models.FileField()

    class Meta:
        abstract = True
        verbose_name = "Embedded PDF"

    def render(self, **kwargs):
        return render_to_string('pdf_embed/pdf_embed.html', {
            'doc_name': self.name,
            'pdf': self.pdf_file.url
        })
