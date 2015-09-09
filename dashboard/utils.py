import requests
from datetime import date
from collections import Counter
from dashboard.models import UserInfo, UserSkill

def get_mozillian_years(userprofile):
	""" Get user contribution years"""
	if userprofile.mozillian_date:
		year_difference = date.today().year - userprofile.mozillian_date.year
		return year_difference
	return None

def get_avarage_contributions_years(country):
	"""Get the avarage contribution years of all the contributors of a country"""
	mozillians_years_list = []
	country_profiles = UserInfo.objects.all().filter(country=country)
	for profile in country_profiles:
		mozillians_years = get_mozillian_years(profile)
		if not mozillians_years == None:
			# list mozillains years of every profile
			mozillians_years_list.append(mozillians_years)
        # Calculate to addition all the years
	total_mozillians_years = sum(mozillians_years_list)
	# Devide the total years with the number of profiles to get the avarage year
	if len(mozillians_years_list) != 0:
	    avarage_contributions_years = total_mozillians_years / len(mozillians_years_list)
	else:
		avarage_contributions_years = 0
	return avarage_contributions_years

def get_top_skill(country):
	"""
	Get top skill from the DB

	In the DB, the user skills is stored separately. it calls all the skills and return top
	5 skills of the country's mozillian
	"""
	# Get all the skills of the specific country's mozillians
	country_skills = UserSkill.objects.all().filter(
		                                            country=country).values_list(
		                                            "skill", flat=True)
	# Count all the skills of the specific country's mozillians
	all_skills = Counter(country_skills)
	# Get top 5 skills of the country from all the skills
	# Get the top 5 only if there are more than 5 skills from all the mozillians of the country
	# If there are less than 5 skills from all the mozillains, list that 5
	if len(all_skills) >=5:
	    top_skill = all_skills.most_common()[:5]
	else:
		top_skill = all_skills
	return top_skill