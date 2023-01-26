# bulls-and-cows - improved
An improved version of the famous bulls-and-cows games

## highlights
- This code has the flexibility for the user to guess more than four numbers in its traditional settings.
- This code enables the user to request hints during his guesses.
- The number of round the user wants to repeat can be defined at the begining of the games.

## Installation
You just need to download the raw file from this repository or clone this on your system and run the python code.

`git clone https://github.com/someparsa/bulls-and-cows.git`

## Requirements
`Python 3.10+` is used to develop the code but there are not any specific libraries, packages and classes called when using the code. The only package used is the `random` which is initially installed when you install the python on your system.

As long as the user works with a python code, the game can be played on any operatingn system, like linux, windows, etc.

## Development
The functions developed in this code can be edited to be used in TKinter or any other GUI system. The current code only needs a terminal to interact with the user.

## How to play?
After running the code, you need to specify three initial questions.

### How many numbers?
You specify how many numbers you want to guess. Traditionally the games was set to guess four individual numbers ranging from 0 to 9. In the current implementation, user can specify to guess from one to ten numbers which never repeat. For example, if the first number is randomly set to be 5 by the application, the second and third and any other place holders will be never 5.

### How many rounds?
This parameter specifies how many round the user wants to play. There are no limits on this and can be specified from one round to as many rounds the user prefers.

### Do you need help? [Y/N]
If you need help and hints in each round, you can have it by typing `Y`, otherwise the `N` will be sufficient to prevent the code from printing hints. Hints will be printed in each step.

### Number:
After setting all previous steps, the game will be repeated as many rounds you specified and asks you to type and enter your guesses. After you guess and type one number, press enter to input the next number.

## Reports
This is a sample report when you run the code and the guess is wrong. You will see how many round are remaining for you have to guess more numbers, number of correct guesses, number of correct positions of the numbers and wrong guesses. The hint part also specifies whether the guess is correct and its position or not. Obviously the hint makes the guess so much easier for the user.

```
*** fail ***
remaining rounds 1
correct guess: 2
correct place: 0
your guess: [2, 4, 8, 9]

Hint: ['N', 'Y', 'Y', 'N']
C: correct guess - correct position
Y: correct guess - incorrect position
Y: incorrect guess
```
