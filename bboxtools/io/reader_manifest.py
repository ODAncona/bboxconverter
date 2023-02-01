import json

def read_manifest(self, path, format='auto') -> None:
        print("Not Implemented")
        with open(path, 'r') as f:
            for line in f:
                json_obj = json.loads(line)
                print(json_obj)
                print("\n")
        pass
