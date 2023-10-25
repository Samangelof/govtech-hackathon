from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured
import os


load_dotenv()

def get_env_variable(env_variable: str) -> str:
	try:
		return os.getenv(env_variable)
	except KeyError:
		raise ImproperlyConfigured(f'Set {env_variable} enviroment variable')