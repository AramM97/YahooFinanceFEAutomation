import os
from dotenv import load_dotenv

load_dotenv("infra/.env")

# Print environment variables
print(f"Environment Variables: {dict(os.environ)}")