from django.conf.urls import include
from django.conf.urls.defaults import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from board.views import PostitList, PostitDetail, LineList, LineDetail

urlpatterns = patterns('board.views',
    url(r'^$', 'home'),
    url(r'^new$', 'create_board'),
    url(r'^subscribe', 'subscribe'),
    #API
    url(r'^api/boards/(?P<board_id>\d+)/postits/$', PostitList.as_view(), name='postit-list'),
    url(r'^api/boards/(?P<board_id>\d+)/postits/(?P<pk>\d+)$', PostitDetail.as_view(), name='postit-detail'),
    url(r'^api/boards/(?P<board_id>\d+)/lines/$', LineList.as_view(), name='line-list'),
    url(r'^api/boards/(?P<board_id>\d+)/lines/(?P<pk>\d+)$', LineDetail.as_view(), name='line-detail'),
    url(r'^(?P<board_hash>\w+)$', 'board'),
    url(r'^(?P<board_id>\d+)/postit/new', 'new_postit'),
    url(r'^(?P<board_id>\d+)/authorize', 'authorize_board', name="board-authorization"),
    url(r'^(?P<board_id>\d+)/lines/clear', 'clear_lines'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])


urlpatterns += patterns('',
    url(r'^api/$', 'board.views.api_root'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
