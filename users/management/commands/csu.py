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
            email="admin@admin.com",
            is_active=True,
            is_superuser=True,
            is_staff=True,
            phone="+79994561236"
        )
        user.set_password(os.getenv("EMAIL_PASS"))
        user.save()
