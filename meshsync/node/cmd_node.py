# Copyright (c) 2023, Kanda-Mashiro. All rights reserved.
#
# Use of this code is governed by a MIT license
# that can be found in the LICENSE file.

# -*- coding: utf-8 -*-

import click

from meshsync.node.workspace.cmd_workspace import workspace


@click.group()
def node():
    pass


node.add_command(workspace)
