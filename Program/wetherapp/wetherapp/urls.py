from django.urls import path, include
from wetherprog import views

urlpatterns = [
    path("", views.user),
    path("admin/", views.admin),
    path("autor", views.autor),
    path("add", views.add),
    path("up/<int:id>/", views.up),
    path("dele/<int:id>/", views.dele),
    path("errmsguser/<str:error>/", views.errmsguser),
    path("errmsgadmin/<str:error>/", views.errmsgadmin),
]
