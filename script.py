import random
import csv
import datetime

viennoiserie = [   "croissant","3croissant+1offert","pain au chocolat", "3painchocolat+1offert","cookiz","3cookiz+1offert",
                   "pain aux raisins", "maxi-pain-chocolat","pain suisse","pain brioché"]



pains = ["Baguette","3baguette+1offerte", "Pain de campagne", "Pain complet", "Pain aux céréales", "Pain aux noix",
         "Pain aux raisins", "Pain brioché", "Pain aux grains entiers", ]



patisserie = ["rouchet chocolat","tartelette ","flan","eclair","bulle","brownie","tiramisu","millefeuille","galette du rois"]




salade_sandwich=  ["sandwich nordique","salade cesar",
    "salade niçoise","sandwich poulet cesar","salade kalama","sandwich saumon","salade poké","sandwich jombon","ciabata poulet",
     "sandwich thon"]



menu_sandwich= ["menu sandwich nordique","menu salade cesar","menu salade niçoise","menu sandwich poulet cesar",
    "menu salade kalama","menu sandwich saumon","menu salade poké","menus andwich jombon","menu ciabata poulet","menu sandwich thon"]

boisson=["coca", "cocazero","aosis","fanta","lipton","orangina","café","café au lait","capochino","milleshake"]

produit = [   "croissant","3croissant+1offert","pain au chocolat","3painchocolat+1offert", "cookiz","3cookiz+1offert","pain aux raisins",
    "maxi-pain-chocolat", "pain suisse","pain brioché", "Baguette","3baguette+1offerte", "Pain de campagne", "Pain complet",
    "Pain aux céréales", "Pain aux noix","Pain aux raisins", "Pain brioché", "Pain aux grains entiers","rouchet chocolat",
    "tartelette ","flan","eclair","bulle","brownie","tiramisu","millefeuille","sandwich nordique","salade cesar",
    "salade niçoise","sandwich poulet cesar","salade kalama","sandwich saumon","salade poké","sandwich jombon","ciabata poulet",
     "sandwich thon","menu sandwich nordique","menu salade cesar","menu salade niçoise","menu sandwich poulet cesar",
    "menu salade kalama","menu sandwich saumon","menu salade poké","menus andwich jombon","menu ciabata poulet",
        "menu sandwich thon","coca", "cocazero","aosis","fanta","lipton","orangina","café","café au lait","capochino","milleshake"]



prix={"croissant":1.00,"3croissant+1offert":3,"pain au chocolat":1.10,"3painchocolat+1offert":3.30,"cookiz":0.90,"3cookiz+1offert":2.70,
    "pain aux raisins":1.03,"maxi-pain-chocolat":1.50,"pain suisse":1.30, "pain brioché":1.00, "Baguette":1.00,
      "3baguette+1offerte":3.50, "Pain de campagne":1.50, "Pain complet":1.90, "Pain aux céréales":2.50, "Pain aux noix":2.50,
         "Pain aux raisins":2.50, "Pain brioché":1.90, "Pain aux grains entiers":2.50,"rouchet chocolat":3.20,"tartelette ":3.20,
      "flan":3.50,"eclair":3.50,"bulle":4.00,"brownie":3.50,"tiramisu":3.50,"millefeuille":2.90,"sandwich nordique":5.00,
      "salade cesar":6.50,"salade niçoise":6.50,"sandwich poulet cesar":6.50,"salade kalama":7.00,"sandwich saumon":7.00,
      "salade poké":7.90,"sandwich jombon":5.00,"ciabata poulet":6.00,"sandwich thon":6.00,"menu sandwich nordique":8.50,
      "menu salade cesar":9.50,"menu salade niçoise":9.50,"menu sandwich poulet cesar":9.50,
    "menu salade kalama":9.90,"menu sandwich saumon":9.90,"menu salade poké":10.80,"menus andwich jombon":8.50,
      "menu ciabata poulet":8.90,"menu sandwich thon":8.90,"coca":1.70, "cocazero":1.70,"aosis":1.70,"fanta":1.70,
      "lipton":1.70,"orangina":1.70,"café":1.50,"café au lait":1.90,"capochino":1.90,"milleshake":3.90}


id_article={"croissant":1,"3croissant+1offert":2,"pain au chocolat":3,"3painchocolat+1offert":4,"cookiz":5,"3cookiz+1offert":6,
    "pain aux raisins":7,"maxi-pain-chocolat":8,"pain suisse":9, "pain brioché":10, "Baguette":11,
      "3baguette+1offerte":12, "Pain de campagne":13, "Pain complet":14, "Pain aux céréales":15, "Pain aux noix":16,
         "Pain aux raisins":17, "Pain brioché":18, "Pain aux grains entiers":19,"rouchet chocolat":20,"tartelette ":21,
      "flan":22,"eclair":23,"bulle":24,"brownie":25,"tiramisu":26,"millefeuille":27,"sandwich nordique":28,
      "salade cesar":29,"salade niçoise":30,"sandwich poulet cesar":31,"salade kalama":32,"sandwich saumon":33,
      "salade poké":34,"sandwich jombon":35,"ciabata poulet":36,"sandwich thon":37,"menu sandwich nordique":38,
      "menu salade cesar":39,"menu salade niçoise":40,"menu sandwich poulet cesar":41,
    "menu salade kalama":42,"menu sandwich saumon":43,"menu salade poké":44,"menus andwich jombon":45,
      "menu ciabata poulet":46,"menu sandwich thon":47,"coca":48, "cocazero":49,"aosis":50,"fanta":51,
      "lipton":52,"orangina":53,"café":54,"café au lait":55,"capochino":56,"milleshake":57}

