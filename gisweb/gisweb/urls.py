"""gisweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from nccu_gis_app.views import index, map, add, login, logout, profileUpdate, error, map_refine, modify, blog, blog_detail, user_blog, add_lonlat, upload_avatar, add_refine
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',index),
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index),
    url(r'^map/$', map),
    url(r'^map_refine/$', map_refine),
    url(r'^add/$',add_refine),
    url(r'^modify/$', modify),
    url(r'^login/$',login),
    url(r'^logout/$',logout),
    url(r'^profileUpdate/$',profileUpdate),
    url(r'^error/$',error),
    url(r'^blog/$',blog),
    url(r'^user_blog/$',user_blog),
    url(r'^blog-detail/(\w+)$',blog_detail),
    url(r'^modify/(\w+)/$',modify),
    url(r'^modify/(\w+)/(\w+)/$',modify),
    url(r'^add_lonlat/$',add_lonlat),
    url(r'^upload_avatar/', upload_avatar), # 上傳頭像
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)