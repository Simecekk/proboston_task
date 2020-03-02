from django.db import models
from ares_util.validators import czech_company_id_ares_api_validator

class FormModel(models.Model):
    jméno = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    ičo = models.PositiveIntegerField(validators=[czech_company_id_ares_api_validator],)


    def __str__(self):
        return self.ičo
    

