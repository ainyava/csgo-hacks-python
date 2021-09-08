import keyboard
import pymem.process
from pymem import Pymem
from Helpers import Offset, Vars
from wallhack import handle_brightness, handle_glow

cheat_is_running = True

def main():

    # Load process and client module
    Vars.process = Pymem('csgo.exe')
    if not Vars.process:
        print("Cannot find CSGO")
        exit(-1)
    print(f'Process found: {Vars.process.process_id}')

    Vars.engine = pymem.process.module_from_name(Vars.process.process_handle, 'engine.dll').lpBaseOfDll
    Vars.client = pymem.process.module_from_name(Vars.process.process_handle, 'client.dll').lpBaseOfDll

    if not Vars.engine or not Vars.client:
        print('Cant find modules')
        exit(-1)
    print(f'Engine module: {Vars.engine}, Client module: {Vars.client}')

    client_state = Vars.process.read_int(Vars.engine + Offset.dw_client_state)
    if not client_state:
        print('Cant find client state')
        exit(-1)
    print(f'Client state {client_state}')

    handle_brightness()

    global cheat_is_running
    # Run the code for every frame of the game
    while cheat_is_running:

        # Try to find player entity in memory and run it until player found
        player_index = Vars.process.read_int(client_state + Offset.dw_client_state_get_local_player)
        Vars.player = Vars.process.read_int(Vars.client + Offset.dw_entity_list + (player_index * 0x10))

        # Run handlers
        handle_glow()

        if keyboard.is_pressed('F8'):
            cheat_is_running = False


if __name__ == '__main__':
    main()