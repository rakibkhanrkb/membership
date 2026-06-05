from django.contrib import admin
from .models import VisitorIP, reg,bitboxc, VisitorCount
from .models import SupportMessage

admin.site.register(reg)
admin.site.register(bitboxc)
admin.site.register(SupportMessage)
admin.site.register(VisitorCount)
admin.site.register(VisitorIP) 