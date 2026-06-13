# QmlSortFilterProxyModel

This project is a python PySide2 port of [PyQmlSortFilterProxyModel](https://github.com/dogezen/PyQmlSortFilterProxyModel) based on [SortFilterProxyModel](https://github.com/oKcerG/SortFilterProxyModel).

Please refer to oKcerG's documentation for usage as much of this implementation is based on oKcerG's implementation.

**Note:** The version of the qml exposed `SortFilterProxyModel` is `0.2` to match that of oKcerG's project so that existing .qml code from your projects can be re-used quickly.

## Components not (yet) ported

- `ProxyRoles`
- `QQmlSortFilterProxyModel::componentCompleted` - In PySide2, there is no `Q_INTERFACES` macro enabling a class to inherit from `QSortFilterProxyModel` and `QQmlParserStatus`
- Some of the sorters are not yet ported
- The `delay` functionality is not ported
- Attached properties not ported

## Differences - Container Filters

Because attached properties are not ported, there is a difference in using the `AnyOf` and `AllOf` filters:

### oKcerG's implementation:
```qml
AnyOf {
    RoleFilter {...}
    RegExpFilter {...}
    //...
}
```

### Python implementation:
```qml
AnyOf {
    // need to assign a list of Filter to the filters property
    filters: [
        RoleFilter {...},
        RegExpFilter {...},
        //...
    ]
}
```

## Usage

1. Download/clone the repository
2. Copy `src/qmlsortfilterproxymodel` to your project
3. Import and register the `SortFilterProxyModel` to QML

**main.py:**
```python
import qmlsortfilterproxymodel
# register qml types before QQmlApplicationEngine.load("main.qml") is called
qmlsortfilterproxymodel.registerQmlTypes()
```

4. Instantiate `SortFilterProxyModel` in QML

**SomeFile.qml:**
```qml
import SortFilterProxyModel 0.2

SortFilterProxyModel {
    //...
}
```

## Running the Example

1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install requirements (PySide2):
   ```bash
   pip3 install -r requirements.txt
   ```

3. Run the example project:
   ```bash
   python3 example/main.py
   ```

Once the example window launches, you can use the `TextField` to filter by name.

---

**Stack:** QML (63.8%) • Python (35.3%) • JavaScript (0.9%)
