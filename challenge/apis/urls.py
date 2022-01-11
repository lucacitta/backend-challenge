from django.urls import path

from .api.views import populateApis, findKeyword


urlpatterns = [
    path('populate-apis', populateApis, name='populate-apis'),
    path('keyword', findKeyword, name='keyword')
]