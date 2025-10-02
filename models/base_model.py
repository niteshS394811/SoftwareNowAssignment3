from abc import ABC, abstractmethod

class BaseModel(ABC):
    """Abstract base class for all AI models"""
    
    def __init__(self, model_name, category, description):
        # Encapsulation: Private-like attributes
        self._model_name = model_name
        self._category = category
        self._description = description
        self._is_loaded = False
    
    @abstractmethod
    def load_model(self):
        pass
    
    @abstractmethod
    def predict(self, input_data):
        pass
    
    def get_model_info(self):
        return {
            "Model Name": self._model_name,
            "Category": self._category,
            "Description": self._description,
            "Status": "Loaded" if self._is_loaded else "Not Loaded"
        }
    
    @abstractmethod
    def get_usage_example(self):
        pass