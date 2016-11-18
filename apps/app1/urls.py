from django.conf.urls import url
from views import index
from . import views
urlpatterns = [
    url(r'^$', index, name='index2'),
]
