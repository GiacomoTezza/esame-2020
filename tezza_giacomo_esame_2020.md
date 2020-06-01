# ELABORATO INDIVIDUALE DI INFORMATICA E SISTEMI E RETI
#### Classe: **5AI**, Alunno: **Tezza Giacomo**
----------

## Analisi
<!-- Dalla descrizione della realtà di interesse, ipotizzo l'autoscuola necessiti di un'applicazione web divisa in due parti. La prima, pubblica, che permetta di mostrare le informazioni sui corsi per le varie patenti ai clienti e potenziali clienti. La seconda, interna, per la gestione degli iscritti e dei loro relativi esami, accessibile solo al personale dell'autoscuola.

Scelgo quindi di implementare questa divisione tramite un login che permette al personale della autoscuola di accedere alle funzionalità interne che non devono essere visibili da tutti. -->

- Evito il CF per privacy.
- Assumo non si possano conseguire più patenti contemporaneamente.


## Modello Concettuale ER
![ER](https://link)


## Modello Logico
```
license(ID, Name, Description)
client(ID, Name, Surname)
test(LicenceID, ClientID, DATE, PASSED)
```


## Query significative
```sql

```