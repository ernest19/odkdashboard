from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import *
from django.db.models import *

from datetime import date

 # Check login
""""
NON CALLABLE FIELDS IN MODELS
1. PRESURVEY('name_of_respondent','gps_of_structure','contact_of_respondent','reasons_elevy_bestway_increase_revenue','why_wont_collection_elevy_help_govenment','reason_elevy_affect_momo_business_opinion','if_no_why_support_Governments_decision_introduce_elevy')

2. QUESTIONNAIRE1()

3. QUESTIONNAIRE2('if_no_why_have_confidence_in_government_handling_risk_covid19')
4. POSTSURVEY('reason_publicity_about_today_Town_Hall_Meeting','reason_reduce_rate_allotted_elevy','give_reason_for_your_opinion_increase_the_threshold')
"""
def dashboard(request):
	allAgesPre = preSurvey.objects.values_list('age')
	allAgesQues = Questionaire1.objects.values_list('age')
	allAgesPos = postSurvey.objects.values_list('age')
	allAgesPre = [i[0] for i in allAgesPre]
	allAgesQues = [i[0] for i in allAgesQues]
	allAgesPos = [i[0] for i in allAgesPos]
	ageList = allAgesPre + allAgesQues + allAgesPos
	min_age = min(ageList)
	max_age = max(ageList)
	# regions
	allRegions = Questionaire1.objects.distinct('region')
	# allRegions = [i[0] for i in allRegions]
	return render(request, 'portal/dashboard.html',locals())

def landingPage(request):

	today = date.today()
	today =today.strftime("%B %d, %Y")

	message=welcomeMessage.objects.all().latest('id')
	quest=QuestionaireInfo.objects.all()
	for aa in quest:
		print(aa.title)
	return render(request, 'portal/index.html',locals())



def getDistricts(request,region):
	# if request.is_ajax():
	districts=True
	if region :
	   districts = Questionaire2.objects.filter(region=region).values_list('district').distinct()
	if region :
	   districts = preSurvey.objects.filter(region=region).values_list('district').distinct()
	if region :
	   districts = Questionaire1.objects.filter(region=region).values_list('district').distinct()
	districts = [i[0] for i in districts]
	print(districts)

	data = {
		'alldistricts':render_to_string('portal/districts.html',locals())
	}
	return JsonResponse(data)

from django.db.models import F

