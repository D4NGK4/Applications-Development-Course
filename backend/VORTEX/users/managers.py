from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password

class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try: 
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Invalid Email"))
        
        
    
    def create_user(self, firstname, lastname, email, password, **extra_fields):
        if not firstname:
            raise ValueError(_("First name required"))
        
        if not lastname:
            raise ValueError(_("Last name required"))
        
        if email: 
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User: and email is required"))

                             
        user = self.model(
            firstname = firstname,
            lastname=lastname,
            email=email,
            **extra_fields
        )
        
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        
        user.save()
        
        return user
    
    def create_superuser(self, firstname, lastname, email, password, **extra_fields):
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser=True"))
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True"))
                
        if not password:
            raise ValueError(_("Superusers must have password"))
            
        if email: 
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin User: and email is required"))
                              
        user = self.create_user(firstname, lastname, email, password, **extra_fields)
        
        user.save()
        
        return user