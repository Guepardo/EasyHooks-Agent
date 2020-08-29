# from IPython import embed
from datetime import datetime

def print_version():
    ART = """
    _____                _   _             _          __   _____
    |  ___|              | | | |           | |        /  | |  _  |
    | |__  __ _ ___ _   _| |_| | ___   ___ | | _____  `| | | |/' |
    |  __|/ _` / __| | | |  _  |/ _ \ / _ \| |/ / __|  | | |  /| |
    | |__| (_| \__ \ |_| | | | | (_) | (_) |   <\__ \ _| |_\ |_/ /
    \____/\__,_|___/\__, \_| |_/\___/ \___/|_|\_\___/ \___(_)___/
                    __/ |
                    |___/
    """

    print(ART)


def print_api_key_does_not_exists():
    print("""
      Invalid api key

      Go to easyhook.tk and get one. After that, do this:

      echo "my-api-key" > ~/.easyhooks
    """)


def welcome_back(profile, local_url):
    print(f"""
      Authenticated as {profile['name']}
      Forwarding activated to {local_url}
    """)


def forward_log(forward_result, context):
    print(
        f"[{datetime.now()}]--> { 'SUCCESS' if forward_result['ok'] else 'FAILED' } - {forward_result['method']} --> {context}")
