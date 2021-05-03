from stockapp import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


app_name = 'stockapp'


urlpatterns =[
    path('stocks/<stock_id>/', csrf_exempt(views.StockView.as_view()), name='stocks'),
    path('goods/<wd>/', views.GoodsView.as_view(), name='goods'),
    path('query/<wd>/', views.QueryView.as_view(), name='query'),
]