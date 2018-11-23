#!/usr/bin/env python3

# For every directory, recursive:
# * If .git does not exist, continue.
# * If .git does exist, we found something to track in repos.csv.
#     * Determine local path (example: github/username)
#     * If this already exists in repos.csv, do nothing
#     * Else, append local path and origin remote to repos.csv. Use `git remote` or scan .git/config to find out where.

# Using recursion:
# * Base case: Either the dir name is .git, or there are no subdirectories. Return.
# * Otherwise: 
#     * Check if .git in subdirectories. If so, append line for this dir to repos.csv
#     * For each subdir, call this method
