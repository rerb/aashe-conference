from django.db import models
from django.template.loader import render_to_string
from feincms.content.richtext.models import RichTextField
from django.utils.safestring import mark_safe


class FAQBlock(models.Model):
    questions = models.ForeignKey('FAQCollection')

    class Meta:
        abstract = True
        verbose_name = "FAQ Block"

    def make_email_links(self, text_block):
        words = [word if '@' not in word
                 else '<a href="mailto:{0}">{0}</a>'.format(word)
                 for word in text_block.split(" ")]
        return " ".join(words)

    def render(self, **kwargs):
        questions = self.questions.questions.select_related()
        for question in questions:
            question.answer = mark_safe(self.make_email_links(question.answer))
        return render_to_string('faq/faq.html', {
            'questions': questions,
        })


class FAQCollection(models.Model):
    name = models.CharField(max_length=256)
    questions = models.ManyToManyField('FAQ')

    class Meta:
        verbose_name = 'FAQ Collection'

    def __unicode__(self):
        return u'%s' % self.name


class FAQ(models.Model):
    question = models.TextField(max_length=1024)
    answer = RichTextField()

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __unicode__(self):
        return u'%s' % self.question
