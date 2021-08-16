from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from .views import ParticipantView, NotificationView, PingView, installation, uninstallation
from .views import download#, download_one, download_two, download_three, download_four, download_five, download_six, \
#                    download_seven, download_eight, download_nine, download_ten, download_eleven, download_tweleve

urlpatterns = [
    url(r'^installation/$', installation),
    url(r'^uninstallation/$', uninstallation),
    path('post/participant/', ParticipantView.as_view()),
    path('post/notification/', NotificationView.as_view()),
    path('post/ping/', PingView.as_view()),

    url(r'download/(?P<path>.*)$', download, {'document_root': settings.STATIC_ROOT}),
    # url(r'^f97c5d/$', download_one),
    """
    url(r'^b8a9f7/$', download_two),
    url(r'^35d6d3/$', download_three),
    url(r'^8cbad9/$', download_four),
    url(r'^30056e/$', download_five),
    url(r'^f52b5e/$', download_six),
    url(r'^bb3aec/$', download_seven),
    url(r'^24d27c/$', download_eight),
    url(r'^c785e1/$', download_nine),
    url(r'^b1b9a9/$', download_ten),
    url(r'^9c8454/$', download_eleven),
    url(r'^91ca74/$', download_tweleve),
    """
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)