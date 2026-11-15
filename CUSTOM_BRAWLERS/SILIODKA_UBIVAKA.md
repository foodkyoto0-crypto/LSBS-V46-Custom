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
- Intended main attack: 5-shot automatic burst
- Intended damage: 300 per projectile (up to 1,500 if all five hit)
- Current server CSV still points to Colt's skill; the 5-shot/300 values are a target spec, not active gameplay behavior
- Intended super: throw an explosive fish can
- Super fish-can projectile and explosion: not implemented yet

## Server changes
- Added a separate character row to Classes/Files/assets/csv_logic/characters.csv.
- Mirrored the row in ContentUpdater/Content/assets/csv_logic/characters.csv.
- Added unlock, health, attack, and super card rows to Classes/Files/assets/csv_logic/cards.csv. The active unlock card ID is 503; four disabled rows reserve earlier indexes.
- Mirrored cards.csv to ContentUpdater/Content/assets/csv_logic/cards.csv.
- Restored Shelly's original health and skill references; Shelly remains a separate, unchanged character.

## Client/APK requirements
The server repository has no battle simulation or client asset source for implementing custom projectile behavior. It also does not include the V46 APK or its model, texture, icon, animation, localization, or skill resources. A matching modified APK/client is required to implement and test the fish model, five-shot 300-damage burst, and explosive fish-can super. The new ID and TID must also be recognized by the client. Until a matching APK is built and tested, do not assume the character will appear or be selectable in-game.
