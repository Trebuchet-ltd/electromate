from rest_framework import serializers

from home.models import Department, Product, ProductAttribute, PayIn, ProductVariant


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'code', 'category', 'colour', 'icon']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'short_description', 'product_hsn', 'code', 'description', 'price', 'stock', 'category',
                  'best_seller', 'rating', 'modified_user', 'created_date']


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = ['name', 'value', 'product']


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['product', 'name', 'value']


class ProductOrder(serializers.ModelSerializer):
    class Meta:
        models = ProductVariant
        fields = ['order_time', 'user', 'item_details', 'amount', 'cashback_amount',
                  'business_volume', 'pincode', 'dilivary_address', 'status', 'processed_user',
                  'payment_type', 'modified_date_time']


class PayInSerializer(serializers.ModelSerializer):
    class Meta:
        models = PayIn
        fields = ['id', 'transaction_id', 'purchase_order_id', 'paid_date_time', 'amount', 'type', 'status',
                  'processed_user_id', 'payment_received_user_id', 'cash_back_debited']
