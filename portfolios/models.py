from django.db import models


class SiteSettings(models.Model):
    loader_status = (
        ('On', 'On'),
        ('Off', 'Off'),
    )
    site_title = models.CharField(max_length=200)
    site_logo = models.ImageField(upload_to='logos', blank=True)
    logo_text = models.CharField(max_length=50, blank=True)
    favicon = models.ImageField(upload_to='favicons', blank=True)
    cpy_text = models.CharField(max_length=1000, blank=True)
    loader = models.CharField(choices=loader_status, max_length=5, default=loader_status[0][0])


    def __str__(self):
        return self.site_title


class EnableSections(models.Model):
    status = (
        ('Show', 'Show'),
        ('Hide', 'Hide'),
    )
    
    header = models.CharField(max_length=5, choices=status, default='Shwo')
    footer = models.CharField(max_length=5, choices=status, default='Show')
    about = models.CharField(max_length=5, choices=status, default='show', blank=False)
    resume = models.CharField(max_length=5, choices=status, default='Show')
    service = models.CharField(max_length=5, choices=status, default='Show')
    skill = models.CharField(max_length=5, choices=status, default='Show')
    projects = models.CharField(max_length=5, choices=status, default='Show')
    blog = models.CharField(max_length=5, choices=status, default='Show')
    footer_section = models.CharField(max_length=5, choices=status, default='Show')
    contact = models.CharField(max_length=5, choices=status, default='Show')
    loader = models.CharField(max_length=5, choices=status, default='Show')
    

    def __str__(self):
        return self.about


class HeroSection(models.Model):
    greeting_text = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='slider_image', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Buttons(models.Model):
    status = (
        ('primary', 'primary'),
        ('secondary', 'secondary'),
        ('success', 'success'),
        ('danger', 'danger'),
        ('warning', 'warning'),
        ('info', 'info'),
        ('light', 'light'),
        ('dark', 'dark'),
    )
    slider = models.ForeignKey(HeroSection, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    url = models.URLField(max_length=1000)
    status = models.CharField(choices=status, max_length=20, blank=True)

    def __str__(self):
        return self.text




class AboutUs(models.Model):
    short_description = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.PositiveIntegerField()
    total_project = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to="about", blank=True)

    def __str__(self):
        return self.name



class Resume(models.Model):
    starting_time = models.DateField()
    ending_time = models.DateField()
    title = models.CharField(max_length=25)
    university = models.CharField(max_length=255)
    short_description = models.CharField(max_length=180)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    def get_starting_year(self):
        return self.starting_time.year

    def get_ending_year(self):
        return self.ending_time.year



# For Contact us Sections
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SkillSection(models.Model):
    status = (
        ('Published', 'Published'),
        ('Draft', 'Draft'),
    )
    name = models.CharField(max_length=255, blank=False)
    value = models.PositiveBigIntegerField(default=0, blank=False)
    status = models.CharField(max_length=10, choices=status, default='Published')

    def __str__(self):
        return self.name

class Projects(models.Model):
    status = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
    )
    title = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Projects')
    status = models.CharField(max_length=10, choices=status, default='Publish')
    created_at = models.DateTimeField(auto_now_add=True)
    live_link = models.URLField(blank=True)

    def __str__(self):
        return self.title