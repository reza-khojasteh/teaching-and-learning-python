"""
Checks the ENV_NAME environment variable to determine the environment.
current_env (a str) gets the ENV_NAME environment variable, defaulting to DEVELOPMENT.
You can test this program using "export ENV_NAME=something_else" in terminal (Mac/Linux.)
"""

import os

DEVELOPMENT = "development"
STAGING = "staging"
PRODUCTION = "production"

current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
else:
    print("Unknown environment")
