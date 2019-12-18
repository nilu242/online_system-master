from django.urls import path

from online_system.api.views import api_detail_product_view, api_update_product_view


app_name = "product_api"

urlpatterns = [
    path('<int:id>', api_detail_product_view, name="detail"),
    path('<int:id>/update/', api_update_product_view, name="update"),
]
