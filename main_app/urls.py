from django.urls import path
from .views import Home, CatList, CatDetail, FeedingListCreate, FeedingDetail

urlpatterns = [
    path("", Home.as_view(), name="Home" ),
    path("cats/", CatList.as_view(), name="Cat-list"),
    path("cats/<int:id>/", CatDetail.as_view(), name="Cat-detail"),
    path('cats/<int:cat_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
	path('cats/<int:cat_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
]
