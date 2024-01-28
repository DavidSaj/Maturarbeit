class CipherMachine:
    def __init__(self):
        self.printwheel = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.pinwheels = []  # List to store pin wheel configurations
        self.barsetups1 = []  # List to store bar setups for each of the 32 bars
        self.mode = None
        self.message = []
        self.inputmessage2 = []
        self.pinwpos = []
        self.activepin = [0] * 6
        self.totalbardisplacement = 0
        self.check_list = []
        self.check_list1 = []
        self.check_list2 = []
        self.check_list3 = []
        self.Acheck = 0
        self.Bcheck = 0
        self.Ccheck = 0
        self.pinwheelconfig = []
        self.selfdefinedsetup = []
        self.activebardisplacements = 0

        # check icecream for loging test


        # Here you can define the active pins
        self.predefpinwheels = [
        [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
        [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    ]


        # The lesft is for the lug placement and right for the cam types on the bar. 
        self.barsetups1 = [
        {'lug': [0, 0, 0, 0, 0, 0], 'cam': ['A', '0', '0', '0', '0', '0']},
        {'lug': [1, 0, 0, 0, 0, 0], 'cam': ['B', '0', '0', '0', '0', '0']},
        {'lug': [1, 0, 0, 0, 0, 0], 'cam': ['0', 'A', '0', '0', '0', '0']},
        {'lug': [1, 0, 0, 0, 0, 0], 'cam': ['0', 'B', '0', '0', '0', '0']},
        {'lug': [1, 0, 0, 0, 0, 0], 'cam': ['0', '0', 'A', '0', '0', '0']},
        {'lug': [0, 1, 0, 0, 0, 0], 'cam': ['0', '0', 'B', '0', '0', '0']},
        {'lug': [0, 1, 0, 0, 0, 0], 'cam': ['0', '0', '0', 'A', '0', '0']},
        {'lug': [0, 1, 0, 0, 0, 0], 'cam': ['0', '0', '0', 'B', '0', '0']},
        {'lug': [0, 1, 0, 0, 0, 0], 'cam': ['A', '0', '0', '0', 'A', '0']},
        {'lug': [0, 1, 0, 0, 0, 0], 'cam': ['0', '0', '0', '0', 'B', '0']},
        {'lug': [0, 0, 1, 0, 0, 0], 'cam': ['0', '0', '0', '0', '0', 'A']},
        {'lug': [0, 0, 1, 0, 0, 0], 'cam': ['A', '0', '0', '0', '0', 'B']},
        {'lug': [0, 0, 1, 0, 0, 0], 'cam': ['0', '0', '0', '0', '0', '0']},
        {'lug': [0, 0, 1, 0, 0, 0], 'cam': ['A', 'A', 'A', 'A', 'A', 'A']},
        {'lug': [0, 0, 1, 0, 0, 0], 'cam': ['C', 'C', 'C', 'C', 'C', 'C']},
        {'lug': [0, 0, 0, 0, 0, 0], 'cam': ['0', '0', '0', '0', '0', '0']},
        {'lug': [0, 1, 0, 0, 0, 0], 'cam': ['C', '0', '0', '0', '0', '0']},
        {'lug': [0, 0, 0, 1, 0, 0], 'cam': ['0', '0', '0', '0', '0', '0']},
        {'lug': [0, 0, 0, 1, 0, 0], 'cam': ['0', 'A', '0', '0', '0', '0']},
        {'lug': [0, 0, 0, 1, 0, 0], 'cam': ['0', 'A', '0', '0', '0', '0']},
        {'lug': [0, 0, 0, 0, 1, 0], 'cam': ['A', 'A', 'C', 'A', '0', '0']},
        {'lug': [0, 0, 0, 0, 1, 0], 'cam': ['0', '0', 'B', '0', '0', '0']},
        {'lug': [0, 0, 0, 0, 0, 0], 'cam': ['0', '0', 'A', '0', '0', '0']},
        {'lug': [0, 0, 0, 0, 0, 0], 'cam': ['0', '0', '0', '0', '0', '0']},
        {'lug': [0, 0, 0, 0, 0, 0], 'cam': ['0', '0', '0', '0', '0', '0']},
        {'lug': [0, 0, 0, 0, 0, 1], 'cam': ['0', '0', '0', 'A', '0', '0']},
        {'lug': [0, 0, 0, 0, 0, 0], 'cam': ['0', 'C', '0', '0', '0', '0']},
        {'lug': [0, 0, 0, 0, 0, 0], 'cam': ['0', '0', '0', '0', 'A', 'A']},
        {'lug': [0, 0, 0, 0, 0, 0], 'cam': ['0', '0', '0', '0', '0', 'B']},
        {'lug': [0, 0, 0, 0, 0, 0], 'cam': ['0', '0', '0', 'B', '0', '0']},
        {'lug': [0, 0, 0, 0, 0, 1], 'cam': ['0', '0', 'A', '0', '0', '0']},
        {'lug': [0, 0, 0, 0, 0, 1], 'cam': ['A', '0', '0', 'A', 'B', '0']},
    ]

    def setpinofpinwheels(self):
        setup = []
        for g in range(6):
            while True:
                try:
                    x = int(input(f"Enter position for Pin Wheel {g + 1} (1-47): "))
                    if 1 <= x <= 47:
                        pinwheelconfig = self.predefpinwheels[g]
                        activepin = pinwheelconfig[x - 1]
                        setup.append(activepin)
                        self.selfdefinedsetup.append(x)
                        break
                    else:
                        print("Invalid position")
                except ValueError:
                    print("Invalid input")

        if len(setup) == 6:
            self.pinwheelsstart = setup 
            self.activepin = self.pinwheelsstart

            print("Pin Wheel Setup:")
            print(self.pinwheelsstart)
            return
        else:

            print("Invalid number of positions entered. Please enter exactly 6 positions between 1 and 47.") 


    def shiftbars(self):
        for g in range(32):
            updatedpinwheels = self.selfdefinedsetup

            for h in range(6):
                lug = self.barsetups1[g]['lug'][h]
                activitycheck = self.activepin[h]
                cam_type = self.barsetups1[g]['cam'][h]
                
                self.check_list1.append(lug)
                self.check_list2.append(cam_type)
                self.check_list3.append(activitycheck)
                # Advance the pin wheel based on the cam type
                if cam_type == 'A' and lug == 1 and activitycheck == 1:
                    updatedpinwheels[h] = (updatedpinwheels[h] + 1) % 47
                    self.Acheck += 1

                if cam_type == 'B' and (lug != 1 or activitycheck != 1): 
                    updatedpinwheels[h] = (updatedpinwheels[h] + 1) % 47
                    self.Bcheck += 1 

                if cam_type == 'C':
                    updatedpinwheels[h] = (updatedpinwheels[h] + 1) % 47
                    self.Ccheck += 1 

                if lug == 1 and activitycheck == 1: 
                    self.totalbardisplacement += 1  #here is the main problem.... 
                self.activebardisplacements = self.totalbardisplacement 
                self.pinwheels = updatedpinwheels
                self.selfdefinedsetup = self.pinwheels
                self.activepin = [self.predefpinwheels[h][x - 1] \
                                   for h, x in enumerate(self.pinwheels)]
                
                

                
        print(self.Acheck)
        print(self.Bcheck)
        print(self.Ccheck)
        self.totalbardisplacement = 0
        return self.activebardisplacements, self.pinwheels, self.selfdefinedsetup, self.check_list, self.check_list1, self.check_list2, self.check_list3, self.Acheck, self.Bcheck, self.Ccheck  # Return the bar displacement status after processing all bars




    def encrypt(self, letter):

        letter = letter.upper()
        self.shiftbars()
        encrypted_char = self.printwheel[(self.printwheel.index(letter) + \
                                          self.activebardisplacements) % 26]
        print("selfbar",self.activebardisplacements)
        return encrypted_char 



    
    def decrypt(self, letter):
        letter = letter.upper()
        self.shiftbars()
        decrypted_char = self.printwheel[(self.printwheel.index(letter) - \
                                          self.activebardisplacements) % 26]
        return decrypted_char


    def inputmessage(self, message):
        result = ''
        for char in message:
            if self.mode == 'encrypt':
                result += self.encrypt(char)
                print("Pin Wheel Positions After Letter:", self.pinwheels)
            elif self.mode == 'decrypt':
                result += self.decrypt(char)
                print("Pin Wheel Positions After Letter:", self.pinwheels)
            else: 
                print("error")
        return result



    def run(self, startpos:[0] * 6 = None, mode: str = None, msg:[] = None):
        
        if mode : self.mode = mode
        else:
            while True:
                action = input("Do you want to encrypt or decrypt? (e/d): ")
                if action.lower() == 'e':
                    self.mode = 'encrypt'
                    break
                elif action.lower() == 'd':
                    self.mode = 'decrypt'
                    break
                else:
                    print("Invalid input. Please enter 'e' for encrypt or 'd' for decrypt.")

        if startpos:
            self.selfdefinedsetup = startpos
        else: 
            self.setpinofpinwheels()

        if self.mode == 'encrypt':
            if msg:
                message = msg
            else:
                message = input("Enter the message (single letter at a time, '<' to finish): ")
                while message != '<':
                    self.message.append(message)
                    message = input("Enter the next letter (or '<' to finish): ")
            encryptedmessage = self.inputmessage(''.join(self.message))
            print("Encrypted Message:", encryptedmessage)
        elif self.mode == 'decrypt':
            if msg:
                message = msg
            else:
                encryptedmessage = input("Enter the encrypted message \
                                        single letter at a time, '<' to finish): ")
                while encryptedmessage != '<':
                    self.message.append(encryptedmessage)
                    encryptedmessage = input("Enter the next letter (or '<' to finish): ")
            decrypted_message = self.inputmessage(''.join(self.message))
            print("Decrypted Message:", decrypted_message)

# Example usage:
cipher_machine = CipherMachine()
cipher_machine.run()