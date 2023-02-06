from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField("Имя" , max_length=100)
    email = models.EmailField('Почта',null=True)
    number = models.IntegerField('Номер телефона')

    class Meta:
        verbose_name="Заявка"
        verbose_name_plural ="Заявки"



    def __str__(self):
        return self.name