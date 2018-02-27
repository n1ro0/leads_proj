from django.conf.urls import patterns, url


from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.LeadsList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.LeadDetail.as_view(), name='detail'),
    url(r'^create/$', views.LeadCreate.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.LeadUpdate.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.LeadDelete.as_view(), name='delete'),
    url(r'^delete-all/$', views.delete_all, name='delete-all')
)
