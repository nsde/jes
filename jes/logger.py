"""Prints messages of any kind (error, warn, info, success, etc.)."""

import colorama

colorama.init(autoreset=True)

colors = {
    'info': colorama.Fore.BLUE,
    'success': colorama.Fore.GREEN,
    'warn': colorama.Fore.YELLOW,
    'error': colorama.Fore.RED,
}

def log(color: str, message: str):
    """
    This will actually print the text. <color> is not a colorcode, but any key of the dictionary <colors>.
    """
    for c in colors:
        if c == color:
            fg = colors[c]
            break

    reset = colorama.Style.RESET_ALL
    mag = colorama.Fore.MAGENTA

    print(f'[{mag}JES{reset}] {fg}{message}')

def info(message: str):
    log('info', message)

def success(message: str):
    log('success', message)

def warn(message: str):
    log('warn', message)

def error(message: str):
    log('error', message)
