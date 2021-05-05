from signals import codeSignal
from django import dispatch

# 接收信号
@dispatch.receiver(codeSignal)
def cache_code(sender, **kwargs):
    print('dispatch.receiver<codeSignal>')
    print(sender, kwargs)


