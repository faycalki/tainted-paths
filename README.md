![Logo of the project](https://media.moddb.com/images/members/1/286/285487/icon_for_moddb_and_steam.gif)

![Picture](https://media.moddb.com/images/mods/1/35/34552/20171015151356_1.jpg)

![Picture](https://media.moddb.com/images/mods/1/35/34552/20170923224624_1.jpg)

![Picture](https://media.moddb.com/images/mods/1/35/34552/20171015144417_1.jpg)

![Picture](https://media.moddb.com/images/mods/1/35/34552/20171021194048_1.jpg)

![Picture](https://media.moddb.com/images/mods/1/35/34552/20171015151316_1.jpg)


# Tainted Paths
Tainted Paths is a full game modification of Mount & Blade: Warband written with over 100000 lines of custom code, custom assets as well as a vision for a more fun and intense experience, it attempts to provide you with a fun and unique large scale experience as well as a captivating story that is shaped by you, the player. From swords and chainmails to muskets and plate armours you will be able to fight and conquer in multiple time periods and across multiple continents.

## Installing / Getting started

A quick introduction of the minimal setup you need to get Medieval Conquests up and running
1. Make sure you have a copy of Mount & Blade: Warband video game
2. Download the latest build from Moddb at: https://www.moddb.com/mods/tainted-paths or the releases page in github.
3. Insert the module into the Modules folder in your game folder, launch the game and switch the module from the launcher into the name of the overhaul.

## Developing

Here's a brief intro about what a developer must do in order to start developing
the project further

unfortunately Python 3 is not supported by the warband module system, so you'll have to install Python 2.7 in order to further develop this project, here are some steps to install Python 2.7 easily, but any other method would work as long as the version between 2 to 2.8 of Python.

First, git clone the repository for the latest source code.
```shell
sudo apt-get update
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
cd /usr/src
sudo tar xzf Python-2.7.16.tgz
sudo wget https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz
cd Python-2.7.16
sudo ./configure --enable-optimizations
sudo make altinstall
```

1. After installing Python, obtain the latest build files from ModDb hosting website or at the Github releases page.
2. Adjust the export directory within module_info.py to the game's full module folder.
3. Run build_module.bat and wait for the compilation to finish.
4. Once the compilation finishes successfully, attempt to launch the project within the game Mount & Blade: Warband's by switching the Module from "Native" to the project's name.
5. Play and enjoy your new changes.


## Features
The features of the overhaul are listed in descending order from latest additions to oldest.

- Multiple unique pieces of gear, that are acquireable only through certain methods, such as the famed fictional Excalibur which allows you to slice through multiple enemies with each attack!

- Over 1600+ new items freshly made for you to experience!

- Several religions included in the game, as well as the ability to change or leave your religion.

- Multiple cultures included in the game, as well as the ability to change your culture!

- Brand new world map covering most of earth, spanning from the Americas all the way to the middle east and back!

- Improved siege battles, featuring catapults, trebuchets, battering rams, and your old favorite ladders too of course!

- Weather systems featuring sandstorms, dust storms, and blizzards!

- Multiple starting choices, ranging from a respected Monarch, all the way to a lowly bandit or pirate!

- Player permanent death and characters permanent death!

- Disasters, affecting everyone in the game depending on certain traits and skills they might have!

- Coup d'etat and conspiracies!

- Religious wars and massive holy wars!

- Unique character leveling and trait adaptability

- Rivalries

- Improved combat flow with animations, sounds, and textures!

- Horn sounds during battles for both AI and the player!

- Deep quests intertwined within the world, where your decisions shape their course

- Decapitation and gore!

- Fully rewritten combat system!

- Fully rewritten political system, ranging from military alliances, to declaring war. Also a place where rivalries can arise when disagreements happen!

- Deep financial and political system: taxing, culture, building structures, and more!

- Monarchies and Republics, each with their own changes in Politics and Finance!

- Unsettled land where you can build your own settlements!

- An intuitive and revolutionary battle commanding system, allowing you to dive deep into the heat of battle and control your armies to the best extent possible!

- Selectable eras to play featuring different factions and gear!

- Improved AI decision making, making them able to produce strategies both in the overworld and during battles by using tactical strategies to beat their opponent

- Improved AI combat systems (feint, kick, retreat, reform, track, backup, formations, shield bash and more!)

- Hundreds of new events depending on your character status (King-vassal-neither).

- World-map events such as storms, floods, fires, epidemics and more.

- Particle effects for hitting shields.

- Weapon breaking

- Hardcore mode makes several changes to the game making every battle important towards your characters wellbeing, with persistant injuries, and other things to discover.

- Extended camera mode, allowing the player to adjust the camera to their preference, you can now view in your character in a top down view, and any angle you want.

- Troops use torches during night-time.

- Dynamic skybox!

- Terrain-aware music system for all situations, depending on where you are, and what is going on. Providing the player with an immersive experience into the world!

- Political marriages!

- Random Events while travelling some with benefits/consequences depending on the choice you choose!

- Even more Random Events for Kings with benefits/consequences depending on the choice you choose!

- Realistic Ballistics.

- Realistic sounds from hitting a wooden shield to grunting and death sounds.

- Many other features!

## Contributing

This project's custom code is licensed under MIT, all native warband code and assets are NOT covered by the MIT license.

This module has several contributors listed in the taleworlds page and special thanks to everyone who assisted.

## Links
- Project homepage: https://forums.taleworlds.com/index.php?topic=371652.0
- Mirror 1: https://www.moddb.com/mods/tainted-paths
- Mirror 2: https://www.nexusmods.com/mbwarband/mods/6206
- Repositories and my other projects: https://github.com/faycalki/
  - In case of sensitive bugs like security vulnerabilities, please feel free to contact me whenever, I value all efforts to improve the security of the project.
