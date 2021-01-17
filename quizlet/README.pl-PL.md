# *Quizlet* - strategie oszukiwania
| Typ oszustwa              | Wykonalne?    |
| -----------------         |:-------------:|
| Wyciek klucza odpowiedzi  | TAK           |
| Wyciek odpowiedzi innych  | NIE           |
| Obejście zabezpieczeń     | NIE DOTYCZY   |
| Zwiększenie limitu czasu  | NIE           |
| Spamowanie/floodowanie    | TAK           |
| Inne                      | 1             |

## Wyciek klucza odpowiedzi
 Istnieje do tego działający skrypt.
 - Pobierz przeglądarkę obsługującą rozszerzenia (na telefonie najlepszy Firefox)
- Zainstaluj dodatek Tampermonkey [[Firefox](https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/)] [[Chrome](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=en)]
- Dodaj skrypt stealer.user.js do Tampermonkey, klikając [[Ten przycisk](https://raw.githubusercontent.com/PetrusTryb/school-hacks/main/quizlet/stealer.user.js)]
- Wejdź na https://quizlet.com/live, wpisz kod gry w oba pola.
- Przy każdej rundzie klikaj "obtain correct answers". Poprawne odpowiedzi pokażą się w rogu ekranu i będą się klikać za Ciebie!

## Wyciek odpowiedzi innych
Nie sprawdzone, ponieważ istnieją metody kradzieży poprawnych odpowiedzi.

## Obejście zabezpieczeń
W Quizizz nie ma ochrony przed oszustwami.

## Zwiększenie limitu czasu
Nie sprawdzone, ponieważ działa wykradanie poprawnych odpowiedzi. Ranking opiera się również na czasie, więc w Twoim interesie jest jak najszybsze rozwiązanie quizu.

## Spamowanie/floodowanie
Bardzo proste, bez captcha. Możesz użyć spambota: https://raw.githubusercontent.com/PetrusTryb/school-hacks/main/quizlet/spam.py

## Inne
 - Atak siłowy na kody rozgrywek (uzyskiwanie dostępu do losowych quizów):
    https://raw.githubusercontent.com/PetrusTryb/school-hacks/main/quizlet/brute.py