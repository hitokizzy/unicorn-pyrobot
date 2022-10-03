# Copyright (C) 2020-2022 TeamDerUntergang <https://github.com/TeamDerUntergang>
#
# This file is part of TeamDerUntergang project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from collections import OrderedDict

from unicorn import HELP
from geezram.core import edit, extract_args, get_translation, reply, unicorn


@unicorn(pattern='^.(unicorn|help)')
def unicorn(message):
    unicorn = extract_args(message).lower()
    cmds = OrderedDict(sorted(HELP.items()))
    if len(unicorn) > 0:
        if unicorn in cmds:
            edit(message, str(cmds[unicorn]))
        else:
            edit(message, f'**{get_translation("unicornUsage")}**')
    else:
        edit(message, get_translation('unicornUsage2', ['**', '`']))
        metin = f'{get_translation("unicornShowLoadedModules", ["**", "`", len(cmds)])}\n'
        for item in cmds:
            metin += f'• `{item}`\n'
        reply(message, metin)
