from django.urls import path

from website import views

urlpatterns = [
    path("logout/", views.logout_view, name="logout"),
    path("", views.index_view, name="index")
]
