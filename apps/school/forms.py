from django import forms
from .models import *


class SliderForm(forms.ModelForm):
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Slider nomi uz",
                "class": "form-control"
            }
        ))

    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Slider nomi ru",
                "class": "form-control"
            }
        ))
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Slider nomi en",
                "class": "form-control"
            }
        ))
    image = forms.ImageField(
      widget=forms.FileInput()
    )
    description_uz = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "description_uz",
                "class": "form-control"
            }
        ))

    description_ru = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "description_ru",
                "class": "form-control"
            }
        ))
    description_en = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "description_en",
                "class": "form-control"
            }
        ))
    class Meta:
        model = Slider
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Category name uz",
                "class": "form-control"
            }
        ))

    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Category name  ru",
                "class": "form-control"
            }
        ))
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Category name en",
                "class": "form-control"
            }
        ))
    image = forms.ImageField(
      widget=forms.FileInput()
    )

    class Meta:
        model = CourseCategory
        fields = "__all__"


class PartnerForm(forms.ModelForm):
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Hamkor name uz",
                "class": "form-control"
            }
        ),
        required=False,
        )

    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Hamkor name  ru",
                "class": "form-control"
            }
        ),
        required=False,
        )
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Hamkor name en",
                "class": "form-control"
            }
        ),
        required=False,
        )
    image = forms.ImageField(
      widget=forms.FileInput()
    )
    
    class Meta:
        model = Partners
        fields = "__all__"


# class CategoryForm(forms.ModelForm):
#     name_uz = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Category name uz",
#                 "class": "form-control"
#             }
#         ))

#     name_ru = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Category name  ru",
#                 "class": "form-control"
#             }
#         ))
#     name_en = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Category name en",
#                 "class": "form-control"
#             }
#         ))
#     image = forms.ImageField(
#       widget=forms.FileInput()
#     )
#     class Meta:
#         model = Category
#         fields = "__all__"


class DocumentForm(forms.ModelForm):
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Hujjat nomi uz",
                "class": "form-control"
            }
        ),
        required=False,
        )

    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Hujjat nomi  ru",
                "class": "form-control"
            }
        ),
        required=False,
        )
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Hujjat nomi en",
                "class": "form-control"
            }
        ),
        required=False,
        )
    file = forms.FileField(
      widget=forms.FileInput()
    )
    
    class Meta:
        model = Documents
        fields = "__all__"


class CourseForm(forms.ModelForm):
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Kurs nomi uz",
                "class": "form-control"
            }
        ),
        required=False,
        )
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Kurs nomi en",
                "class": "form-control"
            }
        ),
        required=False,
        )
    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Kurs nomi  ru",
                "class": "form-control"
            }
        ),
        required=False,
        )
    description_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Kurs izohi uz",
                "class": "form-control"
            }
        ),
        required=False,
        )
    description_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Kurs izohi ru",
                "class": "form-control"
            }
        ),
        required=False,
        )
    description_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Kurs izohi en",
                "class": "form-control"
            }
        ),
        required=False,
        )
    category = forms.ModelChoiceField(
        widget=forms.Select(),
        queryset=CourseCategory.objects.all())

    image = forms.ImageField(
      widget=forms.FileInput()
    )
    class Meta:
        model = Course
        fields = ["name_uz", "name_ru", "name_en", "description_uz", "description_ru", "description_en", "category", "image"]


class NewsForm(forms.ModelForm):

    Media = (
        ("media", 'Matbuot xizmati'),
        ("news", 'Yangilik')
    )


    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Kurs nomi uz",
                "class": "form-control"
            }
        ),
        required=False,
        )
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Kurs nomi en",
                "class": "form-control"
            }
        ),
        required=False,
        )
    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Kurs nomi  ru",
                "class": "form-control"
            }
        ),
        required=False,
        )
    text_uz = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Yangilik matni uz",
                "class": "form-control"
            }
        ),
        required=False,
        )
    text_ru = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Yangilik matni ru",
                "class": "form-control"
            }
        ),
        required=False,
        )
    text_en = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Yangilik matni en",
                "class": "form-control"
            }
        ),
        required=False,
        )
    media = forms.ChoiceField(
        
        choices = Media,
        )
    photo = forms.ImageField(
      widget=forms.FileInput()
    )
    class Meta:
        model = News
        fields = ["name_uz", "name_ru", "name_en", "text_uz", "text_ru", "text_en", "media", "photo"]


class LeadershipForm(forms.ModelForm):
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ism En",
                "class": "form-control"
            }
        ))
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ism Uz",
                "class": "form-control"
            }
        ))
    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ism Ru",
                "class": "form-control"
            }
        ))
    position_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Lavozim uz",
                "class": "form-control"
            }
        ),
        required=False,
        )
    position_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Lavozim ru",
                "class": "form-control"
            }
        ),
        required=False,
        )
    position_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Lavozim en",
                "class": "form-control"
            }
        ),
        required=False,
        )
    type = forms.ChoiceField(
        choices=Leadership.EMPLOYEE
    )

    image = forms.ImageField(
      widget=forms.FileInput()
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Telefon",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Leadership
        fields = "__all__"


class CourseOwnerForm(forms.ModelForm):
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ism En",
                "class": "form-control"
            }
        ))
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ism Uz",
                "class": "form-control"
            }
        ))
    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ism Ru",
                "class": "form-control"
            }
        ))
    position_uz = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Yangilik matni uz",
                "class": "form-control"
            }
        ),
        required=False,
        )
    position_ru = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Yangilik matni ru",
                "class": "form-control"
            }
        ),
        required=False,
        )
    position_en = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Yangilik matni en",
                "class": "form-control"
            }
        ),
        required=False,
        )
    image = forms.ImageField(
      widget=forms.FileInput()
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Telefon",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Leadership
        fields = "__all__"


class PhotoGalleryForm(forms.ModelForm):
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nomi En",
                "class": "form-control"
            }
        ))
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nomi Uz",
                "class": "form-control"
            }
        ))
    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nomi Ru",
                "class": "form-control"
            }
        ))
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
            }
        ))
    image1 = forms.ImageField(
      widget=forms.FileInput(),
      required=False,
    )

    image2 = forms.ImageField(
      widget=forms.FileInput(),
      required=False,
    )

    image3 = forms.ImageField(
      widget=forms.FileInput(),
      required=False,
    )

    image4 = forms.ImageField(
      widget=forms.FileInput(),
      required=False,
    )

    image5 = forms.ImageField(
      widget=forms.FileInput(),
      required=False,
    )

    image6 = forms.ImageField(
      widget=forms.FileInput(),
      required=False,
    )

    class Meta:
        model = PhotoGallery
        fields = "__all__"


class VideoGalleryForm(forms.ModelForm):
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nomi En",
                "class": "form-control"
            }
        ))
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nomi Uz",
                "class": "form-control"
            }
        ))
    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nomi Ru",
                "class": "form-control"
            }
        ))
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
            }
        ))
    image1 = forms.ImageField(
      widget=forms.FileInput(),
      required=False,
    )

    image2 = forms.ImageField(
      widget=forms.FileInput(),
      required=False,
    )

    image3 = forms.ImageField(
      widget=forms.FileInput(),
      required=False,
    )

    image4 = forms.ImageField(
      widget=forms.FileInput(),
      required=False,
    )

    image5 = forms.ImageField(
      widget=forms.FileInput(),
      required=False,
    )

    image6 = forms.ImageField(
      widget=forms.FileInput(),
      required=False,
    )

    class Meta:
        model = VideoGallery
        fields = "__all__"

