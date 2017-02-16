from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
          raise ValueError(_('Usuario já registrado.'))
        username = self.normalize_usernanem(username)
        user = self.model(
                username=username,
                email=email,
                is_active=True,
                is_superuser=is_superuser,
                last_login=now,
                date_joined=now,
                date_update=now,
                **extra_fields
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            username,
            email,
            password,
            **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
