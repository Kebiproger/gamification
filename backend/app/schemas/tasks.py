from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    id: int = Field(0, ge=0)
    title: str = Field(..., max_length=100)
    description: str = Field(..., max_length=500)
    completed: bool = Field(False)
    difficulty: Optional[str] = Field(None,max_length=50)
    urgent_task: bool = Field(False)
    created_at: datetime = Field(default_factory=datetime.timezone.now)
    score: int = Field(0, ge=0)
    expected_completion_time: Optional[datetime] = None
    # completed_at : datetime 
    

