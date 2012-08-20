from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('board.views',
    url(r'^$', 'create_board'),
    url(r'^(?P<board_id>\d+)$', 'board'),
    url(r'^(?P<board_id>\d+)/postits', 'get_postits'),
    url(r'^(?P<board_id>\d+)/postit/new', 'new_postit'),
    url(r'^postit/(?P<postit_id>\d+)/delete', 'delete_postit'),
)