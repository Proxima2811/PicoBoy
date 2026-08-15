Raspberry pi zero w wiring schematic : raspberry pi zero w pinout


## Wiring / GPIO Pinout

<img width="1088" height="523" alt="schem1" src="https://github.com/user-attachments/assets/bd1b50ec-20a2-4d67-af9c-06266e60d239" />

### 2.8" SPI LCD (ILI9341)
| GPIO Pin (BCM) | Physical Pin | LCD Pin | Notes                     |
|-----------------|--------------|---------|----------------------------|
| GPIO10          | 19           | MOSI    | master device to peripheral|
| GPIO9           | 21           | MISO    | Peripheral back to master  |
| GPIO11          | 23           | SCLK    | SPI clock                  |
| GPIO8           | 24           | CS      | Chip select                |
| GPIO25          | 22           | DC      | Data/Command select        |
| GPIO6           | 31           | RST     | Reset                      |
| 3.3V            | 1            | VCC     | Power                      |
| Ground          | 34           | GND     | Common ground              |
| 3.3V            | 17           | LED     | Backlight                  |




### Buttons (GPIO → Button)
(Take the button wiring with a grain of salt.. In reality, you can wire the buttons to whichever gpio pins as all you need is an input from the button and no specific functions) 

| GPIO Pin (BCM) | Physical Pin | Button       | Notes                        |
|-----------------|--------------|--------------|-------------------------------|
| GPIO21          | 40           | D-Pad Up     |                                |
| GPIO4           | 7            | D-Pad Down   |                                |
| GPIO26          | 37           | D-Pad Left   |                                |
| GPIO2           | 3            | D-Pad Right  |                                |
| GPIO22          | 15           | X Button     |                                |
| GPIO3           | 5            | C Button     |                                |
| GPIO19          | 35           | Enter        |                                |
| GND (for all pins)| any GND    | Common Ground | All buttons share this ground |

<img width="600" height="800" alt="button layout irl" src="https://github.com/user-attachments/assets/cb3223ed-5777-477f-8ea5-ac754f41304a" />


