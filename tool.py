import os
import sys
import platform
import subprocess
import pandas as pd
from datetime import datetime
from colorama import init, Fore

init()


def pre_setup():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.YELLOW + "Select Counseling type:")
    print(Fore.GREEN + "1." + Fore.BLUE + "JOSAA")
    print(Fore.GREEN + "2." + Fore.BLUE + "CSAB" + Fore.RESET)
    option = input("Select Option (1 to 2) : ")
    if option == '1':
        josaa_rounds()
    elif option == '2':
        csab_rounds()
    else :
        pre_setup()


def josaa_rounds():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.YELLOW + "Select JOSAA round (2022)")

    menu_options = [
        "Round 1",
        "Round 2",
        "Round 3",
        "Round 4",
        "Round 5",
        "Round 6"
    ]

    for i, option in enumerate(menu_options, start=1):
        print(f"{Fore.GREEN}{i}. {Fore.RESET}{Fore.BLUE}{option}" + Fore.RESET)

    selected_round = input("Select Option (1 to 6): ")
    if int(selected_round) > 6:
        return josaa_rounds()  # Return the function call instead of directly calling it
    csv_files("josaa", selected_round)



def csab_rounds():
    os.system("cls" if os.name == "nt" else "clear")
    print("Select CSAB round (2022)")
    print(Fore.GREEN + "1." + Fore.BLUE + "Round 1")
    print(Fore.GREEN + "2." + Fore.BLUE + "Round 2")
    csab_round = input(Fore.RESET + "Select Option (1 to 2) : ")
    csv_files("csab", csab_round)

# define the path of csv files for different types of colleges


def csv_files(type, round):
    # Get path to the temporary folder created by PyInstaller
    if getattr(sys, 'frozen', False):
        # If the script is running in a PyInstaller bundle
        cwd = sys._MEIPASS
    else:
        # If the script is running from the original Python file
        cwd = os.getcwd()
    if type == "josaa":
        josaa_rounds = round
        CSV_FILES = {
            "ALL": os.path.join(cwd, "josaa", "2022", f"round_{josaa_rounds}", "ranks_all.csv"),
            "IIITs": os.path.join(cwd, "josaa", "2022", f"round_{josaa_rounds}", "ranks_iiits.csv"),
            "IITs": os.path.join(cwd, "josaa", "2022", f"round_{josaa_rounds}", "ranks_iits.csv"),
            "NITs": os.path.join(cwd, "josaa", "2022", f"round_{josaa_rounds}", "ranks_nits.csv"),
            "GFTIs": os.path.join(cwd, "josaa", "2022", f"round_{josaa_rounds}", "ranks_gftis.csv")
        }
        josaa_institue_types(CSV_FILES)
    elif type == "csab":
        csab_rounds = round
        csv_path = os.path.join(
            cwd,
            "csab",
            "2022",
            f"round_{csab_rounds}",
            "ranks.csv")
        df = pd.read_csv(csv_path)
        csab_institue_types(df)


def csab_institue_types(df):
    # clear the screen
    os.system("cls" if os.name == "nt" else "clear")

    # ask for user input for institute type
    print("Select Institute type:")
    print(Fore.GREEN + "1." + Fore.BLUE + "ALL (No IITs Included)")
    print(Fore.GREEN + "2." + Fore.BLUE + "IIITs")
    print(Fore.GREEN + "3." + Fore.BLUE + "NITs")
    print(Fore.GREEN + "4." + Fore.BLUE + "GFTIs")
    print(Fore.GREEN + "5." + Fore.BLUE + "IITs")
    option = input(Fore.RESET + "Select Option (1 to 5): ")

    # filter the dataframe based on the selected option
    if option == "1":
        df = df[~df['Institute'].str.contains(
            'Indian Institute of Technology')]
    elif option == "2":
        df = df[df['Institute'].str.contains(
            'Indian Institute of Information Technology')]
    elif option == "3":
        df = df[df['Institute'].str.contains(
            'National Institute of Technology')]
    elif option == "4":
        df = df[~df['Institute'].str.contains(
            'National Institute of Technology')]
        df = df[~df['Institute'].str.contains(
            'Indian Institute of Information Technology')]
        df = df[~df['Institute'].str.contains(
            'Indian Institute of Technology')]
    elif option == "5":
        df = df[df['Institute'].str.contains(
            'Indian Institute of Technology')]
    else:
        print("Invalid option. Please select again.")

    main(df)


