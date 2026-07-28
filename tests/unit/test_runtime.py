import unittest
from packages.core import Engine

from unittest.mock import Mock

class TestRuntime(unittest.TestCase):

    def setUp(self):
        self.agent_registry = Mock()
        self.service_registry = Mock()
        self.engine = Engine(self.agent_registry, self.service_registry)

    def test_request_service(self):
        service_id = 'service1'
        self.engine.request_service(service_id)
        self.service_registry.request_service.assert_called_once_with(service_id)