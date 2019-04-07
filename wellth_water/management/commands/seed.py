from django.core.management.base import BaseCommand
import random

from wellth_water.models import Users
from wellth_water.models import Entries

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    logger.info("Delete User instances")
    Entries.objects.all().delete()
    Users.objects.all().delete()


def create_user(name):
    """Creates a user object combining different elements from the list"""
    logger.info("Creating users")

    user = Users(
        name=f'{name}',
        email=f'{name}@gmail.com'
    )
    user.save()
    for i in range(3):
        create_entry(user)
    logger.info("{} user created.".format(user))
    return user


def create_entry(user):
    """Creates a entry object combining different elements from the list"""
    logger.info("Creating entrys")

    types = [ "coffee", "beer", "soda", "wine","mixed drinks", "tea" ]
    amounts = [ 250, 299, 350, 550, 650 ]

    entry = Entries(
        drinktype=random.choice(types),
        amount=random.choice(amounts),
        user_id=user.id
    )
    entry.save()
    logger.info("{} entry created.".format(entry))
    return entry

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    clear_data()
    names = ['Justin', 'Ben', 'Shannon', 'Sal', 'Bob']
    for name in names:
        create_user(name)
