# linux-workspace

Welcome to `linux-workspace`, a skeleton for a version-controlled Linux work area that you can bring with you anywhere.

## Getting Started

```
cd
clone git@github.com:stephengrice/linux-workspace.git
```

## Synchronize home files

```
cd ~/linux-workspace
./sync-home.bash
```

## Clone all repositories

```
cd ~/linux-workspace
./clone-repos.py
```

## Scan Repositories

```
./scan-repos.py
```

Automatically detect repositories in `wkdir` directory and create/update `repos.csv` to match this strucutre.

**It is assumed you only want _one_ copy of each repo in wkdir at a time.**

If you have more than one, a warning will be printed when you run the script
