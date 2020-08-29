import sys
import argparse

# from IPython import embed
from time import sleep
from os import path


from helpers.api import Api
from helpers.local_callback import LocalCallback
from helpers.functions import print_version, print_api_key_does_not_exists, welcome_back, forward_log

print_version()

parser = argparse.ArgumentParser(description='EasyHooks 1.0')
parser.add_argument('--host', type=str, help='Local host to forward income webooks', default='http://localhost:3000')

class Agent:
    def __init__(self, host=""):
        self.host = host
        api_key = self.load_credentials()
        self.api = Api(api_key)
        self.auth(api_key)

        self.local_callback = LocalCallback()

    def load_credentials(self):
        user_home = path.expanduser('~')
        file_path = f'{user_home}/.easyhooks'

        if not path.exists(file_path):
            print_api_key_does_not_exists()
            sys.exit()

        api_key = None

        with open(file_path) as arq:
            api_key = arq.readline().strip()

        return api_key

    def auth(self, api_key):
        try:
            profile = self.api.profile()
        except:
            print_api_key_does_not_exists()
            sys.exit()

        welcome_back(profile, self.host)

    def run(self):
        while True:
            hooks = self.api.hooks()

            for hook in hooks:
                result = self.local_callback.call(
                    hook['method'],
                    self.host,
                    data=hook['payload'],
                    headers={}
                )

                forward_log(result, self.host)
                sleep(0.1)

            sleep(2)


if __name__ == '__main__':
    args = parser.parse_args()
    agent = Agent(args.host)
    agent.run()
