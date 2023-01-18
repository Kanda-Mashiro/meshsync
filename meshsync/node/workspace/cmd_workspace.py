# Copyright (c) 2023, Kanda-Mashiro. All rights reserved.
#
# Use of this code is governed by a MIT license
# that can be found in the LICENSE file.

# -*- coding: utf-8 -*-

import click

from meshsync.node.workspace.commands.cmd_init import init
from meshsync.node.workspace.commands.cmd_shadow import shadow
from meshsync.node.workspace.commands.cmd_deshadow import deshadow
from meshsync.node.workspace.commands.cmd_list import list
from meshsync.node.workspace.commands.cmd_status import status


@click.group()
def workspace():
    pass


workspace.add_command(init)
workspace.add_command(shadow)
workspace.add_command(deshadow)
workspace.add_command(list)
workspace.add_command(status)
