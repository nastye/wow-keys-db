import keys_model
import slpp
import time
from bottle import run, get, post, request, template, BaseRequest
BaseRequest.MEMFILE_MAX = 1024 * 1024


@get('/')
def idx():
    keys_model.db.connect()

    def determine_row_color(character):
        if character.character_class == 'DEATHKNIGHT':
            return 'style=\"background-color:#C41E3A\"'
        elif character.character_class == 'DEMONHUNTER':
            return 'style=\"background-color:#A330C9\"'
        elif character.character_class == 'DRUID':
            return 'style=\"background-color:#FF7C0A\"'
        elif character.character_class == 'EVOKER':
            return 'style=\"background-color:#33937F\"'
        elif character.character_class == 'HUNTER':
            return 'style=\"background-color:#AAD372\"'
        elif character.character_class == 'MAGE':
            return 'style=\"background-color:#3FC7EB\"'
        elif character.character_class == 'MONK':
            return 'style=\"background-color:#00FF98\"'
        elif character.character_class == 'PALADIN':
            return 'style=\"background-color:#F48CBA\"'
        elif character.character_class == 'PRIEST':
            return 'style=\"background-color:#FFFFFF\"'
        elif character.character_class == 'ROGUE':
            return 'style=\"background-color:#FFF468\"'
        elif character.character_class == 'SHAMAN':
            return 'style=\"background-color:#0070DD\"'
        elif character.character_class == 'WARLOCK':
            return 'style=\"background-color:#8788EE\"'
        elif character.character_class == 'WARRIOR':
            return 'style=\"background-color:#C69B6D\"'

    tpl = template('idx', characters=keys_model.Character.select(),
                   time=int(time.time()), row_color=determine_row_color)
    keys_model.db.close()
    return tpl


@post('/')
def post_character():
    if request.files.get('SavedInstances.lua'):
        fileupload = request.files.get('SavedInstances.lua')
        data = slpp.slpp.decode(fileupload.file.read()
                                .decode('UTF-8')
                                .replace('SavedInstancesDB = ', ''))

        characters_added = []
        keys_model.db.connect()

        for toon in data['Toons'].keys():
            if data['Toons'][toon]['MythicKey'] \
                    and data['Toons'][toon]['MythicKey']['ResetTime'] \
                    and data['Toons'][toon]['MythicKey']['ResetTime'] > int(time.time()):
                character_name = toon.split(' - ')[0]
                character_realm = toon.split(' - ')[1]
                character_class = data['Toons'][toon]['Class']
                character_item_level = data['Toons'][toon]['ILe']
                if data['Toons'][toon]['MythicKey']['name']:
                    dungeon_name = data['Toons'][toon]['MythicKey']['name']
                    dungeon_level = data['Toons'][toon]['MythicKey']['level']
                    dungeon_reset_time = data['Toons'][toon]['MythicKey']['ResetTime']
                else:
                    dungeon_name = ' '
                    dungeon_level = ' '
                    dungeon_reset_time = ' '

                co, created = keys_model.Character.get_or_create(
                    character_name=character_name, character_realm=character_realm)

                co.character_name = character_name
                co.character_realm = character_realm
                co.character_class = character_class
                co.character_item_level = character_item_level
                co.dungeon_name = dungeon_name
                co.dungeon_level = dungeon_level
                co.dungeon_reset_time = dungeon_reset_time
                updated = co.save()

                characters_added.append((toon, updated))

        keys_model.db.close()

        print(str(characters_added))

        return str(characters_added)
    else:
        return '???'


def main():
    run(host='0.0.0.0', port=8080)
