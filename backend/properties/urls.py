from django.urls import path
from .views import PropertyView, PropertyListView


urlpatterns = [
    path('post/', PropertyView.as_view(), name= 'post Property'),
    path("list/", PropertyListView.as_view(), name = "property list" ),
    path("<str:property_id>/", PropertyView.as_view(), name = "individual_property")
]