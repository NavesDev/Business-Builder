"""Data Model Architect skill — produces entity-relationship and schema suggestions."""

from src.utils import load_prompt


class DataModelArchitect:
    """Generates an entity-relationship diagram and database schema for the idea."""

    SKILL_NAME = "data_model_architect"

    def run(self, idea: str) -> str:
        """
        Generate a data model for the given idea.

        Args:
            idea: Plain-text description of the business concept.

        Returns:
            Data model description as a string.
        """
        prompt = load_prompt(self.SKILL_NAME)
        raise NotImplementedError("Skill not yet wired to an LLM provider.")
