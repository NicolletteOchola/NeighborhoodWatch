from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^neighborhood/(\d+)', views.my_area, name='hood'),
    url(r'^neighborhood/(\d+)/join/$', views.join, name='join'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^new/business$', views.new_business, name='new-business')
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
