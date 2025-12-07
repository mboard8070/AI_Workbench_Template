from config_loader import load_config

cfg = load_config()
print(f"Starting {cfg['project']['name']} — {cfg['project']['description']}")
