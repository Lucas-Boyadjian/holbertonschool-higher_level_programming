#!/usr/bin/python3
"""
Generate personalized invitation files from a template and a list of attendees.
"""

import os


def generate_invitations(template, attendees):
    """
    Generates invitation files for each attendee using a template.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): List of dictionaries with attendee data.

    Raises:
        TypeError: If template is not a string or attendees is not a
        list of dicts.

    Behavior:
        - If template is empty, prints an error and does not create files.
        - If attendees is empty, prints an error and does not create files.
        - If a value is missing in an attendee, uses "N/A" in the output.
        - Output files are named output_X.txt (X starts at 1).
    """
    if not isinstance(template, str):
        print("template must be a string")
        return

    if not isinstance(attendees, list):
        print("attendees must be a list of dictionaries")
        return
    
    for x in attendees:
        if not isinstance(x, dict):
            print("attendees must be a list of dictionaries")
            return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, person in enumerate(attendees, 1):
        name = person.get("name") or "N/A"
        event_title = person.get("event_title") or "N/A"
        event_date = person.get("event_date") or "N/A"
        event_location = person.get("event_location") or "N/A"

        invitation = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location
        )

        new_file = "output_{}.txt".format(index)
        try:
            if os.path.exists(new_file):
                print("File {} already exists. Skipping.".format(new_file))
                continue
            with open(new_file, 'w') as file:
                file.write(invitation)
        except Exception as e:
            print("Error writing to {}: {}".format(new_file, e))
