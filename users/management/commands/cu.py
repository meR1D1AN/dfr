from django.core.management import BaseCommand
from pathlib import Path
from dotenv import load_dotenv
import os

from users.models import User

BASE_DIR = Path(__file__).resolve().parent.parent

dot_env = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=dot_env)


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="user@user.com",
            is_active=True,
            is_superuser=False,
            is_staff=False,
            phone="+79998885522"
        )
        user.set_password(os.getenv("EMAIL_PASS"))
        user.save()
