from django.core.management.base import BaseCommand
from nijisanji.models import Liver

import json


class Command(BaseCommand):
    help = 'Import liver info from Nijisanji member json.'

    def add_arguments(self, parser):
        parser.add_argument('file_paths', nargs='+', type=str)

    def handle(self, *args, **options):
        for path in options['file_paths']:
            data = json.load(open(path))
            for liver_data in data['props']['pageProps']['livers']['contents']:
                try:
                    liver = Liver.objects.get(slug=liver_data['slug'])
                    liver.ruby = liver_data['ruby']
                    liver.save()
                except Liver.DoesNotExist:
                    liver = Liver(name=liver_data['name'],
                                  slug=liver_data['slug'])
                    liver.save()
                print("{} / {}".format(liver_data['name'],
                                       liver_data['slug']))

        self.stdout.write(self.style.SUCCESS('success'))
