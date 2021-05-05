import time
from celery import shared_task


@shared_task
def qbuy(goods_id, user_id):
    print('%s Qbuying %s' % (goods_id, user_id))
    # time.sleep(5)
    return '%s OK %s' % (goods_id, user_id)
