from django.conf.urls import url
from app import views


urlpatterns = [
    url(r'^Datos/$', views.Datos_list),
    # url(r'^Datos/(?P<pk>[0-9]+)/$', views.Datos_detail),
]