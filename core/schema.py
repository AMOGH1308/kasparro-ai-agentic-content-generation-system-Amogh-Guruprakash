from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class ProductData(BaseModel):
    name: str
    concentration: str
    skin_type: str
    ingredients: str
    benefits: str
    usage: str
    side_effects: str
    price: str

class FAQItem(BaseModel):
    q: str
    a: str

class FAQData(BaseModel):
    Informational: List[FAQItem]
    Usage: List[FAQItem]
    Safety: List[FAQItem]
    Purchase: List[FAQItem]
    Comparison: List[FAQItem]

class ProductBData(BaseModel):
    name: str
    ingredients: str
    benefits: str
    price: str

class QuestionOutput(BaseModel):
    product: ProductData
    product_b: ProductBData
    questions: FAQData
    critique: Optional[str] = None
    iteration: int = 1

class AuditLog(BaseModel):
    timestamp: str
    sender: str
    receiver: str
    payload_type: str
    payload: Dict[str, Any]
