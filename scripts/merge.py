import sys
import copy
import yaml

def merge_topology(topology1: dict, topology2: dict) -> dict:
  topology = copy.deepcopy(topology1)
  topology['topology']['nodes'].update(topology2['topology']['nodes'])
  topology['topology']['links'].extend(topology2['topology']['links'])
  return topology

def main(input_file_paths: list[str], output_file_path: str, name: str):
  output_topology = {
    'topology': {
      'nodes': {},
      'links': []
    }
  }
  for input_file_path in input_file_paths:
    with open(input_file_path, mode='r', encoding='utf-8') as f:
      topology: dict = yaml.safe_load(f)
      output_topology = merge_topology(topology, output_topology)
  output_topology['name'] = name
  with open(output_file_path, 'w', encoding='utf-8') as f:
    yaml.dump(output_topology, f, sort_keys=False, allow_unicode=True, default_flow_style=False)

if __name__ == "__main__":
  input_file_paths = sys.argv[1:-2]
  output_file_path = sys.argv[-2]
  name = sys.argv[-1]
  main(input_file_paths, output_file_path, name)
