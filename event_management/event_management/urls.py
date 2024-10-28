"""
URL configuration for event_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from events.views import event_list, add_event, edit_event, delete_event, event_detail, location_comments
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', event_list, name='event_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add/', add_event, name='add_event'),
    path('edit/<int:pk>/', edit_event, name='edit_event'),
    path('delete/<int:pk>/', delete_event, name='delete_event'),
    path('event/<int:pk>/', event_detail, name='event_detail'),
    path('location/<int:location_id>/comments/', location_comments, name='location_comments'),
]
