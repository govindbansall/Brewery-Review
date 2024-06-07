"""
URL configuration for brewery_review project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from breweries import views as brewery_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', brewery_views.signup_view, name='signup'),
    path('login/', brewery_views.login_view, name='login'),
    path('search/', brewery_views.search_view, name='search'),
    path('brewery/<int:brewery_id>/', brewery_views.brewery_detail_view, name='brewery_detail'),
    path('brewery/<int:brewery_id>/add_review/', brewery_views.add_review_view, name='add_review'),
]