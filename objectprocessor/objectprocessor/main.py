"""Input and process objects about people."""

from pathlib import Path
from typing import List

import typer
from rich.console import Console

from objectprocessor import approach, person, process

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()


def prepare_person_list_for_display(person_list: List[person.Person]) -> str:
    """Process the list of people for display in the console."""
    person_list_text = ""
    # iterate through each of the people in the person_list and
    # add all of their textual details to a string; making sure to
    # preface each entry with a "-" and add a newline
    for current_person in person_list:
        person_list_text += "- " + str(current_person) + "\n"
    # return the list of generated text for each person
    return person_list_text


@cli.command()
def main(
    search_term: str = typer.Option(...),
    attribute: str = typer.Option(...),
    approach: approach.SearchApproach = typer.Option(
        approach.SearchApproach.containment
    ),
    input_file: Path = typer.Option(...),
    output_file: Path = typer.Option(...),
):
    """Input data about a person and then analyze and save it."""
    # display details about the file provided on the command line
    data_text = ""
    # the file was not specified so we cannot continue using program
    if input_file is None:
        console.print("No data file specified!")
        raise typer.Abort()
    # the file was specified and it is valid so we should read and check it
    if input_file.is_file():
        # read in the data from the specified file containing information about people
        console.print(
            f":abacus: Reading in the data from the specified file {input_file!s}"
        )
        data_text = input_file.read_text()
        # transform the data in the CSV file (now in a string) into a list of instances of the Person class
        console.print("")
        console.print(
            ":rocket: Parsing the data file and transforming it into people objects"
        )
        person_list = process.extract_person_data(data_text)
        # search for the people with an attribute that matches the search term
        console.print("")
        console.print(
            f":runner: Searching for the people with an {attribute} that matches the search term '{search_term}'"
        )
        matching_person_list = process.find_matching_people(
            attribute, search_term, person_list, approach
        )
        console.print("")
        # display the details about the matching people to the console
        # make sure to use the prepare_person_list_for_display function for creating a suitable display
        console.print(":sparkles: Here are the matching people:")
        console.print("")
        console.print(prepare_person_list_for_display(matching_person_list))
        # save the details about the matching people to the file system in the specified output directory
        console.print(
            f":sparkles: Saving the matching people to the file {output_file!s}"
        )
        process.write_person_data(str(output_file), matching_person_list)
