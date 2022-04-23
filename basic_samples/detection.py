import argparse
import boto3
import json

def get_modes():
    return '\n' + \
        '--mode detect_labels or\n' + \
        '--mode detect_faces or\n' + \
        '--mode detect_protective_equipment or\n' + \
        '--mode detect_text\n'

def get_args():

    modes = get_modes()

    parser = argparse.ArgumentParser()
    parser.add_argument('s3_config', help='Path location of S3 JSON config file.')
    parser.add_argument('output_path', help='File path to dump the output detection in JSON.')
    parser.add_argument('--mode', help=f'Use different modes from the following: {modes}')

    args = parser.parse_args()
    return args

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def dump_json(path, json_obj):
    with open(path, 'w') as f:
        json_str = json.dumps(json_obj, indent=4)
        f.write(json_str)

def detect_labels(s3_config):

    client = boto3.client('rekognition')
    response = client.detect_labels(Image=s3_config)

    return response


def execute_mode(s3_config, mode):

    print(f'Current Mode: {mode}')

    client = boto3.client('rekognition')
    if mode == 'detect_labels':
        return client.detect_labels(Image=s3_config)
    elif mode == 'detect_faces':
        return client.detect_faces(Image=s3_config)
    elif mode == 'detect_protective_equipment':
        return client.detect_protective_equipment(Image=s3_config)
    elif mode == 'detect_text':
        return client.detect_text(Image=s3_config)
    else:
        return {
            'Error' : 'Mode is either not supported or invalid.',
            'Valid Modes' : [
                'detect_labels',
                'detect_faces',
                'detect_protective_equipment',
                'detect_text'
            ]
        }

def main():
    args = get_args()
    s3_config = load_json(args.s3_config)

    print('==============================')
    print('S3 Input: ')

    s3_config_str = json.dumps(s3_config, indent=4)
    print(s3_config_str)

    mode = args.mode
    response = execute_mode(s3_config, mode)
    
    print('==============================')
    print('Rekognition Main Response: ')

    response_str = json.dumps(response, indent=4)
    print(response_str)

    dump_json(args.output_path, response)


if __name__ == '__main__':
    main()
