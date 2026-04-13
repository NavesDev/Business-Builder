"""Prompt Engineer skill — manages and optimises prompt templates for all skills."""

from pathlib import Path


class PromptEngineer:
    """
    Evaluates and refines the prompt templates used by every other skill
    to ensure consistent, high-quality LLM output.
    """

    SKILL_NAME = "prompt_engineer"
    PROMPTS_DIR = Path(__file__).parent.parent / "prompts"

    def list_prompts(self) -> list[str]:
        """Return the names of all available prompt templates."""
        return [p.stem for p in self.PROMPTS_DIR.glob("*.md")]

    def load(self, skill_name: str) -> str:
        """
        Load a prompt template by skill name.

        Args:
            skill_name: File stem of the prompt (e.g. 'business_architect').

        Returns:
            The prompt template as a string.
        """
        path = self.PROMPTS_DIR / f"{skill_name}.md"
        if not path.exists():
            raise FileNotFoundError(f"Prompt not found: {path}")
        return path.read_text(encoding="utf-8")

    def save(self, skill_name: str, content: str) -> None:
        """
        Persist an updated prompt template.

        Args:
            skill_name: File stem of the prompt to save.
            content: New prompt content.
        """
        path = self.PROMPTS_DIR / f"{skill_name}.md"
        path.write_text(content, encoding="utf-8")
