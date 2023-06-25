from django.urls import path
from. import views



urlpatterns = [
    
    path('',views.index ),
    path('about/', views.about ),
    path('insert', views.insert),
    path('update/<id>', views.update),
    path('delete/<id>', views.delete),

]    