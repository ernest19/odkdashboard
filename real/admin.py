# from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
# from .models import *

# from import_export import resources
# from import_export.admin import ImportExportModelAdmin
# from django.contrib.auth.decorators import login_required



# class welcomeMessageAdmin(admin.ModelAdmin):
#     list_display = ['message','date']
#     # search_fields = ['skill_fk','mentee']
# admin.site.register(welcomeMessage, welcomeMessageAdmin)



# class QuestionaireInfoAdmin(admin.ModelAdmin):
#     list_display = ['title','description']
#     # search_fields = ['skill_fk','mentee']
# admin.site.register(QuestionaireInfo, QuestionaireInfoAdmin)

# # class postSurveyResource(resources.ModelResource):

# # 	class Meta:

# # 		model = postSurvey
# # 		fields =["region","district","sex","age","engaged_in_any_economy","economic_activity_engaged_in","education_level","listen_n_understand_finance_minister","changed_your_perception_about_the_elevy","should_government_increase_the_threshold","should_the_government_reduce_elevy_tax","has_there_been_enough_sensitization","enough_publicity_about_today_Town_Hall_Meeting"]
# # 		# search_fields = ['region','district']
			
# # 		search_fields = ['region','district']


# # class adminpostSurvey(ImportExportModelAdmin):
# # 	resource_class = postSurveyResource,
# # 	list_display = ["region","district","sex","age","engaged_in_any_economy","economic_activity_engaged_in","education_level","listen_n_understand_finance_minister","changed_your_perception_about_the_elevy","should_government_increase_the_threshold","should_the_government_reduce_elevy_tax","has_there_been_enough_sensitization","enough_publicity_about_today_Town_Hall_Meeting"]
# # 	search_fields = ['region','district']
# # admin.site.register(postSurvey, adminpostSurvey)


# # class preSurveyResource(resources.ModelResource):

# # 	class Meta:

# # 		model = preSurvey
# # 		fields =("id","region","district","sex","age","engaged_in_any_economy","economic_activity_engaged_in","education_level","aware_of_elevy_introduction","support_elevy_introduction","gov_considered_other_area_instead_elevy","elevy_affect_momo_business","collection_elevy_help_govenment","ur_opinion_elevey_increase_revenue" )
# # 		# exclude = ('id',)
# # 		import_id_fields = ['id']
# # 		search_fields = ("region","district")


# class preSurveyAdmin(ImportExportModelAdmin):
# 	# resource_class = preSurveyResource
# 	list_display =("region","district","dio_name","dio_contact","sex","age","engaged_in_any_economy","economic_activity_engaged_in",'education_level',"aware_of_elevy_introduction",'support_Governments_decision_introduce_elevy',"if_no_why_support_Governments_decision_introduce_elevy","gov_considered_other_area_instead_elevy",'elevy_affect_momo_business',"reason_elevy_affect_momo_business_opinion",'collection_elevy_help_govenment',"why_wont_collection_elevy_help_govenment",'do_you_see_the_elevy_bestway_increase_revenue','reasons_elevy_bestway_increase_revenue','gps_of_structure','name_of_respondent','contact_of_respondent','entry_date','created_date')
# 	# exclude = ('id',)
# 	list_filter = ['engaged_in_any_economy']
# 	search_fields = ['region','district']

# admin.site.register(preSurvey, preSurveyAdmin)





# # class QuestionaireResource(resources.ModelResource):

# # 	class Meta:

# # 		model = Questionaire
# # 		fields =("id","region","region","sex","age","district","sex","age","engaged_in_any_economy","economic_activity_engaged_in","education_level","aware_of_suspension_of_the_referendum","why_do_u_think_is_ryt_direction","no_why_do_u_think_is_ryt_direction" )
# # 		# exclude = ('id',)
# # 		import_id_fields = ['id']
# # 		search_fields = ("region","district")


# class QuestionaireAdmin(ImportExportModelAdmin):
# 	# resource_class = QuestionaireResource
# 	list_display =("region","sex","age","district","sex","age","engaged_in_any_economy","economic_activity_engaged_in","education_level","aware_of_suspension_of_the_referendum",'why_not_aware',"do_u_think_is_ryt_direction","no_why_do_u_think_is_ryt_direction" )
# 	# exclude = ('id',)
# 	search_fields = ['region','district']

# admin.site.register(Questionaire1, QuestionaireAdmin)


# class Questionaire2Admin(ImportExportModelAdmin):
# 	# resource_class = QuestionaireResource
# 	list_display =("region","district","dio_name","dio_contact","sex","age","engaged_in_any_economy","economic_activity_engaged_in","education_level","aware_the_easing_restrictions_by_president",'think_easing_restrictions_by_president_call_right_direction',"have_confidence_in_government_handling_risk_covid19","if_no_why_have_confidence_in_government_handling_risk_covid19",'how_would_you_rate_government_handling_covid19' )
# 	# exclude = ('id',)
# 	search_fields = ['region','district']

# admin.site.register(Questionaire2, Questionaire2Admin)




# # class postSurveyResource(resources.ModelResource):

# # 	class Meta:

# # 		model = postSurvey
# # 		fields =("region","district","sex","age","engaged_in_any_economy","economic_activity_engaged_in","education_level","listen_n_understand_finance_minister","changed_your_perception_about_the_elevy","should_government_increase_the_threshold","should_the_government_reduce_elevy_tax","has_there_been_enough_sensitization","enough_publicity_about_today_Town_Hall_Meeting" )
# # 		# exclude = ('id',)
# # 		import_id_fields = ['id']
# # 		search_fields = ("region","district")


# class postSurveyAdmin(ImportExportModelAdmin):
# 	# resource_class = postSurveyResource
# 	list_display =("region","district","dio_name","dio_contact","sex","age","engaged_in_any_economy","economic_activity_engaged_in","education_level","listen_n_understand_finance_minister","changed_your_perception_about_the_elevy","think_the_Government_should_increase_the_threshold","give_reason_for_your_opinion_increase_the_threshold","government_should_reduce_rate_allotted_elevy","reason_reduce_rate_allotted_elevy","enough_sensitization_elevy","enough_publicity_about_today_Town_Hall_Meeting","reason_publicity_about_today_Town_Hall_Meeting","gps_of_structure","name_of_respondent","contact_of_respondent","entry_date")
# 	search_fields = ("region","district", )
# 	# exclude = ('id',)

# admin.site.register(postSurvey, postSurveyAdmin)




# class Questionaire4Admin(ImportExportModelAdmin):
# 	# resource_class = QuestionaireResource
# 	list_display =("region","district","dio_name","dio_contact","sex","age","engaged_in_any_economy","economic_activity_engaged_in","education_level","registered_your_sim_card",'delay_in_issuance_Ghana_card_affected_Sim_registration' )
# 	# exclude = ('id',)
# 	search_fields = ['region','district']

# admin.site.register(Questionaire4, Questionaire4Admin)







# # class adminClient(admin.ModelAdmin):
# #     list_display = ['name','initials','logo']
# #     search_fields = ['name','initials','logo']
# # admin.site.register(Client, adminClient)


# # class adminuserTbl(admin.ModelAdmin):
# #     list_display = ['user','client_fk']
# #     search_fields = ['user','client_fk']
# # admin.site.register(userTbl, adminuserTbl)