def josaa_institue_types(CSV_FILES):
    # clear the screen
    os.system("cls" if os.name == "nt" else "clear")

    # ask for user input for institute type
    print("Select Institute type:")
    print(Fore.GREEN + "1." + Fore.BLUE + "ALL (No IITs Included)")
    print(Fore.GREEN + "2." + Fore.BLUE + "IIITs")
    print(Fore.GREEN + "3." + Fore.BLUE + "NITs")
    print(Fore.GREEN + "4." + Fore.BLUE + "GFTIs")
    print(Fore.GREEN + "5." + Fore.BLUE + "IITs")
    option = input(Fore.RESET + "Select Option (1 to 5): ")

    # filter the dataframe based on the selected option
    if option == "1":
        college_type = "ALL"
    elif option == "2":
        college_type = "IIITs"
    elif option == "3":
        college_type = "NITs"
    elif option == "4":
        college_type = "GFTIs"
    elif option == "5":
        college_type = "IITs"
    else:
        print("Invalid option. Please select again.")
        josaa_institue_types

    # read the csv file based on the selected college type
    csv_path = CSV_FILES[college_type]
    df = pd.read_csv(csv_path)
    if option == "1":
        # Remove all IITs occurance if "ALL" option was choosed.
        df = df[~df['Institute'].str.contains(
            'Indian Institute of Technology')]
        main(df)
    elif option == "5":
        # fix ranks with strings in it.
        df['Closing Rank'] = df['Closing Rank'].str.extract(
            r'(\d+)').astype(float)
        df['Opening Rank'] = df['Opening Rank'].str.extract(
            r'(\d+)').astype(int)
        main(df)
    else:
        main(df)

def filter_programs(institute_df):
    print("Note: Programs marked with '*' will display all the programs similar to them.")
    print("Select Program:")
    print(Fore.GREEN + "1." + Fore.BLUE + "All")
    print(Fore.GREEN + "2." + Fore.BLUE + "Computer Science and Engineering*")
    print(Fore.GREEN + "3." + Fore.BLUE + "Artificial Intelligence and Data Science*")
    print(Fore.GREEN + "4." + Fore.BLUE + "Electronics and Communication Engineering*")
    print(Fore.GREEN + "5." + Fore.BLUE + "Information Technology*")
    print(Fore.GREEN + "6." + Fore.BLUE + "Mechanical Engineering*")
    print(Fore.GREEN + "7." + Fore.BLUE + "Civil Engineering*")
    print(Fore.GREEN + "8." + Fore.BLUE + "Electrical Engineering*")
    print(Fore.GREEN + "9." + Fore.BLUE + "Data Science and Engineering*")
    print(Fore.GREEN + "10." + Fore.BLUE + "Biotechnology*")
    print(Fore.GREEN + "11." + Fore.BLUE + "Chemical Engineering*")
    print(Fore.GREEN + "12." + Fore.BLUE + "Smart Manufacturing*")
    print(Fore.GREEN + "13." + Fore.YELLOW + "Check Next Page" + Fore.RESET)
    print("")

    program_choices = {
        1: '',
        2: 'Computer Science and Engineering',
        3: 'Artificial Intelligence and Data Science',
        4: 'Electronics and Communication Engineering',
        5: 'Information Technology',
        6: 'Mechanical Engineering',
        7: 'Civil Engineering',
        8: 'Electrical Engineering',
        9: 'Data Science and Engineering',
        10: 'Biotechnology',
        11: 'Chemical Engineering',
        12: 'Smart Manufacturing'
    }

    program_input = input("Choose Option(s) (separated by space): ")
    program_choices_list = program_input.split()

    filtered_df = institute_df

    if '1' not in program_choices_list:
        filtered_df = institute_df[institute_df["Academic Program Name"].str.contains(
            '|'.join([program_choices.get(int(choice), '') for choice in program_choices_list]))]

    if len(filtered_df) == 0:
        print(Fore.RED + "No programs found matching the selected options." + Fore.RESET)
        return filtered_df

    if '13' in program_choices_list:
        os.system("cls" if os.name == "nt" else "clear")
        programs = filtered_df["Academic Program Name"].unique()
        for i, program in enumerate(programs, start=14):
            print(f"{Fore.GREEN}{i}. {Fore.BLUE}{program}{Fore.RESET}")
        program_choice = int(input("Choose Option: "))
        if program_choice >= 14 and program_choice < 14 + len(programs):
            program = programs[program_choice - 14]
            filtered_df = filtered_df[filtered_df["Academic Program Name"] == program]
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Fore.RESET)
            return filtered_df

    return filtered_df



