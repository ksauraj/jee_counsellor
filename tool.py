import os
import random
import sys
import time
import platform
import subprocess
import pandas as pd
from datetime import datetime
from colorama import init, Fore
import http.server
import socketserver
import threading
from tqdm import tqdm 
import shutil

init()

ascii_art = '''
     ██╗███████╗███████╗     ██████╗ ██████╗ ██╗   ██╗███╗   ██╗███████╗███████╗██╗     ██╗      ██████╗ ██████╗ 
     ██║██╔════╝██╔════╝    ██╔════╝██╔═══██╗██║   ██║████╗  ██║██╔════╝██╔════╝██║     ██║     ██╔═══██╗██╔══██╗
     ██║█████╗  █████╗      ██║     ██║   ██║██║   ██║██╔██╗ ██║███████╗█████╗  ██║     ██║     ██║   ██║██████╔╝
██   ██║██╔══╝  ██╔══╝      ██║     ██║   ██║██║   ██║██║╚██╗██║╚════██║██╔══╝  ██║     ██║     ██║   ██║██╔══██╗
╚█████╔╝███████╗███████╗    ╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║███████║███████╗███████╗███████╗╚██████╔╝██║  ██║
 ╚════╝ ╚══════╝╚══════╝     ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
                                                 - A command-line tool for JEE counselling assistance by Ksauraj.
'''

author_name = "Ksauraj"
version = "v2.0.2"

class NoLogRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_request(self, code='-', size='-'):
        pass
def display_progress_bar(task_description, steps_completed, total=100, duration=3):
    """
    function which Displays a progress bar.
    """
    with tqdm(total=total, desc=task_description, ncols=100, colour='green',bar_format='{l_bar}{bar} | {n_fmt}/{total_fmt}') as pbar:
        for _ in range(steps_completed):
            time.sleep(duration / steps_completed)  # Control smoothness of progress
            pbar.update(1)  # Increment the bar by 1 step



def delete_output_directory():
    """Offers an option to delete the output directory if the user selects the appropriate menu option."""
    output_dir = 'output'
    if os.path.exists(output_dir):
        print(f"{Fore.MAGENTA}Warning: This will delete all contents in the 'output' directory.")
        user_input = input(f"{Fore.YELLOW}Press 1 to confirm deletion, or any other key to cancel: {Fore.RESET}")
        
        if user_input == '1':
            shutil.rmtree(output_dir)  # Delete the directory and all its contents
            print(f"{Fore.GREEN}Output directory deleted successfully.{Fore.RESET}")
        else:
            print(f"{Fore.YELLOW}Output directory was not deleted.{Fore.RESET}")
       
    else:
        print(f"{Fore.YELLOW}Output directory does not exist.{Fore.RESET}")
    time.sleep(1)
    pre_setup()
    

def pre_setup():
    #progress bar for loading tool...
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.GREEN + ascii_art)
    total=100
    steps_completed= int(total*1.0)
    display_progress_bar("Loadiing Tool...",steps_completed=steps_completed,total=total, duration=0.3)
    

    print(Fore.YELLOW + "Select Counseling type:")
    print(Fore.GREEN + "1." + Fore.BLUE + "JOSAA")
    print(Fore.GREEN + "2." + Fore.BLUE + "CSAB" + Fore.RESET)
    print(Fore.GREEN + "3." + Fore.BLUE + "About" + Fore.RESET)
    print(Fore.GREEN + "4." + Fore.BLUE + "Clean Output Directory" + Fore.RESET)  # Added option to clean the output directory
    print(Fore.GREEN + "5." + Fore.BLUE + "Exit" + Fore.RESET)  #adding exit function in main menu
   
    option = input("Select Option (1 to 5) : ")                 #increasing last choice value
    if option == '1':
        josaa_rounds_year()
    elif option == '2':
        csab_rounds_year()
    elif option == '3':
        show_about_section()
    elif option=='4':
        delete_output_directory()
    elif option == '5':     #adding exit condition
        print("Exiting...") #printing exiting
        exit(0)             #calling exit function
    
    else:
        pre_setup()


