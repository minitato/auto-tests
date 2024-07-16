import yaml

def parse_yaml_string(yaml_string):
    return yaml.safe_load(yaml_string)

def write_yaml_file(file_path, data):
    with open(file_path, 'w') as f:
        yaml.safe_dump(data, f)

if __name__ == '__main__':
    yml = """\
    dev: 
        funcional:  1
        password: 'XXXXXX'
    hom:
        funcional:  2
        password: 'XXXXXX'
    """

    config_data = parse_yaml_string(yml)
    write_yaml_file('config.yml', config_data)
