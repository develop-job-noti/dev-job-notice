from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str, nickname: str, **extra_fields):
        """
        이 함수는 이메일, 비밀번호, 닉네임을 받아서 유저를 생성합니다.

        Args:
            email (str): 아이디입니다.
            password (str): 비밀번호입니다.
            nickname (str): 닉네임입니다.
            **extra_fields: 추가적인 필드입니다.
        Returns:
            User: 유저 객체입니다.
        """

        if not email:
            raise ValueError("이메일 주소를 필수로 가져야 합니다.")

        email = self.normalize_email(email=email)

        user = self.model(
            email=email,
            nickname=nickname,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_admin(self, email: str, password: str, nickname: str, **extra_fields):
        """
        이 함수는 아이디, 비밀번호, 닉네임을 받아서 관리자를 생성합니다.

        Args:
            email (str): 아이디입니다.
            password (str): 비밀번호입니다.
            nickname (str): 닉네임입니다.
            **extra_fields: 추가적인 필드입니다.
        Returns:
            User: 유저 객체입니다.
        """

        if not email:
            raise ValueError("이메일 주소를 필수로 가져야 합니다.")

        email = self.normalize_email(email=email)
        user = self.model(
            email=email,
            nickname=nickname,
            is_admin=True,
            **extra_fields,
        )
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(
        self, email: str, password: str, nickname: str, **extra_fields
    ):
        """
        이 함수는 아이디, 비밀번호, 닉네임을 받아서 슈퍼 유저를 생성합니다.

        Args:
            email (str): 아이디입니다.
            password (str): 비밀번호입니다.
            nickname (str): 닉네임입니다.
            **extra_fields: 추가적인 필드입니다.
        Returns:
            User: 유저 객체입니다.
        """
        user = self.model(
            email=email,
            nickname=nickname,
            is_admin=True,
            is_superuser=True,
            **extra_fields,
        )
        user.set_password(password)

        user.save(using=self._db)
        return user
