#-----------------------------------------------------------------------------
# Copyright (c) 2015-2020, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

# Hook for textdistance: https://pypi.org/project/textdistance/4.1.3/

from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = collect_all('textdistance')
