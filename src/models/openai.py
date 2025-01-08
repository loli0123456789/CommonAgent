from typing import Dict, Any
import openai
from .base import BaseModel

class OpenAIModel(BaseModel):
    """OpenAI model integration"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        openai.api_key = self.config.get("api_key")
        self.model_name = self.config.get("model_name", "gpt-3.5-turbo")
        
    async def predict(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Make prediction using OpenAI model"""
        try:
            response = await openai.ChatCompletion.acreate(
                model=self.model_name,
                messages=input_data.get("messages", []),
                temperature=input_data.get("temperature", 0.7),
                max_tokens=input_data.get("max_tokens", 1000)
            )
            return {
                "success": True,
                "response": response.choices[0].message.content
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    async def train(self, training_data: Dict[str, Any]) -> Dict[str, Any]:
        """Training not supported for OpenAI models"""
        return {
            "success": False,
            "error": "Training not supported for OpenAI models"
        }

    async def evaluate(self, test_data: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluation not supported for OpenAI models"""
        return {
            "success": False,
            "error": "Evaluation not supported for OpenAI models"
        }
