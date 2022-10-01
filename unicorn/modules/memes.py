# Copyright (C) 2020-2022 TeamDerUntergang <https://github.com/TeamDerUntergang>
#
# This file is part of TeamDerUntergang project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from io import BytesIO
from random import choice, getrandbits, randint
from re import sub
from textwrap import wrap
from time import sleep

from cowpy import cow
from PIL import Image, ImageDraw, ImageFont
from requests import get
from unicorn import HELP
from geezram.core import (
    download_media_wc,
    edit,
    extract_args,
    get_download_dir,
    get_translation,
    parse_cmd,
    reply_img,
    reply_sticker,
    unicorn,
)

# ================= CONSTANT =================
ZALGS = [
    [
        '̖',
        ' ̗',
        ' ̘',
        ' ̙',
        ' ̜',
        ' ̝',
        ' ̞',
        ' ̟',
        ' ̠',
        ' ̤',
        ' ̥',
        ' ̦',
        ' ̩',
        ' ̪',
        ' ̫',
        ' ̬',
        ' ̭',
        ' ̮',
        ' ̯',
        ' ̰',
        ' ̱',
        ' ̲',
        ' ̳',
        ' ̹',
        ' ̺',
        ' ̻',
        ' ̼',
        ' ͅ',
        ' ͇',
        ' ͈',
        ' ͉',
        ' ͍',
        ' ͎',
        ' ͓',
        ' ͔',
        ' ͕',
        ' ͖',
        ' ͙',
        ' ͚',
        ' ',
    ],
    [
        ' ̍',
        ' ̎',
        ' ̄',
        ' ̅',
        ' ̿',
        ' ̑',
        ' ̆',
        ' ̐',
        ' ͒',
        ' ͗',
        ' ͑',
        ' ̇',
        ' ̈',
        ' ̊',
        ' ͂',
        ' ̓',
        ' ̈́',
        ' ͊',
        ' ͋',
        ' ͌',
        ' ̃',
        ' ̂',
        ' ̌',
        ' ͐',
        ' ́',
        ' ̋',
        ' ̏',
        ' ̽',
        ' ̉',
        ' ͣ',
        ' ͤ',
        ' ͥ',
        ' ͦ',
        ' ͧ',
        ' ͨ',
        ' ͩ',
        ' ͪ',
        ' ͫ',
        ' ͬ',
        ' ͭ',
        ' ͮ',
        ' ͯ',
        ' ̾',
        ' ͛',
        ' ͆',
        ' ̚',
    ],
    [
        ' ̕',
        ' ̛',
        ' ̀',
        ' ́',
        ' ͘',
        ' ̡',
        ' ̢',
        ' ̧',
        ' ̨',
        ' ̴',
        ' ̵',
        ' ̶',
        ' ͜',
        ' ͝',
        ' ͞',
        ' ͟',
        ' ͠',
        ' ͢',
        ' ̸',
        ' ̷',
        ' ͡',
    ],
]

EMOJIS = [
    '😂',
    '😂',
    '👌',
    '✌',
    '💞',
    '👍',
    '👌',
    '💯',
    '🎶',
    '👀',
    '😂',
    '👓',
    '👏',
    '👐',
    '🍕',
    '💥',
    '🍴',
    '💦',
    '💦',
    '🍑',
    '🍆',
    '😩',
    '😏',
    '👉👌',
    '👀',
    '👅',
    '😩',
    '🚰',
    '♿',
]

UWUS = [
    '(・`ω´・)',
    ';;w;;',
    'owo',
    'UwU',
    '>w<',
    '^w^',
    r'\(^o\) (/o^)/',
    '( ^ _ ^)∠☆',
    '(ô_ô)',
    '~:o',
    ';-;',
    '(*^*)',
    '(>_',
    '(♥_♥)',
    '*(^O^)*',
    '((+_+))',
]

