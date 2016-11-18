from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.utils import timezone

class User(AbstractBaseUser, PermissionsMixin):
    MALE = 1
    FEMALE = 2
    TRANS = 3
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (TRANS, 'Transgender'),
    )

    PROVIDER = 1
    DRIVER = 2
    BROKER = 3
    USER_ROLES = (
        (PROVIDER, 'Provider'),
        (DRIVER, 'Driver'),
        (BROKER, 'Broker'),
    )

    username = models.CharField(
        _('username'),
        max_length=200,
        blank=True,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    gender = models.PositiveSmallIntegerField(_('Gender'), choices=GENDER_CHOICES, blank=True, null=True)
    role = models.PositiveSmallIntegerField(_('Role'), choices=USER_ROLES, blank=True, null=True)
    birth_date = models.DateField(_('Birth date'), blank=True, null=True)
    address1 = models.CharField(_('Address1'), blank=True, max_length=100)
    address2 = models.CharField(_('Address2'), blank=True, max_length=100)
    city = models.CharField(_('City'), blank=True, max_length=100)
    state = models.CharField(_('State'), blank=True, max_length=100, help_text='or Province')
    zip = models.CharField(_('Pin Code'), blank=True, max_length=10)
    country = models.CharField(_('Country'), blank=True, max_length=100)
    phone = models.CharField(_('Phone'), max_length=20, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name
