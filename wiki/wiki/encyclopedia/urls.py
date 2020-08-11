from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_page", views.new_page, name="new_page"),
    path("random_page", views.random_page, name="random_page"),
    path("save_edit/<str:title>", views.save_edit, name="save_edit"),
    path("edit_page/<str:title>", views.edit_page, name="edit_page"),
    path("search_results", views.get_name, name="search_results"),
    path("<str:name>", views.load_page, name="load_page"),

]
