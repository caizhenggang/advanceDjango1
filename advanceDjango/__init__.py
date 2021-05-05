from __future__ import absolute_import, unicode_literals

import pymysql
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver


pymysql.install_as_MySQLdb()


def model_delete_pre(sender, **kwargs):
    from user.models import Order
    # sender 表示 哪一个Model的对象将要被删除，信号发送者
    # kwargs 表示 信息的基本信息，信号发送时，传递的一些信息
    # print(sender)  # model.Model的子类
    # print(kwargs)  # key: signal, instance, using

    info = 'Prepare Delete %s 类的 id=%s, title=%s'
    # print(issubclass(sender, Order)) # True
    # print(isinstance(sender, Order)) # False
    # print(sender == Order) # True
    # print(sender is Order) # True
    if sender == Order:
        print(info %('订单模型',
                     kwargs.get('instance').id,
                     kwargs.get('instance').title))

# 接收信号
@receiver(post_delete)
def delete_model_post(sender, **kwargs):
    print(sender, '删除成功', kwargs)

pre_delete.connect(model_delete_pre)


# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app
# 向项目模块中增加celery_app对象
__all__ = ('celery_app',)


