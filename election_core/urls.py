from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    return redirect('accounts:login')


urlpatterns = [
    path('admin/',      admin.site.urls),
    path('accounts/',   include('accounts.urls',   namespace='accounts')),
    path('elections/',  include('elections.urls',  namespace='elections')),
    path('reports/',    include('reports.urls',    namespace='reports')),
    path('dashboard/',  include('dashboard.urls',  namespace='dashboard')),
    path('',            root_redirect),
]

if settings.DEBUG:
    urlpatterns.append(path('__reload__/', include('django_browser_reload.urls')))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
