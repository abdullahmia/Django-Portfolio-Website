from django.shortcuts import render, HttpResponse, redirect

from .models import SiteSettings, HeroSection, Buttons, AboutUs, Resume, Contact, SkillSection, EnableSections, Projects
from django.db.models import Count
# Import from blog app to blog model
from blog.models import Blog, Category, Comment

# Create your views here.
def index(request):
    setting = SiteSettings.objects.get(pk=1)
    enable_sections = EnableSections.objects.get(pk=1)
    # For Hero Sections
    hero_section = HeroSection.objects.all()[::-1]
    hero_button = []
    for i in hero_section:
        btn = Buttons.objects.filter(slider_id=i.id)
        hero_button.append(btn)

    # For About us sections
    about = AboutUs.objects.filter(status=True).first()

    # Resume Sections
    resumes = Resume.objects.filter(status=True)

    # Blog Sections
    blog = Blog.objects.filter(status='Publish')

    # For Skill Progress Sections
    skill_progress = SkillSection.objects.filter(status='Published')

    # For Projects
    projects = Projects.objects.filter(status='Publish')

    ctx = {
        'setting': setting,
        'enable_sections': enable_sections,
        'hero': hero_section,
        'hero_button': hero_button,
        'about': about,
        'resumes': resumes,
        'blog': blog,
        'skills': skill_progress,
        'projects': projects,

    }
    return render(request, 'index.html', ctx)


def blog_details(request, id):
    setting = SiteSettings.objects.get(pk=1)

    try:
        post = Blog.objects.get(pk=id)
        post.view += 1
        post.save()
    except Exception as e:
        return HttpResponse("<a href='/'>Home</a>")

    categories = Category.objects.filter(status='Publish').annotate(blog_count=Count('blog'))
    for i in categories:
        print("This is blog post count: ", i.blog_count)
    recent_post = Blog.objects.filter(status='Publish')[::-1]
    comments = Comment.objects.filter(post_id=id)
    comment_count = comments.count()


    ctx = {
        'setting': setting,
        'post': post,
        'categories': categories,
        'recent_post': recent_post,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'single.html', ctx)


def contact(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        add_contact = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        add_contact.save()
        return redirect(url)

    return redirect(url)