REACTS = [
    'ʘ‿ʘ',
    'ヾ(-_- )ゞ',
    '(っ˘ڡ˘ς)',
    '(´ж｀ς)',
    '( ಠ ʖ̯ ಠ)',
    '(° ͜ʖ͡°)╭∩╮',
    '(ᵟຶ︵ ᵟຶ)',
    '(งツ)ว',
    'ʚ(•｀',
    '(っ▀¯▀)つ',
    '(◠﹏◠)',
    '( ͡ಠ ʖ̯ ͡ಠ)',
    '( ఠ ͟ʖ ఠ)',
    '(∩｀-´)⊃━☆ﾟ.*･｡ﾟ',
    '(⊃｡•́‿•̀｡)⊃',
    '(._.)',
    '{•̃_•̃}',
    '(ᵔᴥᵔ)',
    '♨_♨',
    '⥀.⥀',
    'ح˚௰˚づ ',
    '(҂◡_◡)',
    '(っ•́｡•́)♪♬',
    '◖ᵔᴥᵔ◗ ♪ ♫ ',
    '(☞ﾟヮﾟ)☞',
    '[¬º-°]¬',
    '(Ծ‸ Ծ)',
    '(•̀ᴗ•́)و ̑̑',
    'ヾ(´〇`)ﾉ♪♪♪',
    "(ง'̀-'́)ง",
    'ლ(•́•́ლ)',
    'ʕ •́؈•̀ ₎',
    '♪♪ ヽ(ˇ∀ˇ )ゞ',
    'щ（ﾟДﾟщ）',
    '( ˇ෴ˇ )',
    '눈_눈',
    '(๑•́ ₃ •̀๑) ',
    '( ˘ ³˘)♥ ',
    'ԅ(≖‿≖ԅ)',
    '♥‿♥',
    '◔_◔',
    '⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾',
    '乁( ◔ ౪◔)「      ┑(￣Д ￣)┍',
    '( ఠൠఠ )ﾉ',
    '٩(๏_๏)۶',
    '┌(ㆆ㉨ㆆ)ʃ',
    'ఠ_ఠ',
    '(づ｡◕‿‿◕｡)づ',
    '(ノಠ ∩ಠ)ノ彡( \\o°o)\\',
    '“ヽ(´▽｀)ノ”',
    '༼ ༎ຶ ෴ ༎ຶ༽',
    '｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡',
    '(づ￣ ³￣)づ',
    '(⊙.☉)7',
    'ᕕ( ᐛ )ᕗ',
    't(-_-t)',
    '(ಥ⌣ಥ)',
    'ヽ༼ ಠ益ಠ ༽ﾉ',
    '༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽',
    'ミ●﹏☉ミ',
    '(⊙_◎)',
    '¿ⓧ_ⓧﮌ',
    'ಠ_ಠ',
    '(´･_･`)',
    'ᕦ(ò_óˇ)ᕤ',
    '⊙﹏⊙',
    '(╯°□°）╯︵ ┻━┻',
    r'¯\_(⊙︿⊙)_/¯',
    '٩◔̯◔۶',
    '°‿‿°',
    'ᕙ(⇀‸↼‶)ᕗ',
    '⊂(◉‿◉)つ',
    'V•ᴥ•V',
    'q(❂‿❂)p',
    'ಥ_ಥ',
    'ฅ^•ﻌ•^ฅ',
    'ಥ﹏ಥ',
    '（ ^_^）o自自o（^_^ ）',
    'ಠ‿ಠ',
    'ヽ(´▽`)/',
    'ᵒᴥᵒ#',
    '( ͡° ͜ʖ ͡°)',
    '┬─┬﻿ ノ( ゜-゜ノ)',
    'ヽ(´ー｀)ノ',
    '☜(⌒▽⌒)☞',
    'ε=ε=ε=┌(;*´Д`)ﾉ',
    '(╬ ಠ益ಠ)',
    '┬─┬⃰͡ (ᵔᵕᵔ͜ )',
    '┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻',
    r'¯\_(ツ)_/¯',
    'ʕᵔᴥᵔʔ',
    '(`･ω･´)',
    'ʕ•ᴥ•ʔ',
    'ლ(｀ー´ლ)',
    'ʕʘ̅͜ʘ̅ʔ',
    '（　ﾟДﾟ）',
    r'¯\(°_o)/¯',
    '(｡◕‿◕｡)',
]

