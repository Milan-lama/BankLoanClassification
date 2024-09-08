from django.db import models


class Customer(models.Model):
    # Numeric fields
    age = models.IntegerField()
    experience = models.IntegerField()
    income = models.FloatField()
    family = models.IntegerField()
    cc_avg = models.FloatField()  # Assuming 'CCAvg' refers to credit card average spending
    mortgage = models.FloatField()
    
    # Categorical fields
    zip_code = models.CharField(max_length=10)  # Adjust length as needed
    home_ownership = models.CharField(max_length=20)  # Adjust length as needed
    education = models.CharField(max_length=20)  # Adjust length as needed
    
    # Boolean fields
    securities_account = models.BooleanField(default=False)
    cd_account = models.BooleanField(default=False)
    online = models.BooleanField(default=False)
    credit_card = models.BooleanField(default=False)
    
    # Gender
    gender = models.CharField(max_length=10)  # Adjust length as needed

    def __str__(self):
        return f'Customer {self.pk} - {self.gender}'
