from django.urls import path
from .views import index,create,update,delete,get
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path("",index,name="index"),
    path("create/<str:type_of_data>",csrf_exempt(create),name="create"),
    path("get/<str:type_of_data>/<int:id>",get,name="get"),
    path("update/<str:type_of_data>/<int:id>",csrf_exempt(update),name="update"),
    path("delete/<str:type_of_data>/<int:id>",delete,name="delete")
]