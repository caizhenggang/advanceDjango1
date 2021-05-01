from django.db import models

# Create your models here.
<<<<<<< HEAD


class Order(models.Model):

    __pay_status_tuple__ = ((0, '待支付'),
                            (1, '已支付'))

    title = models.CharField(max_length=100,
                             verbose_name='标题')
    price = models.DecimalField(verbose_name='单价',
                                max_digits=10,
                                decimal_places=2)
    pay_status = models.IntegerField(choices=__pay_status_tuple__,
                                     verbose_name='支付状态')
    @property
    def pay_status_title(self):
        return self.__pay_status_tuple__[self.pay_status][1]

    class Meta:
        db_table = 't_order'
=======
>>>>>>> b37281cb98517eceaa6982e7bafafee32895456a
