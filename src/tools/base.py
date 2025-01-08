from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class BaseTool(ABC):
    """Base class for tool integrations"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        
    @abstractmethod
    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the tool with given input"""
        pass

    @abstractmethod
    def get_description(self) -> Dict[str, Any]:
        """Get tool description and metadata"""
        pass
