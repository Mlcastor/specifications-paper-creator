from crewai_tools import BaseTool
from typing import Any, Dict, Optional
import yaml
import sys

sys.path.append("src")


class ToolModel(BaseTool):
    def __init__(
        self, tool_name: str, description: str = "", config_path: Optional[str] = None
    ):
        """
        Initialize the ToolModel with configurations loaded from a YAML file (if provided).
        :param tool_name: The name of the tool.
        :param description: The description of the tool.
        :param config_path: (Optional) Path to the YAML configuration file.
        """
        if config_path:
            config = self.load_config(config_path, tool_name)
            tool_name = config.get("name", tool_name)
            description = config.get("description", description)

        super().__init__(name=tool_name, description=description)
        self.setup_tool()

    @staticmethod
    def load_config(config_path: str, tool_name: str) -> Dict[str, Any]:
        """
        Load tool configuration from a YAML file.
        :param config_path: Path to the YAML configuration file.
        :param tool_name: The name of the tool in the configuration file.
        :return: A dictionary containing the configuration for the tool.
        """
        with open(config_path, "r") as file:
            config = yaml.safe_load(file).get(tool_name)
            if not config:
                raise ValueError(f"No configuration found for tool '{tool_name}'")
            return config

    def setup_tool(self):
        """
        Additional setup logic for the tool, if needed.
        This method can be overridden in subclasses to perform custom setup.
        """
        pass

    def _run(self, argument: str) -> str:
        """
        The core logic of the tool.
        This method needs to be implemented in subclasses.
        :param argument: The input argument for the tool.
        :return: The result of running the tool.
        """
        raise NotImplementedError(
            "The '_run' method must be implemented in subclasses."
        )
