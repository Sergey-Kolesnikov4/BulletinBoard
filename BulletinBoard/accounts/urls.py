from django.urls import path
from .views import registration,confirmation,LoginUser,LogoutUser,about
urlpatterns = [
    path('registration', registration, name = 'registration'),
    path('confirmation', confirmation, name = 'confirmation_code'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('about/', about, name='about'),

]