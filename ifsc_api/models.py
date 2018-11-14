from django.db import models

class IFSC(models.Model):
    ifsc_code = models.CharField(max_length=15, null=False)
    bank_name = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=80, null=False)
    branch_name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=300,null=False)

    def __str__(self):
        return self.bank_name