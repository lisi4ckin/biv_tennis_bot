from django.core.management.base import BaseCommand
from bot.bot import bot


class Command(BaseCommand):
    help = "Telegram bot starting"

    def handle(self, *args, **options):
        bot.infinity_polling()
