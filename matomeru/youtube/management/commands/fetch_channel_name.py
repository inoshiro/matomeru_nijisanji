from django.core.management.base import BaseCommand, CommandError
from youtube.models import Channel

import os
import pyyoutube


class Command(BaseCommand):
    help = 'Fetch channel name from youtube API.'

    def add_arguments(self, parser):
        parser.add_argument('channel_ids', nargs='*', type=str)

        parser.add_argument(
            '--all',
            action='store_true',
            help='fetch all liver channel info.'
        )

    def handle(self, *args, **options):
        if options['all']:
            channels = Channel.objects.all()
            for channel in channels:
                channel_name = self._fetch_channel_name(channel.cid)
                channel.name = channel_name
                channel.save()
            return

        if not options['channel_ids']:
            raise CommandError('Channel ids are required.')

        for channel_id in options['channel_ids']:
            try:
                channel = Channel.objects.get(cid=channel_id)
            except Channel.DoesNotExist:
                CommandError('Channel(id={}) is not exist.'.format(channel_id))
            channel_name = self._fetch_channel_name(channel_id)
            channel.name = channel_name
            channel.save()

    def _fetch_channel_name(self, channel_id):
        youtube_api = pyyoutube.Api(api_key=os.environ['YOUTUBE_API_KEY'])
        channel_data = youtube_api.get_channel_info(channel_id=channel_id)
        return channel_data.items[0].snippet.title
