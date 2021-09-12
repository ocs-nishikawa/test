from django.urls import path,include
from django.contrib import admin

from . import views

app_name = 'e_app'

urlpatterns = [
    path("", views.LineChartsView.as_view(), name="plot", ),

    # ホーム、教室一覧ページ
    path('home/' , views.homepage_view , name = 'home') ,

    # ログイン失敗画面(okでログイン画面へ遷移)
    path('login_failed/' , views.login_failed_view , name = 'login_failed') ,

    path('admin/', admin.site.urls),

    # ログアウト
    path('logout/' , views.logout,name="logout") ,
# のむへ
    path("plot/",views.LineChartsView.as_view(),name="plot"),
    path("setting/",views.SettingView.as_view(),name="setting"),
    path("classroom/",views.ClassroomView.as_view(),name="classroom"),
    path("select/",views.SelectView.as_view(),name="select"),

    # path('', include(('e_app.urls', 'e_app'),namespace='e_app',)),

    ] 
