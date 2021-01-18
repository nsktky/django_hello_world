from django.urls import path
from .views import hello_world_app_view

# プロジェクトで書いたurlパターンを記入するとエラーになる
# NG:app/hello_world_app/ OK:hello_world_app/
urlpatterns = [
    path('hello_world_app/', hello_world_app_view)

]
