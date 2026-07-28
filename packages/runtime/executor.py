import logging
from ..core.engine import Engine
from ..core.types import AgentID, ServiceID

logger = logging.getLogger(__name__)


class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine

    def execute(self, agent_id: AgentID, service_id: ServiceID) -> None:
        try:
            self.engine.execute(agent_id, service_id)
            logger.info(f"Executed agent {agent_id} with service {service_id} successfully")
        except Exception as e:
            logger.error(f"Error executing agent {agent_id} with service {service_id}: {str(e)}")

    def register_agent(self, agent_id: AgentID) -> None:
        try:
            self.engine.register_agent(agent_id)
            logger.info(f"Registered agent {agent_id} successfully")
        except Exception as e:
            logger.error(f"Error registering agent {agent_id}: {str(e)}")

    def discover_services(self) -> list[ServiceID]:
        try:
            services = self.engine.discover_services()
            logger.info(f"Discovered services: {services}")
            return services
        except Exception as e:
            logger.error(f"Error discovering services: {str(e)}")

    def request_service(self, service_id: ServiceID) -> None:
        try:
            self.engine.request_service(service_id)
            logger.info(f"Requested service {service_id} successfully")
        except Exception as e:
            logger.error(f"Error requesting service {service_id}: {str(e)}")
