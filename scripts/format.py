import sys
import yaml

def main(input_file_path: str, output_file_path: str):
  topology = {}
  with open(input_file_path, mode='r', encoding='utf-8') as f:
    topology: dict = yaml.safe_load(f)
  with open(output_file_path, 'w', encoding='utf-8') as f:
    yaml.dump(topology, f, sort_keys=False, allow_unicode=True, default_flow_style=False)

if __name__ == "__main__":
  input_file_path = sys.argv[1]
  output_file_path = sys.argv[2]
  main(input_file_path, output_file_path)
