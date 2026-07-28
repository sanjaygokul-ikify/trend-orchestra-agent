import time

from dataclasses import dataclass
from typing import Dict

class Metrics:
    def __init__(self):
        self.metrics = {}

    def record(self, name: str, duration: float):
        self.metrics[name] = duration

    def get_metrics(self) -> Dict[str, float]:
        return self.metrics