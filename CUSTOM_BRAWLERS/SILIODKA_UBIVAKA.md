# SilodKaYbivaka — custom brawler

Status: design prototype only. This file does not register a playable brawler in the V46 client or server.

## Identity
- Display name: SilodKaYbivaka
- Internal name: ShotgunGirl (temporary compatibility base)
- Temporary visual base: Shelly (ShotgunGirl / BanditGirlDefault)
- Role: damage dealer
- Rarity: Legendary

## Description
A fearless silver herring with a tactical vest and an automatic blaster. She sprays enemies with a rapid burst and turns an ordinary fish can into an explosive surprise. Never underestimate the fish!

## Base stats (prototype targets)
- Health: 5,000
- Movement speed: 720
- Main attack: automatic blaster
- Target damage: 300 per projectile
- Firing pattern: rapid 5-shot burst
- Super: explosive fish-can projectile (not implemented yet)

## Implementation notes
The current server-side prototype reuses Shelly's existing character row, so the game may still show Shelly's original name, description, model, and icon. The display name and description above are the intended custom text; they will appear in-game only after the matching localization and client resources are added to the V46 APK.

A fully separate playable character requires a new compatible character/card ID and client-side resources/definitions. Do not claim this is complete until the APK recognizes the new ID, weapon, animations, icon, and localization.
