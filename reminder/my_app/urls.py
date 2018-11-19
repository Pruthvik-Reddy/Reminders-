from django.conf.urls import url
from my_app import views

urlpatterns=[
        url(r'^reminders/',views.reminder,name='reminder'),
        #url(r'^reminders/<int:pk>',views.details,name='details'),
        url(r'^add/',views.add,name="add"),

        url(r'^$',views.index,name='index'),


]