from multiprocessing import context
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from product.models import Product, Gallery


class ProductSerializer(ModelSerializer):
    class Meta:
        fields = ("product_name", "id", "featured_image", "product")
        model = Product


class GallerySerializer(ModelSerializer):
    class Meta:
        fields = ("image", "id", )
        model = Gallery


class ProductDetailSerializer(ModelSerializer):

    gallery = serializers.SerializerMethodField()

    class Meta:
        fields = ("product_name", "id", "featured_image",
                  "product", "description", "category", "gallery")
        model = Product

    def get_gallery(self, instance):
        request = self.context.get("request")
        images = Gallery.objects.filter(product=instance)
        serializer = GallerySerializer(
            images, many=True, context={"request": request})
        return serializer.data
