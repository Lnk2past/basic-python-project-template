import yaml


def run(who):
    return yaml.load(f'Hello: {who}', Loader=yaml.FullLoader)
