# Copyright (C) 2020-2022 TeamDerUntergang <https://github.com/TeamDerUntergang>
#
# This file is part of TeamDerUntergang project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from PIL import Image, ImageColor
from unicorn import HELP
from geezram.core import edit, extract_args, get_translation, reply_img, unicorn


@unicorn(pattern='^.color')
def color(message):
    input_str = extract_args(message)

    if input_str.startswith('#'):
        try:
            usercolor = ImageColor.getrgb(input_str)
        except Exception as e:
            edit(message, str(e))
            return False
        else:
            im = Image.new(mode='RGB', size=(1920, 1080), color=usercolor)
            im.save('unicorncik.png', 'PNG')
            reply_img(
                message,
                'unicorncik.png',
                caption=input_str,
                delete_file=True,
                delete_orig=True,
            )
    else:
        edit(message, f'`{get_translation("colorsUsage")}`')


HELP.update({'color': get_translation('colorsInfo')})
