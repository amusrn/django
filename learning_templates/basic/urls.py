from django.conf.urls import url
from basic import views

app_name='basic'

urlpatterns = [
    url(r'^other/$',views.other,name='other'),
    url(r'^relative/$',views.relative,name='relative')

]
