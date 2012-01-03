'''
Created on Jan 2, 2012

@author: wonjohnchoi
'''
from coordi.base.models import Promocode
from django.contrib.auth.models import Permission
promocode = Promocode()
promocode.permissions = Permission.objects.filter(codename = '')
print(promocode.promocode_id)