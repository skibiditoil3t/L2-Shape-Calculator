# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")

# Main fucntion
make_statement("maths calculator", "=")

def instruction(instructions):
    make_statement(instructions)