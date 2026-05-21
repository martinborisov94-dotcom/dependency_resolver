"""Dependency resolver module for determining package installation order."""
import json
import sys
from pathlib import Path

def load_packages(filename: str = None) -> dict:
    """Load packages from a JSON file and return them as a dictionary.

    Args:
        filename (str or Path, optional): Path to the JSON file. Defaults to
            <project_root>/files/package.json relative to this module.

    Returns:
        dict: A dictionary mapping package names to their list of required dependencies.

    """
    if filename is None:
        filename = Path(__file__).resolve().parent.parent / "files" / "package.json"

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    package_map = {}
    for package in data['packages']:
        package_map[package['name']] = package['requires']

    return package_map

def resolve_dependencies \
    (package_name: str, pkg_map: dict, visited: set, result: list, rec_stack: set):
    """Recursively resolve dependencies for a package using depth-first search (DFS).

    Performs a post-order DFS traversal so that each dependency is added to the
    result list before the package that depends on it.

    Args:
        package_name (str): The name of the package to resolve.
        pkg_map (dict): A dictionary mapping package names to their dependencies.
        visited (set): Set of already-resolved package names (avoids duplicates).
        result (list): Ordered list of packages accumulated during traversal.
        rec_stack (set): Set of packages currently on the recursion stack (cycle detection).

    Raises:
        ValueError: If a circular dependency is detected.
    """
    if package_name in rec_stack:
        raise ValueError(f"Circular dependency detected: {package_name}")

    if package_name in visited:
        return

    rec_stack.add(package_name)

    dependencies = pkg_map[package_name]
    for dependency in reversed(dependencies):
        resolve_dependencies(dependency, pkg_map, visited, result, rec_stack)

    rec_stack.remove(package_name)
    visited.add(package_name)
    result.append(package_name)

def get_installation_order(target_package: str, pkg_map: dict) -> list:
    """Return the installation order of all dependencies for a given package.

    Args:
        target_package (str): The name of the package to install.
        pkg_map (dict): A dictionary mapping package names to their dependencies.

    Returns:
        list: An ordered list of package names where each dependency appears
            before the package that requires it.
    """
    visited = set()
    result = []
    rec_stack = set()

    resolve_dependencies(target_package, pkg_map, visited, result, rec_stack)
    return result

def main(target: str):
    packages = load_packages()
    return get_installation_order(target, packages)


if __name__ == "__main__":
    target = sys.argv[1]

    try:
        order = main(target)
        print(order)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
