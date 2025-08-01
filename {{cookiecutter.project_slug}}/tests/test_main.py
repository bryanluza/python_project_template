from pytest import CaptureFixture

from app.main import main


def test_main_function_runs_without_error(capsys: CaptureFixture[str]) -> None:
    """Test that the main function executes without raising an error."""
    main()
    captured = capsys.readouterr()
    assert (
        "Hello from your new project: {{ cookiecutter.project_name }}!" in captured.out
    )
