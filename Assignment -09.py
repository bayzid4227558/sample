 
#----                                 Assignmeant no.- 09                                              ----#

#          Through this program we can know which company's SIM we are using in our Mobile

All_Operators = ['GrameenPhone','Robi','Banglalink','Airtel','Teletakl']

mobile_numbers = input("If you want to see which company sim user you are then provide your Mobile number : ")

for _ in range(5):
    if mobile_numbers == "017" or "013":
        print ("You are currenly using this Sim {}".format(All_Operators[0]))
    elif mobile_numbers == "018":
        print ("You are currenly using this Sim {}".format(All_Operators[1]))
    elif mobile_numbers == "014" or "019":
        print ("You are currenly using this Sim {}".format(All_Operators[2]))
    elif mobile_numbers == "016":
        print ("You are currenly using this Sim {}".format(All_Operators[3]))
    elif mobile_numbers == "015":
        print ("You are currenly using this Sim {}".format(All_Operators[4]))
    else :
        print ("Sorry! the mobile number is not valid in Bangladesh")

#AllOperators In. No- GP-0, RO-1, BL-02, AR-03, TE-04 


 

