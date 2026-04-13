"""Business Architect skill — decomposes a business idea into logical domains."""

from src.utils import load_prompt


class BusinessArchitect:
    """Analyses the business idea and produces a structured domain map."""

    SKILL_NAME = "business_architect"

    def run(self, idea: str) -> str:
        """
        Generate a business architecture for the given idea.

        Args:
            idea: Plain-text description of the business concept.

        Returns:
            Structured business architecture as a string.
        """
        prompt = load_prompt(self.SKILL_NAME)
        raise NotImplementedError("Skill not yet wired to an LLM provider.")
