__author__ = 'Dominic Fitzgerald'
from django.db import models

from mezzanine.core.models import RichText
from mezzanine.pages.models import Page

import mezzanine.core.fields


class HomePage(Page, RichText):
    heading = models.CharField(max_length=256)
    soundcloud_url = models.URLField('Soundcloud URL', blank=True, null=True)
    youtube_url = models.URLField('Youtube Video URL', blank=True, null=True)


class EventsPage(Page):
    heading = models.CharField('Page Heading', max_length=256, blank=True, null=True)
    richtext_content = mezzanine.core.fields.RichTextField('Content', blank=True, null=True)


class OptionalRichtextPage(Page):
    heading = models.CharField('Page Heading', max_length=256, blank=True, null=True)
    richtext_content = mezzanine.core.fields.RichTextField('Optional Content', blank=True, null=True)


class Event(models.Model):
    name = models.CharField('Event Name', max_length=512)
    time = models.DateTimeField('Event DateTime', blank=True, null=True)
    location = models.CharField('Event Location', max_length=512, blank=True, null=True)
    details = models.TextField('Event Details', blank=True, null=True)
    image = models.ImageField('Event Image', null=True, blank=True)
