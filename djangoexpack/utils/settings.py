import os
from configparser import ConfigParser
from pyhiera import Hiera


def get_project_name(base_dir):

    def from_environ():
        return os.environ.get('PROJECT')

    def from_dotenv():
        try:
            with open(os.path.join(base_dir, '.env')) as fp:
                dotenv = ConfigParser(default_section='common')
                dotenv.read_string("[common]\n" + fp.read())
                return dotenv['common'].get('COMPOSE_PROJECT_NAME')
        except FileNotFoundError:
            return None

    return from_environ() or from_dotenv() or os.path.basename(base_dir)

    
def load_settings_from_config(hiera_configs, **context):
    for confpath in hiera_configs if isinstance(hiera_configs, (list, tuple)) else (hiera_configs,):
        if not os.path.exists(confpath):
            continue
        # print("# config:", confpath)
        hiera = Hiera.load_data(confpath, context=context)
        hiera_data = hiera.flatten()
        return hiera_data

    print("# WARNING -- no config file found.")
    return {}
