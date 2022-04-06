

def install_and_import(package):
    import importlib
    def install(package):
        if hasattr(pip, 'main'):
            pip.main(['install', package])
        else:
            pip._internal.main(['install', package])

    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        install(package)
    finally:
        globals()[package] = importlib.import_module(package)


