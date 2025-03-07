def main_menu():
    # Title Screen
    print()
    print(rf"""
  █████▒▒█████   ▒█████   ██▓      ██████      ▄████  ▒█████   ▄▄▄       ██▓    
▓██   ▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒     ██▒ ▀█▒▒██▒  ██▒▒████▄    ▓██▒    
▒████ ░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄      ▒██░▄▄▄░▒██░  ██▒▒██  ▀█▄  ▒██░    
░▓█▒  ░▒██   ██░▒██   ██░▒██░      ▒   ██▒   ░▓█  ██▓▒██   ██░░██▄▄▄▄██ ▒██░    
░▒█░   ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒   ░▒▓███▀▒░ ████▓▒░ ▓█   ▓██▒░██████▒
 ▒ ░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░    ░▒   ▒ ░ ▒░▒░▒░  ▒▒   ▓▒█░░ ▒░▓  ░
 ░       ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░     ░   ░   ░ ▒ ▒░   ▒   ▒▒ ░░ ░ ▒  ░
 ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░     ░ ░   ░ ░ ░ ░ ▒    ░   ▒     ░ ░   
           ░ ░      ░ ░      ░  ░      ░           ░     ░ ░        ░  ░    ░  ░
                                                                                
""")
    
    # Main Menu Options
    print("Start Game")
    print("Settings")
    print("Exit Game")
    print()

    choice = input("> ").strip().lower()

    if choice in ["start", "settings", "exit"]:
        return choice
    else:
        print("Invalid choice. Please try again.")
        return main_menu()
    
# Adjust console size here so you can see the ASCII art better
def settings_menu():
    print("\n--- Settings ---")
    print("Resolution")
    print("Back to Main Menu")

    choice = input("> ").strip().lower()

    if choice == "resolution":
        return resolution_check()
    
    elif choice == "back":
        return main_menu()
    
    else:
        print("Invalid choice. Please try again.")
        return settings_menu()

