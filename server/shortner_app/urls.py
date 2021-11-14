from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('short-url', views.generate_shorter_url),
    path("u/<str:slugs>", views.url_redirect)
]

handler404 = "shortner_app.views.page_not_found_view"