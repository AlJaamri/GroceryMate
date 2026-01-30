from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guide/', views.guide, name='guide'),
    path('groceries/', views.groceries_index, name='index'),
    path('groceries/<int:grocery_id>/', views.groceries_detail, name='detail'),
    path('groceries/create/', views.GroceryCreate.as_view(), name='groceries_create'),
    path('groceries/<int:pk>/update/', views.GroceryUpdate.as_view(), name='groceries_update'),
    path('groceries/<int:pk>/delete/', views.GroceryDelete.as_view(), name='groceries_delete'),
]
