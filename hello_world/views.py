from django.http import HttpResponse
from django.views.generic import TemplateView

# function based viewでの作成。httpレスポンスをurls.pyで受け取って、この関数にrequestオブジェクトを渡している
# 渡されたrequestオブジェクトに対し、httpresponseでオブジェクトをブラウザに返す
# functionベースビューで作成すると、自分でコードを組み立てる必要があるが、細かい調整等がしやすいし分かりやすい
def hello_world_fanction(request):
    returned_object = HttpResponse('<h1>hello world</h1>')
    return returned_object

# class based viewでの作成。必要なクラスを承継して使用。今回はTemplateViewを承継
# 簡単に作れるが、細かい調整はできない。何やってるかは分かりづらい
# template_nameにhtmlを指定することで、htmlを呼び出す
# htmlはsettings.py内のDIRに記載した場所に作成する
class HelloWorldClass(TemplateView):
    template_name = 'hello.html'