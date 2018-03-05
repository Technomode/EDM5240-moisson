# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

fichier = "film.csv"

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
	name= nameetdate[:-6]
	date= nameetdate[-6:]
	print(name)
	print(date)

	film.append(name)
	film.append(date)

	directors= page2.find_all(attrs={"itemprop" : "director"}) 
	#print(directors)
	
	for director in directors:

		#print(director.text.strip())
		try:
			d = director.text.strip().split(":")
			print(d[0])
			film.append(d[0])
##            if d[0]=="Director":
##				realisateur= d[1]
#				print(realisateur)
##				film.append(realisateur)
##			else:
##				print("°")
		except:
			print("Impossible de trouver le directeur")


	infos= page2.find_all("div", class_="txt-block")
			#print (infos)

	
	for info in infos:
#		print (info.text.strip())
		
		try:
			i= info.text.strip().split(":")
			
			if i[0]=="Country":
				country = i[1]
#				print(country)
				film.append(country)
			if i[0]== "Budget":
				budget =i[1]
#				print(budget)
				film.append(budget)
			if i[0]== "Gross USA":
				gross= i[1]	
#				print(gross)
				film.append(gross)

			
			else:
				print("-")
			
		except:
			print("")
	

	urlaward = "http://www.imdb.com" + link[:-14] + "awards?ref_=tt_awd"
	#print (urlaward)
	contenu3= requests.get(urlaward)
	page3 = BeautifulSoup(contenu3.text,"html.parser")
#	print (page3)
	




	autresrecompenses = page3.find_all("h3")
	 #print(autresrecompenses)

	for holycrap in autresrecompenses:
	 	autresnominations=holycrap.text.strip()
	 	autrenomm= autresnominations[:-4]
#	 	print (autrenomm)
	 	film.append(autrenomm)

	print(film)


	hello= open(fichier,"a")
	holla= csv.writer(hello)
	holla.writerow(film) 





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
