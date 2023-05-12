"""
Checks the ENV_NAME environment variable to determine the environment.

Parameters:
DEVELOPMENT (str): The string representing the development environment.
STAGING (str): The string representing the staging environment. 
PRODUCTION (str): The string representing the production environment.

current_env (str): Gets the ENV_NAME environment variable, defaulting to DEVELOPMENT.

if current_env == DEVELOPMENT:
Prints a message indicating the development environment.

elif current_env == PRODUCTION:  
Prints a message indicating the production environment.

elif current_env == STAGING:
Prints a message indicating the staging environment.

else:  
Prints a message indicating an unknown environment.
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
# Can test using "export ENV_NAME=something_else" in terminal (Mac/Linux)
else:
    print("Unknown environment")
