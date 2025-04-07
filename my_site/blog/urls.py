from django.urls import path
from . import views

urlpatterns = [
    path("", views.default_page, name="default-page"),
    path("posts", views.portifolio_names, name="portifolio-names"),
    path("posts/<slug>", views.portifolio_details, name="portifolio-details") # posts/my-first-page
]
