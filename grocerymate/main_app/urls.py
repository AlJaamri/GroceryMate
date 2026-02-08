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
    path('groceries/<int:grocery_id>/add_bought/', views.add_bought, name='add_bought'),
    path('groceries/<int:grocery_id>/apply_coupon/<int:coupon_id>/', views.apply_coupon, name='apply_coupon'),
    path('groceries/<int:grocery_id>/unapply_coupon/<int:coupon_id>/', views.unapply_coupon, name='unapply_coupon'),
    
    path('coupons/', views.CouponList.as_view(), name='coupons_index'),
    path('coupons/<int:pk>/', views.CouponDetail.as_view(), name='coupons_detail'),
    path('coupons/create/', views.CouponCreate.as_view(), name='coupons_create'),
    path('coupons/<int:pk>/update/', views.CouponUpdate.as_view(), name='coupons_update'),
    path('coupons/<int:pk>/delete/', views.CouponDelete.as_view(), name='coupons_delete'),
]
