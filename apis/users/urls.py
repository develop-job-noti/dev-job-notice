# System
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from dj_rest_auth.views import (
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
    UserDetailsView,
)
from dj_rest_auth.registration.views import (
    RegisterView,
    VerifyEmailView,
    ResendEmailVerificationView,
)


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    # https://github.com/iMerica/dj-rest-auth/issues/152
    path(
        "password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("password/change/", PasswordChangeView.as_view(), name="rest_password_change"),
    path("signup/", RegisterView.as_view(), name="sign_up"),
    path("detail/", UserDetailsView.as_view(), name="rest_user_details"),
    path("verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
    path(
        "resend-email/", ResendEmailVerificationView.as_view(), name="rest_resend_email"
    ),
]
