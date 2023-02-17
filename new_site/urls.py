from django.contrib import admin
from django.urls import path
from animals.views import animal_list_view, animal_detail_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('animals/', animal_list_view),
    path('animal/<int:animal_pk>', animal_detail_view),
]
