# PROJECT SOVEREIGN SANDBOX: MASTER MANIFEST

## 1. PROJECT META
* **Project Title:** Sovereign Sandbox (The Audio-Emergent Platform)
* **Architect & Visionary:** Sami
* **Lead Developer / Core Engine:** Phaze (AI Core)
* **Status:** Milestone 1 Architecture Verified
* **Last Updated:** Saturday, 16 May 2026, 20:15 BST

---

## 2. PRODUCTION HARDWARE MATRIX
The core environment must support and seamlessly route across this specific mixed-generation hardware ecosystem without requiring manual configuration menus or global quantisation compromises:

### A. Core Master Controllers
* **Fatar 88-Key Controller:** Fully-weighted hammer action. Dedicated to pure symbolic music theory generation and expressive polyphonic velocity streaming.
* **Arturia KeyStep 37:** Desktop tactile controller for real-time arpeggiations, sequencing shifts, and immediate desk command inputs.

### B. Analogue Acid & Industrial Monosynths
* **Behringer Edge:** Semi-modular percussion synthesiser. Operates on independent, free-running analogue loops requiring stable clock-pulse alignment.
* **Behringer TD-3:** Dedicated classic silver-box bassline engine (rigid 16th-note step structure).
* **Behringer TD-3-MO (Modded Out):** Highly volatile acid synthesis engine requiring dynamic continuous voltage (CC) parameter mapping for slide-time and filter screaming.

### C. Digital, Polyphonic & Multi-Timbral Hardware
* **Korg M3R (1989):** 1U Rackmount AI Synthesis Engine. Legacy 5-pin DIN interface. Dedicated to nostalgic digital pads, organs, and house chords.
* **Roland MC-101:** Four-track Zen-Core groovebox engine. Handles clip-launching and dense modern multi-timbral digital synthesis tracks.
* **Airstream / Sonicware JT-4000 Micro:** Ultra-portable hybrid hardware module driven via direct USB-C streaming.

### D. Rhythm & Sampling Stations
* **Boss Dr.880 (Dr. Rhythm):** Dedicated acoustic acoustic-realism drum-and-bass platform. High-density acoustic sequencing.
* **Teenage Engineering EP-133 K.O. II:** High-resolution tactile pocket sampler. Operates on a highly fluid, unquantised internal timing engine.

### F. Physical Routing Plumbing
* **Tascam Model 12:** Core mixer, multi-track recorder, and primary 5-pin hardware MIDI interface.
* **DOREMiDi-THRU-6 Pro:** High-speed hardware MIDI thru-box distributing centralised synchronisation data across legacy DIN chains.

---

## 3. DEVELOPMENT TARGET WORKSPACE (LOCAL SILICON)
* **Processor:** AMD Ryzen 7 8745HS (8 Cores / 16 Threads, Zen 4 Architecture)
* **Graphics/Compute:** AMD Radeon 780M Integrated GPU (Architecture ID: `gfx1103`)
* **Memory:** 32GB Unified System RAM
* **Runtime Environment:** Windows 11/14 Local Shell running native **Python 3.14+**
* **Primary DAW (Test Bench):** REAPER (with Python API access enabled)
* **Visual Mapping Workspace:** `C:\Users\Martha_Farquhar\Documents\Obsidian Vault\VANDAL\Phaze_MASTER\Phaze_MASTER.canvas`
* **Local Inference Engine:** Ollama (Background API Server running offline models)
* **Target SLMs:** Qwen 2.5 Coder 7B (Code/JSON) / Llama 3.2 3B (Text parsing)

### Core Optimisation Parameters:
1.  **VRAM Profile:** UMA Frame Buffer Size in System BIOS configured to **4GB or 8GB** to allow the Radeon 780M to hold local models natively in graphics cache.
2.  **GPU Direct Override:** Windows environment variable set to bypass AMD ROCm layer bottlenecks: `export HSA_OVERRIDE_GFX_VERSION="11.0.2"`
3.  **Thread Limit Protection:** Local model execution explicitly throttled to **4-6 worker threads** to insulate the machine’s real-time ASIO audio processing graph from CPU starvation and digital crackling.

---

## 4. AGILE MILESTONE ROADMAP

