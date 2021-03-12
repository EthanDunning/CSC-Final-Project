from winsound import *

#   Using winsound we can generate the tone (make sure your system sounds are
# turned up in windows) I found that the best tone range for us will be between
# 200 and 1200. It makes it easy being a solid 1000 range but we could limit it to
# 200 to 1000 really. I havent figured out volume yet but we will get there.

# frequency is the sound frequency in hertz and duration is in miliseconds

duration = 1000

for frequency in range (200, 1201, 50):
    print(frequency)
    Beep(frequency,duration)

# when we set up the sonic sensors then we can use them to adjust the frequency
