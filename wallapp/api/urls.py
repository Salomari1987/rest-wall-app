from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import MessageView

urlpatterns = {
    url(r'^messages/$', MessageView.as_view(), name="messages"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
