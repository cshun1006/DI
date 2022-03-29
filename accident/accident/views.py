from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse
import requests

def index(request):
    return render(request,'index.html',{'list':InfSpeedBump.objects.all().order_by('-id')})

def two_page(request):
    return render(request,'2_page.html')

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
    elif infra_type == 'InfEleDisplay':
        infra = InfEleDisplay.objects.all().order_by('-id')
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
    name_lst = ['infra_sp','infra_smcro','infra_smlap','infra_yel','infra_cam','infra_chzone','inf_ele_display']
    cnt_17,cnt_18,cnt_19,cnt_20 = 0,0,0,0
    infra_sp = InfSpeedBump.objects.all().order_by('-id')
    infra_smcro = InfSmartCross.objects.all().order_by('-id')
    infra_smlap = InfSmartLamp.objects.all().order_by('-id')
    infra_yel = InfYellowcarpet.objects.all().order_by('-id')
    infra_cam = InfUnCamera.objects.all().order_by('-id')
    infra_chzone = InfChildZone.objects.all().order_by('-id')
    inf_ele_display = InfEleDisplay.objects.all().order_by('-id')

    lst_obj.append(infra_sp)
    lst_obj.append(infra_smcro)
    lst_obj.append(infra_smlap)
    lst_obj.append(infra_yel)
    lst_obj.append(infra_cam)
    lst_obj.append(infra_chzone)
    lst_obj.append(inf_ele_display)
    print('------------------------------------------------')
    # print(infra_sp)
    print('------------------------------------------------')
    # print(lst_obj)
    print('------------------------------------------------')
    for i in range(len(lst_obj)):
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



# 시도별 유형을 할려면 유형 다 가져와서 시도별로 분리해서 보여줌

