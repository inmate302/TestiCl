<pre>
################################################################

            ███████ ███  ██████████ ██ ██████ ██    
            █ ███ █ █    ██ ██  ██  ██ ███ ██ ██    
              ███   ██    ██    ██  ██ ███    ██    
              ███   ██   █ ██   ██  ██ ███ ██ ██    
              ███   █  █ ██ ██  ██  ██ ███ ██ ██    
              ███   ████ █████  ██  ██ ██  ██ ██   █
              ███                      ███ ██ ██ ███
              ███                      ██████ ██████
  
################################################################

     A CLI application to test your Joystick/gamepad inputs.
	     (An anagram of "Test CLI" somehow 
 		   managed to be both 
 	        Western and ball inspired...)


#########################    USAGE    ##########################

  - git clone https://github.com/inmate302/TestiCl
    to directory
  - run python TestiCL.py on your terminal
  - you may need to install pygame
  - or just run with `uv`¹: `uv run TestiCL.py` 
    (it automatically installs dependencies)

NOTE 1: before you run it, make sure your terminal is maximized
      for it to display properly (until I figure out how to
      make it redraw properly :FeelsBadMan:)
      If you're on Windows you can still run it outside a terminal
      but resizing breaks the program :c

NOTE 2: requires the `TERM=xterm-256color` ENV to be set
NOTE 3: Honestly, you'd be better off using the superior [gamepad tool][https://generalarcade.com/gamepadtool/]
	but if you live in the terminal, you might want to give TestiCL a try <3

###########################   TODO   ###########################

   - Finish presentation details. ✓
   - Make the device name be centered. ✓
   - Test display of battery for wireless controllers.
   - Manage to get different configurations 
     working (to display the buttons correctly). ✓
   - Make different "skins"
   - Make binaries for non dev friends(?) ✓
   - Add more quotes!
   - Add default mappings for PS & Nintendo controllers ✓
   - Fix multiple buttons displayed at once ✓
</pre>

1. https://docs.astral.sh/uv/getting-started/installation
