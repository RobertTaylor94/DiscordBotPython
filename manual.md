# /q - custom expression roll
Parameters:

    expression - num of dice d num of side + bonus (eg. 2d6 + 10)

    roll_type - (optional) What you're rolling for (eg. arcana)

# /add_roll - add a custom roll to your user

Parameters:

    name - the name of the roll, this is used to activate this roll in future

    type - defines what other parameters are tied to the roll, will be either attack or other

#### Type: Attack
    
    atkbonus - your base attack bonus

    dmgdice - the dice you roll for damage as an expression (eg. 1d10 + 1d4)

    dmgbonus - your normal plus to damage

#### Type: Other

    dice - the dice to roll as an expression (eg. 1d20)

    bonus - the bonus to the roll

# /check_roles - show your custom rolls
Will send a list of your custom rolls visible only to you

# /cr - used to roll one of your custom rolls
Will roll one of your custom rolls based of the name. If the roll is of type: attack then the firts roll will be for attack with a button attached to roll damage

Parameters:

    roll - this is the name you gave the custom roll on creation

    extraatk - if the roll is of type attack this will be added as an extra bonus to your attack roll

    extradmg - if the roll is of type attack this will be added as a bonus when you click the roll damage button

    extra - if the roll is of type other use this to add an extra bonus to the roll

# /delete_roll - to delete a custom roll

Parameters:
    
    roll - this is the name you gave the custom roll on creation

# /add_inventory - add an item to inventory

Parameters:

    name - the name of the item

    description - the item description

# /inventory - show your inventory
Will list out items in your inventory visible only to you

# /delete - delete an inventory item

Parameters:

    item - the name you gave the item on creation

# /update_supplies - update ship food and drink

Parameters:

    food - a number either positive or negative to update the food total

    drink - a number either positive or negative to update the drink total

# /supplies - display current food and drink supplies