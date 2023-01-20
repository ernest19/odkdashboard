from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.``
class preSurvey(models.Model):#Questionaire3A
	region = models.CharField(max_length=2000,null=True,blank=True) #Region	
	district = models.CharField(max_length=2000,null=True,blank=True)#District
	dio_name= models.CharField(max_length=2000,null=True,blank=True)
	dio_contact = models.CharField(max_length=2000,null=True,blank=True)
	sex = models.CharField(max_length=2000)#Sex
	age = models.IntegerField()#Age	
	engaged_in_any_economy = models.CharField(max_length=2000,null=True,blank=True)#Are You Engaged in Any Economic Activity?
	economic_activity_engaged_in = models.CharField(max_length=2000,null=True,blank=True)#What type of Economic activity are you Engaged in?
	education_level = models.CharField(max_length=2000,null=True,blank=True)#What is your Level of Education?
	aware_of_elevy_introduction = models.CharField(max_length=2000,null=True,blank=True)#Are you aware of the Government’s decision to introduce the e-levy tax?	
	support_Governments_decision_introduce_elevy = models.CharField(max_length=2000,null=True,blank=True)#if yes, do you support Government’s decision to introduce the e-levy tax?
	if_no_why_support_Governments_decision_introduce_elevy= models.CharField(max_length=2000,null=True,blank=True)#if no, do you support Government’s decision
	gov_considered_other_area_instead_elevy = models.CharField(max_length=2000,null=True,blank=True)#If No, Why	
	elevy_affect_momo_business = models.CharField(max_length=2000,null=True,blank=True)#Do you think the e-levy will affect the businesses of mobile money vendors?	
	reason_elevy_affect_momo_business_opinion = models.CharField(max_length=500,null=True,blank=True)
	collection_elevy_help_govenment = models.CharField(max_length=500,null=True,blank=True)#Do you think the collection of the e-levy tax would help the Government achieve the
	why_wont_collection_elevy_help_govenment = models.CharField(max_length=2000,null=True,blank=True)#Give reasons for your opinion
	do_you_see_the_elevy_bestway_increase_revenue= models.CharField(max_length=2000,null=True,blank=True)# do you see the e-levy tax as the best way to increase revenue for the state
	reasons_elevy_bestway_increase_revenue = models.CharField(max_length=500,null=True,blank=True)# Give reasons for your opinion
	gps_of_structure = models.CharField(max_length=500,null=True,blank=True)#GPS of structure
	name_of_respondent = models.CharField(max_length=2000,null=True,blank=True)
	contact_of_respondent = models.CharField(max_length=2000,null=True,blank=True)
	entry_date = models.DateTimeField(auto_now=False,null=True,blank=True)
	created_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Questionaire3A"
	
	



class Questionaire1(models.Model):
	region = models.CharField(max_length=2000,null=True,blank=True)#Region
	district = models.CharField(max_length=2000,null=True,blank=True)#District
	dio_name= models.CharField(max_length=2000)
	dio_contact = models.CharField(max_length=2000)
	sex = models.CharField(max_length=2000,null=True,blank=True)#Sex
	age = models.IntegerField()#Age
	engaged_in_any_economy = models.CharField(max_length=2000,null=True,blank=True)#Are You Engaged in Any Economic Activity?	
	economic_activity_engaged_in = models.CharField(max_length=2000,null=True,blank=True)#What type of Economic activity are you Engaged in?	
	education_level = models.CharField(max_length=2000,null=True,blank=True)#What is your Level of Education?	
	aware_of_suspension_of_the_referendum = models.CharField(max_length=2000,null=True,blank=True)#Are you aware of the suspension of the referendum?	
	why_not_aware = models.CharField(max_length=2000,null=True,blank=True) #if no why
	do_u_think_is_ryt_direction = models.CharField(max_length=2000,null=True,blank=True)#Do you think it is a call in the right direction? 
	no_why_do_u_think_is_ryt_direction = models.CharField(max_length=2000,null=True,blank=True)#If No why
	created_date = models.DateTimeField(auto_now=True)

class Questionaire2(models.Model):
	region = models.CharField(max_length=2000,null=True,blank=True)#Region
	district = models.CharField(max_length=2000,null=True,blank=True)#District
	dio_name= models.CharField(max_length=2000)
	dio_contact = models.CharField(max_length=2000)
	sex = models.CharField(max_length=2000,null=True,blank=True)#Sex
	age = models.IntegerField()#Age
	engaged_in_any_economy = models.CharField(max_length=2000,null=True,blank=True)#Are You Engaged in Any Economic Activity?	
	economic_activity_engaged_in = models.CharField(max_length=2000,null=True,blank=True)#What type of Economic activity are you Engaged in?	
	education_level = models.CharField(max_length=2000,null=True,blank=True)#What is your Level of Education?

	aware_the_easing_restrictions_by_president = models.CharField(max_length=500,null=True,blank=True)#Are you aware of the easing of restrictions by the president?
	think_easing_restrictions_by_president_call_right_direction = models.CharField(max_length=500,null=True,blank=True)# If yes, do you think the easing of restrictions by the President is a call in the right direction?	If No, why?	
	if_no_why_think_easing_restrict_by_president_call_right_direct = models.CharField(max_length=500,null=True,blank=True)# If No, Why
	have_confidence_in_government_handling_risk_covid19 = models.CharField(max_length=2000,null=True,blank=True)#Do you have confidence in how government is handling the risk of covid-19?
	if_no_why_have_confidence_in_government_handling_risk_covid19 = models.CharField(max_length=2000,null=True,blank=True)#Do you have confidence in how government is handling the risk of covid-19?
	how_would_you_rate_government_handling_covid19 = models.CharField(max_length=500,null=True,blank=True) #On a scale of 1-5, how would you rate government’s handling of the covid-19 response programme?CONTACT OF RESPONDENT (OPTIONAL)	
	contact_of_respondent = models.CharField(max_length=2000,null=True,blank=True)
	



