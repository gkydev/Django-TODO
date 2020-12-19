from django.urls import path
from .views import registerPage, loginPage, logoutUser

urlpatterns = [
    path('login/', loginPage),
    path('register/', registerPage),
    path('logout/', logoutUser)
]
