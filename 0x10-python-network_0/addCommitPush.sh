#!/bin/bash

# Prompt user for commit message
read -p "Enter commit message: " commit_message

# Check if the commit message is not empty
if [ -n "$commit_message" ]; then
    # Perform git add
    git add .

    # Perform git commit
    git commit -m "$commit_message"

    # Perform git push
    git push
else
    echo "Commit message cannot be empty. Aborting commit and push."
fi
