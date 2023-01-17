# Copyright (c) 2023, Kanda-Mashiro. All rights reserved.
#
# Use of this code is governed by a MIT license
# that can be found in the LICENSE file.

# -*- coding: utf-8 -*-

import click


@click.group()
def workspace():
    pass


@click.command()
def init():
    pass


@click.command()
def shadow():
    pass


@click.command()
def deshadow():
    pass


@click.command()
def list():
    pass


@click.command()
def status():
    pass


workspace.add_command(init)
workspace.add_command(shadow)
workspace.add_command(deshadow)
workspace.add_command(list)
workspace.add_command(status)
