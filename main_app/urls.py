from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="Home" ),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
    path("cats/", CatList.as_view(), name="Cat-list"),
    path("cats/<int:id>/", CatDetail.as_view(), name="Cat-detail"),
    path('cats/<int:cat_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
	path('cats/<int:cat_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
    path('toys/', ToyList.as_view(), name='Toy-List'),
    path('toys/<int:id>', ToyDetails.as_view(), name='Toy-Details'),
    path('cats/<int:cat_id>/add_toy/<int:toy_id>/', AddToyToCat.as_view(), name='add-toy-to-cat'),
]
