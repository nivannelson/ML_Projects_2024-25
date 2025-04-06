'''
Develop a program to read the employee's name, code, and basic pay
and calculate the gross salary, deduction, and net salary according to
the following conditions. Define a function to find each of the
components. Finally, generate a payslip.
Basic Pay     DA       HRA   MA       PT      PF      IT
(BP)          (%)      (%)   (%)      (%)     (%)     (%)
<10000         5       2.5    500     20        8      _
<30000        7.5       5     2500    60       8       _
<50000        11       7.5    5000    60      11      11
else          25        11    7000    80      12      20

Gross Salary (GS) : BP + DA + HRA + MA
Deduction (D): PT + PF + IT
Net Salary = GS – D

Conditional
Branching

'''
global paychart
paydata=[{"BP":10000,"DA":5,"HRA":2.5,"MA":500,"PT":20,"PF":8,"IT":0},
         {"BP":30000,"DA":7.5,"HRA":5,"MA":2500,"PT":60,"PF":8,"IT":0},
         {"BP":50000,"DA":11,"HRA":7.5,"MA":5000,"PT":60,"PF":11,"IT":11},
         {"BP":"else","DA":25,"HRA":11,"MA":7000,"PT":80,"PF":12,"IT":20}
         ]

def datainput():
    print()

def main():

    try:
        tempname=input("To start enter your Name:")
        tempcode=input("Code:")
        tempbasic=float(input("Basic Pay:"))
        # print(type(paydata[0].get("Basic Pay")))

        print("       Generated Payslip")
        cnt=0
        for cnt in range(0,3):
            if tempbasic<paydata[cnt].get("BP"):
                break
            cnt+=1
            if cnt==3:
                break
        BP=tempbasic
        DA=BP*paydata[cnt].get("DA")/100
        HRA=BP*paydata[cnt].get("HRA")/100
        MA=paydata[cnt].get("MA")
        PT=BP*paydata[cnt].get("PT")/100
        PF=BP*paydata[cnt].get("PF")/100
        IT=BP*paydata[cnt].get("IT")/100
        GS=BP+DA+HRA+MA
        D=PT+PF+IT
        print(f"""
Name: {tempname}

Employment Code: {tempcode}

Basic Pay: {tempbasic}

Gross Salary (GS) : {BP}(BP) + {DA}(DA) + {HRA}(HRA) + {MA}(MA) = {GS}
Deduction (D): {PT}(PT) + {PF}(PF) + {IT}(IT) = {D}
Net Salary = {GS}(GS) – {D}(D) = {GS-D}
""")
        
    except KeyboardInterrupt:
        print("Aborting...")
        exit(0)
    except Exception as e:
        print(e)
        main()


main()


'''
THINGS LEARNED
-
TODO
store employ information
'''