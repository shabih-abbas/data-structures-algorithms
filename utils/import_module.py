import importlib.util

def import_function(file_path, func_name):
    """Dynamically import a function from a given Python file."""
    spec = importlib.util.spec_from_file_location("module.name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, func_name)
