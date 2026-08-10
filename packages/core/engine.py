import logging
from .types import AgentID, ServiceID
from .exceptions import EngineError

logger = logging.getLogger(__name__)


class Engine:
    def __init__(self, agent_registry, service_registry):
        self.agent_registry = agent_registry
        self.service_registry = service_registry

    def register_agent(self, agent_id: AgentID) -> None:
        try:
            self.agent_registry.register_agent(agent_id)
            logger.info(f"Agent {agent_id} registered successfully")
        except Exception as e:
            logger.error(f"Error registering agent {agent_id}: {str(e)}")
            raise EngineError(f"Error registering agent {agent_id}")

    def discover_services(self) -> list[ServiceID]:
        try:
            services = self.service_registry.discover_services()
            logger.info(f"Discovered services: {services}")
            return services
        except Exception as e:
            logger.error(f"Error discovering services: {str(e)}")
            raise EngineError(f"Error discovering services")

    def request_service(self, service_id: ServiceID) -> None:
        try:
            self.service_registry.request_service(service_id)
            logger.info(f"Requested service {service_id} successfully")
        except Exception as e:
            logger.error(f"Error requesting service {service_id}: {str(e)}")
            raise EngineError(f"Error requesting service {service_id}")

    def execute(self, agent_id: AgentID, service_id: ServiceID) -> None:
        try:
            self.agent_registry.execute_agent(agent_id, service_id)
            logger.info(f"Executed agent {agent_id} with service {service_id} successfully")
        except Exception as e:
            logger.error(f"Error executing agent {agent_id} with service {service_id}: {str(e)}")
            raise EngineError(f"Error executing agent {agent_id} with service {service_id}")

    def get_agent_registry(self) -> dict:
        return self.agent_registry.get_registry()

    def get_service_registry(self) -> dict:
        return self.service_registry.get_registry()