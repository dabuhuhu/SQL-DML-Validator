prompt1 = "Überprüfe, ob der folgende SQL Code korrekt ist. Ignoriere ob ein Semikolon (;) fehlt. Dies ist hier nicht relevant. Wenn der Code korrekt ist antworte nur mit 'FALSE' wenn er fehlerhaft ist mit 'TRUE':"

prompt2 = """Überprüfe den folgenden SQL-Code auf Fehler. Analysiere den Code systematisch, finde und liste die Fehler auf. Für jeden Fehler gib eine kurze Beschreibung und dessen Art (z. B. Tippfehler, Syntaxfehler). Gib keine vollständige Korrektur des Codes zurück. Ignoriere fehlende Semikolons (;) und halte deine Antwort kurz und prägnant.

    Positive Anweisungen (was du tun sollst):
        Systematische Analyse: Gehe den Code von links nach rechts durch.
        Fehleridentifikation: Finde konkrete Fehler (z. B. Tippfehler, Syntaxfehler, falsche Schlüsselwörter).
        Kurze Fehlerbeschreibung: Zu jedem Fehler kurz erläutern, warum er problematisch ist (ohne in eine lange Erklärung zu gehen).
        Kategorisieren: Ordne den Fehler z. B. als Syntaxfehler, Tippfehler oder semantischen Fehler ein.

    Negative Anweisungen (was du nicht tun sollst):
        Keine vollständige Korrektur: Liefere ausschließlich die Fehler, keine korrigierte Version des Codes.
        Keine ausführlichen Erklärungen: Verzichte auf umfangreiche Hintergrundinformationen oder SQL-Grundlagen.
        Kein weiterer Kontext: Mach keine Annahmen über Datenbanken, Tabellen oder zusätzliche Informationen.
        Nicht auf fehlende Semikolons hinweisen: Fehler aufgrund fehlender Semikolons sind zu ignorieren.
        """

prompt3 = """
Du bist ein SQL-Korrekturmodell. Analysiere ausschließlich den folgenden SQL-Code, prüfe ihn auf Syntaxfehler, Tippfehler, fehlerhafte Befehlsreihenfolgen und fehlende Schlüsselwörter, und korrigiere diese Fehler. Halte dich an die folgenden Regeln:“

    Positive Anweisungen (was du tun sollst):
        Nur bestehende Befehle korrigieren: Ändere nur das, was tatsächlich falsch ist (z. B. Tippfehler, falsche Reihenfolge etc.).
        Korrekte SQL-Syntax wahren: Achte darauf, dass der Ausgabecode gültig und ausführbar ist.
        Knapp bleiben: Gib nur den korrigierten SQL-Code zurück, ohne Kommentare oder zusätzlichen Text.
        Eigene Zeilenstruktur beibehalten: Wenn der Code mehrere Zeilen hat, übernimm die Zeilenstruktur.

    Negative Anweisungen (was du nicht tun sollst):
        Keine Optimierungen oder Erweiterungen: Füge keine neuen Befehle, Tabellen oder Spalten hinzu, die im Original nicht vorhanden sind.
        Kein zusätzlicher Kontext: Keine Annahmen über Tabellen, Datenbanken oder Abläufe, die nicht im Code stehen.
        Keine Erklärungen oder Kommentare im Code: Verwende keine Anmerkungen wie „-- Hier wurde ein Fehler korrigiert“.
        Nicht mehrzeilig antworten, wenn einzeilig ausreicht: Wenn der Code nur eine Zeile hat, antworte auch nur in einer Zeile.
Hier ist der SQL-Code für deine Analyse:
"""
