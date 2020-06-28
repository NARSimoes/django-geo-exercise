import csv

from django.core.management.base import BaseCommand, CommandError
import psycopg2

from exercises.models import Storage
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import fromstr


class Command(BaseCommand):
    help = 'Populate database with a list of points'

    def add_arguments(self, parser):
        """Add arguments: filename and projection!"""
        parser.add_argument('csv_file', type=str)
        parser.add_argument('proj', type=str)

    def handle(self, *args, **options):
        """handle: read csv file and store values in our model Storage and Database!"""
        with open(options['csv_file'], 'r') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                r = row[0].split(";")
                Storage(id=r[0], point=fromstr(f'POINT({r[1]} {r[2]})')).save()

    def _handle(self, *args, **options):
        """Using psycopg2 to feed database!"""
        conn = psycopg2.connect("host=localhost dbname=geodjango user=admin password=admin")
        cur = conn.cursor()

        with open(options['csv_file'], 'r') as f:
            next(f)  # skip header
            cur.copy_from(f, 'positions', sep=';', columns=2)
        conn.commit()
