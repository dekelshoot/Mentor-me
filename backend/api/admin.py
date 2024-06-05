from django.contrib import admin
from api.models import User, Mentorship, MentorshipSession, LearningResource
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class MyUserAdmin(UserAdmin):
	model = User
	fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_mentor', 'is_mentee', 'age', 'location', 'domain_of_interest', 'level_of_education', 'bio')}),
    )
	
class MentorshipAdmin(admin.ModelAdmin):
	model = Mentorship

class MentorshipSessionAdmin(admin.ModelAdmin):
	model = MentorshipSession

class LearningResourceAdmin(admin.ModelAdmin):
	model = LearningResource
	
admin.site.register(User, MyUserAdmin)
admin.site.register(Mentorship, MentorshipAdmin)
admin.site.register(MentorshipSession, MentorshipSessionAdmin)
admin.site.register(LearningResource, LearningResourceAdmin)