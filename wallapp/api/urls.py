from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import MessageView

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')), 
    url(r'^messages/$', MessageView.as_view(), name="messages"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
