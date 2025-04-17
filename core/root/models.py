from django.db import models
from django.utils.text import slugify


class News(models.Model):
    title = models.CharField(max_length=155, verbose_name='Sarlavha')
    slug = models.SlugField(blank=True, unique=True)
    owner = models.CharField(max_length=155, verbose_name='Owner')
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title  
    
    
class Blog(models.Model):
    title = models.CharField(max_length=155, verbose_name='Sarlavha')
    slug = models.SlugField(blank=True, unique=True)
    owner = models.CharField(max_length=155, verbose_name='Owner')
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title  