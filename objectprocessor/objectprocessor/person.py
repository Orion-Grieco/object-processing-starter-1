"""Represent a person using an object-oriented approach."""

from typing import List

from objectprocessor import constants

# TODO: define the index locations for the person
person_index = None

# TODO: define the names of the attributes for the person
person_attributes = None

# ruff: noqa: PLR0913


class Person:
    """Define a Person class."""

    def __init__(
        self, name: str, country: str, phone_number: str, job: str, email: str
    ) -> None:
        self.name = name
        self.country = country
        self.phone_number = phone_number
        self.job = job
        self.email = email

    def __repr__(self) -> str:
        # TODO: return a textual representation of a person
        # TODO: see the output inside of the README.md file
        return ""

    def create_list(self) -> List[str]:
        # TODO: create a list of strings representing a person
        # where the locations of the index go in the order
        # for which the attributes are defined in the constructor
        details = []
        return details
