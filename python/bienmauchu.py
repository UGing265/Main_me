from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.RESET_ALL)
print('back to normal now')
"""-----------------------------------------------------------------------------"""
import sys
from colorama import Fore, Back, Style
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
print(Fore.RED + 'some red text', file=stream)
print(Back.GREEN + 'and with a green background', file=stream)
print(Style.RESET_ALL, file=stream)
print('back to normal now', file=stream)
"""----------------------------------------------------------------------------"""


import sys
from colorama import Fore, Back, Style
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

colors = {
    'highlight_background': Back.BLUE,
    'default_color': Fore.WHITE,
    'issue_color': Fore.WHITE,
    'warning_color': Fore.CYAN,
    'major_color': Fore.YELLOW,
    'cirtical_color': Fore.MAGENTA,
    'fatal_color': Fore.RED,
    'reset': Style.RESET_ALL,
    'highlight_number_background': Back.GREEN
}
node_template = "System Info node {highlight_number_background} {node_number}{reset}"\
                "# Count: {issue_count} issues"\
                "=> {warning_color}{warning_count} warning;{reset}"\
                "{major_color}{major_count} marjor;{reset}"\
                "{cirtical_color}{cirtical_count} critical;{reset}"\
                "{fatal_count} fatal;"
info_1 = {
    'node_number': 1,
    'issue_count': 300,
    'warning_count': 40,
    'major_count': 2,
    'cirtical_count': 8,
    'fatal_count': 0     
}
info_1.update(colors)
data_line_1 = node_template.format(**info_1)
print(data_line_1, file=stream)