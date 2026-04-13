"""Viability Analyst skill — assesses market fit and risks."""

from src.utils import load_prompt


class ViabilityAnalyst:
    """Produces a viability score and risk assessment for the business idea."""

    SKILL_NAME = "viability_analyst"

    def run(self, idea: str) -> str:
        """
        Analyse the viability of the given idea.

        Args:
            idea: Plain-text description of the business concept.

        Returns:
            Viability analysis as a string.
        """
        prompt = load_prompt(self.SKILL_NAME)
        raise NotImplementedError("Skill not yet wired to an LLM provider.")
