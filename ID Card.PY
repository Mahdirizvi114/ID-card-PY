ID='''


        name:             <name>
        father name:      <father name>
        gender:           <gender>
        institute:        <institute>
        department:       <department>
        roll number:      <roll number>
 '''
 
a=input('enter your name: ')
b=input('enter your father name: ')
c=input('enter your gender: ')
d=input('enter your institute name: ')
e=input('enter your department name: ')
f=input('enter your roll number: ')

ID=ID.replace('<name>', a)
ID=ID.replace('<father name>', b)
ID=ID.replace('<gender>', c)
ID=ID.replace('<institute>', d)
ID=ID.replace('<department>', e)
ID=ID.replace('<roll number>', f)

print(ID)