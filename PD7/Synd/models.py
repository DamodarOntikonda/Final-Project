from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    employer_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = 'User Info'


class SubscriptionType(models.Model):
    subscription_type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subscription_type_name

    class Meta:
        verbose_name_plural = 'SubscriptionType'


class Service(models.Model):
    service_name = models.CharField(max_length=50)
    service_code = models.IntegerField()
    description = models.TextField()
    premium = models.CharField(max_length=50)
    allocation = models.CharField(max_length=50)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name_plural = 'Service'


class Office(models.Model):
    office_name = models.CharField(max_length=50)
    attribution = models.CharField(max_length=50)

    def __str__(self):
        return self.office_name

    class Meta:
        verbose_name_plural = 'Office'


class Organization(models.Model):
    organization_code = models.CharField(max_length=50)
    organization_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date_join = models.DateField()
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.organization_code

    class Meta:
        verbose_name_plural = 'Organization'


class Subscriber(models.Model):
    subscriber_id = models.IntegerField()
    user_name = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    subscription_type_code = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    service_code = models.ForeignKey(Service, on_delete=models.CASCADE)
    request_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    method_of_cancellation = models.CharField(max_length=50)
    beneficiary_id = models.IntegerField()

    def __str__(self):
        return self.subscriber_id

    class Meta:
        verbose_name_plural = 'Subscriber'


class OrganizationMember(models.Model):
    organization_code = models.ForeignKey(Organization, on_delete=models.CASCADE)
    subscriber_id = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    native_country = models.CharField(max_length=30)
    citizenship = models.CharField(max_length=30)
    is_delegate = models.BooleanField(default=False)

    def __str__(self):
        return self.organization_code

    class Meta:
        verbose_name_plural = 'OrganizationMember'


class Officer(models.Model):
    office_code = models.ForeignKey(Office, on_delete=models.CASCADE)
    subscriber_id = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.office_code

    class Meta:
        verbose_name_plural = 'Officer'


class TransferredSubscription(models.Model):
    transfer_id = models.IntegerField()
    transfer_from = models.CharField(max_length=100)
    transfer_to = models.CharField(max_length=100)
    request_date = models.DateField(blank=True, null=True)
    transfer_date = models.DateField(blank=True, null=True)
    subscriber_id = models.ForeignKey(Subscriber, on_delete=models.CASCADE)

    def __str__(self):
        return self.subscriber_id

    class Meta:
        verbose_name_plural = 'TransferredSubscription'

