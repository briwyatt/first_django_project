from django.conf.urls import url

from . import views

app_name = 'history'

urlpatterns = [
    url(r'^artist_list/', include('polls.urls')),
    url(r'^artist_list/artist_details', admin.site.urls),
]