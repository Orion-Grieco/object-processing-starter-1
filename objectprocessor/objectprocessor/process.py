"""Extract and save the data about the person from the CSV file."""

from typing import List

from rapidfuzz import fuzz

from objectprocessor import approach, person

FUZZY_MATCH_THRESHOLD = 90

# Sample of the data set:

# Mrs. Natalie Lee,Bolivia,036-126-0340x0094,"Engineer, building services",david82@example.org
# Michael Anderson,Honduras,(627)610-9166,Writer,ryan23@example.org
# Cindy Burns,Dominican Republic,(102)481-3875,"Pharmacist, hospital",rtorres@example.org
# Jason Bailey,Falkland Islands (Malvinas),+1-552-912-2326,Leisure centre manager,daniel51@example.com
# Andrew Johnson,Portugal,733-554-3949,"Engineer, site",michael94@example.com
# Carol Poole,Isle of Man,365.529.7270,Pensions consultant,piercebrenda@example.com

# TODO: look at the entire data set inside of the inputs/people.txt


def extract_person_data(data: str) -> List[person.Person]:
    """Extract a specified data column from the provided textual contents."""
    data_list = []
    for line in csv.reader(
        data.splitlines(),  # type: ignore
        quotechar='"',
        delimiter=",",
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True,
    ):
        current_name = line[person.person_index.Name]  # line[0]
        current_country = line[person.person_index.Country]  # line[1]
        current_phone_number = line[person.person_index.Phone_Number]  # line[2]
        current_job = line[person.person_index.Job]  # line[3]
        current_email = line[person.person_index.Email]  # line[4]
        new_person = person.Person(
            current_name,
            current_country,
            current_phone_number,
            current_job,
            current_email,
        )
        data_list.append(new_person)
    return data_list


def write_person_data(file_name: str, person_data: List[person.Person]) -> None:  # type: ignore
    """Write the person data stored in a list to the specified file."""
    converted_person_data = []
    for client in person_data:
        converted_list = [
            client.name,
            client.country,
            client.phone_number,
            client.job,
            client.email,
        ]
        converted_person_data.append(converted_list)
    with open(file_name, "w+", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerows(converted_person_data)

def find_matching_people(
    attribute: str, match: str, person_data: List[person.Person]
) -> List[person.Person]:
    """Find people who have matching data for a specified attribute."""
    matching_people_list = []
    for people in person_data:
        # print(is_matching_person(attribute, match, people))
        # print(attribute, match, person_data)
        if is_matching_person(attribute, match, people) is True:
            matching_people_list.append(people)
    return matching_people_list


def is_matching_person(
    attribute: str, match: str, search_person: person.Person
) -> bool:
    """Determine if the person's specified attribute contains the search term in match."""
    if attribute == "name":
        if match in search_person.name:
            return True
    elif attribute == "country":
        if match in search_person.country:
            return True
    elif attribute == "phone_number":
        if match in search_person.phone_number:
            return True
    elif attribute == "job":
        if match in search_person.job:
            return True
    elif attribute == "email":
        if match in search_person.email:
            return True
    return False


def is_matching_person_containment(
    attribute: str,
    match: str,
    search_person: person.Person,
) -> bool:
    """Use containment to determine if the person's specified attribute contains the search term in match."""
    # TODO: determine which attribute was provided and then
    # use the containment checking approach to determine
    # if there is an appropriate match
    return False


def is_matching_person_equality(
    attribute: str,
    match: str,
    search_person: person.Person,
) -> bool:
    """Use equality to determine if the person's specified attribute contains the search term in match."""
    # TODO: determine which attribute was provided and then
    # use the containment checking approach to determine
    # if there is an appropriate match
    return False


def is_matching_person_fuzzy(
    attribute: str,
    match: str,
    search_person: person.Person,
    find_approach: approach.SearchApproach,
) -> bool:
    """Use equality to determine if the person's specified attribute contains the search term in match."""
    # TODO: use getattr to build up a function call based on the string that is stored
    # in the find_approach variable; make sure to call one of the functions
    # provided by the rapidfuzz library that will return a floating-point value
    # Reference: https://github.com/rapidfuzz/RapidFuzz
    # Reference: https://rapidfuzz.github.io/RapidFuzz/
    rapid_fuzz_function = getattr(fuzz, f"{find_approach}")
    # TODO: determine which attribute was provided and then
    # use the containment checking approach to determine
    # if there is an appropriate match
    return False
