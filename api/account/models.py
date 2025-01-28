from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

from core.models import AbstractBaseModel


class User(PermissionsMixin, AbstractBaseUser, AbstractBaseModel):
    """
    ### Common fields ###
    # For cognito-users username will contain `sub` claim from jwt token
    # (unique identifier (UUID) for the authenticated user).
    # For django-users it will contain username which will be used to log in into django-admin site
    """
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(_('Username'), max_length=80, unique=True, validators=[username_validator])
    first_name = models.CharField(_('First name'), max_length=80, blank=True)
    last_name = models.CharField(_('Last name'), max_length=80, blank=True)
    mobile = models.CharField(_('Mobile'), max_length=15, blank=True)
    description = models.CharField(_('Description'), max_length=120, blank=True)
    timezone = models.CharField(_("Timezone of User"), blank=True, max_length=80)
    password = models.CharField(max_length=128, verbose_name='password', null=True)
    email = models.EmailField(_('Email address'), blank=True, unique=True)  # allow non-unique emails
    profile_picture = models.TextField(_('Profile picture'), blank=True)
    date_of_birth = models.DateTimeField(_('Date of birth'), null=True)
    postalcode = models.CharField(_('Postalcode'), max_length=80, blank=True)
    address = models.CharField(_('Cover photo'), max_length=80, blank=True)
    country = models.CharField(_('Country'), max_length=150, blank=True)
    city = models.CharField(_('City'), max_length=150, blank=True)
    country_code = models.CharField(_('Country'), max_length=6, blank=True)
    city_code = models.CharField(_('City'), max_length=150, blank=True)
    is_internal_customer = models.BooleanField(
        _('Internal customer'),
        default=False,
        help_text=_('Customer type.')
    )
    is_staff = models.BooleanField(
        _('Staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.')
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']  # used only on createsuperuser

    @property
    def is_django_user(self):
        return self.has_usable_password()