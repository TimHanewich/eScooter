# eScooter
I may make my own eScooter/eBike.

## Possible Configuration
- Bike: Schwinn SX2000 Mountain Bike
    - [My actual bike](https://i.imgur.com/GaSKJRi.jpeg)
    - [Online listing](https://www.propertyroom.com/l/schwinn-sx2000-mountain-bike/10507696)
    - [Online listing on facebook marketplace](https://www.facebook.com/marketplace/item/3741195909458022/?_rdr)
    - [This tutorial](https://youtu.be/Aj35ce6RfEM?si=b9BWHbFmZhSQtrBy) demonstrates removing the crank that looks like a square, like my bike.
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
        - Outer holes (M4) = 45mm apart
    - It appears to use 4mm male bullet connectors, just like [this motor does](https://a.co/d/dk6BBRY).
- [ESC](https://a.co/d/0q2reOV)
    - Manual: https://maifile.cn/est/a660b60abe5735/pdf, but stored pictures of it [here](https://imgur.com/a/tfH6Hq5).
    - I tested it at 4S, it works at 4S despite it saying 5-12S.
- Batteries: 3 [4S 3300 mAh LiPo batterys (60C)](https://a.co/d/cUkfjpm), in a series (effectively 12S)
- [5V Buck Converter](https://a.co/d/enad4n0)

## Possible Shops
- For motors
    - brushless.com
    - hobbyking.com
    - [Tower Hobbies](https://www.towerhobbies.com/airplanes/parts-electronics-and-accessories/motors/?prefn1=discontinued&prefv1=false&start=0&sz=24&return=true)
        - $250, 230KV, 3750w, 9-15S: https://www.towerhobbies.com/product/avian-8075-230kv-outrunner-brushless-motor/SPMXAM4800.html
        - $300, 160KV, 4400w,9-15S: https://www.towerhobbies.com/product/avian-8085-160kv-outrunner-brushless-motor/SPMXAM4805.html
        - $200, 200KV, 1900w, 9-12S: https://www.towerhobbies.com/product/avian-6362-200kv-outrunner-brushless-motor/SPMXAM4796.html
        - $85, 250KV, ___w, 12s: https://www.towerhobbies.com/product/platinum-4120sl-motor-250kv/HWI30416000.html
        - $120, 220KV, ___w, __s: https://www.towerhobbies.com/product/platinum-5220sl-motor-220kv/HWI30416150.html
        - $140, 190KV, ___w, __s: https://www.towerhobbies.com/product/platinum-5230sl-motor-190kv/HWI30416200.html
            - Specification chart: [page 1](https://cdn.shopify.com/s/files/1/0109/9702/files/5200s-spec0.png?v=1724707806), [page 2](https://cdn.shopify.com/s/files/1/0109/9702/files/5200s-spec1.png?v=1724707804), found [here](https://www.hobbywingdirect.com/collections/hobbywing-brushless-motors-aircraft/products/platinum-fw-5220-motors?variant=42212271358067)
- For ESC
    - 60A 12S ESC: https://store.tmotor.com/product/alpha-60a-12s-esc.html
    - 120A 12S ESC: https://store.tmotor.com/product/alpha-120a-12s-esc.html
    - 80A, 12S ESC: https://www.progressiverc.com/products/t-motor-c80a-12s-esc?variant=41713640571015&country=US&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&com_cvv=8fb3d522dc163aeadb66e08cd7450cbbdddc64c6cf2e8891f6d48747c6d56d2c
    - Amazon
        - $72: 50A, 3-12S VESC: https://a.co/d/eVvcFJE (*Amazon Prime*)
        - $99: 200A, 5-12S ESC: https://a.co/d/26q7Vlr
        - $119, 150A 5-12S ESC (no BEC): https://a.co/d/6W6F2w9
        - $59, 100A 5-12S ESC (no BEC): https://a.co/d/gSVhW4V
            - https://sequremall.com/products/sequre-12100-brushless-electric-speed-controller-5-12s-power-supply-100a-blheli_32-am32-firmware-support-128khz-pwm-frequency-suitable-for-multi-rotor-aircrafts-airplane-models-plant-protection-machine-boat-models-rc-car-models?variant=43436914704572
            - https://alofthobbies.com/products/sequre-100-amp-esc-5-12s
            - Set up guide: https://drive.google.com/file/d/1Ad84Rms98xa7bZ2ibhUmMPNMh6rs4cjZ/view
    - $140: 120A, 12S ESC: https://www.underwaterthruster.com/products/apisqueen-lightning-esc-12s-lipo-48v-60a-120a-160a-for-thrusters-brushless-motors-drones-etc?variant=44063481397476&country=US&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gQT=2
- 5V Buck Converter
    - https://a.co/d/enad4n0
    - https://a.co/d/2DZnsPa

## VESC Challenges
- Articles that seem to describe my problem
    - https://forum.esk8.news/t/one-motor-not-spinning-after-successful-motor-setup/26525
    - https://endless-sphere.com/sphere/threads/anyone-experienced-with-vesc-foc-sensorless.100798/
    - https://vesc-project.com/node/4502
    - https://vesc-project.com/node/4564
    - https://forum.esk8.news/t/motors-not-working-and-making-violent-sounds-after-foc-configuration/68688
- The motor seemed to work reasonably well after [this FOC Detection Result](https://i.imgur.com/M4PzxR8.png).
    - Iterations of this:
    - Iteration 2: https://i.imgur.com/XsOZNj7.png
    - Iteration 3: https://i.imgur.com/KFRICJm.png, but be sure to set "Current No Reverse" (not "Current No Reserve with Brake") in the PPM input settings.
    - Iteration 4: https://i.imgur.com/eYmxS4e.png

## Inspiration
- https://www.youtube.com/watch?v=9rIIJbDkpN8
    - [Motor he used](https://hobbyking.com/en_us/turnigy-aerodrive-sk3-6374-149kv-brushless-outrunner-motor.html/?___store=en_us): $105, 149KV, 2700W, 12S
    - [3D Printed Parts](https://www.thingiverse.com/thing:2191603)
- [This video](https://www.youtube.com/watch?v=V4ohWg4GfYc) describes designing and 3D printing a sprocket.
- [This defaileur pulley](https://www.thingiverse.com/thing:4677579/files) fit perfectly! (I printed and tried)
    - Specs (reversed engineered): https://i.imgur.com/SSaZPZ7.png (10.28mm pitch?)
        - I think these specs are wrong... 
        - I think the gear maker in Blender has its measurements off.
        - When I make a gear with a 12.7mm pitch in FreeCAD and then import it into Blender, it matches this gear with apparently a 10.28mm pitch... 
        - Blender must have its measurements off somehow.
        - So, anyway, if you design a gear in blender, I guess use a 10.28mm pitch because that is *actually* a 12.7mm pitch!
    - I remixed it [here](https://www.thingiverse.com/thing:6930961).