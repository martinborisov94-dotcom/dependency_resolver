
"""Resolve dependency chains from a file-based dependency definition."""

import sys
import json

class DependencyResolver:
    """ TODO """

    @staticmethod
    def get_dependancy_chain(input_letter) -> list[str]:
        """ TODO """
        data = DependencyResolver.load_json_file \
        ("C:\\Appl\\Trainings\\Task 4 ReadFile\\dependency_resolver\\files\\package.json")
        return data

    @staticmethod
    def load_json_file(file_path: str) -> dict:
        """Load and parse a JSON file into a dictionary.

        Args:
            file_path (str): Path to the JSON file to read.

        Returns:
            dict: Parsed JSON content as a dictionary.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

if __name__ == "__main__":
    print("Hello world")
    dependancy_chain =  DependencyResolver.get_dependancy_chain('A') #sys.argv[1:])
    print(dependancy_chain)
