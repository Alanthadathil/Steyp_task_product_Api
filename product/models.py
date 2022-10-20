from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    featured_image = models.FileField(upload_to="products/media/images")
    price = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "products_product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.product_name


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    image = models.FileField(upload_to="category/images")

    class Meta:
        db_table = "products_category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name


class Gallery(models.Model):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images")

    class Meta:
        db_table = "products_gallery"
        verbose_name_plural = "gallery"

    def __str__(self):
        return str(self.id)
