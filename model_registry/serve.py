import netron
from argparse import ArgumentParser

if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument('--model_path', type=str, required=True)
    p.add_argument('--port', type=int, default=17123)
    args = p.parse_args()

    netron.start(None, args.model_path, ('0.0.0.0', args.port), False, False)
