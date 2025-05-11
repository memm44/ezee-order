from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('mypanel-1a63587f/', admin.site.urls),
]
if not getattr(settings, "TESTING", False):
    import debug_toolbar
    from django.urls import path, include
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
def custom_500_view(request):
    return render(request, '500.html', status=500)

handler404 = custom_404_view
handler500 = custom_500_view