# SilodKaYbivaka — custom brawler

Status: server-side prototype entry added. A matching V46 client/APK update is still required before this can be confirmed playable.

## Identity
- Display name: SilodKaYbivaka
- Internal character name: SilodKaYbivaka
- Server-side character ID: 169 (based on current CSV row order)
- Temporary visual base: Shelly (BanditGirlDefault)
- Role: damage dealer
- Rarity: Legendary

## Description
A fearless silver herring in a tactical vest with an automatic blaster. She sprays enemies with rapid fire and turns an ordinary fish can into an explosive surprise. Never underestimate the fish!

## Prototype stats
- Health: 5,000
- Movement speed: 720
- Main attack: Colt's automatic blaster skill (GunslingerWeapon)
- Super: Colt's super skill (GunslingerUlti) as a temporary placeholder
- Target damage: not yet customized; currently inherited from the placeholder skill
- Super fish-can projectile: not implemented yet

## Server changes
- Added a separate character row to Classes/Files/assets/csv_logic/characters.csv.
- Mirrored the row in ContentUpdater/Content/assets/csv_logic/characters.csv.
- Added unlock, health, attack, and super card rows to Classes/Files/assets/csv_logic/cards.csv.
- Restored Shelly's original health and skill references; Shelly remains a separate, unchanged character.

## Client/APK requirements
This repository change alone does not add the custom fish model, texture, icon, animations, localized name/description, or custom attack/super assets to the V46 APK. The new ID and TID must also be recognized by the client. Until a matching APK is built and tested, do not assume the character will appear or be selectable in-game.
