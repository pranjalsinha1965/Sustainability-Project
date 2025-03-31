from django.contrib import admin
from equipment.models import Equipment

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'purchase_date', 'status')  # Ensure these exist in models.py
    search_fields = ('name', 'category')
    list_filter = ('status', 'purchase_date')  # Ensure these exist in models.py
    ordering = ('-purchase_date',)  # Ensure this exists in models.py

    def category(self, obj):
        return obj.category  # Ensure this function exists if category isn't a field

    def status(self, obj):
        return obj.status  # Ensure this function exists if status isn't a field
