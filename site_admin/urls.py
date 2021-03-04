from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='login'),
    path('logout', views.admin_logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('site-settings', views.site_settings, name='site_settings'),
    path('all-blog', views.all_blog, name='all_blog'),
    path('delete-blog/<int:id>', views.delete_blog, name='delete_blog'),
    path('resume', views.resume, name='resume'),
    # For Resume
    path('add-draft-resume/<int:id>', views.add_draft_resume, name='add_draft_resume'),
    path('add-publish-resume/<int:id>', views.add_publish_resume, name='add_publish_resume'),
    path('add-delete-resume/<int:id>', views.add_delete_resume, name='add_delete_resume'),
    # For Project Sections
    path('project', views.projects, name='project'),
    path('add-draft-project/<int:id>', views.add_draft_project, name='add_draft_project'),
    path('add-publish-project/<int:id>', views.add_publish_project, name='add_publish_project'),
    path('add-delete-project/<int:id>', views.add_delete_project, name='add_delete_project'),
    # About us section
    path('aboutus', views.aboutus, name='aboutus'),
]