def chartsPlot(request):
	presurvey = preSurvey.objects.all()
	Questions = Questionaire1.objects.all()
	postsurvey = postSurvey.objects.all()
	Questions2 = Questionaire2.objects.all()
	Questions4 = Questionaire4.objects.all()
	# minAge = request.GET.get('minAge')
	# maxAge = request.GET.get('maxAge')
	otherFields = request.GET.get('otherFields')
	print(otherFields)
	# checkMin = presurvey.aggregate(Min('age'))

	# if maxAge:
	# 	if int(maxAge) > checkMin['age__min']:
	# 		presurvey = presurvey.filter(age__lte=maxAge)
	# 		presurvey = presurvey.filter(age__gte=minAge)
	# 		Questions = Questions.filter(age__lte=maxAge)
	# 		Questions = Questions.filter(age__gte=minAge)
	# 		postsurvey = postsurvey.filter(age__lte=maxAge)
	# 		postsurvey = postsurvey.filter(age__gte=minAge)

	if otherFields:
		otherFields = otherFields.split(',')
		if otherFields[0] != "Empty":
			presurvey = presurvey.filter(region=otherFields[0])
			Questions = Questions.filter(region=otherFields[0])
			postsurvey = postsurvey.filter(region=otherFields[0])
			Questions2 = Questions2.filter(region=otherFields[0])
			Questions4 = Questions4.filter(region=otherFields[0])



		if otherFields[1] != "Empty":
			presurvey = presurvey.filter(district=otherFields[1])
			Questions = Questions.filter(district=otherFields[1])
			postsurvey = postsurvey.filter(district=otherFields[1])
			Questions2 = Questions2.filter(region=otherFields[1])
			Questions4 = Questions4.filter(region=otherFields[1])


		if otherFields[2] != "Empty":
			if otherFields[2] == 'Sex':
				
				"""
				This groups into both sex then does the ordering and count, but don't think it will be 100% correct always,thats why i'm doing them one after the other  hj
				"""
				
				# anyEconomyMale = presurvey.order_by('sex').values_list('engaged_in_any_economy').annotate(Count('id'))

				##########################33 PRESURVEY #################################################################
				# engaged in any economic activity
				anyEconomyMale1 = presurvey.filter(sex='Male').values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyFeMale1 = presurvey.filter(sex='Female').values_list('engaged_in_any_economy').annotate(Count('id'))

				# what economic_activity_engaged_in
				engagedActivityMale = presurvey.filter(sex='Male').values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivityFemale = presurvey.filter(sex='Female').values_list('economic_activity_engaged_in').annotate(Count('id'))
				
				# what is your education_level
				educationlevelMale = presurvey.filter(sex='Male').values_list('education_level').annotate(Count('id'))
				educationlevelFemale = presurvey.filter(sex='Female').values_list('education_level').annotate(Count('id'))
				
				# Are you aware of the Government’s decision to introduce the e-levy tax?
				awareOfElevyMale = presurvey.filter(sex='Male').values_list('aware_of_elevy_introduction').annotate(Count('id'))
				awareOfElevyFemale = presurvey.filter(sex='Female').values_list('aware_of_elevy_introduction').annotate(Count('id'))
				
				# support_Governments_decision_introduce_elevy
				supportElevyMale = presurvey.filter(sex='Male').values_list('support_Governments_decision_introduce_elevy').annotate(Count('id'))
				supportElevyFemale = presurvey.filter(sex='Female').values_list('support_Governments_decision_introduce_elevy').annotate(Count('id'))
				
				# gov_considered_other_area_instead_elevy
				gov_considered_other_area_instead_elevyMale = presurvey.filter(sex='Male').values_list('gov_considered_other_area_instead_elevy').annotate(Count('id'))
				gov_considered_other_area_instead_elevyFemale = presurvey.filter(sex='Female').values_list('gov_considered_other_area_instead_elevy').annotate(Count('id'))
				
				#  Do you think the e-levy will affect the businesses of mobile money vendors?
				affectMomoBusinessMale = presurvey.filter(sex='Male').values_list('elevy_affect_momo_business').annotate(Count('id'))
				affectMomoBusinessFemale = presurvey.filter(sex='Female').values_list('elevy_affect_momo_business').annotate(Count('id'))
				
				#  Do you think the collection of the e-levy tax would help the Government achieve the 
				willCollectionHelpMale = presurvey.filter(sex='Male').values_list('collection_elevy_help_govenment').annotate(Count('id'))
				willCollectionHelpFemale = presurvey.filter(sex='Female').values_list('collection_elevy_help_govenment').annotate(Count('id'))
				
				# do_you_see_the_elevy_bestway_increase_revenue
				yourOpinionIncreaseMale = presurvey.filter(sex='Male').values_list('do_you_see_the_elevy_bestway_increase_revenue').annotate(Count('id'))
				yourOpinionIncreaseFemale = presurvey.filter(sex='Female').values_list('do_you_see_the_elevy_bestway_increase_revenue').annotate(Count('id'))

				# # if_no_why_support_Governments_decision_introduce_elevy
				# inysgdieM = presurvey.filter(sex='Male').values_list('if_no_why_support_Governments_decision_introduce_elevy').annotate(Count('id'))
				# inysgdieF = presurvey.filter(sex='Female').values_list('if_no_why_support_Governments_decision_introduce_elevy').annotate(Count('id'))
				# print(inysgdie)


				#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ END OF PRESURVEY $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
				
				# ###################################### QUESTIONNAIRE1 ##################################################
				# engaged in any economic activity
				anyEconomyMale1Q = Questions.filter(sex='MALE').values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyFeMale1Q = Questions.filter(sex='FEMALE').values_list('engaged_in_any_economy').annotate(Count('id'))
				

				# what economic_activity_engaged_in
				engagedActivityMaleQ = Questions.filter(sex='MALE').values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivityFemaleQ = Questions.filter(sex='FEMALE').values_list('economic_activity_engaged_in').annotate(Count('id'))
				
				# what is your education_level
				educationlevelMaleQ = Questions.filter(sex='MALE').values_list('education_level').annotate(Count('id'))
				educationlevelFemaleQ = Questions.filter(sex='FEMALE').values_list('education_level').annotate(Count('id'))
				
				# Do you think it is a call in the right direction?
				do_u_think_is_ryt_directionMale = Questions.filter(sex='MALE').values_list('do_u_think_is_ryt_direction').annotate(Count('id'))
				do_u_think_is_ryt_directionFemale = Questions.filter(sex='FEMALE').values_list('do_u_think_is_ryt_direction').annotate(Count('id'))
				
				# Are you aware of the suspension of the referendum?
				aware_of_suspension_of_the_referendumMale = Questions.filter(sex='MALE').values_list('aware_of_suspension_of_the_referendum').annotate(Count('id'))
				aware_of_suspension_of_the_referendumFemale = Questions.filter(sex='FEMALE').values_list('aware_of_suspension_of_the_referendum').annotate(Count('id'))
				################################# END OF QUESTIONNAIRE ###################################################

				# ####################################### QUESTIONNAIRE 2 ###############################################
				# engaged in any economic activity
				anyEconomyMale1Q2 = Questions2.filter(sex='Male').values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyFeMale1Q2 = Questions2.filter(sex='Female').values_list('engaged_in_any_economy').annotate(Count('id'))
				

				# what economic_activity_engaged_in
				engagedActivityMaleQ2 = Questions2.filter(sex='Male').values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivityFemaleQ2 = Questions2.filter(sex='Female').values_list('economic_activity_engaged_in').annotate(Count('id'))
				print(engagedActivityMaleQ2)
				print(engagedActivityMaleQ2)

				
				# what is your education_level
				educationlevelMaleQ2 = Questions2.filter(sex='Male').values_list('education_level').annotate(Count('id'))
				educationlevelFemaleQ2 = Questions2.filter(sex='Female').values_list('education_level').annotate(Count('id'))
				
				# aware_the_easing_restrictions_by_president
				aware_the_easing_restrictions_by_presidentMale = Questions2.filter(sex='Male').values_list('aware_the_easing_restrictions_by_president').annotate(Count('id'))
				aware_the_easing_restrictions_by_presidentFemale = Questions2.filter(sex='Female').values_list('aware_the_easing_restrictions_by_president').annotate(Count('id'))
				
				# think_easing_restrictions_by_president_call_right_direction
				terbpcrdMaleQ = Questions2.filter(sex='Male').values_list('think_easing_restrictions_by_president_call_right_direction').annotate(Count('id'))
				terbpcrdFemaleQ = Questions2.filter(sex='Female').values_list('think_easing_restrictions_by_president_call_right_direction').annotate(Count('id'))
				
				# have_confidence_in_government_handling_risk_covid19 
				hcighrcMaleQ = Questions2.filter(sex='Male').values_list('have_confidence_in_government_handling_risk_covid19').annotate(Count('id'))
				hcighrcFemaleQ = Questions2.filter(sex='Female').values_list('have_confidence_in_government_handling_risk_covid19').annotate(Count('id'))

				# how_would_you_rate_government_handling_covid19 
				hwyrghcMaleQ = Questions2.filter(sex='Male').values_list('how_would_you_rate_government_handling_covid19').annotate(Count('id'))
				hwyrghcFemaleQ = Questions2.filter(sex='Female').values_list('how_would_you_rate_government_handling_covid19').annotate(Count('id'))
				#################################### END OF UESTIONNAIRE 2 #####################################################

				#$############################# POST SURVEY #################################################
				# engaged in any economic activity
				anyEconomyMale1PS = postsurvey.filter(sex='Male').values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyFeMale1PS = postsurvey.filter(sex='Female').values_list('engaged_in_any_economy').annotate(Count('id'))
				
				# what economic_activity_engaged_in
				engagedActivityMalePS = postsurvey.filter(sex='Male').values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivityFemalePS = postsurvey.filter(sex='Female').values_list('economic_activity_engaged_in').annotate(Count('id'))
				
				# what is your education_level
				educationlevelMalePS = postsurvey.filter(sex='Male').values_list('education_level').annotate(Count('id'))
				educationlevelFemalePS = postsurvey.filter(sex='Female').values_list('education_level').annotate(Count('id'))

				# # Did you listen and understand the presentations made by the Finance Minister as well as other Government Officials on the e-levy?
				listen_n_understand_finance_ministerMale = postsurvey.filter(sex='Male').values_list('listen_n_understand_finance_minister').annotate(Count('id'))
				listen_n_understand_finance_ministerFemale = postsurvey.filter(sex='Female').values_list('listen_n_understand_finance_minister').annotate(Count('id'))
				
				# changed_your_perception_about_the_elevy
				changed_your_perception_about_the_elevyMale = postsurvey.filter(sex='Male').values_list('changed_your_perception_about_the_elevy').annotate(Count('id'))
				changed_your_perception_about_the_elevyFemale = postsurvey.filter(sex='Female').values_list('changed_your_perception_about_the_elevy').annotate(Count('id'))
				
				# # think_the_Government_should_increase_the_threshold
				think_the_Government_should_increase_the_thresholdMale = postsurvey.filter(sex='Male').values_list('think_the_Government_should_increase_the_threshold').annotate(Count('id'))
				think_the_Government_should_increase_the_thresholdFemale = postsurvey.filter(sex='Female').values_list('think_the_Government_should_increase_the_threshold').annotate(Count('id'))
				
				# government_should_reduce_rate_allotted_elevy
				government_should_reduce_rate_allotted_elevyMale = postsurvey.filter(sex='Male').values_list('government_should_reduce_rate_allotted_elevy').annotate(Count('id'))
				government_should_reduce_rate_allotted_elevyFemale = postsurvey.filter(sex='Female').values_list('government_should_reduce_rate_allotted_elevy').annotate(Count('id'))
				
				# enough_sensitization_elevy
				enough_sensitization_elevyMale = postsurvey.filter(sex='Male').values_list('enough_sensitization_elevy').annotate(Count('id'))
				enough_sensitization_elevyFemale = postsurvey.filter(sex='Female').values_list('enough_sensitization_elevy').annotate(Count('id'))
				
				# enough_publicity_about_today_Town_Hall_Meeting
				enough_publicity_about_today_Town_Hall_MeetingMale = postsurvey.filter(sex='Male').values_list('enough_publicity_about_today_Town_Hall_Meeting').annotate(Count('id'))
				enough_publicity_about_today_Town_Hall_MeetingFemale = postsurvey.filter(sex='Female').values_list('enough_publicity_about_today_Town_Hall_Meeting').annotate(Count('id'))
				
				############################### END OF POST SURVEY ########################################################

				################ QUESTIONNAIRE 4 ##############################
				# engaged in any economic activity
				anyEconomyMale1Q44 = Questions4.filter(sex='Male').values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyFeMale1Q44 = Questions4.filter(sex='Female').values_list('engaged_in_any_economy').annotate(Count('id'))

				# what economic_activity_engaged_in
				engagedActivityMaleQ44 = Questions4.filter(sex='Male').values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivityFemaleQ44 = Questions4.filter(sex='Female').values_list('economic_activity_engaged_in').annotate(Count('id'))
				print(engagedActivityFemaleQ44)

				
				# what is your education_level
				educationlevelMaleQ4 = Questions4.filter(sex='Male').values_list('education_level').annotate(Count('id'))
				educationlevelFemaleQ4 = Questions4.filter(sex='Female').values_list('education_level').annotate(Count('id'))

				# registered_your_sim_card
				registered_your_sim_cardMaleQ4 = Questions4.filter(sex='Male').values_list('registered_your_sim_card').annotate(Count('id'))
				registered_your_sim_cardFemaleQ4 = Questions4.filter(sex='Female').values_list('registered_your_sim_card').annotate(Count('id'))

				# delay_in_issuance_Ghana_card_affected_Sim_registration
				diigcasrMaleQ4 = Questions4.filter(sex='Male').values_list('delay_in_issuance_Ghana_card_affected_Sim_registration').annotate(Count('id'))
				diigcasrFemaleQ4 = Questions4.filter(sex='Female').values_list('delay_in_issuance_Ghana_card_affected_Sim_registration').annotate(Count('id'))
				##############################################################

				#  chart counts
				totalResponse_Presurvey = presurvey.count()
				totalResponse_questionnaire = Questions.count()
				totalResponse_questionnaire2 = Questions2.count()
				totalResponse_questionnaire4 = Questions4.count()
				totalResponse_Postsurvey = postsurvey.count()

				# male and femle counts
				presurveyMaleFemale = presurvey.values('sex').annotate(Count('id'))
				QuestionsMaleFemale = Questions.values('sex').annotate(Count('id'))
				Questions2MaleFemale = Questions2.values('sex').annotate(Count('id'))
				Questions4MaleFemale = Questions4.values('sex').annotate(Count('id'))
				postsurveyMaleFemale = postsurvey.values('sex').annotate(Count('id'))

				data = {
						'pre':render_to_string('portal/newpre.html',locals()),
						'questionaire':render_to_string('portal/newques.html',locals()),
						'questionaire2':render_to_string('portal/newques2.html',locals()),
						'questionaire4':render_to_string('portal/newques4.html',locals()),
						'post':render_to_string('portal/newpost.html',locals())
						}
				
				
			if otherFields[2] == 'Age':
				print("Age")

				# ################# ###### PRESURVEY ######################################

					# engaged in any economic activity
				anyEconomyAge1 = presurvey.filter(age__gte=18,age__lte=28).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge2 = presurvey.filter(age__gte=29,age__lte=39).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge3 = presurvey.filter(age__gte=40,age__lte=49).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge4 = presurvey.filter(age__gte=50,age__lte=59).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge5 = presurvey.filter(age__gte=60).values_list('engaged_in_any_economy').annotate(Count('id'))
				# anyEconomyAge6 = presurvey.filter(age__gte=48,age__lte=57).values_list('engaged_in_any_economy').annotate(Count('id'))
				# anyEconomyAge7 = presurvey.filter(age__gte=56,age__lte=60).values_list('engaged_in_any_economy').annotate(Count('id'))

				# what economic_activity_engaged_in
				engagedActivity1 = presurvey.filter(age__gte=18,age__lte=28).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity2 = presurvey.filter(age__gte=29,age__lte=39).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity3 = presurvey.filter(age__gte=40,age__lte=49).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity4 = presurvey.filter(age__gte=50,age__lte=59).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity5 = presurvey.filter(age__gte=60).values_list('economic_activity_engaged_in').annotate(Count('id'))
				# engagedActivity6 = presurvey.filter(age__gte=48,age__lte=57).values_list('economic_activity_engaged_in').annotate(Count('id'))
				# engagedActivity7 = presurvey.filter(age__gte=56,age__lte=60).values_list('economic_activity_engaged_in').annotate(Count('id'))
				
				# what is your education_level
				education_level1 = presurvey.filter(age__gte=18,age__lte=28).values_list('education_level').annotate(Count('id'))
				education_level2 = presurvey.filter(age__gte=29,age__lte=39).values_list('education_level').annotate(Count('id'))
				education_level3 = presurvey.filter(age__gte=40,age__lte=49).values_list('education_level').annotate(Count('id'))
				education_level4 = presurvey.filter(age__gte=50,age__lte=59).values_list('education_level').annotate(Count('id'))
				education_level5 = presurvey.filter(age__gte=60).values_list('education_level').annotate(Count('id'))
				# education_level6 = presurvey.filter(age__gte=48,age__lte=57).values_list('education_level').annotate(Count('id'))
				# education_level7 = presurvey.filter(age__gte=56,age__lte=60).values_list('education_level').annotate(Count('id'))
			
				# Are you aware of the Government’s decision to introduce the e-levy tax?
				aware_of_elevy_introduction1 = presurvey.filter(age__gte=18,age__lte=28).values_list('aware_of_elevy_introduction').annotate(Count('id'))
				aware_of_elevy_introduction2 = presurvey.filter(age__gte=29,age__lte=39).values_list('aware_of_elevy_introduction').annotate(Count('id'))
				aware_of_elevy_introduction3 = presurvey.filter(age__gte=40,age__lte=49).values_list('aware_of_elevy_introduction').annotate(Count('id'))
				aware_of_elevy_introduction4 = presurvey.filter(age__gte=50,age__lte=59).values_list('aware_of_elevy_introduction').annotate(Count('id'))
				aware_of_elevy_introduction5 = presurvey.filter(age__gte=60).values_list('aware_of_elevy_introduction').annotate(Count('id'))
				# aware_of_elevy_introduction6 = presurvey.filter(age__gte=48,age__lte=57).values_list('aware_of_elevy_introduction').annotate(Count('id'))
				# aware_of_elevy_introduction7 = presurvey.filter(age__gte=56,age__lte=60).values_list('aware_of_elevy_introduction').annotate(Count('id'))
				
				# support_elevy_introduction
				support_elevy_introduction1 = presurvey.filter(age__gte=18,age__lte=28).values_list('support_Governments_decision_introduce_elevy').annotate(Count('id'))
				support_elevy_introduction2 = presurvey.filter(age__gte=29,age__lte=39).values_list('support_Governments_decision_introduce_elevy').annotate(Count('id'))
				support_elevy_introduction3 = presurvey.filter(age__gte=40,age__lte=49).values_list('support_Governments_decision_introduce_elevy').annotate(Count('id'))
				support_elevy_introduction4 = presurvey.filter(age__gte=50,age__lte=59).values_list('support_Governments_decision_introduce_elevy').annotate(Count('id'))
				support_elevy_introduction5 = presurvey.filter(age__gte=60).values_list('support_Governments_decision_introduce_elevy').annotate(Count('id'))
				# support_elevy_introduction6 = presurvey.filter(age__gte=48,age__lte=57).values_list('support_Governments_decision_introduce_elevy').annotate(Count('id'))
				# support_elevy_introduction7 = presurvey.filter(age__gte=56,age__lte=60).values_list('support_Governments_decision_introduce_elevy').annotate(Count('id'))
			
				# gov_considered_other_area_instead_elevy
				gov_considered_other_area_instead_elevy1 = presurvey.filter(age__gte=18,age__lte=28).values_list('gov_considered_other_area_instead_elevy').annotate(Count('id'))
				gov_considered_other_area_instead_elevy2 = presurvey.filter(age__gte=29,age__lte=39).values_list('gov_considered_other_area_instead_elevy').annotate(Count('id'))
				gov_considered_other_area_instead_elevy3 = presurvey.filter(age__gte=40,age__lte=49).values_list('gov_considered_other_area_instead_elevy').annotate(Count('id'))
				gov_considered_other_area_instead_elevy4 = presurvey.filter(age__gte=50,age__lte=59).values_list('gov_considered_other_area_instead_elevy').annotate(Count('id'))
				gov_considered_other_area_instead_elevy5 = presurvey.filter(age__gte=60).values_list('gov_considered_other_area_instead_elevy').annotate(Count('id'))
				# gov_considered_other_area_instead_elevy6 = presurvey.filter(age__gte=48,age__lte=57).values_list('gov_considered_other_area_instead_elevy').annotate(Count('id'))
				# gov_considered_other_area_instead_elevy7 = presurvey.filter(age__gte=56,age__lte=60).values_list('gov_considered_other_area_instead_elevy').annotate(Count('id'))


				#  Do you think the e-levy will affect the businesses of mobile money vendors?
				elevy_affect_momo_business1 = presurvey.filter(age__gte=18,age__lte=28).values_list('elevy_affect_momo_business').annotate(Count('id'))
				elevy_affect_momo_business2 = presurvey.filter(age__gte=29,age__lte=39).values_list('elevy_affect_momo_business').annotate(Count('id'))
				elevy_affect_momo_business3 = presurvey.filter(age__gte=40,age__lte=49).values_list('elevy_affect_momo_business').annotate(Count('id'))
				elevy_affect_momo_business4 = presurvey.filter(age__gte=50,age__lte=59).values_list('elevy_affect_momo_business').annotate(Count('id'))
				elevy_affect_momo_business5 = presurvey.filter(age__gte=60).values_list('elevy_affect_momo_business').annotate(Count('id'))
				# elevy_affect_momo_business6 = presurvey.filter(age__gte=48,age__lte=57).values_list('elevy_affect_momo_business').annotate(Count('id'))
				# elevy_affect_momo_business7 = presurvey.filter(age__gte=56,age__lte=60).values_list('elevy_affect_momo_business').annotate(Count('id'))
				
				#  Do you think the collection of the e-levy tax would help the Government achieve the 
				collection_elevy_help_govenment1 = presurvey.filter(age__gte=18,age__lte=28).values_list('collection_elevy_help_govenment').annotate(Count('id'))
				collection_elevy_help_govenment2 = presurvey.filter(age__gte=29,age__lte=39).values_list('collection_elevy_help_govenment').annotate(Count('id'))
				collection_elevy_help_govenment3 = presurvey.filter(age__gte=40,age__lte=49).values_list('collection_elevy_help_govenment').annotate(Count('id'))
				collection_elevy_help_govenment4 = presurvey.filter(age__gte=50,age__lte=59).values_list('collection_elevy_help_govenment').annotate(Count('id'))
				collection_elevy_help_govenment5 = presurvey.filter(age__gte=60).values_list('collection_elevy_help_govenment').annotate(Count('id'))
				# collection_elevy_help_govenment6 = presurvey.filter(age__gte=48,age__lte=57).values_list('collection_elevy_help_govenment').annotate(Count('id'))
				# collection_elevy_help_govenment7 = presurvey.filter(age__gte=56,age__lte=60).values_list('collection_elevy_help_govenment').annotate(Count('id'))
				
				# # In your opinion, do you see the e-levy tax as the best way to increase revenue for the 
				ur_opinion_elevey_increase_revenue1 = presurvey.filter(age__gte=18,age__lte=28).values_list('do_you_see_the_elevy_bestway_increase_revenue').annotate(Count('id'))
				ur_opinion_elevey_increase_revenue2 = presurvey.filter(age__gte=29,age__lte=39).values_list('do_you_see_the_elevy_bestway_increase_revenue').annotate(Count('id'))
				ur_opinion_elevey_increase_revenue3 = presurvey.filter(age__gte=40,age__lte=49).values_list('do_you_see_the_elevy_bestway_increase_revenue').annotate(Count('id'))
				ur_opinion_elevey_increase_revenue4 = presurvey.filter(age__gte=50,age__lte=59).values_list('do_you_see_the_elevy_bestway_increase_revenue').annotate(Count('id'))
				ur_opinion_elevey_increase_revenue5 = presurvey.filter(age__gte=60).values_list('do_you_see_the_elevy_bestway_increase_revenue').annotate(Count('id'))
				# ur_opinion_elevey_increase_revenue6 = presurvey.filter(age__gte=48,age__lte=57).values_list('do_you_see_the_elevy_bestway_increase_revenue').annotate(Count('id'))
				# ur_opinion_elevey_increase_revenue7 = presurvey.filter(age__gte=56,age__lte=60).values_list('do_you_see_the_elevy_bestway_increase_revenue').annotate(Count('id'))

				# ################# ###### END OF PRESURVEY ######################################


				# ########################  QUESTIONNAIRE 1##########################################
					# engaged in any economic activity
				anyEconomyAge1Q = Questions.filter(age__gte=18,age__lte=28).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge2Q = Questions.filter(age__gte=29,age__lte=39).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge3Q = Questions.filter(age__gte=40,age__lte=49).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge4Q = Questions.filter(age__gte=50,age__lte=59).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge5Q = Questions.filter(age__gte=60).values_list('engaged_in_any_economy').annotate(Count('id'))
				# anyEconomyAge6Q = Questions.filter(age__gte=48,age__lte=57).values_list('engaged_in_any_economy').annotate(Count('id'))
				# anyEconomyAge7Q = Questions.filter(age__gte=56,age__lte=60).values_list('engaged_in_any_economy').annotate(Count('id'))
				
				# what economic_activity_engaged_in
				engagedActivity1Q = Questions.filter(age__gte=18,age__lte=28).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity2Q = Questions.filter(age__gte=29,age__lte=39).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity3Q = Questions.filter(age__gte=40,age__lte=49).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity4Q = Questions.filter(age__gte=50,age__lte=59).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity5Q = Questions.filter(age__gte=60).values_list('economic_activity_engaged_in').annotate(Count('id'))
				# engagedActivity6Q = Questions.filter(age__gte=48,age__lte=57).values_list('economic_activity_engaged_in').annotate(Count('id'))
				# engagedActivity7Q = Questions.filter(age__gte=56,age__lte=60).values_list('economic_activity_engaged_in').annotate(Count('id'))
				
				# what is your education_level
				education_level1Q = Questions.filter(age__gte=18,age__lte=28).values_list('education_level').annotate(Count('id'))
				education_level2Q = Questions.filter(age__gte=29,age__lte=39).values_list('education_level').annotate(Count('id'))
				education_level3Q = Questions.filter(age__gte=40,age__lte=49).values_list('education_level').annotate(Count('id'))
				education_level4Q = Questions.filter(age__gte=50,age__lte=59).values_list('education_level').annotate(Count('id'))
				education_level5Q = Questions.filter(age__gte=60).values_list('education_level').annotate(Count('id'))
				# education_level6Q = Questions.filter(age__gte=48,age__lte=57).values_list('education_level').annotate(Count('id'))
				# education_level7Q = Questions.filter(age__gte=56,age__lte=60).values_list('education_level').annotate(Count('id'))
				
				# # Do you think it is a call in the right direction?
				do_u_think_is_ryt_direction1 = Questions.filter(age__gte=18,age__lte=28).values_list('do_u_think_is_ryt_direction').annotate(Count('id'))
				do_u_think_is_ryt_direction2 = Questions.filter(age__gte=29,age__lte=39).values_list('do_u_think_is_ryt_direction').annotate(Count('id'))
				do_u_think_is_ryt_direction3 = Questions.filter(age__gte=40,age__lte=49).values_list('do_u_think_is_ryt_direction').annotate(Count('id'))
				do_u_think_is_ryt_direction4 = Questions.filter(age__gte=50,age__lte=59).values_list('do_u_think_is_ryt_direction').annotate(Count('id'))
				do_u_think_is_ryt_direction5 = Questions.filter(age__gte=60).values_list('do_u_think_is_ryt_direction').annotate(Count('id'))
				# do_u_think_is_ryt_direction6 = Questions.filter(age__gte=48,age__lte=57).values_list('do_u_think_is_ryt_direction').annotate(Count('id'))
				# do_u_think_is_ryt_direction7 = Questions.filter(age__gte=56,age__lte=60).values_list('do_u_think_is_ryt_direction').annotate(Count('id'))
				

				# # Do you think it is a call in the right direction?
				aware_of_suspension_of_the_referendum1 = Questions.filter(age__gte=18,age__lte=28).values_list('aware_of_suspension_of_the_referendum').annotate(Count('id'))
				aware_of_suspension_of_the_referendum2 = Questions.filter(age__gte=29,age__lte=39).values_list('aware_of_suspension_of_the_referendum').annotate(Count('id'))
				aware_of_suspension_of_the_referendum3 = Questions.filter(age__gte=40,age__lte=49).values_list('aware_of_suspension_of_the_referendum').annotate(Count('id'))
				aware_of_suspension_of_the_referendum4 = Questions.filter(age__gte=50,age__lte=59).values_list('aware_of_suspension_of_the_referendum').annotate(Count('id'))
				aware_of_suspension_of_the_referendum5 = Questions.filter(age__gte=60).values_list('aware_of_suspension_of_the_referendum').annotate(Count('id'))
				# aware_of_suspension_of_the_referendum6 = Questions.filter(age__gte=48,age__lte=57).values_list('aware_of_suspension_of_the_referendum').annotate(Count('id'))
				# aware_of_suspension_of_the_referendum7 = Questions.filter(age__gte=56,age__lte=60).values_list('aware_of_suspension_of_the_referendum').annotate(Count('id'))

				# ################# ###### END OF QUESTIONNAIRE 1 ######################################

				
				# ########################  QUESTIONNAIRE2 #########################################
					# engaged in any economic activity
				anyEconomyAge1Q2 = Questions2.filter(age__gte=18,age__lte=28).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge2Q2 = Questions2.filter(age__gte=29,age__lte=39).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge3Q2 = Questions2.filter(age__gte=40,age__lte=49).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge4Q2 = Questions2.filter(age__gte=50,age__lte=59).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge5Q2 = Questions2.filter(age__gte=60).values_list('engaged_in_any_economy').annotate(Count('id'))
				# anyEconomyAge6Q2 = Questions2.filter(age__gte=48,age__lte=57).values_list('engaged_in_any_economy').annotate(Count('id'))
				# anyEconomyAge7Q2 = Questions2.filter(age__gte=56,age__lte=60).values_list('engaged_in_any_economy').annotate(Count('id'))
				
				# what economic_activity_engaged_in
				engagedActivity1Q2 = Questions2.filter(age__gte=18,age__lte=28).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity2Q2 = Questions2.filter(age__gte=29,age__lte=39).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity3Q2 = Questions2.filter(age__gte=40,age__lte=49).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity4Q2 = Questions2.filter(age__gte=50,age__lte=59).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity5Q2 = Questions2.filter(age__gte=60).values_list('economic_activity_engaged_in').annotate(Count('id'))
				# engagedActivity6Q2 = Questions2.filter(age__gte=48,age__lte=57).values_list('economic_activity_engaged_in').annotate(Count('id'))
				# engagedActivity7Q2 = Questions2.filter(age__gte=56,age__lte=60).values_list('economic_activity_engaged_in').annotate(Count('id'))
				
				# what is your education_level
				education_level1Q2 = Questions2.filter(age__gte=18,age__lte=28).values_list('education_level').annotate(Count('id'))
				education_level2Q2 = Questions2.filter(age__gte=29,age__lte=39).values_list('education_level').annotate(Count('id'))
				education_level3Q2 = Questions2.filter(age__gte=40,age__lte=49).values_list('education_level').annotate(Count('id'))
				education_level4Q2 = Questions2.filter(age__gte=50,age__lte=59).values_list('education_level').annotate(Count('id'))
				education_level5Q2 = Questions2.filter(age__gte=60).values_list('education_level').annotate(Count('id'))
				# education_level6Q2 = Questions2.filter(age__gte=48,age__lte=57).values_list('education_level').annotate(Count('id'))
				# education_level7Q2 = Questions2.filter(age__gte=56,age__lte=60).values_list('education_level').annotate(Count('id'))
				
				# aware_the_easing_restrictions_by_president NEW CHANGE
				aware_the_easing_restrictions_by_president1 = Questions2.filter(age__gte=18,age__lte=28).values_list('aware_the_easing_restrictions_by_president').annotate(Count('id'))
				aware_the_easing_restrictions_by_president2 = Questions2.filter(age__gte=29,age__lte=39).values_list('aware_the_easing_restrictions_by_president').annotate(Count('id'))
				aware_the_easing_restrictions_by_president3 = Questions2.filter(age__gte=40,age__lte=49).values_list('aware_the_easing_restrictions_by_president').annotate(Count('id'))
				aware_the_easing_restrictions_by_president4 = Questions2.filter(age__gte=50,age__lte=59).values_list('aware_the_easing_restrictions_by_president').annotate(Count('id'))
				aware_the_easing_restrictions_by_president5 = Questions2.filter(age__gte=60).values_list('aware_the_easing_restrictions_by_president').annotate(Count('id'))
				# aware_the_easing_restrictions_by_president6 = Questions2.filter(age__gte=48,age__lte=57).values_list('aware_the_easing_restrictions_by_president').annotate(Count('id'))
				# aware_the_easing_restrictions_by_president7 = Questions2.filter(age__gte=56,age__lte=60).values_list('aware_the_easing_restrictions_by_president').annotate(Count('id'))

				# think_easing_restrictions_by_president_call_right_direction NEW CHANGE
				terbpcrd1 = Questions2.filter(age__gte=18,age__lte=28).values_list('think_easing_restrictions_by_president_call_right_direction').annotate(Count('id'))
				terbpcrd2 = Questions2.filter(age__gte=29,age__lte=39).values_list('think_easing_restrictions_by_president_call_right_direction').annotate(Count('id'))
				terbpcrd3 = Questions2.filter(age__gte=40,age__lte=49).values_list('think_easing_restrictions_by_president_call_right_direction').annotate(Count('id'))
				terbpcrd4 = Questions2.filter(age__gte=50,age__lte=59).values_list('think_easing_restrictions_by_president_call_right_direction').annotate(Count('id'))
				terbpcrd5 = Questions2.filter(age__gte=60).values_list('think_easing_restrictions_by_president_call_right_direction').annotate(Count('id'))
				# terbpcrd6 = Questions2.filter(age__gte=48,age__lte=57).values_list('think_easing_restrictions_by_president_call_right_direction').annotate(Count('id'))
				# terbpcrd7 = Questions2.filter(age__gte=56,age__lte=60).values_list('think_easing_restrictions_by_president_call_right_direction').annotate(Count('id'))

				# have_confidence_in_government_handling_risk_covid19 NEW CHANGE
				hcighrc1 = Questions2.filter(age__gte=18,age__lte=28).values_list('have_confidence_in_government_handling_risk_covid19').annotate(Count('id'))
				hcighrc2 = Questions2.filter(age__gte=29,age__lte=39).values_list('have_confidence_in_government_handling_risk_covid19').annotate(Count('id'))
				hcighrc3 = Questions2.filter(age__gte=40,age__lte=49).values_list('have_confidence_in_government_handling_risk_covid19').annotate(Count('id'))
				hcighrc4 = Questions2.filter(age__gte=50,age__lte=59).values_list('have_confidence_in_government_handling_risk_covid19').annotate(Count('id'))
				hcighrc5 = Questions2.filter(age__gte=60).values_list('have_confidence_in_government_handling_risk_covid19').annotate(Count('id'))
				# hcighrc6 = Questions2.filter(age__gte=48,age__lte=57).values_list('have_confidence_in_government_handling_risk_covid19').annotate(Count('id'))
				# hcighrc7 = Questions2.filter(age__gte=56,age__lte=60).values_list('have_confidence_in_government_handling_risk_covid19').annotate(Count('id'))
				
				# how_would_you_rate_government_handling_covid19
				hwyrghc1 = Questions2.filter(age__gte=18,age__lte=28).values_list('how_would_you_rate_government_handling_covid19').annotate(Count('id'))
				hwyrg2hc = Questions2.filter(age__gte=29,age__lte=39).values_list('how_would_you_rate_government_handling_covid19').annotate(Count('id'))
				hwyrghc3 = Questions2.filter(age__gte=40,age__lte=49).values_list('how_would_you_rate_government_handling_covid19').annotate(Count('id'))
				hwyrghc4 = Questions2.filter(age__gte=50,age__lte=59).values_list('how_would_you_rate_government_handling_covid19').annotate(Count('id'))
				hwyrghc5 = Questions2.filter(age__gte=60).values_list('how_would_you_rate_government_handling_covid19').annotate(Count('id'))
				# hwyrghc6 = Questions2.filter(age__gte=48,age__lte=57).values_list('how_would_you_rate_government_handling_covid19').annotate(Count('id'))
				# hwyrghc7 = Questions2.filter(age__gte=56,age__lte=60).values_list('how_would_you_rate_government_handling_covid19').annotate(Count('id'))

				# ################# ###### END OF QUESTIONNAIRE 2 ######################################


				# ################# ###### POST SURVEY ######################################
					# engaged in any economic activity
				anyEconomyAge1PS = postsurvey.filter(age__gte=18,age__lte=28).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge2 = postsurvey.filter(age__gte=29,age__lte=39).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge3PS = postsurvey.filter(age__gte=40,age__lte=49).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge4PS = postsurvey.filter(age__gte=50,age__lte=59).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge5PS = postsurvey.filter(age__gte=60).values_list('engaged_in_any_economy').annotate(Count('id'))
				# anyEconomyAge6PS = postsurvey.filter(age__gte=48,age__lte=57).values_list('engaged_in_any_economy').annotate(Count('id'))
				# anyEconomyAge7PS = postsurvey.filter(age__gte=56,age__lte=60).values_list('engaged_in_any_economy').annotate(Count('id'))

				# what economic_activity_engaged_in
				engagedActivity1PS = postsurvey.filter(age__gte=18,age__lte=28).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity2PS = postsurvey.filter(age__gte=29,age__lte=39).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity3PS = postsurvey.filter(age__gte=40,age__lte=49).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity4PS = postsurvey.filter(age__gte=50,age__lte=59).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity5PS = postsurvey.filter(age__gte=60).values_list('economic_activity_engaged_in').annotate(Count('id'))
				# engagedActivity6PS = postsurvey.filter(age__gte=48,age__lte=57).values_list('economic_activity_engaged_in').annotate(Count('id'))
				# engagedActivity7PS = postsurvey.filter(age__gte=56,age__lte=60).values_list('economic_activity_engaged_in').annotate(Count('id'))
				
				# what is your education_level
				education_level1PS = postsurvey.filter(age__gte=18,age__lte=28).values_list('education_level').annotate(Count('id'))
				education_level2PS = postsurvey.filter(age__gte=29,age__lte=39).values_list('education_level').annotate(Count('id'))
				education_level3PS = postsurvey.filter(age__gte=40,age__lte=49).values_list('education_level').annotate(Count('id'))
				education_level4PS = postsurvey.filter(age__gte=50,age__lte=59).values_list('education_level').annotate(Count('id'))
				education_level5PS = postsurvey.filter(age__gte=60).values_list('education_level').annotate(Count('id'))
				# education_level6PS = postsurvey.filter(age__gte=48,age__lte=57).values_list('education_level').annotate(Count('id'))
				# education_level7PS = postsurvey.filter(age__gte=56,age__lte=60).values_list('education_level').annotate(Count('id'))
				
				 # Did you listen and understand the presentations made by the Finance Minister as well as other Government Officials on the e-levy?
				listen_n_understand_finance_minister1 = postsurvey.filter(age__gte=18,age__lte=28).values_list('listen_n_understand_finance_minister').annotate(Count('id'))
				listen_n_understand_finance_minister2 = postsurvey.filter(age__gte=29,age__lte=39).values_list('listen_n_understand_finance_minister').annotate(Count('id'))
				listen_n_understand_finance_minister3 = postsurvey.filter(age__gte=40,age__lte=49).values_list('listen_n_understand_finance_minister').annotate(Count('id'))
				listen_n_understand_finance_minister4 = postsurvey.filter(age__gte=50,age__lte=59).values_list('listen_n_understand_finance_minister').annotate(Count('id'))
				listen_n_understand_finance_minister5 = postsurvey.filter(age__gte=60).values_list('listen_n_understand_finance_minister').annotate(Count('id'))
				# listen_n_understand_finance_minister6 = postsurvey.filter(age__gte=48,age__lte=57).values_list('listen_n_understand_finance_minister').annotate(Count('id'))
				# listen_n_understand_finance_minister7 = postsurvey.filter(age__gte=56,age__lte=60).values_list('listen_n_understand_finance_minister').annotate(Count('id'))
				
				# changed_your_perception_about_the_elevy
				changed_your_perception_about_the_elevy1 = postsurvey.filter(age__gte=18,age__lte=28).values_list('changed_your_perception_about_the_elevy').annotate(Count('id'))
				changed_your_perception_about_the_elevy2 = postsurvey.filter(age__gte=29,age__lte=39).values_list('changed_your_perception_about_the_elevy').annotate(Count('id'))
				changed_your_perception_about_the_elevy3 = postsurvey.filter(age__gte=40,age__lte=49).values_list('changed_your_perception_about_the_elevy').annotate(Count('id'))
				changed_your_perception_about_the_elevy4 = postsurvey.filter(age__gte=50,age__lte=59).values_list('changed_your_perception_about_the_elevy').annotate(Count('id'))
				changed_your_perception_about_the_elevy5 = postsurvey.filter(age__gte=60).values_list('changed_your_perception_about_the_elevy').annotate(Count('id'))
				# changed_your_perception_about_the_elevy6 = postsurvey.filter(age__gte=48,age__lte=57).values_list('changed_your_perception_about_the_elevy').annotate(Count('id'))
				# changed_your_perception_about_the_elevy7 = postsurvey.filter(age__gte=56,age__lte=60).values_list('changed_your_perception_about_the_elevy').annotate(Count('id'))
				

				# think_the_Government_should_increase_the_threshold   new change
				should_government_increase_the_threshold1 = postsurvey.filter(age__gte=18,age__lte=28).values_list('think_the_Government_should_increase_the_threshold').annotate(Count('id'))
				should_government_increase_the_threshold2 = postsurvey.filter(age__gte=29,age__lte=39).values_list('think_the_Government_should_increase_the_threshold').annotate(Count('id'))
				should_government_increase_the_threshold3 = postsurvey.filter(age__gte=40,age__lte=49).values_list('think_the_Government_should_increase_the_threshold').annotate(Count('id'))
				should_government_increase_the_threshold4 = postsurvey.filter(age__gte=50,age__lte=59).values_list('think_the_Government_should_increase_the_threshold').annotate(Count('id'))
				should_government_increase_the_threshold5 = postsurvey.filter(age__gte=60).values_list('think_the_Government_should_increase_the_threshold').annotate(Count('id'))
				# should_government_increase_the_threshold6 = postsurvey.filter(age__gte=48,age__lte=57).values_list('think_the_Government_should_increase_the_threshold').annotate(Count('id'))
				# should_government_increase_the_threshold7 = postsurvey.filter(age__gte=56,age__lte=60).values_list('think_the_Government_should_increase_the_threshold').annotate(Count('id'))


				# government_should_reduce_rate_allotted_elevy
				should_the_government_reduce_elevy_tax1 = postsurvey.filter(age__gte=18,age__lte=28).values_list('government_should_reduce_rate_allotted_elevy').annotate(Count('id'))
				should_the_government_reduce_elevy_tax2 = postsurvey.filter(age__gte=29,age__lte=39).values_list('government_should_reduce_rate_allotted_elevy').annotate(Count('id'))
				should_the_government_reduce_elevy_tax3 = postsurvey.filter(age__gte=40,age__lte=49).values_list('government_should_reduce_rate_allotted_elevy').annotate(Count('id'))
				should_the_government_reduce_elevy_tax4 = postsurvey.filter(age__gte=50,age__lte=59).values_list('government_should_reduce_rate_allotted_elevy').annotate(Count('id'))
				should_the_government_reduce_elevy_tax5 = postsurvey.filter(age__gte=60).values_list('government_should_reduce_rate_allotted_elevy').annotate(Count('id'))
				# should_the_government_reduce_elevy_tax6 = postsurvey.filter(age__gte=48,age__lte=57).values_list('government_should_reduce_rate_allotted_elevy').annotate(Count('id'))
				# should_the_government_reduce_elevy_tax7 = postsurvey.filter(age__gte=56,age__lte=60).values_list('government_should_reduce_rate_allotted_elevy').annotate(Count('id'))

