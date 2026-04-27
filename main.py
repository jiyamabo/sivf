import importlib.util
from pathlib import Path

# a python class to load multiple letterGrade modules
class ModuleLoader:
    def __init__(self, base_path="./processing"):
        self.base_path = Path(base_path)
        self.loaded_modules = {}
    
    def load_module(self, filename, alias=None):
        """Load and execute a module by filename"""
        module_path = self.base_path / filename
        
        if not module_path.exists():
            raise FileNotFoundError(f"Module not found: {module_path}")
        
        # Use alias if provided, otherwise use filename without extension
        module_name = alias or module_path.stem
        
        spec = importlib.util.spec_from_file_location(
            module_name, 
            module_path
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        self.loaded_modules[module_name] = module
        return module
    
    def run_all(self, filenames):
        """Load and optionally execute multiple modules"""
        for filename in filenames:
            module = self.load_module(filename)
            print(f"Loaded: {filename}")
            
            # Optionally call main() if it exists
            if hasattr(module, 'main'):
                module.main()
        
        return self.loaded_modules

def main():
    loader = ModuleLoader("./processing")
    
    # load specific modules
    modules = loader.run_all([
        "winter26_bus239b_finals.py"
    ])
    
if __name__ == "__main__":
    main()