from django.core.management.base import BaseCommand
from schools.models import Schools
from datetime import datetime
import random
import names
import json
import sys
import os

class Command(BaseCommand):
    help = 'Custom command for generate data fo filling up database'

    def _generate_number(self):
        """Generate number"""

        _number_from = 10
        _number_to = 99

        return random.randint(_number_from,_number_to,)

    def _generate_schooles(self):
        f = open("C:/Users/User/Desktop/ggg/ggg/hackhathon_proj/apps/schools/management/commands/sample.json", 'r')
        data = json.loads(f.read())
        print(data)

        # Post fields
        school_name: str = ''
        location: str = ''
        type = ','
        for value in data:
            school_name = value['name']
            location = value['Местоположение']
            type = type.join(value['Тип'])
            post: dict = {
                'school_name': school_name,
                'location': location,
                'type': type,
            }
            Schools.objects.get_or_create(**post)

    def handle(self, *args: tuple, **kwargs: dict) -> None:
        """Handles data filling"""

        start: datetime = datetime.now()

        self._generate_schooles()

        print('Generating Data: {} seconds'.format((datetime.now()-start).total_seconds()))