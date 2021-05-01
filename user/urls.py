from django.urls import path, re_path
from user import views

app_name = 'user'

urlpatterns = [
    path('regist/', views.regist, name='regist1'),
    path('regist/<user_id>/', views.regist, name='regist2'),
    path('cookie/', views.add_cookie),
    path('del_cookie/', views.del_cookie),
    path('login/', views.login),
    path('code/', views.new_code),
    path('logout/', views.logout),
    path('list/', views.list),
]