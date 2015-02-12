from django.conf.urls import patterns, url
from original import views as original_views
from quick import views as quick_views
from better import views as better_views
from the_way import views as the_way_views


urlpatterns = patterns('',
    # Examples:
    url(r'^$', original_views.HomePageView.as_view(), name='home'),
    url(r'^quick/$', quick_views.HomePageView.as_view(), name='quick_home'),
    url(r'^better/$', better_views.HomePageView.as_view(), name='better_home'),
    url(r'^the_way/$', the_way_views.HomePageView.as_view(), name='the_way_home'),
)
