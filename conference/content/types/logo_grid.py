from django.db import models
from django.template.loader import render_to_string
from logo_ticker import LogoCollection


class LogoGrid(models.Model):
    images = models.ForeignKey('LogoCollection')

    class Meta:
        abstract = True
        verbose_name = "Logo Image Grid"

    def render(self, **kwargs):
        images = self.images.images.select_related()
        return render_to_string('logo_grid/logo_grid.html', {
            'images': images,
        })
