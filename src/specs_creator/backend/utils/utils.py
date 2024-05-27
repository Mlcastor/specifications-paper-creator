import json
import logging
from logging.handlers import RotatingFileHandler
from typing import Union, List, Tuple, Dict

from langchain_core.agents import AgentFinish
from langchain.schema import AgentFinish

# Setup logging
log_directory = "./src/specs_creator/backend/logs/"
log_filename = "crew_callback_logs.txt"
log_path = log_directory + log_filename

# Create logger
logger = logging.getLogger("AgentLogger")
logger.setLevel(logging.DEBUG)  # Set to DEBUG for more detailed logging

# Create file handler which logs even debug messages
fh = RotatingFileHandler(log_path, maxBytes=10485760, backupCount=5)  # 10MB per file
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

# Create console handler with the same log level
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)

agent_finishes = []
call_number = 0


def print_agent_output(
    agent_output: Union[str, List[Tuple[Dict, str]], AgentFinish],
    agent_name: str = "Generic call",
):
    global call_number
    call_number += 1
    try:
        if isinstance(agent_output, str):
            agent_output = json.loads(agent_output)  # Try to parse the JSON string
    except json.JSONDecodeError:
        pass  # If there's an error, leave agent_output as is

        log_message = f"-{call_number}------------------------------------------\n"

        if isinstance(agent_output, list) and all(
            isinstance(item, tuple) for item in agent_output
        ):
            for action, description in agent_output:
                log_message += (
                    f"Agent Name: {agent_name}\n"
                    f"Tool used: {getattr(action, 'tool', 'Unknown')}\n"
                    f"Tool input: {getattr(action, 'tool_input', 'Unknown')}\n"
                    f"Action log: {getattr(action, 'log', 'Unknown')}\n"
                    f"Description: {description}\n"
                    "--------------------------------------------------\n"
                )

        elif isinstance(agent_output, AgentFinish):
            agent_finishes.append(agent_output)
            output = agent_output.return_values
            log_message += (
                f"Agent Name: {agent_name}\n"
                f"AgentFinish Output: {output['output']}\n"
                "--------------------------------------------------\n"
            )

        else:
            log_message += f"Unknown format of agent_output: {type(agent_output)}\n{agent_output}\n"

        logger.info(log_message)

    except Exception as e:
        logger.error(f"Error in print_agent_output: {str(e)}")
