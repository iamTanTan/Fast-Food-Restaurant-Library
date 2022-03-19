<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">Fast Food Restaurant Library</h3>

  <p align="center">
    A collaborative Fast Food Restaurant Library Application
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#set-up-steps">Set-up Steps</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

A project for ASU CSE412.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

-   [Flask](https://flask.palletsprojects.com/en/2.0.x/)
-   [Python](https://www.python.org/)
-   [PostgreSQL](https://www.postgresql.org/)
-   [Bootstrap](https://getbootstrap.com)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Set-up Steps

1. Clone the repo
    ```sh
    git clone https://github.com/iamTanTan/Fast-Food-Restaurant-Library.git
    ```
2. Install [Python](https://www.python.org/) (Check if installed via the following command)
    ```sh
    python --version
    ```
3. Create a virtual environment for your current python packages
    ```sh
    pip install virtualenv
    virtualenv venv
    ```
4. Activate virtual environment and install packages
    ```sh
    venv/Scripts/activate
    pip install -r requirements.txt
    ```
5. Modify/Create Postgres DB_URL

    ```sh
    # Local steps (some ommitted)
    psql -U username
    # enter password for username
    CREATE DATABASE fastfood_db;
    # NOTE: you need to edit init_db.py and app.py for the local postgres details for psycopg2 to work
    ```

    OR **use online hosting**

    ```sh
    cd application
    # NOTE: ASK Tanner for this file if in CSE412 Spring 2022
    touch credentials.py
    # in credentials.py
    # I suggest Heroku or Amazon (Heroku actually uses AWS)
    DB_URL = "postgres://<the rest of the url>"
    ```

6. Run Flask Application
    ```sh
    cd application
    python app.py
    # * Serving Flask app 'app' (lazy loading)
    # * Environment: production
    # WARNING: This is a development server. Do not use it in a production deployment.
    # Use a production WSGI server instead.
    # * Debug mode: off
    # * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

This shows the steps after the initial set up to run the application

    ```sh
    # in the root directory
    venv/Scripts/activate
    cd application
    python app.py
    ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/iamTanTan/Fast-Food-Restaurant-Library.svg?style=for-the-badge
[contributors-url]: https://github.com/iamTanTan/Fast-Food-Restaurant-Library/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/iamTanTan/Fast-Food-Restaurant-Library.svg?style=for-the-badge
[forks-url]: https://github.com/iamTanTan/Fast-Food-Restaurant-Library/network/members
[stars-shield]: https://img.shields.io/github/stars/iamTanTan/Fast-Food-Restaurant-Library.svg?style=for-the-badge
[stars-url]: https://github.com/iamTanTan/Fast-Food-Restaurant-Library/stargazers
[issues-shield]: https://img.shields.io/github/issues/iamTanTan/Fast-Food-Restaurant-Library.svg?style=for-the-badge
[issues-url]: https://github.com/iamTanTan/Fast-Food-Restaurant-Library/issues
[license-shield]: https://img.shields.io/github/license/iamTanTan/Fast-Food-Restaurant-Library.svg?style=for-the-badge
[license-url]: https://github.com/iamTanTan/Fast-Food-Restaurant-Library/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
