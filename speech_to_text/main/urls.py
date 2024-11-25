from django.urls import path

from .views import text_create_view
from .views import text_delete_view
from .views import text_list_view
from .views import text_update_view

app_name = "main"
urlpatterns = [
    path("", view=text_list_view, name="list"),
    path("add", view=text_create_view, name="add"),
    path("<int:pk>", view=text_update_view, name="update"),
    path("<int:pk>/delete/", view=text_delete_view, name="delete"),
]
