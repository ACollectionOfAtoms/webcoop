from django.conf.urls import url

from . import views

urlpatterns = [
    # /overseer/
    url(r'^$', views.index, name='index'),
]
