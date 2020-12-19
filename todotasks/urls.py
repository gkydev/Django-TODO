from django.urls import path
from .views import index, home, add_list, show_lists, test, update_task, delete_task, delete_list

urlpatterns = [
    path('', index),
    path('home/', home),
    path('add_list/', add_list),
    path('show_lists/', show_lists),
    path('test/', test),
    path('update_task/', update_task),
    path('delete_task/<str:tid>', delete_task),
    path('delete_list/<str:lid>', delete_list)
]