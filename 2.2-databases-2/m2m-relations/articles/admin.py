from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Section, Relationship, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main = {}
        counter = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # print(form)
            # каждой отдельной формы, которые вы можете проверить
            main = form.cleaned_data
            print(main)
            print(main.get('main'))
            if main.get('main') is True:
                counter += 1
                main = {'count': counter}
                # вызовом исключения ValidationError можно указать админке о наличие ошибки
                # таким образом объект не будет сохранен,
                # а пользователю выведется соответствующее сообщение об ошибке
                if main.get('count') > 1:
                    raise ValidationError('Может быть только один основной раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main = {}
        counter = 0
        for form in self.forms:
            main = form.cleaned_data
            print(main)
            print(main.get('is_main'))
            if main.get('is_main') is True:
                counter += 1
                main = {'count': counter}
                if main.get('count') > 1:
                    raise ValidationError('Может быть только один основной раздел')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset
    extra = 3

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [RelationshipInline, ScopeInline]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [RelationshipInline,]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ScopeInline]

# @admin.register(Scope)
# class ScopeAdmin(admin.ModelAdmin):
#     list_display = ['is_main']
#     inlines = [ScopeInline]

