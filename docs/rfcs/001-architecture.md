# Architecture

## Overview
Orchestra Agent uses a microservices architecture to enable scalability, flexibility, and maintainability.

## Components
1. **Agent Registry**: Maintains a list of available agents.
2. **Service Registry**: Provides a list of available services.
3. **Execution Engine**: Responsible for executing agent requests and returning results.

## Interactions
1. **Agent Registration**: Agents register themselves with the agent registry.
2. **Service Discovery**: The service registry provides a list of available services, which agents can discover and request.
3. **Execution**: The execution engine executes agent requests and returns results.