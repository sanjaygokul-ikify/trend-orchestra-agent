import unittest
from packages.core import Engine, AgentID, ServiceID

from unittest.mock import Mock

class TestEngine(unittest.TestCase):

    def setUp(self):
        self.agent_registry = Mock()
        self.service_registry = Mock()
        self.engine = Engine(self.agent_registry, self.service_registry)

    def test_register_agent(self):
        agent_id = AgentID('agent1')
        self.engine.register_agent(agent_id)
        self.agent_registry.register_agent.assert_called_once_with(agent_id)

    def test_discover_services(self):
        services = [ServiceID('service1'), ServiceID('service2')]
        self.service_registry.discover_services.return_value = services
        result = self.engine.discover_services()
        self.assertEqual(result, services)

if __name__ == '__main__':
    unittest.main()