from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import MessageView, UserView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = {
    url(r'^messages/$', MessageView.as_view(), name="messages"),
    url(r'^login/', obtain_auth_token),
    url(r'^register', UserView.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
