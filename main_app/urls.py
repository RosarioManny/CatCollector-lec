from django.urls import path
from .views import Home, CatList, CatDetail, FeedingListCreate, FeedingDetail, ToyList, ToyDetails

urlpatterns = [
    path("", Home.as_view(), name="Home" ),
    path("cats/", CatList.as_view(), name="Cat-list"),
    path("cats/<int:id>/", CatDetail.as_view(), name="Cat-detail"),
    path('cats/<int:cat_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
	path('cats/<int:cat_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
    path('toys/', ToyList.as_view(), name='Toy-List'),
    path('toys/<int:id>', ToyDetails.as_view(), name='Toy-Details')
]
