# PicoBoy

I call it the PicoBoy as i used the pico-8 fantasy console along with the shell of a gameboy. Pretty creative huh?

## Why? ##
Now, Why did I make this in the first place? simply, to have fun. My phone was taking too much of my time so i wanted to direct my energy to something that could keep my attention and me, entertained. My old gameboy was completely out of battery, I couldn't find the charging wire and there were no cartridges in sight, so I thought for a bit and came up with this handheld. It functions more or less the same as the gameboy, with the ability to play any game along with similar mechanics.

<img width="250" height="425" alt="WhatsApp Image 2026-08-05 at 6 52 11 PM" src="https://github.com/user-attachments/assets/c2f3b57a-e54c-4dc0-8da5-90df352d5708" /> 

<img width="250" height="425" alt="WhatsApp Image 2026-08-05 at 6 51 03 PM" src="https://github.com/user-attachments/assets/61927112-c7db-4408-a3b5-1d9c91078ea6" />

https://github.com/user-attachments/assets/fd4c8ff4-f84a-478d-be18-1c1377a9bd91

Bill of components:
## Bill of Materials

| # | Component                          | Qty | Notes                                      |
|---|-------------------------------------|-----|---------------------------------------------|
| 1 | Raspberry Pi Zero W                 | 1   | Main compute board                          |
| 2 | 2.8" 240×320 SPI TFT LCD (ILI9341)  | 1   | Display for the game                        |
| 3 | Tactile push buttons                | 7   | D-Pad (4), X, C, Enter                      |
| 4 | 22AWG wire                          | 1-2m| For button and LCD connections              |
| 5 | GameBoy advance SP shell            | 1   | Original casing, gutted                     |
| 6 | PICO-8 license                      | 1   | Fantasy console software                    |
| 7 | MicroSD card                        | 1   | For Raspberry Pi OS + PICO-8                |
| 8 | Micro HDMI to HDMI adapter          | 1   | Used for initial setup                      |
|10 | Soldering iron & solder             | —   | To build the setup                          


At the moment, the buttons have started malfunctioning which explains why its not responding properly, Keep in mind that this is a prototype and the real project will require a custom-made PCB, 3D model and pad buttons like the ones found on the original GameBoy.


### Lessons Learnt and Improvements : 
## Known Issues

- **Buttons intermittently unresponsive** — some tactile buttons (currently: *specifically X*) 
  don't register presses reliably. Suspected cause: (*Bad soldering job/ faulty button*) 

- **Buttons are painful to use** - unsatisfying and reduces interest in playing.

- **No Battery** - Painful to use a power bank and a micro-USB wire to play.

- **Wiring outside the shell** - although it looks raw and handmade, the look doesn't look clean.

- **No Audio** - One of the biggest flaws that may look trivial but the sound effects from playing provide great satisfaction.

## Lessons Learned

- **Wiring gauge/length** — *(e.g. "22AWG worked fine for button wiring but felt bulky for the tight LCD ribbon 
  area — thinner gauge might route more cleanly next time")*.
- **Prototyping vs. final build** — point-to-point soldering made debugging easy but is fragile long-term; 
- **High quality wires** - tough, easy to solder and thin enough to route efficiently

## Future Plans

- [ ] Using a Raspberry Pi zero 2w. It features a 1GHz quad-core 64-bit processor instead of a single-core 32-bit chip, while keeping the exact same ultra-compact 65mm x 30mm form factor and 512MB of RAM.
    
- [ ] Design a custom PCB to replace point-to-point wiring.
- [ ] 3D print a proper case.
- [ ] Source proper Game Boy–style pad buttons instead of tactile switches (this is where designing a custom PCB will come in, as the pad buttons cannot be found as separate product).
      
- [ ] Add battery management (charging circuit, low-battery indicator)
- [ ] Using a proper Audio module to give a complete experience.


### Progress reports ( I gave up after the 5th day)

## Day 1:
Opened the gba advanced sp to check the dimensions and the design. It is truly mind boggling, the way nintendo made the fit so compact and buttons so easy to press. It might be impossible to actually fit my raspberry pi zero 2 W in there, but we'll get to that part after i get the pico-8 console to work on the raspberry pi. But what is pico-8? It is a fantasy game console built for to play and build games with more ease than a typical game engine and it also doesn't actually require much power so, hopefully it can run on the raspberry pi.

## Day 2:
Got the raspberry pi to fit into the gameboy shell finally, lets gooo. Had to cut a few things out to do it.

## Day 3: 
I did nothing.

## Day 4:

Researched a bit about raspberry pi gpio inputs and how i could use buttons and disguise them as key strokes. Ordered good quality buttons (hopefully), and a big hdmi to small hdmi converter so that i can actually find out whether or not my raspberry pi is even working or not.

## Day 5:
Got the hdmi converter, and got the raspberry pi to work properly. Now, all that's left is to buy pico and launch it. Only, button input, and LCD screen and battery power left.

Progress videos: 



