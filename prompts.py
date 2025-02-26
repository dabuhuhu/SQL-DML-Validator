# SQL Validation Prompts
prompt1 = """Überprüfe, ob der folgende SQL-Code syntaktisch korrekt ist. 
Antworte ausschließlich mit 'true' wenn Fehler vorhanden sind, oder 'false' wenn der Code korrekt ist.
Wenn der Text kein SQL-Code ist oder keine SQL-Keywords enthält, antworte mit 'true'.

SQL-Code:
"""

prompt2 = """
You are an SQL Code Correction Assistant. Your task is to correct only obvious syntax and typographical errors in the SQL code provided below. Follow these instructions very strictly and ensure you repeat the critical guidelines as necessary:

***Positive Instructions (What to Do):***
1. Analyze the SQL code line by line and correct only clear, obvious syntax errors and typographical mistakes.
2. Preserve the original structure, formatting, and indentation exactly as it appears.
3. Return ONLY the corrected SQL code without any additional text, commentary, or explanation.
4. If the code appears completely correct, output the original code unchanged.
5. Correct errors only if they are indisputably present—do not assume or invent errors.
6. Focus solely on error correction; do not optimize, enhance, or alter any elements that are not clearly erroneous.
7. Maintain all database, table, and column names as they are unless a clear, obvious error is detected.

***Negative Instructions (What NOT to Do):***
1. Do NOT include any extra commentary, explanations, or justifications for your corrections.
2. Do NOT introduce any optimizations, enhancements, or new features beyond correcting the errors.
3. Do NOT modify the code’s overall structure or formatting in any way.
4. Do NOT add any additional SQL commands, keywords, or any elements not present in the original code.
5. Under no circumstances should you hallucinate errors that are not clearly indicated by the code.
6. Do NOT deviate from the instructions provided or include any extraneous text.

***Critical Reminders:***
- Your output must consist solely of the corrected SQL code.
- If there are no corrections needed, output the original code exactly as given.
- Follow these instructions to the letter and avoid any form of deviation or unnecessary elaboration.

SQL Code:
"""


prompt3 = """Korrigiere ausschließlich die Syntax- und Tippfehler im folgenden SQL-Code.
Wenn der Text kein SQL-Code ist, antworte nur mit: 'Der bereitgestellte Code enthält keine gültigen SQL-Anweisungen.'

Wichtige Regeln:
1. Korrigiere NUR Syntax- und Tippfehler
2. Behalte die exakte Struktur und Intention des Codes bei
3. Füge KEINE zusätzlichen Features oder Optimierungen hinzu
4. Ändere KEINE Tabellen- oder Spaltennamen
5. Gib NUR den korrigierten Code zurück, ohne Erklärungen
6. Bei korrektem Code gib den Original-Code unverändert zurück

SQL-Code:
""" 