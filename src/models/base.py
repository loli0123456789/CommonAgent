from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class BaseModel(ABC):
    """Base class for model integrations"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        
    @abstractmethod
    async def predict(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Make prediction using the model"""
        pass

    @abstractmethod
    async def train(self, training_data: Dict[str, Any]) -> Dict[str, Any]:
        """Train the model"""
        pass

    @abstractmethod
    async def evaluate(self, test_data: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate model performance"""
        pass
