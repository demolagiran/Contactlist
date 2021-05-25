from django.urls import path
from . import views

urlpatterns = [
    path('', views.allContacts , name = 'allContacts'),
    path('viewcontacts', views.viewContacts , name = 'viewContacts'),
    path('delete_contact/<int:pk>', views.deleteContact, name = 'deleteContact'),
    path('update_contact/<int:pk>', views.updateContact, name = 'updateContact')
]
