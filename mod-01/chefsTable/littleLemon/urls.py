from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home),
    path('ml', views.menuList),
    path('getuser/<name>/<int:id>', views.pathview),
    path('getuserq/', views.qryview),
    path('form', views.formview),
    re_path(r'^menu_item/(\d+)/$', views.repath)
]