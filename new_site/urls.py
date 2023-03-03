from django.contrib import admin
from django.urls import path
from animals.views import animal_list_view, animal_detail_view, img_view, about_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('animals/', animal_list_view, name="animal_list"),
    path('animal/<int:animal_pk>', animal_detail_view),
    path('', img_view, name='img'),
    path('about/', about_view, name="about")
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