def show_about_section():
    print(Fore.CYAN + "\nJEE Counselling Assistant - About\n" + Fore.RESET)
    print(f"Version: {version}")
    print(f"Author: {Fore.GREEN}{author_name}{Fore.RESET}")
    print(f"Acknowledgements: {Fore.GREEN}{author_name}{Fore.RESET}")
    print("Description: A tool to display colleges based on JEE Mains rank. Get personalized information based on your rank and make informed decisions.")
    
    input(Fore.YELLOW + "\nPress Enter to continue to the main menu..." + Fore.RESET)
    pre_setup()

def josaa_rounds_year():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.GREEN + ascii_art)
    # progress bar of step 1
    total=100
    steps_completed= int(total*0.1)
    display_progress_bar("STEP 1/10 ",steps_completed=steps_completed,total=total, duration=0.3)

    print(Fore.YELLOW + "Select JOSAA round year")
    print(Fore.GREEN + "1." + Fore.BLUE + "2022")
    print(Fore.GREEN + "2." + Fore.BLUE + "2023")
    print(Fore.GREEN + "3." + Fore.BLUE + "2024" + Fore.RESET)
    josaa_round_year_sel = input("Select Option (1 to 3): ")
    if josaa_round_year_sel == "1":
        josaa_round_year = "2022"
    elif josaa_round_year_sel == "2":
        josaa_round_year = "2023"
    elif josaa_round_year_sel == "3":
        josaa_round_year = "2024"
    print(josaa_round_year)
    josaa_rounds(josaa_round_year)


def josaa_rounds(josaa_round_year):
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.GREEN + ascii_art)
    #progress bar for step-2
    total=100
    steps_completed= int(total*0.2)
    display_progress_bar("STEP 2/10 ",steps_completed=steps_completed,total=total,duration=0.3)
    print("{Fore.YELLOW}Select JOSAA round {{josaa_round_year}}")
    if josaa_round_year == "2024":
        menu_options = [
            "Round 1",
            "Round 2",
            "Round 3",
            "Round 4",
            "Round 5"
        ]
    else:
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
    if josaa_round_year == "2024":
        selected_round = input("Select Option (1 to 5): ")
        if int(selected_round) > 5:
            return josaa_rounds()
        csv_files("josaa", selected_round, josaa_round_year)
    else:
        selected_round = input("Select Option (1 to 6): ")
        if int(selected_round) > 6:
            return josaa_rounds()
        csv_files("josaa", selected_round, josaa_round_year)


def csab_rounds_year():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.GREEN + ascii_art)
    #progress bar for step-1
    total=100
    steps_completed= int(total*0.1)
    display_progress_bar("STEP 1/10 ",steps_completed=steps_completed,total=total, duration=0.3)

    print(Fore.YELLOW + "Select CSAB round year")
    print(Fore.GREEN + "1." + Fore.BLUE + "2021")
    print(Fore.GREEN + "2." + Fore.BLUE + "2022")
    print(Fore.GREEN + "3." + Fore.BLUE + "2023")
    print(Fore.GREEN + "4." + Fore.BLUE + "2024" + Fore.RESET)
    csab_round_year_sel = input("Select Option (1 to 4): ")
    if csab_round_year_sel == "1":
        csab_round_year = "2021"
    elif csab_round_year_sel == "2":
        csab_round_year = "2022"
    elif csab_round_year_sel == "3":
        csab_round_year = "2023"
    elif csab_round_year_sel == "4":
        csab_round_year = "2024"
    print(csab_round_year)
    csab_rounds(csab_round_year)


def csab_rounds(csab_round_year):
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.GREEN + ascii_art)
    #progress bar for step-2
    total=100
    steps_completed= int(total*0.2)
    display_progress_bar("STEP 2/10 ",steps_completed=steps_completed,total=total, duration=0.3)

    print(f"{Fore.YELLOW}Select CSAB round ({csab_round_year})" )
    print(Fore.GREEN + "1." + Fore.BLUE + "Round 1")
    print(Fore.GREEN + "2." + Fore.BLUE + "Round 2")
    csab_round = input(Fore.RESET + "Select Option (1 to 2) : ")
    csv_files("csab", csab_round, csab_round_year)

