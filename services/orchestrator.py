from packages.core import Engine
from packages.utils import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

class Orchestrator:
    def __init__(self, engine: Engine):
        self.engine = engine

    def register_agent(self, agent_id: str) -> None:
        try:
            self.engine.register_agent(agent_id)
            logger.info(f"Agent {agent_id} registered successfully")
        except Exception as e:
            logger.error(f"Error registering agent {agent_id}: {str(e)}")
            raise EngineError(f"Error registering agent {agent_id}")