# # Register your models with Import/Export functionality
# class SDAPunjabAdmin(ImportExportModelAdmin):
#     resource_class = SDAPunjabResource
#     list_display = [field.name for field in SDAPunjab._meta.get_fields()]
#     search_fields = ['name', 'designation', 'email']

# class SDAHaryanaAdmin(ImportExportModelAdmin):
#     resource_class = SDAHaryanaResource
#     list_display = ['officer_name', 'designation', 'email', 'epbx_no']
#     search_fields = ['officer_name', 'email']

# class GovtBuildingAdmin(ImportExportModelAdmin):
#     resource_class = GovtBuildingResource
#     list_display = ['department', 'contact', 'website']
#     search_fields = ['department', 'contact']

# class DivisionDetailAdmin(ImportExportModelAdmin):
#     resource_class = DivisionDetailResource
#     list_display = ['division_name', 'drm_name', 'zone_name', 'zone_code', 'no_of_divisions']
#     search_fields = ['division_name', 'drm_name', 'zone_name']

# class RailwayDetailAdmin(ImportExportModelAdmin):
#     resource_class = RailwayDetailResource
#     list_display = ['zone', 'division_name', 'name']
#     search_fields = ['zone', 'division_name', 'name']

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from core.models import SDAPunjab, SDAHaryana, GovtBuilding, DivisionDetail, RailwayDetail, UploadedFile

class SDAPunjabResource(resources.ModelResource):
    class Meta:
        model = SDAPunjab
        fields = ['id', 'name', 'designation', 'email', 'responsibilities']

class SDAHaryanaResource(resources.ModelResource):
    class Meta:
        model = SDAHaryana
        fields = ['id', 'state', 'officer_name', 'designation', 'headquarter', 'email', 'epbx_no']

class GovtBuildingResource(resources.ModelResource):
    class Meta:
        model = GovtBuilding
        fields = ['id', 'department', 'address', 'email', 'contact', 'website']

class DivisionDetailResource(resources.ModelResource):
    class Meta:
        model = DivisionDetail
        fields = ['id', 'division_name', 'drm_name', 'zone_name', 'zone_code', 'no_of_divisions', 'no_of_stations', 'headquarters', 'address']

class RailwayDetailResource(resources.ModelResource):
    class Meta:
        model = RailwayDetail
        fields = ['id', 'zone', 'division_name', 'name', 'city']

class UploadedFileResource(resources.ModelResource):
    class Meta:
        model = UploadedFile
        fields = ['file', 'uploaded_at']

# Registering models correctly with ImportExportModelAdmin
@admin.register(SDAPunjab)
class SDAPunjabAdmin(ImportExportModelAdmin):
    resource_class = SDAPunjabResource

@admin.register(SDAHaryana)
class SDAHaryanaAdmin(ImportExportModelAdmin):
    resource_class = SDAHaryanaResource

@admin.register(GovtBuilding)
class GovtBuildingAdmin(ImportExportModelAdmin):
    resource_class = GovtBuildingResource

@admin.register(DivisionDetail)
class DivisionDetailAdmin(ImportExportModelAdmin):
    resource_class = DivisionDetailResource

@admin.register(RailwayDetail)
class RailwayDetailAdmin(ImportExportModelAdmin):
    resource_class = RailwayDetailResource

@admin.register(UploadedFile)
class UploadedFileAdmin(ImportExportModelAdmin):
    resource_class = UploadedFileResource