# define the path of csv files for different types of colleges


def csv_files(type, round, year):
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
            "ALL": os.path.join(cwd, "josaa", f"{year}", f"round_{josaa_rounds}", "ranks_all.csv"),
            "IIITs": os.path.join(cwd, "josaa", f"{year}", f"round_{josaa_rounds}", "ranks_iiits.csv"),
            "IITs": os.path.join(cwd, "josaa", f"{year}", f"round_{josaa_rounds}", "ranks_iits.csv"),
            "NITs": os.path.join(cwd, "josaa", f"{year}", f"round_{josaa_rounds}", "ranks_nits.csv"),
            "GFTIs": os.path.join(cwd, "josaa", f"{year}", f"round_{josaa_rounds}", "ranks_gftis.csv")
        }
        josaa_institue_types(CSV_FILES)
    elif type == "csab":
        csab_rounds = round
        csv_path = os.path.join(
            cwd,
            "csab",
            f"{year}",
            f"round_{csab_rounds}",
            "ranks.csv")
        df = pd.read_csv(csv_path)
        csab_institue_types(df)


def csab_institue_types(df):
    # clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.GREEN + ascii_art)
    #progress bar for step-3
    total=100
    steps_completed= int(total*0.3)
    display_progress_bar("STEP 3/10 ",steps_completed=steps_completed,total=total, duration=0.3)
    # ask for user input for institute type
    print(Fore.YELLOW + "Select Institute type:")
    print(Fore.GREEN + "1." + Fore.BLUE + "ALL")
    print(Fore.GREEN + "2." + Fore.BLUE + "IIITs")
    print(Fore.GREEN + "3." + Fore.BLUE + "NITs")
    print(Fore.GREEN + "4." + Fore.BLUE + "GFTIs")
    option = input(Fore.RESET + "Select Option (1 to 4): ")

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
    else:
        print("Invalid option. Please select again.")

    main(df)


def josaa_institue_types(CSV_FILES):
    # clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.GREEN + ascii_art)
    #progress bar for step-3
    total=100
    steps_completed= int(total*0.3)
    display_progress_bar("STEP 3/10 ",steps_completed=steps_completed,total=total, duration=0.3)
    # ask for user input for institute type
    print(Fore.YELLOW + "Select Institute type:")
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
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.GREEN + ascii_art)
    #progress bar for step-4
    total=100
    steps_completed= int(total*0.4)
    display_progress_bar("STEP 4/10 ",steps_completed=steps_completed,total=total, duration=0.3)

    print("Note: Programs marked with '*' will display all the programs similar to them.")
    print("Select Program:")
    print(Fore.GREEN + "1." + Fore.BLUE + "All")
    print(Fore.GREEN + "2." + Fore.BLUE + "Computer Science and Engineering*")
    print(Fore.GREEN + "3." + Fore.BLUE +
          "Artificial Intelligence and Data Science*")
    print(Fore.GREEN + "4." + Fore.BLUE +
          "Electronics and Communication Engineering*")
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
        print(
            Fore.RED +
            "No programs found matching the selected options." +
            Fore.RESET)
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


