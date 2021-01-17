from django.contrib import admin
from django.urls import path
from .views import hello_world_fanction, HelloWorldClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', hello_world_fanction),
    # クラスには.as_view()が必要.クラスからオブジェクトを作成し関数に変える
    path('hello_world2/', HelloWorldClass.as_view()),

]
