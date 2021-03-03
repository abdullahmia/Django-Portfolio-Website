from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blog-details/<int:id>', views.blog_details, name='blog_details'),
    path('contact-message', views.contact, name='contact_message'),
]