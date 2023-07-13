import sys

import logging
import subprocess
from time import sleep
from pathlib import Path


log = logging.getLogger('git-puller')


class GitControl:
    def __init__(self, repository: Path):
        assert self.is_git_repository(repository), f'Not a git repository: `{repository}`'

        self._repository = repository

    def _is_git_repository(self, directory: Path) -> bool:
        if directory is None:
            return False

        try:
            directory.resolve(strict=True)
            self._command('status')
        except Exception as e:
            log.error(f'Path not found: {e.__class__.__name__}: {e}')
            return False
        return True

    def _command(self, command: str) -> subprocess.CompletedProcess:
        p = subprocess.run(['git', '-C', f'{self._repository}', command])
        p.check_returncode()
        return p

    def pull(self):
        self._command('pull')



def main(git_controller: GitControl):

    while True:
        git_controller.pull()
        sleep(5)


if __name__ == '__main__':
    d = None

    if len(sys.argv) == 1:
        d = Path.cwd()
    elif len(sys.argv) == 2:
        d = Path(sys.argv[1])
    else:
        log.error(f'Not expected number of arguments: {len(self.argv)}.')
        sys.exit(1)

    git_controller = GitControl(d)
    main(git_controller)
