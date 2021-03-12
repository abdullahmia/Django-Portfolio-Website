from django.shortcuts import render, redirect
# import Site Setting models
from portfolios.models import EnableSections, Resume, Projects, AboutUs

# import messange and notification from profolio app
from portfolios.models import Contact

# import blog model from blog app
from blog.models import Blog

# import message framework
from django.contrib import messages

# For Authencation
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def admin_login(request):

    if request.session.has_key('login'):
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        get_user = authenticate(username=username, password=password)
        if get_user is not None:
            login(request, get_user)
            request.session['login'] = True
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.WARNING, 'Invalid info')
            return redirect('login')


    return render(request, 'dashboard/login.html')

def admin_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    contacts = Contact.objects.all().order_by('-created_at')
    ctx = {
        'contacts': contacts,
    }
    return render(request, 'dashboard/dashboard.html', ctx)

@login_required(login_url='login')
def site_settings(request):
    if request.method == 'POST':
        header = request.POST.get('header')
        footer = request.POST.get('footer')
        about_me = request.POST.get('about')
        resume = request.POST.get('resume')
        service = request.POST.get('service')
        skill = request.POST.get('skill')
        project = request.POST.get('project')
        loader = request.POST.get('loader')

        setting = EnableSections.objects.get(pk=1)

        setting.header = header
        setting.footer = footer
        setting.loader = loader
        setting.about = about_me
        setting.resume = resume
        setting.service = service
        setting.skill = skill
        setting.projects = project
        setting.save()

    setting = EnableSections.objects.get(pk=1)
    ctx = {
        'settings': setting,
    }
    return render(request, 'dashboard/site_settings.html', ctx)

@login_required(login_url='login')
def all_blog(request):
    live_blogs = Blog.objects.filter(status='Publish')
    drafts = Blog.objects.filter(status='Draft')
    ctx = {
        'live_blogs': live_blogs,
        'drafts': drafts
    }
    return render(request, 'dashboard/all_blog.html', ctx)


def delete_blog(request, id):
    url = request.META.get('HTTP_REFERER')
    del_item = Blog.objects.get(pk=id)
    del_item.delete()
    return redirect(url)

@login_required(login_url='login')
def resume(request):
    resume = Resume.objects.filter(status=True)
    draft = Resume.objects.filter(status=False)
    if request.method == 'POST':
        url = request.META.get('HTTP_REFERER')
        title = request.POST.get('title')
        university = request.POST.get('university')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        status = request.POST.get('status')
        short_des = request.POST.get('s_des')

        add_item = Resume.objects.create(title=title, university=university, starting_time=start_time, ending_time=end_time, status=status, short_description=short_des)
        add_item.save()
        messages.add_message(request, messages.SUCCESS, "Resume has been added")
        return redirect(url)

    ctx = {
        'resume': resume,
        'draft': draft,
    }
    return render(request, 'dashboard/resume.html', ctx)
@login_required(login_url='login')
def add_draft_resume(request, id):
    url = request.META.get('HTTP_REFERER')
    item = Resume.objects.get(pk=id)
    item.status = False
    item.save()
    messages.add_message(request, messages.WARNING, 'Resume add in Draft')
    return redirect(url)

def add_publish_resume(request, id):
    url = request.META.get('HTTP_REFERER')
    item = Resume.objects.get(pk=id)
    item.status = True
    item.save()
    messages.add_message(request, messages.SUCCESS, 'Resume is now Live')
    return redirect(url)

@login_required(login_url='login')
def add_delete_resume(request, id):
    url = request.META.get('HTTP_REFERER')
    item = Resume.objects.get(pk=id)
    item.delete()
    messages.add_message(request, messages.SUCCESS, 'Resume has been deleted')
    return redirect(url)

@login_required(login_url='login')
def projects(request):
    project = Projects.objects.filter(status='Publish')
    draft = Projects.objects.filter(status='Draft')

    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        image = request.FILES['image']
        status = request.POST.get('status')
        live_url = request.POST.get('url')
        url = request.META.get('HTTP_REFERER')

        add_project = Projects.objects.create(title=title, category=category, image=image, status=status, live_link=live_url)
        add_project.save()
        messages.add_message(request, messages.SUCCESS, 'Project has been added..')
        return redirect(url)
    ctx = {
        'projects': project,
        'drafts': draft,
    }
    return render(request, 'dashboard/projects.html', ctx)


@login_required(login_url='login')
def add_draft_project(request, id):
    url = request.META.get('HTTP_REFERER')
    item = Projects.objects.get(pk=id)
    item.status = 'Draft'
    item.save()
    messages.add_message(request, messages.WARNING, 'Projects add in Draft')
    return redirect(url)

def add_publish_project(request, id):
    url = request.META.get('HTTP_REFERER')
    item = Projects.objects.get(pk=id)
    item.status = 'Publish'
    item.save()
    messages.add_message(request, messages.SUCCESS, 'Project is now Live')
    return redirect(url)

@login_required(login_url='login')
def add_delete_project(request, id):
    url = request.META.get('HTTP_REFERER')
    item = Projects.objects.get(pk=id)
    item.delete()
    messages.add_message(request, messages.SUCCESS, 'Project has been deleted')
    return redirect(url)


@login_required(login_url='login')
def aboutus(request):
    data = AboutUs.objects.get(pk=1)

    if request.method == 'POST':
        url = request.META.get('HTTP_REFERER')
        name = request.POST.get('name')
        birthday = request.POST.get('birthday')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        image = request.FILES['image']

        get_data = AboutUs.objects.get(pk=1)
        get_data.name = name
        get_data.birthday = birthday
        get_data.address = address
        get_data.zipcode = zipcode
        get_data.email = email
        get_data.phone = phone
        get_data.image = image
        get_data.save()
        messages.add_message(request, messages.SUCCESS, 'Data Edited')
        return redirect(url)

    ctx = {
        'data': data
    }
    return render(request, 'dashboard/aboutus.html', ctx)


