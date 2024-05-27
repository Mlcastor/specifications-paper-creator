from typing import Optional
import sys

sys.path.append("./src")
from specs_creator.backend.models.tool_model import ToolModel


class InputTool(ToolModel):
    def __init__(self, tool_name: str, config_path: Optional[str] = None):
        """
        Initialize the InputTool with configurations loaded from a YAML file.
        :param tool_name: The name of the tool.
        :param config_path: (Optional) Path to the YAML configuration file.
        """
        super().__init__(
            tool_name=tool_name,
            description="A tool to collect user input. Use this tool to prompt the user for information.",
            config_path=config_path,
        )

    def setup_tool(self):
        """
        Additional setup logic for the InputTool, if needed.
        """
        pass

    def _run(self, prompt: str) -> str:
        """
        Prompts the user with the given message and returns their input.
        :param prompt: The message to display to the user.
        :return: The user's input as a string.
        """
        user_input = input(f"{prompt}\n")
        if not user_input:
            raise ValueError("Empty input. Please provide a valid response.")
        return user_input
