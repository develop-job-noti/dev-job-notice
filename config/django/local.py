# Project
from config.django.base import *
from config.settings.swagger.settings import *


# ==================================================================== #
#                           DB config                                  #
# ==================================================================== #
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
