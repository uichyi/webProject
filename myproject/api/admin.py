from django.contrib import admin
from .models import TestNSI, TestResult, User

# Регистрируем модель TestResult в админке
@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_id', 'user_id', 'try_number', 'accuracy', 'number_all_answers', 'number_correct_answers', 'complete_time')  # Поля, которые будут отображаться в списке
    search_fields = ('user_id', 'test_id')  # Поля, по которым можно искать
    list_filter = ('test_id', 'user_id')  # Фильтры в админке

@admin.register(TestNSI)
class TestNSI(admin.ModelAdmin):
    list_display = ('test_id', 'test_name') # Поля, которые будут отображаться в списке

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.get_fields() if not field.many_to_many and not field.one_to_many]