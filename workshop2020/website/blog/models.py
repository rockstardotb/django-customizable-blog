from django.db import models
from django.contrib import admin
import uuid
from django import forms
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class BackgroundImage(models.Model):
    background_image_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    background_image =  models.ImageField(upload_to='./images', blank=True,unique=True)
    def __str__(self):
        return str(self.background_image)

class ColorPalette(models.Model):
    color_palettes_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    text_color = models.CharField(max_length=25)
    button_color = models.CharField(max_length=25)
    navbar_color = models.CharField(max_length=25)
    icon_color = models.CharField(max_length=25)
    container_color = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "ColorPalettes"

class FontTable(models.Model):
    font_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    font_name = models.CharField(max_length=100)
    def __str__(self):
        return self.font_name

class Setting(models.Model):
    settingid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    background_image =  models.ForeignKey(BackgroundImage, on_delete=models.CASCADE)
    color_palettes =  models.ForeignKey(ColorPalette, on_delete=models.CASCADE)
    font_type = models.ForeignKey(FontTable, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Settings"


