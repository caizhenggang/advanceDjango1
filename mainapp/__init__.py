from django.template.defaultfilters import register
import os

# 自定义过滤器
@register.filter('ellipse')
def ellipse(value):
    return os.path.split(value)[-1]

