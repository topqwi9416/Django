from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainMMI.views import *
from mainMMI.views import edit_characteristic_document

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainMMI, name='main'),
    path('register/', register, name='register'),
    path('login/', loginf, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),

    path('create-practice/', create_practice_document, name='create_practice'),
    path('create-characteristic/', create_characteristic_document, name='create_characteristic'),

    path('practice/<int:doc_id>/', view_practice_document, name='view_practice'),
    path('practice/edit/<int:doc_id>/', edit_practice_document, name='edit_practice'),
    path('practice/delete/<int:doc_id>/', delete_practice_document, name='delete_practice'),
    path('characteristic/<int:doc_id>/', view_characteristic_document, name='view_characteristic'),

    path('practice/<int:doc_id>/download/', download_attestat, name='download_attestat'),
    path('characteristic/<int:doc_id>/download/', download_harakteristika, name='download_harakteristika'),
    path('characteristic/edit/<int:doc_id>/', edit_characteristic_document, name='edit_characteristic'),
    path('characteristic/delete/<int:doc_id>/', delete_characteristic_document, name='delete_characteristic'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
