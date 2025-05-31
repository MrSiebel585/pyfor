#!/bin/bash

# Function to recursively dry run .py scripts
function dry_run_py_scripts() {
    local search_dir="$1"
    echo "Dry run Python scripts in: $search_dir"

    # Find all .py files and run them with the -n (dry-run) option
    find "$search_dir" -type f -name "*.py" -exec python -n {} \;
}

# Function to recursively install supporting pip modules
function install_supporting_pip_modules() {
    local search_dir="$1"
    echo "Installing supporting pip modules in: $search_dir"

    # Find all requirements.txt files and install their contents
    while IFS= read -r -d '' requirements_file; do
        pip install -r "$requirements_file"
    done < <(find "$search_dir" -type f -name "requirements.txt" -print0)
}

# Main function
function main() {
    # Check if Python is installed
    if ! command -v python &> /dev/null; then
        echo "Python is not installed. Aborting."
        exit 1
    fi

    # Dry run .py scripts
    dry_run_py_scripts "."

    # Install supporting pip modules
    install_supporting_pip_modules "."
}

# Call the main function
main
