from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


zodiac_dict = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).",
}

types_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def index(request):
    zodiacs_list = list(zodiac_dict)
    context = {
        'zodiacs': zodiacs_list,
    }
    return render(request, 'horoscope/index.html', context=context)



def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    zodiacs_list = list(zodiac_dict)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        'zodiacs': zodiacs_list,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs_list = list(zodiac_dict)
    if sign_zodiac > len(zodiacs_list):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - "{sign_zodiac}"!')
    name_zodiac = zodiacs_list[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)


def get_type_info(request):
    types_list = list(types_dict)
    li_elem = ''
    for t in types_list:
        redirect_path = reverse('horoscope+type', args=[t])
        li_elem += f'<li><a href="{redirect_path}">{t.title()}</a></li>'
    response = f'<h2><ul>{li_elem}</ul></h2>'
    return HttpResponse(response)


def get_element_info(request, element: str):
    description = types_dict.get(element)
    li_elem = ''
    for i in description:
        redirect_path = reverse('horoscope-name', args=[i])
        li_elem += f'<li><a href="{redirect_path}">{i.title()}</a></li>'
    response = f'<h2><ul>{li_elem}</ul></h2>'
    return HttpResponse(response)
