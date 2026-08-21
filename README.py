input("""
 #     # ####### ######     ######  ####### #       #######    #     #####  #######      #   
 ##   ## #       #     #    #     # #       #       #         # #   #     # #           ##   
 # # # # #       #     #    #     # #       #       #        #   #  #       #          # #   
 #  #  # #####   ######     ######  #####   #       #####   #     #  #####  #####        #   
 #     # #       #          #   #   #       #       #       #######       # #            #   
 #     # #       #          #    #  #       #       #       #     # #     # #            #   
 #     # ####### #          #     # ####### ####### ####### #     #  #####  #######    ##### 

 Mep release 1.0.1                              
Thank you for installing MOMO EXPLOSION PROJECT a.k.a. MEP!

Before using this installation release, Please read this README precisely.

This project's purpose is to TAS the following link:
    https://www.google.com/doodles/halloween-2016
    Magic Cat Academy 1 (Google Doodles, 2016, Web)

Just for fun.
But for serious reason, is to beat Speedrun world records.
    https://www.speedrun.com/gdhw2016
    For more informations.

Current world record(according to August 18, 2026) is 4:34.917 by Voulu.
Our final challenge is to reach 4:34 or lower.

# How to run it?
    Please enter the folder `root` and open mep_background_runner.py to run it.
    After running it, You can freely use your functions!

[Enter to continue]
""")
input("""
# Then how do I use it?
    Use 1~8 to make mouse move automatically for drawing `spells` or aborting and quitting program.
    Each function's command is independent as:
        1: I
        2: -
        3: V
        4: Up-V
        5: Lightning
        6: Heart

        7: Abort inputting spells
        8: Quit program
    And inputting those functions will make mouse draw those spells.
    You can change the hotkey in the program.
    Default running position is x=600, y=500.
    Use tkinter-mouse-test3 to check if this actually runs.

If you ACTUALLY got 4:34 or beat the world record, Congratulations!
I will send this play to TASVideos.org or speedrun.com, as official reached progress!
Please have fun using this!

    DISCLAIMER

    You can copy and modify it and even remix or enhance the code,
    BUT PLEASE DO NOT USE IT FOR COMMERCIAL PURPOSE, UNLESS
    YOU ARE THE DEVELOPER OF GOOGLE DOODLE HALLOWEEN 2016 (MCA1)!
    
    THIS PROGRAM IS NOT BUILT FOR COMMERCIAL USES AND IF YOU SAW
    SOMEONE USING THIS FOR COMMERCIAL PURPOSE, PLEASE REPORT
    US (cuteyumin1004@gmail.com) TO KNOW IT!
    IF SOMONE USE MY GMAIL FOR SPAM, I WILL REPORT IT TOO!

####################################################################

[Enter to continue]
""")
print("""
=--- Update notes ---=

Latest update, Stable: v1.0.1
  Fixed minor bug and modified movement while firing spell.
    I, E:
    Put 1 more pass to drag.

    V, Up-V:
    Modified Drawing timing. (Timing divider: 2 → 1.4)

    Lightning:
    Modified passes. ({30, 50, -50} → {60, 100, -100})
""")