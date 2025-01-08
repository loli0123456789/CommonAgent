from typing import Dict, Any
import requests
from .base import BaseTool

class WebSearchTool(BaseTool):
    """Web search tool using SerpAPI"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.api_key = self.config.get("api_key")
        self.base_url = "https://serpapi.com/search"
        
    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute web search"""
        try:
            params = {
                "q": input_data.get("query"),
                "api_key": self.api_key,
                "num": input_data.get("num_results", 5)
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            return {
                "success": True,
                "results": response.json().get("organic_results", [])
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def get_description(self) -> Dict[str, Any]:
        """Get tool description"""
        return {
            "name": "web_search",
            "description": "Perform web searches using SerpAPI",
            "parameters": {
                "query": {
                    "type": "string",
                    "description": "Search query"
                },
                "num_results": {
                    "type": "integer",
                    "description": "Number of results to return",
                    "default": 5
                }
            }
        }
