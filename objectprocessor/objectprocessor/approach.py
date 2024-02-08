"""Configuration of the benchmarking tool with an approach."""

from enum import Enum


class SearchApproach(str, Enum):
    """Define the name for the approach for searching for a person."""

    containment = "containment"
    equality = "equality"
    ratio = "ratio"
    partial_ratio = "partial_ratio"
    token_sort_ratio = "token_sort_ratio"
    token_set_ratio = "token_set_ratio"
    weighted_ratio = "weighted_ratio"
    quick_ratio = "quick_ratio"

    def __str__(self):
        """Define a default string representation."""
        return self.value
