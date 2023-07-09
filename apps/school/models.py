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


class CourseOwners(models.Model):
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


class PhotoGallery(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    image6 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name_uz

    @property
    def PhotoURL1(self):
        if self.image1:
            return self.image1.url
        else:
            return ''

    @property
    def PhotoURL2(self):
        if self.image2:
            return self.image2.url
        else:
            return ''

    @property
    def PhotoURL3(self):
        if self.image3:
            return self.image3.url
        else:
            return ''

    @property
    def PhotoURL4(self):
        if self.image4:
            return self.image4.url
        else:
            return ''

    @property
    def PhotoURL5(self):
        if self.image5:
            return self.image5.url
        else:
            return ''

    @property
    def PhotoURL6(self):
        if self.image6:
            return self.image6.url
        else:
            return ''


class VideoGallery(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True)
    video1 = models.FileField(null=True, blank=True)
    video2 = models.FileField(null=True, blank=True)
    video3 = models.FileField(null=True, blank=True)
    video4 = models.FileField(null=True, blank=True)
    video5 = models.FileField(null=True, blank=True)
    video6 = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name_uz

    @property
    def VideoURL1(self):
        if self.video1:
            return self.video1.url
        else:
            return ''

    @property
    def VideoURL2(self):
        if self.video2:
            return self.video2.url
        else:
            return ''

    @property
    def VideoURL3(self):
        if self.video3:
            return self.video3.url
        else:
            return ''

    @property
    def VideoURL4(self):
        if self.video4:
            return self.video4.url
        else:
            return ''

    @property
    def VideoURL5(self):
        if self.video5:
            return self.video5.url
        else:
            return ''

    @property
    def VideoURL6(self):
        if self.video6:
            return self.video6.url
        else:
            return ''
