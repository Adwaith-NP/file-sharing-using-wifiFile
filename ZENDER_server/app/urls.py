from django.urls import path
from . import views

urlpatterns = [
    path("authentication/",views.auth,name="authentication"),
    path("getCsrfToken/",views.getCsrfToken,name="getCsrfToken"),
]