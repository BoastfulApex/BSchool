from django.db import models


class Slider(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    @property
    def PhotoURL(self):
        try:
            return self.image.url
        except:
            return ''  


class News(models.Model):
    class Media(models.TextChoices):
        MEDIA = "media", 'Matbuot xizmati'
        NEWS = "News", 'Yangilik'

    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    text_uz = models.TextField(max_length=5000, null=True, blank=True)
    text_ru = models.TextField(max_length=5000, null=True, blank=True)
    text_en = models.TextField(max_length=5000, null=True, blank=True)
    media_type = models.TextField(default=Media.NEWS, choices=Media.choices)
    photo = models.ImageField(null=True)
    date = models.DateField(auto_now_add=False, null=True)    

    @property
    def PhotoURL(self):
        try:
            return self.image.url
        except:
            return ''  


class CourseCategory(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name_uz

    @property
    def PhotoURL(self):
        try:
            return self.image.url
        except:
            return ''


class Course(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)
    top = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name_uz
    
    @property
    def PhotoURL(self):
        if self.image:
            return self.image.url
        else:
            return ''


class Partners(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name_uz

    @property
    def PhotoURL(self):
        if self.image:
            return self.image.url
        else:
            return ''


class Leadership(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    position_uz = models.CharField(max_length=200, null=True, blank=True)
    position_ru = models.CharField(max_length=200, null=True, blank=True)
    position_en = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name_uz

    @property
    def PhotoURL(self):
        if self.image:
            return self.image.url
        else:
            return ''


class Documents(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name_uz

    @property
    def FileURL(self):
        if self.file:
            return self.file.url
        else:
            return ''


    
class About(models.Model):
    about_uz = models.TextField(max_length=5000, null=True, blank=True)
    about_ru = models.TextField(max_length=5000, null=True, blank=True)
    about_en = models.TextField(max_length=5000, null=True, blank=True)
