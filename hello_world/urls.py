from django.contrib import admin
from django.urls import path, include
from .views import hello_world_fanction, HelloWorldClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', hello_world_fanction),
    # クラスには.as_view()が必要.クラスからオブジェクトを作成し関数に変える
    path('hello_world2/', HelloWorldClass.as_view()),
    # アプリへリクエストを繋ぎこむ
    # アプリのディレクトリにurls.pyが生成されないため、自分でつくるのが一般的
    path('app/', include('hello_world_app.urls')),

]
