from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index' ),
    url(r'^CreatePacient/$',views.CreatePacient, name='CreatePacient' ),
    url(r'^NumberSession/$',views.NumberSession, name='NumberSession' ),
    url(r'^CreateMedicine/$',views.CreateMedicine, name='CreateMedicine' ),

]
