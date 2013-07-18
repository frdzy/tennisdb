from django.conf.urls import patterns, url

from players import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^id/(?P<player_id>\d+)/$', views.player, name='player_by_id'),
)
