from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about-us/', about, name='about'),
    path('announcement/', announcement, name='announcement'),
    path('login/', login, name='login'),
    path('add_page/', add_page, name='add_page'),
    path('category/<int:cat_id>/', show_category, name='category')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)