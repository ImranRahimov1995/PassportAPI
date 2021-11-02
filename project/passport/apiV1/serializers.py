from passport.models import Customer, Passport
from rest_framework import serializers



class CustomerSerializer_INC(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'surname', 'phone', 'email')


class PassportSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer_INC()

    class Meta:
        model = Passport
        fields = ('scan', 'document', 'personal', 'first_name',
                  'last_name', 'patronymic', 'nationality', 'gender',
                  'birth', 'issue_date', 'expire_date', 
                  'issuing_authority', 'customer')

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        customer = Customer.objects.filter(
                                            phone=customer_data \
                                            .get('phone')).first()

        if not customer:
            customer = Customer.objects.create(**customer_data)
        new_passport = Passport.objects.create(customer=customer,
                                               **validated_data)
        return new_passport


class CustomerSerializer(serializers.ModelSerializer):
    passport_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Customer
        fields = ('name', 'surname', 'phone',
                  'email', 'passport_set')


class PassportDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = ('scan', 'document', 'personal', 'first_name',
                  'last_name', 'patronymic', 'nationality', 
                  'gender','birth', 'issue_date', 'expire_date', 
                  'issuing_authority', 'customer')