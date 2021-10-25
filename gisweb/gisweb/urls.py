from django.contrib import admin
from django.conf.urls import url
from nccu_gis_app.views import index, map, add, login, logout, profileUpdate, error, modify, blog, user_blog, vrtest
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',map),
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index),
    url(r'^map/$', map),
    url(r'^add/$',add),
    url(r'^modify/$', modify),
    url(r'^login/$',login),
    url(r'^logout/$',logout),
    url(r'^profileUpdate/$',profileUpdate),
    url(r'^error/$',error),
    url(r'^blog/$',blog),
    url(r'^modify/(\w+)/$',modify),
    url(r'^modify/(\w+)/(\w+)/$',modify),
    url(r'^user_blog/$', user_blog),
    url(r'^vrtest/$',vrtest),
    url(r'^vrtest/(\w+)/$',vrtest),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)