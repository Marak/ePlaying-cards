# ePlaying-cards
Hardware project for e-paper based playing card deck.

## Product Mission
Fun and new card game product that provides users the flexibility to play as many games as they wish with the use of just one digital card deck. 

## Target Users
Anyone that might enjoy a card game from ages 4-99+

## User Stories
* As a user I want to be able to hold at least 4 digital cards in my hand.
* As a user I want to be able to refresh a card without any latency.
* As a user I want the ecard controller to keep track of my game score.
* As a user I want the ecard controller to keep a history of game play.
* As a user I want the ability to save an ongoing game state.
* As a user I want the ecards to update to a different game in less than 5 seconds.
* As a user I want to be able to play games of up to four people.
* As a user I want to have an interface to setup games.

## MVP
The basic and minimum need for this product is to have a method of refreshing cards without latency and update the digital deck of at least 4 electronic cards without latency. The functionality shall be seamless as it would be when using a normal paper card deck.

## Patent Implication
This idea has already been patented and the patent is now abandoned which makes this a public patent idea to be used by anyone. Althouhg options exist if specific technologies are implemented that give the product a new 

# System Design
The implementation of this product will be mainly through the use of e-paper displays to display each card value. This technology is the ideal candidate for this implementation as it is very low power and it mimics the look of ink on paper. The system will need a central computer to manage and store the card games, which will be implemented with the use of a small microcontroller or a single board computer enabled with a wifi or bluetooth module in order to communicate with the ecards.

![SystemDesign](AnycardSystemDesign.png)

## E Cards
The electronic cards would be implemented using electronic paper, a technology that uses very low power consumption, is flexible and mimics the look of real paper. Electronic paper uses electronic ink which is comprised of millions of microcapsules that contain a positive or negative charge, the electronic paper

![Image showing simple explanation of how epaper displays function.](https://www.smartcity-displays.com/wp-content/uploads/2017/07/how-does-e-paper-work-1.gif)
Source: https://www.smartcity-displays.com/wp-content/uploads/2017/07/how-does-e-paper-work-1.gif

## Deck Controller
The application will have a deck controller which will be tasked with game management. The operations for game management are the following:
* Shuffle cards
* Deal cards
* Point calculations and distribution
* Game rules
* Game selection
* Score management
* Keep memory of card distribution and card graveyard

## Software Architecture
![SoftwareDesign](SoftwareDesign.png)
