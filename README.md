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
  - or just run with `uv`¹: `uv run TestiCL.py` (it automatically installs dependencies)

NOTE: before you run it, make sure your terminal is maximized
      for it to display properly (until I figure out how to
      make it redraw properly :FeelsBadMan:)
      If you're on Windows you can still run it outside a terminal
      but resizing breaks the program :c

NOTE: requires the `TERM=xterm-256color` ENV to be set 

###########################   TODO   ###########################

   - Finish presentation details.
   - Make the device name be centered.
   - Test display of battery for wireless controllers.
   - Manage to get different configurations
     working (to display the buttons correctly).
   - Make different "skins"
   - make .exe for non dev friends(?)
</pre>

1. https://docs.astral.sh/uv/getting-started/installation