def display_df_web(df, heading, subheading):
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # create a unique filename based on the current date and time
    filename = os.path.join(
        output_dir,
        f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html")

    # convert the DataFrame to an HTML table
    html_table = df.to_html(index=False, classes='table',table_id="tableID")

    # Generate the complete HTML content with headings, CSS styles, and the
    # table
    html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ heading }</title>
    <style>
      html, body {{
        height: 100%;
        text-align: center;
        font-family: Tahoma, sans-serif;
        margin: 0;
        padding: 0;
    }}

    body {{
        margin: 30px;
    }}
    
    /* Title bar styling */
    .title-bar {{
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
        background: #FFFFFF; /* Cool gradient color */
        padding: 20px;
        border-radius: 10px;  /* Rounded border */
        margin-bottom: 25px;  /* Space between title bar and content */
        height: 120px; /* Adjusted height */
    }}

    .title-bar h1 {{
        font-size: 80px; /* Larger heading size */
        color: #000000; /* Black font color */
        font-family: "Anton", sans-serif; /* Updated to Anton font */
        font-weight: 400;  /* Regular weight */
    }}

    .title-bar h2 {{
        font-style: italic;
        font-family: sans-serif;
        font-size: 16px; /* Smaller subheading */
        position: absolute;
        top: 115px;  /* Move below the main heading */
        right: 480px; /* Shifted right */
        
    }}


.typing-text {{
        font-size: 12px;
        position: absolute;
        top: 160px;
        
        font-style: italic;
        color: #000000;
        font-family: "Courier New", Courier, monospace;
    }}

    /* Profile and GitHub icons */
    .icon-container {{
        position: absolute;
        bottom: 10px; /* Move to the bottom */
        right: 10px;
        display: flex;
        align-items: center;
    }}

    /* General styling for all icons */
.icon-container img {{
    height: 25px; /* Slightly larger icon size for all */
    width: 25px;
    border-radius: 100%; /* Round border */
    margin-left: 10px;
    cursor: pointer;
    transition: transform 0.3s ease; /* Hover effect transition */
}}

.icon-container img.github-icon,
.icon-container img.linkedin-icon {{
    height: 30px; 
    width: 28px;
    border-radius: 100%; 
}}

.icon-container img:hover {{
    transform: scale(1.5);
}}

    /* Table styling */
    table.table {{
        border-collapse: separate;
        border-spacing: 0;
        min-width: 350px;
        border: none;  /* Remove the border attribute */
    }}

    table.table tr th,
    table.table tr td {{
        border-right: 1px solid #bbb;
        border-bottom: 1px solid #bbb;
        padding: 5px;
    }}

    table.table tr th:first-child,
    table.table tr td:first-child {{
        border-left: 1px solid #bbb;
    }}

    table.table tr th {{
        background: #eee;
        border-top: 1px solid #bbb;
        text-align: center;
    }}

    /* top-left border-radius */
    table.table tr:first-child th:first-child {{
        border-top-left-radius: 6px;
    }}

    /* top-right border-radius */
    table.table tr:first-child th:last-child {{
        border-top-right-radius: 6px;
    }}

    /* bottom-left border-radius */
    table.table tr:last-child td:first-child {{
        border-bottom-left-radius: 6px;
    }}

    /* bottom-right border-radius */
    table.table tr:last-child td:last-child {{
        border-bottom-right-radius: 6px;
    }}

    a {{
        text-decoration: none;
        color: #18272F;
        font-weight: 700;
        position: relative;
    }}

    a::before {{
        content: '';
        background-color: hsla(0, 100%, 50%, 0.236);
        position: absolute;
        left: 0;
        bottom: 3px;
        width: 100%;
        height: 8px;
        z-index: -1;
        transition: all .3s ease-in-out;
    }}

    a:hover::before {{
        bottom: 0;
        height: 100%;
        background-color: hsla(142, 61%, 58%, 0.359);
    }}

    /* Pagination button styling */
    .dataTables_wrapper .dataTables_paginate .paginate_button {{
        color: #555;
        padding: 8px 16px;
        border: 1px solid #ddd;
        margin: 0 2px;
        background-color: #f9f9f9;
        cursor: pointer;
        border-radius: 4px;
    }}

    .dataTables_wrapper .dataTables_paginate .paginate_button:hover {{
        background-color: #eee;
        color: #333;
    }}

    .dataTables_wrapper .dataTables_paginate .paginate_button.current {{
        background-color: #007bff;
        color: white;
        border: 1px solid #007bff;
    }}

   /* Disabled button styling for Previous and Next buttons */
