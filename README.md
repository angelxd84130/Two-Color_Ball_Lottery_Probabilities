
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h2 align="center">Two-Color Ball Lottery Probabilities</h2>

  <p align="center">
    Automatic classification system
    <br /> 
    <a href="https://github.com/angelxd84130/NewsClassification/issues">Report Bug</a>
    ·
    <a href="https://github.com/angelxd84130/NewsClassification/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#purpose">Purpose</a></li>
        <li><a href="#description">Description</a></li>
        <li><a href="#games">Games</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li> 
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project  
### Purpose  

The goal is to make a program to count all games' probabilities of the two-color ball lottery.  

Here's why:
* Varify all options' probabilities of a game
* Ensure the sum of all options of a game is equal to 1


### Description  
Based on two fixed colors, iterate over all combinations of numbers.  
Calculate the probabilities of each option from the combination based on different game.

### Games  
![Two-Color_Ball][product-screenshot0]  

  

### Built With

* [itertools](https://docs.python.org/3/library/itertools.html)
* [pandas](https://pandas.pydata.org/)


<!-- GETTING STARTED -->
## Getting Started

Run the python file base on the game's main color.

### Prerequisites


1. download/import python packages  

2. Call the game's function
```
''' blue.py '''
# get all combinations of numbers
all = get_all()
# print out the options' probabilities
print(count_prim(all))
```
   
3. Run the python file
   
4. Check the results




<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/angelxd4130/Two-Color_Ball_Lottery_Probabilities/issues) for a list of proposed features (and known issues).


<!-- CONTACT -->
## Contact

Yu-Chieh Wang - [LinkedIn](https://www.linkedin.com/in/yu-chieh-wang/)  
email: angelxd84130@gmail.com




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/angelxd84130/Two-Color_Ball_Lottery_Probabilities.svg?style=for-the-badge
[contributors-url]: https://github.com/angelxd84130/Two-Color_Ball_Lottery_Probabilities/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/angelxd84130/Two-Color_Ball_Lottery_Probabilities.svg?style=for-the-badge
[forks-url]: https://github.com/angelxd84130/Two-Color_Ball_Lottery_Probabilities/network/members
[stars-shield]: https://img.shields.io/github/stars/angelxd84130/Two-Color_Ball_Lottery_Probabilities.svg?style=for-the-badge
[stars-url]: https://github.com/angelxd84130/Two-Color_Ball_Lottery_Probabilities/stargazers
[issues-shield]: https://img.shields.io/github/issues/angelxd84130/Two-Color_Ball_Lottery_Probabilities.svg?style=for-the-badge
[issues-url]: https://github.com/angelxd84130/Two-Color_Ball_Lottery_Probabilities/issues
[license-shield]: https://img.shields.io/github/license/angelxd84130/Two-Color_Ball_Lottery_Probabilities.svg?style=for-the-badge
[license-url]: https://github.com/angelxd84130/Two-Color_Ball_Lottery_Probabilities/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/yu-chieh-wang/
[product-screenshot0]: Two-Color_Ball.png

