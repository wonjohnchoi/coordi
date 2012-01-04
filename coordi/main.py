'''
Created on Jan 2, 2012

@author: wonjohnchoi
'''
from coordi.base.models import Promocode

for promocode in Promocode.objects.all():
    print promocode.promocode_id