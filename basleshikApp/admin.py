from django.contrib import admin
from . import models

admin.site.register(models.Role)

@admin.register(models.Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('answer', 'assess', 'group_id', 'question_id', 'formatted_created', 'formatted_updated')
    def formatted_created(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    formatted_created.short_description = 'Döredilen wagty'

    def formatted_updated(self, obj):
        return obj.updated_at.strftime('%d.%m.%Y %H:%M')
    formatted_updated.short_description = 'Üýtgedilen wagty'


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_num', 'formatted_time', 'compatition_id', 'formatted_created', 'formatted_updated', 'status')

    def formatted_time(self, obj):
        return obj.time.strftime('%H:%M')
    formatted_time.short_description = 'Berilýän wagty'

    def formatted_created(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    formatted_created.short_description = 'Döredilen wagty'

    def formatted_updated(self, obj):
        return obj.updated_at.strftime('%d.%m.%Y %H:%M')
    formatted_updated.short_description = 'Üýtgedilen wagty'


@admin.register(models.Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('year', 'party_num', 'formatted_created', 'formatted_updated', 'status')

    def formatted_created(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    formatted_created.short_description = 'Döredilen wagty'

    def formatted_updated(self, obj):
        return obj.updated_at.strftime('%d.%m.%Y %H:%M')
    formatted_updated.short_description = 'Üýtgedilen wagty'



@admin.register(models.Compatition)
class CompatitionAdmin(admin.ModelAdmin):
    list_display = ('theme', 'formatted_start_time', 'season_id', 'formatted_created', 'formatted_updated', 'status')

    def formatted_start_time(self, obj):
        return obj.start_time.strftime('%d.%m.%Y %H:%M')
    formatted_start_time.short_description = 'Start time'
    
    def formatted_created(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    formatted_created.short_description = 'Döredilen wagty'

    def formatted_updated(self, obj):
        return obj.updated_at.strftime('%d.%m.%Y %H:%M')
    formatted_updated.short_description = 'Üýtgedilen wagty'


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name','point_num', 'formatted_created', 'formatted_updated', 'status')

    def formatted_created(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    formatted_created.short_description = 'Döredilen wagty'

    def formatted_updated(self, obj):
        return obj.updated_at.strftime('%d.%m.%Y %H:%M')
    formatted_updated.short_description = 'Üýtgedilen wagty'


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'last_name', 'group_id', 'role_id', 'status',)
