from django.urls.conf import include
from product.views import login_failed_view , login_view , homepage_view
from django.contrib import admin
from django.urls import path , include

from product import views

urlpatterns = [
    # path ('' , views.homepage_view , name = 'home') , 
    # path('' . views.sensors)

    # ログイン画面
    path ('' , views.login_view , name = 'login' ) , 

    # ホーム、教室一覧ページ
    path('home/' , views.homepage_view , name = 'home') ,

    # ログイン失敗画面(okでログイン画面へ遷移)
    path('login_failed/' , views.login_failed_view , name = 'login_failed') ,


    # path('test/' , views.test_view , name = 'test') , 

    path('admin/', admin.site.urls),

    # ログアウト
    path('logout/' , views.logout,name="logout") ,

]
