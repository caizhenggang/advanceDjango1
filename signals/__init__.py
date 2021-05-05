from django import dispatch


# 定义信号
# providing_args 声明发送信息的参数列表
codeSignal = dispatch.Signal(providing_args=['path',
                                             'phone',
                                             'code'])

