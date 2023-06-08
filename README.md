# Legend Discord Bot

This bot is being actively worked on, most features implemented and working, some WIP and could do with some refactoring.

## About

A discord bot for dice rolls and inventory tracking in Rule of Cool's Legend TTRPG system. Currently refining features and adding new features to have a minimum viable product for use in the Legend game I currently play in.

## Adding bot

WIP not currently available for public use.

## Usage

/r -- the most basic command to roll dice using a string expression. Can roll multiple different types of dice with added bonuses.

/b -- shows a list of buttons with common dice rolls, currently has hard coded versions of common rolls used by players in the game I play.

/inventory -- shows a list of items in the inventory of the user performing the command.

/add_inventory -- enables the user to add an item to their inventory with parameters for name and description.

/delete -- takes the name of an item as a parameter and deletes that item from the users inventory if it is found.

/check_roles -- shows a list of custom rolls the user performing the command has saved.

/add_roll -- allows the user to create a new custom dice roll with two options: an attack type with parameters for attack bonus, damage dice and damage bonus and an other type with parameters for dice to roll and bonus for the roll.

/delete_roll -- allows the user to delete one of their custom rolls.

/cr -- takes the name of a custom roll with an extra parameter for further attack, damage or other bonuses.

### Pirate Campaign

Commands specific to the current pirate campaign

/supplies -- show a list of food and drink supplies onboard the ship

/update_supplies -- allows all users to update the ship supplies
