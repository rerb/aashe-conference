from django.db import models
from django.template.loader import render_to_string
from feincms.content.richtext.models import RichTextField
from django.utils.safestring import mark_safe


class TableContent(models.Model):
    title = models.TextField(max_length=128, verbose_name="Title")
    text_block = RichTextField(verbose_name="Table header text block", blank=True)
    table = RichTextField(verbose_name="Table")

    class Meta:
        abstract = True
        verbose_name = "Rich Text Table Block"

    def render(self, **kwargs):
        fixed_table = self.table.replace('<table ', '<table class="table" ')

        return render_to_string('table/table.html', {
            'title': self.title,
            'text_block': mark_safe(self.text_block),
            'table': mark_safe(fixed_table),
        })
