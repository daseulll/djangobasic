from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

def archives_year(request, year):
    return HttpResponse('{}에 대한 내용'.format(year))

def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')
    if q:
    # 문자열 boolean은 문자열 길이 0이면 f, 0이상이면 T
        qs = qs.filter(name__icontains=q)
        #icontains의 i는 Ignore Case, 영어인경우 대소문자 구별X
        #qs 재할당

    return render(request, 'shop/item_list.html', {
        "item_list" : qs,
        "q": q,
    })