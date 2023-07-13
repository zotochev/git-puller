# git-puller
Script that starts in git repository and pulls it every 10 seconds

## Important notes
Script not tested on merge conflicts and will exit with error if conflict appears.

## Installation
```bash
./install.sh
```

## Usage
Go to directory with git repository.
```bash
cd <directory-with-git-repository>
```
Run command

```bash
git-puller "$PWD"
```
note: `$PWD` argument is not mandatory, but is is recomendet since it is gonna be easyer to find this process in `htop` or `ps` lists.  

Or like this:
```bash
git-puller "/path/to/git/repository"
```
