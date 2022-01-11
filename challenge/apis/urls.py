from django.urls import path

from .api.views import populateApis, findKeyword, orderedList,  CategoryApiView


urlpatterns = [
    path('populate-apis/', populateApis, name='populate-apis'),
    path('keyword/', findKeyword, name='keyword'),
    path('category/',CategoryApiView.as_view(), name='category'),
    path('ordered-list/',orderedList, name='ordered'),
    path('item/',CategoryApiView.as_view(), name='item'),
]