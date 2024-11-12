from django.urls import path
from .views import Home, CatList, CatDetail

urlpatterns = [
    path("", Home.as_view(), name="Home" ),
    path("cats/", CatList.as_view(), name="Cat-list"),
    path("cats/<int:id>/", CatDetail.as_view(), name="Cat-detail"),
]
