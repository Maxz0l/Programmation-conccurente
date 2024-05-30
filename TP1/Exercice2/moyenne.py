import sys
if len(sys.argv)<2:
    print('Aucune moyenne à calculer')
else:
    moyenne = 0
    for note in sys.argv[1:]:
        if int(note)<0 or int(note)>20 or not note.isdigit():
            print('Note(s) non valide(s)')
        else:
            moyenne = moyenne + int(note)
    moyenne = round(moyenne,2)
    print("La moyenne est:",moyenne/(len(sys.argv)-1))