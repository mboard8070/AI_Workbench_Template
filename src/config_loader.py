import yaml
from pathlib import Path

def load_config():
    config_path = Path(__file__).parent.parent / "config" / "project.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    print(load_config())