RUNS = [get_translation(f'runstr{i+1}') for i in range(0, 48)]

SHGS = [
    '┐(´д｀)┌',
    '┐(´～｀)┌',
    '┐(´ー｀)┌',
    '┐(￣ヘ￣)┌',
    '╮(╯∀╰)╭',
    '╮(╯_╰)╭',
    '┐(´д`)┌',
    '┐(´∀｀)┌',
    'ʅ(́◡◝)ʃ',
    '┐(ﾟ～ﾟ)┌',
    "┐('д')┌",
    '┐(‘～`;)┌',
    'ヘ(´－｀;)ヘ',
    '┐( -“-)┌',
    'ʅ（´◔౪◔）ʃ',
    'ヽ(゜～゜o)ノ',
    'ヽ(~～~ )ノ',
    '┐(~ー~;)┌',
    '┐(-。ー;)┌',
    r'¯\_(ツ)_/¯',
    r'¯\_(⊙_ʖ⊙)_/¯',
    r'¯\_༼ ಥ ‿ ಥ ༽_/¯',
    '乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ',
]

CRYS = [
    'أ‿أ',
    '╥﹏╥',
    '(;﹏;)',
    '(ToT)',
    '(┳Д┳)',
    '(ಥ﹏ಥ)',
    '（；へ：）',
    '(T＿T)',
    '（πーπ）',
    '(Ｔ▽Ｔ)',
    '(⋟﹏⋞)',
    '（ｉДｉ）',
    '(´Д⊂ヽ',
    '(;Д;)',
    '（>﹏<）',
    '(TдT)',
    '(つ﹏⊂)',
    '༼☯﹏☯༽',
    '(ノ﹏ヽ)',
    '(ノAヽ)',
    '(╥_╥)',
    '(T⌓T)',
    '(༎ຶ⌑༎ຶ)',
    '(☍﹏⁰)｡',
    '(ಥ_ʖಥ)',
    '(つд⊂)',
    '(≖͞_≖̥)',
    '(இ﹏இ`｡)',
    '༼ಢ_ಢ༽',
    '༼ ༎ຶ ෴ ༎ຶ༽',
]

XDA_STRINGS = [
    'sur',
    'Sir',
    'bro',
    'yes',
    'no',
    'bolte',
    'bolit',
    'bholit',
    'volit',
    'mustah',
    'fap',
    'lit',
    'lmao',
    'iz',
    'jiosim',
    'ijo',
    'nut',
    'workz',
    'workang',
    'flashabl zip',
    'bateri',
    'bacup',
    'bad englis',
    'sar',
    'treble wen',
    'gsi',
    'fox bag',
    'bag fox',
    'fine',
    'bast room',
    'fax',
    'trable',
    'kenzo',
    'plz make room',
    'andreid pai',
    'when',
    'port',
    'mtk',
    'send moni',
    'bad rom',
    'dot',
    'rr',
    'linage',
    'arrows',
    'kernal',
    'meme12',
    'bruh',
    'imail',
    'email',
    'plaka',
    'evox',
]
# ================= CONSTANT =================


@unicorn(pattern=r'^.(\w+)say')
def cowsay(message):
    ext = message.text.split(' ', 1)
    arg = parse_cmd(ext[0])
    arg = arg[: arg.find('say')]
    textx = message.reply_to_message
    if textx and textx.text:
        text = textx.text
    elif len(ext) > 1:
        text = ext[1]
    else:
        edit(message, f'`{get_translation("wrongCommand")}`')
        return

    if arg == 'cow' or arg not in cow.COWACTERS:
        arg = 'default'

    cheese = cow.get_cow(arg)
    cheese = cheese()

    edit(message, f"`{cheese.milk(text).replace('`', '´')}`")


