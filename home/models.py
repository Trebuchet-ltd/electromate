from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    choices = (
        ('value of the day', 'value of the day'), ('top 100 offer', 'top 100 offer'),
        ('new arrivals', 'new arrivals'), ('tv and audio', 'tv and audio'), ('gadgets', 'gadgets'),
        ('all in one', 'all in one'), ('accessories', 'accessories'), ('gaming', 'gaming'),
        ('laptop and computers', 'laptop and computers'), ('mac', 'mac'),
        ('ultrabook', 'ultrabook')
    )
    name = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=3, primary_key=True)
    category = models.CharField(choices=choices, max_length=25, )
    color = models.CharField(max_length=30, blank=True, null=True)
    icon = models.ImageField(upload_to='images/', null=True, blank=True, help_text="Upload the icon")

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField(max_length=2048, default='')
    product_hsn = models.CharField(max_length=50, null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=2048, )
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    bestSeller = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    modified_user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)


class ProductAttribute(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=50)


class PurchaseOrder(models.Model):
    order_time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase')
    item_details = models.CharField(max_length=5000)
    amount = models.FloatField()
    cashback_amount = models.FloatField()
    business_volume = models.IntegerField()
    pincode = models.FloatField()
    delivery_address = models.CharField(max_length=800)
    status = models.CharField(max_length=20)
    processed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authorised_purchase')
    payment_type = models.CharField(max_length=80)
    modified_date_time = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user = models.OneToOneField(User, related_name="cart", on_delete=models.CASCADE)
    total = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user}'s cart"


class CartItem(models.Model):
    item = models.ForeignKey(Product, related_name="cart_item", on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField()
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='variant')


class Addresses(models.Model):
    name = models.TextField(max_length=100)
    address = models.TextField(max_length=3000)
    pincode = models.CharField(max_length=6)
    state = models.TextField(max_length=25, blank=True, null=True)
    phone = models.CharField(max_length=15)
    user = models.ForeignKey(User, related_name="Addresses", on_delete=models.CASCADE, blank=True,
                             null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    delivery_charge = models.IntegerField(null=True, blank=True, choices=((0, 0), (30, 30), (60, 60)))
    gst = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.address}, {self.state}, {self.pincode} (PIN) "
      
class PayIn(models.Model):

    transaction_id = models.IntegerField()
    purchase_order_id = models.IntegerField()
    paid_date_time = models.IntegerField()
    amount = models.IntegerField()
    type = models.CharField(max_length=25)
    status = models.CharField(max_length=25)
    processed_user_id = models.IntegerField()
    payment_received_user_id = models.IntegerField()
    cash_back_debited = models.BooleanField()

