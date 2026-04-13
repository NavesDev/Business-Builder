"""Shared data models and schema definitions for Business Builder."""

from dataclasses import dataclass, field


@dataclass
class BusinessReport:
    """Aggregated output produced by the full Business Builder pipeline."""

    idea: str
    business_architecture: str = ""
    revenue_model: str = ""
    viability_analysis: str = ""
    infrastructure: str = ""
    api_blueprint: str = ""
    data_model: str = ""
    metadata: dict = field(default_factory=dict)
