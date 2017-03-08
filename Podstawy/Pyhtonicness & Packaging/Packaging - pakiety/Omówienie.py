"""
W Pythonie termin Packaging odnosi się do modułów, które wcześniej
zostały napisane i moga być zainstalowane i użye przez innych proga-
mistów.

To zawiera uzycie modułów setuptools and distutils.

Pierwszym krokiem w packaging'u jest organizacja istniejących
plików poprawnie. Włóż wszystkie pliki które chcesz włożych
do biblioteki do jednego folderu.
Ten folder idzie do innego zawierającego readme i license jak
i inny istotny plik setup.py
Przykładowa stuktura:
SoloLearn/
        License.txt
        README.txt
        setup.py
        sololearn/
        __init__.py
        sololearn.py
        sololearn2.py

Plik, który musi być umieszczony w folderze,żeby stał się on
pakietem to __init__/[y

Można umieścic tak dużo plików w folderze ile potrzebujesz


Kolejnym krokiem żeby napisać pakiet to utworzenie pliku
setup.py

To zawiera informacje niezbędne do zamontowanie pakietu
co spawia,ze może on być przekazany do PyPI i zainstalowany
przez pip (name,version,etc)

Przykład pliku setup.py

"""


from distutils.core import setup

setup(
    name = "SoloLearn",
    version = '0.1dev',
    packages =['sololearn',],
    license = 'MIT',
    long_description = open('README.txt').read(),
)

"""
Po utworzeniu pliku setup.py prześlij go do PyPI, albo
użyj wiersza polecenia by stworzyć dystrybucję binarną
(instalator wykonywalny)
By zbudować źródło dystrybucji użyj linii poleceń by
dostać się do folderu zawierającego setup.py i run
komende python setup.py sdist
Run python setup.py bdist albo dla Windowsa python setup.py
bdist_wininst by zbudować dystrybucję binarną
Użyj python setup.py register następnie python setup.py
sdist upload by przekazać pakiet.

Nastepnie zainstaluj pakiet poprzez python setup.py install

Na platformach takich jak Windows or Mac nie ma zainstalowanego
pythona wiec nalezy spakować plik do pliku wykonywalnego (executable -> exe)
By skonwertować skrypt do exe można użyć py2exe,PyInstaller or
cx_Freeze
Dla Mack'ów użyj py2app PyInstaller or cx_Freeze
"""






