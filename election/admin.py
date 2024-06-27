from django.contrib import admin
from .models import voters, candidates

@admin.register(voters)
class VotersAdmin(admin.ModelAdmin):
    list_display = ('Firstname', 'Lastname', 'Other_Name', 'Form', 'Index_Number', 'Token','is_token_used')
    search_fields = ('Index_Number', 'Firstname', 'Lastname')
    list_filter = ('Form',)

@admin.register(candidates)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('Firstname', 'Lastname', 'Other_Name', 'Votes')
    search_fields = ('Firstname', 'Lastname')
