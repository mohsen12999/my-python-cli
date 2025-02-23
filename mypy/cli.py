"""This module provides the MyPy CLI."""

from typing import Optional

import os
import typer
import questionary

from mypy import __app_name__, __version__

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

@app.command()
def new(project_type: str = typer.Argument(None, help="choose a project type")) -> None:
    """choose a project type"""

    options = {
        "Basic": "mkdir my_project && cd my_project && touch main.py && echo 'print(\"Hello, World!\")' > main.py",
        "Django": "pip install django && django-admin startproject my_project",
        "Flask": "pip install Flask && mkdir my_project && cd my_project && touch app.py && echo 'from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef hello_world():\n    return 'Hello, World!'\nif __name__ == '__main__':\n    app.run(debug=True)'\nif __name__ == '__main__':\n    app.run(debug=True)' > app.py",
        "FastAPI": "pip install fastapi && mkdir my_project && cd my_project && touch main.py && echo 'from fastapi import FastAPI\napp = FastAPI()\n@app.get('/')\ndef read_root():\n    return {'message': 'Hello, World!'}\nif __name__ == '__main__':\n    uvicorn.run(app, host='0.0.0.0', port=8000)' > main.py",
        "Scrapy": "pip install scrapy && mkdir my_project && cd my_project && touch main.py && echo 'import scrapy\nclass MySpider(scrapy.Spider):\n    name = 'my_spider'\n    start_urls = ['https://example.com']\n    def parse(self, response):\n        print(response.text)' > main.py",
        "Data Science": "mkdir my_project && cd my_project && pip install jupyter pandas numpy matplotlib seaborn && touch main.py && echo 'import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nimport jupyter\nprint(\"Hello, World!\")' > main.py",
        "Machine Learning": "mkdir my_project && cd my_project && pip install numpy pandas scikit-learn tensorflow torch && touch main.py && echo 'import numpy as np\nimport pandas as pd\nimport scikit-learn\nimport tensorflow as tf\nimport torch\nprint(\"Hello, World!\")' > main.py",
    }

    if project_type == None or project_type not in options:

        project_type = questionary.select(
            "What do you want to do?",
            choices=options.keys()).ask()

    project_name = questionary.text("What's your Project name? [my_project]", default="my_project").ask()

    if project_name == None:
        project_name = "my_project"

    our_command = options[project_type].replace("my_project", project_name)

    os.system(our_command)

