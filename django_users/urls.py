"""django_users URL Configuration

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
import json

from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.urls import path


def user_groups(request):
    user_and_group_ids = []
    for user in User.objects.all():
        user_and_group_ids.append({user.username: [g.id for g in user.groups.all()]})
    return HttpResponse(json.dumps(user_and_group_ids))

def add_user_group(request, user_id: int, group_id):
    User.objects.get(user_id).groups.add(Group.objects.get(group_id))
    return HttpResponse('{"ok": true}')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_groups/', user_groups),
    path('add_user_group/<user_id>/<group_id>', add_user_group),
]