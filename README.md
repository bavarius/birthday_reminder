Das ist ein Geburtstags-Benachrichtiger, der nach dem Login in einem Terminalfenster angezeigt werden soll.
Das kleine Programm ist für den deutschsprachigen Raum gedacht. - Umlaute sollen angezeigt werden können!

Das Programm wurde ursprünglich von c't als VB-Script veröffentlicht.
Ich habe es dann nach python portiert. -
So kann es plattformübergreifend laufen.

Die Daten kommen aus birthday.ini. Wenn eine Jahreszahl dabei steht, wird das Alter berechnet.
Die Anzahl der Tage, an denen vor dem Geburtstag benachrichtigt werden soll,
ist durch einen internen Parameter einstellbar. - Die Meldung erscheint dann für alle Geburtstagskinder,
deren Geburtstag in diesem Zeitraum liegt, bis nach dem Geburtstag.

Jetzt wäre der Plan, dass ich persönliche Informationen aus dem Projekt entferne. -
Die Datei mit den Geburtstagen soll dem Programm übergeben werden.
