from django.db import models

# Create your models here.
class User(models.Model):
    #设置主键，如果不设置主键，Django会给你设置一个
    #AutoField会自动增加，primary_key为ture表示为主键
    user_id = models.AutoField(max_length=9,primary_key=True)
    #设置用户名
    #unique为True表示唯一，blank为False表示不为空
    user_name = models.CharField(max_length=12,unique=True,blank=False)
    #设置密码
    user_password = models.CharField(max_length=20,blank=False)
    def __unicode__(self):
        return self.user_id
