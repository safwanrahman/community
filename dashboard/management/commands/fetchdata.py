import requests
from dashboard.config import COUNTRIES
from dashboard.models import UserInfo, UserSkill, Skill
from django.conf import settings
from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        def get_all_skill_data(api_link):
            """Get skill id, member count of every skill and store it in DB"""
            skills_data = requests.get(api_link).json()
            if skills_data["next"] != None:
                skills = skills_data["results"]
                for skill in skills:
                    skill_id = skill["id"]
                    member_count = skill["member_count"]
                    skill_name = skill["name"]
                    s = Skill(skill_id=skill_id, member_count=member_count, skill_name=skill_name)
                    s.save()
                    print "Done", s.skill_name
                get_all_skill_data(skills_data["next"])
            else:
                skills = skills_data["results"]
                for skill in skills:
                    skill_id = skill["id"]
                    member_count = skill["member_count"]
                    skill_name = skill["name"]
                    s = Skill(skill_id=skill_id, member_count=member_count, skill_name=skill_name)
                    s.save()
                    print "Done", s.skill_name
                return "completed getting skill data"

        print get_all_skill_data("https://mozillians.org/api/v2/skills/?&api-key=%s" %settings.API_KEY)

        def get_country_user_usernames(api_link, country):
              """Get all the Mozillians username of the country"""
              mozilians = requests.get(api_link).json()
              if mozilians["next"] != None:
                 for profile in mozilians["results"]:
                     u = UserInfo(username=profile["username"], country=country, url=profile["_url"])
                     u.save()
                 get_country_user_usernames(mozilians["next"], country)
              else:
                 for profile in mozilians["results"]:
                     u = UserInfo(username=profile["username"], country=country, url=profile["_url"])
                     u.save()
              return "Completed", country

        for country in COUNTRIES:
            _country = country.replace(" ", "%20")
            API = ("https://mozillians.org/api/v2/users/?country=%s&api-key=%s&is_vouched=True"
                   %(_country,settings.API_KEY))
            get_country_user_usernames(api_link=API, country=country)

        print "Done getting usernames of all the countries"

        def get_mozillians_date(user):
            """Get date of Mozillians"""
            print user.url
            url= user.url + "?api-key=%s" %settings.API_KEY
            user_data = requests.get(url).json()
            mozillian = UserInfo.objects.get(username=user.username)
            mozillian.mozillian_date = user_data["date_mozillian"]["value"]
            mozillian.save()
            return "Done", user.username

        users = UserInfo.objects.all()
        for user in users:
            get_mozillians_date(user)

        print "done getting mozillians date"
        print "Finish all! You are almost done. "