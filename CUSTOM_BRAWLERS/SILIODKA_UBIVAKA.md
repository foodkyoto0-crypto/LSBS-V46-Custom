# СільодкаУбівака — custom brawler concept

Status: design prototype only. This file does not register a playable brawler in the V46 client or server.

## Identity
- Display name: СільодкаУбівака
- Internal name: HerringKiller
- Temporary visual base: Shelly (ShotgunGirl / BanditGirlDefault)
- Role: damage dealer
- Rarity: Legendary

## Base stats (prototype targets)
- Health: 5,000
- Movement speed: 720
- Main attack: automatic blaster
- Target damage: 300 per projectile
- Firing pattern: rapid 5-shot burst
- Super: explosive fish-can projectile (to be implemented after client compatibility is confirmed)

## Implementation notes
A new playable character requires a matching character/card ID and client-side resources/definitions. Reusing Shelly's model alone is not enough: the V46 APK must recognize the new ID, weapon, animations, and localization. Do not overwrite Shelly's existing row or modify player database files as a shortcut.

Next implementation step: identify a safe unused character/card ID and verify how this server maps CSV rows to client IDs. Then add the server-side row and player unlock in a backward-compatible way, followed by matching client assets/definitions.
