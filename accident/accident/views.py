from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse
import requests

def index(request):
    return render(request,'index.html',{'list':InfSpeedBump.objects.all().order_by('-id')})


# def get_infra(request):
#     infra_name = request.GET('InfSpeedBump')
#     return 0

def graph_infra(request):
    infra = InfSpeedBump.objects.all().order_by('-id')
    # for inf in infra:
    #     print(inf)
    return render(request,'1_page.html')

def infra_data(request):
    infra_type = request.GET['infra']
    lst = []
    lst_year = []
    cnt_17,cnt_18,cnt_19,cnt_20 = 0,0,0,0
    if infra_type == 'InfSpeedBump':
        infra = InfSpeedBump.objects.all().order_by('-id')
    elif infra_type == 'InfSmartCross':
        infra = InfSmartCross.objects.all().order_by('-id')
    elif infra_type == 'InfSmartLamp':
        infra = InfSmartLamp.objects.all().order_by('-id')
    elif infra_type == 'InfYellowcarpet':
        infra = InfYellowcarpet.objects.all().order_by('-id')
    elif infra_type == 'InfUnCamera':
        infra = InfUnCamera.objects.all().order_by('-id')
    elif infra_type == 'InfChildZone':
        infra = InfChildZone.objects.all().order_by('-id')
    for i in infra:
        lst.append(i.year_code)
        # print(type(i.year_code))
        # print(i.year_code)
        if i.year_code == 17:
            cnt_17 += 1
        elif i.year_code == 18:
            cnt_18 += 1
        elif i.year_code == 19:
            cnt_19 += 1
        elif i.year_code == 20:
            cnt_20 += 1
        # print(infra)
        lst = set(lst)
        lst = list(lst)
        # print(lst_year)
        # print(lst)
        # print(infra)
        json_dict = {'17': cnt_17, '18': cnt_18, '19': cnt_19, '20': cnt_20}
        # print(json_dict)
    return JsonResponse(json_dict)


def all_infra(request):
    lst = []
    lst_obj = []
    tmp = {}
    name_lst = ['infra_sp','infra_smcro','infra_smlap','infra_yel','infra_cam','infra_chzone']
    cnt_17,cnt_18,cnt_19,cnt_20 = 0,0,0,0
    infra_sp = InfSpeedBump.objects.all().order_by('-id')
    infra_smcro = InfSmartCross.objects.all().order_by('-id')
    infra_smlap = InfSmartLamp.objects.all().order_by('-id')
    infra_yel = InfYellowcarpet.objects.all().order_by('-id')
    infra_cam = InfUnCamera.objects.all().order_by('-id')
    infra_chzone = InfChildZone.objects.all().order_by('-id')

    lst_obj.append(infra_sp)
    lst_obj.append(infra_smcro)
    lst_obj.append(infra_smlap)
    lst_obj.append(infra_yel)
    lst_obj.append(infra_cam)
    lst_obj.append(infra_chzone)
    print('------------------------------------------------')
    # print(infra_sp)
    print('------------------------------------------------')
    # print(lst_obj)
    print('------------------------------------------------')
    for i in range(6):
        for obj in lst_obj[i]:
            if obj.year_code == 17:
                cnt_17 += 1
            elif obj.year_code == 18:
                cnt_18 += 1
            elif obj.year_code == 19:
                cnt_19 += 1
            elif obj.year_code == 20:
                cnt_20 += 1
        lst.append(cnt_17)
        lst.append(cnt_18)
        lst.append(cnt_19)
        lst.append(cnt_20)
        cnt_17, cnt_18, cnt_19, cnt_20 = 0, 0, 0, 0
        tmp[name_lst[i]] = lst
        # print(tmp)
        lst = []
    # print(tmp)
    # print(lst)
    # 연도별 사망자수 + 부상자수 sum 컬럼만
    acc = InfCarAcc.objects.all().order_by('id')
    for i in acc:
        sum_cg = 0
        if (i.cg == '사망자수' or i.cg == '부상자수') and i.year_code == 17:
            # print(i.sum)
            sum_cg = i.sum
        elif (i.cg == '사망자수' or i.cg == '부상자수') and i.year_code == 18:

            sum_cg = i.sum
        elif (i.cg == '사망자수' or i.cg == '부상자수') and i.year_code == 19:

            sum_cg+= i.sum
        elif (i.cg == '사망자수' or i.cg == '부상자수') and i.year_code == 20:

            sum_cg = i.sum

        lst.append(sum_cg)

    tmp['CG'] = lst
    print(tmp)
    return JsonResponse(tmp)

def graph_sago(request):
    seoul_sago = InfCarAcc.objects.all()
    return render(request,'seoul_sago.html')

def sago_data(request):
    sago_type = request.GET['seoul_sago']
    print(sago_type)

    s_death = []
    s_hurt = []
    json_ddict = {}

    sago_years = [17, 18, 19, 20]
    count_num = ['사망자수', '부상자수']
    sago_category = ['ctoc', 'ctop', 'calone']

    if sago_type == 'CtoC':
        sago_CtoC = InfCarAcc.objects.values('cg', 'ctoc', 'year_code')

        for i in range(len(sago_years)):
            s_death.append(sago_CtoC.filter(cg=count_num[0], year_code=sago_years[i])[0]['ctoc'])
            s_hurt.append(sago_CtoC.filter(cg=f'{count_num[1]}', year_code=f'{sago_years[i]}')[0]['ctoc'])
            json_ddict[i] = s_death[i]
            json_ddict[i + 4] = s_hurt[i]

    elif sago_type == 'CtoP':
        sago_CtoP = InfCarAcc.objects.values('cg','ctop','year_code')

        for i in range(len(sago_years)):
            for _ in range(len(count_num)):
                s_death.append(sago_CtoP.filter(cg=f'{count_num[0]}', year_code=f'{sago_years[i]}')[0]['ctop'])
                s_hurt.append(sago_CtoP.filter(cg=f'{count_num[1]}', year_code=f'{sago_years[i]}')[0]['ctop'])
            json_ddict[i] = s_death[i]
            json_ddict[i + 4] = s_hurt[i]

    elif sago_type == 'CAlone':
        sago_CAlone = InfCarAcc.objects.values('cg','calone','year_code')

        for i in range(len(sago_years)):
            for _ in range(len(count_num)):
                s_death.append(sago_CAlone.filter(cg=f'{count_num[0]}', year_code=f'{sago_years[i]}')[0]['calone'])
                s_hurt.append(sago_CAlone.filter(cg=f'{count_num[1]}', year_code=f'{sago_years[i]}')[0]['calone'])
            json_ddict[i] = s_death[i]
            json_ddict[i + 4] = s_hurt[i]

    return JsonResponse(json_ddict)
