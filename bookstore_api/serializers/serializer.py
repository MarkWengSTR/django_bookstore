from rest_framework import serializers
from bookstore_api.models import User, PurchaseHistory

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = ('store_name', 'book_name', 'transaction_amount')


class UpdateSerializer(serializers.ModelSerializer):
    purchasehistory = PurchaseSerializer(many=True, required=False)
#purchasehistory = PurchaseSerializer(many=True)

    class Meta:
        model = User
        fields = ( 'name','purchasehistory')
    

    def create(self, validated_data):
        purchasehistory_data = validated_data.pop('purchasehistory')
        user = User.objects.create(**validated_data)

        for purchase in purchasehistory_data:
            PurchaseHistory.objects.create(user=user, **purchase)
        return user

    def update(self, instance, validated_data):
        purchasehistory_data = validated_data.pop('purchasehistory')
        purchases = (instance.purchasehistory).all()
        purchases = list(purchases)

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        for purchase_data in purchasehistory_data:
            purchase = purchases.pop(0)
            purchase.store_name = purchase_data.get('store_name', purchase.store_name)
            purchase.book_name = purchase_data.get('book_name', purchase.book_name)
            purchase.transaction_amount = purchase_data.get('transaction_amount', purchase.transaction_amount)
            purchase.save()

        return  instance 
