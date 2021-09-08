import keyboard
from time import sleep
from Helpers import Offset, Vars

trigger_bot_in_on = False

def handle_trigger_bot():

    global trigger_bot_in_on

    if keyboard.is_pressed('F3'):
        trigger_bot_in_on = not trigger_bot_in_on
        sleep(0.2)

    if trigger_bot_in_on:
        crosshair = Vars.process.read_int(Vars.player + Offset.m_i_crosshair_id)
        my_team = Vars.process.read_int(Vars.player + Offset.m_i_team_num)
        entity = Vars.process.read_int(Vars.client + Offset.dw_entity_list + (crosshair - 1) * 0x10)
        team = Vars.process.read_int (entity + Offset.m_i_team_num)
        health = Vars.process.read_int (entity + Offset.m_i_health)
        if my_team != team and health > 0:
            Vars.process.write_int(Vars.client + Offset.dw_force_attack, 5)
            sleep(.02)
            Vars.process.write_int(Vars.client + Offset.dw_force_attack, 4)
