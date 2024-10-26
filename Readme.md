This project contains cipher algorithms such as vigenere, des, aes

# Running the project

Linux:

```
virtualenv venv

source /venv/bin/activate

pip install PySide6 pycryptodome

python .\main.py
```

Windows:

```
python -m venv .\venv

venv\Scripts\Activate.ps1

pip install PySide6 pycryptodome

python .\main.py
```

# Building UI

After changing ui file, you need to run the following command to generate the ui file

Linux:

```
pyside6-uic ./Ui/mainwindow.ui -o ./Ui/MainWindow.py

pyside6-uic ./Ui/networkDevicesForm.ui -o ./Ui/networkDevicesForm.py

pyside6-rcc ./Ui/resources.qrc -o ./Ui/resources_rc.py
```

Windows:

```
pyside6-uic .\Ui\mainwindow.ui -o .\Ui\MainWindow.py

pyside6-uic .\Ui\networkDevicesForm.ui -o .\Ui\networkDevicesForm.py

pyside6-rcc .\Ui\resources.qrc -o .\Ui\resources_rc.py
```
