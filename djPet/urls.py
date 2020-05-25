"""djPet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler400, handler403, handler404, handler500
from django.urls import include, path, re_path
from .views import (
    home_page,
    contact_page,
    about_page,
    new_pricer_page,
    easter_egg_page,
    # page_not_found
)

urlpatterns = [
    path('home/', home_page),
    path('about/', about_page),
    re_path(r'^contacts?/$', contact_page),
    # path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('pricer/', new_pricer_page),
    path('easter_egg/', easter_egg_page),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handler400 = 'djPet.views.page_not_found'
# handler403 = 'djPet.views.page_not_found'
# handler404 = 'djPet.views.page_not_found'
# handler500 = 'djPet.views.error_500'
