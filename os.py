# This was annoying to make  i dont know why i made this
#!/usr/bin/env python
print ("Check out the #README in the dir you cloned this into for all the avalible options and distros \n")
import subprocess
call = subprocess.call

fetch = input("What do you want for a fetch? \n")

if fetch == "big":
    call("neofetch", shell=True)
elif fetch == "small":
    call('ufetch')
elif fetch == "arch":
    call('neofetch --ascii_distro arch', shell=True)
elif fetch == "arch cow":
    call('neofetch --ascii "$(cowsay i use arch btw :D)"', shell=True)
elif fetch == "rainbow":
    call('neofetch | lolcat', shell=True)
elif fetch == "small rainbow":
    call('ufetch | lolcat', shell=True)
elif fetch == "gentoo":
    call('neofetch --ascii_distro gentoo', shell=True)
elif fetch == "gentoo small":
    call('neofetch --ascii_distro gentoo_small', shell=True)
elif fetch == "gentoo rainbow":
    call('neofetch --ascii_distro gentoo | lolcat', shell=True)
elif fetch == 'gentoo small rainbow':
    call('neofetch --ascii_distro gentoo_small | lolcat', shell=True)
elif fetch == 'nixos':
    call('neofetch --ascii_distro nixos', shell=True)
elif fetch == 'nixos small':
    call('neofetch --ascii_distro nixos_small', shell=True)
elif fetch == 'suse':
    call('neofetch --ascii_distro opensuse', shell=True)
elif fetch == 'kali':
    call('neofetch --ascii_distro kali', shell=True)
elif fetch == 'kali rainbow':
    call('neofetch --ascii_distro kali | lolcat', shell=True)
elif fetch == 'void':
    call('neofetch --ascii_distro void', shell=True)
elif fetch == 'void small':
    call('neofetch --ascii_distro void_small', shell=True)
elif fetch == 'void small rainbow':
    call('neofetch --ascii_distro void_small | lolcat', shell=True)
elif fetch == 'void rainbow':
    call('neofetch --ascii_distro void | lolcat', shell=True)
elif fetch == 'bedrock':
    call('neofetch --ascii_distro bedrock', shell=True)
elif fetch == 'bedrock rainbow':
    call('neofetch --ascii_distro bedrock | lolcat', shell=True)
elif fetch == 'slackware':
    call('neofetch --ascii_distro slackware', shell=True)
else:
    call('exit', shell=True)
    print ("Wrong command. Rerun the script.")
