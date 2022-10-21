from django.urls import path
from . import views


urlpatterns =[
    # path('',views.index,name="home"),
    path('main/',views.main_home,name="main"),
    path('stocks/<team_name>/',views.stocks_list,name="stocks"),
    path('portfolio/<team_name>/',views.portfolio,name="stocks"),
    path('ranklist/<team_name>/',views.ranklist,name="stocks"),
    path('stockname/<stock>/',views.stockers,name="stockname"),
    path('createform/',views.Create_team,name="creater"),
    path('showname/<team_hel>',views.shownum,name="show"),
    path('join/',views.join,name="join"),
    path('stock_detail/<room_name>/<stock_name>/', views.stock_details, name='stock_details'),
    path('push_detail<room_name>/<stock_name>/<current_stock_price>/', views.push_details, name='push_details'),
    path('pull_detail<room_name>/<stock_name>/<current_stock_price>/<no_of_shares>/', views.pull_details, name='pull_details'),
]