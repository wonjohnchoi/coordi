'''
Created on Dec 22, 2011

@author: wonjohnchoi
'''
'''
from coordi.base.models import CustomUser
def custom_user(request):
    if request.user.is_authenticated():
        try:
            return {'custom_user' : CustomUser.objects.get(user = request.user)}
        except CustomUser.DoesNotExist:
            raise Exception('Each user must have a corresponding CustomUser object')
            #return {'custom_user' : None}
    else:
        return {'custom_user': None}
'''
'''
def permissions(request):
    if request.user.is_authenticated():
        try:
            custom_user = CustomUser.objects.get(user = request.user)
        except CustomUser.DoesNotExist:
            raise Exception('Each user must have a corresponding CustomUser object')
        permissions = []
        for permission in custom_user.permissions:
            permissions.append(permission)
        return {'permissions': permissions}
    else:
        return {'permissions': []}
'''