from django.db import models

from common.models import BaseModel
from stores.models import Employee, Store


class RawMaterial(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"ROW MATERIAL {self.name}: {self.price}₩"

    class Meta:
        db_table = "raw_materials"
        verbose_name = "Raw Material"
        verbose_name_plural = "Raw Materials"
        ordering = ["name"]
        indexes = [models.Index(fields=["name"], name="raw_material_name_idx")]


class Supplier(BaseModel):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"SUPPLIER: {self.name}"

    class Meta:
        db_table = "suppliers"
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"
        ordering = ["name"]
        indexes = [models.Index(fields=["name"], name="supplier_name_idx")]


class OrderRecord(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=11,
        choices=[
            ("UNCONFIRMED", "Unconfirmed"),
            ("CONFIRMED", "Confirmed"),
            ("PREPARING", "Preparing"),
            ("SHIPPING", "Shipping"),
            ("RECEIVED", "Received"),
            ("REJECTED", "Rejected"),
        ],
        default="UNCONFIRMED",
    )

    def __str__(self):
        return f"[{self.status}] RECORD {self.id}: {self.employee.user.first_name} orders {self.quantity} {self.raw_material.name}s from {self.supplier.name}"

    class Meta:
        db_table = "order_records"
        verbose_name = "Order Record"
        verbose_name_plural = "Order Records"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["employee"], name="order_employee_idx"),
            models.Index(fields=["supplier"], name="order_supplier_idx"),
            models.Index(fields=["status"], name="order_status_idx"),
        ]


class Stock(BaseModel):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    pre_quantity = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    change_type = models.CharField(
        max_length=10,
        choices=[
            ("IN", "In"),
            ("OUT", "Out"),
            ("RETURNED", "Returned"),
            ("DISCARDED", "Discarded"),
        ],
    )
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        quantity = (
            self.pre_quantity + self.quantity
            if self.change_type in ["IN", "RETURNED"]
            else self.pre_quantity - self.quantity
        )
        return f"[{self.change_type}] {quantity} {self.raw_material.name}s at {self.store.name}"

    class Meta:
        db_table = "stocks"
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"
        ordering = ["store", "raw_material", "change_type"]
        indexes = [
            models.Index(fields=["store"], name="stock_store_idx"),
            models.Index(fields=["raw_material"], name="stock_raw_material_idx"),
        ]
