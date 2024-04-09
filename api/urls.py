from django.urls import path
from .views import CrudView,CreateForm,Todo,Detail,UpdatePlace,PersonCreateView,PersonUpdateDeleteView,delete
app_name='api'
urlpatterns = [
    # api
    path('api/',CrudView.as_view(),name='crudview'),
    path('create/', PersonCreateView.as_view()),
    path('api/<int:id>/', PersonUpdateDeleteView.as_view()),
    # 
    path('',Todo.as_view(),name='todo'),
    path('detail/<int:id>/',Detail.as_view(),name='detail'),
    path('person/',CreateForm.as_view(),name='create'),
    path('delete/<int:pk>/',delete,name='delete'),
    path('update/<int:pk>/',UpdatePlace.as_view(),name='update'),
]
