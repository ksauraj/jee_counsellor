import os
import platform
import pandas as pd
from datetime import datetime
import subprocess

def pre_setup():
    os.system("cls" if os.name == "nt" else "clear")
    print("Select Counseling type:")
    print("1. JOSAA")
    print("2. CSAB")
    option = input("Select Option (1 to 2) : ")
    if option == '1':
        josaa_rounds()
    else:
        csab_rounds()

def josaa_rounds():
    os.system("cls" if os.name == "nt" else "clear")
    print("Select JOSAA round (2022)")
    print("1. Round 1")
    print("2. Round 2")
    print("3. Round 3")
    print("4. Round 4")
    print("5. Round 5")
    print("6. Round 6")
    josaa_rounds = input("Select Option (1 to 6) : ")
    csv_files("josaa", josaa_rounds)

def csab_rounds():
    os.system("cls" if os.name == "nt" else "clear")
    print("Select CSAB round (2022)")
    print("1. Round 1")
    print("2. Round 2")
    csab_round = input("Select Option (1 to 2) : ")
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
    if type == "josaa" :
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
        csv_path = os.path.join(cwd, "csab", "2022", f"round_{csab_rounds}", "ranks.csv")
        df = pd.read_csv(csv_path)
        main(df)

def josaa_institue_types(CSV_FILES):
    # clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    
    # ask for user input for institute type
    print("Select Institute type:")
    print("1. ALL")
    print("2. IIITs")
    print("3. NITs")
    print("4. GFTIs")
    print("5. IITs")
    option = input("Select Option (1 to 5): ")
    
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
    main(df)


def display_df_web(df):
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # create a unique filename based on the current date and time
    filename = os.path.join(output_dir, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html")

    # convert the DataFrame to an HTML table and save it to the file
    html = df.to_html()
    with open(filename, "w") as file:
        file.write(html)
    print(filename)
    # open the file in the default web browser

    if platform.system() == "Windows":
        subprocess.Popen(["start", filename], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", filename], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.Popen(["xdg-open", filename], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# main function to run the CLI tool
def main(df):
    while True:
        institute_df = df
        os.system("cls" if os.name == "nt" else "clear")
        print("Note, Program marked with '*' will display all the programs which is similar to it.")
        print("Select Program :")
        print("1. All")
        print("2. Computer Science and Engineering*")
        print("3. Artificial Intelligence and Data Sciene*")
        print("4. Electronics and Communication Engineering*")
        print("5. Information Technology*")
        print("6. Mechanical Engineering*")
        print("7. Civil Engineering*")
        print("8. Electrical Engineering*")
        print("9. Data Science and Engineering*")
        print("10. Biotechnology*")
        print("11. Chemical Engineering*")
        print("12. Smart Manufacturing*")
        print("13. Check Next Pagee")
        print("0. For next page")
        print("")
        program_choice = int(input("Choose Option : "))
        

        if program_choice == 1:
            filtered_df = institute_df
        elif program_choice == 2:
            program_regex = "Computer Science.*"
            filtered_df = institute_df[institute_df["Academic Program Name"].str.contains(program_regex)]
            
        elif program_choice == 3:
            program_regex = "Artificial Intelligence and Data Science.*"
            filtered_df = institute_df[institute_df["Academic Program Name"].str.contains(program_regex)]
            
        elif program_choice == 4:
            program_regex = "Electronics and Communication Engineering.*"
            filtered_df = institute_df[institute_df["Academic Program Name"].str.contains(program_regex)]
            
        elif program_choice == 5:
            program_regex = "Information Technology.*"
            filtered_df = institute_df[institute_df["Academic Program Name"].str.contains(program_regex)]
            
        elif program_choice == 6:
            program_regex = "Mechanical Engineering.*"
            filtered_df = institute_df[institute_df["Academic Program Name"].str.contains(program_regex)]
            
        elif program_choice == 7:
            program_regex = "Civil Engineering.*"
            filtered_df = institute_df[institute_df["Academic Program Name"].str.contains(program_regex)]
            
        elif program_choice == 8:
            program_regex = "Electrical Engineering.*"
            filtered_df = institute_df[institute_df["Academic Program Name"].str.contains(program_regex)]
            
        elif program_choice == 9:
            program_regex = "Data Science and Engineering.*"
            filtered_df = institute_df[institute_df["Academic Program Name"].str.contains(program_regex)]

        elif program_choice == 10:
            program_regex = "Biotechnology.*"
            filtered_df = institute_df[institute_df["Academic Program Name"].str.contains(program_regex)]

        elif program_choice == 11:
            program_regex = "Chemical Engineering*.*"
            filtered_df = institute_df[institute_df["Academic Program Name"].str.contains(program_regex)]
        
        elif program_choice == 12:
            program_regex = "Smart Manufacturing.*"
            filtered_df = institute_df[institute_df["Academic Program Name"].str.contains(program_regex)]
        
        elif program_choice == 0:
            os.system("cls" if os.name == "nt" else "clear")
            programs = institute_df["Academic Program Name"].unique()
            for i, program in enumerate(programs, start=14):
                print(f"{i}. {program}")
            program_choice = int(input("Choose Option : "))
            program = programs[program_choice - 14]
            filtered_df = institute_df[institute_df["Academic Program Name"] == program]


        os.system("cls" if os.name == "nt" else "clear")
        print("Select Quota :")
        print("1. All")
        quotas = institute_df["Quota"].unique()
        for i, quota in enumerate(quotas, start=2):
            print(f"{i}. {quota}")
        quota_choice = int(input("Choose Option : "))

        if quota_choice == 1:
            filtered_df = filtered_df
        else:
            quota = quotas[quota_choice - 2]
            filtered_df = filtered_df[filtered_df["Quota"] == quota]

        os.system("cls" if os.name == "nt" else "clear")
        print("Select Seat Type :")
        print("1. All")
        seat_types = institute_df["Seat Type"].unique()
        for i, seat_type in enumerate(seat_types, start=2):
            print(f"{i}. {seat_type}")
        seat_type_choice = int(input("Choose Option : "))

        if seat_type_choice == 1:
            filtered_df = filtered_df
        else:
            seat_type = seat_types[seat_type_choice - 2]
            filtered_df = filtered_df[filtered_df["Seat Type"] == seat_type]
        
        os.system("cls" if os.name == "nt" else "clear")
        print("Select Gender :")
        print("1. All")
        gneders = institute_df["Gender"].unique()
        for i, gender in enumerate(gneders, start=2):
            print(f"{i}. {gender}")
        gender_choice = int(input("Choose Option : "))

        if gender_choice == 1:
            filtered_df = filtered_df
        else:
            gender = gneders[gender_choice - 2]
            filtered_df = filtered_df[filtered_df["Gender"] == gender]

        os.system("cls" if os.name == "nt" else "clear")
        rank = int(input("Enter your rank : "))
        filtered_df["Closing Rank"] = filtered_df["Closing Rank"].apply(lambda x: int(x) if str(x).isdigit() else x)
        filtered_df = filtered_df[filtered_df["Closing Rank"] > rank]
        filtered_df = filtered_df.sort_values(by=["Closing Rank"], ascending=True)
        os.system("cls" if os.name == "nt" else "clear")
        display_df_web(filtered_df)
        print("Congratulations! File successfully opened in browser.")
        print("")
        choice = input("Press Enter to continue or type 'exit' to exit: ")
        if choice.lower() == "exit":
            break

# run the main function
pre_setup()
