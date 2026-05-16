import ctypes
import time
import sys

# 1. Map the Windows Multimedia C-Types Structures
class MIDIOUTCAPSW(ctypes.Structure):
    _fields_ = [
        ('wMid', ctypes.c_ushort),
        ('wPid', ctypes.c_ushort),
        ('vDriverVersion', ctypes.c_ulong),
        ('szPname', ctypes.c_wchar * 32), # Holds the port name
        ('wTechnology', ctypes.c_ushort),
        ('wVoices', ctypes.c_ushort),
        ('wNotes', ctypes.c_ushort),
        ('wChannelMask', ctypes.c_ushort),
        ('dwSupport', ctypes.c_ulong),
    ]

def fire_bare_metal_note():
    # Load the native Windows Multimedia DLL
    try:
        winmm = ctypes.windll.winmm
    except Exception as e:
        print(f" ERROR: Failed to link to Windows Multimedia subsystem: {e}")
        return

    print("[Synaptic Core] Scanning Windows Multimedia subsystem natively...")
    
    # Query how many MIDI output devices Windows sees
    num_devs = winmm.midiOutGetNumDevs()
    target_device_id = None
    port_name_target = "Synapse_Out"

    # Loop through hardware/virtual devices to find loopMIDI
    for i in range(num_devs):
        caps = MIDIOUTCAPSW()
        winmm.midiOutGetDevCapsW(i, ctypes.byref(caps), ctypes.sizeof(caps))
        print(f" -> Found System Port [{i}]: {caps.szPname}")
        if port_name_target in caps.szPname:
            target_device_id = i
            break

    if target_device_id is None:
        print(f"\n ERROR: '{port_name_target}' was not detected by the Windows kernel.")
        print("-> Ensure 'loopMIDI' is running and you have added a port with that exact name.")
        return

    print(f"[Synaptic Core] Handshaking directly with Device ID [{target_device_id}]")

    # Open the MIDI device handle
    h_midi_out = ctypes.c_void_p()
    open_res = winmm.midiOutOpen(ctypes.byref(h_midi_out), target_device_id, 0, 0, 0)
    
    if open_res != 0:
        print(f" ERROR: Windows refused to allocate MIDI device handle. Code: {open_res}")
        return

    try:
        # Construct raw MIDI messages using bitwise operations
        # Format: 0x00 [Velocity] [Note] [Status]
        note_on_msg = 0x90 | (60 << 8) | (100 << 16)   # Note On, Middle C (60), Vel 100, Ch 0
        note_off_msg = 0x80 | (60 << 8) | (0 << 16)     # Note Off, Middle C (60), Vel 0, Ch 0

        print("[Synaptic Core] Streaming raw bytes directly to Windows kernel... NOW.")
        
        # Fire Note On
        winmm.midiOutShortMsg(h_midi_out, note_on_msg)
        time.sleep(0.5) # Sustain for 500ms
        
        # Fire Note Off
        winmm.midiOutShortMsg(h_midi_out, note_off_msg)
        print("[Synaptic Core] Raw bytes transmitted. Bare-metal loopback verified.")

    except Exception as e:
        print(f" Execution fault during stream: {e}")
    finally:
        # Always close the handle to release the system driver resource
        winmm.midiOutClose(h_midi_out)
        print("[Synaptic Core] System driver released cleanly.")

if __name__ == "__main__":
    fire_bare_metal_note()  # Fully unified name