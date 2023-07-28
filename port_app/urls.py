from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('links/', views.links_view, name='links'),
    path('work_history/', views.work_history_view, name='work_history_view'),
    path('education/', views.education_view, name='education_view'),
    path('certifications/', views.certifications_view, name='certifications_view'),
    path('skills/', views.skills_view, name='skills_view'),
    path('projects/', views.projects_view, name='projects_view'),
    path('references/', views.references_view, name='references_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('blog/', views.blog_view, name='blog_view'),
    path('testing/', views.testing_view, name='testing_view'),
]