# ````````````````enough_sensitization_elevy   new change
				has_there_been_enough_sensitization1 = postsurvey.filter(age__gte=18,age__lte=28).values_list('enough_sensitization_elevy').annotate(Count('id'))
				has_there_been_enough_sensitization2 = postsurvey.filter(age__gte=29,age__lte=39).values_list('enough_sensitization_elevy').annotate(Count('id'))
				has_there_been_enough_sensitization3 = postsurvey.filter(age__gte=40,age__lte=49).values_list('enough_sensitization_elevy').annotate(Count('id'))
				has_there_been_enough_sensitization4 = postsurvey.filter(age__gte=50,age__lte=59).values_list('enough_sensitization_elevy').annotate(Count('id'))
				has_there_been_enough_sensitization5 = postsurvey.filter(age__gte=60).values_list('enough_sensitization_elevy').annotate(Count('id'))
				# has_there_been_enough_sensitization6 = postsurvey.filter(age__gte=48,age__lte=57).values_list('enough_sensitization_elevy').annotate(Count('id'))
				# has_there_been_enough_sensitization7 = postsurvey.filter(age__gte=56,age__lte=60).values_list('enough_sensitization_elevy').annotate(Count('id'))


				# enough_publicity_about_today_Town_Hall_Meeting
				enough_publicity_about_today_Town_Hall_Meeting1 = postsurvey.filter(age__gte=18,age__lte=28).values_list('enough_publicity_about_today_Town_Hall_Meeting').annotate(Count('id'))
				enough_publicity_about_today_Town_Hall_Meeting2 = postsurvey.filter(age__gte=29,age__lte=39).values_list('enough_publicity_about_today_Town_Hall_Meeting').annotate(Count('id'))
				enough_publicity_about_today_Town_Hall_Meeting3 = postsurvey.filter(age__gte=40,age__lte=49).values_list('enough_publicity_about_today_Town_Hall_Meeting').annotate(Count('id'))
				enough_publicity_about_today_Town_Hall_Meeting4 = postsurvey.filter(age__gte=50,age__lte=59).values_list('enough_publicity_about_today_Town_Hall_Meeting').annotate(Count('id'))
				enough_publicity_about_today_Town_Hall_Meeting5 = postsurvey.filter(age__gte=60).values_list('enough_publicity_about_today_Town_Hall_Meeting').annotate(Count('id'))
				# enough_publicity_about_today_Town_Hall_Meeting6 = postsurvey.filter(age__gte=48,age__lte=57).values_list('enough_publicity_about_today_Town_Hall_Meeting').annotate(Count('id'))
				# enough_publicity_about_today_Town_Hall_Meeting7 = postsurvey.filter(age__gte=56,age__lte=60).values_list('enough_publicity_about_today_Town_Hall_Meeting').annotate(Count('id'))
				# # ################# ###### END POST SURVEY ######################################

				################QUESTIONNAIRE 4 ######################
					# engaged in any economic activity
				anyEconomyAge1PSQ4 = Questions4.filter(age__gte=18,age__lte=28).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge2PSQ4 = Questions4.filter(age__gte=29,age__lte=39).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge3PSQ4 = Questions4.filter(age__gte=40,age__lte=49).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge4PSQ4 = Questions4.filter(age__gte=50,age__lte=59).values_list('engaged_in_any_economy').annotate(Count('id'))
				anyEconomyAge5PSQ4 = Questions4.filter(age__gte=60).values_list('engaged_in_any_economy').annotate(Count('id'))
				# anyEconomyAge6PSQ4 = Questions4.filter(age__gte=48,age__lte=57).values_list('engaged_in_any_economy').annotate(Count('id'))
				# anyEconomyAge7PSQ4 = Questions4.filter(age__gte=56,age__lte=60).values_list('engaged_in_any_economy').annotate(Count('id'))

				# what economic_activity_engaged_in
				engagedActivity1PSQ4 = Questions4.filter(age__gte=18,age__lte=28).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity2PSQ4 = Questions4.filter(age__gte=29,age__lte=39).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity3PSQ4 = Questions4.filter(age__gte=40,age__lte=49).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity4PSQ4 = Questions4.filter(age__gte=50,age__lte=59).values_list('economic_activity_engaged_in').annotate(Count('id'))
				engagedActivity5PSQ4 = Questions4.filter(age__gte=60).values_list('economic_activity_engaged_in').annotate(Count('id'))
				# engagedActivity6PSQ4 = Questions4.filter(age__gte=48,age__lte=57).values_list('economic_activity_engaged_in').annotate(Count('id'))
				# engagedActivity7PSQ4 = Questions4.filter(age__gte=56,age__lte=60).values_list('economic_activity_engaged_in').annotate(Count('id'))
				
				# what is your education_level
				education_level1PSQ4 = Questions4.filter(age__gte=18,age__lte=28).values_list('education_level').annotate(Count('id'))
				education_level2PSQ4 = Questions4.filter(age__gte=29,age__lte=39).values_list('education_level').annotate(Count('id'))
				education_level3PSQ4 = Questions4.filter(age__gte=40,age__lte=49).values_list('education_level').annotate(Count('id'))
				education_level4PSQ4 = Questions4.filter(age__gte=50,age__lte=59).values_list('education_level').annotate(Count('id'))
				education_level5PSQ4 = Questions4.filter(age__gte=60).values_list('education_level').annotate(Count('id'))
				# education_level6PSQ4 = Questions4.filter(age__gte=48,age__lte=57).values_list('education_level').annotate(Count('id'))
				# education_level7PSQ4 = Questions4.filter(age__gte=56,age__lte=60).values_list('education_level').annotate(Count('id'))

				# registered_your_sim_card
				registered_your_sim_card1PSQ4 = Questions4.filter(age__gte=18,age__lte=28).values_list('registered_your_sim_card').annotate(Count('id'))
				registered_your_sim_card2PSQ4 = Questions4.filter(age__gte=29,age__lte=39).values_list('registered_your_sim_card').annotate(Count('id'))
				registered_your_sim_card3PSQ4 = Questions4.filter(age__gte=40,age__lte=49).values_list('registered_your_sim_card').annotate(Count('id'))
				registered_your_sim_card4PSQ4 = Questions4.filter(age__gte=50,age__lte=59).values_list('registered_your_sim_card').annotate(Count('id'))
				registered_your_sim_card5PSQ4 = Questions4.filter(age__gte=60).values_list('registered_your_sim_card').annotate(Count('id'))
				# registered_your_sim_card6PSQ4 = Questions4.filter(age__gte=48,age__lte=57).values_list('registered_your_sim_card').annotate(Count('id'))
				# registered_your_sim_card7PSQ4 = Questions4.filter(age__gte=56,age__lte=60).values_list('registered_your_sim_card').annotate(Count('id'))

				# delay_in_issuance_Ghana_card_affected_Sim_registration
				diigcasr1PSQ4 = Questions4.filter(age__gte=18,age__lte=28).values_list('delay_in_issuance_Ghana_card_affected_Sim_registration').annotate(Count('id'))
				diigcasr2PSQ4 = Questions4.filter(age__gte=29,age__lte=39).values_list('delay_in_issuance_Ghana_card_affected_Sim_registration').annotate(Count('id'))
				diigcasr3PSQ4 = Questions4.filter(age__gte=40,age__lte=49).values_list('delay_in_issuance_Ghana_card_affected_Sim_registration').annotate(Count('id'))
				diigcasr4PSQ4 = Questions4.filter(age__gte=50,age__lte=59).values_list('delay_in_issuance_Ghana_card_affected_Sim_registration').annotate(Count('id'))
				diigcasr5PSQ4 = Questions4.filter(age__gte=60).values_list('delay_in_issuance_Ghana_card_affected_Sim_registration').annotate(Count('id'))
				# diigcasr6PSQ4 = Questions4.filter(age__gte=48,age__lte=57).values_list('delay_in_issuance_Ghana_card_affected_Sim_registration').annotate(Count('id'))
				# diigcasr7PSQ4 = Questions4.filter(age__gte=56,age__lte=60).values_list('delay_in_issuance_Ghana_card_affected_Sim_registration').annotate(Count('id'))
				# ####################### END OF Q4 #####################

				#  chart counts
				totalResponse_Presurvey = presurvey.count()
				totalResponse_questionnaire = Questions.count()
				totalResponse_questionnaire2 = Questions2.count()
				totalResponse_questionnaire4 = Questions4.count()
				totalResponse_Postsurvey = postsurvey.count()

				# male and femle counts
				presurveyMaleFemale = presurvey.values('sex').annotate(Count('id'))
				QuestionsMaleFemale = Questions.values('sex').annotate(Count('id'))
				Questions2MaleFemale = Questions2.values('sex').annotate(Count('id'))
				Questions4MaleFemale = Questions4.values('sex').annotate(Count('id'))
				postsurveyMaleFemale = postsurvey.values('sex').annotate(Count('id'))
				# print(presurveyMaleFemale)
								
				

				data = {
						'pre':render_to_string('portal/qnewpreAge.html',locals()),
						'questionaire':render_to_string('portal/qnewquesAge.html',locals()),
						'questionaire2':render_to_string('portal/qnewquesAge2.html',locals()),
						'questionaire4':render_to_string('portal/qnewquesAge4.html',locals()),
						'post':render_to_string('portal/newpostAge.html',locals())
						}
			if otherFields[2] == 'Education': 
				print('education')
				# ############################# PRESURVEY ###22
				######################
				# engaged in any economic activity
				yesAnyEconomyEducationSheet = presurvey.filter(engaged_in_any_economy='Yes').values_list('education_level').annotate(Count('id'))
				noAnyEconomyEducationSheet = presurvey.filter(engaged_in_any_economy='No').values_list('education_level').annotate(Count('id'))

				# what economic_activity_engaged_in
				EngagedActivity_notWorking = presurvey.filter(economic_activity_engaged_in='Not working').values_list('education_level').annotate(Count('id'))
				EngagedActivity_privateSector = presurvey.filter(economic_activity_engaged_in='Private sector').values_list('education_level').annotate(Count('id'))
				EngagedActivity_publicSector = presurvey.filter(economic_activity_engaged_in='Public sector').values_list('education_level').annotate(Count('id'))
				EngagedActivity_student = presurvey.filter(economic_activity_engaged_in='Student').values_list('education_level').annotate(Count('id'))
				EngagedActivity_selfEmployed = presurvey.filter(economic_activity_engaged_in='Self-employed').values_list('education_level').annotate(Count('id'))

				# Are you aware of the Government’s decision to introduce the e-levy tax?
				awareOfElevy_yes = presurvey.filter(aware_of_elevy_introduction='Yes').values_list('education_level').annotate(Count('id'))
				awareOfElevy_no = presurvey.filter(aware_of_elevy_introduction='No').values_list('education_level').annotate(Count('id'))
				awareOfElevy_indifference = presurvey.filter(aware_of_elevy_introduction='Indifferent').values_list('education_level').annotate(Count('id'))

				# # support_elevy_introduction
				support_elevy_introduction_yes = presurvey.filter(support_Governments_decision_introduce_elevy='Yes').values_list('education_level').annotate(Count('id'))
				support_elevy_introduction_no = presurvey.filter(support_Governments_decision_introduce_elevy='No').values_list('education_level').annotate(Count('id'))
				support_elevy_introduction_indifference = presurvey.filter(support_Governments_decision_introduce_elevy='Indifferent').values_list('education_level').annotate(Count('id'))

				#gov_considered_other_area_instead_elevy
				gov_considered_other_area_instead_elevy_yes = presurvey.filter(gov_considered_other_area_instead_elevy='Yes').values_list('education_level').annotate(Count('id'))
				gov_considered_other_area_instead_elevy_no = presurvey.filter(gov_considered_other_area_instead_elevy='No').values_list('education_level').annotate(Count('id'))
				gov_considered_other_area_instead_elevy_indifference = presurvey.filter(gov_considered_other_area_instead_elevy='Indifferent').values_list('education_level').annotate(Count('id'))


				# Do you think the e-levy will affect the businesses of mobile money vendors?
				elevy_affect_momo_business_yes = presurvey.filter(elevy_affect_momo_business='Yes').values_list('education_level').annotate(Count('id'))
				elevy_affect_momo_business_no = presurvey.filter(elevy_affect_momo_business='No').values_list('education_level').annotate(Count('id'))
				elevy_affect_momo_business_indifference = presurvey.filter(elevy_affect_momo_business='Indifferent').values_list('education_level').annotate(Count('id'))
				
				# Do you think the collection of the e-levy tax would help the Government achieve the 
				collection_elevy_help_govenment_yes = presurvey.filter(collection_elevy_help_govenment='Yes').values_list('education_level').annotate(Count('id'))
				collection_elevy_help_govenment_no = presurvey.filter(collection_elevy_help_govenment='No').values_list('education_level').annotate(Count('id'))
				collection_elevy_help_govenment_indifference = presurvey.filter(collection_elevy_help_govenment='Indifferent').values_list('education_level').annotate(Count('id'))
				
				# In your opinion, do you see the e-levy tax as the best way to increase revenue for the 
				ur_opinion_elevey_increase_revenue_yes = presurvey.filter(do_you_see_the_elevy_bestway_increase_revenue='Yes').values_list('education_level').annotate(Count('id'))
				ur_opinion_elevey_increase_revenue_no = presurvey.filter(do_you_see_the_elevy_bestway_increase_revenue='No').values_list('education_level').annotate(Count('id'))
				ur_opinion_elevey_increase_revenue_yes_indifference = presurvey.filter(do_you_see_the_elevy_bestway_increase_revenue='Indifferent').values_list('education_level').annotate(Count('id'))
				
				##################### END OF PRESURVEY ##########################

				# ###################  QUESTIONNAIRE ########################### 
				# engaged in any economic activity
				yesAnyEconomyEducationSheetQ = Questions.filter(engaged_in_any_economy='YES').values_list('education_level').annotate(Count('id'))
				noAnyEconomyEducationSheetQ = Questions.filter(engaged_in_any_economy='NO').values_list('education_level').annotate(Count('id'))
				# print(yesAnyEconomyEducationSheetQ)
				# print(noAnyEconomyEducationSheetQ)

				# what economic_activity_engaged_in
				EngagedActivity_NONEQ = Questions.filter(economic_activity_engaged_in='NOT WORKING').values_list('education_level').annotate(Count('id'))
				EngagedActivity_privateSectorQ = Questions.filter(economic_activity_engaged_in='PRIVATE SECTOR').values_list('education_level').annotate(Count('id'))
				EngagedActivity_publicSectorQ = Questions.filter(economic_activity_engaged_in='PUBLIC SECTOR').values_list('education_level').annotate(Count('id'))
				EngagedActivity_studentQ = Questions.filter(economic_activity_engaged_in='STUDENT').values_list('education_level').annotate(Count('id'))
				EngagedActivity_selfEmployedQ = Questions.filter(economic_activity_engaged_in='SELF EMPLOYED').values_list('education_level').annotate(Count('id'))
				EngagedActivity_OTHERSQ = Questions.filter(economic_activity_engaged_in='OTHERS').values_list('education_level').annotate(Count('id'))

				# Do you think it is a call in the right direction?
				do_u_think_is_ryt_direction_yes = Questions.filter(do_u_think_is_ryt_direction='YES').values_list('education_level').annotate(Count('id'))
				do_u_think_is_ryt_direction_no = Questions.filter(do_u_think_is_ryt_direction='NO').values_list('education_level').annotate(Count('id'))
				do_u_think_is_ryt_direction_indifference = Questions.filter(do_u_think_is_ryt_direction='INDIFFERENT').values_list('education_level').annotate(Count('id'))

				# aware_of_suspension_of_the_referendum
				aware_of_suspension_of_the_referendum_yes = Questions.filter(aware_of_suspension_of_the_referendum='YES').values_list('education_level').annotate(Count('id'))
				aware_of_suspension_of_the_referendum_no = Questions.filter(aware_of_suspension_of_the_referendum='NO').values_list('education_level').annotate(Count('id'))
				aware_of_suspension_of_the_referendum_indifference = Questions.filter(aware_of_suspension_of_the_referendum='INDIFFERENT').values_list('education_level').annotate(Count('id'))

				################# END OF QUESTIONNAIRE 1 ####################

				# ###################  QUESTIONNAIRE 2 #########################
				# engaged in any economic activity
				yesAnyEconomyEducationSheetQ2 = Questions2.filter(engaged_in_any_economy='Yes').values_list('education_level').annotate(Count('id'))
				noAnyEconomyEducationSheetQ2 = Questions2.filter(engaged_in_any_economy='No').values_list('education_level').annotate(Count('id'))
				# print(yesAnyEconomyEducationSheetQ)
				# print(noAnyEconomyEducationSheetQ)

				# what economic_activity_engaged_in
				EngagedActivity_NONEQ2 = Questions2.filter(economic_activity_engaged_in='Not working').values_list('education_level').annotate(Count('id'))
				EngagedActivity_privateSectorQ2 = Questions2.filter(economic_activity_engaged_in='Private sector').values_list('education_level').annotate(Count('id'))
				EngagedActivity_publicSectorQ2 = Questions2.filter(economic_activity_engaged_in='Public sector').values_list('education_level').annotate(Count('id'))
				EngagedActivity_studentQ2 = Questions2.filter(economic_activity_engaged_in='Student').values_list('education_level').annotate(Count('id'))
				EngagedActivity_selfEmployedQ2 = Questions2.filter(economic_activity_engaged_in='Self-employed').values_list('education_level').annotate(Count('id'))
				EngagedActivity_OTHERSQ2 = Questions2.filter(economic_activity_engaged_in='Others').values_list('education_level').annotate(Count('id'))

				# aware_the_easing_restrictions_by_president
				aterbp_yes = Questions2.filter(aware_the_easing_restrictions_by_president='Yes').values_list('education_level').annotate(Count('id'))
				aterbp_no = Questions2.filter(aware_the_easing_restrictions_by_president='No').values_list('education_level').annotate(Count('id'))
				aterbp_indifferent = Questions2.filter(aware_the_easing_restrictions_by_president='Indifferent').values_list('education_level').annotate(Count('id'))


				# think_easing_restrictions_by_president_call_right_direction
				terbpcrd_yes = Questions2.filter(think_easing_restrictions_by_president_call_right_direction='Yes').values_list('education_level').annotate(Count('id'))
				terbpcrd_no = Questions2.filter(think_easing_restrictions_by_president_call_right_direction='No').values_list('education_level').annotate(Count('id'))
				terbpcrd_indifferent = Questions2.filter(think_easing_restrictions_by_president_call_right_direction='Indifferent').values_list('education_level').annotate(Count('id'))

				# have_confidence_in_government_handling_risk_covid19
				hcighrc_yes = Questions2.filter(have_confidence_in_government_handling_risk_covid19='Yes').values_list('education_level').annotate(Count('id'))
				hcighrc_no = Questions2.filter(have_confidence_in_government_handling_risk_covid19='No').values_list('education_level').annotate(Count('id'))
				hcighrc_indifferent = Questions2.filter(have_confidence_in_government_handling_risk_covid19='Indifferent').values_list('education_level').annotate(Count('id'))

				# how_would_you_rate_government_handling_covid19
				hwyrghc_g = Questions2.filter(how_would_you_rate_government_handling_covid19='Good').values_list('education_level').annotate(Count('id'))
				hwyrghc_f = Questions2.filter(how_would_you_rate_government_handling_covid19='Fair').values_list('education_level').annotate(Count('id'))
				hwyrghc_vg = Questions2.filter(how_would_you_rate_government_handling_covid19='Very Good').values_list('education_level').annotate(Count('id'))
				hwyrghc_ex = Questions2.filter(how_would_you_rate_government_handling_covid19='Excellent').values_list('education_level').annotate(Count('id'))
				hwyrghc_p = Questions2.filter(how_would_you_rate_government_handling_covid19='Poor').values_list('education_level').annotate(Count('id'))

				################# END OF QUESTIONNAIRE 2 #####################

				########################## Postsurvey
				# engaged in any economic activity
				yesAnyEconomyEducationSheetPS = postsurvey.filter(engaged_in_any_economy='Yes').values_list('education_level').annotate(Count('id'))
				noAnyEconomyEducationSheetPS = postsurvey.filter(engaged_in_any_economy='No').values_list('education_level').annotate(Count('id'))
				
				# what economic_activity_engaged_in
				EngagedActivity_notWorkingPS = postsurvey.filter(economic_activity_engaged_in='Not working').values_list('education_level').annotate(Count('id'))
				EngagedActivity_privateSectorPS = postsurvey.filter(economic_activity_engaged_in='Private sector').values_list('education_level').annotate(Count('id'))
				EngagedActivity_publicSectorPS = postsurvey.filter(economic_activity_engaged_in='Public sector').values_list('education_level').annotate(Count('id'))
				EngagedActivity_studentPS = postsurvey.filter(economic_activity_engaged_in='Student').values_list('education_level').annotate(Count('id'))
				EngagedActivity_selfEmployedPS = postsurvey.filter(economic_activity_engaged_in='Self-employed').values_list('education_level').annotate(Count('id'))
				EngagedActivity_othersPS = postsurvey.filter(economic_activity_engaged_in='Others').values_list('education_level').annotate(Count('id'))
				
				# # Did you listen and understand the presentations made by the Finance Minister as well as other Government Officials on the e-levy?
				listen_n_understand_finance_minister_yes = postsurvey.filter(listen_n_understand_finance_minister='Yes').values_list('education_level').annotate(Count('id'))
				listen_n_understand_finance_minister_no = postsurvey.filter(listen_n_understand_finance_minister='No').values_list('education_level').annotate(Count('id'))
				listen_n_understand_finance_minister_indifference = postsurvey.filter(listen_n_understand_finance_minister='Indifferent').values_list('education_level').annotate(Count('id'))
				
				# changed_your_perception_about_the_elevy
				changed_your_perception_about_the_elevy_yes = postsurvey.filter(changed_your_perception_about_the_elevy='Yes').values_list('education_level').annotate(Count('id'))
				changed_your_perception_about_the_elevy_no = postsurvey.filter(changed_your_perception_about_the_elevy='No').values_list('education_level').annotate(Count('id'))
				changed_your_perception_about_the_elevy_indifference = postsurvey.filter(changed_your_perception_about_the_elevy='Indifferent').values_list('education_level').annotate(Count('id'))
				
				# think_the_Government_should_increase_the_threshold   new change
				should_government_increase_the_threshold_yes = postsurvey.filter(think_the_Government_should_increase_the_threshold='Yes').values_list('education_level').annotate(Count('id'))
				should_government_increase_the_threshold_no = postsurvey.filter(think_the_Government_should_increase_the_threshold='No').values_list('education_level').annotate(Count('id'))
				should_government_increase_the_threshold_indifference = postsurvey.filter(think_the_Government_should_increase_the_threshold='Indifferent').values_list('education_level').annotate(Count('id'))
			
				# government_should_reduce_rate_allotted_elevy
				should_the_government_reduce_elevy_tax_yes = postsurvey.filter(government_should_reduce_rate_allotted_elevy='Yes').values_list('education_level').annotate(Count('id'))
				should_the_government_reduce_elevy_tax_no = postsurvey.filter(government_should_reduce_rate_allotted_elevy='No').values_list('education_level').annotate(Count('id'))
				should_the_government_reduce_elevy_tax_indifference = postsurvey.filter(government_should_reduce_rate_allotted_elevy='Indifferent').values_list('education_level').annotate(Count('id'))
				
				# collection_elevy_help_govenment   new change
				has_there_been_enough_sensitization_yes = postsurvey.filter(enough_sensitization_elevy='Yes').values_list('education_level').annotate(Count('id'))
				has_there_been_enough_sensitization_no = postsurvey.filter(enough_sensitization_elevy='No').values_list('education_level').annotate(Count('id'))
				has_there_been_enough_sensitization_indifference = postsurvey.filter(enough_sensitization_elevy='Indifferent').values_list('education_level').annotate(Count('id'))
			
				# has_there_been_enough_sensitization
				enough_publicity_about_today_Town_Hall_Meeting_yes = postsurvey.filter(enough_publicity_about_today_Town_Hall_Meeting='Yes').values_list('education_level').annotate(Count('id'))
				enough_publicity_about_today_Town_Hall_Meeting_no = postsurvey.filter(enough_publicity_about_today_Town_Hall_Meeting='No').values_list('education_level').annotate(Count('id'))
				enough_publicity_about_today_Town_Hall_Meeting_indifference = postsurvey.filter(enough_publicity_about_today_Town_Hall_Meeting='Indifferent').values_list('education_level').annotate(Count('id'))
				
				######################### END OF POST SURVEY ###############

				#####################  QUESTIONNAIRE 4 ###########################
				# engaged in any economic activity
				yesAnyEconomyEducationSheetQ4 = Questions4.filter(engaged_in_any_economy='Yes').values_list('education_level').annotate(Count('id'))
				noAnyEconomyEducationSheetQ4 = Questions4.filter(engaged_in_any_economy='No').values_list('education_level').annotate(Count('id'))
				# print(yesAnyEconomyEducationSheetQ)
				# print(noAnyEconomyEducationSheetQ)

				# what economic_activity_engaged_in
				EngagedActivity_NONEQ4 = Questions4.filter(economic_activity_engaged_in='Not working').values_list('education_level').annotate(Count('id'))
				EngagedActivity_privateSectorQ4 = Questions4.filter(economic_activity_engaged_in='Private sector').values_list('education_level').annotate(Count('id'))
				EngagedActivity_publicSectorQ4 = Questions4.filter(economic_activity_engaged_in='Public sector').values_list('education_level').annotate(Count('id'))
				EngagedActivity_studentQ4 = Questions4.filter(economic_activity_engaged_in='Student').values_list('education_level').annotate(Count('id'))
				EngagedActivity_selfEmployedQ4 = Questions4.filter(economic_activity_engaged_in='Self-employed').values_list('education_level').annotate(Count('id'))
				EngagedActivity_OTHERSQ4 = Questions4.filter(economic_activity_engaged_in='Others').values_list('education_level').annotate(Count('id'))

				# registered_your_sim_card   new change
				registered_your_sim_card_yes = Questions4.filter(registered_your_sim_card='Yes').values_list('education_level').annotate(Count('id'))
				registered_your_sim_card_no = Questions4.filter(registered_your_sim_card='No').values_list('education_level').annotate(Count('id'))
				registered_your_sim_card_indifference = Questions4.filter(registered_your_sim_card='Indifferent').values_list('education_level').annotate(Count('id'))

				# delay_in_issuance_Ghana_card_affected_Sim_registration   new change
				diigcasr_yes = Questions4.filter(delay_in_issuance_Ghana_card_affected_Sim_registration='Yes').values_list('education_level').annotate(Count('id'))
				diigcasr_no = Questions4.filter(delay_in_issuance_Ghana_card_affected_Sim_registration='No').values_list('education_level').annotate(Count('id'))
				diigcasr_indifference = Questions4.filter(delay_in_issuance_Ghana_card_affected_Sim_registration='Indifferent').values_list('education_level').annotate(Count('id'))
				################### END OF QUESTIONNAIRE 4 #####################

				#  chart counts
				totalResponse_Presurvey = presurvey.count()
				totalResponse_questionnaire = Questions.count()
				totalResponse_questionnaire2 = Questions2.count()
				totalResponse_questionnaire4 = Questions4.count()
				totalResponse_Postsurvey = postsurvey.count()

				# male and femle counts
				presurveyMaleFemale = presurvey.values('sex').annotate(Count('id'))
				QuestionsMaleFemale = Questions.values('sex').annotate(Count('id'))
				Questions2MaleFemale = Questions2.values('sex').annotate(Count('id'))
				Questions4MaleFemale = Questions4.values('sex').annotate(Count('id'))
				postsurveyMaleFemale = postsurvey.values('sex').annotate(Count('id'))

				data = {
						'pre':render_to_string('portal/newpreEducation.html',locals()),
						'questionaire':render_to_string('portal/newquesEducation.html',locals()),
						'questionaire2':render_to_string('portal/newquesEducation2.html',locals()),
						'questionaire4':render_to_string('portal/newquesEducation4.html',locals()),
						'post':render_to_string('portal/newpostEducation.html',locals())
						}

		return JsonResponse(data)



























	# # ########engaged_in_any_economy
	# # anyEconomy = presurvey.values('engaged_in_any_economy').annotate(Count('id'))



	# # #########economic_activity_engaged_in
	# # engagedActivity = presurvey.values('economic_activity_engaged_in').annotate(Count('id'))
	# ################ education_level
	# # educationlevel = presurvey.values('education_level').annotate(Count('id'))
	# ##############3 aware_of_elevy_introduction
	# # awareOfElevy = presurvey.values('aware_of_elevy_introduction').annotate(Count('id'))
	# ############ support_elevy_introduction
	# # supportElevy = presurvey.values('support_elevy_introduction').annotate(Count('id'))
	# ############# gov_considered_other_area_instead_elevy
	# if_no_why = presurvey.values('gov_considered_other_area_instead_elevy')

	# # should_government_increase_tax_or_elevy
	# shouldIncreaseElevy = presurvey.values('should_government_increase_tax_or_elevy').annotate(Count('id'))
	# # elevy_affect_momo_business
	# affectMomoBusiness = presurvey.values('elevy_affect_momo_business').annotate(Count('id'))

	# # print("ernest")

	# # print(affectMomoBusiness)

	# # print("ernest")
	# # collection_elevy_help_govenment
	# willCollectionHelp = presurvey.values('collection_elevy_help_govenment').annotate(Count('id'))
	# # ur_opinion_elevey_increase_revenue
	# yourOpinionIncrease = presurvey.values('ur_opinion_elevey_increase_revenue').annotate(Count('id'))

	# # questionaire chart details
	# # engaged_in_any_economy
	# anyEconomy_q = Questions.values('engaged_in_any_economy').annotate(Count('id'))
	# # economic_activity_engaged_in
	# engagedActivity_q = Questions.values('economic_activity_engaged_in').annotate(Count('id'))
	# # education_level
	# educationlevel_q = Questions.values('education_level').annotate(Count('id'))
	# # aware_of_suspension_of_the_referendum
	# aware_of_suspension_of_the_referendum = Questions.values('aware_of_suspension_of_the_referendum').annotate(Count('id'))
	# # if_no_why
	# why_not_aware = Questions.values('why_not_aware').annotate(Count('id'))
	# # why_do_u_think_is_ryt_direction
	# do_u_think_is_ryt_direction = Questions.values('do_u_think_is_ryt_direction').annotate(Count('id'))
	# # no_why_do_u_think_is_ryt_direction
	# no_why_do_u_think_is_ryt_direction = Questions.values('no_why_do_u_think_is_ryt_direction').annotate(Count('id'))
	

	# # postsurvey chart details
	# # engaged_in_any_economy
	# anyEconomy_p = postsurvey.values('engaged_in_any_economy').annotate(Count('id'))
	# # economic_activity_engaged_in
	# engagedActivity_p = postsurvey.values('economic_activity_engaged_in').annotate(Count('id'))
	# # education_level
	# educationlevel_p = postsurvey.values('education_level').annotate(Count('id'))
	# # Did you listen and understand the presentations made by the Finance Minister as well as other Government Officials on the e-levy?
	# listen_n_understand_finance_minister = postsurvey.values('listen_n_understand_finance_minister').annotate(Count('id'))
	# # changed_your_perception_about_the_elevy
	# changed_your_perception_about_the_elevy = postsurvey.values('changed_your_perception_about_the_elevy').annotate(Count('id'))
	# # should_government_increase_the_threshold
	# should_government_increase_the_threshold = postsurvey.values('should_government_increase_the_threshold').annotate(Count('id'))
	# # should_the_government_reduce_elevy_tax
	# should_the_government_reduce_elevy_tax = postsurvey.values('should_the_government_reduce_elevy_tax').annotate(Count('id'))
	# # has_there_been_enough_sensitization
	# has_there_been_enough_sensitization = postsurvey.values('has_there_been_enough_sensitization').annotate(Count('id'))
	# # enough_publicity_about_today_Town_Hall_Meeting
	# enough_publicity_about_today_Town_Hall_Meeting = postsurvey.values('enough_publicity_about_today_Town_Hall_Meeting').annotate(Count('id'))