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
        
    def _create_model_selection(self):
        """Creates the model selection dropdown and Load button."""
        model_frame = ttk.LabelFrame(self._root, text="Model Selection", padding="10")
        model_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(model_frame, text="Select Model:").pack(side=tk.LEFT, padx=5)
        self._model_var = tk.StringVar()
        self._models_list = ["Text-to-Image", "Sentiment Analysis"]
        self._model_combo = ttk.Combobox(
            model_frame,
            textvariable=self._model_var,
            values=self._models_list,
            state="readonly",
            width=30
        )
        self._model_combo.set(self._models_list[0])
        self._model_combo.pack(side=tk.LEFT, padx=5)
        self._model_combo.bind('<<ComboboxSelected>>', self._on_model_selected)
        
        ttk.Button(model_frame, text="Load Model", command=self._load_model).pack(side=tk.LEFT, padx=10)
        
    def _create_input_section(self, parent):
        """Creates the User Input section (Left Column - 30%)."""
        input_frame = ttk.LabelFrame(parent, text="Text Input Prompt", padding="10")
        
        # Only text input is supported in this final version
        self._input_type = tk.StringVar(value="text") 
        
        # ScrolledText area for user input. Decreased height from 15 to 8.
        self._input_text = scrolledtext.ScrolledText(input_frame, height=8, wrap=tk.WORD) 
        self._input_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Action Buttons
        btn_frame = ttk.Frame(input_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        
        # Run Button (Green)
        ttk.Button(btn_frame, text="Run Model", command=self._run_model, 
                   style='G.TButton').pack(side=tk.LEFT, padx=5, expand=True)
        
        # Clear Button (Red)
        ttk.Button(btn_frame, text="Clear All", command=self._clear_all, 
                   style='R.TButton').pack(side=tk.LEFT, padx=5, expand=True)
        
        return input_frame
        
    def _create_output_section(self, parent):
        """Creates the Output section (Right Column - 70%)."""
        output_frame = ttk.LabelFrame(parent, text="Model Output", padding="10")
        
        self._output_container = ttk.Frame(output_frame)
        self._output_container.pack(fill=tk.BOTH, expand=True)
        
        # Text output area
        self._output_text = scrolledtext.ScrolledText(self._output_container, height=10, wrap=tk.WORD)
        self._output_text.pack(fill=tk.BOTH, expand=True)
        
        # Image output label (for Text-to-Image results)
        self._output_image_label = tk.Label(self._output_container)
        
        return output_frame
        
 