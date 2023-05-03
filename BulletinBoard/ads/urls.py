from django.urls import path
from .views import AdsList,AdsUpdate,AdsCreate,AdsDelete,AdvertisementDetail,ResponsesCreate,ResponsesList,ResponsesDelete,ResponseUpdate

urlpatterns = [
    path('', AdsList.as_view(), name = 'ads_list'),
    path('<int:pk>',AdvertisementDetail.as_view(),name = 'advertisement_detail'),
    path('create/',AdsCreate.as_view(), name = 'ads_create'),
    path('<int:pk>/update/',AdsUpdate.as_view(), name = 'ads_update'),
    path('<int:pk>/delete/',AdsDelete.as_view(), name = 'ads_delete'),
    path('<int:pk>/delete/',AdsDelete.as_view(), name = 'ads_delete'),
    path('<int:pk>/create_response', ResponsesCreate.as_view(), name='create_response'),
    path('my_responses', ResponsesList.as_view(), name='my_responses'),
    path('my_responses/<int:pk>/delete/', ResponsesDelete.as_view(), name='delete_responses'),
    path('my_responses/<int:pk>/acceptance/', ResponseUpdate.as_view(), name='update_responses')

    ]


