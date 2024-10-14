# Run

```
Linux:
virtualenv venv

Windows:
python -m venv .\venv
```

```
Linux:
source /venv/bin/activate

Windows:
venv\Scripts\Activate.ps1
```

```
pip install PySide6
```

```
python .\main.py
```

# Building UI

You need to run the following command to generate the ui.py file

`pyside6-uic .\Ui\mainwindow.ui -o .\Ui\MainWindow.py`

`pyside6-rcc resources.qrc -o resources_rc.py`
