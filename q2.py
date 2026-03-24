n=int(input("enter the nummber of parentheses: "))

well_formed_parentheses=[]

def generate_parentheses(left,right,parens):
    if left==0 and right==0:
        well_formed_parentheses.append(parens)
    if left>0:
        generate_parentheses(left-1,right,parens+"(")
    if right>left:
        generate_parentheses(left,right-1,parens+")")

generate_parentheses(n,n,"")

print(well_formed_parentheses)