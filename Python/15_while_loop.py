a = 1

while a <= 20:  # While loop will continue until the condition is true. 
    # In this case 20>1 is always true, so it'll keep on running infinitely. This is called an infinite loop.
    print(a)    # Prints value of a infinitely.
    a += 1      # To make this loop stop at some point, we are making a increment by 1 at each iteration.
                # That way, when value of a reaches 21, the condition for while loop won't be true.
                # And since it's not true, the loop will break. In other world, the loop will stop.