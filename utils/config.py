import yaml

def load_config(config_file_path):
    with open(config_file_path, 'r') as config_file:
        return yaml.safe_load(config_file)