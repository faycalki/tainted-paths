from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

factions = [
	("no_faction", "No Faction", 0, 0.9, []),

	("commoners", "Commoners", 0, 0.1, [("player_faction",0.10),("undeads",-0.70),("outlaws",-0.60)]),

	("outlaws", "Outlaws", 0, 0.5, [("kingdom_13",-0.05),("kingdom_58",-0.05),("africa_people",-0.05),("kingdom_47",-0.05),("kingdom_57",-0.05),("kingdom_62",-0.05),("east_euro_people",-0.05),("kingdom_32",-0.05),("kingdom_33",-0.05),("kingdom_53",-0.05),("kingdom_11",-0.05),("kingdom_19",-0.05),("kingdom_46",-0.05),("american_native",-0.05),("kingdom_49",-0.05),("player_faction",-0.15),("kingdom_35",-0.05),("kingdom_23",-0.05),("kingdom_60",-0.05),("kingdom_1",-0.05),("kingdom_40",-0.05),("kingdom_36",-0.05),("kingdom_41",-0.05),("kingdom_44",-0.05),("kingdom_6",-0.05),("kingdom_38",-0.05),("kingdom_29",-0.05),("kingdom_20",-0.05),("mid_euro_people",-0.05),("indochina_people",-0.05),("kingdom_34",-0.05),("china_people",-0.05),("kingdom_3",-0.05),("kingdom_25",-0.05),("kingdom_64",-0.05),("kingdom_50",-0.05),("pioneers",-0.05),("arabian_people",-0.05),("kingdom_43",-0.05),("kingdom_48",-0.05),("kingdom_9",-0.05),("kingdom_59",-0.05),("kingdom_30",-0.05),("kingdom_42",-0.05),("kingdom_14",-0.05),("kingdom_45",-0.05),("kingdom_24",-0.05),("kingdom_63",-0.05),("kingdom_51",-0.05),("kingdom_21",-0.05),("kingdom_52",-0.05),("kingdom_18",-0.05),("kingdom_2",-0.05),("kingdom_37",-0.05),("kingdom_26",-0.05),("kingdom_31",-0.05),("kingdom_17",-0.05),("kingdom_10",-0.05),("japan_people",-0.05),("kingdom_15",-0.05),("kingdom_56",-0.05),("kingdom_28",-0.05),("kingdom_55",-0.05),("kingdom_8",-0.05),("kingdom_66",-0.05),("commoners",-0.60),("kingdom_27",-0.05),("kingdom_67",-0.05),("kingdom_16",-0.05),("kingdom_12",-0.05),("hindu_people",-0.05),("kingdom_7",-0.05),("nomad_people",-0.05),("player_supporters_faction",-0.08),("kingdom_5",-0.05),("kingdom_54",-0.05),("kingdom_65",-0.05),("kingdom_22",-0.05),("kingdom_4",-0.05),("kingdom_61",-0.05),("kingdom_39",-0.05)], [], 0x00888888),

	("neutral", "Neutral", 0, 0.1, [], [], 0x00ffffff),

	("tradeport", "Tradeport", 0, 0.1, [], [], 0x00a3ccff),

	("ally_faction_for_slot", "Ally faction for slot", 0, 0.5, [], [], 0x00c37187),

	("enemy_faction_for_slot", "Enemy faction for slot", 0, 0.5, []),

	("hot_points", "Hot points", 0, 0.1, [], [], 0x00ffa1a8),

	("player_faction", "Player Faction", 0, 0.9, [("undeads",-0.50),("commoners",0.10),("player_supporters_faction",1.00),("outlaws",-0.15)], [], 0x00706d5a),

	("player_supporters_faction", "Player's Supporters", 0, 0.9, [("player_faction",1.00),("outlaws",-0.08)], [], 0x00706d5a),

	("kingdom_1", "Joseon", 0, 0.9, [("outlaws",-0.05)], [], 0x00bdba24),

	("kingdom_2", "Macedonia", 0, 0.9, [("outlaws",-0.05)], [], 0x005ad2f1),

	("kingdom_3", "Carthage", 0, 0.9, [("outlaws",-0.05)], [], 0x005f2112),

	("kingdom_4", "Ghurid", 0, 0.9, [("outlaws",-0.05)], [], 0x00abf052),

	("kingdom_5", "Rome", 0, 0.9, [("outlaws",-0.05)], [], 0x00911098),

	("kingdom_6", "Crusader States", 0, 0.9, [("outlaws",-0.05)], [], 0x00fcfbfb),

	("kingdom_7", "Kievan Rus", 0, 0.9, [("outlaws",-0.05)], [], 0x00f368ff),

	("kingdom_8", "France", 0, 0.9, [("outlaws",-0.05)], [], 0x002b6cc3),

	("kingdom_9", "Achaemenid", 0, 0.9, [("outlaws",-0.05)], [], 0x00e6090a),

	("kingdom_10", "Anglo-Scandinavian", 0, 0.9, [("outlaws",-0.05)], [], 0x0088ffbb),

	("kingdom_11", "Holy Roman Empire", 0, 0.9, [("outlaws",-0.05)], [], 0x00ffff00),

	("kingdom_12", "Sweden", 0, 0.9, [("outlaws",-0.05)], [], 0x004dd71c),

	("kingdom_13", "Ayyubid", 0, 0.9, [("outlaws",-0.05)], [], 0x00ebe800),

	("kingdom_14", "Khwarazmian", 0, 0.9, [("outlaws",-0.05)], [], 0x009e0b6f),

	("kingdom_15", "Poland", 0, 0.9, [("outlaws",-0.05)], [], 0x00ff0000),

	("kingdom_16", "Lithuania", 0, 0.9, [("outlaws",-0.05)], [], 0x000092b0),

	("kingdom_17", "Liu Bei", 0, 0.9, [("outlaws",-0.05)], [], 0x0012b314),

	("kingdom_18", "England", 0, 0.9, [("outlaws",-0.05)], [], 0x00931124),

	("kingdom_19", "Sun Ce", 0, 0.9, [("outlaws",-0.05)], [], 0x00ef0000),

	("kingdom_20", "Muromachi shogunate", 0, 0.9, [("outlaws",-0.05)], [], 0x00ff1f58),

	("kingdom_21", "Jadaran", 0, 0.9, [("outlaws",-0.05)], [], 0x007163a5),

	("kingdom_22", "Khereid", 0, 0.9, [("outlaws",-0.05)], [], 0x00baff4b),

	("kingdom_23", "Espana", 0, 0.9, [("outlaws",-0.05)], [], 0x00d85ac4),

	("kingdom_24", "Hungary", 0, 0.9, [("outlaws",-0.05)], [], 0x00448415),

	("kingdom_25", "Portugal", 0, 0.9, [("outlaws",-0.05)], [], 0x00350b86),

	("kingdom_26", "Byzantine Empire", 0, 0.9, [("outlaws",-0.05)], [], 0x007b0033),

	("kingdom_27", "Khmer", 0, 0.9, [("outlaws",-0.05)], [], 0x00ff00ff),

	("kingdom_28", "Cao Cao", 0, 0.9, [("outlaws",-0.05)], [], 0x001010ff),

	("kingdom_29", "Jurchen", 0, 0.9, [("outlaws",-0.05)], [], 0x00a86500),

	("kingdom_30", "Mongol Empire", 0, 0.9, [("outlaws",-0.05)], [], 0x00a33e32),

	("kingdom_31", "Ma Teng", 0, 0.9, [("outlaws",-0.05)], [], 0x00763001),

	("kingdom_32", "Huns", 0, 0.9, [("outlaws",-0.05)], [], 0x00666147),

	("kingdom_33", "Majapahit", 0, 0.9, [("outlaws",-0.05)], [], 0x00862554),

	("kingdom_34", "Songhai", 0, 0.9, [("outlaws",-0.05)], [], 0x0075823e),

	("kingdom_35", "Lu Bu", 0, 0.9, [("outlaws",-0.05)], [], 0x00818182),

	("kingdom_36", "Yuan Shao", 0, 0.9, [("outlaws",-0.05)], [], 0x00ffbc00),

	("kingdom_37", "Liu Biao", 0, 0.9, [("outlaws",-0.05)], [], 0x008adaff),

	("kingdom_38", "Liu Zhang", 0, 0.9, [("outlaws",-0.05)], [], 0x004b0061),

	("kingdom_39", "Gongsun Zan", 0, 0.9, [("outlaws",-0.05)], [], 0x00ff3e00),

	("kingdom_40", "Morocco", 0, 0.9, [("outlaws",-0.05)], [], 0x00e32a82),

	("kingdom_41", "XiXia", 0, 0.9, [("outlaws",-0.05)], [], 0x00b655ff),

	("kingdom_42", "Yuan Shu", 0, 0.9, [("outlaws",-0.05)], [], 0x00ff00bb),

	("kingdom_43", "LiJue GuoSi", 0, 0.9, [("outlaws",-0.05)], [], 0x00eae961),

	("kingdom_44", "Kara Khitan", 0, 0.9, [("outlaws",-0.05)], [], 0x00ff744a),

	("kingdom_45", "Inca", 0, 0.9, [("outlaws",-0.05)], [], 0x00eed66a),

	("kingdom_46", "Aztec", 0, 0.9, [("outlaws",-0.05)], [], 0x00923f1f),

	("kingdom_47", "Novgorod", 0, 0.9, [("outlaws",-0.05)], [], 0x00915ac1),

	("kingdom_48", "Galicia-Volyn", 0, 0.5, [("outlaws",-0.05)], [], 0x00c15c30),

	("kingdom_49", "Granada", 0, 0.5, [("outlaws",-0.05)], [], 0x00d0ac6a),

	("kingdom_50", "American natives", 0, 0.9, [("outlaws",-0.05)], [], 0x00b8c0c0),

	("kingdom_51", "Aksum", 0, 0.9, [("outlaws",-0.05)], [], 0x00b3e345),

	("kingdom_52", "Tibet", 0, 0.9, [("outlaws",-0.05)], [], 0x009f9fb9),

	("kingdom_53", "Scotland", 0, 0.9, [("outlaws",-0.05)], [], 0x00a9cd19),

	("kingdom_54", "Ireland", 0, 0.9, [("outlaws",-0.05)], [], 0x00ff7045),

	("kingdom_55", "Teutonic Order", 0, 0.9, [("outlaws",-0.05)], [], 0x00dbdbdb),

	("kingdom_56", "Abassid", 0, 0.9, [("outlaws",-0.05)], [], 0x00d0ac6a),

	("kingdom_57", "Almohad", 0, 0.9, [("outlaws",-0.05)], [], 0x005f2112),

	("kingdom_58", "Aragon", 0, 0.9, [("outlaws",-0.05)], [], 0x0012b314),

	("kingdom_59", "Leon", 0, 0.9, [("outlaws",-0.05)], [], 0x00b8c0c0),

	("kingdom_60", "Sicily", 0, 0.9, [("outlaws",-0.05)], [], 0x005ad2f1),

	("kingdom_61", "Denmark", 0, 0.9, [("outlaws",-0.05)], [], 0x0075823e),

	("kingdom_62", "Song", 0, 0.9, [("outlaws",-0.05)], [], 0x00ffbc00),

	("kingdom_63", "Taira", 0, 0.9, [("outlaws",-0.05)], [], 0x00911098),

	("kingdom_64", "Fujiwara", 0, 0.9, [("outlaws",-0.05)], [], 0x008adaff),

	("kingdom_65", "Minamoto", 0, 0.9, [("outlaws",-0.05)], [], 0x00ef0000),

	("kingdom_66", "Uesugi", 0, 0.9, [("outlaws",-0.05)], [], 0x007163a5),

	("kingdom_67", "Shimazu", 0, 0.9, [("outlaws",-0.05)], [], 0x00baff4b),

	("kingdoms_end", "{!}kingdoms end", 0, 0.0, []),

	("pioneers", "Pioneers", 0, 0.5, [("outlaws",-0.05)], [], 0x00a76e32),

	("africa_people", "Africans tribe", 0, 0.5, [("outlaws",-0.05)], [], 0x00a76e32),

	("nomad_people", "Nomads", 0, 0.5, [("outlaws",-0.05)], [], 0x00a28e39),

	("hindu_people", "Hindus tribe", 0, 0.5, [("outlaws",-0.05)], [], 0x0028989b),

	("china_people", "Independent states", 0, 0.5, [("outlaws",-0.05)], [], 0x00b0b286),

	("indochina_people", "Indochinas tribe", 0, 0.5, [("outlaws",-0.05)], [], 0x00dcb2c6),

	("arabian_people", "Arabians tribe", 0, 0.5, [("outlaws",-0.05)], [], 0x00b36d19),

	("mid_euro_people", "Independent european states", 0, 0.5, [("outlaws",-0.05)], [], 0x00fc8800),

	("east_euro_people", "Independent eastern states", 0, 0.5, [("outlaws",-0.05)], [], 0x0093a884),

	("american_native", "Americans tribe", 0, 0.5, [("outlaws",-0.05)], [], 0x0079ae5c),

	("japan_people", "Independent clan", 0, 0.5, [("outlaws",-0.05)], [], 0x0079ae5c),

	("undeads", "{!}Undeads", 0, 0.5, [("player_faction",-0.50),("commoners",-0.70)]),

]