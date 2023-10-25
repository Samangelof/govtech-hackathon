from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="home"),
    path('registration/', RegistrationStudent.as_view(), name='registration'),
    path('authorization/', AuthorizationStudent.as_view(), name='auth'),
    path('logout/', logout_user, name='logout'),
    path('thanks/', thanks, name='thanks'),
    path('personal/', personal_kab, name='personal_kab'),
    path('administration_user/', administration, name='administration'),
    path('schools/', schools, name='schools')
]
