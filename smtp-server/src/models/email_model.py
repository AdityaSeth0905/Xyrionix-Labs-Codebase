
from pydantic import BaseModel
from typing import List, Optional

class Email(BaseModel):
    to: str
    subject: str
    body: str
    attachments: Optional[List[str]] = None
