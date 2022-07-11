"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from account.views import LoginUserView, RegisterUserView
from app.views import (
    BranchPostView,
    BranchView,
    EventView,
    OrganisationView,
    PostView,
    UserPostView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", RegisterUserView.as_view(), name="createuser"),
    path("login/", LoginUserView.as_view(), name="authuser"),
    path(
        "organisation/", OrganisationView.as_view(), name="create organisation"
    ),
    path("post/", PostView.as_view(), name="create Post"),
    path("branchpost/", BranchPostView.as_view(), name="create BranchPost"),
    path("branch/", BranchView.as_view(), name="create Branch"),
    path("userpost/", UserPostView.as_view(), name="create UserPost"),
    path("event/", EventView.as_view(), name="create Event"),
]
