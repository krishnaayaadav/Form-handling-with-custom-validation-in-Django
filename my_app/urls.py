from django.urls import path
from .views import * # all views imported

urlpatterns = [
    path('defualt-validation/', defualt_form_validation, name='default1'),
    path('field-level/validation/', field_level_validations, name='field1'),
    path('complete/form-validation/', complete_form_validation),
    


]
