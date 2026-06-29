"""
Project Phaze Tech — Sovereign Shell Engine (Identity Edition)
Module: sovereign_shell.py
Specification Reference: PROJ_UX_IDENTITY_BANNER (Hierarchical Nomenclature)
Runtime Environment: Pure Python 3.14+ (Zero-Dependency UI Architecture)
Thread Profile: Main UI Thread with Context-Driven Identity States
"""

import tkinter as tk
from tkinter import ttk
import os
from datetime import datetime
import math

class SovereignShellUI:
    def __init__(self, window_root):
        """Initialises the visual shell with dynamic departmental identity tracking."""
        self.root = window_root
        self.root.title("Phaze Sovereign Shell v1.7 -- LOGICAL IDENTITY COCKPIT")
        self.root.geometry("1340x760")
        
        # 3px Solid Copper Outer Border for rapid Alt-Tab visual target capture
        self.root.configure(bg="#D27D2D", bd=3)
        
        # Industrial Colour Palette Definitions
        self.bg_basalt = "#121315"
        self.bg_obsidian = "#070708"
        self.accent_amber = "#FF9F00"
        self.text_muted = "#8A929C"
        self.text_pure = "#FFFFFF"
        self.alert_green = "#00FF66"
        self.link_copper = "#A0522D"
        
        # Dynamic State Trackers for Reciprocal Governance
        self.background_scraping_active = tk.BooleanVar(value=True)
        self.thread_limit_allocation = tk.IntVar(value=4)
        
        # NEW STATE TRACKER: String variable to hold active department head identification
        self.active_agent_identity = tk.StringVar(value="COMMUNICATIONS ANCHOR ➔ STANDBY_MODE")
        
        self.apply_industrial_styling()
        self.assemble_tactile_interface()

    def apply_industrial_styling(self):
        """Configures native layout themes to bind custom components to the industrial palette."""
        style = ttk.Style()
        style.theme_use("clam")
        
        style.configure(
            "Treeview",
            background=self.bg_obsidian,
            fieldbackground=self.bg_obsidian,
            foreground=self.text_pure,
            font=("Consolas", 9),
            rowheight=24,
            bd=0,
            highlightthickness=0
        )
        style.configure("Treeview.Heading", background=self.bg_basalt, foreground=self.text_muted, font=("Consolas", 9, "bold"), borderwidth=0)
        
        style.map(
            "Treeview",
            background=[("selected", self.accent_amber)],
            foreground=[("selected", self.bg_obsidian)]
        )
        style.configure("Sash", background=self.bg_basalt, sashthickness=4)

    def assemble_tactile_interface(self):
        """Builds the industrial layout frames and integrates the identity sub-panes."""
        # Main Canvas Backdrop Frame
        self.main_container = tk.Frame(self.root, bg=self.bg_basalt)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # 1. Routing Header Address Bar
        self.routing_bar = tk.Frame(self.main_container, bg=self.bg_obsidian, height=35)
        self.routing_bar.pack(fill=tk.X, side=tk.TOP, padx=5, pady=5)
        
        self.routing_label = tk.Label(
            self.routing_bar, 
            text="SOVEREIGN://CORE_WORKSPACE//C:\\Users\\Martha_Farquhar\\synaptic_core\\", 
            fg=self.accent_amber, bg=self.bg_obsidian, 
            font=("Consolas", 10, "bold")
        )
        self.routing_label.pack(side=tk.LEFT, padx=10, pady=6)

        # 2. Multi-Panel Native Horizontal Resizable Paned Window
        self.deck_splitter = ttk.PanedWindow(self.main_container, orient=tk.HORIZONTAL)
        self.deck_splitter.pack(fill=tk.BOTH, expand=True, padx=5, pady=0)

        # MODULE A: Node-to-Task Sidebar (Left Column Pane)
        self.sidebar_frame = tk.Frame(self.deck_splitter, bg=self.bg_obsidian, width=330, bd=1)
        
        self.label_sidebar = tk.Label(self.sidebar_frame, text="PHAZE TRACK NODE MAP REGISTRY", fg=self.text_muted, bg=self.bg_obsidian, font=("Consolas", 9, "bold"))
        self.label_sidebar.pack(anchor=tk.NW, padx=10, pady=8)
        
        self.session_tree = ttk.Treeview(self.sidebar_frame, show="tree", selectmode="browse")
        self.session_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.populate_nestable_session_data()
        self.session_tree.bind("<<TreeviewSelect>>", self.handle_session_navigation_click)
        self.deck_splitter.add(self.sidebar_frame, weight=1)

        # MODULE B: High-Transparency Logging Stream & Command Input (Middle Column Pane)
        self.zone_a = tk.Frame(self.deck_splitter, bg=self.bg_obsidian, bd=1)
        
        self.label_a = tk.Label(self.zone_a, text="ZONE A: PROCESS TRANSPARENCY DECK", fg=self.text_muted, bg=self.bg_obsidian, font=("Consolas", 9, "bold"))
        self.label_a.pack(anchor=tk.NW, padx=10, pady=4)
        
        # NEW INTERACTIVE COMPONENT: High-Density Active Identity Banner Block
        self.identity_banner = tk.Frame(self.zone_a, bg=self.bg_basalt, bd=1, relief="solid")
        self.identity_banner.pack(fill=tk.X, padx=10, pady=4)
        
        self.identity_text_label = tk.Label(
            self.identity_banner, 
            textvariable=self.active_agent_identity, 
            fg=self.accent_amber, bg=self.bg_basalt, 
            font=("Consolas", 9, "bold"), anchor="w", justify="left"
        )
        self.identity_text_label.pack(fill=tk.X, padx=8, pady=6)
        
        # Scrolling Telemetry Text Logger Viewport
        self.log_display = tk.Text(self.zone_a, bg=self.bg_obsidian, fg=self.text_pure, insertbackground=self.accent_amber, font=("Consolas", 10), bd=0, highlightthickness=0)
        self.log_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.input_frame = tk.Frame(self.zone_a, bg=self.bg_obsidian)
        self.input_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=(5, 10))
        
        self.prompt_symbol = tk.Label(self.input_frame, text=">>> ", fg=self.accent_amber, bg=self.bg_obsidian, font=("Consolas", 10, "bold"))
        self.prompt_symbol.pack(side=tk.LEFT)
        
        self.command_entry = tk.Entry(self.input_frame, bg=self.bg_basalt, fg=self.text_pure, insertbackground=self.accent_amber, font=("Consolas", 10), bd=1, relief="solid", highlightthickness=0)
        self.command_entry.pack(fill=tk.X, expand=True, side=tk.LEFT)
        self.command_entry.bind("<Return>", self.handle_command_submission)
        self.command_entry.focus_set()
        self.deck_splitter.add(self.zone_a, weight=2)

        # MODULE C: Interactive Obsidian Vector Cluster Map (Right Column Pane)
        self.zone_b = tk.Frame(self.deck_splitter, bg=self.bg_obsidian, width=450, bd=1)
        
        self.label_b = tk.Label(self.zone_b, text="ZONE B: NATIVE VAULT CLUSTER RELATIONS", fg=self.text_muted, bg=self.bg_obsidian, font=("Consolas", 9, "bold"))
        self.label_b.pack(anchor=tk.NW, padx=10, pady=8)
        
        self.media_canvas = tk.Canvas(self.zone_b, bg="#050506", highlightthickness=1, highlightbackground="#1A1C1F")
        self.media_canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.media_canvas.bind("<Configure>", lambda e: self.generate_geometric_vault_clusters())
        self.deck_splitter.add(self.zone_b, weight=2)

        # 3. ZONE C: The Tweakable System Governance Control Tray (Bottom Pane)
        self.zone_c = tk.Frame(self.main_container, bg=self.bg_obsidian, bd=1)
        self.zone_c.pack(fill=tk.X, side=tk.BOTTOM, padx=5, pady=5)
        
        self.status_indicator = tk.Label(self.zone_c, text="● REPOS SYNCED", fg=self.alert_green, bg=self.bg_obsidian, font=("Consolas", 9, "bold"))
        self.status_indicator.pack(side=tk.LEFT, padx=10, pady=12)
        
        self.scraper_check = tk.Checkbutton(
            self.zone_c, text="BACKGROUND DAEMONS", 
            variable=self.background_scraping_active,
            command=self.handle_control_toggle_event,
            bg=self.bg_obsidian, fg=self.text_pure, selectcolor=self.bg_basalt,
            activebackground=self.bg_obsidian, activeforeground=self.accent_amber,
            font=("Consolas", 9, "bold"), bd=0
        )
        self.scraper_check.pack(side=tk.LEFT, padx=20)
        
        self.thread_label = tk.Label(self.zone_c, text="ALLOCATED THREADS:", fg=self.text_muted, bg=self.bg_obsidian, font=("Consolas", 9, "bold"))
        self.thread_label.pack(side=tk.LEFT, padx=(10, 5))
        
        self.thread_spin = tk.Spinbox(
            self.zone_c, from_=1, to=8, width=3, 
            textvariable=self.thread_limit_allocation,
            command=self.handle_thread_throttling_event,
            bg=self.bg_basalt, fg=self.accent_amber, buttonbackground=self.bg_obsidian,
            bd=0, font=("Consolas", 10, "bold"), justify="center"
        )
        self.thread_spin.pack(side=tk.LEFT, padx=5)

        self.heartbeat_btn = tk.Button(self.zone_c, text="DMS HEARTBEAT ENTRY", bg="#1A1C1F", fg=self.text_pure, activebackground=self.accent_amber, font=("Consolas", 8, "bold"), bd=0, padx=12, pady=4, relief="flat")
        self.heartbeat_btn.pack(side=tk.RIGHT, padx=10)

        # Establish default starting channel profile alignment
        self.select_departmental_context("track_3")
        self.stream_telemetry_event("[INIT] Identity Nomenclature Framework Binding Complete.")

    def generate_geometric_vault_clusters(self):
        """Calculates algorithmic node offsets and renders clean 2D interconnected network graphs."""
        self.media_canvas.delete("all")
        w = self.media_canvas.winfo_width()
        h = self.media_canvas.winfo_height()
        if w < 10 or h < 10:
            w, h = 430, 560
            
        centre_x, centre_y = w // 2, h // 2
        
        clusters = {
            "core": (centre_x, centre_y - 30, self.accent_amber, "SYSTEM SPEC"),
            "audio": (centre_x - 100, centre_y + 110, self.alert_green, "PROJ_SAMP"),
            "strategy": (centre_x + 100, centre_y + 110, self.text_muted, "CBO_MARKET")
        }
        
        edges = [("core", "audio"), ("core", "strategy"), ("audio", "strategy")]
        
        for start, end in edges:
            sx, sy, _, _ = clusters[start]
            ex, ey, _, _ = clusters[end]
            self.media_canvas.create_line(sx, sy, ex, ey, fill=self.link_copper, width=1, dash=(4, 4))
            
        node_id = 1
        for key, (cx, cy, color, label) in clusters.items():
            self.media_canvas.create_oval(cx-8, cy-8, cx+8, cy+8, fill=color, outline=self.bg_basalt, width=2)
            self.media_canvas.create_text(cx, cy-18, text=label, fill=color, font=("Consolas", 8, "bold"))
            
            num_orbits = 5 if key == "core" else 4
            radius = 42
            for i in range(num_orbits):
                angle = (2 * math.pi / num_orbits) * i
                nx = cx + int(radius * math.cos(angle))
                ny = cy + int(radius * math.sin(angle))
                
                self.media_canvas.create_line(cx, cy, nx, ny, fill="#1A1C1F", width=1)
                self.media_canvas.create_oval(nx-4, ny-4, nx+4, ny+4, fill=self.bg_basalt, outline=color, width=1.5)
                self.media_canvas.create_text(nx+8, ny, text=f"doc_{node_id:03d}.md", fill="#4A525A", font=("Consolas", 7), anchor="w")
                node_id += 1

    def populate_nestable_session_data(self):
        """Injects core archive tokens completely mapping explicit application hashes to tracking tasks."""
        t1 = self.session_tree.insert("", "end", "track_1", text="app/e912f0aa ➔ Core Audio Layer", open=True)
        t2 = self.session_tree.insert("", "end", "track_2", text="app/f412f00a ➔ Marketing & Arbitrage", open=True)
        t3 = self.session_tree.insert("", "end", "track_3", text="app/c843d11f ➔ Sovereign UX Shell", open=True)
        
        self.session_tree.insert(t1, "end", "sub_1_1", text=" ↳ [Agent #001] [Lane: PROJ_SAMP] Audio Kernel Hook")
        self.session_tree.insert(t1, "end", "sub_1_2", text=" ↳ [Agent #001] [Lane: PROJ_SAMP] ASIO Isolation Threshold")
        
        self.session_tree.insert(t2, "end", "sub_2_1", text=" ↳ [Agent #004] [Lane: CBO_MARKET] Arbitrage Velocity Feed")
        self.session_tree.insert(t2, "end", "sub_2_2", text=" ↳ [Agent #004] [Lane: CBO_MARKET] Defensive Prior-Art Lock")
        
        self.session_tree.insert(t3, "end", "sub_3_1", text=" ↳ [Agent #002] [Lane: PROJ_UX] Interactive Command Box")
        self.session_tree.insert(t3, "end", "sub_3_2", text=" ↳ [Agent #002] [Lane: PROJ_UX] Obsidian Cluster Drawing")

    def select_departmental_context(self, node_id: str):
        """Maps specific node IDs to the formal hierarchical nomenclature tags."""
        if "track_1" in node_id or "sub_1" in node_id:
            self.active_agent_identity.set("CH_COMM_LINK ➔ ASC-CORE-SAMP // BARE-METAL AUDIO ALCHEMIST [Agent #001]")
        elif "track_2" in node_id or "sub_2" in node_id:
            self.active_agent_identity.set("CH_COMM_LINK ➔ ASC-MGMT-CBO  // CHIEF OF BUSINESS OPERATIONS [Agent #004]")
        elif "track_3" in node_id or "sub_3" in node_id:
            self.active_agent_identity.set("CH_COMM_LINK ➔ ASC-CORE-UX   // SOVEREIGN SHELL ARCHITECT [Agent #002]")
        else:
            self.active_agent_identity.set("CH_COMM_LINK ➔ ASC-MGMT-PA   // ADMINISTRATIVE SHADOW [Agent #003]")

    def stream_telemetry_event(self, log_message: str):
        """Appends timestamped operations data natively to the visual terminal stream."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_display.insert(tk.END, f"[{timestamp}] {log_message}\n")
        self.log_display.see(tk.END)

    def handle_command_submission(self, event):
        """Intercepts keyboard inputs to process strings directly inside the running layout shell."""
        raw_input = self.command_entry.get().strip()
        if not raw_input:
            return
        
        self.stream_telemetry_event(f"[USER_EXEC] {raw_input}")
        self.command_entry.delete(0, tk.END)
        
        lower_input = raw_input.lower()
        if lower_input in ["help", "-h"]:
            self.stream_telemetry_event("[SHELL] Authorised Commands: help | clear | sync | status | redraw")
        elif lower_input == "clear":
            self.log_display.delete("1.0", tk.END)
            self.stream_telemetry_event("[SHELL] Log viewport buffer successfully flushed.")
        elif lower_input == "sync":
            self.stream_telemetry_event("[GUARD] Running validation sweep across path anchors...")
            self.generate_geometric_vault_clusters()
            self.stream_telemetry_event("[CLUSTER] Graph cluster matrix synchronised to local manifest coordinates.")
        elif lower_input == "redraw":
            self.generate_geometric_vault_clusters()
            self.stream_telemetry_event("[CLUSTER] Forcing visual canvas cluster redraw sweep... Complete.")
        elif lower_input == "status":
            threads = self.thread_limit_allocation.get()
            daemon_state = "ACTIVE" if self.background_scraping_active.get() else "PAUSED"
            self.stream_telemetry_event(f"[STATUS] Daemons: {daemon_state} // Worker Ceiling: {threads} active threads.")
        else:
            self.stream_telemetry_event(f"[SHELL] Command registered into stack pipeline text-buffer: '{raw_input}'")

    def handle_session_navigation_click(self, event):
        """Intercepts node selections to track and isolate multi-perspective session coordinates."""
        selected_node = self.session_tree.focus()
        item_text = self.session_tree.item(selected_node, "text")
        
        # Dynamically change the top identity bar based on selection coordinates
        self.select_departmental_context(selected_node)
        
        if "[" in item_text or "➔" in item_text:
            self.stream_telemetry_event(f"[NAVIGATOR] Context switched ➔ {item_text.strip()}")

    def handle_control_toggle_event(self):
        """Captures operator toggles to instantly suspend or resume background scraping routines."""
        current_state = "RUNNING" if self.background_scraping_active.get() else "SUSPENDED"
        self.stream_telemetry_event(f"[USER_UX] Background processing loops dynamically set to: {current_state}")
        if current_state == "SUSPENDED":
            self.status_indicator.configure(text="○ DAEMONS PAUSED", fg=self.accent_amber)
        else:
            self.status_indicator.configure(text="● ALL REPOS SYNCED", fg=self.alert_green)

    def handle_thread_throttling_event(self):
        """Monitors real-time spinbox adjustments to clamp active CPU allocation boundaries."""
        target_threads = self.thread_limit_allocation.get()
        if target_threads > 6:
            self.stream_telemetry_event(f"[ALERT] Core Thread allocation requested: {target_threads} -> EXCEEDS ASIO SAFE WINDOW COUPLING LIMIT.")
            self.status_indicator.configure(text="⚠ AUDIO OVERHEAD RISK", fg="#FF3333")
        else:
            self.stream_telemetry_event(f"[USER_UX] Background thread ceiling restricted to: {target_threads} Max Worker Loops.")
            if self.background_scraping_active.get():
                self.status_indicator.configure(text="● ALL REPOS SYNCED", fg=self.alert_green)

if __name__ == "__main__":
    app_root = tk.Tk()
    shell_engine = SovereignShellUI(app_root)
# --- Target Modification Zone: Lines 318-322 ---
print("[DEBUG 01] Pre-flight check complete. Attempting to launch Tkinter event loop...")

try:
    app_root.mainloop()
except KeyboardInterrupt:
    print("\n[DEBUG 03] Manual exit triggered via KeyboardInterrupt at terminal.")
finally:
    print("[DEBUG 02] Tkinter event loop has officially terminated.")