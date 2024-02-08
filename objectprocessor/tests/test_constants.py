"""Test suite for the constants module."""

# ruff: noqa: PLR2004

# TODO: This provides an example of a test case for the
# constants module. Please make sure that you implement
# your own test cases for all of the code in the constants module.
#
# TODO: You also need to implement test cases for:
# - The constant enumeration(s) in the approach module.
# - All of the methods associated with the Person class.
# - All of the data input and storage functions in process module.
# - All of the data searching functions in the process module.
# - All additional modules inside of the objectprocessor package.

from objectprocessor import constants


def test_constant_values_for_person_attributes():
    """Ensure that all of the person_attributes constants have a value."""
    assert len(vars(constants.person_attributes).items()) == 5
    for _, value in vars(constants.person_attributes).items():
        assert value is not None
