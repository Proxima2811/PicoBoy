## How It Works

### SPI Communication (Display)
Brief explanation of what SPI is and why it's used here — e.g. a synchronous serial protocol 
using MOSI/MISO/SCLK/CS lines, chosen because it's fast enough to drive a 240×320 display 
with relatively few GPIO pins compared to a parallel interface. Explain what each signal does:
- **MOSI** — data sent from the Pi to the display
- **SCLK** — clock signal that syncs data transfer
- **CS (Chip Select)** — tells the display when it should "listen"
- **DC (Data/Command)** — tells the display whether incoming data is a command or pixel data
- **RESET** — hardware reset line for the display controller

### GPIO Buttons
### Understanding Pull-Up and Pull-Down Resistors

A GPIO pin with nothing connected to it is "floating" — it picks up stray electrical 
noise and reads randomly instead of a clean HIGH or LOW. A button doesn't fix this on 
its own, since it only connects two points together when pressed; it doesn't define 
what the pin reads when it's *not* pressed.

A pull-up resistor solves this by connecting the pin to 3.3V through a resistor, while 
the button connects the same pin to Ground. This forms a voltage divider: with the 
button open, almost all the voltage appears at the pin, reading HIGH. When pressed, 
the button offers a near-0Ω path to Ground, overpowering the resistor and pulling the 
pin to LOW. A pull-down resistor is the same idea, flipped — pin reads LOW at rest, 
HIGH when pressed. The Raspberry Pi has these resistors built in, enabled in software, 
so PicoBoy's buttons wire straight to GPIO and Ground with no external resistor needed.

### Button-to-Input Mapping
Explain how a GPIO press gets translated into something PICO-8 or the OS understands as a 
"key press" — e.g. via a Python script polling GPIO states and simulating keyboard events, 
or a driver/overlay that maps GPIO pins directly to input events.

## Device Tree Overlays

The Raspberry Pi doesn't automatically detect SPI displays the way it detects USB devices.
SPI is a "dumb" protocol — there's no handshake or ID that tells the kernel what's connected
on the other end of MOSI/MISO/SCLK. The kernel has to be told explicitly what hardware exists
and how it's wired, and that's what a **device tree overlay** does.

A device tree is a data structure describing the hardware present on the board — CPU, memory,
buses, and any peripherals. On boot, the bootloader loads a base device tree for the Pi model,
then applies **overlays** on top of it to add hardware that isn't built-in, like our SPI LCD.

### Enabling the overlay

The overlay is added as a line in `/boot/config.txt`:

```ini
dtoverlay=ili9341,speed=32000000,rotate=90
```

Breaking this down:

| Parameter | Meaning |
|---|---|
| `ili9341` | Tells the kernel which display driver to bind — matches our LCD's controller chip |
| `speed=32000000` | SPI clock speed in Hz (32 MHz here) — higher speed means faster refresh, but too high can cause display glitches depending on wiring length/quality |
| `rotate=90` | Rotates the display output to match how it's physically mounted inside the shell |

### What happens without it

If this line is missing or misconfigured, the Pi still sends power and can technically toggle
the SPI pins — but the kernel has no driver bound to the display, so nothing gets rendered.
The LCD will stay blank or show garbage, even though the wiring itself is correct. This tripped
me up early on — it *looks* like a wiring problem but is actually a configuration problem.

### Verifying it loaded correctly

After a reboot with the overlay enabled, check that the kernel picked it up:

```bash
dmesg | grep -i ili9341
```

A successful load shows the driver binding to the SPI device and registering a display.
If you see no output here, the overlay isn't being applied — double-check the exact overlay
name matches your kernel version and that `config.txt` was saved to the correct boot partition.

### Power
Explain how power flows from your battery/power source into the Pi and display — voltage 
regulation, whether the LCD backlight is always-on or switchable, and any current draw 
considerations if relevant.

### Why These Design Choices
Optional but valuable: briefly explain *why* you chose SPI over other display interfaces, 
why you chose the Pi Zero W over alternatives, why tactile buttons over other switch types, etc. 
This context helps other makers understand the trade-offs if they want to modify the design.
