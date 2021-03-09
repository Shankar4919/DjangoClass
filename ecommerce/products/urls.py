from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index),
    path('postProduct', views.post_product_data),
    path('getProduct', views.get_product),
    path('postPerson', views.post_person_data),
    path('postStudent', views.post_student),
    path('getStudent', views.get_student),
    path('updateStudent/<int:student_id>', views.update_student),
    path('deleteStudent/<int:student_id>', views.delete_student),
    path('getPersonMF', views.get_person_mf),
    path('postPersonMF', views.post_person_mf),
    path('deletePersonMF/<int:person_id>', views.delete_person_mf),
    path('updatePersonMF/<int:person_id>', views.update_person_mf),
    path('postFile',views.post_file),
    path('getFile',views.get_file),
    path('updateFile/<int:file_id>', views.update_file),
    path('deleteFile/<int:file_id>', views.delete_file),
    path('postFileMF', views.post_file_mf),
    path('getFileMF', views.get_file_mf),
    path('deleteFileMF/<int:file_id>', views.delete_file_mf),
    path('updateFileMF/<int:file_id>', views.update_file_mf)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)