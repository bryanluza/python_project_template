from pydantic_settings import BaseSettings, SettingsConfigDict


def main() -> None:
    """Main function of the project."""
    print("Hello from your new project: { PROJECT_NAME}!")
    get_api_key()


# Example of accessing an environment variable
def get_api_key() -> None:
    """Get API key from .env file."""

    class Settings(BaseSettings):
        model_config = SettingsConfigDict(env_file=".env")
        API_KEY: str = "your_api_key"

    settings = Settings()
    print(f"API Key from .env: {settings.API_KEY}")


if __name__ == "__main__":
    main()
