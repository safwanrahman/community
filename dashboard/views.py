from django.shortcuts import render
from dashboard.models import UserInfo
from dashboard.config import COUNTRIES
from dashboard.utils import get_avarage_contributions_years, get_top_skill
# Create your views here.

def post_form_upload(request):
    data = []
    for country in COUNTRIES:
        country_info = country_informations(country)
        data.append(country_info)

    return render(request, './show_result_form.html', {
        'data': data,
    })

def country_informations(country):
    total_mozillians = UserInfo.objects.all().filter(country=country).count()
    avg_contrib_years = get_avarage_contributions_years(country)
    top_skills = list(get_top_skill(country))
    data = {
    'country': country,
    'total_mozillians': total_mozillians,
    'avg_contrib_years': avg_contrib_years,
    'top_skills': top_skills
    }
    return data
