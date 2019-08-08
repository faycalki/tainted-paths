from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0

parties = [
	("main_party", "Player Army", icon_player_horseman|pf_limit_members, no_menu, pt_none, fac_player_faction, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [(trp_player, 1, 0)]),

	("temp_party", "None", icon_player|pf_disabled, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("camp_bandits", "{!}camp bandits", icon_player|pf_disabled, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [(trp_temp_troop, 3, 0)]),

	("exparty_backup", "{!}", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("temp_party_2", "{!}temp party 2", icon_player|pf_disabled, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("temp_casualties", "{!}casualties", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("temp_casualties_2", "{!}casualties", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("temp_casualties_3", "{!}casualties", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("temp_wounded", "{!}enemies wounded", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("temp_killed", "{!}enemies killed", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("main_party_backup", "{!} ", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("encountered_party_backup", "{!} ", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("collective_friends_backup", "{!} ", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("player_casualties", "{!} ", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("enemy_casualties", "{!} ", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("ally_casualties", "{!} ", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("collective_enemy", "{!}collective enemy", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("collective_ally", "{!}collective ally", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("collective_friends", "{!}collective ally", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("total_enemy_casualties", "{!} ", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("routed_enemies", "{!}routed enemies", icon_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("zendar", "none", icon_point_mark|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("town_1", "nnn", icon_point_mark|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("castle_1", "nnn", icon_point_mark|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("village_1", "nnn", icon_point_mark|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("salt_mine", "nnn", icon_point_mark|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("four_ways_inn", "nnn (inn)", icon_point_mark|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("test_scene", "test scene", icon_point_mark|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("battlefields", "battlefields", icon_point_mark|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("dhorak_keep", "Dhorak Keep", icon_point_mark|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("training_ground", "Training ground", icon_cantsee|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("training_ground_1", "Training ground", icon_cantsee|pf_disabled|pf_label_large|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [], 100.0),

	("training_ground_2", "Training ground", icon_cantsee|pf_disabled|pf_label_large|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [], 100.0),

	("training_ground_3", "Training ground", icon_cantsee|pf_disabled|pf_label_large|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [], 100.0),

	("training_ground_4", "Training ground", icon_cantsee|pf_disabled|pf_label_large|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [], 100.0),

	("training_ground_5", "Training ground", icon_cantsee|pf_disabled|pf_label_large|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [], 100.0),

	("pyongyang", "Pyongyang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1144.42, -170.76), [], 170.0),

	("hanseong", "Hanseong", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1158.0, -152.04), []),

	("hoeryong", "Hoeryong", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1186.4, -212.0), [], 125.0),

	("hamhung", "Hamhung", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1165.2, -185.2), [], 45.0),

	("jeonju", "Jeonju", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1157.76, -130.56), [], 245.0),

	("gaesung", "Gaesung", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1152.76, -158.24), [], 175.0),

	("chungju", "Chungju", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1167.8, -144.6), [], 260.0),

	("jinju", "Jinju", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1170.32, -121.64), [], 95.0),

	("sangju", "Sangju", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1170.88, -137.04), [], 55.0),

	("gilju", "Gilju", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1179.2, -194.0), [], 65.0),

	("uiju", "Uiju", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1132.4, -182.0), [], 125.0),

	("gangleung", "Gangleung", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1178.64, -152.8), [], 75.0),

	("busan", "Busan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1181.04, -123.44), [], 280.0),

	("jeju", "Jeju", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1152.8, -101.76), [], 100.0),

	("hyesan", "Hyesan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1171.16, -199.42), [], 110.0),

	("gongju", "Gongju", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1160.12, -138.52), [], 120.0),

	("haeju", "Haeju", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1145.48, -156.14), [], 130.0),

	("naju", "Naju", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1154.92, -120.56), [], 170.0),

	("cheongjin", "Cheongjin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1187.8, -205.36), [], 170.0),

	("wonsan", "Wonsan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1162.6, -171.08), [], 260.0),

	("sokcho", "Sokcho", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1175.0, -159.08), [], 45.0),

	("myohyangsan", "Myohyangsan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1153.8, -183.28), [], 125.0),

	("nampo", "Nampo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1139.98, -166.6), []),

	("chuncheon", "Chuncheon", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1165.84, -155.6), [], 270.0),

	("ganggae", "Ganggae", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1153.28, -194.08), [], 110.0),

	("ulsan", "Ulsan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1182.8, -127.2), [], 240.0),

	("athens", "Athens", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-29.68, -156.4), [], 260.0),

	("sparta", "Sparta", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-16.52, -145.2), [], 180.0),

	("pella", "Pella", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-6.68, -202.76), [], 110.0),

	("crete", "Crete", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-43.6, -122.0), [], 180.0),

	("dalmatia", "Dalmatia", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (39.2, -224.8), [], 160.0),

	("philippopolis", "Philippopolis", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-41.2, -209.96), [], 240.0),

	("buthrotum", "Buthrotum", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (12.48, -183.64), [], 15.0),

	("patra", "Patra", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-8.46, -159.28), []),

	("larissa", "Larissa", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-16.24, -178.8), [], 15.0),

	("sarajevo", "Sarajevo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (28.16, -232.36), [], 180.0),

	("trikala", "Trikala", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-8.0, -177.6), [], 45.0),

	("corinth", "Corinth", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-22.28, -152.16), [], 240.0),

	("thessalonica", "Thessalonica", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-21.16, -190.56), [], 240.0),

	("khania", "Khania", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-32.4, -125.6), [], 90.0),

	("sardika", "Sardika", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-25.44, -217.32), [], 155.0),

	("darryhachium", "Darryhachium", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (16.16, -195.64), [], 45.0),

	("arta", "Arta", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-0.76, -172.56), [], 180.0),

	("carthage", "Carthage", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (118.88, -142.56), [], 25.0),

	("gabes", "Gabes", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (122.2, -109.68), [], 75.0),

	("bejaia", "Bejaia", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (174.96, -140.48), [], 90.0),

	("syracuse", "Syracuse", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (63.86, -146.1), [], 120.0),

	("hadrumetum", "Hadrumetum", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (113.72, -129.76), [], 255.0),

	("tarabulus", "Tarabulus", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (85.52, -94.52), [], 270.0),

	("palermo", "Palermo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (84.0, -157.04), [], 35.0),

	("annaba", "Annaba", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (145.2, -141.8), [], 10.0),

	("lilybaeum", "Lilybaeum", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (91.76, -153.8), [], 90.0),

	("gaspar", "Gaspar", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (133.24, -114.04), [], 80.0),

	("sirte", "Sirte", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (48.72, -75.8), [], 180.0),

	("constantine", "Constantine", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (157.44, -137.08), [], 240.0),

	("laghouat", "Laghouat", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (197.84, -106.4), [], 155.0),

	("tebessa", "Tebessa", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (140.8, -125.48), [], 275.0),

	("agra", "Agra", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-618.36, -36.76), [], 175.0),

	("karachi", "Karachi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-502.8, -7.2), [], 30.0),

	("indore", "Indore", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-599.08, 15.96), [], 35.0),

	("satna", "Satna", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-653.12, -4.24), [], 115.0),

	("multan", "Multan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-547.0, -65.68), [], 245.0),

	("nagpur", "Nagpur", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-634.0, 33.2), [], 120.0),

	("allahabad", "Allahabad", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-666.4, -13.94), [], 130.0),

	("kota", "Kota", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-598.88, -10.2), [], 180.0),

	("jaipur", "Jaipur", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-597.96, -28.52), [], 180.0),

	("bikaner", "Bikaner", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-571.12, -41.48), [], 185.0),

	("jaisalmer", "Jaisalmer", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-542.62, -26.5), [], 180.0),

	("quetta", "Quetta", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-502.48, -65.72), [], 10.0),

	("rome", "Rome", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (92.8, -206.4), [], 135.0),

	("ravenna", "Ravenna", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (98.8, -243.16), [], 135.0),

	("messana", "Messana", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (62.4, -157.6), [], 280.0),

	("brundisium", "Brundisium", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (34.12, -189.24), [], 260.0),

	("verona", "Verona", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (109.56, -254.12), [], 280.0),

	("liguria", "Liguria", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (139.2, -246.4), [], 65.0),

	("cagliari", "Cagliari", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (130.4, -174.8), [], 145.0),

	("capua", "Capua", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (78.64, -199.48), [], 145.0),

	("croton", "Croton", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (44.6, -171.04), [], 275.0),

	("aquileia", "Aquileia", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (82.56, -259.04), [], 90.0),

	("arretium", "Arretium", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (101.32, -229.72), [], 225.0),

	("bologna", "Bologna", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (106.08, -240.2), [], 180.0),

	("neapolis", "Neapolis", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (73.72, -193.56), []),

	("ajaccio", "Ajaccio", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (132.0, -206.8), [], 160.0),

	("salerno", "Salerno", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (67.6, -191.12), [], 55.0),

	("pescara", "Pescara", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (74.8, -213.44), [], 15.0),

	("foggia", "Foggia", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (58.36, -201.56), [], 60.0),

	("udine", "Venice", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (93.88, -255.26), [], 55.0),

	("spalato", "Spalato", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (131.16, -191.96), [], 90.0),

	("terni", "Terni", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (91.04, -215.0), [], 90.0),

	("bari", "Bari", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (45.56, -195.48), [], 45.0),

	("mediolanum", "Mediolanum", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (129.12, -254.72), [], 90.0),

	("etruscan", "Etruscan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (110.0, -223.24), [], 90.0),

	("locri", "Locri", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (51.0, -161.68), [], 85.0),

	("thurii", "Thurii", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (49.68, -177.24), [], 125.0),

	("genoa", "Genoa", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (131.44, -241.08), [], 270.0),

	("ancona", "Ancona", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (82.04, -228.3), [], 175.0),

	("modena", "Modena", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (110.6, -242.76), []),

	("terracina", "Terracina", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (85.24, -199.36), [], 105.0),

	("jerusalem", "Jerusalem", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-154.8, -82.92), [], 170.0),

	("antioch", "Antioch", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-167.12, -133.12), [], 100.0),

	("cyprus", "Cyprus", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-136.8, -121.6), [], 260.0),

	("acre", "Acre", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-154.4, -93.2), [], 115.0),

	("tripoli", "Tripoli", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-166.8, -115.6), [], 10.0),

	("sidon", "Sidon", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-157.28, -103.04), [], 275.0),

	("tarsus", "Tarsus", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-157.8, -144.2), [], 240.0),

	("saheth", "Saheth", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-171.08, -112.16), [], 240.0),

	("tyre", "Tyre", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-160.28, -107.68), [], 180.0),

	("aleppo", "Aleppo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-178.12, -134.48), [], 45.0),

	("kiev", "Kiev", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-103.46, -321.88), [], 90.0),

	("lutsk", "Lutsk", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-47.2, -331.2), [], 270.0),

	("chernigov", "Chernigov", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-112.24, -342.84), [], 280.0),

	("mariupol", "Mariupol", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-180.28, -278.12), [], 180.0),

	("mazyr", "Mazyr", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-90.0, -351.48), []),

	("kirovohrad", "Kirovohrad", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-122.6, -297.52), [], 15.0),

	("belgorod", "Belgorod", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-170.36, -328.68), [], 80.0),

	("armabir", "Armabir", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-219.56, -248.2), [], 80.0),

	("poltava", "Poltava", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-148.0, -313.6), [], 55.0),

	("zhytomyr", "Zhytomyr", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-83.32, -323.68), [], 10.0),

	("babrujsk", "Babrujsk", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-90.24, -369.24), [], 45.0),

	("bryansk", "Bryansk", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-146.52, -371.12), [], 60.0),

	("syutuka", "Syutuka", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-136.28, -348.92), [], 90.0),

	("tambov", "Tambov", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-222.8, -361.8), [], 180.0),

	("paris", "Paris", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (202.04, -303.52), [], 120.0),

	("rouen", "Rouen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (217.2, -312.0), [], 45.0),

	("toulon", "Toulon", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (164.72, -224.0), [], 260.0),

	("nancy", "Nancy", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (161.6, -300.4), [], 130.0),

	("toulouse", "Toulouse", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (212.7, -230.38), [], 45.0),

	("lyon", "Lyon", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (176.4, -258.6), [], 270.0),

	("reims", "Reims", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (185.44, -308.44), [], 45.0),

	("le_mans", "Le mans", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (227.52, -290.64), [], 315.0),

	("dijon", "Dijon", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (173.76, -280.52), []),

	("troyes", "Troyes", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (181.88, -292.96), [], 180.0),

	("lille", "Lille", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (196.2, -329.56), [], 20.0),

	("avignon", "Avignon", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (176.64, -233.64), [], 60.0),

	("orleans", "Orleans", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (209.34, -290.64), [], 260.0),

	("digoin", "Digoin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (186.28, -268.44), [], 15.0),

	("caen", "Caen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (233.28, -307.8), [], 80.0),

	("valladolid", "Valladolid", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (194.0, -253.84), [], 165.0),

	("bourges", "Bourges", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (199.2, -276.8), [], 145.0),

	("laon", "Laon", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (190.2, -313.48), [], 270.0),

	("angers", "Angers", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (235.8, -284.24), [], 180.0),

	("babylon", "Babylon", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-258.16, -102.78), [], 150.0),

	("persepolise", "Persepolise", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-348.0, -62.0), [], 90.0),

	("susa", "Susa", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-291.06, -83.44), [], 50.0),

	("egbatana", "Egbatana", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-290.24, -117.3), [], 80.0),

	("birjand", "Birjand", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-416.8, -95.2), [], 280.0),

	("mosul", "Mosul", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-244.56, -136.22), [], 260.0),

	("herat", "Herat", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-449.6, -112.8), [], 315.0),

	("zahedan", "Zahedan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-434.8, -57.2), [], 225.0),

	("abu_dhabi", "Abu Dhabi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-364.24, 2.48), [], 90.0),

	("dammam", "Dammam", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-315.88, -23.28), [], 120.0),

	("kandahar", "Kandahar", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-488.12, -81.92), [], 45.0),

	("kashan", "Kashan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-332.52, -108.88), [], 275.0),

	("turbat", "Turbat", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-459.16, -19.4), [], 315.0),

	("al_ain", "Al Ain", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-379.6, 0.8), [], 180.0),

	("isfahan", "Isfahan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-334.72, -92.92), [], 20.0),

	("semnan", "Semnan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-353.68, -127.36), [], 90.0),

	("kerman", "Kerman", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-393.68, -66.2), [], 240.0),

	("bandar_abbas", "Bandar Abbas", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-384.84, -32.44), [], 35.0),

	("erzurum", "Erzurum", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-221.24, -180.92), [], 180.0),

	("batman", "Batman", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-219.6, -154.92), [], 90.0),

	("tabriz", "Tabriz", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-276.4, -157.16), [], 90.0),

	("abadan", "Abadan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-298.84, -63.44), []),

	("farah", "Farah", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-448.92, -89.88), [], 20.0),

	("qazvin", "Qazvin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-316.4, -135.2), [], 90.0),

	("dubai", "Dubai", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-374.72, -10.72), [], 95.0),

	("al_batin", "Al batin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-272.48, -45.56), [], 125.0),

	("arak", "Arak", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-313.12, -109.84), [], 45.0),

	("chabahar", "Chabahar", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-433.8, -13.72), [], 45.0),

	("loskile", "Loskile", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (98.4, -409.4), [], 80.0),

	("oslo", "Oslo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (111.5816, -488.68), [], 260.0),

	("bergen", "Bergen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (171.8, -498.36), [], 260.0),

	("viborg", "Viborg", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (126.48, -425.0), [], 125.0),

	("husum", "Husum", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (131.6, -392.0), [], 125.0),

	("stavanger", "Stavanger", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (167.2, -471.16), [], 75.0),

	("faroe", "Faroe", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (306.08, -534.52), [], 110.0),

	("trondheim", "Trondheim", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (114.64, -559.16), []),

	("kristiansand", "Kristiansand", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (142.36, -455.32), [], 345.0),

	("aalborg", "Aalborg", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (121.16, -435.48), [], 55.0),

	("helsingborg", "Helsingborg", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (90.16, -417.92), [], 15.0),

	("odense", "Odense", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (115.8, -406.68), [], 90.0),

	("haugesund", "Haugesund", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (171.4, -479.8), [], 160.0),

	("skien", "Skien", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (124.6, -475.76), [], 180.0),

	("hamar", "Hamar", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (108.48, -506.28), [], 60.0),

	("torshavn", "Torshavn", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (304.36, -530.8), [], 145.0),

	("mold", "Mold", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (151.08, -546.04), [], 215.0),

	("lerwick", "Lerwick", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (243.08, -492.56), [], 35.0),

	("grimstad", "Grimstad", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (136.96, -458.4), [], 175.0),

	("frankfurt", "Frankfurt", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (134.4, -321.88), [], 135.0),

	("luebeck", "Luebeck", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (112.56, -381.28), [], 80.0),

	("magdeburg", "Magdeburg", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (102.0, -352.8), [], 300.0),

	("hamburg", "Hamburg", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (119.6, -376.0), [], 260.0),

	("munich", "Munich", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (102.8, -292.4), [], 260.0),

	("vienna", "Vienna", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (48.96, -295.48), [], 235.0),

	("nuremberg", "Nuremberg", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (108.4, -311.6), [], 55.0),

	("cologne", "Cologne", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (153.6, -333.6), [], 85.0),

	("dresden", "Dresden", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (77.88, -338.28), [], 155.0),

	("rostock", "Rostock", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (95.68, -384.24), [], 80.0),

	("karlsruhe", "Karlsruhe", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (137.88, -305.0), [], 270.0),

	("bielefeld", "Bielefeld", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (136.48, -351.08), [], 125.0),

	("essen", "Essen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (152.8, -342.72), [], 180.0),

	("bremen", "Bremen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (133.32, -367.72), [], 40.0),

	("chemnitz", "Chemnitz", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (87.2, -327.6), [], 20.0),

	("kiel", "Kiel", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (118.84, -388.4), [], 10.0),

	("dortmund", "Dortmund", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (148.08, -343.32), [], 55.0),

	("prague", "Prague", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (71.72, -321.08), [], 45.0),

	("stuttgart", "Stuttgart", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (64.6, -301.52), [], 45.0),

	("berlin", "Berlin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (82.64, -359.04), [], 85.0),

	("brno", "Brno", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (48.4, -307.6), [], 45.0),

	("groningen", "Groningen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (157.2, -365.6), [], 225.0),

	("leipzig", "Leipzig", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (94.32, -340.24), [], 125.0),

	("plzen", "Plzen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (83.4, -315.72), []),

	("neubrandenburg", "Neubrandenburg", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (84.6, -375.84), [], 145.0),

	("brunswick", "Brunswick", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (114.4, -354.84), [], 15.0),

	("antwerp", "Antwerp", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (181.22, -343.58), [], 85.0),

	("amsterdam", "Amsterdam", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (175.6, -356.0), [], 55.0),

	("geneva", "Geneva", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (162.2, -265.04), [], 160.0),

	("luxembourg", "Luxembourg", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (162.84, -316.0), [], 60.0),

	("uppsala", "Uppsala", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (36.0, -487.2), [], 290.0),

	("gothenburg", "Gothenburg", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (98.76, -451.12), [], 260.0),

	("skara", "Skara", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (82.4, -454.0), [], 260.0),

	("visby", "Visby", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (28.4, -443.6), [], 50.0),

	("helsinki", "Helsinki", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-42.84, -493.72), [], 95.0),

	("norrkoping", "Norrkoping", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (53.28, -462.52), [], 180.0),

	("falun", "Falun", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (58.56, -501.96), [], 275.0),

	("turku", "Turku", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-13.64, -498.88), []),

	("kalmar", "Kalmar", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (52.6, -429.82), [], 95.0),

	("varberg", "Varberg", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (95.92, -444.0), [], 45.0),

	("tingsryd", "Tingsryd", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (65.24, -423.92), [], 60.0),

	("stockholm", "Stockholm", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (31.6, -477.6), [], 15.0),

	("karlstad", "Karlstad", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (81.6, -478.72), [], 35.0),

	("tallinn", "Tallinn", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-40.48, -479.4), [], 90.0),

	("linkoping", "Linkoping", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (58.92, -459.2), [], 225.0),

	("salo", "Salo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-23.2, -498.0), [], 15.0),

	("orebro", "Orebro", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (63.24, -476.24), [], 85.0),

	("damascus", "Damascus", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-166.8, -102.76), [], 310.0),

	("alexandria", "Alexandria", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-97.6, -75.8456), []),

	("cairo", "Cairo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-111.56, -63.6), [], 75.0),

	("kaerak", "Kaerak", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-158.0, -72.4), [], 260.0),

	("damietta", "Damietta", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-116.76, -79.0), [], 45.0),

	("benghazi", "Benghazi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (8.4, -85.96), [], 45.0),

	("aqaba", "Aqaba", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-154.32, -59.56), [], 260.0),

	("al_arish", "Al Arish", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-143.6, -75.2), [], 125.0),

	("suwayda", "Suwayda", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-175.36, -87.16), [], 265.0),

	("mecca", "Mecca", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-205.48, 29.96), [], 80.0),

	("medinah", "Medinah", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-203.04, -2.6), [], 90.0),

	("sanaa", "Sanaa", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-253.16, 91.88), [], 180.0),

	("aswan", "Aswan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-128.8, 1.44), [], 270.0),

	("asyut", "Asyut", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-108.98, -31.32), [], 75.0),

	("tubruq", "Tubruq", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-31.56, -86.48), [], 195.0),

	("amadabad", "Amadabad", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-243.52, -58.88), [], 95.0),

	("abha", "Abha", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-234.8, 62.52), [], 95.0),

	("arar", "Arar", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-218.36, -73.84), [], 315.0),

	("riyadh", "Jeddah", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-198.96, -28.2), [], 95.0),

	("riyadh", "Jeddah", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-198.96, -28.2), [], 95.0),

	("shah_kaka", "Shah Kaka", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-209.36, -62.8), [], 40.0),

	("beni_suef", "Beni suef", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-110.8, -52.4), [], 45.0),

	("tabuk", "Tabuk", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-169.76, -44.52), [], 180.0),

	("tanta", "Tanta", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-108.76, -71.76), [], 90.0),

	("el_daba", "El Daba", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-78.84, -74.76), [], 180.0),

	("suez", "Suez", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-128.12, -64.5), [], 35.0),

	("luxor", "Luxor", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-126.74, -14.58), [], 180.0),

	("amman", "Amman", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-163.08, -84.88), [], 260.0),

	("adabiyah", "Adabiyah", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (8.4, -71.72), [], 180.0),

	("al_madiq", "Al madiq", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-129.12, -5.16), [], 55.0),

	("buraydah", "Buraydah", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-250.64, -22.8), [], 255.0),

	("yanbu", "Yanbu", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-187.6, 0.8), [], 45.0),

	("aden", "Aden", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-261.56, 115.76), [], 45.0),

	("tayma", "Tayma", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-191.12, -36.6), [], 270.0),

	("derna", "Derna", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-17.28, -94.08), [], 140.0),

	("samalut", "Samalut", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-107.16, -44.18), []),

	("wadi_addawasir", "Wadi addawasir", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-259.6, 39.4), [], 185.0),

	("hail", "Hail", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-225.64, -35.4), [], 80.0),

	("deir_ez_zur", "Deir ez-zur", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-208.48, -124.4), [], 45.0),

	("samarkand", "Samarkand", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-501.2, -177.2), [], 155.0),

	("nishapur", "Nishapur", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-412.68, -135.6), [], 80.0),

	("kabul", "Kabul", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-526.0, -114.88), [], 35.0),

	("mazarisharif", "MazariSharif", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-503.84, -140.64), [], 245.0),

	("taraz", "Taraz", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-550.12, -218.92), [], 215.0),

	("ashgabat", "Ashgabat", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-407.84, -156.16), [], 45.0),

	("aktau", "Aktau", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-330.72, -230.72), [], 115.0),

	("baku", "Baku", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-314.8, -188.0), [], 95.0),

	("bishukec", "Bishukec", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-585.04, -218.68), [], 10.0),

	("tashkent", "Tashkent", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-526.684, -197.6), [], 160.0),

	("urgench", "Urgench", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-429.88, -199.72), [], 40.0),

	("shymkent", "Shymkent", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-530.72, -211.48), [], 20.0),

	("mary", "Mary", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-445.8, -152.12), []),

	("gizab", "Gizab", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-493.84, -102.56), [], 275.0),

	("zhanaozen", "Zhanaozen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-347.84, -225.6), [], 175.0),

	("shirvan", "Shirvan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-304.72, -181.32), [], 45.0),

	("gdansk", "Gdansk", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (26.0, -388.64), [], 120.0),

	("poznan", "Poznan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (44.4, -357.2), [], 260.0),

	("krakow", "Krakow", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (11.6, -321.12), [], 260.0),

	("warsaw", "Warsaw", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1.12, -348.12), [], 185.0),

	("lublin", "Lublin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-17.2, -338.96), [], 180.0),

	("szczecin", "Szczecin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (70.32, -374.08), [], 175.0),

	("bialystok", "Bialystok", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-23.4, -368.8), []),

	("rzeszow", "Rzeszow", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-10.68, -320.0), []),

	("bydgoszcz", "Bydgoszcz", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (32.72, -368.48), [], 315.0),

	("lodz", "Lodz", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (16.76, -347.2), [], 100.0),

	("wroclaw", "Wroclaw", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (43.24, -337.2), [], 100.0),

	("opole", "Opole", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (33.72, -330.48), [], 260.0),

	("gorzow", "Gorzow", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (64.84, -363.68), [], 115.0),

	("elk", "Elk", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-14.32, -379.48), [], 90.0),

	("koszalin", "Koszalin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (53.04, -385.28), [], 255.0),

	("olsztyn", "Olsztyn", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (5.76, -377.08), []),

	("kielce", "Kielce", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (4.24, -332.52), [], 155.0),

	("konin", "Konin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (30.2, -354.04), [], 45.0),

	("siedlce", "Siedlce", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-13.92, -352.8), [], 225.0),

	("vilnius", "Vilnius", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-46.76, -394.76), [], 90.0),

	("kaunas", "Kaunas", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-32.0, -398.4), [], 15.0),

	("kelme", "Kelme", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-14.0, -412.0), [], 10.0),

	("hrodna", "Hrodna", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-30.8, -377.28), [], 125.0),

	("lida", "Lida", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-47.4, -381.12), [], 90.0),

	("baranavichy", "Baranavichy", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-54.56, -368.8), [], 45.0),

	("siauliai", "Siauliai", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-24.92, -416.4), [], 240.0),

	("pinsk", "Pinsk", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-54.32, -352.72), [], 45.0),

	("xuzhou", "Xuzhou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1054.78, -111.58), [], 290.0),

	("pizhou", "Pizhou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1059.52, -112.88), [], 60.0),

	("huaian", "Huaian", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1070.24, -104.72), [], 180.0),

	("lianyungang", "Lianyungang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1072.76, -115.84), [], 45.0),

	("linyi", "Linyi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1063.32, -121.76), [], 80.0),

	("london", "London", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (230.48, -343.36), [], 180.0),

	("bordeaux", "Bordeaux", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (238.22, -249.12), [], 255.0),

	("york", "York", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (241.08, -382.72), [], 90.0),

	("nante", "Nante", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (247.64, -280.22), [], 235.0),

	("bristol", "Bristol", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (257.48, -342.32), [], 260.0),

	("chester", "Chester", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (259.2, -369.6), [], 90.0),

	("bamber", "Bamber", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (246.8, -398.4), [], 45.0),

	("dublin", "Dublin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (298.8, -372.4), [], 90.0),

	("hastings", "Hastings", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (222.4, -334.8), [], 180.0),

	("hawick", "Hawick", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (259.6, -406.64), [], 280.0),

	("portsmouth", "Portsmouth", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (241.08, -333.16), [], 75.0),

	("limoges", "Limoges", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (215.2, -259.0), [], 140.0),

	("plymouth", "Plymouth", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (274.76, -325.68), [], 65.0),

	("norwich", "Norwich", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (215.8, -360.84), [], 125.0),

	("northamton", "Northamton", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (238.92, -353.4), [], 275.0),

	("nottingham", "Nottingham", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (241.68, -366.08), [], 315.0),

	("sheffield", "Sheffield", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (245.52, -373.36), [], 20.0),

	("cardiff", "Cardiff", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (264.8, -343.4), [], 80.0),

	("blackpool", "Blackpool", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (260.92, -379.72), [], 35.0),

	("wolverhampton", "Wolverhampton", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (253.12, -358.4), []),

	("brest", "Brest", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (276.88, -293.64), [], 45.0),

	("maan", "Maan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (278.88, -386.8), [], 20.0),

	("derby", "Derby", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (246.24, -365.32), [], 55.0),

	("southampton", "Southampton", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (244.64, -334.0), [], 15.0),

	("cahors", "Cahors", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (214.12, -242.12), [], 35.0),

	("poitiers", "Poitiers", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (227.28, -272.08), [], 160.0),

	("rennes", "Rennes", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (247.12, -292.76), []),

	("exeter", "Exeter", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (268.24, -330.72), [], 90.0),

	("cambridge", "Cambridge", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (228.44, -352.44), [], 180.0),

	("colchester", "Colchester", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (220.24, -349.88), [], 45.0),

	("aberystwyth", "Aberystwyth", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (273.28, -358.04), [], 315.0),

	("dungannon", "Dungannon", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (273.76, -398.2), [], 125.0),

	("la_lochelle", "La lochelle", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (241.8, -264.24), [], 90.0),

	("nanjing", "Nanjing", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1068.96, -86.16), []),

	("shaoxing", "Shaoxing", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1087.36, -63.8), [], 45.0),

	("suzhou", "Suzhou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1087.68, -78.0), [], 225.0),

	("shanghai", "Shanghai", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1097.24, -77.32), [], 130.0),

	("yizhou", "Yizhou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1092.8, 2.4), [], 90.0),

	("wenzhou", "Wenzhou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1088.4, -39.86), [], 170.0),

	("nanping", "Nanping", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1061.24, -26.72), [], 80.0),

	("yancheng", "Yancheng", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1082.72, -101.52), [], 110.0),

	("ningbo", "Ningbo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1097.68, -62.0), [], 115.0),

	("jinhua", "Jinhua", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1077.16, -53.12), [], 45.0),

	("shanyue", "Shanyue", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1066.4, -66.28), [], 185.0),

	("kyoto", "Kyoto", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1253.6, -121.08), [], 240.0),

	("edo", "Edo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1296.4, -129.12), [], 90.0),

	("nagasaki", "Nagasaki", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1189.2, -95.2), [], 80.0),

	("hiroshima", "Hiroshima", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1216.8, -114.4), [], 260.0),

	("osaka", "Osaka", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1251.36, -115.58), [], 45.0),

	("sendai", "Sendai", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1309.24, -160.48), [], 125.0),

	("nagano", "Nagano", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1280.4, -143.2), [], 45.0),

	("tokushima", "Tokushima", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1240.2, -109.52), [], 280.0),

	("morioka", "Morioka", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1312.44, -178.4), [], 90.0),

	("fukuoka", "Fukuoka", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1194.68, -104.76), [], 315.0),

	("kagoshima", "Kagoshima", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1196.28, -81.2), [], 125.0),

	("matsuyama", "Matsuyama", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1220.94, -106.92), [], 185.0),

	("matsue", "Matsue", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1224.16, -125.32), [], 45.0),

	("takayama", "Takayama", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1271.38, -134.06), [], 155.0),

	("utsunomiya", "Utsunomiya", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1298.4, -139.32), [], 245.0),

	("sapporo", "Sapporo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1314.8, -221.92), [], 120.0),

	("kobayashi", "Kobayashi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1198.92, -84.56), [], 130.0),

	("tottori", "Tottori", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1239.0, -126.28), [], 170.0),

	("nagoya", "Nagoya", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1266.44, -122.92), [], 45.0),

	("fukushima", "Fukushima", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1304.76, -153.8), [], 110.0),

	("akita", "Akita", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1301.64, -178.88), [], 120.0),

	("amami", "Amami", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1183.64, -44.12), [], 90.0),

	("shizuoka", "Shizuoka", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1281.6, -121.2), [], 180.0),

	("katsuyama", "Katsuyama", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1260.0, -133.48), [], 100.0),

	("yamaguchi", "Yamaguchi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1206.4, -111.2), [], 45.0),

	("aomori", "Aomori", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1307.92, -191.76), [], 45.0),

	("oita", "Oita", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1207.8, -99.78), [], 25.0),

	("miyazaki", "Miyazaki", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1205.48, -85.04), [], 180.0),

	("kochi", "Kochi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1228.76, -104.32), [], 85.0),

	("okayama", "Okayama", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1233.16, -116.96), [], 315.0),

	("niigata", "Niigata", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1289.18, -154.9), [], 255.0),

	("maebashi", "Maebashi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1289.32, -137.24), []),

	("ryukyu", "Ryukyu", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1167.2, -24.4), [], 145.0),

	("gorgonac", "Gorgonac", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1036.4, -290.4), [], 55.0),

	("olkhunuud", "Olkhunuud", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-978.4, -232.4), [], 25.0),

	("khongirad", "Khongirad", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-967.2, -268.68), [], 15.0),

	("hulunber", "Hulunber", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1079.32, -306.68), [], 175.0),

	("ulaanbaatar", "Ulaanbaatar", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-938.04, -288.88), [], 275.0),

	("khongirad_ger", "Khongirad ger", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-962.88, -298.24), [], 90.0),

	("olkhunuud_ger", "Olkhunuud ger", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1026.28, -257.0), [], 170.0),

	("hulunber_yurt", "Hulunber yurt", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1044.16, -313.92), [], 295.0),

	("ulaanbaatar_yurt", "Ulaanbaatar yurt", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-923.6, -275.44), [], 25.0),

	("gorgonac_ger", "Gorgonac ger", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-997.16, -310.36), [], 170.0),

	("tola", "Tola", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-849.18, -297.1), [], 175.0),

	("kyrgyz", "Kyrgyz", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-871.92, -301.24), [], 80.0),

	("oirats", "Oirats", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-759.6, -321.2), [], 115.0),

	("kyzyl", "Kyzyl", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-803.08, -343.98), []),

	("kyrgyz_ger", "Kyrgyz ger", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-858.4, -325.6), [], 170.0),

	("tola_ger", "Tola ger", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-834.1, -281.68), [], 170.0),

	("zaysan", "Zaysan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-697.68, -282.48), [], 15.0),

	("ulaangom", "Ulaangom", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-776.92, -321.96), [], 155.0),

	("toledo", "Toledo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (274.0932, -180.8844), [], 170.0),

	("sevilla", "Sevilla", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (294.4, -149.2), [], 260.0),

	("murcia", "Murcia", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (241.6, -157.0), [], 260.0),

	("valencia", "Valencia", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (234.4, -175.6), [], 225.0),

	("barcelona", "Barcelona", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (205.2, -200.8), [], 225.0),

	("zaragoza", "Zaragoza", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (239.16, -203.36), [], 125.0),

	("cordova", "Cordova", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (282.32, -156.0), [], 25.0),

	("leon", "Leon", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (289.96, -215.6), [], 35.0),

	("badahose", "Badahose", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (305.4, -167.88), [], 155.0),

	("burgos", "Burgos", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (269.88, -212.44), [], 55.0),

	("merida", "Merida", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (297.96, -169.08), [], 10.0),

	("baza", "Baza", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (261.68, -152.76), [], 35.0),

	("madrid", "Madrid", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (269.64, -187.64), []),

	("salamanca", "Salamanca", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (291.16, -194.44), [], 40.0),

	("almagro", "Almagro", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (271.28, -167.14), [], 20.0),

	("tortosa", "Tortosa", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (217.36, -197.04), [], 10.0),

	("huelva", "Huelva", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (305.2, -147.84), [], 240.0),

	("cuenca", "Cuenca", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (255.48, -181.88), [], 180.0),

	("palma", "Palma", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (197.36, -176.92), [], 240.0),

	("cieza", "Cieza", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (245.56, -163.84), [], 125.0),

	("bilbao", "Bilbao", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (258.0, -223.2), [], 45.0),

	("szeged", "Szeged", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (9.28, -265.56), [], 290.0),

	("belgrade", "Belgrade", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (5.76, -245.56), [], 115.0),

	("zagreb", "Zagreb", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (54.8, -259.2), [], 260.0),

	("clujnapoca", "ClujNapoca", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-28.32, -272.72), [], 45.0),

	("perek", "Perek", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-2.72, -304.4), [], 45.0),

	("tuircmureci", "Tuircmureci", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-38.8, -268.8), [], 65.0),

	("debrecen", "Debrecen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-6.64, -283.44), []),

	("pecs", "Pecs", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (30.52, -262.64), []),

	("graz", "Graz", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (61.08, -276.8), [], 90.0),

	("nis", "Nis", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-10.08, -225.64), [], 80.0),

	("petro_baradin", "Petro Baradin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (12.4, -232.2), [], 90.0),

	("arad", "Arad", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-3.44, -264.0), [], 80.0),

	("budapest", "Budapest", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (21.44, -283.4), [], 35.0),

	("kraljevo", "Kraljevo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-31.04, -238.92), [], 90.0),

	("miskolc", "Miskolc", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (2.68, -291.2), [], 30.0),

	("novi_sad", "Novi sad", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (12.8, -251.4), [], 315.0),

	("lisbon", "Lisbon", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (329.12, -167.96), [], 120.0),

	("coimbra", "Coimbra", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (321.2, -184.4), [], 255.0),

	("braga", "Braga", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (321.2, -202.0), [], 255.0),

	("faro", "Faro", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (316.4, -145.56), [], 45.0),

	("porto", "Porto", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (323.44, -196.92), [], 160.0),

	("evora", "Evora", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (315.4, -163.88), [], 60.0),

	("braganca", "Braganca", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (301.56, -204.84), [], 260.0),

	("constantinople", "Constantinople", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-86.34, -196.3), [], 90.0),

	("ancyra", "Ancyra", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-129.08, -180.6), [], 45.0),

	("chonai", "Chonai", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-88.0, -154.0), [], 260.0),

	("adrianople", "Adrianople", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-60.8, -203.2), [], 180.0),

	("marcianopolis", "Marcianopolis", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-75.04, -223.8), [], 190.0),

	("bucharest", "Bucharest", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-55.56, -240.12), []),

	("karaman", "Karaman", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-133.28, -147.12), []),

	("sivas", "Sivas", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-175.08, -178.76), [], 275.0),

	("samsun", "Samsun", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-166.8, -197.6), [], 10.0),

	("manisa", "Manisa", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-70.08, -164.44), [], 90.0),

	("tarnovo", "Tarnovo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-53.88, -227.8), [], 90.0),

	("baris", "Baris", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-104.4, -155.0), [], 35.0),

	("thyatira", "Thyatira", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-90.04, -173.44), [], 45.0),

	("gallipoli", "Gallipoli", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-60.3, -187.14), [], 45.0),

	("buzau", "Buzau", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-63.52, -249.88), [], 25.0),

	("iconium", "Iconium", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-125.28, -155.28), [], 145.0),

	("attalia", "Attalia", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-107.2, -144.0), [], 315.0),

	("angkor_thom", "Angkor Thom", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-898.8, 108.8), []),

	("tuguegarao", "Tuguegarao", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1100.0, 69.2), [], 240.0),

	("sukhothai", "Sukhothai", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-864.99, 88.97), [], 45.0),

	("naypyidaw", "Naypyidaw", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-820.0, 46.4), [], 280.0),

	("hanoi", "Hanoi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-926.4, 34.0), [], 15.0),

	("luang_namtha", "Luang namtha", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-878.08, 34.6), [], 145.0),

	("kohima", "Kohima", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-798.36, -13.8), [], 15.0),

	("myeik", "Myeik", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-847.64, 121.0), [], 170.0),

	("hainan", "Hainan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-969.6, 51.8), [], 110.0),

	("baguio", "Baguio", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1087.6, 79.88), [], 240.0),

	("danang", "Danang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-951.6, 85.88), [], 260.0),

	("thaton", "Thaton", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-834.4, 75.48), [], 55.0),

	("nha_trang", "Nha trang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-963.08, 122.52), [], 260.0),

	("lashio", "Lashio", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-838.4, 13.84), [], 115.0),

	("udon_thani", "Udon thani", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-893.48, 71.6), [], 25.0),

	("shwebo", "Shwebo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-815.84, 17.44), [], 25.0),

	("namman", "Namman", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-877.68, -0.12), [], 115.0),

	("xuchang", "Xuchang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1014.0, -109.2), [], 290.0),

	("luoyang", "Luoyang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-999.6, -113.6), [], 90.0),

	("kaifeng", "Kaifeng", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1019.16, -118.68), [], 80.0),

	("puyang", "Puyang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1027.12, -129.8), [], 125.0),

	("taikang", "Taikang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1025.12, -109.76), [], 125.0),

	("jinan", "Jinan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1050.86, -139.78), [], 115.0),

	("liaocheng", "Liaocheng", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1037.32, -138.2), [], 175.0),

	("yanjin", "Yanjin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1017.8, -122.48), [], 110.0),

	("heze", "Heze", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1032.04, -123.68), [], 120.0),

	("pingdingshan", "Pingdingshan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1007.36, -107.6), [], 15.0),

	("zibo", "Zibo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1059.88, -141.96), [], 45.0),

	("taian", "Taian", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1049.28, -135.12), [], 90.0),

	("bozhou", "Bozhou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1037.62, -109.04), [], 65.0),

	("jilin", "Jilin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1152.8, -231.16), [], 80.0),

	("mishan", "Mishan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1201.2, -251.6), [], 45.0),

	("harbin", "Harbin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1150.82, -259.56), [], 90.0),

	("siping", "Siping", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1128.56, -223.08), [], 275.0),

	("yi_chun", "Yi chun", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1177.96, -286.88), [], 100.0),

	("mudanjiang", "Mudanjiang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1185.4, -241.44), [], 100.0),

	("songyuan", "Songyuan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1134.0, -250.68), [], 100.0),

	("qiqihar", "Qiqihar", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1124.16, -280.92), [], 115.0),

	("changchun", "Changchun", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1139.6, -232.0), []),

	("hinggan", "Hinggan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1103.96, -262.76), [], 240.0),

	("onon", "Onon", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-959.6, -332.4), [], 155.0),

	("merkit", "Merkit", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-894.8, -369.08), [], 45.0),

	("darkhan", "Darkhan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-927.8, -311.92), []),

	("onon_ger", "Onon ger", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-941.6, -348.92), [], 110.0),

	("merkit_ger", "Merkit ger", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-892.4, -327.48), [], 120.0),

	("tayichiud", "Tayichiud", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1006.16, -352.39), [], 130.0),

	("erdenet", "Erdenet", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-907.76, -305.64), [], 45.0),

	("xining", "Xining", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-882.28, -140.32), [], 25.0),

	("qingyang", "Qingyang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-947.84, -130.44), [], 25.0),

	("anding", "Anding", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-912.04, -127.56), [], 65.0),

	("tianshui", "Tianshui", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-925.2, -115.2), [], 85.0),

	("haixi", "Haixi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-834.04, -149.8), [], 125.0),

	("longnan", "Longnan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-916.16, -102.0), [], 170.0),

	("pingliang", "Pingliang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-934.96, -126.36), [], 170.0),

	("lanzhou", "Lanzhou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-905.28, -133.6), [], 170.0),

	("gannan", "Gannan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-894.68, -120.92), [], 180.0),

	("wuwei", "Wuwei", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-892.08, -156.1204), [], 240.0),

	("aktube", "Aktube", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-394.8, -324.0), [], 270.0),

	("volgograd", "Volgograd", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-258.28, -298.64), []),

	("aralsk", "Aralsk", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-444.76, -274.2), [], 90.0),

	("atyrau", "Atyrau", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-336.44, -279.6), [], 185.0),

	("kyzylorda", "Kyzylorda", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-487.72, -246.68), [], 275.0),

	("saratov", "Saratov", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-273.12, -343.56), [], 90.0),

	("surabaya", "Surabaya", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1001.72, 313.44), [], 90.0),

	("palembang", "Palembang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-916.72, 267.1), [], 225.0),

	("kuala_lumpur", "Kuala lumpur", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-881.24, 211.56), [], 55.0),

	("davao", "Davao", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1140.96, 172.52), [], 65.0),

	("pontianak", "Pontianak", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-965.12, 240.12), [], 315.0),

	("makassar", "Makassar", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1075.7, 293.36), [], 225.0),

	("palu", "Palu", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1079.6, 251.08), [], 155.0),

	("banduang", "Banduang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-943.2, 308.32), [], 225.0),

	("banzarmasin", "Banzarmasin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1022.98, 275.76), [], 145.0),

	("medan", "Medan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-848.0, 207.6), [], 45.0),

	("kota_kinabalu", "Kota kinabalu", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1039.04, 184.56), [], 265.0),

	("kurching", "Kurching", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-975.68, 227.2), [], 125.0),

	("cebu", "Cebu", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1123.64, 141.82), [], 255.0),

	("timbuktu", "Timbuktu", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (260.76, 76.4), [], 190.0),

	("bamako", "Bamako", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (158.74, 58.24), [], 180.0),

	("gao", "Gao", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (232.12, 81.74), [], 45.0),

	("tamale", "Tamale", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (239.0, 150.6), [], 315.0),

	("dakar", "Dakar", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (416.36, 98.6), [], 25.0),

	("abidjan", "Abidjan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (273.76, 190.32), []),

	("niamey", "Niamey", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (204.96, 109.26), [], 315.0),

	("djenne", "Djenne", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (277.84, 104.24), [], 125.0),

	("accra", "Accra", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (232.24, 188.2), [], 270.0),

	("peixian", "Peixian", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1048.8, -117.62), [], 15.0),

	("jining", "Jining", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1048.52, -123.22), [], 45.0),

	("tianjin", "Tianjin", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1050.8, -170.8), [], 240.0),

	("weifang", "Weifang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1072.16, -141.4), [], 240.0),

	("pingyuan", "Pingyuan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1042.2, -146.76), [], 150.0),

	("linzhang", "Linzhang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1022.08, -136.8), [], 225.0),

	("hengshui", "Hengshui", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1033.8, -153.8), [], 290.0),

	("shijiazhuang", "Shijiazhuang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1021.32, -157.8), [], 315.0),

	("taiyuan", "Taiyuan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1001.58, -154.22), [], 245.0),

	("qingdao", "Qingdao", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1085.2, -134.2), []),

	("hekou", "Hekou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1065.08, -155.56), [], 170.0),

	("yangquan", "Yangquan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1011.24, -155.24), [], 170.0),

	("haixing", "Haixing", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1055.72, -158.8), [], 90.0),

	("baoding", "Baoding", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1031.6, -168.0), [], 215.0),

	("zhangbei", "Zhangbei", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1023.64, -196.84), [], 125.0),

	("dezhou", "Dezhou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1041.76, -150.32), []),

	("linqing", "Linqing", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1034.56, -142.92), [], 90.0),

	("yantai", "Yantai", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1096.84, -149.88), [], 180.0),

	("xiangyang", "Xiangyang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-994.8, -85.52), [], 190.0),

	("wuhan", "Wuhan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1019.26, -68.76), [], 90.0),

	("xinye", "Xinye", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-997.44, -92.2), [], 60.0),

	("changsha", "Changsha", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1003.76, -43.76), [], 265.0),

	("changde", "Changde", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-990.2, -52.32), [], 225.0),

	("jingzhou", "Jingzhou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-995.52, -67.64), [], 155.0),

	("chenzhou", "Chenzhou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1004.72, -16.52), [], 45.0),

	("zhangjiajie", "Zhangjiajie", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-976.64, -53.52), [], 180.0),

	("yongzhou", "Yongzhou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-989.68, -23.36), [], 170.0),

	("hengyang", "Hengyang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-999.92, -29.04), [], 100.0),

	("zhongshan", "Zhongshan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1009.24, 18.24), [], 170.0),

	("tianmen", "Tianmen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1006.28, -70.76), [], 10.0),

	("suizhou", "Suizhou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1009.16, -81.84), [], 260.0),

	("xianning", "Xianning", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1019.0, -61.68), [], 240.0),

	("shaoyang", "Shaoyang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-987.68, -33.12), [], 45.0),

	("yichang", "Yichang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-985.8, -71.44), [], 90.0),

	("yichun", "Yichun", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1020.0, -39.24), [], 180.0),

	("tongren", "Tongren", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-962.76, -38.04), [], 315.0),

	("chengdu", "Chengdu", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-907.2, -69.16), [], 90.0),

	("jiangzhou", "Jiangzhou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-933.96, -58.4), [], 80.0),

	("hanzhong", "Hanzhong", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-939.48, -97.44), [], 115.0),

	("fengjie", "Fengjie", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-965.64, -74.2), [], 125.0),

	("zitong", "Zitong", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-918.68, -82.44), [], 65.0),

	("kunming", "Kunming", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-893.32, -7.44), [], 180.0),

	("zhushan", "Zhushan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-972.56, -87.88), [], 175.0),

	("qujing", "Qujing", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-904.0, -13.64), [], 170.0),

	("dazhou", "Dazhou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-944.04, -76.84), [], 100.0),

	("zhaotong", "Zhaotong", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-902.68, -34.12), [], 120.0),

	("wuzhangyuanzhen", "Wuzhangyuanzhen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-946.08, -111.92), [], 130.0),

	("yuexi", "Yuexi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-903.8, -52.6), [], 90.0),

	("neijiang", "Neijiang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-917.52, -58.44), [], 175.0),

	("ankang", "Ankang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-960.68, -94.32), [], 225.0),

	("nanchong", "Nanchong", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-929.12, -72.68), [], 275.0),

	("guiyang", "Guiyang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-935.04, -26.16), [], 45.0),

	("tangshan", "Tangshan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1061.4, -177.32), [], 275.0),

	("liaoyang", "Liaoyang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1116.0, -198.2), [], 90.0),

	("beiping", "Beiping", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1041.88, -181.08), [], 155.0),

	("chifeng", "Chifeng", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1068.92, -211.32), [], 155.0),

	("yingkou", "Yingkou", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1105.8, -190.92), [], 170.0),

	("chengde", "Chengde", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1059.04, -194.36), [], 170.0),

	("qinhuangdao", "Qinhuangdao", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1076.52, -181.72), [], 45.0),

	("chaoyang", "Chaoyang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1086.2, -202.16), [], 155.0),

	("marrakech", "Marrakech", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (316.8, -81.6), [], 90.0),

	("fez", "Fez", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (283.6, -109.2), [], 135.0),

	("oran", "Oran", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (236.0, -128.0), [], 55.0),

	("tangier", "Tangier", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (292.6, -129.08), [], 45.0),

	("rabat", "Rabat", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (303.88, -108.48), [], 15.0),

	("melia", "Melia", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (262.4, -122.0), [], 180.0),

	("agadir", "Agadir", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (333.0, -67.56), [], 240.0),

	("safi", "Safi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (329.2, -89.64), [], 45.0),

	("saidia", "Saidia", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (254.28, -118.84), [], 180.0),

	("meknes", "Meknes", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (290.44, -107.68), [], 155.0),

	("yinchuan", "Yinchuan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-931.2, -163.0), [], 45.0),

	("dunhuang", "Dunhuang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-824.0, -186.48), [], 15.0),

	("kumul", "Kumul", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-792.0, -218.44), [], 225.0),

	("zhangye", "Zhangye", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-867.6, -168.72), [], 45.0),

	("shanshan", "Shanshan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-756.4, -219.04), [], 100.0),

	("jiuquan", "Jiuquan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-846.2, -178.84), [], 135.0),

	("jinchang", "Jinchang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-887.04, -163.52), [], 225.0),

	("bayannuur", "Bayannuur", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-943.36, -191.88), [], 90.0),

	("runan", "Runan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1019.68, -97.8), [], 90.0),

	("jiujiang", "Jiujiang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1039.08, -60.86), [], 45.0),

	("shouxian", "Shouxian", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1044.26, -90.84), [], 260.0),

	("lujiang", "Lujiang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1051.2, -77.56), []),

	("fuyang", "Fuyang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1035.24, -96.36), [], 45.0),

	("hefei", "Hefei", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1050.8, -83.44), [], 35.0),

	("xinyang", "Xinyang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1016.24, -87.52), [], 130.0),

	("anqing", "Anqing", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1048.96, -69.56), [], 240.0),

	("xian", "Xian", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-960.56, -112.2), [], 170.0),

	("lingbao", "Lingbao", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-981.64, -115.08), [], 45.0),

	("nanyang", "Nanyang", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-999.44, -97.32), [], 60.0),

	("weinan", "Weinan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-967.62, -115.58), [], 100.0),

	("luanchuan", "Luanchuan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-989.64, -106.72), [], 90.0),

	("linfen", "Linfen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-988.44, -133.76), [], 90.0),

	("almaty", "Almaty", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-610.4, -224.0), [], 80.0),

	("taldykrogan", "Taldykrogan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-626.6, -248.0), [], 315.0),

	("urumqi", "Urumqi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-728.44, -231.24), [], 260.0),

	("bayingol", "Bayingol", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-711.2, -204.52), [], 215.0),

	("naringol", "Naringol", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-646.28, -217.92), []),

	("usharal", "Usharal", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-654.36, -263.72), [], 275.0),

	("changji", "Changji", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-724.24, -234.6), [], 100.0),

	("luntai", "Luntai", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-694.76, -206.52), [], 100.0),

	("kashgar", "Kashgar", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-582.97, -176.07), [], 150.0),

	("cusco", "Cusco", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1015.28, 374.84), [], 70.0),

	("quito", "Quito", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1089.6, 249.24), [], 235.0),

	("tiwanaku", "Tiwanaku", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (973.96, 405.56), [], 125.0),

	("cajamarca", "Cajamarca", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1086.64, 312.4), [], 45.0),

	("lima", "Lima", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1070.84, 360.24), [], 125.0),

	("cochabamba", "Cochabamba", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (951.76, 413.96), [], 115.0),

	("chimbote", "Chimbote", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1086.68, 330.72), [], 65.0),

	("abancay", "Abancay", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1025.68, 376.16), [], 45.0),

	("pisco", "Pisco", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1060.8, 376.48), [], 35.0),

	("tacna", "Tacna", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (996.52, 419.6), [], 115.0),

	("tucuman", "Tucuman", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (937.6, 459.6), [], 65.0),

	("pasto", "Pasto", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1062.08, 223.24), [], 240.0),

	("sucre", "Sucre", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (942.68, 430.32), [], 315.0),

	("tenochtitlan", "Tenochtitlan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1307.6, 49.84), [], 85.0),

	("teotihuacan", "Teotihuacan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1297.32, -12.4), [], 95.0),

	("tikal", "Tikal", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1208.84, 73.12), [], 225.0),

	("tegucigalpa", "Tegucigalpa", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1182.08, 103.68), [], 115.0),

	("tecpan", "Tecpan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1328.2, 72.36), [], 45.0),

	("autlan", "Autlan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1369.24, 46.6), [], 15.0),

	("texcoco", "Texcoco", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1300.0, 22.0), [], 135.0),

	("chalco", "Chalco", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1277.52, 72.16), [], 225.0),

	("tlacopan", "Tlacopan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1364.32, 21.36), [], 185.0),

	("uxmal", "Uxmal", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1208.28, 34.8), [], 90.0),

	("acapulco", "Acapulco", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1320.28, 75.64), [], 45.0),

	("tecoman", "Tecoman", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1363.88, 55.44), [], 135.0),

	("managua", "Managua", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1171.12, 123.36), [], 225.0),

	("veliky_novgorod", "Veliky novgorod", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-112.16, -462.8), [], 180.0),

	("torzhok", "Torzhok", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-152.64, -434.76), [], 55.0),

	("smolensk", "Smolensk", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-120.8, -396.4), [], 185.0),

	("polatsk", "Polatsk", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-85.082, -406.94), [], 270.0),

	("moscow", "Moscow", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-181.04, -412.4), [], 345.0),

	("minsk", "Minsk", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-71.92, -381.96), [], 115.0),

	("velikiye_luki", "Velikiye Luki", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-104.16, -423.08), [], 80.0),

	("pskov", "Pskov", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-80.0, -449.2), [], 240.0),

	("kaluga", "Kaluga", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-166.96, -391.84), [], 180.0),

	("ryazan", "Ryazan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-203.92, -393.08), [], 255.0),

	("halych", "Halych", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-40.8, -306.24), [], 125.0),

	("odesa", "Odesa", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-105.8, -269.04), [], 155.0),

	("chisinau", "Chisinau", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-85.48, -276.0), [], 45.0),

	("galati", "Galati", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-76.68, -253.84), [], 15.0),

	("bacau", "Bacau", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-64.52, -269.6), [], 125.0),

	("vinnytsia", "Vinnytsia", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-81.36, -308.28), []),

	("chernivtsi", "Chernivtsi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-53.88, -294.44), [], 240.0),

	("lviv", "Lviv", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-32.72, -317.24), [], 105.0),

	("granada", "Granada", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (268.84, -147.28), [], 180.0),

	("malaga", "Malaga", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (277.68, -141.4), [], 25.0),

	("ronda", "Ronda", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (284.0, -146.0), [], 260.0),

	("motril", "Motril", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (266.12, -144.52), [], 85.0),

	("onondaga", "Onondaga", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1062.0, -217.36), [], 290.0),

	("branford", "Branford", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1021.28, -200.52), [], 175.0),

	("bufflo_creek", "Bufflo creek", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1174.16, -190.04), [], 255.0),

	("grandriver", "Grandriver", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1117.6, -195.76), [], 115.0),

	("ottawa", "Ottawa", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1056.52, -253.48), [], 225.0),

	("milwaukee", "Milwaukee", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1191.56, -220.72), [], 15.0),

	("springfield", "Springfield", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1208.8, -178.68), [], 95.0),

	("montreal", "Montreal", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1030.56, -255.62), [], 45.0),

	("silverspring", "Silverspring", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1075.76, -163.28), [], 275.0),

	("quebec", "Quebec", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1008.1, -274.84), [], 315.0),

	("chicago", "Chicago", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1186.64, -206.12), [], 180.0),

	("mississauga", "Mississauga", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1100.64, -228.84), [], 335.0),

	("oshkosh", "Oshkosh", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1196.68, -235.0), [], 225.0),

	("aksum", "Aksum", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-199.93, 107.18), [], 25.0),

	("gondar", "Gondar", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-181.15, 117.21), [], 185.0),

	("kassala", "Kassala", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-165.03, 92.78), [], 50.0),

	("mek_ele", "Mek'ele", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-204.78, 111.14), [], 270.0),

	("dessie", "Dessie", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-216.83, 135.91), [], 270.0),

	("lhasa", "Lhasa", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-765.6, -58.8), [], 25.0),

	("ngari", "Ngari", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-645.2, -91.88), [], 15.0),

	("nagqu", "Nagqu", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-785.69, -78.82), [], 45.0),

	("xigaze", "Xigaze", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-734.78, -58.31), [], 180.0),

	("yushu", "Yushu", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-839.98, -93.95), [], 120.0),

	("skardu", "Skardu", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-587.32, -123.49), [], 30.0),

	("edinburgh", "Edinburgh", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (265.52, -415.32), [], 45.0),

	("glasgo", "Glasgo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (276.0, -414.8), [], 90.0),

	("inverness", "Inverness", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (275.18, -445.72), [], 65.0),

	("aberdeen", "Aberdeen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (253.0, -436.8), [], 270.0),

	("kirkwall", "Kirkwall", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (261.14, -471.74), [], 65.0),

	("stornoway", "Stornoway", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (298.9, -456.3), [], 180.0),

	("dunnegol", "Dunnegol", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (317.64, -393.92), [], 180.0),

	("dungenen", "Dungenen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (302.88, -391.36), [], 25.0),

	("galway", "Galway", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (328.36, -371.0), [], 25.0),

	("cork", "Cork", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (322.08, -348.96), [], 25.0),

	("carlow", "Carlow", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (305.04, -363.84), [], 160.0),

	("waterford", "Waterford", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (307.36, -354.8), [], 55.0),

	("erbing", "Erbing", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (17.2, -385.6), [], 240.0),

	("riga", "Riga", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-35.24, -434.74), [], 15.0),

	("kaliningrad", "Kaliningrad", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (5.12, -395.28), [], 80.0),

	("klaipeda", "Klaipeda", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1.88, -412.8), [], 80.0),

	("ventspils", "Ventspils", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-6.64, -440.96), [], 45.0),

	("tartu", "Tartu", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-62.24, -459.44), [], 315.0),

	("parnu", "Parnu", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-38.0, -459.92), [], 25.0),

	("jelgava", "Jelgava", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-29.44, -428.2), [], 215.0),

	("daugavpils", "Daugavpils", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-60.4, -414.8), [], 175.0),

	("santo_domingo", "Santo domingo", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (997.9, 59.66), [], 35.0),

	("south_hedland", "South hedland", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1068.16, 446.68), [], 15.0),

	("darwin", "Darwin", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1201.28, 366.12), [], 25.0),

	("nashville", "Nashville", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1177.16, -134.92), [], 125.0),

	("wilmington", "Wilmington", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1080.6, -111.56), [], 180.0),

	("saint_augustine", "Saint Augustine", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1119.32, -62.16), [], 280.0),

	("oklahoma", "Oklahoma", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1294.36, -126.72), [], 280.0),

	("kansas", "Kansas", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1262.32, -171.0), [], 180.0),

	("hauston", "Hauston", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1271.24, -61.04), [], 255.0),

	("santa_clara", "Santa clara", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1102.24, 19.04), [], 35.0),

	("new_orleans", "New orleans", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1214.32, -62.04), [], 45.0),

	("rio_de_janeiro", "Rio de janeiro", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (702.2, 470.4), [], 45.0),

	("salvador", "Salvador", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (648.64, 366.78), [], 65.0),

	("reykjabik", "Reykjabik", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (469.14, -574.7), [], 255.0),

	("la_romana", "La romana", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (982.64, 59.92), [], 315.0),

	("karratha", "Karratha", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1020.36, 467.16), [], 255.0),

	("kakadu", "Kakadu", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1217.72, 367.08), [], 175.0),

	("huntsville", "Huntsville", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1175.12, -117.76), [], 115.0),

	("fayetteville", "Fayetteville", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1091.0, -121.56), [], 35.0),

	("lakeland", "Lakeland", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1124.64, -41.88), [], 65.0),

	("tulsa", "Tulsa", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1277.6, -134.64), [], 235.0),

	("omaha", "Omaha", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1277.68, -197.64), [], 255.0),

	("san_antonio", "San antonio", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1305.4, -56.68), [], 225.0),

	("bayamo", "Bayamo", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1066.28, 40.16), [], 185.0),

	("mobile", "Mobile", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1191.2, -71.72), [], 75.0),

	("santos", "Santos", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (736.0, 481.08), [], 65.0),

	("porto_seguro", "Porto seguro", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (656.4, 403.76), [], 45.0),

	("arborg", "Arborg", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (458.64, -571.36), [], 90.0),

	("vinland", "Vinland", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (852.12, -326.56), [], 125.0),

	("brattalid", "Brattalid", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (720.12, -493.96), [], 145.0),

	("vinland_village", "Vinland Settlements", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (858.6, -317.2), [], 25.0),

	("brattalid_village", "Brattalid Settlements", icon_point_mark|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (726.08, -500.68), [], 115.0),

	("mombasa", "Mombasa", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-200.88, 280.4), [], 40.0),

	("mozambique", "Mozambique", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-213.48, 389.36), [], 35.0),

	("luanda", "Luanda", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (82.32, 329.72), [], 125.0),

	("yaounde", "Yaounde", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (103.64, 205.0), [], 280.0),

	("gunue", "Gunue", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-174.24, 394.48), [], 65.0),

	("malabo", "Malabo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (133.68, 207.86), [], 265.0),

	("nairobi", "Nairobi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-173.2, 255.08), [], 45.0),

	("kimayo", "Kimayo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-233.56, 242.4), [], 85.0),

	("boma", "Boma", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (86.24, 309.72), [], 85.0),

	("karagandy", "Karagandy", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-568.52, -312.12), [], 145.0),

	("samara", "Samara", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-316.56, -371.94), [], 55.0),

	("naiman", "Naiman", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-733.2, -275.2), [], 165.0),

	("oskemen", "Oskemen", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-671.0, -318.0), [], 25.0),

	("saransk", "Saransk", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-263.92, -385.72), []),

	("karazhal", "Karazhal", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-547.8, -289.2), [], 45.0),

	("ridder", "Ridder", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-682.72, -325.08), [], 55.0),

	("yalta", "Yalta", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-143.16, -241.52), [], 90.0),

	("naiman_ger", "Naiman ger", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-760.0, -269.76), [], 170.0),

	("nomad_yurt_1", "Nomad yurt 1", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-181.16, -300.8), [], 70.0),

	("nomad_yurt_2", "Nomad yurt 2", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-331.52, -338.52), [], 15.0),

	("nomad_yurt_3", "Nomad yurt 3", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-473.8, -317.88), [], 275.0),

	("nomad_yurt_4", "Nomad yurt 4", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-617.28, -321.96), [], 315.0),

	("xiongnu", "Xiongnu", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-962.96, -154.6), [], 15.0),

	("wuhuan", "Wuhuan", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1047.2, -208.0), [], 325.0),

	("goa", "Goa", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-580.0, 92.0), [], 135.0),

	("calcutta", "Calcutta", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-735.6, 17.6), [], 260.0),

	("vijayanagara", "Vijayanagara", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-681.8, 64.0), [], 260.0),

	("mumbai", "Mumbai", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-567.2, 54.24), []),

	("columbo", "Columbo", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-644.64, 175.48), []),

	("mysore", "Mysore", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-608.0, 121.92), [], 180.0),

	("cochi", "Cochi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-605.3, 147.06), [], 75.0),

	("chennai", "Chennai", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-646.56, 114.76), [], 45.0),

	("aurangabad", "Aurangabad", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-593.48, 45.48), [], 145.0),

	("ranchi", "Ranchi", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-702.4, 8.96), [], 275.0),

	("vijayawada", "Vijayawada", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-650.52, 81.2), [], 260.0),

	("pune", "Pune", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-577.2, 60.0), [], 90.0),

	("kandy", "Kandy", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-651.24, 170.0), [], 180.0),

	("rajkot", "Rajkot", icon_point_mark|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-544.0, 20.28), [], 45.0),

	("place_end", "place end", icon_cantsee|pf_disabled|pf_is_static|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (64.0, 52.0), []),

	("tradeport1", "St Helena", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (291.16, 398.48), [], 340.0),

	("tradeport2", "Toliara", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-247.8, 477.1), [], 90.0),

	("tradeport3", "Socotra", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-359.54, 121.58), [], 180.0),

	("tradeport4", "Batavia", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-943.8, 300.88), [], 330.0),

	("tradeport5", "Santa Cruz", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (406.86, -45.64), [], 225.0),

	("tradeport6", "Sierra Leone", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (395.38, 135.4), [], 135.0),

	("tradeport7", "Nicobar", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-781.8, 123.6), [], 90.0),

	("tradeport8", "Aceh", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-811.6, 188.48), [], 45.0),

	("tradeport9", "Luanda", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (85.78, 329.1), [], 45.0),

	("tradeport10", "Bermuda", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (935.68, -87.88), [], 225.0),

	("tradeport11", "Chaleston", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (1100.48, -95.32), [], 215.0),

	("tradeport12", "San Juan", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (950.72, 59.48), [], 340.0),

	("tradeport13", "Barbados", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (880.32, 111.98), [], 40.0),

	("tradeport14", "Havana", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (1127.8, 10.88), []),

	("tradeport15", "Santo Domingo", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (997.88, 62.24), [], 180.0),

	("tradeport16", "Santo Maria", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (1040.02, 132.42), [], 15.0),

	("tradeport17", "New Heaven", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (1025.34, -197.46), [], 200.0),

	("tradeport18", "San Miguel", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (1178.56, 39.34), []),

	("tradeport19", "Aden", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-262.7, 116.36), [], 195.0),

	("tradeport20", "Mogadishu", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-267.94, 221.96), [], 225.0),

	("tradeport21", "Cape Verde", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (486.38, 93.22), []),

	("tradeport22", "Port Hedland", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1069.08, 442.64), [], 20.0),

	("tradeport23", "Merauke", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1305.82, 327.38), [], 135.0),

	("tradeport24", "Nagasaki", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1188.14, -93.18), [], 135.0),

	("tradeport25", "Busan", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1181.26, -122.0), [], 225.0),

	("tradeport26", "Shanghai", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1101.94, -75.68), [], 265.0),

	("tradeport27", "Weihai", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1105.26, -150.98), [], 315.0),

	("tradeport28", "Manila", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1091.96, 99.3), [], 90.0),

	("tradeport29", "Nanzi", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1084.34, 16.9), [], 135.0),

	("tradeport30", "Haiphong", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-936.62, 37.92), [], 225.0),

	("tradeport31", "Bangkok", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-869.76, 110.7), [], 180.0),

	("tradeport32", "Calcutta", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-735.8, 26.8), [], 165.0),

	("tradeport33", "Goa", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-575.82, 90.2), [], 105.0),

	("tradeport34", "Lisbon", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (328.62, -162.24), [], 180.0),

	("tradeport35", "Cadiz", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (298.24, -140.0), [], 120.0),

	("tradeport36", "Bristol", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (259.52, -342.56), [], 80.0),

	("tradeport37", "Nante", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (249.9, -279.66), [], 135.0),

	("tradeport38", "Amsterdam", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (173.64, -358.62), [], 330.0),

	("tradeport39", "Copenhagen", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (94.34, -407.86), [], 270.0),

	("tradeport40", "Stockholm", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (23.52, -472.22), [], 225.0),

	("tradeport41", "Ceuta", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (288.74, -130.76), []),

	("tradeport42", "Valencia", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (231.8, -177.28), [], 270.0),

	("tradeport43", "Marseille", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (170.56, -224.36), [], 100.0),

	("tradeport44", "Syracuse", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (62.26, -146.62), [], 270.0),

	("tradeport45", "Roma", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (96.08, -206.28), [], 135.0),

	("tradeport46", "Tunis", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (117.12, -144.96), [], 300.0),

	("tradeport47", "Athens", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-33.04, -152.98), [], 210.0),

	("tradeport48", "Alexandria", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-97.82, -77.6), [], 25.0),

	("tradeport49", "Constantinople", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-84.18, -194.84), [], 160.0),

	("tradeport50", "Tripoli", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-163.08, -115.28), [], 60.0),

	("tradeport51", "Muscat", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-410.0, 5.92), []),

	("tradeport52", "Cape town", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (28.34, 592.82), [], 45.0),

	("tradeport53", "Mozambique", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-215.28, 384.76), [], 270.0),

	("tradeport54", "Calabar", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (138.34, 198.74), [], 180.0),

	("tradeport55", "Ponta Delgada", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (509.42, -152.42), [], 135.0),

	("tradeport56", "Funchal", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (414.36, -93.14), [], 175.0),

	("tradeport57", "San Andres", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (1119.84, 121.94), [], 115.0),

	("tradeport58", "London", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (225.0, -342.52), [], 240.0),

	("tradeport59", "Incheon", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1153.04, -148.46), [], 90.0),

	("tradeport60", "Lome", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (217.46, 184.68), [], 225.0),

	("tradeport61", "Gdynia", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (25.94, -391.94), [], 295.0),

	("tradeport62", "Oslo", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (113.6, -487.32), [], 180.0),

	("tradeport63", "Carballo", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (324.58, -225.52), []),

	("tradeport64", "Hongkong", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1014.72, 21.88), [], 180.0),

	("tradeport65", "Le havre", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (228.04, -312.32), [], 90.0),

	("tradeport66", "Rio de janeiro", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (697.74, 471.84), [], 180.0),

	("tradeport67", "Sakai", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1249.52, -115.96), [], 90.0),

	("tradeport68", "Mombasa", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-203.56, 283.12), [], 260.0),

	("tradeport69", "Venezia", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (92.61, -254.04), [], 225.0),

	("tradeport70", "Sham el sheikh", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-145.0, -39.42), [], 225.0),

	("tradeport71", "Abadan", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-300.42, -60.64), [], 225.0),

	("tradeport72", "Tianjin", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1057.0, -168.2), [], 225.0),

	("tradeport73", "Karachi", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-504.06, -4.82), [], 125.0),

	("tradeport74", "Trabzon", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-206.4, -195.26), []),

	("tradeport75", "Riga", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-33.66, -436.26), [], 35.0),

	("tradeport76", "Edo", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1297.84, -126.76), [], 235.0),

	("tradeport77", "Izumo", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1220.72, -124.96), [], 90.0),

	("tradeport78", "Lianyungang", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1075.2, -117.66), [], 315.0),

	("tradeport79", "Yingkou", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1103.68, -189.48), [], 135.0),

	("tradeport80", "Haesamwi", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1209.86, -219.32), [], 225.0),

	("tradeport81", "Sapporo", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1313.76, -223.98), [], 35.0),

	("tradeport82", "Caliari", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (131.48, -169.62), [], 245.0),

	("tradeport83", "Rhodes", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-77.66, -134.42), [], 225.0),

	("tradeport84", "Mokpo", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1148.2, -116.14), [], 115.0),

	("tradeport85", "Wenzhou", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1089.58, -39.26), [], 225.0),

	("tradeport86", "Bordeaux", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (237.82, -251.74), [], 5.0),

	("tradeport87", "Dublin", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (295.7, -372.86), [], 270.0),

	("tradeport88", "Bremerhavan", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (136.5, -376.6), [], 40.0),

	("tradeport89", "Odesa", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-106.22, -266.62), [], 225.0),

	("tradeport90", "Benghazi", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (9.08, -88.36), [], 55.0),

	("tradeport91", "Jeddah", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-197.64, 28.44), [], 100.0),

	("tradeport92", "Gaza", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-146.48, -80.9), [], 45.0),

	("tradeport93", "Columbo", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-642.28, 173.3), [], 100.0),

	("tradeport94", "Bintulu", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1006.6, 209.14), [], 45.0),

	("tradeport95", "Darwin", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1199.3, 363.54), [], 45.0),

	("tradeport96", "Sipontum", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (54.8, -202.74), [], 235.0),

	("tradeport97", "Massawa", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-203.64, 90.0), [], 20.0),

	("tradeport98", "Tortuga", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (1022.12, 43.54), [], 170.0),

	("tradeport99", "Alger", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (195.08, -142.5), []),

	("tradeport100", "Port Royal", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (1077.12, 65.84), [], 200.0),

	("tradeport101", "Tsushima", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1183.9, -112.0), [], 225.0),

	("tradeport102", "Shilin", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1097.08, -11.02), [], 25.0),

	("tradeport103", "Jaffna", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-643.94, 149.14), [], 155.0),

	("tradeport104", "Mayotte", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-262.54, 368.54), [], 135.0),

	("tradeport105", "Mindelo", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (502.22, 73.54), [], 315.0),

	("tradeport106", "San fernaldo", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (900.62, 141.98), [], 90.0),

	("tradeport107", "Angra do heroismo", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (523.34, -165.38), [], 270.0),

	("tradeport108", "Farsund", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (157.04, -453.92), [], 135.0),

	("tradeport109", "Antalaha", icon_harbor|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-319.72, 387.96), [], 315.0),

	("tradeport_end", "tradeport end", icon_cantsee|pf_disabled|pf_is_static|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("tradeguild1", "Turpan", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-744.84, -219.96), [], 145.0),

	("tradeguild2", "Changzhou", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1046.84, -160.52), [], 15.0),

	("tradeguild3", "Thai Nguyen", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-926.28, 27.92), [], 265.0),

	("tradeguild4", "Enshi", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-966.36, -66.4), [], 115.0),

	("tradeguild5", "Huelun", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1077.62, -304.6), [], 45.0),

	("tradeguild6", "Fuxin", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-1099.4, -207.96), [], 275.0),

	("tradeguild7", "Gorgan", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-364.96, -142.56), [], 35.0),

	("tradeguild8", "Abadeh", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-345.36, -76.36), [], 225.0),

	("tradeguild9", "Adrar", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (232.96, -39.56), [], 95.0),

	("tradeguild10", "Linz", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (73.64, -294.68), [], 175.0),

	("tradeguild11", "Garrotxa", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (202.52, -210.12), [], 45.0),

	("tradeguild12", "Ales", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (184.88, -236.04), [], 25.0),

	("tradeguild13", "Brest", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-28.84, -352.84), [], 75.0),

	("tradeguild14", "Ternopil", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-50.0, -313.08), [], 145.0),

	("tradeguild15", "Al Bukamal", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-217.36, -115.32), [], 325.0),

	("tradeguild16", "Elverum", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (103.2, -507.44), [], 115.0),

	("tradeguild17", "Shumen", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-64.6, -224.6), [], 225.0),

	("tradeguild18", "Ahbaz", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-302.08, -78.08), [], 270.0),

	("tradeguild19", "Dhaka", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-758.08, 5.2), [], 75.0),

	("tradeguild20", "Uliastai", icon_house_exn|pf_label_medium|pf_village, no_menu, pt_none, fac_tradeport, aggressiveness_0, ai_bhvr_hold, 0, (-831.4, -292.88), [], 195.0),

	("tradeguild_end", "tradeguild end", icon_cantsee|pf_disabled|pf_is_static|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (48.0, 48.0), []),

	("bridge_1", "{!}1", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1304.0, -130.8), [], 335.0),

	("bridge_2", "{!}2", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1174.2, -126.2), [], 90.0),

	("bridge_3", "{!}3", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1019.58, -267.12), [], 40.0),

	("bridge_4", "{!}4", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1131.2, -186.2), [], 40.0),

	("bridge_5", "{!}5", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1182.2, -211.2), [], 40.0),

	("bridge_6", "{!}6", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1103.4, -196.94), [], 40.0),

	("bridge_7", "{!}7", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1121.76, -217.25), [], 100.0),

	("bridge_8", "{!}8", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1091.14, -216.18), []),

	("bridge_9", "{!}9", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1220.28, -288.88), [], 70.0),

	("bridge_10", "{!}10", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1084.14, -43.58), [], 145.0),

	("bridge_11", "{!}11", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1084.18, -66.24), [], 45.0),

	("bridge_12", "{!}12", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1000.22, -154.22), [], 80.0),

	("bridge_13", "{!}13", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1048.32, -176.34), [], 140.0),

	("bridge_14", "{!}14", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1226.04, -177.54), [], 100.0),

	("bridge_15", "{!}15", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1253.8, -92.74), [], 105.0),

	("bridge_16", "{!}16", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1224.32, -95.52), [], 105.0),

	("bridge_17", "{!}17", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (228.72, 82.76), [], 115.0),

	("bridge_18", "{!}18", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (284.9, 102.96), [], 195.0),

	("bridge_19", "{!}19", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (156.56, 185.86), [], 75.0),

	("bridge_20", "{!}20", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-996.1, -86.88), [], 340.0),

	("bridge_21", "{!}21", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-906.336, -126.5336), [], 45.0),

	("bridge_22", "{!}22", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-924.72, -88.28), [], 280.0),

	("bridge_23", "{!}23", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-935.28, -57.68), [], 45.0),

	("bridge_24", "{!}24", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-899.9, -37.98), [], 260.0),

	("bridge_25", "{!}25", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-920.16, 29.38), [], 95.0),

	("bridge_26", "{!}26", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1059.24, -110.36), [], 330.0),

	("bridge_27", "{!}27", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-984.34, -168.48), [], 75.0),

	("bridge_28", "{!}28", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-932.8, -164.68), [], 75.0),

	("bridge_29", "{!}29", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-988.78, -50.68), [], 30.0),

	("bridge_30", "{!}30", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1023.22, -14.46), [], 45.0),

	("bridge_31", "{!}31", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1178.78, -131.38), []),

	("bridge_32", "{!}32", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1037.48, -2.62), [], 100.0),

	("bridge_33", "{!}33", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1074.86, -93.6), [], 135.0),

	("bridge_34", "{!}34", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-895.78, -397.18), [], 110.0),

	("bridge_35", "{!}35", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-672.32, -319.64), [], 160.0),

	("bridge_36", "{!}36", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-644.24, -231.7), [], 170.0),

	("bridge_37", "{!}37", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-451.824, -186.734), [], 115.0),

	("bridge_38", "{!}38", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-490.22, -242.38), [], 330.0),

	("bridge_39", "{!}39", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-338.98, -279.98), [], 260.0),

	("bridge_40", "{!}40", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-267.46, -297.68), []),

	("bridge_41", "{!}41", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-297.22, -359.04), [], 90.0),

	("bridge_42", "{!}42", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-218.24, -284.58), [], 40.0),

	("bridge_43", "{!}43", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-35.84, -431.28), [], 165.0),

	("bridge_44", "{!}44", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-144.64, -301.52), [], 145.0),

	("bridge_45", "{!}45", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (21.82, -379.28), [], 90.0),

	("bridge_46", "{!}46", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (73.66, -377.06), [], 90.0),

	("bridge_47", "{!}47", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (7.54, -249.88), [], 135.0),

	("bridge_48", "{!}48", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (136.22, -270.24), [], 20.0),

	("bridge_49", "{!}49", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (263.62, -217.34), [], 105.0),

	("bridge_50", "{!}50", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-106.66, -72.68), [], 100.0),

	("bridge_51", "{!}51", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-112.92, -59.76), [], 90.0),

	("bridge_52", "{!}52", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-116.32, -26.08), [], 120.0),

	("bridge_53", "{!}53", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-129.32, -8.72), [], 105.0),

	("bridge_54", "{!}54", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-103.04, 50.54), [], 95.0),

	("bridge_55", "{!}55", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-517.5, -9.3), [], 90.0),

	("bridge_56", "{!}56", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-549.28, -63.08), [], 75.0),

	("bridge_57", "{!}57", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-597.46, 14.52), [], 100.0),

	("bridge_58", "{!}58", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-573.18, 25.74), []),

	("bridge_59", "{!}59", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-626.04, 85.68), [], 100.0),

	("bridge_60", "{!}60", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-671.64, -10.34), [], 170.0),

	("bridge_61", "{!}61", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-760.96, 13.86), [], 105.0),

	("bridge_62", "{!}62", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-749.08, -8.16), [], 85.0),

	("bridge_63", "{!}63", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-811.62, 27.4), [], 130.0),

	("bridge_64", "{!}64", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-805.78, 35.38), [], 105.0),

	("bridge_65", "{!}65", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-928.08, 107.04), [], 100.0),

	("bridge_wood_end", "Bridge wood end", icon_cantsee|pf_disabled|pf_is_static|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (64.0, 52.0), []),

	("bridge_stone_1", "{!}1", icon_bridge_stone|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1157.4, -153.8), []),

	("bridge_stone_2", "{!}2", icon_bridge_stone|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1018.14, -121.12), [], 20.0),

	("bridge_stone_3", "{!}3", icon_bridge_stone|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-964.82, -110.16), [], 75.0),

	("bridge_stone_4", "{!}4", icon_bridge_stone|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-944.96, -113.62), [], 340.0),

	("bridge_stone_5", "{!}5", icon_bridge_stone|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-967.64, -114.16), []),

	("bridge_stone_6", "{!}6", icon_bridge_stone|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-985.38, -69.88), [], 330.0),

	("bridge_stone_7", "{!}7", icon_bridge_stone|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1043.0, -91.82), [], 20.0),

	("bridge_stone_8", "{!}8", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (8.3, -356.58), [], 170.0),

	("bridge_stone_9", "{!}9", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-63.92, -235.78), [], 5.0),

	("bridge_stone_10", "{!}10", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (7.84, -250.62), [], 100.0),

	("bridge_stone_11", "{!}11", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (71.02, -262.86), [], 90.0),

	("bridge_stone_12", "{!}12", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (88.0, -280.1), []),

	("bridge_stone_13", "{!}13", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (174.28, -231.68), [], 90.0),

	("bridge_stone_14", "{!}14", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (106.5, -369.9), [], 140.0),

	("bridge_stone_15", "{!}15", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (178.56, -345.4), [], 155.0),

	("bridge_stone_16", "{!}16", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (144.88, -321.42), [], 120.0),

	("bridge_stone_17", "{!}17", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (221.92, -191.98), [], 10.0),

	("bridge_stone_18", "{!}18", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (319.12, -198.68), [], 170.0),

	("bridge_stone_19", "{!}19", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (327.8, -166.72), [], 40.0),

	("bridge_stone_20", "{!}20", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (283.28, -179.12), [], 10.0),

	("bridge_stone_21", "{!}21", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-252.92, -92.58), [], 100.0),

	("bridge_stone_22", "{!}22", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-262.32, -96.42), [], 160.0),

	("bridge_stone_23", "{!}23", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-299.32, -65.58), [], 100.0),

	("bridge_stone_24", "{!}24", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-624.6, -24.38), [], 10.0),

	("bridge_stone_25", "{!}25", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (292.72, -148.4), [], 30.0),

	("bridge_stone_26", "{!}26", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (226.92, -279.34), [], 175.0),

	("bridge_stone_27", "{!}27", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (211.42, -305.06), [], 150.0),

	("bridge_stone_28", "{!}28", icon_bridge_wood|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1147.36, -169.28), [], 20.0),

	("bridge_stone_end", "Bridge stone end", icon_cantsee|pf_disabled|pf_is_static|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (52.0, 64.0), []),

	("wasteland1", "Wasteland Santo domingo", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (997.9, 59.66), []),

	("wasteland2", "Wasteland South hedland", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (-1068.16, 446.68), []),

	("wasteland3", "Wasteland Darwin", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (-1201.28, 366.12), []),

	("wasteland4", "Wasteland Nashville", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (1177.16, -134.92), []),

	("wasteland5", "Wasteland Wilmington", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (1080.6, -111.56), []),

	("wasteland6", "Wasteland Saint Augustine", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (1117.88, -62.2), []),

	("wasteland7", "Wasteland Oklahoma", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (1294.36, -126.72), []),

	("wasteland8", "Wasteland Kansas", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (1262.32, -171.0), []),

	("wasteland9", "Wasteland Hauston", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (1271.24, -61.04), []),

	("wasteland10", "Wasteland Santa clara", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (1102.24, 19.04), []),

	("wasteland11", "Wasteland New orleans", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (1214.32, -62.04), []),

	("wasteland12", "Wasteland Rio de janeiro", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (702.2, 470.4), []),

	("wasteland13", "Wasteland Salvador", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (648.64, 366.78), []),

	("wasteland14", "Wasteland Reykjabik", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (469.14, -574.7), []),

	("wasteland15", "Wasteland Vinland", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (852.12, -326.56), []),

	("wasteland16", "Wasteland Brattalid", icon_point_mark|pf_label_medium|pf_village, no_menu, pt_none, fac_hot_points, aggressiveness_0, ai_bhvr_hold, 0, (720.12, -493.96), []),

	("ruin_1", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (27.08, 593.92), []),

	("ruin_2", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1183.62, -131.16), []),

	("ruin_3", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-107.96, -62.92), []),

	("ruin_4", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-27.32, -159.2), []),

	("ruin_5", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (112.0, -228.0), []),

	("ruin_6", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (92.0, -212.0), []),

	("ruin_7", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (260.0, -220.0), []),

	("ruin_8", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-19.0, -164.0), []),

	("ruin_9", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (249.2, -340.0), []),

	("ruin_10", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-120.0, -12.0), []),

	("ruin_11", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1042.4, -202.4), []),

	("ruin_12", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-38.0, -124.0), []),

	("ruin_13", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-58.46, -179.66), []),

	("ruin_14", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (246.8, -299.2), []),

	("ruin_15", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (262.6, -285.68), []),

	("ruin_16", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (728.0, -576.0), []),

	("ruin_17", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (324.0, -168.0), []),

	("ruin_18", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (205.88, -297.56), []),

	("ruin_19", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (270.24, -145.66), []),

	("ruin_20", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1045.2, -189.6), []),

	("ruin_21", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-120.0, -24.0), []),

	("ruin_22", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1407.8, -147.36), []),

	("ruin_23", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1197.2, 39.6), []),

	("ruin_24", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (659.16, -625.0), []),

	("ruin_25", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1025.28, 161.92), []),

	("ruin_26", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1022.84, 372.52), []),

	("ruin_27", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-635.2, 134.0), []),

	("ruin_28", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-156.6, -65.52), []),

	("ruin_29", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-259.72, -95.0), []),

	("ruin_30", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-895.24, 103.12), []),

	("ruin_31", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1240.0, -119.2), []),

	("ruin_32", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1015.2, -161.6), []),

	("ruin_33", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-964.9, -115.64), []),

	("ruin_34", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1423.8, 516.72), []),

	("ruin_35", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1158.32, -140.28), []),

	("ruin_36", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (279.68, 107.16), []),

	("ruin_37", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-113.1, 20.28), []),

	("ruin_38", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (298.0, -152.0), []),

	("ruin_39", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-102.6, -74.4), []),

	("ruin_40", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-55.4, 440.0), []),

	("ruin_41", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1093.48, -222.0), []),

	("ruin_42", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1223.52, 250.64), []),

	("ruin_43", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-762.4, -58.8), []),

	("ruin_44", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-30.0, -160.8), []),

	("ruin_45", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (276.0, -441.8), []),

	("ruin_46", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1033.66, -183.48), []),

	("ruin_47", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1016.48, 19.84), []),

	("ruin_48", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1250.24, -123.56), []),

	("ruin_49", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1198.24, -94.36), []),

	("ruin_50", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1155.98, -102.8), []),

	("ruin_51", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1149.92, -211.4), []),

	("ruin_52", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-138.14, -244.58), []),

	("ruin_53", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1155.2, -136.0), []),

	("ruin_54", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1018.64, -65.2), []),

	("ruin_55", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-788.96, -174.68), []),

	("ruin_56", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-907.28, -95.76), []),

	("ruin_57", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-903.6, -58.72), []),

	("ruin_58", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1006.8, -118.8), []),

	("ruin_59", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-896.0, -76.4), []),

	("ruin_60", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1056.0, -8.0), []),

	("ruin_61", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1154.72, -125.16), []),

	("ruin_62", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1253.6, -116.0), []),

	("ruin_63", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1160.62, -154.06), []),

	("ruin_64", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-893.2, -286.8), []),

	("ruin_65", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-790.0, -318.8), []),

	("ruin_66", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1165.12, -21.64), []),

	("ruin_67", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1287.12, -123.0), []),

	("ruin_68", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1169.84, -130.0), []),

	("ruin_69", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-622.36, -32.4), []),

	("ruin_70", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-654.88, 165.88), []),

	("ruin_71", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-651.2, 164.8), []),

	("ruin_72", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-614.96, 11.36), []),

	("ruin_73", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-589.88, 42.92), []),

	("ruin_74", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-594.8, 86.4), []),

	("ruin_75", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-698.64, -5.68), []),

	("ruin_76", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-713.04, 42.12), []),

	("ruin_77", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1073.12, 158.88), []),

	("ruin_78", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1072.0, 140.6), []),

	("ruin_79", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-975.4, 316.94), []),

	("ruin_80", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-869.2, 94.4), []),

	("ruin_81", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-976.56, 317.44), []),

	("ruin_82", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-954.0, 88.4), []),

	("ruin_83", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1381.2, 417.2), []),

	("ruin_84", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1170.4, 406.8), []),

	("ruin_85", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1010.0, 498.8), []),

	("ruin_86", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1199.2, 498.0), []),

	("ruin_87", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1411.6, 589.04), []),

	("ruin_88", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (179.6, -131.4), []),

	("ruin_89", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (306.0, 71.6), []),

	("ruin_90", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-129.28, -15.08), []),

	("ruin_91", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (121.4, -145.88), []),

	("ruin_92", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-9.28, -95.0), []),

	("ruin_93", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (76.04, -92.96), []),

	("ruin_94", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (289.36, -104.98), []),

	("ruin_95", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-139.32, 74.88), []),

	("ruin_96", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (156.0, -141.6), []),

	("ruin_97", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-204.4, 277.44), []),

	("ruin_98", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-68.0, 500.4), []),

	("ruin_99", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-177.2, 270.8), []),

	("ruin_100", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (126.8, -17.2), []),

	("ruin_101", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (229.64, 85.82), []),

	("ruin_102", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-8.4, 424.68), []),

	("ruin_103", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-69.6, 510.4), []),

	("ruin_104", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (4.4, 50.4), []),

	("ruin_105", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-183.76, -29.36), []),

	("ruin_106", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-167.6, -92.44), []),

	("ruin_107", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-391.04, 8.0), []),

	("ruin_108", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-407.48, -53.48), []),

	("ruin_109", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-285.2, -113.52), []),

	("ruin_110", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-132.4, -119.26), []),

	("ruin_111", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-309.08, -182.32), []),

	("ruin_112", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-372.92, -148.16), []),

	("ruin_113", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-237.08, -130.08), []),

	("ruin_114", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-361.8, 119.48), []),

	("ruin_115", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1212.0, 65.36), []),

	("ruin_116", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1311.6, 62.0), []),

	("ruin_117", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (894.12, 193.44), []),

	("ruin_118", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (908.92, 188.64), []),

	("ruin_119", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1406.0, -136.0), []),

	("ruin_120", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1073.28, 331.92), []),

	("ruin_121", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (963.12, 635.36), []),

	("ruin_122", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1291.0, 39.44), []),

	("ruin_123", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (799.76, -626.6), []),

	("ruin_124", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1056.0, 380.8), []),

	("ruin_125", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1200.0, 99.6), []),

	("ruin_126", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1405.6, -152.0), []),

	("ruin_127", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1059.8, 213.88), []),

	("ruin_128", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (694.0, 322.8), []),

	("ruin_129", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1057.6, 44.0), []),

	("ruin_130", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1079.6, 344.8), []),

	("ruin_131", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (942.4, 472.0), []),

	("ruin_132", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1180.0, 188.0), []),

	("ruin_133", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1438.0, -298.0), []),

	("ruin_134", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1205.2, 105.6), []),

	("ruin_135", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (154.0, -531.04), []),

	("ruin_136", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-39.92, -494.08), []),

	("ruin_137", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (126.0, -414.8), []),

	("ruin_138", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (111.0, -424.56), []),

	("ruin_139", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-503.46, -178.48), []),

	("ruin_140", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-596.0, -232.8), []),

	("ruin_141", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-406.2, -159.8), []),

	("ruin_142", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-515.2, -233.0), []),

	("ruin_143", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1156.56, -509.16), []),

	("ruin_144", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-701.44, -317.04), []),

	("ruin_145", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1266.0, -258.0), []),

	("ruin_146", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (965.84, 554.88), []),

	("ruin_147", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-156.68, -77.84), []),

	("ruin_148", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1165.6, -144.16), []),

	("ruin_149", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-244.68, -138.56), []),

	("ruin_150", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1015.32, -66.2), []),

	("ruin_151", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1018.26, -121.1), []),

	("ruin_152", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1259.36, -125.88), []),

	("ruin_153", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1174.52, -118.44), []),

	("ruin_154", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-18.08, -168.52), []),

	("ruin_155", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (56.88, -199.68), []),

	("ruin_156", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1050.48, -109.4), []),

	("ruin_157", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-196.96, -143.08), []),

	("ruin_158", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-28.36, -152.0), []),

	("ruin_159", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-32.84, -159.2), []),

	("ruin_160", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (156.0, -296.56), []),

	("ruin_161", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (4.64, -167.2), []),

	("ruin_162", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-57.76, -203.0), []),

	("ruin_163", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1143.6, -182.2), []),

	("ruin_164", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-201.32, 6.6), []),

	("ruin_165", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-15.6, -329.16), []),

	("ruin_166", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-234.32, -169.8), []),

	("ruin_167", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-986.84, -72.8), []),

	("ruin_168", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (180.84, -311.12), []),

	("ruin_169", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-172.72, -116.28), []),

	("ruin_170", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-534.16, -224.32), []),

	("ruin_171", "   ", icon_point_mark|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1010.48, -116.08), []),

	("ruin_end", "ruin end", icon_cantsee|pf_disabled|pf_is_static|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (36.0, 36.0), []),

	("ruin_dummy_1", "ruin end", icon_cantsee|pf_disabled|pf_is_static|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("ruin_dummy_2", "ruin end", icon_cantsee|pf_disabled|pf_is_static|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("ruin_dummy_3", "ruin end", icon_cantsee|pf_disabled|pf_is_static|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("ruin_dummy_4", "ruin end", icon_cantsee|pf_disabled|pf_is_static|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("ruin_dummy_5", "ruin end", icon_cantsee|pf_disabled|pf_is_static|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("attack_target", "   ", icon_attack_target|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("defence_target", "   ", icon_defence_target|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("tournament_flag_1", "   ", icon_tournament_flag|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("tournament_flag_2", "   ", icon_tournament_flag|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("tournament_flag_3", "   ", icon_tournament_flag|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("tournament_flag_4", "   ", icon_tournament_flag|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("tournament_flag_5", "   ", icon_tournament_flag|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("tournament_flag_6", "   ", icon_tournament_flag|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("tournament_flag_7", "   ", icon_tournament_flag|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("tournament_flag_8", "   ", icon_tournament_flag|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_01", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_02", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_03", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_04", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_05", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_06", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_07", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_08", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_09", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_10", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_11", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_12", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_13", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_14", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_15", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_16", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_17", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_18", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_19", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_20", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_21", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_22", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_23", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_24", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_25", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_26", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_27", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_28", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_29", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_30", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_31", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_32", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_33", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_34", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_35", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_36", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_37", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_38", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_39", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_40", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_41", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_42", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_43", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_44", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_45", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_46", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_47", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_48", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_49", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_50", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_cave_end", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_01", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_02", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_03", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_04", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_05", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_06", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_07", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_08", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_09", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_10", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_11", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_12", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_13", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_14", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_15", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_16", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_17", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_18", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_19", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_20", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_21", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_22", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_23", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_24", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_25", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_26", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_27", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_28", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_29", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_30", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_31", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_32", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_33", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_34", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_35", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_36", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_37", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_38", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_39", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_40", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_fort_end", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_rescue_lady_01", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_rescue_lady_02", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_rescue_lady_03", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_rescue_lady_end", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_01", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_02", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_03", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_04", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_05", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_06", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_07", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_08", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_09", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_10", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_11", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_12", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_13", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_14", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_15", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_16", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_17", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_18", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_19", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_20", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_nomad_end", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_01", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_02", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_03", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_04", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_05", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_06", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_07", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_08", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_09", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_10", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_11", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_12", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_13", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_14", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_15", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_16", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_17", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_18", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_19", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_20", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_21", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_22", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_23", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_24", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_25", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_26", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_27", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_28", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_29", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_30", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_farmhouse_end", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_01", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_02", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_03", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_04", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_05", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_06", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_07", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_08", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_09", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_10", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_11", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_12", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_13", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_14", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_15", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_16", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_17", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_18", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_19", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_20", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("rand_quest_caravan_end", "   ", icon_point_mark|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("for_quest_villa", "   ", icon_point_mark|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("workshop_party", "   ", icon_point_mark|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("brothel_party", "   ", icon_point_mark|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("nakepit_party", "   ", icon_point_mark|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("ply_hideout", "   ", icon_house_exn|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_riot", "   ", icon_disaster_riot|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_fire", "   ", icon_disaster_fire|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_typhoon", "   ", icon_disaster_typhoon|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_flood", "   ", icon_disaster_flood|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_epidemic", "   ", icon_disaster_blackdeath|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_earthquake", "   ", icon_disaster_earthquake|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_tides", "   ", icon_disaster_tides|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_ice_town", "   ", icon_disaster_ice|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_volcano", "   ", icon_disaster_volcano|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_malaria", "   ", icon_disaster_malaria|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_sand_town", "   ", icon_disaster_sand|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_sand_ply", "   ", icon_disaster_sand|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_storm_ply", "   ", icon_disaster_storm|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_ice_ply", "   ", icon_disaster_ice|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_sand_ai_1", "   ", icon_disaster_sand|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_storm_ai_1", "   ", icon_disaster_storm|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_ice_ai_1", "   ", icon_disaster_ice|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_sand_ai_2", "   ", icon_disaster_sand|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_storm_ai_2", "   ", icon_disaster_storm|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_ice_ai_2", "   ", icon_disaster_ice|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_sand_ai_3", "   ", icon_disaster_sand|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_storm_ai_3", "   ", icon_disaster_storm|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("disaster_ice_ai_3", "   ", icon_disaster_ice|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("markpoint_sea_mid1", "   ", icon_text_sea_01|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (177.0, -165.0), [], 5.0),

	("markpoint_sea_mid2", "   ", icon_text_sea_01|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-26.0, -105.0), [], 355.0),

	("markpoint_sea_oriental", "   ", icon_text_sea_02|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1210.0, -146.0), [], 20.0),

	("markpoint_sea_baltic", "   ", icon_text_sea_03|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (24.0, -420.0), [], 40.0),

	("markpoint_sea_north", "   ", icon_text_sea_04|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (185.0, -408.0), [], 25.0),

	("markpoint_sea_black", "   ", icon_text_sea_05|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-141.0, -225.0), []),

	("markpoint_sea_schina", "   ", icon_text_sea_06|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1022.0, 95.0), []),

	("markpoint_sea_caspi", "   ", icon_text_sea_07|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-323.0, -207.0), []),

	("markpoint_sea_adri", "   ", icon_text_sea_08|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (54.0, -214.0), [], 330.0),

	("markpoint_sea_red", "   ", icon_text_sea_09|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-194.0, 49.0), [], 315.0),

	("markpoint_sea_cari", "   ", icon_text_sea_10|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (997.0, 95.0), []),

	("markpoint_sea_aeg", "   ", icon_text_sea_11|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-49.0, -151.0), [], 335.0),

	("markpoint_sea_echina", "   ", icon_text_sea_12|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1144.0, -63.0), [], 10.0),

	("markpoint_sea_arab", "   ", icon_text_sea_13|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-445.0, 89.0), []),

	("markpoint_sea_pers", "   ", icon_text_sea_14|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-335.0, -27.0), [], 330.0),

	("markpoint_sea_anda", "   ", icon_text_sea_15|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-815.0, 137.0), []),

	("markpoint_sea_ioni", "   ", icon_text_sea_16|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (26.0, -153.0), []),

	("markpoint_sea_bengal", "   ", icon_text_sea_17|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-720.0, 94.0), []),

	("markpoint_sea_lacca", "   ", icon_text_sea_18|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-598.0, 176.0), [], 340.0),

	("markpoint_sea_bohai", "   ", icon_text_sea_19|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1081.0, -165.0), [], 15.0),

	("markpoint_sea_yellow", "   ", icon_text_sea_20|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1118.0, -125.0), [], 20.0),

	("markpoint_sea_oho", "   ", icon_text_sea_21|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1383.0, -389.0), []),

	("markpoint_sea_java", "   ", icon_text_sea_22|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-992.0, 291.0), [], 350.0),

	("markpoint_sea_siam", "   ", icon_text_sea_23|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-885.0, 149.0), [], 320.0),

	("markpoint_sea_aral", "   ", icon_text_sea_24|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-426.0, -246.0), []),

	("markpoint_sea_albo", "   ", icon_text_sea_25|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (262.0, -131.0), []),

	("markpoint_sea_levan", "   ", icon_text_sea_26|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-144.0, -103.0), [], 70.0),

	("markpoint_sea_biscay", "   ", icon_text_sea_27|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (283.0, -255.0), [], 25.0),

	("markpoint_sea_norway", "   ", icon_text_sea_28|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (262.0, -566.0), []),

	("markpoint_sea_engc", "   ", icon_text_sea_29|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (244.0, -322.0), [], 10.0),

	("markpoint_sea_maxi", "   ", icon_text_sea_30|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1213.0, -10.0), []),

	("markpoint_sea_sagas", "   ", icon_text_sea_31|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1040.0, -70.0), [], 5.0),

	("markpoint_sea_tyr", "   ", icon_text_sea_32|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (98.0, -179.0), [], 335.0),

	("markpoint_sea_hud", "   ", icon_text_sea_33|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1165.0, -482.0), []),

	("markpoint_sea_carpen", "   ", icon_text_sea_34|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1289.0, 376.0), []),

	("markpoint_geo_gobi", "   ", icon_text_geo_01|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-923.0, -212.0), []),

	("markpoint_geo_xinjiang", "   ", icon_text_geo_02|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-704.0, -184.0), []),

	("markpoint_geo_balqash", "   ", icon_text_geo_03|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-586.0, -268.0), [], 35.0),

	("markpoint_geo_sahara", "   ", icon_text_geo_04|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (132.0, -28.0), []),

	("markpoint_geo_gibr", "   ", icon_text_geo_05|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (288.0, -134.0), []),

	("markpoint_geo_alps", "   ", icon_text_geo_06|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (137.0, -260.0), [], 25.0),

	("markpoint_geo_green", "   ", icon_text_geo_07|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (735.0, -589.0), []),

	("markpoint_geo_ice", "   ", icon_text_geo_08|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (425.0, -592.0), []),

	("markpoint_geo_aus", "   ", icon_text_geo_09|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1214.0, 489.0), []),

	("markpoint_geo_papu", "   ", icon_text_geo_10|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1301.0, 287.0), []),

	("markpoint_geo_himal", "   ", icon_text_geo_11|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-716.0, -43.0), [], 355.0),

	("markpoint_geo_pyre", "   ", icon_text_geo_12|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (222.0, -215.0), [], 350.0),

	("markpoint_geo_cauc", "   ", icon_text_geo_13|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-259.0, -217.0), []),

	("markpoint_geo_arades", "   ", icon_text_geo_14|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-294.0, 32.0), []),

	("markpoint_geo_vic", "   ", icon_text_geo_15|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-128.0, 252.0), []),

	("markpoint_geo_mada", "   ", icon_text_geo_16|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-278.0, 433.0), []),

	("markpoint_geo_amaz", "   ", icon_text_geo_17|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (888.0, 275.0), []),

	("markpoint_geo_baikal", "   ", icon_text_geo_18|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-943.0, -365.0), [], 40.0),

	("pirate_spawn_point_01", "Calico Jack John Rackham", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-413.0, 100.0), []),

	("pirate_spawn_point_02", "Conajee Angria", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-534.0, 95.0), []),

	("pirate_spawn_point_03", "Black Sam Samuel Bellamy", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (884.0, 79.0), []),

	("pirate_spawn_point_04", "Aziza Nurenahal", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-688.0, 105.0), []),

	("pirate_spawn_point_05", "Koxinga", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1133.0, 6.0), []),

	("pirate_spawn_point_06", "Shu Nian", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1116.0, -108.0), []),

	("pirate_spawn_point_07", "Ching Shih", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1025.0, 61.0), []),

	("pirate_spawn_point_08", "Murakami Yositada", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1172.0, -105.0), []),

	("pirate_spawn_point_09", "Murakami Takeyosi", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1204.0, -137.0), []),

	("pirate_spawn_point_10", "Alvilda", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (26.0, -421.0), []),

	("pirate_spawn_point_11", "Rollo", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (207.0, -446.0), []),

	("pirate_spawn_point_12", "Ragnar Lodbrok", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (201.0, -396.0), []),

	("pirate_spawn_point_13", "Francis Drake", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (314.0, -282.0), []),

	("pirate_spawn_point_14", "Joao Ferrero", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (527.0, -158.0), []),

	("pirate_spawn_point_15", "Catalina Errantzo", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (338.0, -120.0), []),

	("pirate_spawn_point_16", "Murat", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-99.0, -108.0), []),

	("pirate_spawn_point_17", "Uluj Ali", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (6.0, -119.0), []),

	("pirate_spawn_point_18", "Aruj Reis", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (86.0, -118.0), []),

	("pirate_spawn_point_19", "Hayreddin Reis", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (196.0, -159.0), []),

	("pirate_spawn_point_20", "Edward England", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-260.0, 352.0), []),

	("pirate_spawn_point_21", "Samuel Burgess", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (42.0, 619.0), []),

	("pirate_spawn_point_22", "Thomas White", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (192.0, 221.0), []),

	("pirate_spawn_point_23", "Edward Ned Low", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1057.0, -72.0), []),

	("pirate_spawn_point_24", "John Hawkins", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (438.0, -34.0), []),

	("pirate_spawn_point_25", "Jean Fleurie", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (840.0, 152.0), []),

	("pirate_spawn_point_26", "Howell Davis", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (475.0, 69.0), []),

	("pirate_spawn_point_27", "Edward Teach Blackbeard", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1001.0, 90.0), []),

	("pirate_spawn_point_28", "William Kidd", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (989.0, 18.0), []),

	("pirate_spawn_point_29", "Bartholomew Roberts", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1082.0, 75.0), []),

	("spawn_points_end", "{!}last spawn point", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("reserved_1", "{!}last spawn point", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("reserved_2", "{!}last spawn point", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("reserved_3", "{!}last spawn point", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("reserved_4", "{!}last spawn point", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("reserved_5", "{!}last spawn point", icon_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

]