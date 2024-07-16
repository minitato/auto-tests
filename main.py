import json
import yaml

def read_json_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def write_yaml_file(file_path, data):
    with open(file_path, 'w') as f:
        yaml.safe_dump(data, f)

if __name__ == '__main__':
    yml = """\
    dev: 
        funcional: #devFuncional
        password: '#devPassword'
    hom:
        funcional: #homFuncional
        password: '#homPassword'
    """

    config_dev = read_json_file('config-dev.json')
    funcional_dev = int(config_dev.get('funcional'))
    password_dev = config_dev.get('password', 'N/A')
    print(f"Dev environment: funcional={funcional_dev}, password={password_dev}")

    config_hom = read_json_file('config-hom.json')
    funcional_hom = int(config_hom.get('funcional'))
    password_hom = config_hom.get('password', 'N/A')
    print(f"Hom environment: funcional={funcional_hom}, password={password_hom}")

    yml = yml.replace('#devFuncional', str(funcional_dev))
    yml = yml.replace('#devPassword', password_dev)
    yml = yml.replace('#homFuncional', str(funcional_hom))
    yml = yml.replace('#homPassword', password_hom)
    print(yml)
    write_yaml_file('config.yml', yml)