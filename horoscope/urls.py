from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('type', views.get_type_info),
    path('type/<str:element>', views.get_element_info, name='horoscope+type'),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),
]