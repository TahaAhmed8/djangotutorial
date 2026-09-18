from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create the live Django superuser"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = input("Enter admin username: ")
        email = input("Enter admin email: ")
        password = input("Enter admin password: ")

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(
                    f"User '{username}' already exists."
                )
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Superuser '{username}' created successfully!"
            )
        )