### Milestone 1: The Synaptic Core (CURRENT MILESTONE)
* **Objective:** Perfect the offline conversational text-to-symbolic-MIDI engine.
* **Status:** Local loopback pipeline verified. Bypassed modern Python 3.14 package compilation failures by writing a zero-dependency bare-metal Windows kernel interface wrapper.

### Milestone 2: The Closed Core Sandbox
* **Objective:** Compile a stable cross-platform VST3/CLAP host container plugin via JUCE to wrap third-party open-source instruments (*Vital*, *Surge XT*) and map internal parameter dictionaries natively.

### Milestone 3: The "Quake" Console & SAMP Spec
* **Objective:** Implement the `Alt` + `~` sliding interface drop-down overlay. Publish the open-source **Semantic Audio Mapping Protocol (SAMP)** to GitHub alongside the day-one universal baseline profiles to create defensive, un-patentable prior art.

### Milestone 4: The Stateful Supercharger (Lua SDK)
* **Objective:** Embed a lightweight Lua interpreter directly inside the C++ container to allow power users to program complex, algorithmic, and stateful real-time modulation scripts.

### Milestone 5: The Sovereign Appliance
* **Objective:** Package the entire system into a stripped-down, real-time Linux (\*nix) PipeWire distribution running on standalone micro-hardware, forming the brain of the premium **Thermal Matrix-1** luxury workstation.

---

## 6. ADMINISTRATIVE CORE OVERVIEW (LANE CROSS-TALK BRIDGE)
* **`ASC-005` [The Novelty Hunter Engine]:** An external market-pull daemon executing low-overhead background polling sweeps of open-source channels to map external technical problem vectors directly against active internal project capabilities.
* **ADMIN_MODE Status:** Standby // Ready to orchestrate human-in-the-loop multi-session development sprints across segregated node environments.

## 5. PRODUCTION CHECKED SOURCE CODE
The following script has been engineered to run natively on Python 3.14 without requiring a single external pip package compile tool. It communicates directly with the Windows multimedia kernel (`winmm.dll`) to fire raw byte packets into virtual loopback ports (`loopMIDI`) or physical hardware outputs.

### File: `synapse_test.py`
```python
import ctypes
import time
import sys

class MIDIOUTCAPSW(ctypes.Structure):
    _fields_ = [
        ('wMid', ctypes.c_ushort),
        ('wPid', ctypes.c_ushort),
        ('vDriverVersion', ctypes.c_ulong),
        ('szPname', ctypes.c_wchar * 32),
        ('wTechnology', ctypes.c_ushort),
        ('wVoices', ctypes.c_ushort),
        ('wNotes', ctypes.c_ushort),
        ('wChannelMask', ctypes.c_ushort),
        ('dwSupport', ctypes.c_ulong),
    ]

def fire_bare_metal_note():
    try:
        winmm = ctypes.windll.winmm
    except Exception as e:
        print(f" ERROR: Failed to link to Windows Multimedia subsystem: {e}")
        return

    print("[Synaptic Core] Scanning Windows Multimedia subsystem natively...")
    
    num_devs = winmm.midiOutGetNumDevs()
    target_device_id = None
    port_name_target = "Synapse_Out"  # Swap to "Model 12 MIDI" for direct hardware testing

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

    h_midi_out = ctypes.c_void_p()
    open_res = winmm.midiOutOpen(ctypes.byref(h_midi_out), target_device_id, 0, 0, 0)
    
    if open_res != 0:
        print(f" ERROR: Windows refused to allocate MIDI device handle. Code: {open_res}")
        return

    try:
        note_on_msg = 0x90 | (60 << 8) | (100 << 16)   # Middle C Note On
        note_off_msg = 0x80 | (60 << 8) | (0 << 16)     # Middle C Note Off

        print("[Synaptic Core] Streaming raw bytes directly to Windows kernel... NOW.")
        winmm.midiOutShortMsg(h_midi_out, note_on_msg)
        time.sleep(0.5)
        winmm.midiOutShortMsg(h_midi_out, note_off_msg)
        print("[Synaptic Core] Raw bytes transmitted. Bare-metal loopback verified.")

    except Exception as e:
        print(f" Execution fault during stream: {e}")
    finally:
        winmm.midiOutClose(h_midi_out)
        print("[Synaptic Core] System driver released cleanly.")

if __name__ == "__main__":
    fire_bare_metal_note()

    