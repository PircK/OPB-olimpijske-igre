from olympic_games.models import Drzava, Disciplina, OlimpijskeIgre, Tekmovalec, Rezultat
import csv

def zapisi_drzave():
    with open('podatki/seznam_drzav.csv', 'r', encoding='utf-8') as drzave:
        reader = csv.reader(drzave)
        for row in reader:
            if row != [] and row[0] != 'kratica':
                krat, ime = row
                d = Drzava(kratica=krat, ime=ime)
                d.save()

def zapisi_discipline_in_olimpijske():
    with open('podatki/rezultati.csv', 'r', encoding='utf-8') as rezultati:
        reader = csv.reader(rezultati)
        for row in reader:
            if row != [] and row[0] != 'igre':
                igre = row[0]
                disciplina = row[1]
                mesto_iger = igre[:-4]
                leto = int(igre[-4:])
                
                try:
                    d = Disciplina(ime=disciplina)
                    d.save()
                except:
                    disciplina = " "
                
                try:
                    o = OlimpijskeIgre(leto=leto, mesto=mesto_iger)
                    o.save()
                except:
                    mesto_iger = " "

def zapisi_tekmovalce():

    with open('podatki/roj_dan_tekmovalcev.csv', 'r', encoding='utf-8') as tekmovalci:
        reader = csv.reader(tekmovalci)
        for row in reader:
            if row != [] and row[0] != 'ime':
                ime, datum = row
                if type(ime[-1]) == int:
                    t = Tekmovalec(ime=ime, rojstvo=datum)
                    t.save()
                else:
                    t = Tekmovalec(ime=ime, rojstvo=datum)
                    t.save() 

def zapisi_rezultat():

    with open('podatki/rezultati.csv', 'r', encoding='utf-8') as rezultati:
        reader = csv.reader(rezultati)
        for row in reader:
            if row != [] and row[0] != 'igre':
                igre, disciplina, mesto, ime, drzava, rezultat = row
                mesto_iger = igre[:-4]
                leto = int(igre[-4:])
                if type(ime[-1]) == int:
                    r = Rezultat(ime=ime[:-2],disciplina=disciplina, mesto=mesto, rezultat=rezultat, igre=leto)
                    r.save()
                else:
                    r = Rezultat(ime=ime,disciplina=disciplina, mesto=mesto, rezultat=rezultat, igre=leto)
                    r.save()





#zapisi_drzave()
#zapisi_discipline_in_olimpijske()
zapisi_tekmovalce()

