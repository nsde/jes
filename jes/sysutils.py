import os, sys

class HidePrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
        print('JES tries to disable the output. Apparently, it doesn\'t work. So please just ignore the following:')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('JES tried to disable the output. Apparently, it didn\'t work. So please just ignore output above.')
        sys.stdout.close()
        sys.stdout = self._original_stdout
