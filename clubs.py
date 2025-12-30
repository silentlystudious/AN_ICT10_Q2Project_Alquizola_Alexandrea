from pyscript import document, display

# TUPLES FOR HEADINGS
headings = (
    "School Information",
    "Select a OBMC Junior High School Club:"
)

# DISPLAY FOR HEADINGS
display(headings [0], target="heading")
display(headings [1], target="subheading")

# CODE TO RUN THE CLUB INFORMATION WHEN CLICKING THE "SHOW CLUB INFORMATION" BUTTON
def club_information(e):

    # DICTIONARY VARIABLES THROUGH ID FROM CLUBS.HTML
        # THE OVERVIEW DATA IS NOT MADE INTO MULTILINE COMMENTS SINCE IT DOES NOY FORMAT THE TEXT PROPERLY.
        # THE OVERVIEW LINES ARE SHORTENED FOR CONVIENIENCE IN CODE VIEWING.
    data = {
    "Varsity": {
        "Name": "Boys' Basketball Varsity",
        "Overview": "The Boys' Basketball Varsity allows male students in developing teamwork, grit, and "
                    "diligence while strategizing moves with their peers and making shots toward the basketball hoop.",
        "Schedule": "Every Monday, 2:30PM - 4:30PM",
        "Location": "Quadrangle",
        "Moderator": "Mr. Layug",
        "Members": 20,
        "Category": "Extracurricular"
    },
    "COCC": {
        "Name": "Cadet Officer Candidate Course",
        "Overview": "The Cadet Officer Candidate Course helps students develop their leadership and peacebuilding skills "
                    "while adapating to a culture of peace and spearheading environmental protection in the OB Montessori "
                    "community.",
        "Schedule": "Every Friday, 2:30PM - 4:30PM",
        "Location": "Quadrangle",
        "Moderator": "Mr. Santos",
        "Members": 20,
        "Category": "Extracurricular"
    },
    "CommArts": {
        "Name": "Communication Arts Club",
        "Overview": "The Communication Arts Club allows students to showcase their talent in writing and speaking. The club "
                    "also prepares students to be well-equipped public speakers, eloquent writers, and confident emcees.",
        "Schedule": "Every Monday and Wednesday, 3:00PM - 4:00PM",
        "Location": "Room 404",
        "Moderator": "Mr. Alegrid",
        "Members": 20,
        "Category": "Academic"
    },
    "Glee": {
        "Name": "Glee Club",
        "Overview": "The Glee Club prepares students to showcase their talent in singing and performing by fostering "
                    "their vocal technique, identifying their vocal strengths, and enhancing their stage confidence.",
        "Schedule": "Every Tuesday and Thursday, 2:30PM - 4:30PM",
        "Location": "Glee Club Room",
        "Moderator": "Ms. Aguirre",
        "Members": 50,
        "Category": "Extracurricular"
    },
    "Band": {
        "Name": "Marching Band",
        "Overview": "The Marching Band allows students to enhance their musical knowledge on playing instruments that "
                    "encompass the spirit of nationalism and patriotism in the OB Montessori community and beyond the "
                    "Philippines.",
        "Schedule": "Every Tuesday and Thursday, 2:30PM - 4:00PM",
        "Location": "Band Room",
        "Moderator": "Mr. Guballa",
        "Members": 25,
        "Category": "Extracurricular"
    },
    "Math": {
        "Name": "Math Guild",
        "Overview": "The Math Guild enables students to enhance their math skills and broaden their opportunities by sharpening "
                    "their problem-solving skills and enhancing their agility to quickly find mathematical solutions.",
        "Schedule": "Every Monday, 2:30PM - 4:30PM",
        "Location": "Room 304 (Junior Division) and Room 416 (Senior Divsion)",
        "Moderator": "Ms. Garcia (Junior Division) and Mr. Tuzon (Senior Division)",
        "Members": 30,
        "Category": "Academic"
    },
    "Science": {
        "Name": "Science Club",
        "Overview": "The Science Club builds students in developing curiosity and critical thinking while "
                    "performing experiments, investigating organisms, and exploring the world around them.",
        "Schedule": "Every Monday and Wednesday, 3:00PM - 4:00PM",
        "Location": "Science Laboratory Room",
        "Moderator": "Mrs. Galang",
        "Members": 30,
        "Category": "Academic"
    },
    "SS": {
        "Name": "Social Studies Club",
        "Overview": "The Social Studies Club allows students to explore history, politics, culture, and current issues "
                    "while developing skills that shape both thought and action beyond the classroom.",
        "Schedule": "Every Monday, 2:30PM - 4:00PM",
        "Location": "Room 405 (Junior Division) and Room 415 (Senior Division)",
        "Moderator": "Mr. Roque (Junior Division) and Ms. Roxas (Senior Division)",
        "Members": 25,
        "Category": "Academic"
    }
}

    # STRING VARIABLES FOR CLUB SELECTION THROUGH ID FROM CLUBS.HTML
    select =  document.getElementById("club").value
    club = data[select]

    # EMPHASIZES THE CLUB NAME WHEN DISPLAYED IN CLUBS.HTML
    name = (
        f"{club['Name']}\n"
    )

    # DISPLAY THE REMAINING CLUB INFORMATION WHEN DISPLAYED IN CLUBS.HTML
    display = (
        f"Overview:  {club['Overview']}\n"
        f"Schedule:  {club['Schedule']}\n"
        f"Location:  {club['Location']}\n"
        f"Club Moderator:  {club['Moderator']}\n"
        f"Number of Members:  {club['Members']}\n"
        f"Club Category:  {club['Category']}"
    )

    # DISPLAYS FOR THE NAME AND CLUB INFORMATION WHEN THE "SHOW CLUB INFORMATION" BUTTON IS CLICKED
    document.getElementById("name").innerText = name
    document.getElementById("information").innerText = display
    
