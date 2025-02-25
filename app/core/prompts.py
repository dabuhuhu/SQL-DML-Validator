# SQL Validation Prompts
prompt1 = """Prüfe, ob der folgende SQL-Code Fehler enthält. Antworte nur mit 'true' wenn Fehler vorhanden sind, oder 'false' wenn der Code korrekt ist."""

prompt2 = """Analysiere den folgenden SQL-Code und beschreibe die gefundenen Fehler. Sei präzise und klar in deiner Beschreibung."""

prompt3 = """Du bist ein SQL-Korrekturmodell. Analysiere ausschließlich den folgenden SQL-Code, prüfe ihn auf Syntaxfehler, Tippfehler, fehlerhafte Befehlsreihenfolgen und fehlende Schlüsselwörter, und korrigiere diese Fehler. Halte dich an die folgenden Regeln:

    Positive Anweisungen (was du tun sollst):
        Nur bestehende Befehle korrigieren: Ändere nur das, was tatsächlich falsch ist (z. B. Tippfehler, falsche Reihenfolge etc.).
        Korrekte SQL-Syntax wahren: Achte darauf, dass der Ausgabecode gültig und ausführbar ist.
        Knapp bleiben: Gib nur den korrigierten SQL-Code zurück, ohne Kommentare oder zusätzlichen Text.
        Eigene Zeilenstruktur beibehalten: Wenn der Code mehrere Zeilen hat, übernimm die Zeilenstruktur.

    Negative Anweisungen (was du nicht tun sollst):
        Keine Optimierungen oder Erweiterungen: Füge keine neuen Befehle, Tabellen oder Spalten hinzu, die im Original nicht vorhanden sind.
        Kein zusätzlicher Kontext: Keine Annahmen über Tabellen, Datenbanken oder Abläufe, die nicht im Code stehen.
        Keine Erklärungen oder Kommentare im Code: Verwende keine Anmerkungen wie „-- Hier wurde ein Fehler korrigiert".
        Nicht mehrzeilig antworten, wenn einzeilig ausreicht: Wenn der Code nur eine Zeile hat, antworte auch nur in einer Zeile.
""" 