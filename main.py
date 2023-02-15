# Example of how to determine Python version information at run-time
import sys


@staticmethod
def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def read_text_file(filePath: str):
    print(f'reading text file {filePath}')
    count: int = 0
    with open(filePath, mode='r') as f:
        for line in f:
            count += 1
            print(line, end='')

    print(f'Finished reading {count} lines from file {filePath}')


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    read_text_file('textfile.txt')
