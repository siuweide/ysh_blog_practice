from django.urls import path
from blog import views

urlpatterns = [
    # 博客详情
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    # 博客列表
    path('', views.blog_list, name='blog_list'),
    # 博客分类
    path('type/<int:blog_type_id>/', views.blogs_with_type, name='blogs_with_type'),
    # 博客分类（年、月）
    path('date/<int:year>/<int:month>', views.blogs_with_date, name='blogs_with_date')
]