all_produit=[]
id_produit=0



start_date = datetime.date(2021, 1, 1)
end_date = datetime.date(2021, 12, 31)
delta = datetime.timedelta(days=1)
lis_date=[]
for single_date in range((end_date - start_date).days + 1):
    current_date = start_date + datetime.timedelta(days=single_date)
    lis_date.append(current_date)

total=0
crois=0
a=0
b=0
prixvie=0
vente_final=[]
for dat in lis_date:
          if dat<=lis_date[165]:
              n = random.randint(250, 350)
              for i in range(n):
                l = [1, 2, 3, 4, 5, 6, 7, 8]
                x = random.choices(l, weights=(90, 50, 20, 10, 5, 5, 5, 5), k=1)

                y = x[0]

                vente = random.choices(produit, weights=(70, 50, 70, 50, 80, 50, 15, 20, 15, 10, 80, 50, 10,
                                                         30, 10, 5, 5, 5, 5, 15, 15, 15, 10, 15, 10, 10, 15, 5, 15, 5, 5, 5,
                                                         5, 5, 5, 5, 5, 5,
                                                         5, 7, 6, 8, 5, 7, 8, 5, 6, 7, 8, 6, 7, 8, 8, 5, 5, 5, 5), k=y)

                for e in vente:
                    if e in viennoiserie:
                        id_produit = 1
                    elif e in pains:
                        id_produit = 2

                    elif e in patisserie:
                        id_produit = 3

                    elif e in salade_sandwich:
                        id_produit = 4

                    elif e in menu_sandwich:
                        id_produit = 5
                    elif e in boisson:
                        id_produit = 6

                    vente_final.append((dat, id_article[e], e, prix[e], id_produit))

                    total += prix[e]
                    if e == "croissant":
                        crois += 1

                    if e == "3croissant+1offert":
                        a += 1
                    if e == "menu sandwich thon":
                        b += 1
          elif  dat<=lis_date[250] :

                n= random.randint(800,850)


                for i in range (n) :

                    l =  [1,2,3,4,5,6,7,8]
                    x= random.choices( l ,  weights=(90, 50, 20 , 10, 5, 5,5,5), k=1)

                    y= x[0]

                    vente=random.choices(produit ,weights=(70,50, 70, 50, 80, 50,15,20,15,10,80,50,10,
                                                           30,10,5,5,5,5,15,15,15,10,15,10,10,15,5,15,5,5,5,5,5,5,5,5,5,
                                                           5,7,6,8,5,7,8,5,6,7,8,6,7,8,8,5,5,5,5), k=y)


                    for e in vente:
                        if e in viennoiserie:
                            id_produit = 1
                        elif e in pains:
                            id_produit = 2

                        elif e in patisserie:
                            id_produit = 3

                        elif e in salade_sandwich:
                            id_produit = 4

                        elif e in menu_sandwich:
                            id_produit = 5
                        elif e in boisson:
                            id_produit = 6

                        vente_final.append((dat,id_article[e],e,prix[e],id_produit))

                        total+= prix[e]
                        if e== "croissant":
                           crois+= 1

                        if e == "3croissant+1offert":
                            a+=1
                        if e == "menu sandwich thon":
                             b+=1

          elif dat>=lis_date[250]:
            n = random.randint(500, 550)

            for i in range(n):
                l = [1, 2, 3, 4, 5, 6, 7, 8]
                x = random.choices(l, weights=(90, 50, 20, 10, 5, 5, 5, 5), k=1)

                y = x[0]

                vente = random.choices(produit, weights=(70, 50, 70, 50, 80, 50, 15, 20, 15, 10, 80, 50, 10,
                                                         30, 10, 5, 5, 5, 5, 15, 15, 15, 10, 15, 10, 10, 15, 5, 15, 5, 5, 5,
                                                         5, 5, 5, 5, 5, 5,
                                                         5, 7, 6, 8, 5, 7, 8, 5, 6, 7, 8, 6, 7, 8, 8, 5, 5, 5, 5), k=y)

                for e in vente:
                    if e in viennoiserie:
                        id_produit = 1
                    elif e in pains:
                        id_produit = 2

                    elif e in patisserie:
                        id_produit = 3

                    elif e in salade_sandwich:
                        id_produit = 4

                    elif e in menu_sandwich:
                        id_produit = 5
                    elif e in boisson:
                        id_produit = 6

                    vente_final.append((dat, id_article[e], e, prix[e], id_produit))

                    total += prix[e]
                    if e == "croissant":
                        crois += 1

                    if e == "3croissant+1offert":
                        a += 1
                    if e == "menu sandwich thon":
                        b += 1
print(vente_final)
print(total)
print(crois)
print(a)
print(b)
print (prixvie)

with open('vente2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['date','id_produit', 'product_name', 'price', 'id_category'])

    for record in vente_final:
        writer.writerow(record)