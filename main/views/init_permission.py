from main.models import User

def init_permission(request, user_obj):
    permission_item_list = user_obj.roles.values('permissions__group_id',
                                                 'permissions__code',
                                                 'permissions__url',
                                                 'permissions__group__menu__id',
                                                 'permissions__group__menu__title',
                                                 'permissions__title',
                                                 'permissions__url',
                                                 'permissions__is_menu',
                                                ).distinct()

    dest_dic = {}
    
