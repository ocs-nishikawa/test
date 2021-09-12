from django.http import HttpResponse
from django.shortcuts import render
# ログイン時のみ表示可能な機能
from django.contrib.auth.decorators import login_required
# ログイン、ログアウトに必要
from django.contrib.auth import authenticate , login , logout
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
# のむへの
from django.views.generic import TemplateView
import plotly.graph_objects as go
from .models import Userid_Table, Classroom_Table, Co2_Table
# import requests
from django.shortcuts import redirect
from django.urls import reverse_lazy


@login_required
def homepage_view(request , *args , **kwargs):
    print(args , kwargs)
    print(request.user)
    return render(request , "home.html" , {})

def login_view(request , *args , **kwargs):
    if request.method == 'POST':
        if 'login_button' in request.POST:
            userID = request.POST.get("userID")
            passw = request.POST.get("password")
            user = authenticate(username=userID, password=passw)

            if user:
                #ユーザーアクティベート判定
                if user.is_active:
                    # ログイン
                    login(request,user)
                    # ホームページ遷移
                # return render(request , "select.html" , {})
                return redirect("/select/")
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        else:
            # ユーザー認証失敗
            return HttpResponse("ログインIDまたはパスが間違ってます")
    else:
        return render (request , "e_app/login.html" , {} )


def login_failed_view(requst , *args , **kwargs):
    return render(requst , "e_app/login_failed.html" , {}) 

@login_required
def logout(request):
    # return HttpResponseRedirect(reverse("login"))
    return redirect("/")

def login_failed_view(requst , *args , **kwargs):
    return render(requst , "e_app/login_failed.html" , {}) 


# のむへ

#変数初期値
a = 100

m2x = 0
m3x = 0



# Create your views here.
def line_charts(requests):
    
    L1 = [x for x in range(0, a, 1)]
    L2 = [x for x in range(0, a, 1)]

    if requests.session.get('classroomID') is None and requests.session.get('start_time') is None and requests.session.get('end_time') is None:
        q1 = Co2_Table.objects.values_list('date', flat=True)
        q2 = Co2_Table.objects.values_list('CO2conce', flat=True)
    elif requests.session.get('start_time') is None and requests.session.get('end_time') is None:
        abc = requests.session.get('classroomID')
        q1 = Co2_Table.objects.values_list('date', flat=True).filter(classroom_id = abc)
        q2 = Co2_Table.objects.values_list('CO2conce', flat=True).filter(classroom_id = abc)
    else:
        q1 = Co2_Table.objects.values_list('date',flat=True).filter(date__lte=requests.session.get('start_time'),date__gte=requests.session.get('end_time'),classroom_name=requests.session.get('classroomID'))
        q2 = Co2_Table.objects.values_list('CO2conce',flat=True).filter(date__lte=requests.session.get('start_time'),date__gte=requests.session.get('end_time'),classroom_name=requests.session.get('classroomID'))

    n = 0
    for w1 in q1:
        L1[n] = w1
        n = n + 1

    m = 0
    for w2 in q2:
        L2[m] = w2
        m = m + 1

    fig = go.Figure(
        go.Scatter(x=L1[0:n:1],y=L2[0:m:1]),layout=go.Layout(width=1000,height=500)
    )
    return fig.to_html(include_plotlyjs=False)

class LineChartsView(TemplateView):
    template_name = "e_app/plot.html"

    def get_context_data(self, **kwargs):
        ctx = super(LineChartsView, self).get_context_data(**kwargs)
        ctx["plot"] = line_charts(self.request)
        return ctx

class SettingView(TemplateView): #設定画面
    template_name = "e_app/setting.html"

    def post(self, requests):

        if requests.method == 'POST':
            if 'btnsave' in requests.POST:
                requests.session['ppm'] = requests.POST['Ppm']
                requests.session['start_time'] = requests.POST['StartTime']
                requests.session['end_time'] = requests.POST['EndTime']
                return render(requests,"e_app/classroom_register.html",{})

class ClassroomView(TemplateView): #教室登録画面
    template_name = "e_app/classroom_register.html"

    def post(self, requests): #
        if requests.method == 'POST':
            if 'btnregister' in requests.POST: #ボタンを押されたときデータベースに教室名と機器番号を登録する
                saveclass = Classroom_Table(classroom_name=requests.POST['classroomName'], user_id = 1, equipment_number=requests.POST['machineNumber'])
                saveclass.save()
                return render(requests , "e_app/setting.html" ,{})

class SelectView(TemplateView): #教室選択画面
    template_name = "e_app/select.html"

    def get_context_data(self, **kwargs): #基準値を超えない教室を得る
        m2 = 0
        m3 = 0

        L3 = [x for x in range(0, a, 1)]
        L4 = [x for x in range(0, a, 1)]

        if 'ppm' in self.request.session:
            classroomID = Co2_Table.objects.values_list('classroom_id', flat=True).filter(CO2conce__lte = self.request.session.get('ppm'))
            for clid in classroomID:
                if 'classroom_id' == clid:
                    classsroomname = Classroom_Table.objects.values_list('classroom_name', flat=True).filter('classroom_id' == clid)
                    L3[m2] = classsroomname
                    m2 = m2 + 1
                else:
                    m2 = m2 + 1
        else:
            classsroomname = Classroom_Table.objects.values_list('classroom_name',flat=True)
            for clname in classsroomname:
                L3[m2] = clname
                m2 = m2 + 1

        print(L3)

        if 'ppm' in self.request.session: #基準値を超える教室を得る
            warnclassroomID = Co2_Table.objects.values_list('classroom_id',flat=True).filter(CO2conce__gt =  self.request.session.get('ppm'))
            for clid in warnclassroomID:
                if 'warnclassroom_id' == clid:
                    warnclasssroomname = Classroom_Table.objects.values_list('classroom_name',flat=True).filter('classroom_id' == clid)
                    L4[m3] = warnclasssroomname
                    m3 = m3 + 1
                else:
                    m3 = m3 + 1

        ctx = super().get_context_data(**kwargs)
        ctx['params']  = L3[0:m2:1] #基準値を超えない教室を得る
        if 'ppm' in self.request.session:
            ctx['params2']  = L4[0:m3:1] #基準値を超える教室を得る
        return ctx

    def post(self, request):
        btnname = tuple(request.POST.keys())[1]
        if request.method == 'POST':
            if btnname in request.POST:
                request.session['classroomID'] = btnname #押されたボタンの教室名から教室IDを得る
                return redirect("/plot/")