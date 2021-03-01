from django.contrib import admin
from .models import SiteSettings, Buttons, HeroSection, AboutUs, Resume, Contact

class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'logo_text', 'loader']
    list_editable = ['loader']

admin.site.register(SiteSettings)

admin.site.register(Buttons)
class InlineButtons(admin.TabularInline):
    model = Buttons
    extra = 1


# HeroSection
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'created_at']
    inlines = [InlineButtons]


admin.site.register(HeroSection, HeroSectionAdmin)

# AboutUs

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'status']
    list_editable = ['status']

admin.site.register(AboutUs, AboutUsAdmin)



# For Resume

class ResumeAdmin(admin.ModelAdmin):
    list_display = ['title', 'university', 'created_at', 'status']
    list_editable = ['status']
    list_per_page = 10

admin.site.register(Resume, ResumeAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']
    list_per_page = 20

admin.site.register(Contact, ContactAdmin)