import sys, time, random, os
from time import sleep

def progressBar(count_value, total, suffix=''):
        bar_length = 100
        filled_up_Length = int(round(bar_length* count_value / float(total)))
        percentage = round(100.0 * count_value/float(total),1)
        bar = '=' * filled_up_Length + '-' * (bar_length - filled_up_Length)
        sys.stdout.write('[%s] %s%s %s\r' %(bar, percentage, '%', suffix))
        sys.stdout.flush()
def loadingScreen(logFile):
    screen = """
                    ██████╗  █████╗  ██████╗██╗  ██╗ █████╗  ██████╗ ███████╗
                    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔════╝ ██╔════╝
                    ██████╔╝███████║██║     █████╔╝ ███████║██║  ███╗█████╗  
                    ██╔═══╝ ██╔══██║██║     ██╔═██╗ ██╔══██║██║   ██║██╔══╝  
                    ██║     ██║  ██║╚██████╗██║  ██╗██║  ██║╚██████╔╝███████╗
                    ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
    """
    print(screen)
    shell = os.environ['SHELL']
    for i in range(11):
        time.sleep(random.random()) #task to do
        progressBar(i,10, "loaded") 
    sleep(500)
    if shell == "/bin/bash":
        os.system("clear")
    else:
        os.system("cls")



        
loadingScreen(None)

print(os.environ['SHELL'])
        




