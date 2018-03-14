### BONJOUR, ICI Jean-Hugues ###
### Comme toujours, mes notes et corrections sont précédées de trois dièses ###

### Il serait intéressant de décrire ce que tu cherches à faire dans des commentaires
### Je vois que tu moissonnes les films qui ont remporté l'Oscar du meilleur film
### Mais quels sont les problèmes que tu as éprouvés?

### Je vois que tu as essayé plein de choses. C'est bien!

# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

fichier = "film.csv"
### Je crée un fichier pour l'output de mon code
fichierJHR = "oscarsJHR.csv"

### Tout le début est très bien adapté au site que tu as choisi de moissonner

url= "http://www.imdb.com/search/title?count=100&groups=oscar_best_picture_winners&sort=year,desc&ref_=nv_ch_osc_2"

contenu = requests.get(url)
#print (contenu)

page = BeautifulSoup(contenu.text,"html.parser")
#print(page)

urlDesFilms = page.find_all("div", class_="lister-item-image float-left")
#print (urlDesFilms)

for link in urlDesFilms:
	film=[]
	link= link.a["href"]
#	print (link)
	urlcomplet = "http://www.imdb.com" + link
	print (urlcomplet)

	film.append(urlcomplet)

	contenu2= requests.get(urlcomplet)
	page2 = BeautifulSoup(contenu2.text,"html.parser")
	#print(page2)
	nameetdate = page2.title.text.split(" - ")[0].strip()
	name= nameetdate[:-6].strip() ### J'ajoute un «strip» ici aussi
	date= nameetdate[-6:]
	print(name)
	print(date)

	film.append(name)
	# film.append(date)

### On peut enlever les parenthèses de l'année
	date = date.strip("(").strip(")")
	film.append(date)

### Pour les réalisateurs/trices, comme il y a certains films qui en ont plusieurs,
### on peut créer une liste pour les contenir tous,
### et c'est cette liste qu'on va mettre dans la colonne «réalisateur»

	directors= page2.find_all(attrs={"itemprop" : "director"}) 
	#print(directors)
	reals = []
	
	for director in directors:

		real = director.find("span",class_="itemprop").text.strip()
		reals.append(real)

	film.append(reals)

# 		#print(director.text.strip())
# 		try:
# 			d = director.text.strip().split(":")
# 			print(d[0])
# 			# film.append(d[0])
# ##            if d[0]=="Director":
# ##				realisateur= d[1]
# #				print(realisateur)
# ##				film.append(realisateur)
# ##			else:
# ##				print("°")
# 		except:
# 			print("Impossible de trouver le directeur")

### Ici, je comprends que tu crées une boucle avec toutes les autres infos du film
### C'est une bonne méthode qui, un peu comme je viens de le faire avec les réalisateurs,
### Te permet d'enregistrer les cas où il y a plusieurs pays, par exemple

	infos= page2.find_all("div", class_="txt-block")
			#print (infos)

	
	for info in infos:
#		print (info.text.strip())
		
		try:
			i= info.text.strip().split(":")
			
			if i[0]=="Country":
### J'ajoute juste un .strip() aux différents éléments que tu moissonnes
				country = i[1].strip()
#				print(country)
				film.append(country)
### Pour le budget, j'enlève le mot «(estimated)»
			if i[0]== "Budget":
				budget =i[1].split("(")
				budget = budget[0].strip()
#				print(budget)
				film.append(budget)
			if i[0]== "Gross USA":
				gross= i[1].strip()
#				print(gross)
				film.append(gross)

			
			# else:
			# 	print("-")
			
		except:
			print("")
	

### Je comprends que tu veux ramasser tous les prix remportés par un film donné
### Mais puisqu'il est question des Oscars, pourquoi ne pas aller chercher uniquement
### le nombre d'Oscars que ce film a récoltés cette année-là?

	urlaward = "http://www.imdb.com" + link[:-14] + "awards?ref_=tt_awd"
	#print (urlaward)
	contenu3= requests.get(urlaward)
	page3 = BeautifulSoup(contenu3.text,"html.parser")
#	print (page3)

	prix = page3.find_all("h3")

	for p in prix:
		if "Academy Awards, USA" in p.text:
			oscars = p.find_next("table").find_all("tr")
			nbOscars = oscars[0].td["rowspan"]
			print(nbOscars)
			film.append(nbOscars)

# 	autresrecompenses = page3.find_all("h3")
# 	 #print(autresrecompenses)

# 	for holycrap in autresrecompenses:
# 	 	autresnominations=holycrap.text.strip()
# 	 	autrenomm= autresnominations[:-4]
# #	 	print (autrenomm)
# 	 	# film.append(autrenomm)

	print(film)


	hello= open(fichierJHR,"a")
	holla= csv.writer(hello)
	holla.writerow(film) 

### Ma solution n'est pas parfaite, puisqu'il y a des films où on n'a pas l'info sur leurs ventes
### Mon csv est donc décalé
### C'est dur le scraping, j'avoue! :P

#############################






	# autresawards= page2.find_all("a", class_="btn-full")
	# for autre in autresawards:
	# 	autres = autresawards.find_all()
	# 	print (autre)
# 		autresawards= autresawards.a["href"]
# 	print (autresawards)	
# #	for urlautres in autresawards:
#	 	try:
# #	 		urlA= urlautres.a["href"]
# 	 		print (urlA)
# 	 	except:
# 	 		print ("caca")

#############################


#	
#		print (urlautres)
		
		

# 	for urlautres in autresawards:
# 		urlautres= urlautres.a["href"]
# 		print (urlautres)
# #		urlcomplet = "http://www.imdb.com" + link
# #		print (urlcomplet)

##########################
			


#########




#		print(USA)

#	for pays in info[9]:
#		film=[]
#		pays=pays.a[""]
#		print(pays)

	
#	film.append(name)
#	for name in page2.find_all("div", class_= "title_wrapper"):
#		name = page2.find_all("div", class_= "title_wrapper")
#		print (name)
#		nom= name.find("h1)
#		film []


#	nom = name.find("a",id="name")
#	print(nom)
	
	# link= link.a["href"]
	# urlaward= "http://www.imdb.com" + link +"/awards?ref_=tt_awd"
	# print(urlaward)

#	film = []
#	try:
#		film = []
#		urlwtf = link.a[href]
#		print(urlwtf)
#	except:
#		print("fuck")
#urlUnFilm=urlDesFilms.find("a")
#print (urlUnFilm)



#for urlFilm in urlDesFilms:
#	film = []
#	try:
# 		film = []
# 		url2 = urlfilm.a["href"]
# 		print(url2)
# 		url4real = "http://www.imdb.com" + url2
#		print(url4real)
#		film.append(url4real)




#	except:
#		print("Nada")
		












# for wtf in urlDesFilms.find("a href"):
# 	wtf= urlDesFilms.find("a href")
# 	print (wtf)

#for film in urlDesFilms.find_all("a"):
#	urlhref= urlDesFilms.a["href"]
#	print (urlDesFilms)

# for urlUnFilm in urlDesFilms:
#	film= []
# urlhref= urlDesFilms.find("href")
# print (urlhref)


#	urlhref= urlDesFilms.a["href"]
#	print(urlhref)
