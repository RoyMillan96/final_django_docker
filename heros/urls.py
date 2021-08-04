from django.urls import path
from heros.views import SuperHeroList, SuperPowerList, SuperHeroDetail, SuperPowerDetail

urlpatterns = [
    path('v1/superheros/', SuperHeroList.as_view(), name="superheroslist"),
    path('v1/superheros/<int:pk>/', SuperHeroDetail.as_view(), name="superherosdetail"),
    path('v1/superpower/', SuperPowerList.as_view(), name="superhpowerlist"),
    path('v1/superpower/<int:pk>/', SuperPowerDetail.as_view(), name="superowerdetail"),
]