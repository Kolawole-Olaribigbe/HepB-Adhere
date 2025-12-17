from datetime import datetime
from typing import Optional, Dict

class USSDSession:
    def __init__(self, session_id: str, phone_number: str):
        self.session_id = session_id
        self.phone_number = phone_number
        self.start_time = datetime.now()
        self.state = "initialized"
        self.data: Dict[str, Optional[str]] = {}

    def update_state(self, new_state: str):
        self.state = new_state

    def set_data(self, key: str, value: Optional[str]):
        self.data[key] = value

    def get_data(self, key: str) -> Optional[str]:
        return self.data.get(key)

    def is_active(self) -> bool:
        return self.state not in ["completed", "terminated"]

    def terminate(self):
        self.state = "terminated"