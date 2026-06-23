sec_g = {
    1: {"name": "Sujit", "regno": "250301370001"},
    2: {"name": "Subha", "regno": "250301370002"},
    3: {"name": "Nikita", "regno": "250301370003"},
    4: {"name": "Subhasis", "regno": "250301370004"},
    5: {"name": "Sai", "regno": "250301370005"},
    6: {"name": "Bigi", "regno": "250301370006"},
    7: {"name": "Navisha", "regno": "250301370007"},
    8: {"name": "Pritesh", "regno": "250301370008"},
    9: {"name": "Rudra", "regno": "250301370009"},
    10: {"name": "Sky", "regno": "250301370010"},
    11: {"name": "Satyam", "regno": "250301370011"},
    12: {"name": "Bidhyak", "regno": "250301370012"},
    13: {"name": "Sohan", "regno": "250301370013"},
    14: {"name": "Riju", "regno": "250301370014"},
    15: {"name": "Arka", "regno": "250301370015"},
    16: {"name": "Tanmay", "regno": "250301370016"},
    17: {"name": "Manoj", "regno": "250301370017"},
    18: {"name": "Dj Ishu", "regno": "250301370018"},
    19: {"name": "Sexy Shashi", "regno": "250301370019"},
    20: {"name": "Ps-5", "regno": "250301370020"},
    21: {"name": "Raj", "regno": "250301370021"},
    22: {"name": "Swapnarani", "regno": "250301370022"},
    23: {"name": "Swadhin", "regno": "250301370023"},
    24: {"name": "X-student", "regno": "250301370024"},
    25: {"name": "Ananda", "regno": "250301370025"},
    26: {"name": "Subham", "regno": "250301370026"},
    27: {"name": "Gopal", "regno": "250301370027"},
    28: {"name": "Muskan", "regno": "250301370028"},
    29: {"name": "Himadri", "regno": "250301370029"},
    30: {"name": "Udit", "regno": "250301370030"},
    31: {"name": "Parnika", "regno": "250301370031"},
    32: {"name": "X-student", "regno": "250301370032"},
    33: {"name": "Chandrika", "regno": "250301370033"},
    34: {"name": "Sumit", "regno": "250301370034"},
    35: {"name": "Jnana", "regno": "250301370035"},
    36: {"name": "Manjeet", "regno": "250301370036"},
    37: {"name": "Abhisek", "regno": "250301370037"},
    38: {"name": "Amit", "regno": "250301370038"},
    39: {"name": "Divya", "regno": "250301370039"},
    40: {"name": "Abinash", "regno": "250301370040"},
    41: {"name": "Swapnil", "regno": "250301370041"},
    42: {"name": "Kaju", "regno": "250301370042"},
    43: {"name": "Ashriwad", "regno": "250301370043"},
    44: {"name": "Himanshu", "regno": "250301370044"},
    45: {"name": "Abhinandan", "regno": "250301370045"},
    46: {"name": "Anwesha", "regno": "250301370046"},
    47: {"name": "Dipankar", "regno": "250301370047"},
    48: {"name": "Sahil", "regno": "250301370048"},
    49: {"name": "Smruti", "regno": "250301370049"},
    50: {"name": "Bhuban", "regno": "250301370050"},
    51: {"name": "Jay", "regno": "250301370051"},
    52: {"name": "Ultra Bott", "regno": "250301370052"},
    53: {"name": "Palak", "regno": "250301370053"},
    54: {"name": "MD", "regno": "250301370054"},
    55: {"name": "Pratik", "regno": "250301370055"},
    56: {"name": "Arpita", "regno": "250301370056"},
    57: {"name": "Santanu", "regno": "250301370057"},
    58: {"name": "Trilokesh", "regno": "250301370058"},
    59: {"name": "Nalua", "regno": "250301370059"},
    60: {"name": "Susu", "regno": "250301370060"}
}

def info(roll_no):
    student = sec_g.get(roll_no)

    if student:
        print(f"""
Student Details
---------------
Name  : {student['name']}
RegNo : {student['regno']}
        """)
    else:
        print("Student not found.")


# Example
