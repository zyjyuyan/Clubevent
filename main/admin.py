from django.contrib import admin

from main.models import EventDetail
from main.models import EventSituation
from main.models import Ticket
from main.models import Review
from main.models import Menu
from main.models import Group
from main.models import User
from main.models import Role
from main.models import Permission

admin.site.register(EventDetail)
admin.site.register(EventSituation)
admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(Menu)
admin.site.register(Group)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)


# Register your models here.
