import yaml

import core


docs: list[dict]

input_path = './input_lite.yaml'
with open(input_path, 'r', encoding='utf-8') as f:
    docs = [doc for doc in yaml.full_load_all(f.read()) if doc]

new_docs = []

for doc in docs:
    linear_velocity_x = doc['twist']['linear']['x']
    angular_velocity_z = doc['twist']['angular']['z']
    angle, freq = core.get_wheel_angle_rad_and_frequency(linear_velocity_x, angular_velocity_z)
    new_docs.append({
        'linear': {
            'x': freq,
            'y': 0,
            'z': 0,
        },
        'angular': {
            'x': 0,
            'y': 0,
            'z': angle,
        },
    })

output_string = yaml.dump_all(new_docs, Dumper=yaml.CDumper)

output_path = './output_lite.yaml'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(output_string)
