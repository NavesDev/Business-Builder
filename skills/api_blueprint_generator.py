"""API Blueprint Generator skill — produces a high-level API contract."""

from src.utils import load_prompt


class ApiBlueprintGenerator:
    """Generates a REST/GraphQL API contract aligned with the business logic."""

    SKILL_NAME = "api_blueprint_generator"

    def run(self, idea: str) -> str:
        """
        Generate an API blueprint for the given idea.

        Args:
            idea: Plain-text description of the business concept.

        Returns:
            API blueprint as a string.
        """
        prompt = load_prompt(self.SKILL_NAME)
        raise NotImplementedError("Skill not yet wired to an LLM provider.")
