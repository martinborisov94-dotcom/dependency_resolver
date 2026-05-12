# dependency_resolver
Implement a dependency resolver that reads package definitions from package.json and prints the installation order for a requested package. Each package is represented by a single-letter string (always valid input).

## Installation

1. To install venv -> python -m venv .venv
2. Create requirements.txt for the dependencies -> echo . > requirements.txt
or pip freeze > requirements.txt
3. Add Pylint to requirements.txt
4. Add coverage to requirements.txt

## Usage

1. To activate .venv -> .venv\Scripts\activate
2. To deactivate .venv -> deactivate
3. To install all packages from requirements.txt, run: python -m pip install -r requirements.txt
4. To run module with pylint-> pylint .\src\string_tasks.py
5. Run coverage -> coverage run --source=src --omit="*/init.py" -m unittest tests.test_my_math
6. Generate html report -> coverage html
7. To run pytest -> python -m pytest -v

# ------------------------
Requirements

Behavior

Given a package name, print the installation order as a list where dependencies appear before dependents.
Preserve correct order for nested dependencies and avoid duplicates.
Testing (TDD)

Practice Test Driven Development: before writing any implementation code, create at least 3 tests.
Use an appropriate test framework of your choice (e.g., pytest, unittest).
Tests must cover normal cases and edge cases.
Acceptance criteria

A working script that prints the installation order for the requested package.
Full testing including edge cases.
Test coverage report showing 100% coverage.
Code passes pylint with a minimum quality score of 9.75.
Documentation describing the algorithm used.
Code must follow SOLID principles, with special attention to:
Single Responsibility Principle
KISS ("Keep It Simple, Stupid")
Implementation topics practiced

Requirement and specification understanding
File I/O and data formats (reading package.json)
Command-line interaction
Algorithms and data structures (dependency resolution, graph traversal, cycle detection)
Correctness and reliability design
TDD workflow
Modular code organization
Hints (joker hints available if you get stuck)

Consider topological sorting of a dependency graph.
Detect and handle cycles (report error).
Avoid installing a package more than once.
Deliverables

dependency_resolver.py — the script that accepts a one-letter package name and prints the installation order.
package.json — sample data used by tests and demo.
tests/ — at least 3 tests (unit tests) created before implementation, covering nominal and edge cases.
test coverage report — demonstrating 100% coverage.
pylint report — showing quality score >= 9.75.
documentation — README or separate document describing:
The algorithm (e.g., DFS-based topological sort with cycle detection).
Design decisions and how SOLID/KISS were applied.
How to run tests, view coverage, run lint, and execute the script.
Demo — brief demonstration after tests pass.
Suggested test cases (minimum 3, to be written before implementation)

Simple dependency chain

package.json contains: D -> [G], G -> []
Input: "D"
Expect: ["G", "D"]
Multiple dependencies with shared sub-dependencies

package.json contains suitable packages so that installing "A" results in ["E", "G", "D", "F", "B", "A"] (example from prompt).
Input: "A"
Expect: ["E", "G", "D", "F", "B", "A"]
Edge cases

Package with no dependencies
Input: a package X with [] dependencies
Expect: ["X"]
Cycle detection (separate test)
package.json contains cycle A -> B -> A
Expect: an error/exception indicating circular dependency