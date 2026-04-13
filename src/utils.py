"""Shared utility functions for Business Builder."""


def load_prompt(skill_name: str) -> str:
    """
    Load the prompt template for a given skill from the /prompts directory.

    Args:
        skill_name: The file stem of the prompt (e.g. 'business_architect').

    Returns:
        The prompt template as a string.
    """
    from pathlib import Path

    prompt_path = Path(__file__).parent.parent / "prompts" / f"{skill_name}.md"
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt template not found: {prompt_path}")
    return prompt_path.read_text(encoding="utf-8")
