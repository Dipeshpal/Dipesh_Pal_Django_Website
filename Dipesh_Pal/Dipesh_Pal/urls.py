from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from home.sitemaps import PostSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'posts': PostSitemap,
    'static': StaticViewSitemap(['sitemap',
                                 'home:list',
                                 'home:News', 'home:android', 'home:PC', 'home:Others', 'home:create',
                                 'about:about',
                                 'disclaimer:disclaimer',
                                 'contact_us:contact_us',
                                 'videos:videos_page',
                                 ]),
}


urlpatterns = [
    url('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^admin/', admin.site.urls),
    url('accounts/', include('accounts.urls'), name='accounts'),
    url(r'^', include('home.urls'), name='home'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^about/', include('about.urls'), name='about'),
    url(r'^disclaimer/', include('disclaimer.urls'), name='disclaimer'),
    url(r'^privacy_policy/', include('privacy_policy.urls')),
    url(r'^contact_us/', include('contact_us.urls'), name='contact_us'),
    url(r'^videos/', include('videos.urls'), name='videos'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
