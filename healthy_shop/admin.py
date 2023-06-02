from django.contrib import admin

from .models import ProductIsInTransaction, CustomUser, Category, Transaction, Product


# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


class ProductAdmin(admin.ModelAdmin):
    exclude = ('code', 'user',)

    def save_model(self, request, obj, form, change):
        obj.user = CustomUser.objects.all().filter(user=request.user).first()
        obj.save()

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == CustomUser.objects.all().filter(user=request.user).first():
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == CustomUser.objects.all().filter(user=request.user).first():
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    exclude = ('code',)


class ProductIsInTransactionInlineAdmin(admin.TabularInline):
    model = ProductIsInTransaction
    extra = 0


class TransactionAdmin(admin.ModelAdmin):
    inlines = [ProductIsInTransactionInlineAdmin]

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ['name', ]

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
