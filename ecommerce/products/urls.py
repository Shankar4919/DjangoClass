from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('postProduct', views.post_product_data),
    path('getProduct', views.get_product),
    path('postPerson', views.post_person_data),
    path('postStudent', views.post_student),
    path('getStudent', views.get_student),
    path('updateStudent/<int:student_id>', views.update_student),
    path('deleteStudent/<int:student_id>', views.delete_student),
    path('getPersonMF', views.show_person_mf),
    path('postPersonMF', views.post_person_data),
    path('/deletePersonMF/<int:person_id',views.deletePersonMF)
]