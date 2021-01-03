import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 600)

pixels[0] = (100, 0, 0)
pixels[1] = (0, 100, 0)
pixels[2] = (0, 0, 100)
pixels[599] = (0, 0, 255)