from django.shortcuts import render
from django.http import HttpResponse
from dash_app.models import Registration, Reward_Sli, Registration_KR, Reward_KR, VDP_Sli_KR
from django.db.models import Sum
from django_pivot.pivot import pivot
import datetime, calendar
from .forms import DateFilterForm
# Create your views here.


#helper function
def get_friday():
    
    lastFriday = datetime.date.today()
    oneday = datetime.timedelta(days=1)

    while lastFriday.weekday() != calendar.FRIDAY:
        lastFriday -= oneday

    return (lastFriday)


def index(request):
    return render(request, 'dash_app/landing.html')


def sli_dash(request):
    form = DateFilterForm(request.GET or None)
    if form.is_valid():
    #if request.GET.get("from_date") is not None and request.GET.get("to_date") is not None:
        req_d1 = datetime.datetime.strptime(request.GET.get("from_date"), "%m/%d/%Y").strftime("%Y-%m-%d")
        req_d2 = datetime.datetime.strptime(request.GET.get("to_date"), "%m/%d/%Y").strftime("%Y-%m-%d")
        d2 = req_d1
        d1 = req_d2 
    else:
        d1 = get_friday()
        d2 = d1 - datetime.timedelta(days=7)

    reg_data = Registration.objects.filter(event_type='ActivateVMembership', date_time__range=(d2,d1)).order_by('date_time')
    can_data = Registration.objects.filter(event_type='CancelVMembership', date_time__range=(d2,d1)).order_by('date_time')
    assessment = Registration.objects.values('event_type').annotate(Sum('count')).filter(event_type__in=['VHRAssmntCompleted', 
    'VNAAssmntCompleted', 
    'NonsmokersDeclrtn',
    'MWBAssmntCompleted',
    'VHCAssmntCompleted',
    'SV Document Uploads',
    'PapSmear',
    'Mammogram',], )

    daily_assess = Registration.objects.filter(event_type__in=['VHRAssmntCompleted', 
    'VNAAssmntCompleted', 
    'NonsmokersDeclrtn',
    'MWBAssmntCompleted',
    'VHCAssmntCompleted',
    'SV Document Uploads',
    'PapSmear',
    'Mammogram',], 
    date_time__range=(d2,d1)).order_by('date_time')
    daily_assess_pivot = pivot(daily_assess, 'date_time', 'event_type', 'count')
    daily_assess_formatted =[]
    for d in daily_assess_pivot:
        d= dict(((k.replace(' ',''),v) for k,v in d.items()))
        daily_assess_formatted.append(d)
    #VDP Data
    VDP_data = VDP_Sli_KR.objects.values("partner_system_name").annotate(Sum('count')).filter(name='SLI Japan')
    # Reward Data
    reward_sli_data = Reward_Sli.objects.all()
    # print(reward_sli_data)
    reward_sli_pivot = pivot(reward_sli_data, 'awarded_on', 'reward','count')
    
    reward_sli_formatted = []
    for d in reward_sli_pivot:
        d= dict(((k.replace(' ',''),v) for k,v in d.items()))
        d = dict(((k.replace('(',''),v) for k,v in d.items()))
        d = dict(((k.replace(')',''),v) for k,v in d.items()))
        reward_sli_formatted.append(d)

    return render(request, 'dash_app/sli_dash.html', {'reg_data': reg_data, 
    'can_data': can_data, 
    'assess_data': assessment,
    'daily_assess': daily_assess_formatted,
    'reward_sli':reward_sli_formatted,
    'vdp' : VDP_data,
    'filter_form': DateFilterForm})


def kr_dash(request):
    form = DateFilterForm(request.GET or None)
    if form.is_valid():
    #if request.GET.get("from_date") is not None and request.GET.get("to_date") is not None:
        req_d1 = datetime.datetime.strptime(request.GET.get("from_date"), "%m/%d/%Y").strftime("%Y-%m-%d")
        req_d2 = datetime.datetime.strptime(request.GET.get("to_date"), "%m/%d/%Y").strftime("%Y-%m-%d")
        d2 = req_d1
        d1 = req_d2 
    else:
        d1 = get_friday()
        d2 = d1 - datetime.timedelta(days=7)

    reg_data = Registration_KR.objects.filter(event_type='ActivateVMembership', date_time__range=(d2,d1)).order_by('date_time')
    can_data = Registration_KR.objects.filter(event_type='CancelVMembership', date_time__range=(d2,d1)).order_by('date_time')
    assessment = Registration_KR.objects.values('event_type').annotate(Sum('count')).filter(event_type__in=['VHRAssmntCompleted', 
    'VNAAssmntCompleted', 
    'NonsmokersDeclrtn',
    'MWBAssmntCompleted',
    'VHCAssmntCompleted',
    'SV Document Uploads',
    'PapSmear',
    'Mammogram',], )

    daily_assess = Registration_KR.objects.filter(event_type__in=['VHRAssmntCompleted', 
    'VNAAssmntCompleted', 
    'NonsmokersDeclrtn',
    'MWBAssmntCompleted',
    'VHCAssmntCompleted',
    'SV Document Uploads',
    'PapSmear',
    'Mammogram',], 
    date_time__range=(d2,d1)).order_by('date_time')
    daily_assess_pivot = pivot(daily_assess, 'date_time', 'event_type', 'count')
    daily_assess_formatted =[]
    for d in daily_assess_pivot:
        d= dict(((k.replace(' ',''),v) for k,v in d.items()))
        daily_assess_formatted.append(d)
    #VDP Data
    VDP_data = VDP_Sli_KR.objects.values("partner_system_name").annotate(Sum('count')).filter(name='AIA Republic of Korea')
    # Reward Data
    reward_kr_data = Reward_KR.objects.all()
    # print(reward_sli_data)
    reward_kr_pivot = pivot(reward_kr_data, 'awarded_on', 'reward','count')
    
    reward_kr_formatted = []
    for d in reward_kr_pivot:
        d= dict(((k.replace(' ',''),v) for k,v in d.items()))
        d = dict(((k.replace('(',''),v) for k,v in d.items()))
        d = dict(((k.replace(')',''),v) for k,v in d.items()))
        reward_kr_formatted.append(d)
    
    # print(reward_kr_formatted)

    return render(request, 'dash_app/kr_dash.html', {'reg_data': reg_data, 
    'can_data': can_data, 
    'assess_data': assessment,
    'daily_assess': daily_assess_formatted,
    'reward_kr':reward_kr_formatted,
    'vdp' : VDP_data,
    'filter_form': DateFilterForm})


