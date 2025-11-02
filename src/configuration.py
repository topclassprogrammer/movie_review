import os

import yaml


class Configuration:
    def __init__(self, config_file):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(current_dir, '..', 'config', config_file), 'r', encoding="utf-8") as f:
            self.config = yaml.safe_load(f)