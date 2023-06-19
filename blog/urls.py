from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('patient/', views.patient_view_blog_posts, name='patient_view_blog_posts'),
    path('doctor/', views.doctor_view_blog_posts, name='doctor_view_blog_posts'),
    path('blog/post/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
]
