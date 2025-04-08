# CrewAI Project

## Overview
CrewAI is a Python-based framework designed to manage and orchestrate autonomous agents. The project is built around the concept of a "crew" of agents that work together to perform various tasks. It is ideal for applications that require task automation, intelligent scheduling, and coordinated workflows. The architecture is modular, allowing you to easily extend and customize the agents and tasks to fit your needs.

## Features
- **Modular Agent Architecture:** Define multiple agents that each perform specific roles.
- **Task Management:** Manage and schedule tasks dynamically.
- **Utility Tools:** Leverage built-in utilities for common operations and integrations.
- **Environment Configuration:** Use environment variables for flexible, secure configuration.
- **Preconfigured Environment:** Comes with a virtual environment setup for consistent dependency management.

## Installation

### Prerequisites
- **Python 3.8 or higher**
- **pip (Python package installer)**

### Setup Steps
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Srinija1102/crewai.git
   cd crewai-main
   ```
2. **Create a Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. **Configure Environment Variables:**
   Modify the `.env` file with any necessary settings (e.g., API keys, debug flags).
   
2. **Run the Application:**
   Start the main application by running:
   ```sh
   python crew.py
   ```
   This script initializes the agents and tasks, coordinating the workflow as defined in the project.

## Project Structure
- **agents.py:** Contains the logic for creating and managing individual agents. Each agent is designed to perform specific tasks autonomously.
- **crew.py:** Acts as the main entry point and orchestrator, coordinating the interactions between agents.
- **tasks.py:** Defines various tasks that the agents execute. This module handles task scheduling and management.
- **tools.py:** Offers utility functions that support the main functionality of the agents and tasks.
- **.env:** A file for storing environment-specific configuration values, ensuring sensitive data remains separate from the code.
- **requirements.txt:** Lists all the external Python packages required to run the project.
- **venv:** A preconfigured virtual environment directory to ensure consistent dependency management across different setups.

## Environment Configuration
The project uses a `.env` file to manage configuration parameters. This file may include variables such as:
```env
API_KEY=your_api_key_here
DEBUG=True
```
By externalizing configuration, you can maintain security and flexibility, adapting the setup easily for different environments.

## License
This project is licensed under the MIT License. See `LICENSE.txt` for further details.

