# Copyright (C) 2020-2022 TeamDerUntergang <https://github.com/TeamDerUntergang>
#
# This file is part of TeamDerUntergang project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from ast import Add, BinOp, BitXor, Div, Mult, Num, Pow, Sub, UnaryOp, USub, parse
from datetime import datetime
from getpass import getuser
from operator import add, mul, neg, pow, sub, truediv, xor
from shutil import which

from pyrogram.raw.functions.help import GetNearestDc
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from sys import version as pyver
from pyrogram import __version__ as pyrover
from unicorn import ALIVE_MSG, BOT_VERSION, CHANNEL, HELP, HOSTNAME, USER
from geezram.core import (
    edit,
    extract_args,
    get_translation,
    reply,
    reply_doc,
    unicorn,
    send_log,
)
logo = "https://telegra.ph/file/4b788cea5c1413f9496a3.png"
# ================= CONSTANT =================
CUSTOM_MSG = ALIVE_MSG or f"`{get_translation('unicornAlive')}`"
# ============================================


@unicorn(pattern='^.neofetch$')
def neofetch(message):
    try:
        from subprocess import PIPE, Popen

        process = Popen(
            ['neofetch', f'HOSTNAME={HOSTNAME}', f'USER={USER}', '--stdout'],
            stdout=PIPE,
            stderr=PIPE,
        )
        result, _ = process.communicate()
        edit(message, f'`{result.decode()}`')
    except BaseException:
        edit(message, f'`{get_translation("neofetchNotFound")}`')


@unicorn(pattern='^.botver$')
def bot_version(message):
    if which('git'):
        from subprocess import PIPE, Popen

        changes = Popen(
            ['git', 'rev-list', '--all', '--count'],
            stdout=PIPE,
            stderr=PIPE,
            universal_newlines=True,
        )
        result, _ = changes.communicate()

        edit(
            message,
            get_translation(
                'unicornShowBotVersion',
                ['**', '`', CHANNEL, BOT_VERSION, result],
            ),
            preview=False,
        )
    else:
        edit(message, f'`{get_translation("unicornGitNotFound")}`')


@unicorn(pattern='^.ping$')
def ping(message):
    start = datetime.now()
    edit(message, '**Pong!**')
    finish = datetime.now()
    time = (finish - start).microseconds / 1000
    edit(message, f'**Pong!**\n`{time}ms`')


#@unicorn(pattern='^.alive$')
#async def alive(message):
    #Alive_msg = f"**[Unicorn-Pyrobot](https://t.me/deldelinaa):**\n\n"
    #Alive_msg += f"**Python:** `{pyver.split()[0]}`\n"
    #Alive_msg += f"**Pyrogram:** `{pyrover}`\n"
    #Alive_msg += f"**Profiles:** [BOT](t.me/{USER})\n"
    #Alive_msg += f"**Unicorn Version:** `{BOT_VERSION}\n\n`"
    #Alive_msg += f"**Powered By : Geez | RAM | TOD**" 
    #await message.reply_photo(
    #photo=logo,
    #caption=Alive_msg,
    #reply_markup=InlineKeyboardMarkup(
    #        [[
    #                InlineKeyboardButton(
    #                    "• Geez •", url="https://t.me/GeezSupport")
    #            ], [
    #                InlineKeyboardButton(
    #                    "• RAM •", url="https://t.me/ramsupportt")
     #           ]],
    #    ),
    #)
    
 


@unicorn(pattern='^.echo')
def test_echo(message):
    args = extract_args(message)
    if len(args) > 0:
        message.delete()
        reply(message, args)
    else:
        edit(message, f'`{get_translation("echoHelp")}`')


@unicorn(pattern='^.dc$', compat=False)
def data_center(client, message):
    result = client.invoke(GetNearestDc())

    edit(
        message,
        get_translation(
            'unicornNearestDC',
            ['**', '`', result.country, result.nearest_dc, result.this_dc],
        ),
    )


@unicorn(pattern='^.term')
def terminal(message):
    command = extract_args(message)

    if len(command) < 1:
        edit(message, f'`{get_translation("termUsage")}`')
        return

    curruser = getuser()
    try:
        from os import geteuid

        uid = geteuid()
    except ImportError:
        uid = 0

    if not command:
        edit(message, f'`{get_translation("termHelp")}`')
        return

    result = get_translation("termNoResult")
    try:
        from geezram.core.misc import __status_out__

        _, result = __status_out__(command)
    except BaseException as e:
        pass

    if len(result) > 4096:
        output = open('output.txt', 'w+')
        output.write(result)
        output.close()
        reply_doc(
            message,
            'output.txt',
            caption=f'`{get_translation("outputTooLarge")}`',
            delete_after_send=True,
        )
        return

    edit(message, f'`{curruser}:~{"#" if uid == 0 else "$"} {command}\n{result}`')

    send_log(get_translation('termLog', [command]))


@unicorn(pattern='^.eval')
def eval(message):
    args = extract_args(message)
    if len(args) < 1:
        edit(message, f'`{get_translation("evalUsage")}`')
        return

    try:
        evaluation = safe_eval(args)
        if evaluation:
            if isinstance(evaluation, str):
                if len(evaluation) >= 4096:
                    file = open('output.txt', 'w+')
                    file.write(evaluation)
                    file.close()
                    reply_doc(
                        message,
                        'output.txt',
                        caption=f'`{get_translation("outputTooLarge")}`',
                        delete_after_send=True,
                    )
                    return
                edit(
                    message,
                    get_translation('unicornQuery', ['**', '`', args, evaluation]),
                )
        else:
            edit(
                message,
                get_translation(
                    'unicornQuery', ['**', '`', args, get_translation('unicornErrorResult')]
                ),
            )
    except Exception as err:
        edit(message, get_translation('unicornQuery', ['**', '`', args, str(err)]))

    send_log(get_translation('evalLog', [args]))


operators = {
    Add: add,
    Sub: sub,
    Mult: mul,
    Div: truediv,
    Pow: pow,
    BitXor: xor,
    USub: neg,
}


def safe_eval(expr):
    expr = expr.lower().replace('x', '*').replace(' ', '')
    return str(_eval(parse(expr, mode='eval').body))


def _eval(node):
    if isinstance(node, Num):
        return node.n
    elif isinstance(node, BinOp):
        return operators[type(node.op)](_eval(node.left), _eval(node.right))
    elif isinstance(node, UnaryOp):
        return operators[type(node.op)](_eval(node.operand))
    else:
        raise TypeError(f'`{get_translation("safeEval")}`')


HELP.update({'system': get_translation('systemInfo')})
