class CipherMachine:
    def __init__(self):
        self.print_wheel = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.pin_wheels = []  # List to store pin wheel configurations
        self.bar_setups = []  # List to store bar setups for each of the 32 bars
        self.mode = None
        self.message = []
        self.pin_wheel_positions = []
        self.active_pin = [0] * 6
        self.bar_displacement = 0
        self.check_list = []
        self.check_list1 = []
        self.check_list2 = []
        self.check_list3 = []
        self.Acheck = 0
        self.Bcheck = 0
        self.Ccheck = 0
        self.pin_wheel_config = []
        self.current_setup = []
        self.bar_displacement_active = 0


        # Define predefined pin wheel configurations with active (1) and non-active (0) pins
        self.predefined_pinwheels = [
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
        [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    ]


        # Define individual bar setups here as dictionaries
        self.bar_setups = [
        {'lug': [0, 0, 0, 0, 0, 0], 'cam': ['A', '0', '0', '0', '0', '0']},
        {'lug': [0, 0, 0, 0, 0, 0], 'cam': ['B', '0', '0', '0', '0', '0']},
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

    def set_pin_wheels(self):
        # Initialize the list to store pin wheel positions as 1s and 0s
        pin_wheel_setup = []

        for i in range(6):
            while True:
                try:
                    pos = int(input(f"Enter position for Pin Wheel {i + 1} (1-47): "))
                    if 1 <= pos <= 47:
                        # Extract the corresponding pin wheel configuration
                        pin_wheel_config = self.predefined_pinwheels[i]
                        # Check if there is a 1 or 0 at the specified position
                        pin_wheel_active = pin_wheel_config[pos - 1]
                        # Append the result (1 or 0) to the pin_wheel_setup list
                        pin_wheel_setup.append(pin_wheel_active)

                        self.current_setup.append(pos)
                        break
                    else:
                        print("Invalid position. Please enter a number between 1 and 47.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 47.")


        # Ensure that exactly 6 positions were entered
        if len(pin_wheel_setup) == 6:
            # Store the pin wheel positions as 1s and 0s
            self.pin_wheels_0 = pin_wheel_setup

            print("Pin Wheel Setup:")
            print(self.pin_wheels_0)
            return
        else:
            print("Invalid number of positions entered. Please enter exactly 6 positions between 1 and 47.")
            return  # Added return statement to exit the function

    def shift_bars(self):
        self.active_pin = self.pin_wheels_0
        # Check if each bar should be displaced based on lug and pin wheel configurations
        for i in range(32):
            new_pin_wheels = self.current_setup
            for j in range(6):
                lug = self.bar_setups[i]['lug'][j]
                pin_wheel_active = self.active_pin [j]
                cam_type = self.bar_setups[i]['cam'][j]

                self.check_list1.append(lug)
                self.check_list2.append(cam_type)
                self.check_list3.append(pin_wheel_active)

                # Advance the pin wheel based on the cam type
                if cam_type == 'A' and lug == 1 and pin_wheel_active == 1:
                    new_pin_wheels[j] = (new_pin_wheels[j] + 1) % 47
                    self.Acheck += 1

                if cam_type == 'B' and (lug != 1 or pin_wheel_active != 1):
                    new_pin_wheels[j] = (new_pin_wheels[j] + 1) % 47
                    self.Bcheck += 1 

                if cam_type == 'C':
                    new_pin_wheels[j] = (new_pin_wheels[j] + 1) % 47
                    self.Ccheck += 1 

                if lug == 1 and pin_wheel_active == 1: 
                    self.bar_displacement += 1  #here is the main problem.... the addition goes all the way up to 29 sometimes. there are 32 bars though. impossible.
                self.bar_displacement_active = self.bar_displacement 
                self.pin_wheels = new_pin_wheels
                self.current_setup = self.pin_wheels
                self.active_pin = [self.predefined_pinwheels[j][pos - 1] for j, pos in enumerate(self.pin_wheels)]
                
        print(self.Acheck)
        print(self.Bcheck)
        print(self.Ccheck)
        self.bar_displacement = 0
        return self.bar_displacement_active, self.pin_wheels, self.current_setup, self.check_list, self.check_list1, self.check_list2, self.check_list3, self.Acheck, self.Bcheck, self.Ccheck  # Return the bar displacement status after processing all bars



        # Return the bar displacement status

    def encrypt_letter(self, letter):
        if letter.isalpha():
            letter = letter.upper()

            # Determine if any bar should be displaced based on the current pin wheel positions
            self.shift_bars()
            # Encrypt the letter by adding the displacement to the print wheel
            encrypted_char = self.print_wheel[(self.print_wheel.index(letter) + self.bar_displacement_active) % 26]
            print("selfbar",self.bar_displacement_active)
            #print("lug", self.check_list1)
            #print("cam type", self.check_list2) 
            #print("pinwheelactive", self.check_list3)
            #print("a", self.Acheck)
            #print("b", self.Bcheck)
            #print("c: ", self.Ccheck)
            # Update the pin wheel positions based on the presence of pins and lug configuration


            return encrypted_char 
        else:
            return letter


    
    def decrypt_letter(self, letter):
        if letter.isalpha():
            letter = letter.upper()
            self.shift_bars()
            decrypted_char = self.print_wheel[(self.print_wheel.index(letter) - self.bar_displacement_active) % 26]
            return decrypted_char
        else:
            return letter


    def process_message(self, message):
        result = ''

        for char in message:
            if self.mode == 'encrypt':
                result += self.encrypt_letter(char)
                print("Pin Wheel Positions After Letter:", self.pin_wheels)
            elif self.mode == 'decrypt':
                result += self.decrypt_letter(char)
                print("Pin Wheel Positions After Letter:", self.pin_wheels)
            else: 
                print("error")
        return result



    def run(self):
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

        self.set_pin_wheels()

        if self.mode == 'encrypt':
            message = input("Enter the message (single letter at a time, '<' to finish): ")
            while message != '<':
                self.message.append(message)
                message = input("Enter the next letter (or '<' to finish): ")
            encrypted_message = self.process_message(''.join(self.message))
            print("Encrypted Message:", encrypted_message)
        elif self.mode == 'decrypt':
            encrypted_message = input("Enter the encrypted message (single letter at a time, '<' to finish): ")
            while encrypted_message != '<':
                self.message.append(encrypted_message)
                encrypted_message = input("Enter the next letter (or '<' to finish): ")
            decrypted_message = self.process_message(''.join(self.message))
            print("Decrypted Message:", decrypted_message)

# Example usage:
cipher_machine = CipherMachine()
cipher_machine.run()