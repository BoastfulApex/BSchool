from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, render
from apps.school.forms import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from datetime import datetime, timedelta


@login_required(login_url="/login/")
def index(request):

    context = {
        
    }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:

        load_template = request.path.split('/')[-1]
        print(request.path.split('/')[-1])

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def sliders(request):
    
    sliders = Slider.objects.all()
    context = {
        "sliders": sliders,
        "segment":"sliders"
    }
    
    html_template = loader.get_template('home/sliders.html')
    return HttpResponse(html_template.render(context, request))

    
def slider_detail(request, pk):
    slider = Slider.objects.get(id=pk)

    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES, instance=slider)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sliders')
    else:
        form = SliderForm(instance=slider)

    return render(request,
                'home/slider_update.html',
                {'form': form, 'slider': slider})

    
def slider_create(request):
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sliders')
    else:
        form = SliderForm()

    return render(request,
                'home/slider_create.html',
                {'form': form})


class SliderDelete(DeleteView):
    model = Slider
    fields = '__all__'
    success_url = reverse_lazy('sliders')
  

def partners(request):
    
    partners = Partners.objects.all()
    context = {
        "partners": partners,
        "segment":"partners"
    }
    
    html_template =loader.get_template('home/partners.html')
    return HttpResponse(html_template.render(context, request))


