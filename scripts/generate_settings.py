# Created: 9/12/2019
# Author:  Emiliano Jordan,
# Project: WrapPlotLib
from pathlib import Path

from matplotlib import rcParams


def sanatize_for_attribute(string: str):
    return string.replace('-', '_')


settings_file = Path(__file__).parent.parent \
                / 'wrapplotlib' \
                / 'settings' \
                / '_settings.py'

file_heading = """
from sejings import Sejings as Settings, extract_sejings as extract_settings
from matplotlib import rcParams

__all__ = ['settings', 'extract_settings']

settings = Settings()
"""

values = []
constructors = []
constructors_tracker = []

for key in rcParams:
    key = key.replace('-', '_')

    args = key.split('.')

    builder = 'settings'

    for arg in args[:-1]:

        builder += f'.{arg}'

        constructors.append(f'{builder} = Settings()')

    values.append(f'settings.{key} = rcParams["{key}"]')

with open(settings_file, mode='w') as f:

    f.write(file_heading)

    f.write('\n\n')

    f.write('\n'.join(sorted(set(constructors))))

    f.write('\n\n')

    f.write('\n'.join(sorted(values)))