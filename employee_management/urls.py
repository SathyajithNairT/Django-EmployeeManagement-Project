from django.urls import path
from . import views 


urlpatterns = [
    path('', views.registration, name = 'registration'),
    path('manage/', views.manage, name = 'manage'),
    path('view/<int:emp_id>', views.view, name = 'view'),
    path('edit/<int:emp_id>', views.edit, name = 'edit'),
    path('delete/<int:emp_id>', views.delete, name = 'delete')
]