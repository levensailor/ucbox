from django.urls import path
from . import views


urlpatterns = [
    path("numbers", views.NumberListView.as_view(), name="number_list_view"),
    path("numbers/<int:pk>/", views.NumberView.as_view(), name="number_view"),
    path("numbers/add_number/", views.NumberEditView.as_view(), name="add_number"),
    path('numbers/import_numbers/', views.NumberBulkImportView.as_view(), name='import_numbers'),
    path("numbers/<int:pk>/edit/", views.NumberEditView.as_view(), name="number_edit"),
    path("numbers/number_bulk_edit", views.NumberBulkEditView.as_view(), name="number_bulk_edit"),
    path("numbers/<int:pk>/delete/", views.NumberDeleteView.as_view(), name="number_delete"),
    path("numbers/number_bulk_delete", views.NumberBulkDeleteView.as_view(), name="number_bulk_delete"),
    path("trunks", views.TrunkListView.as_view(), name="trunk_list_view"),
    path("trunks/<int:pk>/", views.TrunkView.as_view(), name="trunk_view"),
    path("trunks/add_trunk/", views.TrunkEditView.as_view(), name="add_trunk"),
    path('trunks/import_trunks/', views.TrunkBulkImportView.as_view(), name='import_trunks'),
    path("trunks/<int:pk>/edit/", views.TrunkEditView.as_view(), name="trunk_edit"),
    path("trunks/trunk_bulk_edit", views.TrunkBulkEditView.as_view(), name="trunk_bulk_edit"),
    path("trunks/<int:pk>/delete/", views.TrunkDeleteView.as_view(), name="trunk_delete"),
    path("trunks/trunk_bulk_delete", views.TrunkBulkDeleteView.as_view(), name="trunk_bulk_delete"),
]
