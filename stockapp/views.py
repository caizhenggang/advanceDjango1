from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, RedirectView

class ContextError(Exception):
    pass

class LoginError(Exception):
    pass


class StockView(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, **kwargs):
        stock_id = kwargs.get('stock_id')
        page = kwargs.get('page', 5)
        return render(request, 'stock/list.html', locals())

    def post(self, request):
        return HttpResponse('POST请求')

    def put(self, request):
        return HttpResponse('PUT请求')

    def delete(self, request):
        return HttpResponse('Delete请求')


class GoodsView(TemplateView):
    # 针对get请求
    template_name = 'goods/list.html'

    extra_context = {'msg': '我是扩展的消息'}

    def get_context_data(self, **kwargs):
        # raise ContextError('抛出异常')
        # 渲染模板之前。提供上下文数据
        context = super().get_context_data(**kwargs)
        wd = context.get('wd', '')
        datas = ['iphone 6', 'iphone 8', 'iphonX'] if wd == 'iphone'\
            else ['Vivo', '华为']
        context['datas'] = datas
        context['msg'] = '查询成功 %s ' %(datetime.now())
        return context


class QueryView(RedirectView):
    pattern_name = 'stockapp:goods'
    query_string = True # 确定是否拼接查询参数

    def get_redirect_url(self, *args, **kwargs):
        # raise LoginError('查询异常')
        return super(QueryView, self).get_redirect_url(*args, **kwargs)
