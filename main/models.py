from django.db import models
from django.forms.models import model_to_dict
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class BaseManager(models.Manager):
    def get_or_none(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs)
        except self.model.DoesNotExist:
            return None

    def get_or_404(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs)
        except self.model.DoesNotExist:
            raise Http404(_('The {t} you are looking for does not exist. (Request arguments {a} {k})').format(t=self.model.__name__, a=args or '', k=kwargs or ''))


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = BaseManager()

    class Meta:
        abstract = True

    def toArray(self):
        self.created = self.created.isoformat(' ')
        self.modified = self.modified.isoformat(' ')
        return model_to_dict(self)

# Create your models here.


class EventDetail(BaseModel):
    STATUSES =(
        ('未发布','未发布'),
        ('已结束','已结束'),
        ('未开始','未开始'),
        ('正在报名中','正在报名中'),
        ('活动人数已满','活动人数已满'),
        ('打折中','打折中'),
    )
    name = models.CharField(max_length=200, blank=False)
    location = models.CharField(max_length=200, blank=True)
    time = models.DateTimeField()
    detail = models.TextField()
    poster = models.ImageField(upload_to='img')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_peoples = models.IntegerField()
    register_number = models.IntegerField()
    review_number = models.IntegerField()
    tickets = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=20, blank=True, choices=STATUSES, default='未发布')

class EventSituation(BaseModel):
    STATUSES=(
        ('未参加','未参加'),
        ('已参加','已参加'),
        ('已报名','已报名'),
        ('已通过审核','已通过审核'),
        ('未通过审核','未通过审核'),
        ('已通过审核但未参加','已通过审核但未参加'),
        ('已取消','已取消'),
    )
    userid = models.IntegerField()
    usergroup = models.CharField(max_length=20)
    eventid = models.IntegerField()
    original_tickets = models.DecimalField(max_digits=20, decimal_places=2)
    final_tickets = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=20, blank=True, choices=STATUSES, default='未参加')
    explanation = models.CharField(max_length=100)

class Ticket(BaseModel):
    eventid = models.IntegerField()
    original_tickets = models.DecimalField(max_digits=20, decimal_places=2)
    conditions = models.CharField(max_length=100)
    discount = models.DecimalField(max_digits=20, decimal_places=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Review(BaseModel):
    userid = models.IntegerField()
    usergroup = models.CharField(max_length=20)
    eventid = models.IntegerField()
    eventstatus = models.CharField(max_length=20)
    reviewid = models.IntegerField()
    reviewresult = models.CharField(max_length=20)

class Menu(BaseModel):
    title = models.CharField(max_length=32)

class Group(BaseModel):
    caption = models.CharField(verbose_name='组名称', max_length=32)
    menu = models.ForeignKey(verbose_name='组所属菜单',to='Menu',default=1)

    class Meta:
        verbose_name_plural = 'Group组表'

    def __str__(self):
        return self.caption

class User(BaseModel):
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.CharField(verbose_name='邮箱', max_length=32)

    roles = models.ManyToManyField(verbose_name='角色', to='Role', blank=True)

    class Meta:
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.username

class Role(BaseModel):
    title = models.CharField(max_length=32)
    permissions = models.ManyToManyField(verbose_name='具有的所有权限', to='Permission', blank=True)

    class Meta:
        verbose_name_plural = '角色表'

    def __str__(self):
        return self.title

class Permission(BaseModel):
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则URL', max_length=64)
    is_menu = models.BooleanField(verbose_name='是否是菜单')

    code = models.CharField(verbose_name='url代码', max_length=32, default=0)
    group = models.ForeignKey(verbose_name='所属组', to='Group', null=True, blank=True)

    class Meta:
        verbose_name_plural = '权限表'

    def __str__(self):
        return self.title

# class Group(BaseModel):



