import unittest
from packages.core import Engine
from packages.services import Orchestrator

from unittest.mock import Mock

class TestPipeline(unittest.TestCase):

    def setUp(self):
        self.agent_registry = Mock()
        self.service_registry = Mock()
        self.engine = Engine(self.agent_registry, self.service_registry)
        self.orchestrator = Orchestrator(self.engine)

    def test_register_agent(self):
        agent_id = 'agent1'
        self.orchestrator.register_agent(agent_id)
        self.agent_registry.register_agent.assert_called_once_with(agent_id)

    def test_orchestrate(self):
        agent_id = 'agent1'
        service_id = 'service1'
        self.orchestrator.register_agent(agent_id)
        self.engine.execute(agent_id, service_id)
        self.service_registry.request_service.assert_called_once_with(service_id)

if __name__ == '__main__':
    unittest.main()