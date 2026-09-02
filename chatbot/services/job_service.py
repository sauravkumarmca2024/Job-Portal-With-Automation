import os

import requests


SPRING_BOOT_URL = os.getenv(
    "CHATBOT_SPRING_BOOT_URL",
    "http://localhost:9090"
)


class JobService:

    @staticmethod
    def get_all_jobs():

        try:
            response = requests.get(
                f"{SPRING_BOOT_URL}/api/jobs/getall",
                timeout=10
            )

            response.raise_for_status()

            return response.json()

        except Exception as error:
            print(f"Failed to fetch jobs: {error}")

            return []