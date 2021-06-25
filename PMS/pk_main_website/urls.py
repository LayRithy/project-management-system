from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index ,name='index'),
    path('profile/', views.profile, name='profile'),
    path('board/', views.board, name='board'),
    path('task/', views.task_view, name='task'),
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('delete_task/<str:pk>/', views.delete_task, name='delete_task'),
    path('board_detail/<str:pk>/', views.board_detail, name='board_detail'),
    path('board_creation/', views.board_creation, name='board_creation'),
    path('delete_board/<str:pk>/', views.delete_board, name='delete_board'),
    # path('delete_board/', views.delete_board, name='delete_board'),
    path('category/', views.category_view, name='category'),
    path('category_creation/', views.category_creation, name='category_creation'),
    path('category_detail/<str:pk>/', views.category_detail, name='category_detail'),
    path('delete_category/<str:pk>/', views.delete_category, name='delete_category'),

]

