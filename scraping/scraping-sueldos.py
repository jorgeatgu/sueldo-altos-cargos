import requests
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import html5lib
import csv
import time


session = requests.session()
res = ''
headers = {'User-Agent': 'Mozilla/5.0'}

lista = [
    'https://sueldode.org/patricia-franco-jimenez/',
    'https://sueldode.org/patricia-goma-pons/',
    'https://sueldode.org/patricia-juana-gomez-i-picard/',
    'https://sueldode.org/patricio-valverde-espin/',
    'https://sueldode.org/patxi-xabier-aizpurua-telleria/',
    'https://sueldode.org/paul-ortega-etcheverry/',
    'https://sueldode.org/paula-fernandez-viana/',
    'https://sueldode.org/paula-gomez-angulo-amoros/',
    'https://sueldode.org/paula-maria-alvarez-herrera/',
    'https://sueldode.org/paz-fernandez-mendaza/',
    'https://sueldode.org/pedro-acosta-robles/',
    'https://sueldode.org/pedro-afonso-padron/',
    'https://sueldode.org/pedro-agustin-pernias-peco/',
    'https://sueldode.org/pedro-alvarez-palomino/',
    'https://sueldode.org/pedro-angullo-ruiz/',
    'https://sueldode.org/pedro-anitua-aldekoa/',
    'https://sueldode.org/pedro-antonio-ruiz-santos/',
    'https://sueldode.org/pedro-guitart-gonzalez-valerio/',
    'https://sueldode.org/pedro-irigoyen-barja/',
    'https://sueldode.org/pedro-j-garcia-carmona/',
    'https://sueldode.org/pedro-javier-jauregui-fernandez/',
    'https://sueldode.org/pedro-jimenez-ramirez/',
    'https://sueldode.org/pedro-luis-bazaco-atucha/',
    'https://sueldode.org/pedro-manuel-castro-cobos/',
    'https://sueldode.org/pedro-manuel-rollan-ojeda/',
    'https://sueldode.org/pedro-maria-azpiazu-uriarte/',
    'https://sueldode.org/pedro-maria-pellejero-goni/',
    'https://sueldode.org/pedro-medina-rebollo/',
    'https://sueldode.org/pedro-munoz-barco/',
    'https://sueldode.org/pedro-ortega-rodriguez/',
    'https://sueldode.org/pedro-pascual-hernandez-verges/',
    'https://sueldode.org/pedro-perez-eslava/',
    'https://sueldode.org/pedro-rivera-barrachina/',
    'https://sueldode.org/peli-manterola-arteta/',
    'https://sueldode.org/pere-aragones-garcia/',
    'https://sueldode.org/pere-martinez-ammetller/',
    'https://sueldode.org/pere-padrosa-pierre/',
    'https://sueldode.org/pere-palacin-farre/',
    'https://sueldode.org/pere-perello-payeras/',
    'https://sueldode.org/perfecto-rodriguez-muinos/',
    'https://sueldode.org/pilar-alegria-continente/',
    'https://sueldode.org/pilar-blanco-morales-limones/',
    'https://sueldode.org/pilar-costa-i-serra/',
    'https://sueldode.org/pilar-garces-garcia/',
    'https://sueldode.org/pilar-gomez-lopez/',
    'https://sueldode.org/pilar-heras-trias/',
    'https://sueldode.org/pilar-herrera-rodriguez/',
    'https://sueldode.org/pilar-irigoien-ostiza/',
    'https://sueldode.org/pilar-navarro-rodriguez/',
    'https://sueldode.org/pilar-salazar-vela/',
    'https://sueldode.org/pilar-serrano-boigas/',
    'https://sueldode.org/pilar-sorribas-arenas/',
    'https://sueldode.org/pilar-valero-huescar/',
    'https://sueldode.org/pilar-varela-diaz/',
    'https://sueldode.org/pilar-ventura-contreras/',
    'https://sueldode.org/polentzi-urquijo-sagredo/',
    'https://sueldode.org/purificacion-galvez-daza/',
    'https://sueldode.org/purificacion-perez-hidalgo/',
    'https://sueldode.org/rafael-ariza-fernandez/',
    'https://sueldode.org/rafael-carbonell-peris/',
    'https://sueldode.org/rafael-carretero-guerra/',
    'https://sueldode.org/rafael-chacon-sanchez/',
    'https://sueldode.org/rafael-climent-gonzalez/',
    'https://sueldode.org/rafael-cubero-rivera/',
    'https://sueldode.org/rafael-de-la-sierra-gonzalez/',
    'https://sueldode.org/rafael-escuredo-rodriguez/',
    'https://sueldode.org/rafael-iturriaga-nieva/',
    'https://sueldode.org/rafael-lopez-fernandez/',
    'https://sueldode.org/rafael-lopez-iglesias/',
    'https://sueldode.org/rafael-lores-domingo/',
    'https://sueldode.org/rafael-manuel-kutz-garaizabal/',
    'https://sueldode.org/rafael-marquez-berral/',
    'https://sueldode.org/rafael-moreno-segura/',
    'https://sueldode.org/rafael-peral-sorroche/',
    'https://sueldode.org/rafael-perezagua-delgado/',
    'https://sueldode.org/rafael-pini-sereno/',
    'https://sueldode.org/rafael-rodriguez-de-la-cruz/',
    'https://sueldode.org/rafael-sanchez-bargiela/',
    'https://sueldode.org/rafael-sanchez-herrero/',
    'https://sueldode.org/rafael-solana-lara/',
    'https://sueldode.org/rafael-van-grieken-salvador/',
    'https://sueldode.org/rafaela-sanchez-benitez/',
    'https://sueldode.org/ramon-lara-sanchez/',
    'https://sueldode.org/ramon-simon-campa/',
    'https://sueldode.org/ramon-tejedor-sanz/',
    'https://sueldode.org/raquel-huete-nieves/',
    'https://sueldode.org/raquel-saenz-blanco/',
    'https://sueldode.org/raul-enriquez-caba/',
    'https://sueldode.org/raul-olivan-cortes/',
    'https://sueldode.org/raul-pelayo-pardo/',
    'https://sueldode.org/raul-perales-acedo/',
    'https://sueldode.org/rebeca-torro-soler/',
    'https://sueldode.org/regina-leal-eizaguirre/',
    'https://sueldode.org/reinaldo-fernandez-manzano/',
    'https://sueldode.org/remedios-lajara-dominguez/',
    'https://sueldode.org/remedios-martel-gomez/',
    'https://sueldode.org/remedios-palma-zambrana/',
    'https://sueldode.org/reyes-alvarez-ossorio-garcia-de-soria/',
    'https://sueldode.org/ricard-font-hereu/',
    'https://sueldode.org/ricardo-almale-bandres/',
    'https://sueldode.org/ricardo-borja-de-la-sota-galdiz/',
    'https://sueldode.org/ricardo-cuevas-campos/',
    'https://sueldode.org/ricardo-gonzalez-mantero/',
    'https://sueldode.org/ricardo-jesus-dominguez-garcia-baquero/',
    'https://sueldode.org/ricardo-jose-duran-rodriguez/',
    'https://sueldode.org/ricardo-lamadrid-intxaurraga/',
    'https://sueldode.org/ricardo-suarez-arguelles/',
    'https://sueldode.org/robert-fabregat-fuentes/',
    'https://sueldode.org/roberto-perez-elorza/',
    'https://sueldode.org/roberto-suarez-malagon/',
    'https://sueldode.org/rocio-briones-morales/',
    'https://sueldode.org/rocio-lucas-navas/',
    'https://sueldode.org/rodrigo-gartzia-azurmendi/',
    'https://sueldode.org/rodrigo-sanchez-haro/',
    'https://sueldode.org/rogelio-llanes-ribas/',
    'https://sueldode.org/roman-rodriguez-gonzalez/',
    'https://sueldode.org/roque-martinez-escandell/',
    'https://sueldode.org/rosa-aguilar-rivero/',
    'https://sueldode.org/rosa-amalia-deniz-santana/',
    'https://sueldode.org/rosa-davila-mamely/',
    'https://sueldode.org/rosa-eva-diaz-tezanos/',
    'https://sueldode.org/rosa-isabel-rios-martinez/',
    'https://sueldode.org/rosa-jimenez-reyes/',
    'https://sueldode.org/rosa-josefa-molero-manes/',
    'https://sueldode.org/rosa-maria-balas-torres/',
    'https://sueldode.org/rosa-maria-castillejo-caiceo/',
    'https://sueldode.org/rosa-maria-cihuelo-simon/',
    'https://sueldode.org/rosa-maria-martinez-rivada/',
    'https://sueldode.org/rosa-maria-sierra-sanchez/',
    'https://sueldode.org/rosa-maria-vilas-nunez/',
    'https://sueldode.org/rosa-quintana-carballo/',
    'https://sueldode.org/rosa-vidal-planella/',
    'https://sueldode.org/rosalia-gonzalo-lopez/',
    'https://sueldode.org/rosana-montanes-fandos/',
    'https://sueldode.org/rosanna-lopez-salgueiro/',
    'https://sueldode.org/rosario-rey-garcia/',
    'https://sueldode.org/rosario-torres-ruiz/',
    'https://sueldode.org/roser-gali-izard/',
    'https://sueldode.org/ruben-goni-urroz/',
    'https://sueldode.org/ruben-manuel-garcia-gonzalez/',
    'https://sueldode.org/ruben-rubio/',
    'https://sueldode.org/ruben-trenzano-juan/',
    'https://sueldode.org/sabino-torre-diez/',
    'https://sueldode.org/sagrario-castro-vidal/',
    'https://sueldode.org/salvador-palazon-ferrando/',
    'https://sueldode.org/sandra-garcia-armesto/',
    'https://sueldode.org/santiago-david-negrin-dorta/',
    'https://sueldode.org/santiago-gonzalez-prado/',
    'https://sueldode.org/santiago-miguel-rodriguez-hernandez/',
    'https://sueldode.org/santiago-salas-lechon/',
    'https://sueldode.org/santiago-valencia-vila/',
    'https://sueldode.org/santiago-vicente-amor-barreiro/',
    'https://sueldode.org/sara-guadalupe-arteaga-darias/',
    'https://sueldode.org/sara-negueruela-garcia/',
    'https://sueldode.org/sara-pagola-aizpiri/',
    'https://sueldode.org/sebastia-sanso-i-jaume/',
    'https://sueldode.org/sebastian-celaya-perez/',
    'https://sueldode.org/sebastian-delgado-amaro/',
    'https://sueldode.org/segundo-benitez-fernandez/',
    'https://sueldode.org/serafin-carballo-garcia/',
    'https://sueldode.org/sergi-tudela-casanovas/',
    'https://sueldode.org/sergio-eiroa-santana/',
    'https://sueldode.org/sergio-emilio-juanena-guruceta/',
    'https://sueldode.org/sergio-fernando-alonso-rodriguez/',
    'https://sueldode.org/sergio-lopez-barrancos/',
    'https://sueldode.org/sergio-perez-pueyo/',
    'https://sueldode.org/severino-alvarez-monteserin/',
    'https://sueldode.org/silvia-gonzalez/',
    'https://sueldode.org/silvia-quesada-escobar/',
    'https://sueldode.org/sol-maria-vazquez-abeal/',
    'https://sueldode.org/soledad-monzon-cabrera/',
    'https://sueldode.org/sonia-diaz-de-corcuera-ruiz-de-ona/',
    'https://sueldode.org/sonia-gaya-sanchez/',
    'https://sueldode.org/sonia-pazos-alvarez/',
    'https://sueldode.org/susana-garcia-dacal/',
    'https://sueldode.org/susana-ibanez-rosa/',
    'https://sueldode.org/susana-lopez-abella/',
    'https://sueldode.org/susana-pastor-pons/',
    'https://sueldode.org/susana-rodriguez-carballo/',
    'https://sueldode.org/tatiana-begona-gonzalez-san-sebastian/',
    'https://sueldode.org/teresa-azcona-alejandre/',
    'https://sueldode.org/teresa-chavarria-gimenez/',
    'https://sueldode.org/teresa-molina-lopez/',
    'https://sueldode.org/teresa-prohias-ricart/',
    'https://sueldode.org/teresa-sevillano-abad/',
    'https://sueldode.org/teresa-suarez-genovard/',
    'https://sueldode.org/teresa-vega-valdivia/',
    'https://sueldode.org/tomas-arrieta-heras/',
    'https://sueldode.org/tomas-fernandez-couto-juanas/',
    'https://sueldode.org/tomas-guajardo-cuervo/',
    'https://sueldode.org/tomas-marcial-perez-gonzalez/',
    'https://sueldode.org/torcuato-manuel-romero-lopez/',
    'https://sueldode.org/urbano-garcia-alonso/',
    'https://sueldode.org/v-luis-sanudo-alonso-de-celis/',
    'https://sueldode.org/valentin-garcia-gomez/',
    'https://sueldode.org/valentina-granados-simon/',
    'https://sueldode.org/valeriano-martinez-garcia/',
    'https://sueldode.org/vanesa-solorzano-villegas/',
    'https://sueldode.org/veronica-lopez-garcia/',
    'https://sueldode.org/veronica-lopez-ramon/',
    'https://sueldode.org/vicenc-vidal-i-matas/',
    'https://sueldode.org/vicent-marza-ibanez/',
    'https://sueldode.org/vicent-soler-i-marco/',
    'https://sueldode.org/vicente-dominguez-martinez/',
    'https://sueldode.org/vicente-guillen-izquierdo/',
    'https://sueldode.org/vicente-hoyos-montero/',
    'https://sueldode.org/vicente-zarza-vazquez/',
    'https://sueldode.org/victor-cullell-i-comellas/',
    'https://sueldode.org/victor-manuel-solla-barcena/',
    'https://sueldode.org/victor-oroz-izaguirre/',
    'https://sueldode.org/victoria-eugenia-nogueira-valladares/',
    'https://sueldode.org/violante-tomas-olivares/',
    'https://sueldode.org/virginia-arnaiz-gonzalez/',
    'https://sueldode.org/virginia-marco-carcel/',
    'https://sueldode.org/virginia-martinez-saiz/',
    'https://sueldode.org/vitelio-manuel-tena-piazuelo/',
    'https://sueldode.org/xabier-patxi-arrieta-goiri/',
    'https://sueldode.org/xabier-unanue-ortega/',
    'https://sueldode.org/xavier-bernadi-gil/',
    'https://sueldode.org/xavier-gatius-garriga/',
    'https://sueldode.org/xavier-navarro-i-garcia/',
    'https://sueldode.org/yasmina-garcia-hernandez/',
    'https://sueldode.org/yolanda-beldarrain-salaberria/',
    'https://sueldode.org/yolanda-blanco-rodriguez/',
    'https://sueldode.org/yolanda-caballero-aceituno/',
    'https://sueldode.org/yolanda-ibarrola-de-la-fuente/',
    'https://sueldode.org/zosimo-darias-armas/',
    'https://sueldode.org/zulima-perez-segui/']


with open('sueldos-ccaa.csv', 'w') as f:
    # Lo segundo es crear el escritor de CSV
    fileCSV = csv.writer(f)
    # Ahora añadimos las columnas del CSV
    fileCSV.writerow(['Nombre', 'CCAA', 'Sueldo'])

    # Ahora iteramos sobre la lista de URLS
    for link in lista:
        res = session.get(link, headers=headers)

        data = res.text
        soup = BeautifulSoup(data, 'html5lib')
        contenedor_lista = soup.find('div', {"class": "entry-content"})

        nombre = soup.find('h1', {"class": "entry-title"})
        nombre = nombre.text

        ccaa = contenedor_lista.findNext('h2')
        ccaa = ccaa.text

        sueldo = soup.select_one(".entry-content p:nth-of-type(3) strong").nextSibling

        print(nombre)
        print(ccaa)
        print(sueldo)

        fileCSV.writerow([nombre, ccaa, sueldo])

        time.sleep(15)



