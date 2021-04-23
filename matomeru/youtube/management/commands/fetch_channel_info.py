from django.core.management.base import BaseCommand
from youtube.models import Channel
from nijisanji.models import Liver

from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse


class Command(BaseCommand):
    help = 'Fetch channel info from Nijisaji official site.'

    def add_arguments(self, parser):
        parser.add_argument('liver_names', nargs='*', type=str)

        parser.add_argument(
            '--all',
            action='store_true',
            help='fetch all liver channel info.'
        )

    def handle(self, *args, **options):
        if options['all']:
            livers = Liver.objects.all()
            for liver in livers:
                self._fetch_and_register(liver)
            return

        for liver_name in options['liver_names']:
            try:
                liver = Liver.objects.get(slug=liver_name)
            except Liver.DoesNotExist:
                self.stderr.write(
                    self.style.ERROR('Liver {} does not exist.'.format('liber_name'))
                )
                continue

            self._fetch_and_register(liver)

    def _fetch_and_register(self, liver):
        r = requests.get(
            'https://www.nijisanji.jp/members/{}'.format(liver.slug))

        soup = BeautifulSoup(r.text, 'html.parser')
        for tag in soup.find_all('a'):
            parse_result = urlparse(tag.get('href'))
            if 'twitter' in parse_result.netloc:
                twitter_id = parse_result.path.split('/')[-1]
                liver.twitter_id = twitter_id
                liver.save()
            if 'youtube' in parse_result.netloc:
                channel_id = parse_result.path.split('/')[-1]
                try:
                    channel = Channel.objects.get(cid=channel_id)
                except Channel.DoesNotExist:
                    channel = Channel(cid=channel_id)
                    channel.save()
                liver.channel = channel
                liver.save()

        print('{} / {}'.format(liver.name, liver.slug))
