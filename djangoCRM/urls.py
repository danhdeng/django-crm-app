"""djangoCRM URL Configuration

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
from django.conf import urls, settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

"import function base view from leads"
from leads.views import landing_page, landingpageview, SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include("leads.urls", namespace='leads')),
    path('', landingpageview.as_view(), name='landing-page'),
    path('login/',LoginView.as_view(), name='login-page'),
    path('logout/',LogoutView.as_view(), name='logout'),
     path('signup/',SignupView.as_view(), name='signup'),
    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    # path('', landing_page, name='landing-page'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    