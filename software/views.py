from .models import Userid_Table, Classroom_Table, Co2_Table
from django.views.generic import TemplateView
import plotly.graph_objects as go
# import requests
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls import reverse_lazy

a = 100
n = 0
m = 0
m2 = 0
m3 = 0

L3 = [x for x in range(0, a, 1)]
L4 = [x for x in range(0, a, 1)]

# Create your views here.
def line_charts(requests):
    L1 = [x for x in range(0, a, 1)]
    L2 = [x for x in range(0, a, 1)]

    if requests.session['classroomID'] is None and requests.session['start_time'] is None and requests.session['end_time']:
        q1 = Co2_Table.objects.values_list('date', flat=True)
        q2 = Co2_Table.objects.values_list('CO2conce', flat=True)
    elif requests.session['classroomID'] is not None:
        q1 = Co2_Table.objects.values_list('date','classroom_id' == requests.session['classroomID'], flat=True)
        q2 = Co2_Table.objects.values_list('CO2conce','classroom_id' == requests.session['classroomID'], flat=True)
    else:
        q1 = Co2_Table.objects.values_list('date', 'date' >= requests.session['start_time'], 'date' <= requests.session['end_time'], 'classroom_id' == requests.session['classroomID'], flat=True)
        q2 = Co2_Table.objects.values_list('CO2conce', 'date' >= requests.session['start_time'], 'date' <= requests.session['end_time'],'classroom_id' == requests.session['classroomID'], flat=True)

    for w1 in q1:
        L1[n] = w1
        n = n + 1

    for w2 in q2:
        L2[m] = w2
        m = m + 1

    fig = go.Figure(
        go.Scatter(x=L1[0:n:1], y=L2[0:m:1]), layout=go.Layout(width=1000, height=500)
    )
    return fig.to_html(include_plotlyjs=False)

class LineChartsView(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        context = super(LineChartsView, self).get_context_data(**kwargs)
        context["plot"] = line_charts(self.request)
        return context

class SettingView(TemplateView): #設定画面
    template_name = "setting.html"

    def post(self, requests):
        if requests.method == 'POST':
            if 'btnsave' in requests.POST:
                requests.session['ppm'] = requests.POST['Ppm']
                requests.session['start_time'] = requests.POST['StartTime']
                requests.session['end_time'] = requests.POST['EndTime']
                return render(requests , "classroom_register.html" ,{})

class ClassroomView(TemplateView): #教室登録画面
    template_name = "classroom_register.html"

    def post(self, requests):
        if requests.method == 'POST':
            if 'btnregister' in requests.POST:
                requests.session['classroom_name'] = requests.POST['classroomName']
                requests.session['machine_number'] = requests.POST['machineNumber']
                return render(requests , "setting.html" ,{})

class SelectView(TemplateView):
    template_name = "select.html"

    def get_context_data(self, **kwargs):
        if 'ppm' in requests.session:
            classroomID = Co2_Table.objects.values_list('classroom_id', 'CO2conce' >= requests.session['ppm'], flat=True)
            for clid in classroomID:
                if 'classroom_id' == clid:
                    classsroomname = Classroom_Table.objects.values_list('classroom_name', 'classroom_id' == clid, flat=True)
                    L3[m2] = classsroomname
                    m2 = m2 + 1
                else:
                    m2 = m2 + 1
        else:
            classsroomname = Classroom_Table.objects.values_list('classroom_name', flat=True)
            for clname in classsroomname:
                L3[m2] = clname
                m2 = m2 + 1

        ctx = super().get_context_data(**kwargs)
        ctx['params']  = L3[0:m2:1]
        return ctx

    def get_context_data2(self, **kwargs):
        if 'ppm' in requests.session:
            warnclassroomID = Co2_Table.objects.values_list('classroom_id', 'CO2conce' < requests.session['ppm'], flat=True)
            for clid in warnclassroomID:
                if 'warnclassroom_id' == clid:
                    warnclasssroomname = Classroom_Table.objects.values_list('classroom_name', 'classroom_id' == clid, flat=True)
                    L4[m3] = warnclasssroomname
                    m3 = m3 + 1
                else:
                    m3 = m3 + 1

        if 'ppm' in requests.session:
            ctx2 = super().get_context_data2(**kwargs)
            ctx2['params2']  = L4[0:m3:1]
            return ctx2

    def post(self, requests):
        if requests.method == 'POST':
            if '{{ value }}' in requests.POST:
                requests.session['classroomID'] = Classroom_Table.objects.values_list('classroom_name' == '{{ value }}', flat=True)
                return render(requests , "plot.html" ,{})