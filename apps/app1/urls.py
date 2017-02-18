from django.conf.urls import url
from views import index, add_trip, create_destination, show_destinations, join_trip
urlpatterns = [
    url(r'^$', index, name='travels'),
    url(r'^add_trip$', add_trip, name='add_trip'),
    url(r'^destination/(?P<dest_id>\d+)', show_destinations, name='destination'),
    url(r'^create_destination$', create_destination, name='create'),
    url(r'^join_trip',join_trip, name = "join")
]
