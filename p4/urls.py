from django.contrib import admin
from django.urls import include, path

# from p4.ahjk.draw import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('draw/', include('draw.urls')),
#     path('edit/text/', views.edit_text, name='edit_text'),
#     path('draw/', include('edit_text.urls')),
]