.dataTables_wrapper .dataTables_paginate .paginate_button.disabled,
.dataTables_wrapper .dataTables_paginate .previous.disabled,
.dataTables_wrapper .dataTables_paginate .next.disabled {{
    background-color: #f0f0f0 !important;
    color: #aaa !important;
    cursor: not-allowed !important;
    border: 1px solid #ddd !important;
}}

/* Normal button styling for Previous and Next buttons */
.dataTables_wrapper .dataTables_paginate .previous,
.dataTables_wrapper .dataTables_paginate .next {{
    background-color: #f9f9f9 !important;
    color: #555 !important;
    padding: 8px 16px !important;
    border: 1px solid #ddd !important;
    border-radius: 4px !important;
    margin: 0 2px !important;
    cursor: pointer !important;
}}

/* Hover state for Previous and Next buttons */
.dataTables_wrapper .dataTables_paginate .previous:hover,
.dataTables_wrapper .dataTables_paginate .next:hover {{
    background-color: #eee !important;
    color: #333 !important;
}}

/* Active/current page button */
.dataTables_wrapper .dataTables_paginate .paginate_button.current {{
    background-color: #007bff !important;
    color: white !important;
    border: 1px solid #007bff !important;
}}
    </style>

    <!-- Importing the custom fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Anton&family=Qwitcher+Grypen:wght@400;700&display=swap" rel="stylesheet">

    <script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.js"></script>
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.23/css/jquery.dataTables.min.css">
    <script src="https://cdn.datatables.net/1.10.23/js/jquery.dataTables.min.js"></script>
</head>
<body>

    <!-- Title bar section -->
    <div class="title-bar">
        <h1><a>{ heading }</a></h1>
        <h2><a>{ subheading }</a></h2>
        <div class="typing-text" id="typing-text"></div>

        <!-- Icon container -->
        <div class="icon-container">
     <a href="https://github.com/ksauraj/jee_counsellor" target="_blank">
        <img src="https://img.icons8.com/?size=100&id=38388&format=png&color=000000" alt="Fork repo Icon">
    </a>
    <a href="https://github.com/ksauraj" target="_blank">
        <img src="https://img.icons8.com/?size=100&id=62856&format=png&color=000000" alt="GitHub Icon" class="github-icon">
    </a>
    <a href="https://sauraj.eu.org/#/" target="_blank">
        <img src="https://github.com/user-attachments/assets/6a1740ee-3492-4bd6-932b-3c7b15f0d254" alt="Profile Icon">
    </a>
    <a href="https://x.com/ksauraj" target="_blank">
        <img src="https://img.icons8.com/?size=100&id=111056&format=png&color=000000" alt="Xlogo Icon">
    </a>
    
    </a><a href="https://www.linkedin.com/in/sauraj-kumar-singh-807295226" target="_blank">
        <img src="https://img.icons8.com/?size=100&id=8808&format=png&color=000000" alt="LinkedIn Icon" class="linkedin-icon">

    </a>
</div>

    </div>

    <!-- Table container -->
    <div class="container">
        { html_table }
    </div>

    <script> 
    $(document).ready(function () {{ 
        $('#tableID').DataTable({{ pageLength: 20, ordering: false, }}); }});
         
        document.addEventListener("DOMContentLoaded", function() {{
        function typeText(text, elementId, speed) {{
            let i = 0;
            const animatedTextElement = document.getElementById(elementId);
            function typeChar() {{
                if (i < text.length) {{
                    animatedTextElement.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(typeChar, speed);  // Control speed of typing here
                }}
                else {{ 
                    setTimeout(restartTyping, 1000);  // Delay before restarting the typing effect
                }}
            }}

            function restartTyping() {{
                animatedTextElement.innerHTML = "";  // Clear the text
                i = 0;  // Reset index
                typeChar();  // Restart typing
            }}

            typeChar();  // Start typing
        }}

        // Start typing effect for the given text
        const quote = "A command-line tool for JEE counselling assistance ";
        typeText(quote, "typing-text", 100);  // 100ms delay for each character
    }}); 
    </script>
</body>
</html>


