import sys, time, random, os
from time import sleep
import threading

class PackageOSBase:
    def __init__(self):
        pass

    def progress_bar(self, count_value, total, suffix=''):
        bar_length = 50  # Adjusted for better visibility
        filled_up_length = int(round(bar_length * count_value / float(total)))
        percentage = round(100.0 * count_value / float(total), 1)
        bar = '=' * filled_up_length + '-' * (bar_length - filled_up_length)
        sys.stdout.write('\r[%s] %s%s %s' % (bar, percentage, '%', suffix))
        sys.stdout.flush()

    def loading_screen(self, log_file):
        screen = """
                    ██████╗  █████╗  ██████╗██╗  ██╗ █████╗  ██████╗ ███████╗
                    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔════╝ ██╔════╝
                    ██████╔╝███████║██║     █████╔╝ ███████║██║  ███╗█████╗  
                    ██╔═══╝ ██╔══██║██║     ██╔═██╗ ██╔══██║██║   ██║██╔══╝  
                    ██║     ██║  ██║╚██████╗██║  ██╗██║  ██║╚██████╔╝███████╗
                    ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═════╝ ╚══════╝
        """
        print(screen)
        for i in range(11):
            time.sleep(random.random())  # Simulate task
            self.progress_bar(i, 10, "loaded")
        print()  # Move to the next line after the progress bar is complete
        sleep(1)  # Short sleep to allow the user to see the completed progress bar
        os.system('clear' if os.name == 'posix' else 'cls')
        print("Loading completed successfully\nPress 'c' for a command line or 'e' to edit")

        def get_input():
            return input().lower()

        input_thread = threading.Thread(target=get_input)
        input_thread.start()
        input_thread.join(timeout=2)

        if input_thread.is_alive():
            print("\nTime's up! No input received.")
        else:
            user_input = get_input()
            if user_input == 'c':
                print("Opening command line...")
                os.system(os.environ['SHELL'])
            elif user_input == 'e':
                print("Opening editor...")
                # Add your editor opening logic here
            else:
                print("Invalid input. Please press 'c' for a command line or 'e' to edit")

# Example usage
if __name__ == "__main__":
    package_os_base = PackageOSBase()
    package_os_base.loading_screen("logfile.txt")




