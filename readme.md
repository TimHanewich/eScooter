# eScooter
I may make my own eScooter/eBike.

## Configuration
- Bike: Schwinn SX2000 Mountain Bike
    - [My actual bike](https://i.imgur.com/GaSKJRi.jpeg)
    - [Online listing](https://www.propertyroom.com/l/schwinn-sx2000-mountain-bike/10507696)
    - [Online listing on facebook marketplace](https://www.facebook.com/marketplace/item/3741195909458022/?_rdr)
    - [This tutorial](https://youtu.be/Aj35ce6RfEM?si=b9BWHbFmZhSQtrBy) demonstrates removing the crank that looks like a square, like my bike.
    - The largest rear gear has **28** teeth. This 28-tooth gear is about **4.5 inches** (approx) in diameter.
    - The "rear pole" (the pole that I'm mounting the gear box on) has a diameter of 32 mm.
    - The "bottom pole" (the pole the other two screws go into) has a diameter of approx. 48.5 mm.
    - The two screws that screw into the frame for the water bottle holder are **M5*15mm** screws.
- Motor: Platinum 5230SL 190KV
    - Listings:
        - [On Hobby Wing](https://www.hobbywingdirect.com/products/platinum-fw-5230-motors?variant=42212563452019)
            - [Marketing Page](https://www.hobbywing.com/en/products/Platinum5230.html)
            - [Specs](https://cdn.shopify.com/s/files/1/0109/9702/files/pl5230-data.pdf?v=1724706933)
        - [On Hobby King](https://www.towerhobbies.com/product/platinum-5230sl-motor-190kv/HWI30416200.html)
        - [On Amain Hobbies](https://www.amainhobbies.com/hobbywing-platinum-5230sl-brushless-outrunner-motor-190kv-hwa30416200/p1578736)
    - Voltage: 12S, but specs show it performing at 10S, so lower S's should work.
    - 112A max current (stall)
    - 4,895w max power
    - Measurements
        - Inner holes (M4) = 30mm apart
        - Outer holes (M4) = 44mm apart
    - It appears to use 4mm male bullet connectors, just like [this motor does](https://a.co/d/dk6BBRY).
- [Motor Coupling](https://a.co/d/3mqO0bW) used to mount the gear to the motor shaft.
    - The 4 holes on the disc are 24mm apart from the opposite side (so 12mm from the center)
- [ESC](https://a.co/d/0q2reOV)
    - Manual: https://maifile.cn/est/a660b60abe5735/pdf, but stored pictures of it [here](https://imgur.com/a/tfH6Hq5).
    - I tested it at 4S, it works at 4S despite it saying 5-12S.
- Batteries: 3 [4S 3300 mAh LiPo batterys (60C)](https://a.co/d/cUkfjpm), in a series (effectively 12S)
- [5V Buck Converter](https://a.co/d/enad4n0)
- [eBike Thumb Throttle](https://a.co/d/3h9mEAN)
    - [wiring](https://m.media-amazon.com/images/I/61KwWizb+DL._AC_SX679_.jpg)
- Hose Clamps
    - [2.5" Clamps](https://a.co/d/6WDhVfk) are used for the motor mount on the bottom pole *(they say KSI on the lock)*
    - 2 hose clamps from Ford's Garage (I think shorter than 2.5"... maybe 1.5"?) are used to mount the gearbox to the mid-pole (verticall) *(they say 304 on the lock)*

## All Development Media
- January 25, 2025: [Photos of Bike Before Modifying it](https://imgur.com/a/QJfTLXH)
- January 27, 2025: [Determining Motor Mounting Position](https://imgur.com/a/0CeCH1P)
- January 31, 2025: [Original Motor Mounting](https://imgur.com/a/6YDlS4K)
- February 2, 2025: [Motor Startup Hesitation](https://youtu.be/MqxyXDnDgKA)
- February 2, 2025: [Motor Running Test with Gear Shifting](https://youtu.be/jSprWTQn9RQ)
- Februry 28, 2025: [New Gearbox Mounted](https://imgur.com/a/rcUkqlp)
- March 12, 2025: [Shaft Slippage](https://imgur.com/a/C1VOYFI)
- March 15, 2025: [No More Slippage (notches etched into shafts)](https://imgur.com/a/ccalIE8)
- March 16, 2025: [Demonstrating Motor Connection](https://imgur.com/a/e7eUgE7)
- March 27, 2025: [Full Drivetrain Test](https://youtu.be/gY1TRV99fqI)
- March 27, 2025: [eBike Development](https://youtu.be/JQQ2eHjpAwc)
- April 4, 2025: [First Test Run](https://youtu.be/8QopB0LM2to)
- April 27, 2025: Second Test Run
    - [Pictures of damage](https://imgur.com/a/OvujgRJ)
    - [Full Video and Pictures (unedited)](https://youtu.be/GyaS9Lfgngo)

## Inspiration
- [Tom Stanton eBike V1](https://www.youtube.com/watch?v=9rIIJbDkpN8)
    - [Motor he used](https://hobbyking.com/en_us/turnigy-aerodrive-sk3-6374-149kv-brushless-outrunner-motor.html/?___store=en_us): $105, 149KV, 2700W, 12S
    - [3D Printed Parts](https://www.thingiverse.com/thing:2191603)
- [Tom Stanton eBike V2](https://www.youtube.com/watch?v=IymLqEPUkvw)
- [This video](https://www.youtube.com/watch?v=V4ohWg4GfYc) describes designing and 3D printing a sprocket.
- [This defaileur pulley](https://www.thingiverse.com/thing:4677579/files) fit perfectly! (I printed and tried)
    - Specs (reversed engineered): https://i.imgur.com/SSaZPZ7.png (10.28mm pitch?)
        - I think these specs are wrong... 
        - I think the gear maker in Blender has its measurements off.
        - When I make a gear with a 12.7mm pitch in FreeCAD and then import it into Blender, it matches this gear with apparently a 10.28mm pitch... 
        - Blender must have its measurements off somehow.
        - So, anyway, if you design a gear in blender, I guess use a 10.28mm pitch because that is *actually* a 12.7mm pitch!
    - I remixed it [here](https://www.thingiverse.com/thing:6930961).
- [Michael Rechtin made a nice stackable gearbox](https://youtu.be/G0DcM60lWSw?si=MsUi8FOoKw17uXnp)
    - [20x27x4mm bearing](https://a.co/d/306vlTe)
    - [45x58x7mm bearing](https://a.co/d/fQ6uB3k)