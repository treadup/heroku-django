from django.urls import path

from website import views

urlpatterns = [
    path("", views.index_view, name="index")
]
