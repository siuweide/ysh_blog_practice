from django.db.models import Count
from blog.models import Blog, BlogType
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404


def get_blog_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, 5)
    page_num = request.GET.get('page', 1)  # 获取url页面的参数（GET请求）
    page_of_blogs = paginator.get_page(page_num)
    currentr_page_num = page_of_blogs.number # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
                list(range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # 获取博客分类对应的博客数量
    # blog_types = BlogType.objects.all()
    # blog_type_count_list = []
    # for blog_type in blog_types:
    #     blog_type.blog_count = Blog.objects.filter(blog_type=blog_type).count()
    #     blog_type_count_list.append(blog_type)


    blog_dates_list = {}
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')
    for blog_date in blog_dates:
         blog_count = Blog.objects.filter(created_time__year=blog_date.year,
                                                created_time__month=blog_date.month).count()
         blog_dates_list[blog_date] = blog_count

    context = {}
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))
    context['blog_dates'] = blog_dates_list
    return context

def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_common_data(request, blogs_all_list)
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if not request.COOKIES.get('blog_%s_read' % blog_id):
        blog.readed_num += 1
        blog.save()

    context = {}
    context['blog'] = blog
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    response = render(request, 'blog/blog_detail.html', context)
    response.set_cookie('blog_%s_read' % blog_id, 'true')
    return response

def blogs_with_type(request, blog_type_id):
    blog_type = get_object_or_404(BlogType, id=blog_type_id)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_common_data(request, blogs_all_list)
    context['blog_type'] = blog_type
    return render(request, 'blog/blogs_with_type.html', context)

def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)
    context = get_blog_common_data(request, blogs_all_list)
    context['blog_with_date'] = '%d年%d月' %(year, month)
    return render(request, 'blog/blogs_with_date.html', context)
