# Copyright (C) 2020-2022 TeamDerUntergang <https://github.com/TeamDerUntergang>
#
# This file is part of TeamDerUntergang project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from requests import get
from unicorn import HELP, UNI_LANG, WEATHER
from geezram.core import edit, extract_args, get_translation, unicorn

# ===== CONSTANT =====
if WEATHER:
    DEFCITY = WEATHER
else:
    DEFCITY = None
# ====================


@unicorn(pattern='^.(weather|w(eathe|tt)r)')
def weather(message):
    args = extract_args(message)

    if len(args) < 1:
        CITY = DEFCITY
        if not CITY:
            edit(message, f'`{get_translation("weatherErrorCity")}`')
            return
    else:
        CITY = args

    if ',' in CITY:
        CITY = CITY[: CITY.find(',')].strip()

    try:
        req = get(
            f'http://wttr.in/{CITY}?mqT0',
            headers={'User-Agent': 'curl/7.66.0', 'Accept-Language': UNI_LANG},
        )
        data = req.text
        if '===' in data:
            raise Exception
        data = data.replace('`', '‛')
        edit(message, f'`{data}`')
    except Exception:
        edit(message, f'`{get_translation("weatherErrorServer")}`')


HELP.update({'weather': get_translation('infoWeather')})