def display_df_web(df):
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # create a unique filename based on the current date and time
    filename = os.path.join(
        output_dir,
        f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html")

    # convert the DataFrame to an HTML table and save it to the file
    html = df.to_html()
    with open(filename, "w") as file:
        file.write(html)
    print(filename)
    # open the file in the default web browser

    if platform.system() == "Windows":
        subprocess.Popen(["start",
                          filename],
                         stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL,
                         shell=True)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", filename],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.Popen(["xdg-open", filename],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# main function to run the CLI tool
def main(df):
    while True:
        institute_df = df
        os.system("cls" if os.name == "nt" else "clear")
        filtered_df = filter_programs(institute_df)

        def filter_by_choice(choices, column_name):
            unique_choices = institute_df[column_name].unique()
            num_choices = len(unique_choices)
            start_index = 0
            batch_size = 15

            while start_index < num_choices:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Select {column_name} :")
                print(Fore.GREEN + "1." + Fore.BLUE + " All")
                end_index = start_index + batch_size
                current_choices = unique_choices[start_index:end_index]

                for i, choice in enumerate(
                        current_choices, start=start_index + 2):
                    print(f"{Fore.GREEN}{i}. {Fore.BLUE}{choice}{Fore.RESET}")

                if end_index < num_choices:
                    print(f"{Fore.GREEN}{end_index+2}. Next {batch_size}")

                if start_index > 0:
                    print(f"{Fore.GREEN}{end_index+3}. Return to Last Page")

                choice = int(input("Choose Option : "))

                if choice == end_index + 2 and end_index < num_choices:
                    start_index = end_index
                elif choice == end_index + 3 and start_index > 0:
                    start_index -= batch_size
                elif choice != 1:
                    selected_choice = unique_choices[choice - 2]
                    return filtered_df[filtered_df[column_name]
                                       == selected_choice]
                else:
                    return filtered_df
            return filtered_df

        filtered_df = filter_by_choice(institute_df["Institute"], "Institute")
        filtered_df = filter_by_choice(institute_df["Quota"], "Quota")
        filtered_df = filter_by_choice(institute_df["Seat Type"], "Seat Type")
        filtered_df = filter_by_choice(institute_df["Gender"], "Gender")

        os.system("cls" if os.name == "nt" else "clear")
        rank = int(input(Fore.YELLOW + "Enter your rank: " + Fore.RESET))
        filtered_df["Closing Rank"] = filtered_df["Closing Rank"].astype(
            str).str.extract(r"(\d+)").astype(int)
        filtered_df = filtered_df[filtered_df["Closing Rank"] > rank].sort_values(
            by=["Closing Rank"], ascending=True)

        os.system("cls" if os.name == "nt" else "clear")
        display_df_web(filtered_df)
        print(
            Fore.GREEN +
            "Congratulations! File successfully opened in browser." +
            Fore.RESET)
        print("")
        choice = input(
            f"Press Enter to continue or type {Fore.YELLOW}'exit'{Fore.RESET} to exit: ")
        if choice.lower() == "exit":
            break


# run the main function
pre_setup()