def sido_pie(request):
    lst_obj = []
    tmp_obj = {}
    childAccident = FrequentzonechildAccident.objects.all().order_by('id')
    lgAccident = FrequentzonelgAccident.objects.all().order_by('id')
    oldmanAccident = FrequentzoneoldmanAccident.objects.all().order_by('id')
    tmzonAccident = FrequentzonetmzonAccident.objects.all().order_by('id')
    Jaywalking = JaywalkingAccident.objects.all().order_by('id')
    Schoolzonechild = SchoolzonechildAccident.objects.all().order_by('id')

    lst_obj.extend([childAccident,lgAccident,oldmanAccident,tmzonAccident,Jaywalking,Schoolzonechild])
    # print(lst_obj)
    name_lst = ['보행어린이','자치구3','노인보행','연휴','무단횡단','스쿨존']
    # print(childAccident)
    cnt_seoul,cnt_busan,cnt_daegu,cnt_inch,cnt_gwan,cnt_daejeon,cnt_ulsan,cnt_sejong,cnt_gyeonggi,cnt_gang,cnt_chungN=0,0,0,0,0,0,0,0,0,0,0
    cnt_chungS,cnt_jeollaN,cnt_jeollaS,cnt_gyeonsanN,cnt_gyeonsanS,cnt_jeju = 0,0,0,0,0,0
    year_lst = [2017,2018,2019,2020]
    year_seoul, year_busan, year_daegu, year_inch, year_gwan, year_daejeon, year_ulsan, year_sejong, year_gyeonggi, year_gang, year_chungN = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    year_chungS, year_jeollaN, year_jeollaS, year_gyeonsanN, year_gyeonsanS, year_jeju = 0, 0, 0, 0, 0, 0
    yearcnt = {}
    top_tmp = {}
    for i in range(len(lst_obj)):
        if i == 1:
            for YY in year_lst:
                for obj in lst_obj[1]:
                    # print(obj.address)
                    if obj.year == YY:
                        if obj.address[0:2] == '서울':
                            year_seoul += obj.occur
                        elif obj.address[0:2] == '부산':
                            year_busan += obj.occur
                        elif obj.address[0:2] == '대구':
                            year_daegu += obj.occur
                        elif obj.address[0:2] == '인천':
                            year_inch += obj.occur
                        elif obj.address[0:2] == '광주':
                            year_gwan += obj.occur
                        elif obj.address[0:2] == '대전':
                            year_daejeon += obj.occur
                        elif obj.address[0:2] == '울산':
                            year_ulsan += obj.occur
                        elif obj.address[0:2] == '세종':
                            year_sejong += obj.occur
                        elif obj.address[0:2] == '경기':
                            year_gyeonggi += obj.occur
                        elif obj.address[0:2] == '강원':
                            year_gang += obj.occur
                        elif obj.address[0:2] == '충청':
                            if obj.address[2:4] == '남도':
                                year_chungS += obj.occur
                            elif obj.address[2:4] == '북도':
                                year_chungN += obj.occur
                        elif obj.address[0:2] == '전라':
                            if obj.address[2:4] == '남도':
                                year_jeollaS += obj.occur
                            elif obj.address[2:4] == '북도':
                                year_jeollaN += obj.occur
                        elif obj.address[0:2] == '경상':
                            if obj.address[2:4] == '남도':
                                year_gyeonsanS += obj.occur
                            elif obj.address[2:4] == '북도':
                                year_gyeonsanN += obj.occur
                        elif obj.address[0:2] == '제주':
                            year_jeju += obj.occur
                yearcnt = {'서울': year_seoul, '부산': year_busan, '대구': year_daegu, '인천': year_inch, '광주': year_gwan,
                       '대전': year_daejeon, '울산': year_ulsan, '세종': year_sejong, '경기': year_gyeonggi,
                       '강원': year_gang, '충청북도': year_chungN, '충청남도': year_chungS, '전라북도': year_jeollaN, '전라남도': year_jeollaS,
                       '경상북도': year_gyeonsanN, '경상남도': year_gyeonsanS, '제주': year_jeju}
                top_tmp[YY] = yearcnt
                # print(top_tmp)
                year_seoul, year_busan, year_daegu, year_inch, year_gwan, year_daejeon, year_ulsan, year_sejong, year_gyeonggi, year_gang, year_chungN = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                year_chungS, year_jeollaN, year_jeollaS, year_gyeonsanN, year_gyeonsanS, year_jeju = 0, 0, 0, 0, 0, 0
                yearcnt = {}
        for obj in lst_obj[i]:  # 여기 까지만 하면 유형별(시도로 묶을수있음)
            # print(i.address)
            if obj.address[0:2] == '서울':
                cnt_seoul += obj.occur
            elif obj.address[0:2] == '부산':
                cnt_busan += obj.occur
            elif obj.address[0:2] == '대구':
                cnt_daegu += obj.occur
            elif obj.address[0:2] == '인천':
                cnt_inch += obj.occur
            elif obj.address[0:2] == '광주':
                cnt_gwan += obj.occur
            elif obj.address[0:2] == '대전':
                cnt_daejeon += obj.occur
            elif obj.address[0:2] == '울산':
                cnt_ulsan += obj.occur
            elif obj.address[0:2] == '세종':
                cnt_sejong += obj.occur
            elif obj.address[0:2] == '경기':
                cnt_gyeonggi += obj.occur
            elif obj.address[0:2] == '강원':
                cnt_gang += obj.occur
            elif obj.address[0:2] == '충청':
                if obj.address[2:4] == '남도':
                    cnt_chungS += obj.occur
                elif obj.address[2:4] == '북도':
                    cnt_chungN += obj.occur
            elif obj.address[0:2] == '전라':
                if obj.address[2:4] == '남도':
                    cnt_jeollaS += obj.occur
                elif obj.address[2:4] == '북도':
                    cnt_jeollaN += obj.occur
            elif obj.address[0:2] == '경상':
                if obj.address[2:4] == '남도':
                    cnt_gyeonsanS += obj.occur
                elif obj.address[2:4] == '북도':
                    cnt_gyeonsanN += obj.occur
            elif obj.address[0:2] == '제주':
                cnt_jeju += obj.occur
        # print(cnt_seoul)
        tmp={'서울':cnt_seoul ,'부산':cnt_busan,'대구':cnt_daegu,'인천':cnt_inch,'광주':cnt_gwan,'대전':cnt_daejeon,'울산':cnt_ulsan,'세종':cnt_sejong,'경기':cnt_gyeonggi,
            '강원':cnt_gang,'충청북도':cnt_chungN,'충청남도':cnt_chungS,'전라북도':cnt_jeollaN,'전라남도':cnt_jeollaS,
            '경상북도':cnt_gyeonsanN,'경상남도':cnt_gyeonsanS,'제주':cnt_jeju}
        cnt_seoul, cnt_busan, cnt_daegu, cnt_inch, cnt_gwan, cnt_daejeon, cnt_ulsan, cnt_sejong, cnt_gyeonggi, cnt_gang, cnt_chungN = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        cnt_chungS, cnt_jeollaN, cnt_jeollaS, cnt_gyeonsanN, cnt_gyeonsanS, cnt_jeju = 0, 0, 0, 0, 0, 0
        tmp_obj[name_lst[i]] = tmp
        tmp={}
    # print(tmp)
    tmp_obj['top'] = top_tmp
    # print(tmp_obj)
    # print(tmp_obj['보행어린이']['서울'])
    a = {'a':50000}
    return JsonResponse(tmp_obj)

