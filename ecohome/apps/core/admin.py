from django.contrib import admin

from ecohome.apps.core.models import Income, Category, Expenses, Budget, Saving
# Register your models here.


admin.site.register(Income)
admin.site.register(Category)
admin.site.register(Expenses)
admin.site.register(Budget)
admin.site.register(Saving)
