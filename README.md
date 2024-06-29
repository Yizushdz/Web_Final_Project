<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#cloning-repo">Cloning Repo</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#breakdown">Breakdown</a></li>
    <li><a href="#improvements">Improvements</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img width="1388" alt="homePage" src="https://github.com/Yizushdz/Web_Final_Project/assets/112721132/5551f4d4-fb95-4921-94a7-7c58b95aeb12">

CASO is a course project by Carlos Hernandez, Gerardo Aguillon Jr, Angel Torres, and myself, Jesus Hernandez. We are all computer science students at the University of Texas Rio Grande Valley (UTRGV). This was our final project for the "Object Oriented Programming in Python" course, taught by [Dr. Erik Enriquez.](https://www.linkedin.com/in/erik-enriquez/)

Below I explain how the website works. There is also a link to this website under the "About" tab on the right side of the screen.



## Built With

* **Python**: For most backend work
* **HTML and CSS**: For most frontend work
* **Bootstrap**: Used along with HTML and CSS
* **SQLite**: Used for the database, along with SQLAlchemy
* **Flask**: Framework used for faster website development
* **OnRender**: Used to host the website online for free

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Cloning Repo

1. To clone the repo
   ```sh
   git clone https://github.com/Yizushdz/Web_Final_Project.git
   ```



## Prerequisites

All installs needed should be contained in the `requirements.txt`. Simply run:
  ```sh
  pip install -r requirements.txt
  ```
on your command line after cloning the project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Breakdown

The website allows users to sign up if they don't have an account, or log in if they have an account already.

<img width="694" alt="logIn" src="https://github.com/Yizushdz/Web_Final_Project/assets/112721132/e7b099bd-a46a-44c1-bf1a-12724de7782e">

<img width="694" alt="signUp" src="https://github.com/Yizushdz/Web_Final_Project/assets/112721132/6dd02fbb-bbb3-43fe-8131-f3756077f46f">


Once you are logged in, you will land on the **Home** page, where you will see a list of all your decks, if you have any.

<img width="694" alt="deckPage" src="https://github.com/Yizushdz/Web_Final_Project/assets/112721132/1640212a-f942-433c-b2df-adfc90dc2d90">


If you don't have any decks, you can create one by clicking on "Add New Deck", where you will be prompted to enter the name of your new deck.

<img width="694" alt="deckCreation" src="https://github.com/Yizushdz/Web_Final_Project/assets/112721132/66a7a863-3551-4952-a3ba-3b83ceac2833">


Click "Submit", and your new deck will appear on the site.

<img width="694" alt="deckCreated" src="https://github.com/Yizushdz/Web_Final_Project/assets/112721132/0f4ebbf9-6fb1-4051-b03c-e77c142cb210">


Once you have created a deck, you may want to add some LeetCode problems that you need to do. If you navigate to the "Practice Problems" tab on top, you will see a list of LeetCode problems. There is a dropdown menu that allows you to only see problems from the selected difficulty. These problems were put into a list (.TXT file), as I could not figure out a way to extract all problems from the website, like using an API. 

<img width="694" alt="difficultyChoice" src="https://github.com/Yizushdz/Web_Final_Project/assets/112721132/f2ed356e-a1a9-4719-ac8e-98d8b0a22791">


From this list of problems, if you see any problem you would like to add to your existing deck, simply click on the '+' icon, and you will be prompted to choose the deck to which you would like to add the current problem to.

<img width="694" alt="AddtoDeck" src="https://github.com/Yizushdz/Web_Final_Project/assets/112721132/f67bdc7d-0af6-464c-8a1e-026e122c02d5">


Now, if you navigate to your deck page and click on a deck, you will see all the problems that you have added.

<img width="694" alt="DeckContent" src="https://github.com/Yizushdz/Web_Final_Project/assets/112721132/6554749f-91de-4195-8481-7be21b2bd162">


Each problem in your deck will flip like a flashcard when you hover over it. Once it turns, you will have a direct link to the actual LeetCode question from their website.

<img width="694" alt="FlashcartLink" src="https://github.com/Yizushdz/Web_Final_Project/assets/112721132/4d8f8f6c-0a3f-44fe-a595-e4b140847624">


This is it. It's a simple project that leverages the tools from Flask framework. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Improvements

- [x] Add Difficulty selection on "Browse Problems"
- [ ] Add delete option inside a deck
- [ ] When signing up or logging in, keep the entered information in the box if it fails to sign up or log in.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jesus Hernandez - [LinkedIn](https://www.linkedin.com/in/jesus-hernandez-55a860210/) - jesus.adrian.hdz27@gmail.com

Project Link: [web-final-project.onrender.com](web-final-project.onrender.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [GitHub Pages](https://pages.github.com)
* [GitHub Template](https://github.com/othneildrew/Best-README-Template)
* [Icons](https://shields.io/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/badge/Contributors-4-blue?style=for-the-badge
[contributors-url]: https://github.com/Yizushdz/Web_Final_Project/graphs/contributors
[forks-shield]: https://img.shields.io/badge/Forks-0-green?style=for-the-badge
[forks-url]: https://github.com/Yizushdz/Web_Final_Project/network/members
[stars-shield]: https://img.shields.io/badge/Stars-0-yellow?style=for-the-badge
[stars-url]: https://github.com/Yizushdz/Web_Final_Project/stargazers
[issues-shield]: https://img.shields.io/badge/Issues-0-red?style=for-the-badge
[issues-url]: https://github.com/Yizushdz/Web_Final_Project/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jesus-hernandez-55a860210/

<!--
To query entries from database:
- User.query.filter_by(id=1)
- User.query.all()

To delete records:
- db.session.delete(User.query.get(1)) // gets user of id=1
Must commit changes to take place: db.session.commit()
-->