def resolution_check():
    print("Testing ASCII resolution...")
    print()
    
    # Sample Art - Make sure you can see it clearly
    print(r"""@@@%%%%%@@@%%%%@###%%%%%###%%%%#################%%%%@#%%%@%#%%%%%%%%@@@@@@@@@@@%@%%@@@%%%@%@@@@@@@@%
@@@@%@%@@@@%##%%####%%%%##%%@@@%%###############%%#%#%%%%%%#%%@%%%%%%@%@@@@@@%%%%%@@@@%%%@%@@@@@@@%@
@%%%%%%@@%%@%#%%*#**#%%%##@@@@%################%%#%##@%%%#%#%@%@@@%#%%%@@%%@@%%%%%@@@@@%%@@@@@@@@@@@
@#@@@%%@%%%@##%#*#*##%%%%%%##%%%#*##########%#%#%##%%#%%#@#%%@@#%%%%%@@%%%%%%%%%%%@%@@%@@%@@@@@@@@@%
@%%@%@%%%@%@%@%%%##*#%@%%#####%%%###########%%#%%#%#%#%%%@%%%@@#@%%#%@@@%%%%%%%%%%%%@%%@@@@@@@@@@@@@
@@@@@@@%%@%@%@@%@%%%%@@@%#*###%%%###@%#####%%%#%%%+#%%%@%@@%@%%%##%#%@@@@%%%%%%%%%%%@%%@@@@@@@@@@@@@
@@@@@@@%%@%%@@@@%%@@@@@@@%###*@@%%##%@#%###%%%@%%%%%%%%@%%%@@%%%%%%%%%@%%%%%%%%%%%%%%@%@@@@@@@@@@@@@
%%@@@@@%@@@%#@@@@@@@@@@%%%#%%%%%@%%%%%###%%%%%@#%#%%%%%@%%#%%%%%%%%@%%%%%%%%%%%%%@@%%%@@@@@@@@@@@@@@
%%@@@@%%@@@@%%%@@@@@@@@%%#%*%%%#@%@%###%%%%%%%%%%#%%%%%%%%%%%%%%%%%%@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@
%%@%%%%@%@@@%@%@@%%@@@@%%%%##%%%##%%+###%%%%%%%%%%%%%%%%%%%%%%%%%%%@@%%%@@@@@@@@@@@@@%@@@@@@@@@@@@@@
@@@@%###%@@@%%%%@%%@@@@%%%@%#####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@%@@@@@@@@@@@@@@@@
%@@%%##+*%@@%%#@@@@%@%@%@@%%##%%%%%%%##%%%####%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@%%%@@@@@@@@@@@@@@
@%%%%#**#@@%%#####%@@#*#@@%%%##%###############%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@%%%@%%%@@@@@@@@@@@@@
@#%#%**#%%%%%%%####%####%%%%%%#############%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@%@@@@@@@@@@@@@@@@@
@%%##*#%%%%%%%%%%%#####*#####%%########%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@%%%@@@@@@@@@@@@
@@%%#*#%%%@@%@%%%%%##########%@%####%%%%%%%%##%%%%%%%%%%%%%%%%%%%%%%%%@@@@%%%%%@%%@@@%%#%@@%%@@@@@@@
@@@@%*%%%@@@@#%%#%%#%########%%%##%%%%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@%%%%%%%#%%@@%@@@@@@@@@@
@@@@@#%@%%%%%####%%#%%##%%%#%%%%%%%%%%%##%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@%%%%%%%%%%%%%%%@@@@@@@%
@@@%%@%@%########%%%%%%%#%%%%%%%%%%%%%%%%%@@@%@@@@@@@@@%%%%%%%%%%%@@@%@@@@@@@@@%%%%%%%%%%#%%%@@@@@%#
%%@#@@%%%#%#%%#%#%%%%%##%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@%%@@@@@@%%%%%%@%%%@@@@@@@%%%#%%%%#@%%@@@#@%%
@@@%%%@%%%%%%##%#####%**#%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##%@@@@@%%%%%@%%@%@%@@%%##@##
%%@#%%%%%%%%%%%%#######*+#%%%%%%%%%%@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@%###@@@@@@@%%%@@@@%@@@@@%####%
##%%%%%%#%%%@%%%###%%%%%*#@@@@@@%@@@@@@@@@@@@@@*#@@@@@@@@@@@@@@@@@@@@@#%%+@@@@@@@@@%@@#@@%@@@@%#@*##
*###%#%%###%%*#*%%%%@%%%*#@@@@@@%@@@@@@@@@@@@@#-=%@@@@@@@@@@@@@@@@@@@%%%%+@@@@@@@@%%@@%@@@@%@%#%@#%#
**+**+%%%##%####%@%@@%%%##@@@@@@@@@@@@@@@@@@%%#++#@%@@@@@@@@@@@@@@@@@@%%#+@@@@@@@@@@%@@@@@@@@%%%@#%@
+***++#%%%%%%%#%@@@@@%%@#%@@@@@@@@@@@@@@@@**+==**++*@#@@@@@@@@@@@@@@@@%@#=@@@@@@@@@@@@@@@@@%@@%%@*%@
+*#*++#%%%%%@#%%@@@@@@###@@@@@@@@@@@@@%%#*+*=+==++=##=#%@@@@@@@@@@@@@@%#**@@@@@@@@@@@@@@@@@@%%%#%#%@
*###++%%%%@%@%@#@@@@@@@@@@@@@@%########**#=*--==-=-=+*###%%%%%%%%@@@@@@@@@@@@@@@@@@@@%%@@@%%%%%%#%%@
##%%+*#%%@%%@%@#@@@@@@@@@@@@@@#=++++=+---=-+:-=##-:***+**###**#*#%@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%@#@@
#%@@*#@%%@@%@%@%@@@@@@@@@@@@@@%:.......+@%=-.-%#%%=::*@@*=======+%@@@@@@@@@@@@@@@@@%%%%*%%%%%##@#%%@
##%@*#%%%%%%%%%%%%%%%%%%%%%%%@%==+-=:-+%%##::=*###%:+%#%@*++*****%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%@#@%@
#***+**#**#%@%******+++++*##%@@+=*=+*=*#**+---@%#+*:*#*########=*%###########**######%%%%%@@%@%@@@%@
%%%%*%@@%@@%@@@#@@@%#@@@@@@@@@%::.-=-:==--=.-=#+#+#:**++***+**===#@@@@%#*+++++*####%%%%%%%@@%@@@@@%@
#%%#**+#*###%%#*#%%#=########%%:..-=..=--=-:==%+%+#:==+*+**=+*=-=#@@@@#+-====+*##%%%@@@@%@@@%@@@@@%@
@%#=#--++=++%*+*#*+*:--=+##+=*%::.--..-:.:.:==#=#**:-:==-++==+=--#@@%@#=:---=*%%%%@@@@@@@%@@@%@%@@%%
@@++*::+==++%:=+%*+*.::-=+%=-*#::....:-:::..==%+@*+:=:==-+*=++=--#@@@@%=:----#%@@%@@@@*#@%@@@%@%@@%%
%#++*::++=++#:=+%*+*.::==+#+-*#::.::::=::-..=-*=#+*--:==-++=++=--#@@@@#-:-==+%##@%@@@@#@@@%@@%@%%%%%
%#+==-:=+=*+*:=*%*++.::=+*#+-*#::.:.::=-:-:.=-%=%+*---===**=+++--*@@@@%=:--=#%%#@%@@@@@@%@%%@@@%#%##
%*=+=--=+-#*#:=*#*++.-:-+*%*-*#:. :..:=-:-:.=:=+#+=:--===**=**+=-*@@%@#=:--*#%%%@@##@##++%@%@@%%##%%
%*-#---+*=#*#:=+#*++.-:=+*#*-+#::.:::-=--=-:-======-==+++*#+***++*%%%%#*+*#%%%%%%@@%%**+*%@@%%%@##%%
**+#+++#*#*#%+*++**+-=-++++*+=+:::.::-+*+==-::-=++..:-=+*#*****++#@%%%%###%@%%@@@@@@@%###@@@%@%%##%%
***+==+*#++*#=*=-=--+++*##%#=:-**###*###=-..-*+++**+:.:==%%%%%%%%%%%%%%%%@@@@@@@@@@@%%##@@@@@#@%#*%%
+=*+++++*+#+*-==-:-++==++*%*-:-===++****=-:::--------==*##%%%%%##%@%%%@@@@@@@@@@@@@@@##*@@@@@@#%##%%
==+====++++*+-==-===:::--+%#++++==++=+*%#++++++=++++++++###%%@@@%@@@@@@@@@@@@@@@@@@@%*#*%#@%%%####%#
:-===--==**#*+**=---::=+*#@#:-:-:::-==++%@%=%%%%@%@@%=%#*#%@@@@@@@@@@@@@@@@@@@@@@@@@%++*%#%%%%%###%#
-::.    .=-*=:+=-:-*@+%@%*@#::-::-=+****%@@:@@@@@@@@@-###%@@@@@@@@@@@@@@@@@@@@@@@@@@%*=+##%%%%%%%###
===:.::..=+#+++*-+%@%-%@%*@#=*#+#==-====*%%.##***#%##.+*#%%#%@@@@@@@@@@@@@@@@@@@@@@@%#=+#%%%%%%%%##*
+++=-=+-.*%%%@%@:*@@%=%@%*@#:=%=#----===+@% ===--=*+*.+#**#%%@@@@@@@@@@@@@@@@@@@@@@@@%#*%@%%%%%@%###
++++=+==.**#*%#%.+@@%=%@%*@#:-#-#:----:.=@# =#@@%%@*= =*+*%%%@@@@@@@@@@@@@@@@@@@@@@@@@%##@@@@@@@###%
*******+.*#*+#*#.+@@%+%@%*@#:-#=#------:=%* =#**#***+.=++*#%%%@@@@@@@@@@@@@@@@@@@@@@@@@#%@@@%%%%####
##**###+-*#****%:+%@%+%@%*@#:-#-#-::---.:%+ :*+***+*+.=++**#*#%@@%@@@@@@@@@@@@@@@@@@@@@%@@@@@%%%#*#*
%#*+*#*=:+#*#*##:+###+*%#*@#--#-#-::-::.:*- :+++#=+*= =+=+**+#%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%*#*+
*#*==**-.-#+#*##-=+*+++***@#:-#=#-----:.:+- :+++*=+*+ -+==+**#%%%%%%%%%@@@@@@@@@%%@@@@@@@@%%%@@@%+*=
+*+--+*-.:#=**##:==+=+=**#@#::#=#-+*-=-.-+- :+++*++#+ -+=++***###%%%%%%%@@@@%%%%%%%%%%%%%%%%%%%%#=+-
*+=-:--- -*=+***-=+*+*++%#@#--#=#-*%#++=++- -=-=*+=*+.-+++**########%%######%%%%%%%%%%%%%%####%#+++-
=+==---: -=-=+*+::+*#+*#%%@*-:#=#=#%%=++++=.:-=:=:+++:-*##########################%%%%%%%######*+=+-
======-...=-+++===+#**#%@@@=-.*:+-*%*---=++=::::::::+==**#%#%%%#%%%#########**#######**###*#****++*-
+=----:.-==-==-=-+**+*##%#%::.*..:+**+--++-==-:+=::--==++%%%%#####%%%###############+==+*+=+###**+*=
+==:--:::=+===:::-==+****+*-::==+-******++:.:.:--....:-++##%###*###%%%%%%###########++=**+=+*###*+*+
+++-+++++=*+**=++++*****#**++==+*+***#*+==+++++++++*++**#*###%%%%######%%%##########+==**+++####*+*+
++*=*******+*#+########***#++++**+++****+++=++==++++****###%%%%%%%%##########**+======++++-=+++***#*
++*=****++*###*###*##*+*+**+++=+=:-+++++*+=-----=++=++=++*##%%%###+*#**##%%%#*#*++++==*+++---=+##***
++*+*+++****###*+++**++++=++==--=====**+*+=---:----===++*+*+++***####**#**#####*%#**++#++++++*##****
++++++*++**##%%*++++=+++===+=--=-:==+*#*#**===-::::-====++*##*#*#####****=*#####%#****#++=++***#****
++++*++=-+#**##+*===-===-=+++=+--=-===++*==+*++=::::--:-:=++***#+*+****+==++*+#+***#*##+==++********
+==++*=++*#+**#*#==+=+=+=++===+-+-==-=+*++=****+=-:::--::::--==*++++++++=++=++#=+#%%#**++=*+*+++**++
+====*****#**##**++=*++--=+++====++==+***+++***+=--::::.. ..:--==++++++=++++++*=##%%##*+++*+++++++++
+++++*####%#%%%#+***#*++==+=+*+****+**#*++++#%*+=-===--::::-:-=++++++++**#*=+=*#%%@%%#*****+**=+++*+
###**#%%%%%%%###*#*###*+++*==++=++****+#+##*%###+*+*+======*+=-=====++++**+++*##%%@#%%%%%###**+****+
%%###%%%%#%@%#%%##*####**+*++++*++*++++*##%%#%%##*=========+========+++*#+***#@%@%@%@%%%%%######***+
%@%%#%@@%%%@%#%%%%##%##+*+*****#*+++=+++#*#%##@%##==+==+==++++======++*=%%%%+@@@%%%%%%@%%%%%%####%##
@%%%%%%@@@%%#%%%%%######**+****#*+*+*+**###%%*####*++=++==++=*+======++*#@%#%%@@#@@@@@@@#%%@%%#%@@@%
%%%%%##@%%%%%%%#%%##**##*****##*#*###**##*###+#%#*++==++*=++++*=+======*#@%%%@@@@@@@@@@@%%@%@#@@%@@@
#%%%%#%%%%%%###*##########**+******#*+=**=*##**%%*+=+==+=+**+++=+*+*+*+++@@@@@@%@@@@@@@@@@@@@@@@@@@@
""")
    print()
    print("Please adjust your Terminal Font Size")
    print("Back")
    print("Main Menu")
    
    choice = input("> ").strip().lower()

    if choice == "back":
        return settings_menu()
    
    elif choice in ["main", "menu", "main menu"]:
        return main_menu()
    
    else:
        print("Invalid choice. Please try again.")
        return resolution_check()