@unicorn(pattern='^:/$')
def kek(message):
    uio = ['/', '\\']
    for i in range(1, 15):
        sleep(0.3)
        edit(message, f':{uio[i % len(uio)]}')


@unicorn(pattern='^.cry$')
def cry(message):
    edit(message, choice(CRYS))


@unicorn(pattern='^.cp')
def copypasta(message):
    textx = message.reply_to_message
    copypasta = extract_args(message)

    if len(copypasta) > 0:
        pass
    elif textx:
        copypasta = textx.text
    else:
        edit(message, f'`{get_translation("cpUsage")}`')
        return

    reply_text = choice(EMOJIS)
    b_char = choice(copypasta).lower()
    for owo in copypasta:
        if owo == ' ':
            reply_text += choice(EMOJIS)
        elif owo in EMOJIS:
            reply_text += owo
            reply_text += choice(EMOJIS)
        elif owo.lower() == b_char:
            reply_text += '🅱️'
        else:
            if bool(getrandbits(1)):
                reply_text += owo.upper()
            else:
                reply_text += owo.lower()
    reply_text += choice(EMOJIS)
    edit(message, reply_text)


@unicorn(pattern='^.vapor')
def vapor(message):
    reply_text = []
    textx = message.reply_to_message
    vapor = extract_args(message)
    if len(vapor) > 0:
        pass
    elif textx:
        vapor = textx.text
    else:
        edit(message, f'`{get_translation("vaporUsage")}`')
        return

    for charac in vapor:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    edit(message, ''.join(reply_text))


@unicorn(pattern='^.str')
def stretch(message):
    textx = message.reply_to_message
    stretch = extract_args(message)
    if len(stretch) > 0:
        pass
    elif textx:
        stretch = textx.text
    else:
        edit(message, f'`{get_translation("strUsage")}`')
        return

    count = randint(3, 10)
    reply_text = sub(r'([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])', (r'\1' * count), stretch)
    edit(message, reply_text)


@unicorn(pattern='^.zal')
def zalgofy(message):
    reply_text = []
    textx = message.reply_to_message
    zalgofy = extract_args(message)
    if len(zalgofy) > 0:
        pass
    elif textx:
        zalgofy = textx.text
    else:
        edit(message, f'`{get_translation("zalUsage")}`')
        return

    for charac in zalgofy:
        if not charac.isalpha():
            reply_text.append(charac)
            continue

        for _ in range(0, 3):
            charac += choice(ZALGS[randint(0, 2)]).strip()

        reply_text.append(charac)

    edit(message, ''.join(reply_text))


@unicorn(pattern='^.owo')
def owo(message):
    textx = message.reply_to_message
    owo = extract_args(message)
    if len(owo) > 0:
        pass
    elif textx:
        owo = textx.text
    else:
        edit(message, f'`{get_translation("owoUsage")}`')
        return

    reply_text = sub(r'(r|l)', 'w', owo)
    reply_text = sub(r'(R|L)', 'W', reply_text)
    reply_text = sub(r'n([aeiou])', r'ny\1', reply_text)
    reply_text = sub(r'N([aeiouAEIOU])', r'Ny\1', reply_text)
    reply_text = sub(r'\!+', ' ' + choice(UWUS), reply_text)
    reply_text = reply_text.replace('ove', 'uv')
    reply_text += ' ' + choice(UWUS)
    edit(message, reply_text)


@unicorn(pattern='^.mock')
def mock(message):
    reply_text = []
    textx = message.reply_to_message
    mock = extract_args(message)
    if len(mock):
        pass
    elif textx:
        mock = textx.text
    else:
        edit(message, f'`{get_translation("mockUsage")}`')
        return

    for charac in mock:
        if charac.isalpha() and randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    edit(message, ''.join(reply_text))


