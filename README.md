<!-- Improved compatibility of back to top link: See: https://github.com/ildebr/ovnis-backend/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">OVNIS Backend</h3>

  <p align="center">
    This is the backend for https://github.com/ildebr/ovnis-frontend.<br />
    Live at https://ovnis-backend.onrender.com/
    
  </p>
    <br />
    
    
    <a href="https://github.com/ildebr/ovnis-backend">View Demo</a>
    
    <a href="https://github.com/ildebr/ovnis-backend/issues">Report Bug</a>
    
    <a href="https://github.com/ildebr/ovnis-backend/issues">Request Feature</a>
  
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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

OVNIS app is a website to store data about OVNIs sightings, this data includes latitude, longitude, date, a description of the sighting, etc. I provide endpoints to filter sightings by continent, country and date (including a date range).
Built using Django, this provides all the endpoints for reading, creating, editing, and deleting sightings for an user. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Django][Django.dev]][Django-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The recomended version of python for this projects is 3.10.10


### Prerequisites

Python 3.10.10
* npm
  ```sh
  pip install -r requirements.txt
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._


1. Clone the repo
   ```sh
   git clone https://github.com/ildebr/ovnis-backend
   ```
2. Install NPM packages
   ```sh
   pip install -r requirements.txt
   ```
3. Go to Open Cage Geocode to get an API key, copy ovnis_api/.env.example delete the .example extension and copy your API Key here.
4. Go to core/ and do the same with .env.example but change data with a postgresql database link (you can use a sqlite database on local commenting the current DATABASES var and uncommenting the one above it) and add a Django Secret Key
5. Run the migrations, and run the server
  ```sh
   py manage.py migrate
   py manage.py createsuperuser
   py manage.py runserver
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You have a list of all the endpoints on ovnis_api/urls.py


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Endpoints
1. Get all sightings
   Making a get request to
   ```sh
   /api/sightings/
   ```
   will return all the sightings available
2. User creation
   ```sh
   /api/user/
   ```
   is the endpoint for user creation, it accepts a JSON post request formatted as follows
   ```json
   {
      "email": "something@something.com",
      "password": "yourpassword"
   }
   ```
3. User authentication
   ```sh
   /auth/jwt/create/
   ```
   is the endpoint for user login, it receives a JSON post request formatted with the parameters email and password
   ```json
   {
      "email": "something@something.com",
      "password": "yourpassword"
   }
   ```
   and returns
   ```json
     {
        "access": "youraccess",
        "refresh": "yourrefresh"
     }
   ```
4. Create a new sighting
   With the access token added to the authentication headers as 'Bearer ${token}', you can make a post request to
   ```sh
   /api/sightings/create/
   ```
   with a json request that contains
   ```json
   {
      "title": "",
      "description": "",
      "latitude": "",
      "longitude": ""
   }
   ```
   it will return the sighting created with its id.
5. Update a sighting
   You can update an existing sighting if you're the author and make a put request to
   ```sh
   /api/sightings/update/<sighting id>
   ```
   with a json request that contains
   ```json
   {
      "title": "",
      "description": "",
      "latitude": "",
      "longitude": ""
   }
   ```
   
<!-- ROADMAP -->
## Roadmap

- [x] Add sighting CRUD endpoints
- [x] Add user creation and authentication endpoints
- [ ] Add filtering endpoints
- [ ] Multi-language Support
    - [ ] English
    - [ ] Spanish

See the [open issues](https://github.com/ildebr/ovnis-backend/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact



Project Link: [https://github.com/ildebr/ovnis-backend](https://github.com/ildebr/ovnis-backend)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


* [Choose an Open Source License](https://choosealicense.com)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ildebr/ovnis-backend.svg?style=for-the-badge
[contributors-url]: https://github.com/ildebr/ovnis-backend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ildebr/ovnis-backend.svg?style=for-the-badge
[forks-url]: https://github.com/ildebr/ovnis-backend/network/members
[stars-shield]: https://img.shields.io/github/stars/ildebr/ovnis-backend.svg?style=for-the-badge
[stars-url]: https://github.com/ildebr/ovnis-backend/stargazers
[issues-shield]: https://img.shields.io/github/issues/ildebr/ovnis-backend.svg?style=for-the-badge
[issues-url]: https://github.com/ildebr/ovnis-backend/issues
[license-shield]: https://img.shields.io/github/license/ildebr/ovnis-backend.svg?style=for-the-badge
[license-url]: https://github.com/ildebr/ovnis-backend/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Django.dev]: https://img.shields.io/badge/Django-4A4A55?style=for-the-badge&logo=Django&logoColor=FF3E00
[Django-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
