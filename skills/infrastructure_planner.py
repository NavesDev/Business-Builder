"""Infrastructure Planner skill — designs cloud architecture."""

from src.utils import load_prompt


class InfrastructurePlanner:
    """Generates an infrastructure blueprint suited to the business idea."""

    SKILL_NAME = "infrastructure_planner"

    def run(self, idea: str) -> str:
        """
        Design an infrastructure blueprint for the given idea.

        Args:
            idea: Plain-text description of the business concept.

        Returns:
            Infrastructure blueprint as a string.
        """
        prompt = load_prompt(self.SKILL_NAME)
        raise NotImplementedError("Skill not yet wired to an LLM provider.")
