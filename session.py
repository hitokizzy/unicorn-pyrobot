# Copyright (C) 2020-2022 TeamDerUntergang <https://github.com/TeamDerUntergang>
#
# This file is part of TeamDerUntergang project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from os import environ
from os.path import isfile

from dotenv import load_dotenv
from pyrogram import Client

if isfile('config.env'):
    load_dotenv('config.env')


def select_lang():
    lang = ''
    while not lang:
        lang = input('Select lang (tr, en): ')

        while lang.lower() not in ('tr', 'en'):
            lang = input('Select lang (tr, en): ')
    return lang


def get_api_hash():
    API_ID = environ.get('API_ID', '')
    API_HASH = environ.get('API_HASH', '') 

    while not API_ID.isdigit() or len(API_ID) < 5 or len(API_ID) > 8:
        API_ID = input('API ID: ')

    API_ID = int(API_ID)

    while len(API_HASH) != 32:
        API_HASH = input('API HASH: ')
    return API_ID, API_HASH


def get_session():
    if lang == 'en':
        print(
            '''\nPlease go to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details\n'''
        )
        API_ID, API_HASH = get_api_hash()
        app = Client('unicorn', api_id=API_ID, api_hash=API_HASH)
        with app:
            self = app.get_me()
            session = app.export_session_string()
            out = f'''**Hi [{self.first_name}](tg://user?id={self.id})
\nAPI_ID:** `{API_ID}`
\n**API_HASH:** `{API_HASH}`
\n**SESSION:** `{session}`
\n**NOTE: Don't give your account information to others!**'''
            out2 = 'Session successfully generated!'
            if self.is_bot:
                print(f'{session}\n{out2}')
            else:
                app.send_message('me', out)
                print(
                    '''Session successfully generated!
Please check your Telegram Saved Messages'''
                )

    elif lang == 'tr':
        print(
            '''L??tfen my.telegram.org adresine gidin
Telegram hesab??n??z?? kullanarak giri?? yap??n
API Development Tools k??sm??na t??klay??n
Gerekli ayr??nt??lar?? girerek yeni bir uygulama olu??turun\n'''
        )
        API_ID, API_HASH = get_api_hash()
        app = Client('unicorn', api_id=API_ID, api_hash=API_HASH)
        with app:
            self = app.get_me()
            session = app.export_session_string()
            out = f'''**Merhaba [{self.first_name}](tg://user?id={self.id})
\nAPI_ID:** `{API_ID}`
\n**API_HASH:** `{API_HASH}`
\n**SESSION:** `{session}`
\n**NOT: Hesap bilgileriniz ba??kalar??na vermeyin!**'''
            out2 = 'Session ba??ar??yla olu??turuldu!'
            if self.is_bot:
                print(f'{session}\n{out2}')
            else:
                app.send_message('me', out)
                print(
                    '''Session ba??ar??yla olu??turuldu!
L??tfen Telegram Kay??tl?? Mesajlar??n??z?? kontrol edin.'''
                )


lang = select_lang()
get_session()
