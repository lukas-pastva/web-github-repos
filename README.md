# web-github-repos

This project is a simple web application that displays public repositories of a specified GitHub user. The application is built using Flask and Docker, and it retrieves repository information via the GitHub API.

## Features

- Displays public repositories of a specified GitHub user.
- Shows repository names, descriptions, and links to the repositories.
- Customizable page title, heading, and initial text via environment variables.
- Simple and clean design with CSS.

## File Structure

- `Dockerfile`: Docker configuration file to build the Docker image.
- `requirements.txt`: List of Python dependencies.
- `app.py`: Main application file.
- `templates/index.html`: HTML template for rendering the web page.
- `static/styles.css`: CSS file for styling the web page.

## Environment Variables

- `GITHUB_USER`: GitHub username to fetch repositories for.
- `PAGE_TITLE`: Title of the web page.
- `HEADING`: Heading displayed on the web page.
- `INITIAL_TEXT`: Initial text displayed under the heading.

## License

This project is licensed under the Apache 2.0 License.
