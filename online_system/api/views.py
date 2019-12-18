from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from product.models import Product
from online_system.api.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def api_list(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def api_detail_product_view(request, id):

    try:
        products = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(products)
    return Response(serializer.data)

@api_view(['PUT',])
def api_update_product_view(request, id):

    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data['success'] = "update successfull"
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_delete_product_view(request, id):

    try:
        products = Product.objects.get(id=id)
        print(products)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    operations = products.delete()
    data = {}
    if operations:
        data['success'] = 'deleted successfull'
    else:
        data['falilure'] = 'deleted unsuccessfull'
    return Response(data=data)