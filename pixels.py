import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 600, auto_write=False)

pixels[2] = (100, 0, 0)
pixels[1] = (0, 100, 0)
pixels[0] = (0, 0, 100)
pixels[599] = (0, 0, 255)
pixels.show()