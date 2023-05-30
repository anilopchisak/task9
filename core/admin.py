from django.contrib import admin
from .models import Worker, Position, Department, TradeUnion

admin.site.register(Worker)
admin.site.register(Position)
admin.site.register(Department)
admin.site.register(TradeUnion)

# Register your models here.
