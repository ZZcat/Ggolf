easy = ("Kaley Espihosa,Turtles,1","NoOne,extra,0")
medium = ("Jayden Mclearon,Black hole,1","Jadon Draeger,Hole 1,2")
hard = ()
other = ("Carly Silva,I don't even know,5","")

ee = 0
em = 0
eh = 0
for i in easy:
    ee+=1
    a,b,c = i.split(",")
    print "   E"+str(ee) + ' = Button("'+a+'")'

for i in medium:
    em+=1
    a,b,c = i.split(",")
    print "   M"+str(em) + ' = Button("'+a+'")'

for i in hard:
    eh+=1
    a,b,c = i.split(",")
    print "   H"+str(eh) + ' = Button("'+a+'")'

le=0
lm=0
lh=0
for i in easy:
    le+=1
    a,b,c = i.split(",")
    
    print "               elif E" + str(le) + ".obj.collidepoint(mouse):"
    print '                  game = "'+str(b)+'"'
    print '                  par = '+ str(c)
    print '                  par = "E"'
    

for i in medium:
    lm+=1
    a,b,c = i.split(",")
    
    print "               elif E" + str(lm) + ".obj.collidepoint(mouse):"
    print '                  game = "'+str(b)+'"'
    print '                  par = '+ str(c)
    print '                  par = "M"'
    

for i in hard:
    lh+=1
    a,b,c = i.split(",")
    
    print "               elif E" + str(lh) + ".obj.collidepoint(mouse):"
    print '                  game = "'+str(b)+'"'
    print '                  par = '+ str(c)
    print '                  mode = "H"'




print ee, "easys"
print em , "mediums"
print eh, "hards"
