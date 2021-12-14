from cmd import Cmd
import os
from random import randint, choice
from time import sleep

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

def safe_path(path: str):
    abs_path = os.path.abspath(os.path.join(ROOT_DIR,path))
    common_path = os.path.commonpath([ROOT_DIR, abs_path])
    if common_path == ROOT_DIR:
        return abs_path
    else:
        return os.path.abspath(ROOT_DIR + abs_path.split(common_path)[1])

class HoSH(Cmd):
    intro    = 'Welcome to HoSH! Type "help" to list commands'
    prompt   = '> '
    secret   = []
    attempts = 0

    def do_exit(self, inp: str):
        return True

    def help_exit(self):
        print('Exit HoSH with "exit".')

    def do_login(self, inp: str):
        if inp.split(' ')[0] == 'h0h0h0day-mastermind_cookies_and_flags':
            print('Bypassed!')
            p = GNLS()
            p.cmdloop()
            return False

        if self.secret == []:
            print('Generating new code...')
            self.secret = [randint(0,3), randint(0,3), randint(0,3), randint(0,3)]
            return False
        
        if self.attempts >= 10:
            print('Too many failed attempts! Generating new code...')
            self.secret = [randint(0,3), randint(0,3), randint(0,3), randint(0,3)]
            self.attempts = 0
            return False

        try:
            code = [int(x) for x in inp.split(' ')[0:4]]
        except ValueError:
            print(f'*** Unknown syntax: {inp}')
            return False

        correct = 0
        for x, y in zip(self.secret, code):
            if x == y: correct += 1

        if correct == 4:
            print('Success!')
            p = GNLS()
            p.cmdloop()
        else:
            print(f'Fail. You had {correct} digits in the right place')
            self.attempts += 1

    def help_login(self):
        print('Login to the Good/Naughty List System with "login 0 1 2 3", where the digits should be the code to login.\nThe code resets after 10 attempts.\nThe digits range from 0 to 3.\nAfter each try, you get feedback about how many digits were right, but not which one.')

    def default(self, inp: str):
        if inp == 'EOF':
            print('')
            return True
        else:
            print(f'*** Unknown syntax: {inp}')

    def emptyline(self):
        pass

class GNLS(Cmd):
    intro  = 'Some leave cookies, others leave flags: h0h0h0day-mastermind_cookies_and_flags\nYou can now login using this flag to bypass the challenge.'
    prompt = 'GNLS> '

    def do_exit(self, inp: str):
        return True

    def help_exit(self):
        print('Exit GNLS with "exit".')

    def do_show(self, inp: str):
        filename = inp.split(' ')[0]
        if filename == '':
            filename = '.'
        filename = safe_path(f'lists/{filename}')
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                for line in file:
                    line = line[:-1]
                    print(line)
        elif os.path.isdir(filename):
            files = os.listdir(filename)
            for file in files:
                print(f' - {file}')
        else:
            print(f'*** "{inp.split(" ")[0]}" not found')

    def help_show(self):
        print('Show the Good List with "show good".')
        print('Show the Naughty List with "show naughty".')

    def do_add(self, inp: str):
        if len(inp.split(' ')) == 2:
            list_name, name = inp.split(' ')[0:2]
            print(f'*** Can\'t add {name} to list {list_name}.')
        else:
            print('*** Unknown syntax: {inp}')

    def help_add(self):
        print('Add a name to a list with "add good Zuyoutoki".')

    def do_remove(self, inp: str):
        if len(inp.split(' ')) == 2:
            list_name, name = inp.split(' ')[0:2]
            print(f'*** Can\'t remove {name} from list {list_name}.')
        else:
            print('*** Unknown syntax: {inp}')

    def help_remove(self):
        print('Remove a name from a list with "remove good Zuyoutoki".')

    def do_sleep(self, inp: str):
        timeout = inp.split(' ')[0]
        if timeout.isdecimal():
            timeout = int(timeout)
        else:
            timeout = 1
        print(f'Sleeping for {timeout} seconds...')
        sleep(timeout)

    def help_sleep(self):
        print('Sleep for 5 seconds with "sleep 5".')

    def default(self, inp: str):
        if inp == 'EOF':
            print('')
            return True
        else:
            print(f'*** Unknown syntax: {inp}')

    def do_meteo(self, inp: str):
        predictions = [
                "Period of light snow ending early this evening then mainly cloudy with 30 percent chance of light snow. Temperature rising to minus 10 by morning.",
                "Cloudy. 30 percent chance of flurries this evening. Wind up to 15 km/h. Low minus 25. Risk of frostbite.",
                "Periods of snow. High minus 25. Low minus 33.",
                "Mainly cloudy. Snow beginning early this evening and ending after midnight. Amount 2 cm.",
                "A mix of sun and cloud.",
                "A few clouds. Wind southwest 20 km/h gusting to 40. Low minus 7, wind chill near minus 14."
                ]
        print(f'{choice(predictions)}')

    def help_meteo(self):
        print('Give okay meteo prediction with "meteo".')

    def do_rudolphsay(self, inp: str):
        print('                      /----------------------------------\\')
        pre  = '                      | '
        post = ' |'
        width = 32
        words = inp.split(' ')
        line = ''
        for i in range(len(words)):
            if line == '':
                line = words[i]
            else:
                if len(line + words[i]) < width:
                    line += ' ' + words[i]
                else:
                    print(pre + line + (width - len(line)) * ' ' + post)
                    line = words[i]
        if not line == '':
            print(pre + line + (width - len(line)) * ' ' + post)
        print('''           \\|/   \\|/  \----------------------------------/
             \\   /    ,
   ___   ___  \\_/    ,
  '   \'''   '-o o   ,
 /|         .- O  .'
   | |\'''| |
   | |   ||
   ||    ||
    "     "''')

    def help_rudolphsay(self):
        print('Make Rudolph say something with "rudolphsay something".')

    def emptyline(self):
        pass

def main():
    p = HoSH()
    p.cmdloop()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass

