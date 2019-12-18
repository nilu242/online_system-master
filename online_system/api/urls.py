from django.urls import path

from online_system.api.views import api_list, api_detail_product_view, api_update_product_view, api_delete_product_view


app_name = "product_api"

urlpatterns = [
    path('', api_list, name="create"),
    path('<int:id>', api_detail_product_view, name="detail"),
    path('<int:id>/update/', api_update_product_view, name="update"),
    path('<int:id>/delete/', api_delete_product_view, name="delete")
]