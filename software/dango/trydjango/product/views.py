from django.http import HttpResponse
from django.shortcuts import render
# ログイン時のみ表示可能な機能
from django.contrib.auth.decorators import login_required
# ログイン、ログアウトに必要
from django.contrib.auth import authenticate , login , logout
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse


@login_required
def homepage_view(request , *args , **kwargs):
    print(args , kwargs)
    print(request.user)
    return render(request , "home.html" , {})

def login_view(request , *args , **kwargs):
    # print(args , kwargs)
    if request.method == 'POST':
<<<<<<< HEAD
        if 'login_button' in request.POST:
            userID = request.POST.get("userID")
            passw = request.POST.get("password")
            user = authenticate(username=userID, password=passw)

<<<<<<< HEAD
<<<<<<< HEAD

def line_charts():
    fig = go.Figure(
        go.Scatter(x=[1, 2, 3], y=[3, 5, 2]), layout=go.Layout(width=400, height=400)
    )
    return fig.to_html(include_plotlyjs=False)  # ❷


class LineChartsView(TemplateView):  # ❶
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        context = super(LineChartsView, self).get_context_data(**kwargs)
        context["plot"] = line_charts()  # ❸
        return context
=======
def login_failed_view(requst , *args , **kwargs):
    return render(requst , "login_failed.html" , {}) 
>>>>>>> 23a3db8789cf24d29afcb6380cdf22c747b7b33b
=======
            if user:
                #ユーザーアクティベート判定
                if user.is_active:
                    # ログイン
                    login(request,user)
=======

        userID = request.POST.get("userID")
        passw = request.POST.get("password")
        user = authenticate(username=userID, password=passw)

        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
<<<<<<< HEAD
>>>>>>> 1c8743a7142cafc076542d802c05d2fe243ab0b8
=======
>>>>>>> 0cbf54544e50ce053bb2100ed26b9c389bd57e52
>>>>>>> 7cf493dc47a53789be76bb5c85f01cab315e59d5
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        else:
            # ユーザー認証失敗
            return HttpResponse("ログインIDまたはパスが間違ってます")
    else:
        return render (request , "login.html" , {} )

@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def login_failed_view(requst , *args , **kwargs):
    return render(requst , "login_failed.html" , {}) 

# def test_view(request , )
>>>>>>> e664fe184c3ddcae5d294c76753e7b93e1f338bf
