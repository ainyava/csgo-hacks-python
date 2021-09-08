import keyboard
from time import sleep
from Helpers import Offset, Vars

bhop_in_on = True

def handle_bhop():
    global bhop_in_on

    if keyboard.is_pressed('F2'):
        bhop_in_on = not bhop_in_on
        sleep(0.2)

    if bhop_in_on:
        flag = Vars.process.read_int(Vars.player + Offset.m_f_flags)
        if keyboard.is_pressed('space') and (flag & 1):
            Vars.process.write_int(Vars.client + Offset.dw_force_jump, 6)
