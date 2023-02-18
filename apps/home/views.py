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
from dateutil.relativedelta import relativedelta


@login_required(login_url="/login/")
def index(request):
    # today = datetime.today()
    # year = today.year
    # week = today.strftime("%V")
    # visit_this_week = 0
    # visit_last_week = 0
    # product_update = ""
    # best_products = []
    # all = 0
    # all_lead_amount = 0
    # week_update = ""
    # lead_update = ""
    # last_month_amount = 0
    # the_month_before_amount = 0
    # visits = Visit.objects.all()
    # leads = Lead.objects.all()
    # today = datetime.today()
    # last_month = today - relativedelta(months=1)
    # the_month_before = today - relativedelta(months=2)
    # for lead in leads:
    #     all_lead_amount += int(lead.price)
    #     if lead.date.month == last_month.month:
    #         last_month_amount += lead.price
    #     elif lead.date.month == the_month_before.month:
    #         the_month_before_amount += lead.price
    # lead_pount = abs(the_month_before_amount-last_month_amount)/(the_month_before_amount+1)
    # if the_month_before_amount > last_month_amount:
    #     lead_update = "down"
    # else:
    #     lead_update = "up"
    # for visit in visits:
    #     all += visit.count
    #     if int(visit.date.strftime("%V")) == int(int(week)-1) and visit.date.year == year:
    #         visit_this_week += visit.count
    #     elif int(visit.date.strftime("%V")) == int(int(week) - 2) and int(visit.date.year) == int(year):
    #         visit_last_week += visit.count 
    # week_pount = abs(100 -  100 * ((visit_this_week+1)/visit_last_week+1))
    # if visit_this_week > visit_last_week:
    #     week_update = "up"
    # else:
    #     week_update = "down"
    # products = Product.objects.all().order_by('-orders')
    # for product in products[0:4]:
    #     pount = abs(100 - 100 * ((product.orders - product.this_week_orders+1)/(product.orders - product.last_week_orders - product.this_week_orders+1)))
    #     if (product.orders - product.this_week_orders) > (product.orders - product.last_week_orders - product.this_week_orders):
    #         product_update = "up"
    #     else:
    #         product_update = "down"        
    #     prd = {
    #         "id": product.id,
    #         "name": product.name_uz,
    #         "orders": product.orders,
    #         "price": product.price,
    #         "product_update": product_update,
    #         'pount': round(pount,2),
    #         'image': product.image,
    #     }
    #     best_products.append(prd)
    # week_date = today - relativedelta(months=1)
    # last_week_date = today - relativedelta(months=2)
    # leads_last_count = 0
    # leads_before_count = 0
    # ls = []
    # visit = Visit.objects.filter(date=week_date).first()
    # lds = Lead.objects.all()
    # for i in lds:
    #     if i.date.month == week_date.month:
    #         leads_last_count += 1
    #     elif i.date.month == last_week_date.month:
    #         leads_before_count += 1
    # leads_mont_edit = abs(100 -  100 * ((leads_last_count+1)/(leads_before_count+1)))
        
    
    # context = {
    #     'segment': 'index',
    #     'week_pount': round(week_pount,2),
    #     'lead_pount': round(lead_pount,2),
    #     'leads_mont_edit': round(leads_mont_edit, 2),
    #     'week_update': week_update,
    #     'lead_update': lead_update,
    #     'all_visits': all,
    #     'all_lead_amount': all_lead_amount,
    #     'best_products': best_products,
    #     }

    context = {
        
    }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
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
        "segment":"leaders"
    }
    
    html_template =loader.get_template('home/leaders.html')
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

    return render(request,
                'home/document_create.html',
                {'form': form})


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


# def product_by_brand(request, pk):
#     products = Product.objects.filter(brand_id=pk).all()
#     context = {
#         "products": products,
#         "segment":"products"
#     }
    
#     html_template =loader.get_template('home/products.html')
#     return HttpResponse(html_template.render(context, request))


# def product_by_news(request, pk):
#     products = Product.objects.filter(news_id=pk).all()
#     context = {
#         "products": products,
#         "segment":"products"
#     }
    
#     html_template =loader.get_template('home/products.html')
#     return HttpResponse(html_template.render(context, request))


# def color_create(request, pk):
#     if request.method == 'POST':
#         form = ColorForm(request.POST, request.FILES)
#         if form.is_valid():
#             color = form.save()
#             product = Product.objects.get(id=pk)
#             color.product = product
#             color.save()
#             return redirect('product_detail', pk)
#     else:
#         form = ColorForm()

#     return render(request,
#                 'home/color_create.html',
#                 {'form': form})


# class ColorDelete(DeleteView):
#     model = Color
#     fields = '__all__'
#     success_url = reverse_lazy('products')