def partner_create(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('partners')
    else:
        form = PartnerForm()

    return render(request,
                'home/partner_create.html',
                {'form': form})

    
def partner_detail(request, pk):
    partner = Partners.objects.get(id=pk)

    if request.method == 'POST':
        form = PartnerForm(request.POST, request.FILES, instance=partner)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('partners')
    else:
        form = PartnerForm(instance=partner)

    return render(request,
                'home/partner_update.html',
                {'form': form, 'partner': partner})


class partnerDelete(DeleteView):
    model = Partners
    fields = '__all__'
    success_url = reverse_lazy('partners')


def categories(request):
    
    categories = CourseCategory.objects.all()
    context = {
        "categories": categories,
        "segment":"categories"
    }
    
    html_template =loader.get_template('home/categories.html')
    return HttpResponse(html_template.render(context, request))


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()

    return render(request,
                'home/category_create.html',
                {'form': form})

    
def category_detail(request, pk):
    category = CourseCategory.objects.get(id=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)

    return render(request,
                'home/category_update.html',
                {'form': form, 'category': category})


class CategoryDelete(DeleteView):
    model = CourseCategory
    fields = '__all__'
    success_url = reverse_lazy('categories')


def courses(request):
    
    courses = Course.objects.all()
    context = {
        "courses": courses,
        "segment":"courses"
    }
    
    html_template =loader.get_template('home/courses.html')
    return HttpResponse(html_template.render(context, request))


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            print("AAAAAAAAAAA")
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()

    return render(request,
                'home/course_create.html',
                {'form': form})

    
def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm(instance=course)

    return render(request,
                'home/course_update.html',
                {'form': form, 'course': course})


class courseDelete(DeleteView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('courses')


def news(request):
    
    news = News.objects.all()
    context = {
        "news": news,
        "segment":"news"
    }
    
    html_template =loader.get_template('home/news.html')
    return HttpResponse(html_template.render(context, request))

    
def news_detail(request, pk):
    news = News.objects.get(id=pk)

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewsForm(instance=news)

    return render(request,
                'home/news_update.html',
                {'form': form, 'news': news})


def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewsForm()

    return render(request,
                'home/news_create.html',
                {'form': form})


class NewsDelete(DeleteView):
    model = News
    fields = '__all__'
    success_url = reverse_lazy('news')


def leaders(request):
    leaders = Leadership.objects.all()
    context = {
        "leaders": leaders,
        "segment": "leaders"
    }

    html_template = loader.get_template('home/leaders.html')
    return HttpResponse(html_template.render(context, request))


def leaders_detail(request, pk):
    leaders = Leadership.objects.get(id=pk)

    if request.method == 'POST':
        form = LeadershipForm(request.POST, request.FILES, instance=leaders)
        if form.is_valid():
            form.save()
            return redirect('leaders')
    else:
        form = LeadershipForm(instance=leaders)

    return render(request,
                  'home/leaders_update.html',
                  {'form': form, 'leaders': leaders})


def leaders_create(request):
    if request.method == 'POST':
        form = LeadershipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('leaders')
    else:
        form = LeadershipForm()

    return render(request,
                  'home/leaders_create.html',
                  {'form': form})


class leadersDelete(DeleteView):
    model = Leadership
    fields = '__all__'
    success_url = reverse_lazy('leaders')


def course_owners(request):
    owners = CourseOwners.objects.all()
    context = {
        "owners": owners,
        "segment": "owners"
    }

    html_template = loader.get_template('home/owners.html')
    return HttpResponse(html_template.render(context, request))


def owners_detail(request, pk):
    owner = CourseOwners.objects.get(id=pk)

    if request.method == 'POST':
        form = CourseOwnerForm(request.POST, request.FILES, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owners')
    else:
        form = CourseOwnerForm(instance=leaders)

    return render(request,
                  'home/owner_update.html',
                  {'form': form, 'owners': leaders})


def owners_create(request):
    if request.method == 'POST':

        form = CourseOwnerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('owners')
    else:
        form = CourseOwnerForm()

    return render(request,
                  'home/owners_create.html',
                  {'form': form})


class ownerDelete(DeleteView):
    model = CourseOwners
    fields = '__all__'
    success_url = reverse_lazy('owners')


def documents(request):
    
    documents = Documents.objects.all()
    context = {
        "documents": documents,
        "segment":"documents"
    }
    
    html_template =loader.get_template('home/documents.html')
    return HttpResponse(html_template.render(context, request))

    
def documents_detail(request, pk):
    documents = Documents.objects.get(id=pk)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=documents)
        if form.is_valid():
            form.save()
            return redirect('documents')
    else:
        form = DocumentForm(instance=documents)

    return render(request,
                'home/document_update.html',
                {'form': form, 'document': documents})


def documents_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('documents')
    else:
        form = DocumentForm()

    return render(request, 'home/document_create.html', {'form': form})


class documentsDelete(DeleteView):
    model = Documents
    fields = '__all__'
    success_url = reverse_lazy('documents')


def course_by_category(request, pk):
    products = Course.objects.filter(category_id=pk).all()
    context = {
        "products": products,
        "segment":"products"
    }
    
    html_template =loader.get_template('home/courses.html')
    return HttpResponse(html_template.render(context, request))


def photo_gallery(request):
    photos = PhotoGallery.objects.all()
    context = {
        "photos": photos,
        "segment": "photos"
    }

    html_template = loader.get_template('home/photos.html')
    return HttpResponse(html_template.render(context, request))


def photos_detail(request, pk):
    photos = PhotoGallery.objects.get(id=pk)

    if request.method == 'POST':
        form = PhotoGalleryForm(request.POST, request.FILES, instance=photos)
        if form.is_valid():
            form.save()
            return redirect('photos')
    else:
        form = PhotoGalleryForm(instance=photos)

    return render(request,
                  'home/photos_update.html',
                  {'form': form, 'photos': photos})


def photos_create(request):
    if request.method == 'POST':
        form = PhotoGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photos')
    else:
        form = PhotoGalleryForm()

    return render(request,
                  'home/photos_create.html',
                  {'form': form})


class PhotoDelete(DeleteView):
    model = PhotoGallery
    fields = '__all__'
    success_url = reverse_lazy('photos')


def video_gallery(request):
    videos = VideoGallery.objects.all()
    context = {
        "videos": videos,
        "segment": "videos"
    }

    html_template = loader.get_template('home/videos.html')
    return HttpResponse(html_template.render(context, request))


def videos_detail(request, pk):
    videos = VideoGallery.objects.get(id=pk)

    if request.method == 'POST':
        form = VideoGalleryForm(request.POST, request.FILES, instance=videos)
        if form.is_valid():
            form.save()
            return redirect('videos')
    else:
        form = VideoGalleryForm(instance=videos)

    return render(request,
                  'home/videos_update.html',
                  {'form': form, 'videos': videos, 'segment': 'videos'})


def videos_create(request):
    if request.method == 'POST':
        form = VideoGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('videos')
    else:
        form = VideoGalleryForm()

    return render(request,
                  'home/videos_create.html',
                  {'form': form, 'sigment': 'videos'})


class VideoDelete(DeleteView):
    model = VideoGallery
    fields = '__all__'
    success_url = reverse_lazy('videos')
