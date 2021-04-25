from django.urls import path

from website import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("files/", views.files_view, name="files"),
    path("", views.index_view, name="index")
]
