import requests
from dashboard.config import COUNTRIES
from dashboard.models import UserInfo, UserSkill, Skill
from django.conf import settings
from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        def get_skill_usernames(skill_id):
            """Get all the mozillians username of every skills"""
            url = "https://mozillians.org/api/v2/skills/%s/?api-key=%s" %(skill_id, settings.API_KEY)
            skill_data = requests.get(url).json()
            profiles = skill_data["members"]
            skill = Skill.objects.get(skill_id=skill_id)
            for profile in profiles:
                username = profile["username"]
                u = UserSkill(username=username, skill=skill_data["name"])
                u.save()
            return skill_id

        skills = Skill.objects.all()

        for skill in skills:
            print "done", get_skill_usernames(skill.skill_id)

        print "Done all skills! Yapp!"

        def enter_country_data_in_userskill(country):
            users = UserInfo.objects.all().filter(country=country)
            for user in users:
                skill = UserSkill.objects.all().filter(username=user.username).update(country=user.country)
                print "Done", user.username
            return "Done", country

        for country in COUNTRIES:
            print enter_country_data_in_userskill(country)

        print "Done all"