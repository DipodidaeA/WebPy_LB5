from django.urls import path, include
from wetherprog import views

admin_patterns = [
    path("", views.admin),
    path("autor", views.autor),
    path("add", views.add),
    path("up", views.up),
    path("dele", views.dele),
]

urlpatterns = [
    path("", views.user),
    path("admin/", include(admin_patterns)),
]