@unicorn(pattern='^.clap')
def clap(message):
    textx = message.reply_to_message
    clap = extract_args(message)
    if clap:
        pass
    elif textx:
        clap = textx.text
    else:
        edit(message, f'`{get_translation("clapUsage")}`')
        return
    reply_text = '👏 '
    reply_text += clap.replace(' ', ' 👏 ')
    reply_text += ' 👏'
    edit(message, reply_text)


@unicorn(pattern='^.lfy')
def lfy(message):
    textx = message.reply_to_message
    qry = extract_args(message)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
    else:
        edit(message, f'`{get_translation("wrongCommand")}`')
        return
        query = query.message
    query_encoded = query.replace(' ', '+')
    lfy_url = f'http://lmgtfy.com/?s=g&iie=1&q={query_encoded}'
    payload = {'format': 'json', 'url': lfy_url}
    r = get('http://is.gd/create.php', params=payload)
    edit(
        message,
        f'`{get_translation("lfyResult")}`' f"\n[{query}]({r.json()['shorturl']})",
    )


@unicorn(pattern=r'.scam', compat=False)
def scam(client, message):
    options = [
        'typing',
        'upload_photo',
        'record_video',
        'upload_video',
        'record_audio',
        'upload_audio',
        'upload_document',
        'find_location',
        'record_video_note',
        'upload_video_note',
        'choose_contact',
        'playing',
    ]
    input_str = extract_args(message)
    args = input_str.split()
    if len(args) == 0:
        scam_action = choice(options)
        scam_time = randint(30, 60)
    elif len(args) == 1:
        try:
            scam_action = str(args[0]).lower()
            scam_time = randint(30, 60)
        except ValueError:
            scam_action = choice(options)
            scam_time = int(args[0])
    elif len(args) == 2:
        scam_action = str(args[0]).lower()
        scam_time = int(args[1])
    else:
        edit(message, f'`{get_translation("wrongCommand")}`')
        return
    try:
        if scam_time > 0:
            chat_id = message.chat.id
            message.delete()
            client.send_chat_action(chat_id, scam_action)
            sleep(scam_time)
    except BaseException:
        return


@unicorn(pattern='^.type')
def type(message):
    textx = message.reply_to_message
    type = extract_args(message)
    if type:
        pass
    elif textx:
        type = textx.text
    else:
        edit(message, f'`{get_translation("wrongCommand")}`')
        return
    typing_symbol = '|'
    old_text = ''
    edit(message, typing_symbol)
    sleep(0.3)
    for character in type:
        old_text = old_text + '' + character
        typing_text = old_text + '' + typing_symbol
        edit(message, typing_text)
        sleep(0.03)
        edit(message, old_text)
        sleep(0.03)


@unicorn(pattern='^[Ss]krrt$')
def skrrt(message):
    t = f'{(message.text or message.caption)[0]}krrt'
    for j in range(16):
        t = f'{t[:-1]}rt'
        edit(message, t)


@unicorn(pattern='^[Oo]of$')
def oof(message):
    t = f'{(message.text or message.caption)[0]}of'
    for j in range(16):
        t = f'{t[:-1]}of'
        edit(message, t)


