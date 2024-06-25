from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('brands/', views.brands, name='brands'),
    path('catalog/', views.product_list, name='product_list'),
    path('brands/', views.brands, name='brands'),
    path('contacts/', views.contacts, name='contacts'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_page'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)