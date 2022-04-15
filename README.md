# CollidingBlocks
3b1b Colliding Blocks made using Python/Pygame

A small program coded in an afternoon to simulate 3b1b's video on colliding blocks computing Pi.

Video can be found here: https://www.youtube.com/watch?v=HEfHFsfGXjs&t=27s

Overall the program runs well up to values of 10000, then it starts to break. When we get to the next power of 100, the program breaks completely and the smaller block will shoot off into infinity. This is probably due to a discrepancy between the objects being drawn and the time it takes for the computer to do the velocity calculations, so perhaps a faster, more efficient language could work better than Python, or perhaps if he had fewer timesteps it would run better.
