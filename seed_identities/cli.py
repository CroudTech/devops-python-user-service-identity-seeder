#!/usr/bin/python3
import click
from .seeder import Seeder

@click.command()
@click.option('--source', required=True, default="http://croudie-network-django.prod-v3-network/croudies", help='The source API endpoint')
@click.option('--dest', required=True, default="http://identity-api.prod-v3-network/api/users", help='The destination API endpoint')
def cli(source, dest):
    click.echo(click.style("Source: {}, Dest: {}".format(source, dest), fg='green'))
    seeder = Seeder(source, dest)

@click.command()
def version():
    """ Takes no arguments, outputs version info"""
    click.echo(__version__)

if __name__ == '__main__':
    cli()