@unicorn(pattern='^.h$')
def h(message):
    edit(
        message,
        '⠀⠀⠀⠀⠀⠀⠀⢀⠀⠂⠂⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠠⠀⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⠀⠄⠈⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⢸⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢣⠀⠀⠀\n'
        '⠀⠀⠀⢸⠀⠀⠀⡜⠀⡆⠀⠀⠀⢀⣲⠀⠀⠀⠀⠀⠀⠴⠀⠀⡇⠀⠀⡀⠀⠀\n'
        '⠀⠀⠀⡜⠀⠀⠁⠀⠀⠘⠀⠀⠀⠀⠀⢘⣄⠀⠀⠀⡜⣀⠀⢠⠉⠀⠀⢠⠀⠀\n'
        '⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢠⠀⠈⠛⠛⠒⡀⠀⡇⠀⡄⠀⠈⠀⠀\n'
        '⠀⠀⠀⢒⠀⠀⡱⠀⠀⠀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠇⠀⠈⠀⠀⠀⠀\n'
        '⠀⠀⠀⢸⠀⢠⠀⠀⠀⢸⠀⠀⠀⠀⢀⠀⠙⠁⠀⠁⣉⠊⠀⡆⠀⠀⠈⠀⡅⠀\n'
        '⠀⠀⠀⠀⡀⠈⠀⠀⠀⠃⠀⠀⠀⠀⡌⠈⠀⠑⠃⠋⠀⠀⠀⡇⠀⠀⠀⠀⢠⠀\n'
        '⠀⠀⠀⠀⠘⠀⠈⡀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⡀⠈⠀\n'
        '⠀⠀⠀⠀⠀⣂⢀⢸⠀⢱⢀⣤⢀⠀⠃⠀⠀⠀⠀⢂⠀⠀⠂⠂⠀⠀⠀⣘⡈⡀\n'
        '⠀⠀⠀⠀⠀⠀⠠⠹⠓⢸⠀⠀⢀⠓⠀⠀⠀⠀⠀⡞⢀⠀⢀⠀⠀⠀⠐⢹⠂⠀\n'
        '⠀⠀⠀⠀⠀⠀⠀⠈⠛⠇⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠂⠁⠀⠀⠀⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⠀⠀⠀⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⡠⠀⠀⠀⠀⠀⠀⡆⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⠀⠀⠀⠊⠠⠂⠉⢤⣀⠀⠀⠀⠀⢠⠀⠐⠣⠠⢤⠀⠀⠀⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⠀⠀⠀⠁⠂⠤⠼⠓⠓⠒⠀⠀⠀⠈⠂⠀⠀⠀⠂⠚⠁⠀⠀⠀⠀⠀',
    )


@unicorn(pattern='^.(amogu|su)s')
def amogus(message):
    args = extract_args(message)
    reply = message.reply_to_message
    if args:
        pass
    elif reply:
        if not reply.text:
            return edit(message, f'`{get_translation("wrongCommand")}`')
        args = reply.text
    else:
        edit(message, f'`{get_translation("wrongCommand")}`')
        return

    edit(message, f"`{get_translation('processing')}`")

    arr = randint(1, 12)
    fontsize = 100
    FONT_FILE = 'geezram/fonts/OpenSans.ttf'
    # https://github.com/KeyZenD/AmongUs
    url = 'https://raw.githubusercontent.com/KeyZenD/AmongUs/master/'
    font = ImageFont.truetype(FONT_FILE, size=int(fontsize))

    imposter = Image.open(BytesIO(get(f'{url}{arr}.png').content))
    text_ = '\n'.join(['\n'.join(wrap(part, 30)) for part in args.split('\n')])
    w, h = ImageDraw.Draw(Image.new('RGB', (1, 1))).multiline_textsize(
        text_, font, stroke_width=2
    )
    text = Image.new('RGBA', (w + 40, h + 40))
    ImageDraw.Draw(text).multiline_text(
        (15, 15), text_, '#FFF', font, stroke_width=2, stroke_fill='#000'
    )
    w = imposter.width + text.width + 30
    h = max(imposter.height, text.height)
    image = Image.new('RGBA', (w, h))
    image.paste(imposter, (0, h - imposter.height), imposter)
    image.paste(text, (w - text.width, 0), text)
    image.thumbnail((512, 512))

    output = BytesIO()
    output.name = 'sus.webp'
    image.save(output, 'WebP')
    output.seek(0)

    reply_sticker(reply or message, output)
    message.delete()


