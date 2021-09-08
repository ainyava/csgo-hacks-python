import keyboard
from time import sleep
from Helpers import Offset, Vars

esp_in_on = False

def handle_brightness():
    pass


def handle_glow():

    global esp_in_on

    if keyboard.is_pressed('F1'):
        esp_in_on = not esp_in_on
        sleep(0.2)

    if esp_in_on or keyboard.is_pressed('F'):
        # find glow object manager
        glow = Vars.process.read_int(Vars.client + Offset.dw_glow_object_manager)
        my_team = Vars.process.read_int(Vars.player + Offset.m_i_team_num)
        # loop through game entities which also contains our allies and enemies
        for i in range(64):
            entity = Vars.process.read_int(Vars.client + Offset.dw_entity_list + (i * 0x10))
            if entity:
                entity_team = Vars.process.read_int(entity + Offset.m_i_team_num)
                glow_index = Vars.process.read_int(entity + Offset.m_i_glow_index)
                health = Vars.process.read_int(entity + Offset.m_i_health)
                # apply glow for our allies and enemies
                # for enemies apply color by their health
                if my_team == entity_team:
                    # blue glow offset
                    Vars.process.write_float(glow + ((glow_index * 0x38) + 0x10), 1.0)
                    # alpha glow offset
                    Vars.process.write_float(glow + ((glow_index * 0x38) + 0x14), 0.7)
                else:
                    # red glow offset
                    Vars.process.write_float(glow + ((glow_index * 0x38) + 0x8), (100 - health) / 100.0)
                    # green glow offset
                    Vars.process.write_float(glow + ((glow_index * 0x38) + 0xC), health / 100.0)
                    # alpha glow offset
                    Vars.process.write_float(glow + ((glow_index * 0x38) + 0x14), 1.0)
                Vars.process.write_char(glow + ((glow_index * 0x38) + 0x29), chr(1))