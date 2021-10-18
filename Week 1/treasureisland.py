#003 Treasure Island - Basic use of conditionals
print('''                        _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-'         ''')

print('Welcome to Treasure Island')
print('Your mission is to find the treasure')

#get input and convert it into lower case
choice = input('You are in a forest lost with ways on two sides. Choose \'left\' or \'right\'').lower()
if choice=='right':
    print('You are eaten by a lion. Game Over')
else:
    choice1= input('You find a lake. Swim or run?').lower()
    if choice1=='run':
        print('Game Over. Drowned')
    else:
        last = input('You have 3 doors. Choose 1, 2 or 3')
if last == 1:
    print('You have to start again.')
elif last ==2:
    print('Treasure is yours')
else:
    print('Game Over')