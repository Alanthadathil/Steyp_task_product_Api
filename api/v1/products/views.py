from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response


from api.v1.products.serializers import ProductSerializer, ProductDetailSerializer
from product.models import Product


@api_view(["GET"])
def products(request):
    instances = Product.objects.filter(is_deleted=False)

    context = {
        "request": request
    }
    serializer = ProductSerializer(instances, many=True, context=context)
    response_data = {
        "status_code": 6000,
        "data": serializer.data
    }

    return Response(response_data)


@api_view(["GET"])
def product(request, pk):
    if Product.objects.filter(pk=pk).exists():
        instance = Product.objects.get(pk=pk)

        context = {
            "request": request
        }
        serializer = ProductDetailSerializer(instance, context=context)
        response_data = {
            "status_code": 6000,
            "data": serializer.data
        }

        return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "Product not found"
        }
        return Response(response_data)


@api_view(["POST"])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        response_data = {
            "status_code": 6000,
            "message": "Success",
        }

        return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "Validation Failed",
            "data": serializer.errors
        }
        return Response(response_data)


@api_view(["POST"])
def update_product(request, pk):
    if Product.objects.filter(pk=pk).exists():
        instance = Product.objects.get(pk=pk)

    serializer = ProductSerializer(
        instance=instance, partial=True,
        data=request.data)
    if serializer.is_valid():
        serializer.save()

        response_data = {
            "status_code": 6000,
            "message": "Success",
        }

        return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "Product Editing Failed",
            "data": serializer.errors
        }
        return Response(response_data)
