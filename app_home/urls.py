from django.urls import path
from app_home import views

app_name = 'app_home'

urlpatterns = [
    path('' , views.home , name="index"),
    path('api/compile/',views.CompilerResponseApi.as_view(),name="compile"),
    path('api/lang_comp_ver/<str:lang>/',views.ApiLanguageCompilerVersions.as_view(),name="version_lang"),
]