class postSurvey(models.Model):#Questionaire3B
	region = models.CharField(max_length=2000,null=True,blank=True)#Region
	district = models.CharField(max_length=2000,null=True,blank=True)#District
	dio_name= models.CharField(max_length=2000,null=True,blank=True)
	dio_contact = models.CharField(max_length=2000,null=True,blank=True)
	sex = models.CharField(max_length=2000,null=True,blank=True)#Sex
	age = models.IntegerField(null=True,blank=True)#Age
	engaged_in_any_economy = models.CharField(max_length=2000,null=True,blank=True)#Are You Engaged in Any Economic Activity?	
	economic_activity_engaged_in = models.CharField(max_length=2000,null=True,blank=True)#What type of Economic activity are you Engaged in?	
	education_level = models.CharField(max_length=2000,null=True,blank=True)#What is your Level of Education?	

	listen_n_understand_finance_minister = models.CharField(max_length=2000,null=True,blank=True)#Did you listen and understand the presentations made by the Finance Minister as well as other Government Officials on the e-levy?
	changed_your_perception_about_the_elevy = models.CharField(max_length=2000,null=True,blank=True)#If you did, has it changed your perception about the e-levy?
	reasons_for_changed_your_perception_about_the_elevy = models.CharField(max_length=2000,null=True,blank=True)#Give reasons for your opinion.

	think_the_Government_should_increase_the_threshold = models.CharField(max_length=2000,null=True,blank=True)#Do you think the Government should increase the threshold (minimum amount) from Ghc 100?
	give_reason_for_your_opinion_increase_the_threshold =  models.CharField(max_length=500,null=True,blank=True)
	government_should_reduce_rate_allotted_elevy=  models.CharField(max_length=500,null=True,blank=True) #Do you think the Government should reduce the 1.75% rate allotted for the e-levy tax?	
	reason_reduce_rate_allotted_elevy =  models.CharField(max_length=500,null=True,blank=True)#Give reasons for your opinion 	
	enough_sensitization_elevy=  models.CharField(max_length=500,null=True,blank=True)#Has there been enough sensitization on the e-levy?		
	enough_publicity_about_today_Town_Hall_Meeting = models.CharField(max_length=2000,null=True,blank=True)#Was there enough publicity about today’s Town Hall Meeting_
	reason_publicity_about_today_Town_Hall_Meeting =  models.CharField(max_length=500,null=True,blank=True)#Give reasons for your opinion	publicity_about_today_Town_Hall_Meeting
	gps_of_structure = models.CharField(max_length=500,null=True,blank=True)#GPS of structure
	name_of_respondent = models.CharField(max_length=2000,null=True,blank=True)
	contact_of_respondent = models.CharField(max_length=2000,null=True,blank=True)
	entry_date = models.DateTimeField(auto_now=False,null=True,blank=True)
	created_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Questionaire3B"



class Questionaire4(models.Model):
	region = models.CharField(max_length=2000,null=True,blank=True)#Region
	district = models.CharField(max_length=2000,null=True,blank=True)#District
	dio_name= models.CharField(max_length=2000,null=True,blank=True)
	dio_contact = models.CharField(max_length=2000,null=True,blank=True)
	sex = models.CharField(max_length=2000,null=True,blank=True)#Sex
	age = models.IntegerField(null=True,blank=True)#Age
	engaged_in_any_economy = models.CharField(max_length=2000,null=True,blank=True)#Are You Engaged in Any Economic Activity?	
	economic_activity_engaged_in = models.CharField(max_length=2000,null=True,blank=True)#What type of Economic activity are you Engaged in?	
	education_level = models.CharField(max_length=2000,null=True,blank=True)#What is your Level of Education?	

	registered_your_sim_card = models.CharField(max_length=2000,null=True,blank=True)#Have you registered your sim card?	
	delay_in_issuance_Ghana_card_affected_Sim_registration = models.CharField(max_length=2000,null=True,blank=True)#Do you think the delay in the issuance of the Ghana card has affected the Sim card registration?	CONTACT OF RESPONDENT (OPTIONAL


class welcomeMessage(models.Model):
	message =  RichTextField()
	date=models.DateField(null=True,blank=True)


class QuestionaireInfo(models.Model):
	title = models.CharField(max_length=2000,null=True,blank=True)
	description =  RichTextField()

