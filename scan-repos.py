#!/usr/bin/env python3
import os, subprocess

WKDIR = "./wkdir"
PWD = os.path.abspath(os.path.dirname(__file__))
REPOS = os.path.join(PWD, 'repos.csv')

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

if __name__ == "__main__":
    repos = {} # accessor: remote_url; value: local_path
    # TODO read in repos.csv
    for root,dirs,files in os.walk(WKDIR, topdown=True):
        # If we have found the root of a git repo,
        if '.git' in dirs:
            # Get local_path, which is the path relative to the wkdir directory
            local_path = root.split('wkdir/')[-1]
            # Move to that directory to run git command
            os.chdir(root)
            # grab origin info
            process = subprocess.Popen(['git', 'remote', 'get-url', 'origin'], stdout=subprocess.PIPE)
            output = process.communicate()[0]
            remote_url = output.decode('utf-8').splitlines()[0]
            # Strip off the '.git' ending from the remote URL if it's there
            if remote_url.endswith('.git'):
                remote_url = remote_url[:-4]
            print("Adding repository: (%s, %s)" % (remote_url, local_path) )
            # If it exists and is a git repo, this is a conflict. WARN but don't remove anything
            if remote_url in repos:
                print('WARNING: Duplicate repository found for %s.' % remote_url)
                print('Replacing "%s" with "%s" in repos.csv' % (repos[remote_url][1], local_path))
            # Update the dict
            repos[remote_url] = (remote_url, local_path)
            # Move back to where we started
            os.chdir(PWD)
        # Do NOT traverse any of the .git directories
        [dirs.remove(d) for d in list(dirs) if d in ['.git']]
    # Write out the new repos.csv file
    with open(REPOS, 'w') as f:
        for key,repo in repos.items():
            f.write("%s,%s\n" % (repo[0], repo[1]))
