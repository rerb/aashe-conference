from django.db import models
from django.template.loader import render_to_string


class PricingTable(models.Model):
    price_row_header = models.TextField(max_length=64, verbose_name="Price Row Header")
    registration_levels = models.ManyToManyField('RegistrationLevel', verbose_name="Registration Levels")

    class Meta:
        abstract = True
        verbose_name = "Pricing Table"

    def render(self, **kwargs):
        # First retrieve our many to many sets
        benefit_set = Benefit.objects.all()
        registration_levels = RegistrationLevel.objects.all()
        # Initialize list to pass to template
        level_list = []

        for level in registration_levels:
            # Initialize Dict for this level with empty list for checks
            # Also process the price into integer and decimal components for fancy display!
            price_decimal = int(level.price % 1 * 100)
            price_int = int(level.price)
            benefits = {
                'level_object': level,
                'price_int': price_int,
                'price_decimal': price_decimal,
            }

            # Loop through the list of all benefits
            benefits_list = []
            checks = level.checks.select_related()
            for benefit in benefit_set:
                # Check each to see if it's contained in the "checks" list
                if benefit in checks:
                    # If so, check that box
                    benefits_list.append(True)
                else:
                    # Otherwise don't
                    benefits_list.append(False)
                benefits['benefits_list'] = benefits_list

            level_list.append(benefits)

        return render_to_string('pricing_table/pricing_table.html', {
            'price_row_header': self.price_row_header,
            'benefit_set': benefit_set,
            'level_list': level_list,
            'registration_levels': registration_levels,
        })


class RegistrationLevel(models.Model):
    level_name = models.TextField(max_length=128, verbose_name="Name")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Registration Price")
    checks = models.ManyToManyField('Benefit', verbose_name="Included Benefits (boxes to check off)")

    class Meta:
        verbose_name = "Registration Level"
        verbose_name_plural = "Registration Levels"

    def __unicode__(self):
        return u'%s' % self.level_name


class Benefit(models.Model):
    name = models.TextField(max_length=128)

    class Meta:
        verbose_name = "Benefit"
        verbose_name_plural = "Benefits"

    def __unicode__(self):
        return u'%s' % self.name
