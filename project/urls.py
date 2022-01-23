
from django.contrib import admin
from django.conf.urls import include, url
from app import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.Home, name='home'),
    url(r'^app/', include('app.urls', namespace='geeks'))
]
