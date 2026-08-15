Raspberry pi zero w wiring schematic : raspberry pi zero w pinout

<img width="945" height="662" alt="image" src="https://github.com/user-attachments/assets/29adc499-0ea8-4c10-9beb-cf681e01e71c" />

## Wiring / GPIO Pinout

### Buttons (GPIO → Button)
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
