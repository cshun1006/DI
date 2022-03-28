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
    sago_death_17 ,sago_death_18 ,sago_death_19, sago_death_20 = 0,0,0,0
    sago_hurt_17 ,sago_hurt_18 , sago_hurt_19 , sago_hurt_20 =0,0,0,0


    if sago_type == 'CtoC':
        '''
        select CG ,CtoC , year_code
        from InfCarAcc;
        '''
        # models에 있는 class 변수로 맞춰주기 ( mysql X)
        sago_CtoC = InfCarAcc.objects.values('cg', 'ctoc', 'year_code')
        print(sago_CtoC)
        '''
        select CtoC -> 계속 변해 
        from 
        where CG = '사망자수' -> 부상자수
        and year_code = '17'; -> 연도
        '''
        sago_death_17 = sago_CtoC.filter(cg='사망자수',year_code='17')[0]['ctoc']
        print(sago_death_17)
        sago_death_18 = sago_CtoC.filter(cg='사망자수',year_code='18')[0]['ctoc']
        sago_death_19 = sago_CtoC.filter(cg='사망자수',year_code='19')[0]['ctoc']
        sago_death_20 = sago_CtoC.filter(cg='사망자수', year_code='20')[0]['ctoc']

        sago_hurt_17 = sago_CtoC.filter(cg='부상자수',year_code='17')[0]['ctoc']
        print(sago_hurt_17)
        sago_hurt_18 = sago_CtoC.filter(cg='부상자수', year_code='18')[0]['ctoc']
        sago_hurt_19 = sago_CtoC.filter(cg='부상자수', year_code='19')[0]['ctoc']
        sago_hurt_20 = sago_CtoC.filter(cg='부상자수', year_code='20')[0]['ctoc']

    elif sago_type == 'CtoP':
        sago_CtoP = InfCarAcc.objects.values('cg','ctop','year_code')

        sago_death_17 = sago_CtoP.filter(cg='사망자수',year_code='17')[0]['ctop']
        sago_death_18 = sago_CtoP.filter(cg='사망자수',year_code='18')[0]['ctop']
        sago_death_19 = sago_CtoP.filter(cg='사망자수',year_code='19')[0]['ctop']
        sago_death_20 = sago_CtoP.filter(cg='사망자수', year_code='20')[0]['ctop']

        sago_hurt_17 = sago_CtoP.filter(cg='부상자수',year_code='17')[0]['ctop']
        sago_hurt_18 = sago_CtoP.filter(cg='부상자수', year_code='18')[0]['ctop']
        sago_hurt_19 = sago_CtoP.filter(cg='부상자수', year_code='19')[0]['ctop']
        sago_hurt_20 = sago_CtoP.filter(cg='부상자수', year_code='20')[0]['ctop']


    elif sago_type == 'CAlone':
        sago_CAlone = InfCarAcc.objects.values('cg','calone','year_code')

        sago_death_17 = sago_CAlone.filter(cg='사망자수',year_code='17')[0]['calone']
        sago_death_18 = sago_CAlone.filter(cg='사망자수',year_code='18')[0]['calone']
        sago_death_19 = sago_CAlone.filter(cg='사망자수',year_code='19')[0]['calone']
        sago_death_20 = sago_CAlone.filter(cg='사망자수', year_code='20')[0]['calone']

        sago_hurt_17 = sago_CAlone.filter(cg='부상자수',year_code='17')[0]['calone']
        sago_hurt_18 = sago_CAlone.filter(cg='부상자수', year_code='18')[0]['calone']
        sago_hurt_19 = sago_CAlone.filter(cg='부상자수', year_code='19')[0]['calone']
        sago_hurt_20 = sago_CAlone.filter(cg='부상자수', year_code='20')[0]['calone']

        print(sago_type)


    # 위치 설정 : UnboundLocalError: local variable 'json_dic' referenced before assignment -> elif 안에서 선언해서 오류남
    json_dic = {'death_17':sago_death_17,'death_18':sago_death_18,'death_19':sago_death_19,'death_20':sago_death_20,
                'hurt_17': sago_hurt_17,'hurt_18':sago_hurt_18,'hurt_19':sago_hurt_19,'hurt_20':sago_hurt_20}
    print(json_dic)
    return JsonResponse(json_dic)
