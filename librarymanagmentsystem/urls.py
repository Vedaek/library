import imp
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('std/',include("library.urls")),
    path('book/',include("library.urls")),
    path('',include("library.urls")),
    path("login/",auth_views.LoginView.as_view(template_name="library/login.html")),
    path("logout/",auth_views.LogoutView.as_view())

]

if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)