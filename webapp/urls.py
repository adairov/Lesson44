from django.urls import path

from webapp.views import index_view, results_view

urlpatterns = [
    path("", index_view),
    path("results/", results_view)
]