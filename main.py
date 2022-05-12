

import os
import sys
from sortfilterproxymodel import SortFilterProxyModel
from mymodel import MyModel, MyItem
from pathlib import Path

from PySide2.QtCore import QCoreApplication, Qt, QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine,qmlRegisterType

if __name__ == "__main__":
    app = QCoreApplication(sys.argv)
    engine = QQmlApplicationEngine()
    qmlRegisterType(MyModel, 'MyModel', 1, 0, 'MyModel')
    qmlRegisterType(MyItem, 'MyItem', 1, 0, 'MyItem')
    qmlRegisterType(SortFilterProxyModel, 'SortFilterProxyModel', 1, 0, 'SortFilterProxyModel')
    engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
    app.setOrganizationName("somename")
    app.setOrganizationDomain("somename")
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
