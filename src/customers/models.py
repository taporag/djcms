from django.db import models

class Customer(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    #last_order_id
    #last_order_name
    note = models.TextField(max_length=150, blank=True)
    orders_count = models.IntegerField(default=0)
    phone = models.CharField(max_length=15, blank=True)
    total_spent = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
    class Meta:
        pass
    

class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=100, blank=False)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=False)
    country_code_alpha = models.CharField(max_length=3, blank=False)
    country = models.CharField(max_length=30, blank=False)
    company = models.CharField(max_length=50, blank=True)
    full_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=15, blank=False)
    province = models.CharField(max_length=20, blank=True)
    province_code = models.CharField(max_length=3, blank=True)
    zip_code = models.CharField(max_length=10, blank=False)

    class Meta:
        verbose_name  = 'Customer Address'
        verbose_name_plural  = 'Customer Addresses'

    def __str__(self):
        return self.address1
    
    
    
