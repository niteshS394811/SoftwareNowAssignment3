import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from PIL import Image, ImageTk
# Import core components (Placeholders for now)
from gui.model_selector import ModelSelector
from models.base_model import BaseModel 
# The following imports will be uncommented by other members
# from models.text_to_image_model import TextToImageModel
# from models.sentiment_model import SentimentModel 

class AIModelGUI:
    def __init__(self, root):
        self._root = root
        self._setup_window()
        self._model_selector = ModelSelector()
        # OOP Encapsulation: Use private-like attributes
        self._current_model: BaseModel = None 
        self._uploaded_file = None
        
        self._create_widgets()
        
    def _setup_window(self):
        self._root.title("HIT137 Assignment 3 - AI Model GUI")
        self._root.geometry("1100x750") 
        self._root.resizable(True, True)
        
        # Define custom styles for colored buttons (Aesthetics Requirement)
        style = ttk.Style()
        style.theme_use('clam')
        # Green for Run
        style.configure('G.TButton', background='#4CAF50', foreground='black', font=('Arial', 10, 'bold')) 
        style.map('G.TButton', background=[('active', '#66BB6A')])
        # Red for Clear
        style.configure('R.TButton', background='#F44336', foreground='white', font=('Arial', 10, 'bold'))  
        style.map('R.TButton', background=[('active', '#E57373')])
        
    def _create_widgets(self):
        self._create_menu()
        self._create_model_selection()
        
        # 1. Main container for Input (Left) and Output (Right)
        main_content = ttk.PanedWindow(self._root, orient=tk.HORIZONTAL)
        main_content.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 2. Left side: User Input (30% width)
        self._input_frame = self._create_input_section(main_content)
        main_content.add(self._input_frame, weight=30) 
        
        # 3. Right side: Output (70% width)
        self._output_frame = self._create_output_section(main_content)
        main_content.add(self._output_frame, weight=70) 
        
        # FIX: Ensure 30/70 split is applied immediately (330px out of 1100px)
        self._root.update_idletasks()
        main_content.sashpos(0, 330)
        
        # 4. Bottom section: Model Information
        self._create_info_section()
        self._on_model_selected()
        
    def _create_menu(self):
        menubar = tk.Menu(self._root)
        self._root.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self._root.quit)
        
    # --- PLACEHOLDERS (To be filled by Members 2, 3, and 4) ---
    def _create_model_selection(self): pass
    def _create_input_section(self, parent): pass
    def _create_output_section(self, parent): pass
    def _create_info_section(self): pass
    def _on_model_selected(self, event=None): pass
    def _load_model(self): pass
    def _run_model(self): pass
    def _get_input_data(self): pass
    def _display_result(self, result): pass
    def _update_info_display(self): pass
    def _clear_all(self): pass
