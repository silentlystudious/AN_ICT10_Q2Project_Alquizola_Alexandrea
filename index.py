from pyscript import document, display

# TUPLE FOR HEADINGS
headings = (
    "Welcome to OB Montessori Center!",
    "About Our School",
    "OB Montessori Center",
    "Junior High School Department",
    '"To fight for the right without question or doubt."'
)

# TUPLE FOR DESCRIPTIONS
descriptions = (
"""In 1966, Dr. Preciosa S. Soliven opened the first Operation Brotherhood Montessori Center (OBMC) branch in Manila.
    Her vision was to bring a newform of education in the Philippines that would liberate the spirit of the
    Filipino child. She successfully integrated the western-based method of Dr. Maria Montessori into the Asian
    milieu, while remaining true to its universal principles.""",
"""The Montessori education emphasizes independence, freedom with responsibility, and respect for the child’s 
    intellectual, spiritual, and social development. Children learn through exploration, manipulation, order, 
    repetition, abstraction, and communication.""",
"""The O.B. Professional Junior High School Program supports the emotional, psychological, and social transformation of 
    students from ages 13 to 16 as they prepare for adult responsibilities. The curriculum focuses on strengthening 
    critical skills like problem-solving, collaboration, and communication by harnessing their creative energies as they 
    begin to seek economic independence."""
)

# DISPLAY FOR HEADINGS 
display(headings [0], target="school_welcome")
display(headings [1], target="school_about")
display(headings [2], target="school_name")
display(headings [3], target="school_department")
display(headings [4], target="school_quote")

# DISPLAY FOR DESCRIPTIONS
display(descriptions [0], target="school_overview")
display(descriptions [1], target="school_values")
display(descriptions [2], target="school_description")