'''



   

    # Save the HTML content to the file
    with open(filename, "w") as file:
        file.write(html_content)
    #progress bar for step-10
    total=100
    steps_completed= int(total*1.0)
    display_progress_bar("STEP 10/10 ",steps_completed=steps_completed,total=total, duration=0.3)


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
    elif "TERMUX_VERSION" in os.environ:
        os.chdir("output")
        PORT = random.randint(50000, 65535)
        handler = NoLogRequestHandler
        server = socketserver.ThreadingTCPServer(("", PORT), handler)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        print(f"{Fore.GREEN} Web server started at http://localhost:{PORT} {Fore.RESET}")

        try:
            fileName = filename.split("/")[1]
            os.system(f"termux-open http://localhost:{PORT}/{fileName}")
            input("Press Enter to stop the server...\n")
        finally:
            print("Stopping web server...")
            return
    else:
        subprocess.Popen(["xdg-open", filename],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# main function to run the CLI tool
def main(df):
    while True:
        institute_df = df
        os.system("cls" if os.name == "nt" else "clear")
        filtered_df = filter_programs(institute_df)

        def filter_by_choices(choices, column_name, steps):
            unique_choices = institute_df[column_name].unique()

            os.system("cls" if os.name == "nt" else "clear")
            print(Fore.GREEN + ascii_art)
            
            total=100
            steps_completed=int(total*steps)
            steps_count = int(steps*10)
            str_steps=f"STEP {steps_count}/10"
            display_progress_bar(str_steps,steps_completed=steps_completed,total=total, duration=0.3)

           
            print(f"{Fore.YELLOW}Select {column_name}:")

            print(Fore.GREEN + "1." + Fore.BLUE +" All")
            for i, choice in enumerate(unique_choices, start=2):
                print(f"{Fore.GREEN}{i}. {Fore.BLUE}{choice}{Fore.RESET}")



            print(f"{Fore.YELLOW}")
            print(f"You are Selecting {column_name}")
            choices_input = input("Choose Options ((space-separated, e.g., 2 3 4) & 1 for all choices) : ")
            selected_choices = list(map(int, choices_input.split()))

            if 1 in selected_choices:
                return filtered_df
            else:
                selected_choices = [choice - 2 for choice in selected_choices]
                filtered_choices = [unique_choices[i] for i in selected_choices]
                return filtered_df[filtered_df[column_name].isin(filtered_choices)]

        filtered_df = filter_by_choices(institute_df["Institute"], "Institute",0.5)
        
        filtered_df = filter_by_choices(institute_df["Quota"], "Quota",0.6)
        
        filtered_df = filter_by_choices(institute_df["Seat Type"], "Seat Type",0.7)
       
       
        filtered_df = filter_by_choices(institute_df["Gender"], "Gender",0.8)
       
        

        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.GREEN + ascii_art)
        display_progress_bar("STEP 9/10 ",steps_completed=90,total=100, duration=0.3)
        rank = int(input(Fore.YELLOW + "Enter your rank: " + Fore.RESET))
        filtered_df["Closing Rank"] = filtered_df["Closing Rank"].astype(
            str).str.extract(r"(\d+)").astype(int)
        filtered_df = filtered_df[filtered_df["Closing Rank"] > rank].sort_values(
            by=["Closing Rank"], ascending=True)

        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.GREEN + ascii_art)
        display_df_web(filtered_df, "JEE COUNSELLOR", "~By Ksauraj")
        print(
            Fore.GREEN +
            "Congratulations! File successfully opened in browser. Please wait......" +
            Fore.RESET)
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.GREEN + ascii_art)
        choice = input(
            f"{Fore.BLUE}1. {Fore.YELLOW}Go back to main menu.\n"
            f"{Fore.BLUE}2. {Fore.YELLOW}Continue with same settings.\n"
            f"{Fore.BLUE}3. {Fore.YELLOW}Exit from tool.\n"
            f"{Fore.RESET}Select option (1-3): ")
        if choice == "1":
            pre_setup()
        elif choice == "3":
            break


# run the main function
pre_setup()
