# Partner vCard QR Code

Odoo modul pro generování QR kódů z kontaktů ve formátu vCard.

## Funkce

- Automatické generování QR kódu pro každého partnera/kontaktu
- QR kód obsahuje kompletní kontaktní informace ve formátu vCard 3.0
- Podporované údaje:
  - Jméno a příjmení
  - Organizace a pozice
  - Telefonní čísla (pracovní, mobilní)
  - E-mailová adresa
  - Adresa (ulice, město, PSČ, stát, země)
  - Webová stránka
- Snadný import kontaktu skenováním QR kódu mobilním telefonem

## Instalace

1. Zkopírujte složku `partner_vcard_qr` do adresáře `addons` vaší Odoo instalace
2. Restartujte Odoo server
3. V Odoo aplikaci přejděte do Aplikace → Odstranit seznam aplikací
4. Aktualizujte seznam aplikací
5. Vyhledejte "Partner vCard QR Code" a nainstalujte modul

## Použití

1. Otevřete jakéhokoliv partnera/kontakt v Odoo
2. Přejděte na záložku "QR vCard"
3. Zobrazí se QR kód obsahující všechny kontaktní údaje
4. Skenujte QR kód mobilním telefonem pro automatický import kontaktu

## Požadavky

- Odoo verze 18.0+
- Python knihovna `qrcode` (obvykle již obsažena v Odoo)

## Autor

Jiří Vysloužil  
Email: jiri.vyslouzil2@gmail.com

## Licence

LGPL-3

## Verze

18.0.1.0.0
