class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('email'),
        max_length=300,
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )

    # Identity Info
    fname = models.CharField(
        _('First Name'),
        max_length=30,
        help_text="Enter your first name."
    )

    lname = models.CharField(
        _('Last Name'),
        max_length=150,
        help_text="Enter your last name."
    )

    # Age
    birthday = models.DateField(
        _('birthday'),
        max_length=150,
        help_text="Enter your birthday."
    )

    # Location and Chapters
    country = CountryField(
        _('Country'),
        help_text="Enter your country."


    # Config Constants
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname', 'birthday', 'country']

    # Automatically Set Fields

    def get_age(self):
        today = date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    # Display
    def __str__(self):              # __unicode__ on Python 2
        return self.get_full_name() + ' - ' + self.email

    def get_full_name(self):
        return self.fname + " " + self.lname