# Copyright (c) 2023, Kanda-Mashiro. All rights reserved.
#
# Use of this code is governed by a MIT license
# that can be found in the LICENSE file.

# -*- coding: utf-8 -*-

import click

from meshsync.node.command import node


@click.group()
def meshsync():
    pass


meshsync.add_command(node)

meshsync()
