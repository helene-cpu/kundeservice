# Kundeservice

### Dette er en enkel nettside hvor brukere kan sende inn henvendelser og admin kan svare på henvendelsene som blir sendt tilbake til brukerens epost.

## Prosjekt beskrivelse
### Prosjektet er utviklet med:
 ##### Python (Flask)
##### HTML og CSS
##### MySQL database
##### SendGrid API for e-post

## Funksjoner

##### Innsending av henvendelser via skjema
##### Generering av unikt ordrenummer
##### Lagring av data i MySQL database
##### Admin-login og registrering med hashed passord
##### Admin dashboard for behandling av saker
##### Automatisk sending av svar via e-post (SendGrid)
##### Dynamic templates for e-post
##### Separat navigasjonbar for bruker og admin
##### Brukermanual for veiledning


## Kjøre programmet lokalt

### 1. Installasjoner:
##### Flask
##### Mysql-connector
##### Flask-WTF
##### Sendgrid

### 2. Opprette en database i Mysql
##### Database: kundeservice
##### Tabeller: brukere, saker

### 3. Lag en config.py
##### inkluder API nøkkel og epost

### 4. Dynamic template
##### Opprett bruker på sendgrid og lag et dynamic template

### 5. Start applikasjon
##### python3 app.py

## Kompetansemål
### Utvikling
#### modellere og opprette databaser for informasjonsflyt i systemer - Jeg har laget en MySQL database med tabeller for brukere og saker.
#### beskrive ulike datalagringsmodeller og metoder for å hente ut og sette inn bestemte data fra databaser som brukes av andre systemer- data fra databaser som brukes av andre systemer- Jeg bruker SQL-spørringer for å hente og lagre data i databasen. 
#### analysere digitale trusler, verdier og sårbarheter og utvikle applikasjoner med innebygget sikkerhet- Jeg har implementert sikker innlogging, registrering med hashing og bruker sessions for å beskytte admin-siden.
#### gjøre rede for hensikten med teknisk dokumentasjon og utarbeide teknisk dokumentasjon for IT-løsninger- Jeg har laget README og brukermanual som forklarer hvordan systemet fungerer og hvordan det brukes.
#### vurdere brukergrensesnitt til IT-tjenester og designe tjenester som er tilpasset brukernes behov- Jeg har laget et enkelt og oversiktlig grensesnitt med tydelig navigasjon og god kontrast for bedre tilgjengelighet.

### Brukerstøtte
#### utøve brukerstøtte og veilede i relevant programvare- Jeg har laget en admin-side og brukermanual som viser hvordan systemet brukes.
#### kartlegge behovet for og utvikle veiledninger for brukere og kunder- Jeg har utviklet en manual basert på behovet for opplæring av admin-brukere.
#### bruke og tilpasse kommunikasjonsform og fagterminologi i møte med brukere, kunder og fagmiljø- Systemet er laget med enkelt språk til brukere og mer teknisk språk i admin-delen.
#### gjøre rede for og anvende etiske retningslinjer og relevant lovverk i eget arbeid- Jeg har tatt hensyn til personvern ved behandling av brukerdata.


### Drift
#### planlegge og dokumentere arbeidsprosesser og IT-løsninger- Jeg har dokumentert prosjektet gjennom README og brukermanual.
#### utforske og beskrive komponenter i en driftsarkitektur - Systemet består av flere komponenter i en driftsarkitektur, inkludert klient (nettleser), webserver (Flask), database (MySQL) og eksterne tjenester (SendGrid).
#### gjøre rede for prinsipper og strukturer for skytjenester og virtuelle tjenester- eg har brukt SendGrid som en skytjeneste for e-postutsending, som viser hvordan eksterne API-er kan integreres i en applikasjon.
#### gjennomføre risikoanalyse av nettverk og tjenester i en virksomhets systemer og foreslå tiltak for å redusere risikoen- Jeg har hashet passord og brukt parameteriserte queries. 
#### forenkle og automatisere arbeidsprosesser i utvikling av IT-løsninger- Systemet automatiserer utsending av e-post når en sak besvares.

## Kilder: 
#### Integrate using our Web API or SMTP Relay(Hentet 17 April) https://app.sendgrid.com/guide/integrate/langs/smtp
#### Outdated Dev(25, Februar) Generate Random Strings with Python: A Quick Guide. https://dev.to/outdated-dev/generate-random-strings-with-python-a-quick-guide-1nfm
#### WebAIM (hentet 27 februar) Contrast Checker. https://webaim.org/resources/contrastchecker/