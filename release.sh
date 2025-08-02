#!/bin/bash

# Clean dist folder
rm -rf dist && mkdir dist


# Update version in setup.py

SETUP_FILE="setup.py"
current_version=$(grep -o 'version="[0-9]\+\.[0-9]\+\.[0-9]\+"' "$SETUP_FILE" | sed 's/version="//;s/"//')

if [[ -z "$current_version" ]]; then
    echo "Error: Could not find version in $SETUP_FILE"
    echo "Expected format: version=\"x.y.z\""
    exit 1
fi

echo "Current version: $current_version"

# Split version into parts
IFS='.' read -r major minor patch <<< "$current_version"

# Increment patch version
new_patch=$((patch + 1))
new_version="$major.$minor.$new_patch"

echo "New version: $new_version"

sed -i "s/version=\"$current_version\"/version=\"$new_version\"/g" "$SETUP_FILE"


# Create distribution
python setup.py sdist bdist_wheel


# Publish to PyPi
export TWINE_USERNAME=__token__
export TWINE_PASSWORD="$PYPI_SERVICESTACK"
python -m twine upload --repository pypi dist/*
