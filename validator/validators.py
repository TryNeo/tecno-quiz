import re

from django.core.exceptions import ValidationError

class Validators(object):
    def __init__(self, value):
        self.value = value
        self.REGEX_STRING = '^[a-zA-ZáéíóñÁÉÍÓÚÑ \-]+$'
        self.REGEX_INTEGER = '^[0-9]+$'
        self.REGEX_EMAIL = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
        self.REGEX_NAME = "^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)"
        

    def validateStringLength(self,message : str ,minLength : int):
        if len(self.value) >= minLength:
            return False
        return ValidationError(
                (message),
                params={'value': self.value},
            )
    
    def validateString(self,message  : str):
        if re.search(self.REGEX_STRING,self.value):
            return False
        return ValidationError(
                (message),
                params={'value': self.value},
            )    

    def validateEmptyField(self,message  : str):
        if len(str(self.value)) >= 2:
            return False
        return ValidationError(
                (message),
                params={'value': self.value},
            )


    def validateNumber(self,message  : str):
        if re.search(self.REGEX_INTEGER,self.value):
            return False
        return ValidationError(
                (message),
                params={'value': self.value},
            ) 
    
    def validateExists(self,message  : str,instance,filter):
        filter = filter
        if not instance.pk:
            return ValidationError(
                (message),
                params={'value': self.value},
                )
        if instance.pk != filter.pk:
            return ValidationError(
                ('No puedes actualizar el registro, ya existe '+self.value),
                params={'value': self.value},
                )
        return False


    def validateEmail(self,message  : str):
        if re.search(self.REGEX_EMAIL,self.value):
            return False
        return ValidationError(
                (message),
                params={'value': self.value},
            )
    
    def validateName(self,message  : str):
        if re.search(self.REGEX_EMAIL,self.value):
            return False
        return ValidationError(
                (message),
                params={'value': self.value},
            )