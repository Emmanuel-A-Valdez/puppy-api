from django.urls import path
from . import views

urlpatterns = [
    path("", views.puppy_api_overview, name="puppy-api-overview"),
    path("puppy-list/", views.puppy_list, name="puppy-list"),
    path("puppy-detail/<int:pk>/", views.puppy_detail, name="puppy-detail"),
    path("puppy-create/", views.puppy_create, name="puppy-create"),
    path("puppy-update/<int:pk>/", views.puppy_update, name="puppy-update"),
    path("puppy-delete/<int:pk>/", views.puppy_delete, name="puppy-delete"),
]
