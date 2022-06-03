from django.contrib import admin
from django.urls import include, re_path
from nccu_gis_app.views import index, map, add, login, logout, profileUpdate, error, modify, blog, user_blog, vrtest
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$',map),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^index/$', index),
    re_path(r'^map/$', map),
    re_path(r'^add/$',add),
    re_path(r'^modify/$', modify),
    re_path(r'^login/$',login),
    re_path(r'^logout/$',logout),
    re_path(r'^profileUpdate/$',profileUpdate),
    re_path(r'^error/$',error),
    re_path(r'^blog/$',blog),
    re_path(r'^modify/(\w+)/$',modify),
    re_path(r'^modify/(\w+)/(\w+)/$',modify),
    re_path(r'^user_blog/$', user_blog),
    re_path(r'^vrtest/$',vrtest),
    re_path(r'^vrtest/(\w+)/$',vrtest),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)