@unicorn(pattern='^.gay')
def gay_calculator(message):
    args = extract_args(message)
    reply = message.reply_to_message
    random = randint(0, 100)

    try:
        replied_user = reply.from_user
    except BaseException:
        pass

    if random:
        if args:
            return edit(message, f'**{get_translation("gayString", [args, random])}**')
        if reply:
            if replied_user.is_self:
                edit(message, f'**{get_translation("gayString3", [random])}**')
            else:
                return edit(message, f'**{get_translation("gayString2", [random])}**')
        edit(message, f'**{get_translation("gayString3", [random])}**')


@unicorn(pattern='^.react$')
def react(message):
    edit(message, choice(REACTS))


@unicorn(pattern='^.shg$')
def shg(message):
    edit(message, choice(SHGS))


@unicorn(pattern='^.run$')
def run(message):
    edit(message, choice(RUNS))


@unicorn(pattern='^.xda$')
def xda(message):
    """
    Copyright (c) @NaytSeyd, Quotes taken
    from friendly-telegram (https://gitlab.com/friendly-telegram) | 2020"""
    edit(message, choice(XDA_STRINGS))


@unicorn(pattern='^.f (.*)')
def payf(message):
    paytext = extract_args(message)
    pay = (
        f'{paytext * 8}\n{paytext * 8}\n{paytext * 2}\n{paytext * 2}'
        f'\n{paytext * 2}\n{paytext * 6}\n{paytext * 6}\n{paytext * 2}'
        f'\n{paytext * 2}\n{paytext * 2}\n{paytext * 2}\n{paytext * 2}'
    )
    edit(message, pay)


@unicorn(pattern='.mem')
def meme_maker(message):
    args = extract_args(message).upper().split(',')
    reply = message.reply_to_message
    font = 'geezram/fonts/impact.ttf'
    if len(args) == 2:
        top, bottom = args[0], args[1]
    else:
        bottom = args[0 if args[1] == '' else 1]

    if (
        reply
        and reply.media
        and (
            reply.photo
            or (reply.sticker and not reply.sticker.is_animated)
            or (reply.document and 'image' in reply.document.mime_type)
        )
    ):
        media = download_media_wc(reply, f'{get_download_dir()}/image.jpg')
        image = Image.open(media)
        draw = ImageDraw.Draw(image)
        width, height = image.size
        estimated_font_size = find_font_size(''.join(args), font, image, 1)

        text_font = ImageFont.truetype(font, estimated_font_size)
        text_per_line = width // text_font.size
        top_text = wrap(top, width=(text_per_line + 5))
        bottom_text = wrap(bottom, width=(text_per_line + 5))
        y = 10
        for text in top_text:
            text_width, text_height = text_font.getsize(text)
            x = (width - text_width) / 2
            draw.text(
                (x, y),
                text,
                fill='white',
                font=text_font,
                stroke_width=3,
                stroke_fill='black',
            )
            y += text_height
        y = height - text_height * len(bottom_text) - 15
        for text in bottom_text:
            text_width, text_height = text_font.getsize(text)
            x = (width - text_width) / 2
            draw.text(
                (x, y),
                text,
                fill='white',
                font=text_font,
                stroke_width=3,
                stroke_fill='black',
            )
            y += text_height

        image.convert('RGB').save(media, 'JPEG')
        reply_img(reply or message, media, delete_file=True)
        message.delete()
    else:
        edit(message, 'Lütfen bir resim yanıtlayın.')


def get_text_size(text, image, font):
    im = Image.new('RGB', (image.width, image.height))
    draw = ImageDraw.Draw(im)
    return draw.textsize(text, font)


def find_font_size(text, font, image, target_width_ratio):
    # https://stackoverflow.com/a/66091387
    tested_font_size = 100
    tested_font = ImageFont.truetype(font, tested_font_size)
    observed_width, observed_height = get_text_size(text, image, tested_font)
    estimated_font_size = (
        tested_font_size / (observed_width / image.width) * target_width_ratio
    )
    return round(estimated_font_size)


HELP.update({'memes': get_translation('memesInfo')})
