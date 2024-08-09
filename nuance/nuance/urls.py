
# #URL configuration for nuance project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# from django.contrib import admin
# from django.urls import path

from django.contrib import admin
from django.urls import path
from filehandler import views

# different urls to route to corresponding views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_files, name='list_files'),  # Home page lists files
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
    path('update/<int:file_id>/', views.update_file, name='update_file'),
    path('files/', views.list_files, name='list_files'),
    path('files/upload/', views.upload_file, name='upload_file'),
    path('files/<int:file_id>/download/', views.download_file, name='download_file'),
    path('files/<int:file_id>/view/', views.view_file, name='view_file'),
    path('files/<int:file_id>/update/', views.update_file, name='update_file'),
    path('files/<int:file_id>/delete/', views.delete_file, name='delete_file'),
]
