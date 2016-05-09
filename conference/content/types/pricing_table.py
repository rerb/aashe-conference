from django.db import models
from django.template.loader import render_to_string


class PricingTable(models.Model):
    registration_levels = models.ManyToManyField('RegistrationLevel', verbose_name="Registration Levels")
    deadlines = models.ManyToManyField('Deadline', verbose_name="Deadlines")
    cvent_link = models.TextField(max_length=256, verbose_name="CVENT Registration Link", blank=True)

    class Meta:
        abstract = True
        verbose_name = "Pricing Table"

    def render(self, **kwargs):
        deadlines = self.deadlines.select_related()
        registration_levels = self.registration_levels.select_related()
        # Need to repack all of the deadlines and prices into organized columns that can be looped through
        columns = []
        for x in range(0, 4):
            # Create a column for this deadline with the deadline name as the header and
            # and empty list to put prices in order
            column = {'deadline': deadlines[x],
                      'prices': []}
            for level in registration_levels:
                # Need to unpack the levels into a temp list in order to match the indexing
                level_deadline_list = [
                    {'price': level.first_deadline_price, 'level': level},
                    {'price': level.second_deadline_price, 'level': level},
                    {'price': level.third_deadline_price, 'level': level},
                    {'price': level.on_site_price, 'level': level},
                ]
                # Add a price to list of prices
                column['prices'].append(level_deadline_list[x])
            # Save it into the columns list that gets passed to the template
            columns.append(column)

        return render_to_string('pricing_table/pricing_table.html', {
            'registration_levels': registration_levels,
            'deadlines': deadlines,
            'columns': columns,
            'cvent_link': self.cvent_link,
        })


class RegistrationLevel(models.Model):
    level_name = models.TextField(max_length=128, verbose_name="Name")
    level_details = models.TextField(max_length=512, verbose_name="Details", blank=True)
    first_deadline_price = models.IntegerField(verbose_name="First Deadline Price")
    second_deadline_price = models.IntegerField(verbose_name="Second Deadline Price")
    third_deadline_price = models.IntegerField(verbose_name="Third Deadline Price")
    on_site_price = models.IntegerField(verbose_name="On-Site Price")

    class Meta:
        verbose_name = "Registration Level"
        verbose_name_plural = "Registration Levels"

    def __unicode__(self):
        return u'%s' % self.level_name


class Deadline(models.Model):
    deadline = models.TextField(max_length=128)

    class Meta:
        verbose_name = "Deadline"
        verbose_name_plural = "Deadlines"

    def __unicode__(self):
        return u'%s' % self.deadline
