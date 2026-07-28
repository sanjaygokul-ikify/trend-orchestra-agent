import argparse
from packages.core import Engine
from packages.services import Orchestrator

parser = argparse.ArgumentParser(description='Orchestra Agent CLI')

parser.add_argument('--agent-id', type=str, help='Agent ID')

parser.add_argument('--service-id', type=str, help='Service ID')

args = parser.parse_args()

engine = Engine(agent_registry={}, service_registry={})

orchestrator = Orchestrator(engine)

if args.agent_id:
    orchestrator.register_agent(args.agent_id)

if args.service_id:
    engine.request_service(args.service_id)