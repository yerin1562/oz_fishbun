from django.db import models

from common.models import BaseModel
from stores.models import Store
from users.models import User


class Product(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"PRODUCT {self.name}: {self.price}₩"

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["name"]
        indexes = [models.Index(fields=["name"], name="product_name_idx")]


class SalesRecord(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    is_refund = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "REFUNDED" if self.is_refund else "PURCHASED"
        return f"RECORD {self.id}: {status} at {self.store.name} on {self.created_at}"

    class Meta:
        db_table = "sales_records"
        verbose_name = "Sales Record"
        verbose_name_plural = "Sales Records"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["user"], name="sales_user_idx"),
            models.Index(fields=["store"], name="sales_store_idx"),
            models.Index(fields=["is_refund"], name="sales_refund_idx"),
        ]


class SalesItem(BaseModel):
    sales_record = models.ForeignKey(SalesRecord, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"RECORD {self.sales_record.id}: {self.sales_record.user.first_name} buy {self.quantity} {self.product.name}s"

    class Meta:
        db_table = "sales_items"
        verbose_name = "Sales Item"
        verbose_name_plural = "Sales Items"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["sales_record"], name="sales_item_record_idx"),
            models.Index(fields=["product"], name="sales_item_product_idx"),
        ]
