# Contenido de la demo Hotel Mar del Plata (A Coruna) (es/ca/en/fr). Hechos de hotelmardelplata.es leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Individual','Twin y Matrimonio','Triple y Familiar'],'ca':['Individual','Twin i Matrimoni','Triple i Familiar'],'en':['Single','Twin and Double','Triple and Family'],'fr':['Individuelle','Twin et Double','Triple et Familiale']}
RD={
'es':['Unos 13 m² con cama de 1,35 m, TV LCD HD, teléfono, wifi gratuito y baño privado con ducha.','Twin económica (15 m²) y estándar (16 m²) con dos camas de 0,90 m; en la twin estándar se puede pedir cuna de viaje sin coste.','La triple, de 19 m², con tres camas de 0,90 m; la familiar, de 27 m², para 4 personas con una cama de 1,35 m y dos de 0,90 m.'],
'ca':['Uns 13 m² amb llit d\'1,35 m, TV LCD HD, telèfon, wifi gratuït i bany privat amb dutxa.','Twin econòmica (15 m²) i estàndard (16 m²) amb dos llits de 0,90 m; a la twin estàndard es pot demanar bressol de viatge sense cost.','La triple, de 19 m², amb tres llits de 0,90 m; la familiar, de 27 m², per a 4 persones amb un llit d\'1,35 m i dos de 0,90 m.'],
'en':['About 13 m² with a 1.35 m bed, HD LCD TV, phone, free wifi and private bathroom with shower.','Economy twin (15 m²) and standard twin (16 m²) with two 0.90 m beds; a travel cot can be requested free of charge in the standard twin.','The triple, 19 m², with three 0.90 m beds; the family room, 27 m², for 4 people with a 1.35 m bed and two 0.90 m beds.'],
'fr':['Environ 13 m² avec lit de 1,35 m, TV LCD HD, téléphone, wifi gratuit et salle de bain privée avec douche.','Twin économique (15 m²) et standard (16 m²) avec deux lits de 0,90 m ; un lit bébé de voyage peut être demandé sans frais dans la twin standard.','La triple, 19 m², avec trois lits de 0,90 m ; la familiale, 27 m², pour 4 personnes avec un lit de 1,35 m et deux lits de 0,90 m.']}
ART={
'hero':('waves',9801,['#1e4f6b','#f0c48a','#f8e3bf','#2f6f8a','#1e4f6b','#12344a']),
'intro':('skyline',9802,['#1e4f6b','#e8aa6a','#f7d9a8','#1c4a5c','#173f4f','#0f2c38']),
'r1':('columns',9811,['#edf1f3','#f6f8f9','#3f7f9a','#1e4f6b','#12344a']),
'r2':('waves',9812,['#22566f','#efc286','#f7e1ba','#33768e','#22566f','#14384b']),
'r3':('hills',9813,['#e5eef1','#f1ebd6','#eec17e','#a3c3c4','#76a0a6','#4d7a82']),
'g1':('waves',9821,['#1b4a64','#eebf82','#f6deb5','#2b6a83','#1b4a64','#103145']),
'g2':('skyline',9822,['#1e4f6b','#e6a766','#f6d7a4','#1b4859','#163c4b','#0e2934']),
'g3':('columns',9823,['#ebf0f2','#f5f7f8','#3b7a95','#1e4f6b','#12344a']),
'g4':('arches',9824,['#eef0f1','#cfdde3','#3f7f9a','#1e4f6b','#12344a']),
'g5':('hills',9825,['#e2ecef','#efe9d2','#ecbe79','#a0c0c1','#739da3','#4a777f']),
'g6':('waves',9826,['#18465f','#ecbc7e','#f5dbb0','#28657e','#18465f','#0e2e40'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Mar del Plata · Frente a la playa de Riazor en A Coruña',see_rooms='Ver habitaciones',hero_k='A Coruña',hero_t='Frente a la playa, junto a Riazor',hero_s='En el centro de A Coruña, enfrente de la playa y al lado del Estadio de Riazor, con el Paseo Marítimo a la salida del hotel.',
 intro_t='Una casa con filosofía familiar',intro_p1='La historia del hotel viene marcada por distintas generaciones de emprendedores con filosofía familiar; algunas habitaciones tienen vistas al mar y, a lo lejos, a la Torre de Hércules.',
 intro_p2='Recepción 24 horas, desayuno buffet, wifi gratuito en todo el hotel y alquiler de bicicletas para recorrer los 9 km del Paseo Marítimo.',
 stats=['Frente a la playa','Recepción 24 h','Desayuno buffet','Mascotas bienvenidas'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Individuales, twin, matrimonio, triples y familiares, todas de no fumadores. Entrada desde las 14:00 y salida hasta las 12:00.',
 svcs=['Recepción 24 horas','Desayuno buffet','Wifi gratuito en todo el hotel','Traslados al aeropuerto','Alquiler de bicicletas','Aparcamiento privado enfrente (de pago)','Mundo Pets para mascotas','Spa en convenio con Casa del Agua'],
 loc_p='Paseo de Ronda, 58 · 15011 A Coruña. Enfrente de la playa y junto al Estadio de Riazor.',
 chips=['¿Qué habitaciones tiene?','¿Admiten mascotas?','¿Hay parking?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Mar del Plata · Davant de la platja de Riazor a la Corunya',see_rooms='Veure habitacions',hero_k='La Corunya',hero_t='Davant de la platja, al costat de Riazor',hero_s='Al centre de la Corunya, davant de la platja i al costat de l\'Estadi de Riazor, amb el Passeig Marítim a la sortida de l\'hotel.',
 intro_t='Una casa amb filosofia familiar',intro_p1='La història de l\'hotel la marquen diverses generacions d\'emprenedors amb filosofia familiar; algunes habitacions tenen vistes al mar i, al lluny, a la Torre d\'Hèrcules.',
 intro_p2='Recepció 24 hores, esmorzar bufet, wifi gratuït a tot l\'hotel i lloguer de bicicletes per recórrer els 9 km del Passeig Marítim.',
 stats=['Davant de la platja','Recepció 24 h','Esmorzar bufet','Mascotes benvingudes'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Individuals, twin, matrimoni, triples i familiars, totes de no fumadors. Entrada des de les 14:00 i sortida fins a les 12:00.',
 svcs=['Recepció 24 hores','Esmorzar bufet','Wifi gratuït a tot l\'hotel','Trasllats a l\'aeroport','Lloguer de bicicletes','Aparcament privat al davant (de pagament)','Mundo Pets per a mascotes','Spa en conveni amb Casa del Agua'],
 loc_p='Paseo de Ronda, 58 · 15011 la Corunya. Davant de la platja i al costat de l\'Estadi de Riazor.',
 chips=['Quines habitacions té?','Admeteu mascotes?','Hi ha pàrquing?','Com es reserva?']),
'en':dict(title='Hotel Mar del Plata · Opposite Riazor beach in A Coruña',see_rooms='See the rooms',hero_k='A Coruña',hero_t='Opposite the beach, next to Riazor',hero_s='In the centre of A Coruña, opposite the beach and next to the Riazor Stadium, with the seafront promenade right outside.',
 intro_t='A family-minded house',intro_p1='The hotel\'s story is marked by several generations of family-minded entrepreneurs; some rooms have sea views and, in the distance, the Tower of Hercules.',
 intro_p2='24-hour reception, buffet breakfast, free wifi throughout the hotel and bike hire to ride the 9 km seafront promenade.',
 stats=['Opposite the beach','24 h reception','Buffet breakfast','Pets welcome'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Single, twin, double, triple and family rooms, all non-smoking. Check-in from 14:00 and check-out until 12:00.',
 svcs=['24-hour reception','Buffet breakfast','Free wifi throughout','Airport transfers','Bike hire','Private car park opposite (paid)','Mundo Pets for pets','Spa through an agreement with Casa del Agua'],
 loc_p='Paseo de Ronda, 58 · 15011 A Coruña. Opposite the beach and next to the Riazor Stadium.',
 chips=['What rooms does it have?','Are pets allowed?','Is there parking?','How do I book?']),
'fr':dict(title='Hotel Mar del Plata · Face à la plage de Riazor à La Corogne',see_rooms='Voir les chambres',hero_k='La Corogne',hero_t='Face à la plage, à côté de Riazor',hero_s='Au centre de La Corogne, face à la plage et à côté du stade de Riazor, avec la promenade maritime à la sortie de l\'hôtel.',
 intro_t='Une maison à l\'esprit familial',intro_p1='L\'histoire de l\'hôtel est marquée par plusieurs générations d\'entrepreneurs à l\'esprit familial ; certaines chambres ont vue sur la mer et, au loin, sur la Tour d\'Hercule.',
 intro_p2='Réception 24h/24, petit-déjeuner buffet, wifi gratuit dans tout l\'hôtel et location de vélos pour parcourir les 9 km de la promenade maritime.',
 stats=['Face à la plage','Réception 24h/24','Petit-déjeuner buffet','Animaux bienvenus'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Individuelles, twin, doubles, triples et familiales, toutes non-fumeurs. Arrivée à partir de 14h00 et départ jusqu\'à 12h00.',
 svcs=['Réception 24h/24','Petit-déjeuner buffet','Wifi gratuit dans tout l\'hôtel','Transferts aéroport','Location de vélos','Parking privé en face (payant)','Mundo Pets pour les animaux','Spa en partenariat avec Casa del Agua'],
 loc_p='Paseo de Ronda, 58 · 15011 La Corogne. Face à la plage et à côté du stade de Riazor.',
 chips=['Quelles chambres a-t-il ?','Les animaux sont-ils admis ?','Y a-t-il un parking ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://app.mews.com/distributor/d17af9a0-6a54-4188-8726-ac8e00b2b9ad?language=es-ES'; REN='https://app.mews.com/distributor/d17af9a0-6a54-4188-8726-ac8e00b2b9ad?language=en-US'; RFR='https://app.mews.com/distributor/d17af9a0-6a54-4188-8726-ac8e00b2b9ad?language=fr-FR'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':REN,'fr':RFR})
D=dict(name='Hotel Mar del Plata',ac='#6b3a1f',ac2='#2f6b5a',ac2_a11y='#235246',book=BOOK,around=[],foot=FOOT,
 address='Paseo de Ronda, 58 · 15011 A Coruña',phones=['+34 981 257 962'],emails=['info@hotelmardelplata.es'],maps='Hotel Mar del Plata, Paseo de Ronda 58, A Coruña',t=T)
META=dict(repo='demo-hotel-mar-del-plata-a-coruna',name='Hotel Mar del Plata',legal_name='Aurea Novo Pena, S.L.',registry_ids=['CIF B70104070','Registro Mercantil de A Coruña'],
 url='https://hotelmardelplata.es/',domain='hotelmardelplata.es',municipality='A Coruña',province='A Coruña',sector='hotel frente a la playa de Riazor en A Coruña',
 read_at='2026-10-29T15:06:00+01:00',created_at='2026-10-29T15:06:00+01:00',built_at='2026-10-29T15:15:00+01:00',audit_date='2026-10-29T15:02:42+01:00',
 rating=dict(value=4.6,coincide=['telefono','web'],date='2026-10-29T10:58:44+01:00',url='https://www.google.com/maps/place/Hotel+Mar+del+Plata/@43.3702162,-8.4164734,17z/data=!4m9!3m8!1s0xd2e7c60dac9baad:0xd7a94d873a4b4560!5m2!4m1!1i2!8m2!3d43.3702162!4d-8.4164734!16s%2Fg%2F1tdmrbjd'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas real del hotel (Mews Distributor, configuracion d17af9a0-6a54-4188-8726-ac8e00b2b9ad, la misma que abre su boton Reservar via mews-init.js); la demo no construye ningun motor.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Tiene habitaciones para familias?','K02'),('¿Dónde está?','K03'),('¿Admiten mascotas?','K04'),('¿Hay parking?','K05'),('¿Tienen desayuno?','K06'),('¿A qué hora es el check-in?','K07'),('¿Hay traslado al aeropuerto?','K08'),('¿Alquilan bicicletas?','K09'),('¿Tienen spa?','K10'),('¿Cómo reservo?','K11'),('¿Quién es el titular?','K12'),('¿Tienen cuna?','K13'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K11'),('¿Tienen piscina?',None),('¿Tienen restaurante para cenar?',None)],
'ca':[('Quines habitacions té?','K01'),('Té habitacions per a famílies?','K02'),('On és?','K03'),('Admeteu mascotes?','K04'),('Hi ha pàrquing?','K05'),('Teniu esmorzar?','K06'),('A quina hora és el check-in?','K07'),('Hi ha trasllat a l\'aeroport?','K08'),('Llogueu bicicletes?','K09'),('Teniu spa?','K10'),('Com reservo?','K11'),('Qui és el titular?','K12'),('Teniu bressol?','K13'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K11'),('Teniu piscina?',None),('Teniu restaurant per sopar?',None)],
'en':[('What rooms does it have?','K01'),('Are there family rooms?','K02'),('Where is it?','K03'),('Are pets allowed?','K04'),('Is there parking?','K05'),('Do you serve breakfast?','K06'),('What time is check-in?','K07'),('Is there an airport transfer?','K08'),('Do you rent bikes?','K09'),('Do you have a spa?','K10'),('How do I book?','K11'),('Who is the owner?','K12'),('Do you have a cot?','K13'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K11'),('Is there a pool?',None),('Is there a restaurant for dinner?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Y a-t-il des chambres familiales ?','K02'),('Où est-il ?','K03'),('Les animaux sont-ils admis ?','K04'),('Y a-t-il un parking ?','K05'),('Servez-vous le petit-déjeuner ?','K06'),('À quelle heure est l\'arrivée ?','K07'),('Y a-t-il un transfert aéroport ?','K08'),('Louez-vous des vélos ?','K09'),('Avez-vous un spa ?','K10'),('Comment réserver ?','K11'),('Qui est le titulaire ?','K12'),('Avez-vous un lit bébé ?','K13'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K11'),('Y a-t-il une piscine ?',None),('Y a-t-il un restaurant pour dîner ?',None)]}
