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

        print "Done fetching all data"
        print "Deleting unnecessary data............................."
        # Delete the User skill data which does not have any specific country. Out of the country range
        # of the dashboard
        UserSkill.objects.all().filter(country='').delete()
        # Delete all the username from the user skill table. As we dont need the username anymore
        UserSkill.objects.all().update(username='')
        # Delete all the user URL data as its not needed for the dashboard
        UserInfo.objects.all().update(url='')
        print "Done deleting all the un necessary data"
        print "Finish all"
