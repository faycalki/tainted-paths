from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *

####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#  
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################

game_menus = [

	("start_game_0", menu_text_color(0xff000000), "Welcome to Tainted Paths.",
"none",
	[
		(set_background_mesh, "mesh_st_pic_sea")
	],
	[
		("selectscen",
		[],
		"Select Scenario",
		[
			(jump_to_menu, "mnu_start_select_age")
		], "."),

		("testtttttt",
		[
			(eq, "$test_mode", 1)
		],
		"Quick Start as a Male",
		[
			(assign, "$start_age", 1184),
			(call_script, "script_start_age_sett", "$start_age"),
			(assign, "$adult_content", 1),
			(troop_set_type, "trp_player", 0),
			(party_set_morale, "p_main_party", 100),
			(tutorial_message, -1),
			(tutorial_message_set_background, 0),
			(change_screen_map)
		], "."),

		("testtttttt_wo",
		[
			(eq, "$test_mode", 1)
		],
		"Quick Start as a Female",
		[
			(assign, "$start_age", 1184),
			(call_script, "script_start_age_sett", "$start_age"),
			(assign, "$adult_content", 1),
			(troop_set_type, "trp_player", 10),
			(party_set_morale, "p_main_party", 100),
			(tutorial_message, -1),
			(tutorial_message_set_background, 0),
			(change_screen_map)
		], "."),

		("go_back",
		[],
		"Go back",
		[
			(change_screen_quit)
		], ".")
	]
	),

	("start_phase_2", 0, "This is your story; In the distant past, a neighbouring nation declared war on your sovereign state. This war had seen casualties of the majority of your bloodline - except for your younger sister.^You yourself had enlisted to fight for your sister and your country, leaving her behind in your home village.",
"none",
	[
		(set_background_mesh, "mesh_pic_siege_sighted"),
		(set_show_messages, 0),
		(assign, "$wm_player_fac", "fac_player_supporters_faction"),
		(assign, "$wm_player_start_culture_fac", "$kingdom_pick_start_faction"),
		(faction_get_slot, ":wm_player_start_culture_fac_29", "$wm_player_start_culture_fac", 29),
		(call_script, "script_temp_save_number11_initialize"),
		(try_for_range, ":party", "p_pyongyang", "p_place_end"),
			(store_faction_of_party, ":faction_of_party_party", ":party"),
			(eq, ":faction_of_party_party", "$wm_player_start_culture_fac"),
			(neq, ":wm_player_start_culture_fac_29", ":party"),
			(call_script, "script_temp_save_number11_inject", ":party"),
		(try_end),
		(call_script, "script_temp_save_number11_choice_rand"),
		(assign, "$g_encountered_party", "$wm_target_number11"),
		(assign, "$current_town", "$wm_target_number11"),
		(assign, "$last_visit_town", "$wm_target_number11"),
		(call_script, "script_troop_type_sett", "trp_player"),
		(try_begin),
			(gt, "$troop_gender_type", 10),
			(call_script, "script_civil_outfit_set_women_no_agent", "$current_town", "trp_player"),
		(else_try),
			(call_script, "script_civil_outfit_set_man_no_agent", "$current_town", "trp_player"),
		(try_end),
		(troop_add_item, "trp_player", 1338),
		(troop_add_item, "trp_player", 1317),
		(troop_add_item, "trp_player", 1290),
		(troop_equip_items, "trp_player"),
		(party_set_morale, "p_main_party", 100),
		(party_get_position, 1, "$current_town"),
		(party_set_position, "p_main_party", 1),
		(call_script, "script_wm_troop_type_depend_train", "$current_town", 50),
		(assign, "$last_hired_troop_id", "$temp_party_troop_01"),
		(set_show_messages, 1)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(party_set_morale, "p_main_party", 100),
			(set_encountered_party, "$g_encountered_party"),
			(assign, "$g_encountered_party", "$current_town"),
			(call_script, "script_start_enemy_cult"),
			(faction_get_slot, "$enemy_commander", "$start_enemy_fac", 19),
			(call_script, "script_instance_battle_sett", "$start_enemy_fac", "$enemy_commander", "$current_town", 7000, 7000, 0)
		], "."),

		("testtttttt",
		[
			(eq, "$test_mode", 1)
		],
		"Quick Start man",
		[
			(assign, "$adult_content", 1),
			(troop_set_type, "trp_player", 0),
			(party_set_morale, "p_main_party", 100),
			(tutorial_message, -1),
			(tutorial_message_set_background, 0),
			(change_screen_map)
		], "."),

		("testtttttt_wo",
		[
			(eq, "$test_mode", 1)
		],
		"Quick Start woman",
		[
			(assign, "$adult_content", 1),
			(troop_set_type, "trp_player", 10),
			(party_set_morale, "p_main_party", 100),
			(tutorial_message, -1),
			(tutorial_message_set_background, 0),
			(change_screen_map)
		], ".")
	]
	),

	("start_game_3", 0, "Choose your scenario:",
"none",
	[],
	[
		("go_back",
		[],
		"Go back",
		[
			(change_screen_quit)
		], ".")
	]
	),

	("tutorial", 0, "You approach a field where the locals are training with weapons. ^You can practice here to improve your combat skills.",
"none",
	[
		(try_begin),
			(eq, "$g_tutorial_entered", 1),
			(change_screen_quit),
		(else_try),
			(set_passage_menu, "mnu_tutorial"),
			(assign, "$g_tutorial_entered", 1),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[], "."),

		("go_back_dot",
		[],
		"Go back.",
		[
			(change_screen_quit)
		], ".")
	]
	),

	("reports", 0, "        ",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger")
	],
	[
		("participate_meeting",
		[],
		"[Attend the Factional Meeting]",
		[
			(call_script, "script_attend_to_national_conference")
		], "."),

		("view_player_info",
		[],
		"-Player information-",
		[
			(assign, "$pst_target_no", "trp_player"),
			(jump_to_menu, "mnu_pst_lord_info")
		], "."),

		("adv_skill_pst",
		[],
		"-Adventure traits-",
		[
			(str_clear, 11),
			(str_store_string, 11, "str_help_right_click_pre"),
			(start_presentation, "prsnt_adv_exp_skill")
		], "."),

		("policy_skill_pst",
		[],
		"-Policy traits-",
		[
			(start_presentation, "prsnt_policy_learn")
		], "."),

		("view_achievements",
		[],
		"-Achievements-",
		[
			(start_presentation, "prsnt_pst_land_occupied")
		], "."),

		("view_ruin_list",
		[],
		"-List of discovered ruins-",
		[
			(str_clear, 41),
			(str_clear, 45),
			(str_store_string, 41, "str_lib_guess"),
			(str_store_string, 45, "str_lib_guess"),
			(assign, reg40, "p_ruin_1"),
			(assign, "$ruin_list_page_start", "p_ruin_1"),
			(start_presentation, "prsnt_pst_found_ruin_list")
		], "."),

		("view_pirate_occu",
		[
			(neq, "$start_age", 1184)
		],
		"-Sea occupancy level-",
		[
			(start_presentation, "prsnt_pst_pirate_occu")
		], "."),

		("view_sex_report",
		[
			(eq, "$adult_content", 1)
		],
		"-Sexual Statistics-",
		[
			(jump_to_menu, "mnu_sexual_report")
		], "."),


#hunger mod      
#("view_hungry_report",[],"Hunger Status (Hardcore Only)", #Default
("view_hungry_report",[(eq, "$hardcore_mode", 1)],"Limbs Status (Hardcore Mode)",
       [(jump_to_menu, "mnu_hungry_report"),
        ]
       ),
#
#####Hunger OSP End & Hardcore mod, Wounded OSP End
		
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("custom_battle_scene", menu_text_color(0xff000000), "(NO TRANS)",
"none",
	[],
	[
		("quick_battle_scene_1",
		[],
		"{!}quick battle scene 1",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_quick_battle_scene_1"),
			(change_screen_mission)
		], "."),

		("quick_battle_scene_2",
		[],
		"{!}quick battle scene 2",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_quick_battle_scene_2"),
			(change_screen_mission)
		], "."),

		("quick_battle_scene_3",
		[],
		"{!}quick battle scene 3",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_quick_battle_scene_3"),
			(change_screen_mission)
		], "."),

		("quick_battle_scene_4",
		[],
		"{!}quick battle scene 4",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_quick_battle_scene_4"),
			(change_screen_mission)
		], "."),

		("quick_battle_scene_5",
		[],
		"{!}quick battle scene 5",
		[
			(set_jump_mission, "mt_ai_training"),
			(jump_to_scene, "scn_quick_battle_scene_5"),
			(change_screen_mission)
		], "."),

		("go_back",
		[],
		"{!}Go back",
		[
			(change_screen_quit)
		], ".")
	]
	),

	("custom_battle_end", 0, "The battle is over. {s1} Your side killed {reg5} enemies and lost {reg6} troops over the battle. You personally slew {reg7} men in the fighting.",
"none",
	[],
	[
		("continue",
		[],
		"Continue.",
		[
			(change_screen_quit)
		], "."),

		("restart",
		[],
		"Restart.",
		[], ".")
	]
	),

	("start_game_1", menu_text_color(0xff000000), "Select your character's gender.",
"none",
	[],
	[
		("select_male",
		[],
		"Male",
		[
			(assign, ":var_1", "$kingdom_pick_start_faction"),
			(try_begin),
				(this_or_next|eq, ":var_1", "fac_kingdom_1"),
				(this_or_next|eq, ":var_1", "fac_kingdom_17"),
				(this_or_next|eq, ":var_1", "fac_kingdom_19"),
				(this_or_next|eq, ":var_1", "fac_kingdom_29"),
				(this_or_next|eq, ":var_1", "fac_kingdom_28"),
				(this_or_next|eq, ":var_1", "fac_kingdom_31"),
				(this_or_next|eq, ":var_1", "fac_kingdom_35"),
				(this_or_next|eq, ":var_1", "fac_kingdom_36"),
				(this_or_next|eq, ":var_1", "fac_kingdom_37"),
				(this_or_next|eq, ":var_1", "fac_kingdom_38"),
				(this_or_next|eq, ":var_1", "fac_kingdom_39"),
				(this_or_next|eq, ":var_1", "fac_kingdom_41"),
				(this_or_next|eq, ":var_1", "fac_kingdom_42"),
				(this_or_next|eq, ":var_1", "fac_kingdom_43"),
				(this_or_next|eq, ":var_1", "fac_kingdom_44"),
				(this_or_next|eq, ":var_1", "fac_kingdom_52"),
				(this_or_next|eq, ":var_1", "fac_kingdom_62"),
				(this_or_next|eq, ":var_1", "fac_china_people"),
				(this_or_next|eq, ":var_1", "fac_kingdom_21"),
				(this_or_next|eq, ":var_1", "fac_kingdom_22"),
				(this_or_next|eq, ":var_1", "fac_kingdom_30"),
				(this_or_next|eq, ":var_1", "fac_kingdom_32"),
				(this_or_next|eq, ":var_1", "fac_nomad_people"),
				(this_or_next|eq, ":var_1", "fac_kingdom_20"),
				(this_or_next|eq, ":var_1", "fac_kingdom_63"),
				(this_or_next|eq, ":var_1", "fac_kingdom_64"),
				(this_or_next|eq, ":var_1", "fac_kingdom_65"),
				(this_or_next|eq, ":var_1", "fac_kingdom_66"),
				(eq, ":var_1", "fac_kingdom_67"),
				(troop_set_type, "trp_player", 2),
				(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 1),
			(else_try),
				(this_or_next|eq, ":var_1", "fac_kingdom_45"),
				(this_or_next|eq, ":var_1", "fac_kingdom_46"),
				(this_or_next|eq, ":var_1", "fac_american_native"),
				(this_or_next|eq, ":var_1", "fac_kingdom_50"),
				(this_or_next|eq, ":var_1", "fac_kingdom_27"),
				(this_or_next|eq, ":var_1", "fac_kingdom_33"),
				(eq, ":var_1", "fac_indochina_people"),
				(troop_set_type, "trp_player", 8),
				(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 3),
			(else_try),
				(this_or_next|eq, ":var_1", "fac_kingdom_4"),
				(this_or_next|eq, ":var_1", "fac_hindu_people"),
				(this_or_next|eq, ":var_1", "fac_kingdom_13"),
				(this_or_next|eq, ":var_1", "fac_kingdom_14"),
				(this_or_next|eq, ":var_1", "fac_kingdom_40"),
				(this_or_next|eq, ":var_1", "fac_kingdom_49"),
				(this_or_next|eq, ":var_1", "fac_kingdom_56"),
				(this_or_next|eq, ":var_1", "fac_kingdom_57"),
				(eq, ":var_1", "fac_arabian_people"),
				(troop_set_type, "trp_player", 8),
				(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 3),
			(else_try),
				(this_or_next|eq, ":var_1", "fac_kingdom_34"),
				(eq, ":var_1", "fac_kingdom_51"),
				(troop_set_type, "trp_player", 6),
				(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 3),
			(else_try),
				(troop_set_type, "trp_player", 0),
				(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 1),
			(try_end),
			(faction_get_slot, ":kingdom_pick_start_faction_27", "$kingdom_pick_start_faction", 27),
			(troop_set_slot, "trp_player", 23, ":kingdom_pick_start_faction_27"),
			(jump_to_menu, "mnu_optional_1")
		], "."),

		("select_female",
		[],
		"Female",
		[
			(assign, ":var_1", "$kingdom_pick_start_faction"),
			(try_begin),
				(this_or_next|eq, ":var_1", "fac_kingdom_1"),
				(this_or_next|eq, ":var_1", "fac_kingdom_17"),
				(this_or_next|eq, ":var_1", "fac_kingdom_19"),
				(this_or_next|eq, ":var_1", "fac_kingdom_29"),
				(this_or_next|eq, ":var_1", "fac_kingdom_28"),
				(this_or_next|eq, ":var_1", "fac_kingdom_31"),
				(this_or_next|eq, ":var_1", "fac_kingdom_35"),
				(this_or_next|eq, ":var_1", "fac_kingdom_36"),
				(this_or_next|eq, ":var_1", "fac_kingdom_37"),
				(this_or_next|eq, ":var_1", "fac_kingdom_38"),
				(this_or_next|eq, ":var_1", "fac_kingdom_39"),
				(this_or_next|eq, ":var_1", "fac_kingdom_41"),
				(this_or_next|eq, ":var_1", "fac_kingdom_42"),
				(this_or_next|eq, ":var_1", "fac_kingdom_43"),
				(this_or_next|eq, ":var_1", "fac_kingdom_44"),
				(this_or_next|eq, ":var_1", "fac_kingdom_52"),
				(this_or_next|eq, ":var_1", "fac_kingdom_62"),
				(this_or_next|eq, ":var_1", "fac_china_people"),
				(this_or_next|eq, ":var_1", "fac_kingdom_21"),
				(this_or_next|eq, ":var_1", "fac_kingdom_22"),
				(this_or_next|eq, ":var_1", "fac_kingdom_30"),
				(this_or_next|eq, ":var_1", "fac_kingdom_32"),
				(this_or_next|eq, ":var_1", "fac_nomad_people"),
				(this_or_next|eq, ":var_1", "fac_kingdom_20"),
				(this_or_next|eq, ":var_1", "fac_kingdom_63"),
				(this_or_next|eq, ":var_1", "fac_kingdom_64"),
				(this_or_next|eq, ":var_1", "fac_kingdom_65"),
				(this_or_next|eq, ":var_1", "fac_kingdom_66"),
				(eq, ":var_1", "fac_kingdom_67"),
				(troop_set_type, "trp_player", 3),
				(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 2),
			(else_try),
				(this_or_next|eq, ":var_1", "fac_kingdom_45"),
				(this_or_next|eq, ":var_1", "fac_kingdom_46"),
				(this_or_next|eq, ":var_1", "fac_american_native"),
				(this_or_next|eq, ":var_1", "fac_kingdom_50"),
				(this_or_next|eq, ":var_1", "fac_kingdom_27"),
				(this_or_next|eq, ":var_1", "fac_kingdom_33"),
				(eq, ":var_1", "fac_indochina_people"),
				(troop_set_type, "trp_player", 15),
				(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 3),
			(else_try),
				(this_or_next|eq, ":var_1", "fac_kingdom_4"),
				(this_or_next|eq, ":var_1", "fac_hindu_people"),
				(this_or_next|eq, ":var_1", "fac_kingdom_13"),
				(this_or_next|eq, ":var_1", "fac_kingdom_14"),
				(this_or_next|eq, ":var_1", "fac_kingdom_40"),
				(this_or_next|eq, ":var_1", "fac_kingdom_49"),
				(this_or_next|eq, ":var_1", "fac_kingdom_56"),
				(this_or_next|eq, ":var_1", "fac_kingdom_57"),
				(eq, ":var_1", "fac_arabian_people"),
				(troop_set_type, "trp_player", 7),
				(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 6),
			(else_try),
				(this_or_next|eq, ":var_1", "fac_kingdom_34"),
				(eq, ":var_1", "fac_kingdom_51"),
				(troop_set_type, "trp_player", 13),
				(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 14),
			(else_try),
				(troop_set_type, "trp_player", 7),
				(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 6),
			(try_end),
			(faction_get_slot, ":kingdom_pick_start_faction_27", "$kingdom_pick_start_faction", 27),
			(troop_set_slot, "trp_player", 23, ":kingdom_pick_start_faction_27"),
			(jump_to_menu, "mnu_optional_1")
		], "."),

		("go_back",
		[],
		"Go back",
		[
			(change_screen_quit)
		], ".")
	]
	),

	#Decapitations checking
	("optional_1", menu_text_color(0xff000000), "Would you like to Enable or Disable decapitations?^Currently, decapitations work almost perfectly. However due to engine limitations they tend to cause red script error text about 10% of the time, which some people may find annoying, rightfully so.^ If you don't mind the script errors every once in a while that won't ever cause you any problems in your game, then I advice you to enable decapitations, otherwise keep them disabled.^^Note: Decapitations can be enabled or disabled at any time inside (Camp --> More mod options pages).",
"none",
	[],
	[
		("select_opt1on",
		[],
		"Enable decapitations",
		[
		(assign, "$dynamic_decap", 1), 
		(jump_to_menu, "mnu_choose_skill")
		], "."),

		("select_opt1off",
		[],
		"Disable decapitations",
		[
		(assign, "$dynamic_decap", 0), 
		(jump_to_menu, "mnu_choose_skill")
		], "."),

	]
	),
	#Decapitations checking
	
	
	("start_character_2", 0, "You spent your early life as...",
"none",
	[],
	[
		("go_back",
		[],
		"Go back.",
		[], ".")
	]
	),

	("start_character_3", 0, "You spent your early life as...",
"none",
	[],
	[
		("go_back",
		[],
		"Go back.",
		[], ".")
	]
	),

	("start_character_4", 0, "You spent your early life as...",
"none",
	[],
	[
		("go_back",
		[],
		"Go back.",
		[], ".")
	]
	),

	("choose_skill", 0, "   ",
"none",
	[
		(set_show_messages, 0),
		(try_begin),
			(troop_raise_attribute, "trp_player", 1, 1),
			(troop_raise_attribute, "trp_player", 0, 1),
			(troop_raise_attribute, "trp_player", 2, 1),
			(troop_raise_skill, "trp_player", "skl_riding", 1),
			(troop_raise_skill, "trp_player", "skl_weapon_master", 1),
			(troop_raise_skill, "trp_player", "skl_shield", 1),
			(troop_add_item, "trp_player", 105, 0),
			(troop_add_item, "trp_player", 105, 0),
		(try_end),
		(call_script, "script_troop_type_sett", "trp_player"),
		(try_begin),
			(lt, "$troop_gender_type", 10),
			(store_random_in_range, ":random_in_range_0_100", 0, 100),
			(try_begin),
				(ge, ":random_in_range_0_100", 97),
				(assign, ":value", 5),
			(else_try),
				(ge, ":random_in_range_0_100", 91),
				(assign, ":value", 4),
			(else_try),
				(ge, ":random_in_range_0_100", 75),
				(assign, ":value", 3),
			(else_try),
				(ge, ":random_in_range_0_100", 40),
				(assign, ":value", 2),
			(else_try),
				(assign, ":value", 1),
			(try_end),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, ":value"),
			(store_random_in_range, ":random_in_range_0_6", 0, 6),
			(troop_set_slot, "trp_player", slot_troop_player_order_object, ":random_in_range_0_6"),
		(else_try),
			(store_random_in_range, ":random_in_range_0_100", 0, 100),
			(try_begin),
				(ge, ":random_in_range_0_100", 93),
				(assign, ":value", 16),
			(else_try),
				(ge, ":random_in_range_0_100", 84),
				(assign, ":value", 15),
			(else_try),
				(ge, ":random_in_range_0_100", 74),
				(assign, ":value", 14),
			(else_try),
				(ge, ":random_in_range_0_100", 59),
				(assign, ":value", 13),
			(else_try),
				(ge, ":random_in_range_0_100", 52),
				(assign, ":value", 12),
			(else_try),
				(ge, ":random_in_range_0_100", 45),
				(assign, ":value", 11),
			(else_try),
				(ge, ":random_in_range_0_100", 36),
				(assign, ":value", 10),
			(else_try),
				(ge, ":random_in_range_0_100", 30),
				(assign, ":value", 9),
			(else_try),
				(ge, ":random_in_range_0_100", 25),
				(assign, ":value", 8),
			(else_try),
				(ge, ":random_in_range_0_100", 20),
				(assign, ":value", 6),
			(else_try),
				(ge, ":random_in_range_0_100", 15),
				(assign, ":value", 5),
			(else_try),
				(ge, ":random_in_range_0_100", 10),
				(assign, ":value", 4),
			(else_try),
				(ge, ":random_in_range_0_100", 3),
				(assign, ":value", 3),
			(else_try),
				(assign, ":value", 1),
			(try_end),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, ":value"),
			(store_random_in_range, ":random_in_range_0_6", 0, 6),
			(troop_set_slot, "trp_player", slot_troop_player_order_object, ":random_in_range_0_6"),
		(try_end),
		(try_begin),
			(jump_to_menu, "mnu_auto_return"),
			(start_presentation, "prsnt_banner_selection"),
		(try_end),
		(set_show_messages, 1),

	],
	[]
	),

	("past_life_explanation", 0, "---",
"none",
	[],
	[
		("go_back_dot",
		[],
		"Go back.",
		[], ".")
	]
	),

	("auto_return", 0, "{!}This menu automatically returns to caller.",
"none",
	[
		(change_screen_return, 0)
	],
	[]
	),

	("morale_report", 0, "---",
"none",
	[],
	[
		("go_back_dot",
		[],
		"Go back.",
		[], ".")
	]
	),

	("courtship_relations", 0, "---",
"none",
	[],
	[
		("go_back_dot",
		[],
		"Go back.",
		[], ".")
	]
	),

	("lord_relations", 0, "---",
"none",
	[],
	[
		("go_back_dot",
		[],
		"Go back.",
		[], ".")
	]
	),

	("companion_report", 0, "---",
"none",
	[],
	[
		("go_back_dot",
		[],
		"Go back.",
		[], ".")
	]
	),

	("faction_orders", 0, "---",
"none",
	[],
	[
		("go_back_dot",
		[],
		"Go back.",
		[], ".")
	]
	),

	("character_report", 0, "---",
"none",
	[],
	[
		("go_back_dot",
		[],
		"Go back.",
		[], ".")
	]
	),

	("party_size_report", 0, "---",
"none",
	[],
	[
		("go_back_dot",
		[],
		"Go back.",
		[], ".")
	]
	),

	("faction_relations_report", 0, "---",
"none",
	[],
	[
		("go_back_dot",
		[],
		"Go back.",
		[], ".")
	]
	),

	("camp", 0, "You set up camp. What do you want to do?",
"none",
	[
		(set_background_mesh, "mesh_pic_messenger"),
		(call_script, "script_troop_equip_items_fix"),
		(try_begin),
			(eq, "$manage_troop_pst_restart", 1),
			(assign, "$manage_troop_pst_restart", 0),
			(start_presentation, "prsnt_manage_troops"),
		(try_end)
	],
	[
		("rest_test",
		[
			(eq, "$test_mode", 1)
		],
		"[Rest test]",
		[
			(rest_for_hours_interactive, 26280, 15, 0),
			(change_screen_return)
		], "."),

		("psttttt",
		[
			(eq, "$test_mode", 1)
		],
		"test butt",
		[], "."),

		("testttttttt",
		[
			(eq, "$test_mode", 1)
		],
		"troopadd",
		[
			(party_add_members, "p_main_party", "trp_ww_m_1", 7),
			(party_add_members, "p_main_party", "trp_ww_m_2", 13),
			(party_add_members, "p_main_party", "trp_ww_a_3", 13),
			(party_add_members, "p_main_party", "trp_ww_c_5", 15),
			(party_add_members, "p_main_party", "trp_ww_c_6_2", 7),
			(party_add_members, "p_main_party", "trp_ww_m_6", 16),
			(party_add_members, "p_main_party", "trp_ww_m_5", 4),
			(party_add_members, "p_main_party", "trp_ww_a_5", 5)
		], "."),

		("manage_troops",
		[],
		">Manage Troops<",
		[
			(assign, "$manage_troop_selected", 0),
			(start_presentation, "prsnt_manage_troops")
		], "."),

		("mq_tip_butt",
		[
			(gt, "$main_q_step", 0)
		],
		"[Main Quest Tip]",
		[
			(try_begin),
				(eq, "$main_q_step", 1),
				(display_message, "str_mq_1_1b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$current_town"),
			(else_try),
				(eq, "$main_q_step", 2),
				(is_between, "$main_q_party", "p_pyongyang", "p_place_end"),
				(neq, "$rt_marked_target", "$main_q_party"),
				(str_store_party_name, 12, "$main_q_party"),
				(display_message, "str_mq_1_2b1", 0x00ffff00),
				(display_message, "str_mq_1_2b2", 0x00ffff00),
				(display_message, "str_mq_1_2b3", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 2),
				(display_message, "str_mq_1_2bb", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 3),
				(assign, reg8, "$main_q_day"),
				(display_message, "str_mq_1_3b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 4),
				(str_store_faction_name, 12, "$main_q_faction"),
				(display_message, "str_mq_1_4b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 5),
				(str_store_party_name, 12, "$main_q_party"),
				(display_message, "str_mq_1_5b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 6),
				(str_store_party_name, 12, "$main_q_party"),
				(display_message, "str_mq_1_6b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 7),
				(is_between, "$main_q_party", "p_pyongyang", "p_place_end"),
				(str_store_party_name, 12, "$main_q_party"),
				(display_message, "str_mq_1_7b1", 0x00ffff00),
				(display_message, "str_mq_1_7b2", 0x00ffff00),
				(display_message, "str_mq_1_7b3", 0x00ffff00),
				(display_message, "str_mq_1_7b4", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 8),
				(str_store_party_name, 12, "$main_q_party"),
				(display_message, "str_mq_1_8b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 9),
				(str_store_party_name, 10, "$main_q_party"),
				(display_message, "str_mq_1_9b", 0x00ffff00),
				(display_message, "str_mq_1_9_1", 0x00ffff00),
				(display_message, "str_mq_1_9_2", 0x00ffff00),
				(display_message, "str_mq_1_9_3", 0x00ffff00),
				(display_message, "str_mq_1_9_4", 0x00ffff00),
				(display_message, "str_mq_1_9_5", 0x00ffff00),
				(display_message, "str_mq_1_9_6", 0x00ffff00),
				(display_message, "str_mq_1_9_7", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 10),
				(str_store_party_name, 10, "$main_q_party"),
				(display_message, "str_mq_1_10b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 11),
				(display_message, "str_mq_1_11b", 0x00ffff00),
				(display_message, "str_mq_1_11b1", 0x00ffff00),
				(display_message, "str_mq_1_11b2", 0x00ffff00),
				(display_message, "str_mq_1_11b3", 0x00ffff00),
				(display_message, "str_mq_1_11b4", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 12),
				(str_store_party_name, 10, "$main_q_party"),
				(display_message, "str_mq_1_12b", 0x00ffff00),
			(else_try),
				(this_or_next|eq, "$main_q_step", 13),
				(eq, "$main_q_step", 14),
				(display_message, "str_mq_1_13b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_qazvin"),
			(else_try),
				(eq, "$main_q_step", 15),
				(str_store_party_name, 10, "$main_q_party"),
				(display_message, "str_mq_1_15b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 16),
				(str_store_party_name, 10, "$main_q_party"),
				(display_message, "str_mq_1_16b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(this_or_next|eq, "$main_q_step", 17),
				(this_or_next|eq, "$main_q_step", 18),
				(eq, "$main_q_step", 19),
				(call_script, "script_main_quest_cla_req", 1),
				(display_message, "str_mq_s9", 0x00ffff00),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 20),
				(str_store_troop_name, 14, "$first_comp_id"),
				(str_store_party_name, 10, "$main_q_party"),
				(display_message, "str_mq_1_20b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 25),
				(call_script, "script_main_quest_cla_req", 2),
				(display_message, "str_mq_s9", 0x00ffff00),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 26),
				(display_message, "str_mq_1_26b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 28),
				(call_script, "script_main_quest_cla_req", 3),
				(display_message, "str_mq_s9", 0x00ffff00),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 29),
				(display_message, "str_mq_1_29b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 30),
				(str_store_troop_name, 14, "trp_npc_18"),
				(str_store_party_name, 10, "$main_q_party"),
				(display_message, "str_mq_1_30b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 31),
				(str_store_party_name, 10, "$main_q_party"),
				(display_message, "str_mq_1_31b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 33),
				(call_script, "script_main_quest_cla_req", 4),
				(display_message, "str_mq_s9", 0x00ffff00),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(this_or_next|eq, "$main_q_step", 37),
				(eq, "$main_q_step", 38),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 42),
				(call_script, "script_main_quest_cla_req", 5),
				(display_message, "str_mq_s9", 0x00ffff00),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 43),
				(display_message, "str_mq_1_43b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_ruin_dummy_3"),
			(else_try),
				(eq, "$main_q_step", 45),
				(call_script, "script_main_quest_cla_req", 6),
				(display_message, "str_mq_s9", 0x00ffff00),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 46),
				(display_message, "str_mq_1_46m", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_ruin_dummy_5"),
			(else_try),
				(eq, "$main_q_step", 47),
				(str_store_troop_name, 14, "$main_q_troop"),
				(display_message, "str_mq_1_47b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_ruin_dummy_5"),
			(else_try),
				(eq, "$main_q_step", 49),
				(call_script, "script_main_quest_cla_req", 7),
				(display_message, "str_mq_s9", 0x00ffff00),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 50),
				(display_message, "str_mq_1_43b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_ruin_dummy_3"),
			(else_try),
				(eq, "$main_q_step", 51),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 52),
				(display_message, "str_mq_1_52b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 53),
				(display_message, "str_mq_1_53b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_tola"),
			(else_try),
				(eq, "$main_q_step", 56),
				(call_script, "script_main_quest_cla_req", 8),
				(display_message, "str_mq_s9", 0x00ffff00),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 57),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 58),
				(str_store_party_name, 10, "$main_q_party"),
				(display_message, "str_mq_1_58b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 61),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 62),
				(display_message, "str_mq_1_62b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 63),
				(display_message, "str_mq_1_63b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_tradeport97"),
			(else_try),
				(eq, "$main_q_step", 64),
				(display_message, "str_mq_1_64b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_tradeport97"),
			(else_try),
				(eq, "$main_q_step", 66),
				(call_script, "script_main_quest_cla_req", 9),
				(display_message, "str_mq_s9", 0x00ffff00),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(this_or_next|eq, "$main_q_step", 67),
				(eq, "$main_q_step", 68),
				(display_message, "str_mq_1_67b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_tradeport71"),
			(else_try),
				(eq, "$main_q_step", 69),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 70),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 71),
				(call_script, "script_main_quest_cla_req", 10),
				(display_message, "str_mq_s9", 0x00ffff00),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 72),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 73),
				(display_message, "str_mq_1_73b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_ruin_dummy_3"),
			(else_try),
				(eq, "$main_q_step", 75),
				(display_message, "str_mq_1_75b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 76),
				(call_script, "script_main_quest_cla_req", 11),
				(display_message, "str_mq_s9", 0x00ffff00),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 77),
				(display_message, "str_mq_1_77b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 78),
				(display_message, "str_mq_1_78b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 79),
				(display_message, "str_mq_1_79b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_ruin_dummy_4"),
			(else_try),
				(eq, "$main_q_step", 81),
				(call_script, "script_main_quest_cla_req", 12),
				(display_message, "str_mq_s9", 0x00ffff00),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 82),
				(display_message, "str_mq_1_82b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 83),
				(display_message, "str_mq_1_83b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_cyprus"),
			(else_try),
				(eq, "$main_q_step", 84),
				(display_message, "str_mq_1_84b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_genoa"),
			(else_try),
				(eq, "$main_q_step", 86),
				(display_message, "str_mq_1_86b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_ruin_dummy_3"),
			(else_try),
				(eq, "$main_q_step", 87),
				(display_message, "str_mq_1_87b", 0x00ffff00),
			(else_try),
				(this_or_next|eq, "$main_q_step", 88),
				(eq, "$main_q_step", 89),
				(display_message, "str_mq_1_88b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_ruin_dummy_4"),
			(else_try),
				(eq, "$main_q_step", 93),
				(call_script, "script_main_quest_cla_req", 13),
				(display_message, "str_mq_s9", 0x00ffff00),
				(display_message, "str_mq_s9b", 0x00ffff00),
			(else_try),
				(eq, "$main_q_step", 94),
				(display_message, "str_mq_1_94b", 0x00ffff00),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_antioch"),
			(else_try),
				(eq, "$main_q_step", 98),
				(display_message, "str_mq_update_later", 0x00ffff00),
			(try_end)
		], "."),

		("hire_villain",
		[
			(eq, "$r_player_class", 4),
			(call_script, "script_party_money_level_ge", "p_main_party", 400),
			(eq, "$wm_mo_continue", 1),
			(party_get_slot, ":last_visit_town_town_claimed_by_player", "$last_visit_town", slot_town_claimed_by_player),
			(try_begin),
				(this_or_next|eq, ":last_visit_town_town_claimed_by_player", 13),
				(this_or_next|eq, ":last_visit_town_town_claimed_by_player", 12),
				(this_or_next|eq, ":last_visit_town_town_claimed_by_player", 11),
				(eq, ":last_visit_town_town_claimed_by_player", 10),
				(assign, ":value", "trp_jj_a_5_2"),
			(else_try),
				(assign, ":value", "trp_ww_a_5_2"),
			(try_end),
			(str_store_troop_name, 8, ":value")
		],
		"Hire: {s8}",
		[
			(party_get_slot, ":last_visit_town_town_claimed_by_player", "$last_visit_town", slot_town_claimed_by_player),
			(try_begin),
				(this_or_next|eq, ":last_visit_town_town_claimed_by_player", 13),
				(this_or_next|eq, ":last_visit_town_town_claimed_by_player", 12),
				(this_or_next|eq, ":last_visit_town_town_claimed_by_player", 11),
				(eq, ":last_visit_town_town_claimed_by_player", 10),
				(assign, ":value", "trp_jj_a_5_2"),
			(else_try),
				(assign, ":value", "trp_ww_a_5_2"),
			(try_end),
			(call_script, "script_new_troop_add_sc", ":value", 1),
			(call_script, "script_party_money_level_diff", "p_main_party", 400, 34)
		], "."),

		("Conversation_companion",
		[],
		"Talk with companion",
		[
			(assign, "$wm_talk_state", 1),
			(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
			(try_begin),
				(try_begin),
					(this_or_next|eq, ":current_terrain_main_party", 7),
					(eq, ":current_terrain_main_party", 2),
					(assign, ":value", "scn_conv_camp_sea"),
				(else_try),
					(eq, ":current_terrain_main_party", 5),
					(assign, ":value", "scn_conv_camp_desert"),
				(else_try),
					(eq, ":current_terrain_main_party", 4),
					(assign, ":value", "scn_conv_camp_snow"),
				(else_try),
					(assign, ":value", "scn_conv_camp"),
				(try_end),
			(try_end),
			(modify_visitors_at_site, ":value"),
			(reset_visitors),
			(set_visitor, 10, "trp_player"),
			(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(troop_slot_eq, "trp_player", slot_troop_state, ":troop"),
				(troop_slot_eq, ":troop", slot_troop_state, "trp_player"),
				(set_visitor, 38, ":troop"),
			(try_end),
			(assign, ":value_2", 11),
			(assign, ":value_3", "$orphan_girl_troop_id"),
			(try_begin),
				(gt, ":value_3", 0),
				(call_script, "script_wm_main_party_has_troop_sc", ":value_3"),
				(neq, "$wm_comp_continue", 1),
				(neg|troop_slot_eq, "trp_player", slot_troop_state, ":value_3"),
				(set_visitor, ":value_2", ":value_3"),
				(val_add, ":value_2", 1),
			(try_end),
			(assign, ":value_3", "$wm_comp_id_1"),
			(try_begin),
				(gt, ":value_3", 0),
				(neq, "$g_sex_officer", ":value_3"),
				(neg|troop_slot_eq, "trp_player", slot_troop_state, ":value_3"),
				(set_visitor, ":value_2", ":value_3"),
				(val_add, ":value_2", 1),
			(try_end),
			(assign, ":value_3", "$wm_comp_id_2"),
			(try_begin),
				(gt, ":value_3", 0),
				(neq, "$g_sex_officer", ":value_3"),
				(neg|troop_slot_eq, "trp_player", slot_troop_state, ":value_3"),
				(set_visitor, ":value_2", ":value_3"),
				(val_add, ":value_2", 1),
			(try_end),
			(assign, ":value_3", "$wm_comp_id_3"),
			(try_begin),
				(gt, ":value_3", 0),
				(neq, "$g_sex_officer", ":value_3"),
				(neg|troop_slot_eq, "trp_player", slot_troop_state, ":value_3"),
				(set_visitor, ":value_2", ":value_3"),
				(val_add, ":value_2", 1),
			(try_end),
			(assign, ":value_3", "$wm_comp_id_4"),
			(try_begin),
				(gt, ":value_3", 0),
				(neq, "$g_sex_officer", ":value_3"),
				(neg|troop_slot_eq, "trp_player", slot_troop_state, ":value_3"),
				(set_visitor, ":value_2", ":value_3"),
				(val_add, ":value_2", 1),
			(try_end),
			(assign, ":value_3", "$wm_comp_id_5"),
			(try_begin),
				(gt, ":value_3", 0),
				(neq, "$g_sex_officer", ":value_3"),
				(neg|troop_slot_eq, "trp_player", slot_troop_state, ":value_3"),
				(set_visitor, ":value_2", ":value_3"),
				(val_add, ":value_2", 1),
			(try_end),
			(assign, ":value_3", "$wm_comp_id_standby"),
			(try_begin),
				(gt, ":value_3", 0),
				(neq, "$g_sex_officer", ":value_3"),
				(neg|troop_slot_eq, "trp_player", slot_troop_state, ":value_3"),
				(set_visitor, ":value_2", ":value_3"),
				(val_add, ":value_2", 1),
			(try_end),
			(try_begin),
				(neq, ":value", "scn_conv_camp_sea"),
				(assign, ":value_2", 51),
				(try_for_range, ":value_3", "trp_tt_lord_01_00", "trp_tt_lord_end"),
					(le, ":value_2", 53),
					(troop_slot_eq, ":value_3", slot_troop_cur_center, 2),
					(set_visitor, ":value_2", ":value_3"),
					(val_add, ":value_2", 1),
				(try_end),
			(try_end),
			(call_script, "script_wm_main_party_has_troop_sc", "$g_sex_officer"),
			(try_begin),
				(neq, ":value", "scn_conv_camp_sea"),
				(eq, "$wm_comp_continue", 1),
				(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
				(assign, ":var_7", 0),
				(assign, ":value_4", 0),
				(try_for_range, ":localvariable", 0, ":num_companion_stacks_main_party"),
					(party_stack_get_troop_id, ":party_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
					(gt, ":party_stack_troop_id_main_party_localvariable", "trp_army_size_troop"),
					(neg|troop_is_hero, ":party_stack_troop_id_main_party_localvariable"),
					(party_stack_get_size, ":party_stack_size_main_party_localvariable", "p_main_party", ":localvariable"),
					(try_begin),
						(gt, ":party_stack_size_main_party_localvariable", 0),
						(val_add, ":var_7", ":party_stack_size_main_party_localvariable"),
						(assign, ":value_4", ":party_stack_troop_id_main_party_localvariable"),
					(try_end),
				(try_end),
				(try_begin),
					(ge, ":var_7", 5),
					(is_between, ":value_4", "trp_farmer", "trp_town_walker_1"),
					(set_visitor, 80, "$g_sex_officer"),
					(set_visitor, 81, ":value_4"),
					(set_visitor, 82, ":value_4"),
					(set_visitor, 83, ":value_4"),
					(set_visitor, 84, ":value_4"),
					(set_visitor, 85, ":value_4"),
				(try_end),
			(try_end),
			(set_jump_mission, "mt_camp_mission"),
			(assign, "$current_mission_template", "mt_camp_mission"),
			(set_jump_entry, 10),
			(jump_to_scene, ":value"),
			(change_screen_mission)
		], "."),

		("troop_clearr",
		[],
		"[Disband army]",
		[
			(jump_to_menu, "mnu_wm_troop_clear")
		], "."),


		
		("mod_option",
		[],
		"Mod options",
		[
			(start_presentation, "prsnt_mod_option")
		], "."),
		
		("camp_more_mod_options",
		[
		],
		"More mod options",
		[
			(start_presentation, "prsnt_mod_options_pt2")
		], "."),
		
		

		
				("camp_notes_and_hotkeys",
		[
		],
		"Notes & Hotkeys how to play!",
		[
			(jump_to_menu, "mnu_notes_and_hotkeys_full"),
			(play_sound, "snd_summary_finance"),
		], "."),
		
		("camp_cheat",
		[
		],
		"Cheats menu",
		[
			(jump_to_menu, "mnu_cheats_picker")
		], "."),


		
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("start_phase_x1", 0, "     ",
"none",
	[],
	[
		("go_back",
		[],
		"Go back",
		[
			(change_screen_quit)
		], ".")
	]
	),

	("start_phase_x3", 0, "The great war has finally ended. However, the dead do not come back to life.^You return home to smoldering ruins.^The village has been razed and looted, with no trace of your sister.^Who knows where she might have gone? It is you against the world.^^Time passes. You take a look around.",
"none",
	[
		(set_background_mesh, "mesh_pic_defeat"),
		(call_script, "script_sister_assign_depand_fac"),
		(try_begin),
			(set_fixed_point_multiplier, 1000),
			(position_set_x, 0, 600),
			(position_set_y, 0, 400),
			(position_set_z, 0, 750),
			(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$younger_sister_id", 0),
		(try_end)
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(call_script, "script_party_common_member_clear", "p_main_party"),
			(call_script, "script_party_common_member_clear", "p_main_party"),
			(call_script, "script_party_common_member_clear", "p_main_party"),
			(call_script, "script_party_common_member_clear", "p_main_party"),
			(call_script, "script_party_army_size_execute", "p_main_party", 0, 5),
			(jump_to_menu, "mnu_start_phase_x4")
		], ".")
	]
	),

	("start_phase_x4", 0, "     ",
"none",
	[
		(assign, "$r_player_class", 3),
		(start_presentation, "prsnt_molda_start_class")
	],
	[]
	),

	("start_phase_x5", 0, "{s14}",
"none",
	[
		(set_background_mesh, "mesh_pic_recruits"),
		(try_begin),
			(eq, "$r_player_class", 1),
			(store_mul, ":value", 1000, 40),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
			(troop_set_slot, "trp_player", slot_troop_love_interest_1, 3),
			(troop_set_slot, "trp_player", slot_troop_love_interest_2, 3),
			(troop_set_slot, "trp_player", slot_troop_betrothal_time, 4),
			(troop_set_slot, "trp_player", 41, 4),
			(troop_set_slot, "trp_player", slot_lady_used_tournament, 1),
			(try_for_range, ":troop", "trp_elite_troops_01", "trp_elite_troops_end"),
				(call_script, "script_outfit_weapon_set_no_agent", "$current_town", ":troop"),
				(call_script, "script_bandit_outfit_setting_no_agent", "$current_town", ":troop"),
				(troop_set_name, ":troop", "str_caravan_guard"),
				(troop_set_slot, ":troop", slot_troop_love_interest_1, 1),
			(try_end),
			(call_script, "script_wm_troop_type_depend_train", "$current_town", 100),
			(party_add_members, "p_main_party", "$temp_party_troop_02", 20),
			(str_store_string, 14, "str_be_merchant"),
		(else_try),
			(eq, "$r_player_class", 2),
			(troop_set_slot, "trp_player", slot_troop_love_interest_3, 4),
			(troop_set_slot, "trp_player", slot_troop_love_interest_1, 4),
			(troop_set_slot, "trp_player", slot_troop_love_interest_2, 4),
			(troop_set_slot, "trp_player", 41, 2),
			(troop_set_slot, "trp_player", slot_troop_father, 3),
			(store_mul, ":value", 1000, 5),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
			(try_for_range, ":troop", "trp_elite_troops_01", "trp_elite_troops_end"),
				(call_script, "script_outfit_weapon_set_no_agent", "$current_town", ":troop"),
				(call_script, "script_bandit_outfit_setting_no_agent", "$current_town", ":troop"),
				(troop_set_name, ":troop", "str_cla_name_2"),
				(troop_set_slot, ":troop", slot_troop_love_interest_1, 1),
			(try_end),
			(store_random_in_range, ":random_in_range_1081_1252", 1081, 1252),
			(troop_add_item, "trp_player", ":random_in_range_1081_1252"),
			(store_random_in_range, ":random_in_range_1081_1252", 1081, 1252),
			(troop_add_item, "trp_player", ":random_in_range_1081_1252"),
			(store_random_in_range, ":random_in_range_1081_1252", 1081, 1252),
			(troop_add_item, "trp_player", ":random_in_range_1081_1252"),
			(call_script, "script_wm_honor_change_diff", "trp_player", 15, 87),
			(str_store_string, 14, "str_be_adventurer"),
		(else_try),
			(eq, "$r_player_class", 0),
			(call_script, "script_battle_exp_diff", 1000, 87),
			(troop_set_slot, "trp_player", slot_troop_love_interests_end, 5),
			(troop_set_slot, "trp_player", slot_troop_spawned_before, 3),
			(troop_set_slot, "trp_player", slot_troop_last_comment_slot, 3),
			(troop_set_slot, "trp_player", slot_troop_spouse, 1),
			(store_mul, ":value", 1000, 5),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
			(try_for_range, ":troop", "trp_elite_troops_01", "trp_elite_troops_end"),
				(call_script, "script_outfit_weapon_set_no_agent", "$current_town", ":troop"),
				(call_script, "script_bandit_outfit_setting_no_agent", "$current_town", ":troop"),
				(troop_set_name, ":troop", "str_cla_name_0"),
				(troop_set_slot, ":troop", slot_troop_love_interest_1, 1),
			(try_end),
			(call_script, "script_wm_troop_type_depend_train", "$current_town", 100),
			(party_add_members, "p_main_party", "$temp_party_troop_07", 40),
			(party_add_members, "p_main_party", "$temp_party_troop_03", 30),
			(str_store_string, 14, "str_volunteered_for_rev"),
		(else_try),
			(eq, "$r_player_class", 3),
			(call_script, "script_ply_wayfarer_join_faction", "$kingdom_pick_start_faction"),
			(troop_set_slot, "trp_player", slot_troop_betrothal_time, 3),
			(troop_set_slot, "trp_player", slot_troop_love_interests_end, 5),
			(troop_set_slot, "trp_player", slot_troop_spawned_before, 3),
			(troop_set_slot, "trp_player", slot_troop_last_comment_slot, 3),
			(troop_set_slot, "trp_player", slot_troop_spouse, 1),
			(store_mul, ":value", 1000, 10),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
			(try_begin),
				(faction_get_slot, ":wm_player_fac_29", "$wm_player_fac", 29),
				(neq, "$current_town", ":wm_player_fac_29"),
				(party_set_slot, "$current_town", slot_town_tavern, "trp_player"),
				(call_script, "script_party_extra_text_for_town", "$current_town"),
				(store_mul, ":value", 1000, 5), #1000 default party size max
				(call_script, "script_party_army_size_execute", "p_main_party", ":value", 5),
				(party_set_slot, "p_main_party", slot_town_elder, 70), #70
				(party_set_slot, "p_main_party", slot_center_player_relation, 70), #70
			(try_end),
			(try_for_range, ":troop", "trp_elite_troops_01", "trp_elite_troops_end"),
				(call_script, "script_outfit_weapon_set_no_agent", "$current_town", ":troop"),
				(call_script, "script_bandit_outfit_setting_no_agent", "$current_town", ":troop"),
				(troop_set_name, ":troop", "str_elite_guard"),
				(troop_set_slot, ":troop", slot_troop_love_interest_1, 1),
			(try_end),
			(call_script, "script_wm_troop_type_depend_train", "$current_town", 100),
			(party_add_members, "p_main_party", "$temp_party_troop_01", 20),
			(party_add_members, "p_main_party", "$temp_party_troop_03", 20),
			(party_add_members, "p_main_party", "$temp_party_troop_04", 20),
			(party_add_members, "p_main_party", "$temp_party_troop_06", 20),
			(call_script, "script_wm_honor_change_diff", "trp_player", 15, 87),
			(str_store_string, 14, "str_inherited_for_rev"),
		(else_try),
			(eq, "$r_player_class", 4),
			(store_mul, ":value", 1000, 15),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
			(troop_set_slot, "trp_player", slot_troop_love_interests_end, 3),
			(troop_set_slot, "trp_player", slot_troop_betrothal_time, 2),
			(troop_set_slot, "trp_player", 41, 2),
			(troop_set_slot, "trp_player", slot_troop_love_interest_1, 1),
			(troop_set_slot, "trp_player", slot_troop_spouse, 1),
			(try_for_range, ":troop", "trp_elite_troops_01", "trp_elite_troops_end"),
				(call_script, "script_outfit_weapon_set_no_agent", "$current_town", ":troop"),
				(call_script, "script_bandit_outfit_setting_no_agent", "$current_town", ":troop"),
				(troop_set_name, ":troop", "str_fighterr"),
				(troop_set_slot, ":troop", slot_troop_love_interest_1, 1),
			(try_end),
			(party_get_slot, ":current_town_town_claimed_by_player", "$current_town", slot_town_claimed_by_player),
			(try_begin),
				(this_or_next|eq, ":current_town_town_claimed_by_player", 13),
				(this_or_next|eq, ":current_town_town_claimed_by_player", 12),
				(this_or_next|eq, ":current_town_town_claimed_by_player", 11),
				(eq, ":current_town_town_claimed_by_player", 10),
				(assign, ":value_2", "trp_jj_a_5_2"),
			(else_try),
				(assign, ":value_2", "trp_ww_a_5_2"),
			(try_end),
			(party_add_members, "p_main_party", ":value_2", 40),
			(call_script, "script_wm_honor_change_diff", "trp_player", 15, 34),
			(str_store_string, 14, "str_be_villain"),
		(else_try),
			(eq, "$r_player_class", 5),
			(store_mul, ":value", 1000, 15),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
			(troop_set_slot, "trp_player", slot_troop_love_interest_2, 4),
			(troop_set_slot, "trp_player", slot_troop_love_interests_end, 3),
			(troop_set_slot, "trp_player", 41, 3),
			(troop_set_slot, "trp_player", slot_troop_last_comment_slot, 4),
			(troop_set_slot, "trp_player", slot_troop_father, 7),
			(try_for_range, ":troop", "trp_elite_troops_01", "trp_elite_troops_end"),
				(call_script, "script_outfit_weapon_set_no_agent", "$current_town", ":troop"),
				(call_script, "script_bandit_outfit_setting_no_agent", "$current_town", ":troop"),
				(troop_set_name, ":troop", "str_cla_name_5"),
				(troop_set_slot, ":troop", slot_troop_love_interest_1, 1),
			(try_end),
			(party_get_slot, ":current_town_town_claimed_by_player", "$current_town", slot_town_claimed_by_player),
			(call_script, "script_pirate_troop_and_ship_type", ":current_town_town_claimed_by_player"),
			(party_add_members, "p_main_party", "$temp_num_01", 40),
			(call_script, "script_for_culture_sett_find_source_party"),
			(call_script, "script_molda_ship_culture_sett", "$wm_target_number11"),
			(assign, ":value_3", reg23),
			(val_sub, ":value_3", "trp_ship_00"),
			(store_add, "$m_ship_type_1", 1400, ":value_3"),
			(call_script, "script_molda_ship_culture_sett", "$wm_target_number11"),
			(assign, ":value_3", reg23),
			(val_sub, ":value_3", "trp_ship_00"),
			(store_add, "$m_ship_type_2", 1400, ":value_3"),
			(call_script, "script_wm_honor_change_diff", "trp_player", 15, 34),
			(str_store_string, 14, "str_be_pirate"),
		(try_end),
		

	],
	[
	
	#start as king
#Hide this unless starting as lord
			("aftertwoyearswithskip",
		[

				(eq, "$r_player_class", 3),
		(eq, "$player_noble", 1),
		],
		"Start as a monarch or doge.",
		[
		(assign, "$started_as_monarch", 2), #Skip coup
		(assign, "$monarch_fix", 1), #Prevent lords from leaving after coup
			(tutorial_message, -1),
			(tutorial_message_set_background, 0),
			(party_set_slot, "p_main_party", slot_town_elder, 50),
			(party_set_slot, "p_main_party", slot_center_player_relation, 50),
			(troop_set_slot, "trp_player", slot_troop_cur_center, 0),
			(try_begin),
				(eq, "$r_player_class", 5),
				(party_set_slot, "p_main_party", slot_center_last_visited_by_lord, 1000),
			(else_try),
				(eq, "$r_player_class", 3),
				(party_set_slot, "p_main_party", slot_village_smoke_added, 1000),
			(try_end),
			(try_begin),
				(neq, "$r_player_class", 3),
				(call_script, "script_wm_simp_tr_init"),
			(try_end),
			(store_mul, ":value", 1000, 20),
			(call_script, "script_party_food_level_dif_no_mes", "p_main_party", ":value", 87),
			(change_screen_map),
			(call_script, "script_faction_army_list_scan"),
			(call_script, "script_wm_check_faction_castle_num_regular_activate"),
			(call_script, "script_check_faction_army_power_and_food"),
			(call_script, "script_wm_turn_dev_output_div_build_ai"),
			(display_message, "@Starting as a monarch or doge will apply after 24 hours of in-game time.", 0x00ffff00),
		], "."),
	
	#Hide this unless starting as lord
		("aftertwoyearsnoskip",
		[
		(eq, "$r_player_class", 3),
		(eq, "$player_noble", 1),
		],
		"Start as a rebel vassal in the process of overthrowing the current royalty. (Dangerous, failure will result in treason charges)",
		[
			(assign, "$started_as_monarch", 1), #Start during coup
			(assign, "$monarch_fix", 1), #Prevent lords from leaving after coup
			(tutorial_message, -1),
			(tutorial_message_set_background, 0),
			(party_set_slot, "p_main_party", slot_town_elder, 50),
			(party_set_slot, "p_main_party", slot_center_player_relation, 50),
			(troop_set_slot, "trp_player", slot_troop_cur_center, 0),
			(try_begin),
				(eq, "$r_player_class", 5),
				(party_set_slot, "p_main_party", slot_center_last_visited_by_lord, 1000),
			(else_try),
				(eq, "$r_player_class", 3),
				(party_set_slot, "p_main_party", slot_village_smoke_added, 1000),
			(try_end),
			(try_begin),
				(neq, "$r_player_class", 3),
				(call_script, "script_wm_simp_tr_init"),
			(try_end),
			(store_mul, ":value", 1000, 20),
			(call_script, "script_party_food_level_dif_no_mes", "p_main_party", ":value", 87),
			(change_screen_map),
			(call_script, "script_faction_army_list_scan"),
			(call_script, "script_wm_check_faction_castle_num_regular_activate"),
			(call_script, "script_check_faction_army_power_and_food"),
			(call_script, "script_wm_turn_dev_output_div_build_ai"),
			(display_message, "@Starting as a monarch or doge will apply after 24 hours of in-game time.", 0x00ffff00),
		], "."),

	#old start as lord
		("aftertwoyears",
		[
				(eq, "$r_player_class", 3),
		(eq, "$player_noble", 1),
		],
		"Start as a loyal vassal.",
		[
			(tutorial_message, -1),
			(tutorial_message_set_background, 0),
			(party_set_slot, "p_main_party", slot_town_elder, 50),
			(party_set_slot, "p_main_party", slot_center_player_relation, 50),
			(troop_set_slot, "trp_player", slot_troop_cur_center, 0),
			(try_begin),
				(eq, "$r_player_class", 5),
				(party_set_slot, "p_main_party", slot_center_last_visited_by_lord, 1000),
			(else_try),
				(eq, "$r_player_class", 3),
				(party_set_slot, "p_main_party", slot_village_smoke_added, 1000),
			(try_end),
			(try_begin),
				(neq, "$r_player_class", 3),
				(call_script, "script_wm_simp_tr_init"),
			(try_end),
			(store_mul, ":value", 1000, 20),
			(call_script, "script_party_food_level_dif_no_mes", "p_main_party", ":value", 87),
			(change_screen_map),
			(call_script, "script_faction_army_list_scan"),
			(call_script, "script_wm_check_faction_castle_num_regular_activate"),
			(call_script, "script_check_faction_army_power_and_food"),
			(call_script, "script_wm_turn_dev_output_div_build_ai"),
		], "."),

	
	
			("aftertwoyearsothers",
		[
		(neq, "$r_player_class", 3),
		(neq, "$player_noble", 1),
		],
		"Continue.",
		[
			(tutorial_message, -1),
			(tutorial_message_set_background, 0),
			(party_set_slot, "p_main_party", slot_town_elder, 50),
			(party_set_slot, "p_main_party", slot_center_player_relation, 50),
			(troop_set_slot, "trp_player", slot_troop_cur_center, 0),
			(try_begin),
				(eq, "$r_player_class", 5),
				(party_set_slot, "p_main_party", slot_center_last_visited_by_lord, 1000),
			(else_try),
				(eq, "$r_player_class", 3),
				(party_set_slot, "p_main_party", slot_village_smoke_added, 1000),
			(try_end),
			(try_begin),
				(neq, "$r_player_class", 3),
				(call_script, "script_wm_simp_tr_init"),
			(try_end),
			(store_mul, ":value", 1000, 20),
			(call_script, "script_party_food_level_dif_no_mes", "p_main_party", ":value", 87),
			(change_screen_map),
			(call_script, "script_faction_army_list_scan"),
			(call_script, "script_wm_check_faction_castle_num_regular_activate"),
			(call_script, "script_check_faction_army_power_and_food"),
			(call_script, "script_wm_turn_dev_output_div_build_ai"),
		], "."),
	]
	),

		("start_phase_3", 0, "{s16}^^You are walking down the street in {s1} when suddenly, you hear a woman scream. Weapon in hand, you turn to find the source of the commotion.",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[], ".")
	]
	),

	("start_phase_4", 0, "{s11}",
"none",
	[],
	[
		("continue",
		[],
		"Continue...",
		[], "."),

		("continue",
		[],
		"Continue...",
		[], ".")
	]
	),

		("end_game", 0, "Thanks for playing Tainted Paths, this mod had been developed by Faycal Kilali. The original versions were developed by Feodor Gerasimov & Molda.",
"none",
	[],
	[
		("end_game_bye",
		[],
		"Farewell.",
		[
			(change_screen_quit)
		], ".")
	]
	),

	("wm_wedding_menu", 0, "Best wishes for this wonderful day...^...and may your partner always be the heart of your marriage,^the light of your home,^and the ever-present partner in your life.^Congratulations.",
"none",
	[
		(set_background_mesh, "mesh_pic_marry")
	],
	[
		("continue",
		[],
		"Continue",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("wm_other_wedding", 0, "A messenger passed these news to you. {s7} and {s8} got married.",
"none",
	[
		(str_store_troop_name, 7, "$propose_target"),
		(str_store_troop_name, 8, "$wm_target_number11"),
		(set_background_mesh, "mesh_pic_marry")
	],
	[
		("continue",
		[],
		"Continue",
		[
			(assign, "$propose_target", 0),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("ruin_menu", 0, "{s41}",
"none",
	[
		(try_begin),
			(gt, "$ruin_qst_target_num", 0),
			(neg|party_slot_ge, "$ruin_qst_target_num", 3, 3),
			(store_sub, ":value", "$ruin_qst_target_num", "p_ruin_1"),
			(try_begin),
				(store_add, ":value_2", "str_r_name_001", ":value"),
				(str_store_string, 45, ":value_2"),
				(party_set_name, "$ruin_qst_target_num", 45),
			(try_end),
			(party_set_slot, "$ruin_qst_target_num", slot_party_ignore_player_until, 3),
			(play_sound, "snd_good_news_2"),
		(try_end),
		(store_sub, ":value", "$ruin_qst_target_num", "p_ruin_1"),
		(try_begin),
			(store_add, ":value_2", "mesh_1pic_ruin_1", ":value"),
			(set_background_mesh, ":value_2"),
		(try_end),
		(try_begin),
			(store_add, ":value_2", "str_r_name_001", ":value"),
			(str_store_string, 45, ":value_2"),
		(try_end),
		(try_begin),
			(store_add, ":value_2", "str_r_text_001", ":value"),
			(str_store_string, 41, ":value_2"),
		(try_end)
	],
	[
		("got_excalibur",
		[
			(party_slot_ge, "p_ruin_45", 3, 3),
			(eq, "$g_encountered_party", "p_ruin_45"),
			(neq, "$ruin_excalibur_clear", 5)
		],
		"Ruins: Approach the lake.",
		[
			(assign, "$ruin_excalibur_clear", 5),
			(display_message, "str_excalibur_1", 0x0000ff00),
			(assign, ":var_1", 928),
			(troop_add_item, "trp_player", ":var_1", 0),
			(play_sound, "snd_experience_gained"),
			(jump_to_menu, "mnu_ruin_menu")
		], "."),

		("got_eldorado",
		[
			(party_slot_ge, "p_ruin_26", 3, 3),
			(eq, "$g_encountered_party", "p_ruin_26"),
			(neq, "$ruin_eldorado_clear", 5)
		],
		"Ruins: Dialogue with local seniors.",
		[
			(assign, "$ruin_eldorado_clear", 5),
			(display_message, "str_eldorado", 0x0000ff00),
			(assign, ":var_1", 1105),
			(troop_add_item, "trp_player", ":var_1", 0),
			(play_sound, "snd_experience_gained"),
			(jump_to_menu, "mnu_ruin_menu")
		], "."),

		("got_blackbron",
		[
			(party_slot_ge, "p_ruin_149", 3, 3),
			(eq, "$g_encountered_party", "p_ruin_149"),
			(neq, "$ruin_blackbron_clear", 5)
		],
		"Ruins: There is something in the ground.",
		[
			(assign, "$ruin_blackbron_clear", 5),
			(display_message, "str_bronzearmor", 0x0000ff00),
			(assign, ":var_1", 531),
			(troop_add_item, "trp_player", ":var_1", 0),
			(play_sound, "snd_experience_gained"),
			(jump_to_menu, "mnu_ruin_menu")
		], "."),

		("got_Shiva_blade",
		[
			(party_slot_ge, "p_ruin_81", 3, 3),
			(eq, "$g_encountered_party", "p_ruin_81"),
			(neq, "$ruin_dun_shiva_blade_clear", 5)
		],
		"Ruins: Enter the Temple.",
		[
			(assign, "$molda_dun_win", 0),
			(assign, ":var_1", "scn_ruin_dun_shiva_blade"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "trp_jungle_2_m"),
			(set_visitor, 2, "trp_jungle_2_m"),
			(set_visitor, 3, "trp_jungle_2_m"),
			(set_visitor, 4, "trp_jungle_3_m"),
			(set_visitor, 10, "trp_jungle_2_ar"),
			(set_visitor, 11, "trp_jungle_2_ar"),
			(set_visitor, 12, "trp_jungle_2_ar"),
			(set_visitor, 13, "trp_jungle_4_m"),
			(set_visitor, 20, "trp_jungle_5_m"),
			(set_visitor, 21, "trp_jungle_4_cav"),
			(set_visitor, 22, "trp_jungle_4_cav"),
			(set_visitor, 31, "trp_jungle_5_cav_ele"),
			(set_visitor, 32, "trp_jungle_5_cav_ele"),
			(set_visitor, 33, "trp_jungle_6_cav_ele"),
			(set_jump_mission, "mt_dungeon_fight"),
			(assign, "$current_mission_template", "mt_dungeon_fight"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("got_Sun_blade",
		[
			(party_slot_ge, "p_ruin_3", 3, 3),
			(eq, "$g_encountered_party", "p_ruin_3"),
			(neq, "$ruin_dun_sun_blade_clear", 5)
		],
		"Ruins: Enter the Pyramid.",
		[
			(assign, "$molda_dun_win", 0),
			(assign, ":var_1", "scn_ruin_dun_sun_blade"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "trp_ww_m_2"),
			(set_visitor, 2, "trp_ww_m_2"),
			(set_visitor, 3, "trp_ww_m_3"),
			(set_visitor, 10, "trp_ww_a_3"),
			(set_visitor, 11, "trp_ww_a_3"),
			(set_visitor, 12, "trp_ww_m_4"),
			(set_visitor, 20, "trp_ww_m_5"),
			(set_visitor, 21, "trp_ww_m_5"),
			(set_visitor, 22, "trp_ww_m_6"),
			(set_jump_mission, "mt_dungeon_fight"),
			(assign, "$current_mission_template", "mt_dungeon_fight"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("got_dracul_armor",
		[
			(party_slot_ge, "p_ruin_124", 3, 3),
			(eq, "$g_encountered_party", "p_ruin_124"),
			(neq, "$ruin_dun_dracul_armor_clear", 5)
		],
		"Ruins: Walk around.",
		[
			(assign, "$molda_dun_win", 0),
			(assign, ":var_1", "scn_ruin_dun_dracul_armor"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "trp_unknown_creature"),
			(set_jump_mission, "mt_dungeon_fight"),
			(assign, "$current_mission_template", "mt_dungeon_fight"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("got_Vorpal_sword",
		[
			(party_slot_ge, "p_ruin_101", 3, 3),
			(eq, "$g_encountered_party", "p_ruin_101"),
			(neq, "$ruin_dun_askia_clear", 5)
		],
		"Ruins: Enter the Tomb.",
		[
			(assign, "$molda_dun_win", 0),
			(assign, ":var_1", "scn_ruin_dun_askia"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "trp_afri_1_m"),
			(set_visitor, 2, "trp_afri_2_m"),
			(set_visitor, 10, "trp_afri_1_m"),
			(set_visitor, 11, "trp_afri_3_m"),
			(set_visitor, 20, "trp_afri_1_m"),
			(set_visitor, 21, "trp_afri_4_m"),
			(set_visitor, 31, "trp_tt_lord_34_01"),
			(set_jump_mission, "mt_dungeon_fight"),
			(assign, "$current_mission_template", "mt_dungeon_fight"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("got_Impaler",
		[
			(party_slot_ge, "p_ruin_7", 3, 3),
			(eq, "$g_encountered_party", "p_ruin_7"),
			(neg|troop_slot_eq, "trp_player", 23, 1),
			(neq, "$ruin_dun_impaler_clear", 5)
		],
		"Ruins: Enter the Cathedral.",
		[
			(assign, "$molda_dun_win", 0),
			(assign, ":var_1", "scn_ruin_dun_impaler"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "trp_qq_m_3"),
			(set_visitor, 2, "trp_qq_m_2"),
			(set_visitor, 10, "trp_qq_m_4"),
			(set_visitor, 11, "trp_qq_a_2"),
			(set_visitor, 20, "trp_qq_c_6"),
			(set_visitor, 21, "trp_qq_a_3"),
			(set_visitor, 22, "trp_qq_a_3"),
			(set_jump_mission, "mt_dungeon_fight"),
			(assign, "$current_mission_template", "mt_dungeon_fight"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("got_shaver",
		[
			(party_slot_ge, "p_ruin_138", 3, 3),
			(eq, "$g_encountered_party", "p_ruin_138"),
			(neq, "$ruin_dun_shaver_clear", 5)
		],
		"Ruins: Enter the Castle.",
		[
			(assign, "$molda_dun_win", 0),
			(assign, ":var_1", "scn_ruin_dun_shaver"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "trp_qq_m_2"),
			(set_visitor, 2, "trp_qq_m_2"),
			(set_visitor, 3, "trp_qq_m_2"),
			(set_visitor, 4, "trp_qq_m_3"),
			(set_visitor, 10, "trp_qq_a_2"),
			(set_visitor, 11, "trp_qq_a_2"),
			(set_visitor, 12, "trp_qq_a_2"),
			(set_visitor, 13, "trp_qq_m_4"),
			(set_visitor, 20, "trp_qq_m_6"),
			(set_visitor, 21, "trp_qq_m_5"),
			(set_visitor, 22, "trp_qq_m_5"),
			(set_jump_mission, "mt_dungeon_fight"),
			(assign, "$current_mission_template", "mt_dungeon_fight"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("got_Archangel",
		[
			(party_slot_ge, "p_ruin_18", 3, 3),
			(eq, "$g_encountered_party", "p_ruin_18"),
			(troop_slot_eq, "trp_player", 23, 1),
			(neq, "$ruin_Archangel_clear", 5)
		],
		"Ruins: Pray.",
		[
			(display_message, "str_archangel", 0x0000ff00),
			(assign, ":var_1", 931),
			(troop_add_item, "trp_player", ":var_1", 0),
			(play_sound, "snd_experience_gained"),
			(assign, "$ruin_Archangel_clear", 5),
			(jump_to_menu, "mnu_ruin_menu")
		], "."),

		("got_Samurai_black_plate",
		[
			(party_slot_ge, "p_ruin_62", 3, 3),
			(eq, "$g_encountered_party", "p_ruin_62"),
			(neq, "$ruin_Samurai_black_plate_clear", 5)
		],
		"Ruins: Dialogue with the monks of the temple.",
		[
			(display_message, "str_samurai_plate", 0x0000ff00),
			(assign, ":var_1", 561),
			(troop_add_item, "trp_player", ":var_1", 0),
			(play_sound, "snd_experience_gained"),
			(assign, "$ruin_Samurai_black_plate_clear", 5),
			(jump_to_menu, "mnu_ruin_menu")
		], "."),

		("got_Evil_spirits_armor",
		[
			(party_slot_ge, "p_ruin_49", 3, 3),
			(eq, "$g_encountered_party", "p_ruin_49"),
			(neq, "$ruin_dun_Evil_spirits_armor_clear", 5)
		],
		"Ruins: Enter the Castle.",
		[
			(assign, "$molda_dun_win", 0),
			(assign, ":var_1", "scn_ruin_dun_evil_spirits_armor"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "trp_castle_samurai"),
			(set_jump_mission, "mt_dungeon_fight"),
			(assign, "$current_mission_template", "mt_dungeon_fight"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("got_Sphinx",
		[
			(party_slot_ge, "p_ruin_21", 3, 3),
			(eq, "$g_encountered_party", "p_ruin_21"),
			(neq, "$ruin_Sphinx_clear", 5)
		],
		"Ruins: Walk over to the sphinx.",
		[
			(assign, "$ruin_Sphinx_clear", 5),
			(jump_to_menu, "mnu_Sphinx_question")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
				(play_track, "track_reset_silence", 1), #Enforces new tracks to play ASAP.
		(music_set_situation, mtf_sit_travel),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("Sphinx_question", 0, "Stop! 'What walks on three legs in the morning, two legs at noon and three at night?' Fail this test and you shall live as a slave til the end of your days.",
"none",
	[
		(set_background_mesh, "mesh_1pic_ruin_21")
	],
	[
		("sphinx_answer_1",
		[],
		"Me",
		[
			(troop_get_type, ":type_player", "trp_player"),
			(troop_get_slot, ":player_last_quest_betrayed", "trp_player", slot_troop_last_quest_betrayed),
			(try_begin),
				(this_or_next|eq, ":type_player", 6),
				(this_or_next|eq, ":player_last_quest_betrayed", 5),
				(eq, ":player_last_quest_betrayed", 4),
				(str_store_string, 18, "str_sphinx_quiz"),
				(jump_to_menu, "mnu_Sphinx_question_2"),
			(else_try),
				(jump_to_menu, "mnu_Sphinx_wrong"),
			(try_end)
		], "."),

		("sphinx_answer_2",
		[],
		"Chiken",
		[
			(jump_to_menu, "mnu_Sphinx_wrong")
		], "."),

		("sphinx_answer_3",
		[],
		"You",
		[
			(jump_to_menu, "mnu_Sphinx_wrong")
		], "."),

		("sphinx_answer_4",
		[
			(store_attribute_level, ":attribute_level_player_2", "trp_player", 2),
			(ge, ":attribute_level_player_2", 20)
		],
		"African",
		[
			(str_store_string, 18, "str_empty_string"),
			(jump_to_menu, "mnu_Sphinx_question_2")
		], ".")
	]
	),

		("Sphinx_question_2", 0, "{s18}^^Correct. As a reward, i will tell you something you will find interesting.",
"none",
	[
		(set_background_mesh, "mesh_1pic_ruin_21")
	],
	[
		("sphinx_answer_end",
		[],
		"Obtain knowledge.",
		[
			(call_script, "script_battle_exp_diff", 1000, 87),
			(call_script, "script_adv_exp_diff", 1000, 87),
			(display_message, "str_sphinx_award", 0x00ffff00),
			(jump_to_menu, "mnu_ruin_menu")
		], ".")
	]
	),

		("Sphinx_wrong", 0, "Wrong!^^^^-Game over-^^You will be enslaved by the sphinx until the day of your death.",
"none",
	[
		(set_background_mesh, "mesh_1pic_ruin_21")
	],
	[
		("game_over",
		[],
		"-Game over-",
		[
			(change_screen_quit)
		], ".")
	]
	),

	("wm_book_store", 0, "You can buy the book here.",
"none",
	[
		(set_background_mesh, "mesh_pic_library")
	],
	[
		("book_1",
		[
			(call_script, "script_party_money_level_ge", "p_main_party", 1000),
			(eq, "$wm_mo_continue", 1),
			(neg|player_has_item, "$temp_glob_rand_1"),
			(str_store_item_name, 11, "$temp_glob_rand_1"),
			(neq, "$temp_glob_rand_1", 1105),
			(neq, "$temp_glob_rand_1", 1125)
		],
		"{s11}",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34),
			(troop_add_item, "trp_player", "$temp_glob_rand_1"),
			(display_message, "str_wm_pur_book", 0x00ffff00),
			(jump_to_menu, "mnu_wm_book_store")
		], "."),

		("book_2",
		[
			(call_script, "script_party_money_level_ge", "p_main_party", 1000),
			(eq, "$wm_mo_continue", 1),
			(neg|player_has_item, "$temp_glob_rand_2"),
			(str_store_item_name, 12, "$temp_glob_rand_2"),
			(neq, "$temp_glob_rand_2", 1105),
			(neq, "$temp_glob_rand_2", 1125)
		],
		"{s12}",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34),
			(troop_add_item, "trp_player", "$temp_glob_rand_2"),
			(display_message, "str_wm_pur_book", 0x00ffff00),
			(jump_to_menu, "mnu_wm_book_store")
		], "."),

		("book_3",
		[
			(call_script, "script_party_money_level_ge", "p_main_party", 1000),
			(eq, "$wm_mo_continue", 1),
			(neg|player_has_item, "$temp_glob_rand_3"),
			(str_store_item_name, 13, "$temp_glob_rand_3"),
			(neq, "$temp_glob_rand_3", 1105),
			(neq, "$temp_glob_rand_3", 1125)
		],
		"{s13}",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34),
			(troop_add_item, "trp_player", "$temp_glob_rand_3"),
			(display_message, "str_wm_pur_book", 0x00ffff00),
			(jump_to_menu, "mnu_wm_book_store")
		], "."),

		("book_4",
		[
			(call_script, "script_party_money_level_ge", "p_main_party", 1000),
			(eq, "$wm_mo_continue", 1),
			(neg|player_has_item, "$temp_glob_rand_4"),
			(str_store_item_name, 14, "$temp_glob_rand_4"),
			(neq, "$temp_glob_rand_4", 1105),
			(neq, "$temp_glob_rand_4", 1125)
		],
		"{s14}",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34),
			(troop_add_item, "trp_player", "$temp_glob_rand_4"),
			(display_message, "str_wm_pur_book", 0x00ffff00),
			(jump_to_menu, "mnu_wm_book_store")
		], "."),

		("book_5",
		[
			(call_script, "script_party_money_level_ge", "p_main_party", 1000),
			(eq, "$wm_mo_continue", 1),
			(neg|player_has_item, "$temp_glob_rand_5"),
			(str_store_item_name, 15, "$temp_glob_rand_5"),
			(neq, "$temp_glob_rand_5", 1105),
			(neq, "$temp_glob_rand_5", 1125)
		],
		"{s15}",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34),
			(troop_add_item, "trp_player", "$temp_glob_rand_5"),
			(display_message, "str_wm_pur_book", 0x00ffff00),
			(jump_to_menu, "mnu_wm_book_store")
		], "."),

		("book_6",
		[
			(call_script, "script_party_money_level_ge", "p_main_party", 1000),
			(eq, "$wm_mo_continue", 1),
			(neg|player_has_item, "$temp_glob_rand_6"),
			(str_store_item_name, 16, "$temp_glob_rand_6"),
			(neq, "$temp_glob_rand_6", 1105),
			(neq, "$temp_glob_rand_6", 1125)
		],
		"{s16}",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34),
			(troop_add_item, "trp_player", "$temp_glob_rand_6"),
			(display_message, "str_wm_pur_book", 0x00ffff00),
			(jump_to_menu, "mnu_wm_book_store")
		], "."),

		("book_7",
		[
			(call_script, "script_party_money_level_ge", "p_main_party", 1000),
			(eq, "$wm_mo_continue", 1),
			(neg|player_has_item, "$temp_glob_rand_7"),
			(str_store_item_name, 17, "$temp_glob_rand_7"),
			(neq, "$temp_glob_rand_7", 1105),
			(neq, "$temp_glob_rand_7", 1125)
		],
		"{s17}",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34),
			(troop_add_item, "trp_player", "$temp_glob_rand_7"),
			(display_message, "str_wm_pur_book", 0x00ffff00),
			(jump_to_menu, "mnu_wm_book_store")
		], "."),

		("back",
		[],
		"[Back]",
		[
			(jump_to_menu, "mnu_wm_town_visit")
		], ".")
	]
	),

("encount_ghost_ship", 0, "Suddenly, fog envelops your ship. You can barely see an arm's reach in front of you. ^Chills run down your spine as despite the thick fog, you glimpse the silhouette of a ship wreck slowly floating straight towards you.",
"none",
	[
		(set_background_mesh, "mesh_pic_ghost_ship_encount")
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(assign, "$ghost_ship_require", 1),
			(assign, ":var_1", 1422),
			(troop_add_item, "trp_player", ":var_1", 0),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

("comp_trade_sex_scene", 0, "In the bedroom..",
"none",
	[
		(set_background_mesh, "mesh_pic_meetlady")
	],
	[
		("continue",
		[],
		"Continue...",
		[
			(assign, "$wm_talk_state", 6),
			(modify_visitors_at_site, "scn_ex_bedroom"),
			(reset_visitors),
			(set_visitor, 10, "trp_player"),
			(set_visitor, 13, "$g_sex_troop_id"),
			(set_visitor, 11, "$g_sex_trade_comp_id"),
			(set_jump_mission, "mt_sex_mission"),
			(assign, "$current_mission_template", "mt_sex_mission"),
			(jump_to_scene, "scn_ex_bedroom"),
			(change_screen_mission)
		], ".")
	]
	),

	("bewanderer", 0, "Abandon everything and become a wanderer.",
"none",
	[
		(set_background_mesh, "mesh_pic_siege_sighted")
	],
	[
		("bewanderer",
		[],
		"Become wanderer.",
		[
			(call_script, "script_abondon_country_proceed", -25),
			(play_track, "track_wedding", 2),
			(display_message, "str_abandon_fac", 0x00ffff00),
			(call_script, "script_init_main_party_core_slot"),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("back",
		[],
		"[Back]",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),

	("wm_bank_menu", 0, "Banker: Greetings, what may i assist you with?^^Remaining months of repayment: {reg11}^Repayment amount with interest per month: {reg12}^Savings: {reg13}",    # I'm unsure what to put here. Context required.
"none",
	[
		(try_begin),
			(eq, "$debt_date_month", 0),
			(assign, "$ply_debt_per_month", 0),
		(try_end),
		(assign, reg11, "$debt_date_month"),
		(assign, reg12, "$ply_debt_per_month"),
		(assign, reg13, "$ply_account"),
		(val_mul, reg13, 5000),
		(set_background_mesh, "mesh_pic_bank_back")
	],
	[
		("deposit",
		[
			(store_mul, ":value", 1000, 10),
			(call_script, "script_party_money_level_ge", "p_main_party", ":value"),
			(eq, "$wm_mo_continue", 1),
			(lt, "$ply_account", 10)
		],
		"Deposit money (10000)",
		[
			(val_add, "$ply_account", 2),
			(store_mul, ":value", 1000, 10),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 34),
			(jump_to_menu, "mnu_wm_bank_menu")
		], "."),

		("withdraw",
		[
			(gt, "$ply_account", 0)
		],
		"Withdraw money (10000)",
		[
			(val_sub, "$ply_account", 2),
			(store_mul, ":value", 1000, 10),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
			(jump_to_menu, "mnu_wm_bank_menu")
		], "."),

		("borrow_5000",
		[
			(le, "$debt_date_month", 0)
		],
		"Borrow money (5000)",
		[
			(store_mul, ":value", 500, 10),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
			(assign, "$ply_debt_per_month", 500),
			(store_add, "$debt_date_month", 10, 2),
			(jump_to_menu, "mnu_wm_bank_menu")
		], "."),

		("borrow_10000",
		[
			(le, "$debt_date_month", 0)
		],
		"Borrow money (10000)",
		[
			(store_mul, ":value", 500, 20),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
			(assign, "$ply_debt_per_month", 1000),
			(store_add, "$debt_date_month", 10, 2),
			(jump_to_menu, "mnu_wm_bank_menu")
		], "."),

		("borrow_20000",
		[
			(le, "$debt_date_month", 0)
		],
		"Borrow money (20000)",
		[
			(store_mul, ":value", 1000, 20),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
			(store_add, "$ply_debt_per_month", 1000, 2),
			(store_add, "$debt_date_month", 10, 2),
			(jump_to_menu, "mnu_wm_bank_menu")
		], "."),

		("buy_checkbook",
		[
			(eq, "$r_player_class", 1),
			(store_mul, ":value", 1000, 50),
			(call_script, "script_party_money_level_ge", "p_main_party", ":value"),
			(eq, "$wm_mo_continue", 1)
		],
		"Buy Checkbook (50000)",
		[
			(store_mul, ":value", 1000, 50),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 34),
			(troop_add_item, "trp_player", 1441, 0),
			(jump_to_menu, "mnu_wm_bank_menu")
		], "."),

		("sell_checkbook",
		[
			(eq, "$r_player_class", 1),
			(player_has_item, 1441)
		],
		"Sell Checkbook (50000)",
		[
			(store_mul, ":value", 1000, 50),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
			(troop_remove_items, "trp_player", 1441, 1),
			(jump_to_menu, "mnu_wm_bank_menu")
		], "."),

		("back",
		[],
		"[Back]",
		[
			(jump_to_menu, "mnu_wm_town_visit")
		], ".")
	]
	),

	("coup_success", 0, "You have successfully overthrown the previous monarch. You may now decide a new form of government.",
"none",
	[
		(set_background_mesh, "mesh_pic_victory"),
		(assign, "$attempt_coup", 0),
		(assign, "$wm_battle_result_state", 0)
	],
	[
		("monarchy",
		[],
		"We will follow a feudal system, with me as its monarch and rightful sole protector.",
		[
			(faction_get_slot, ":wm_player_fac_29", "$wm_player_fac", 29),
			(try_for_range, ":party", "p_pyongyang", "p_place_end"),
				(store_faction_of_party, ":faction_of_party_party", ":party"),
				(eq, ":faction_of_party_party", "$wm_player_fac"),
				(call_script, "script_party_army_size_execute", ":party", 50, 3),
				(call_script, "script_disaster_damage_to_build", ":party", 50),
				(call_script, "script_party_extra_text_for_town", ":party"),
			(try_end),
			(try_for_parties, ":party"),
				(party_slot_eq, ":party", slot_party_type, 1),
				(store_faction_of_party, ":faction_of_party_party", ":party"),
				(eq, ":faction_of_party_party", "$wm_player_fac"),
				(call_script, "script_party_army_size_execute", ":party", 30, 3),
			(try_end),
			(faction_set_slot, "$wm_player_fac", slot_faction_ai_object, 0),
			(faction_get_slot, ":wm_player_fac_1", "$wm_player_fac", 1),
			(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(eq, ":faction_of_troop_troop", "$wm_player_fac"),
				(store_random_in_range, ":random_in_range_0_2", 0, 2),
				(try_begin),
					(eq, ":wm_player_fac_1", ":troop"),
					(call_script, "script_lord_change_faction", ":troop"),
				(else_try),
					(neq, "$monarch_fix", 1),
					(troop_slot_eq, ":troop", slot_troop_leaded_party, 0),
					(eq, ":random_in_range_0_2", 0),
					(call_script, "script_lord_change_faction", ":troop"),
				(try_end),
				(try_begin),
					(troop_slot_ge, ":troop", 10, 1),
					(call_script, "script_change_player_relation_with_troop", ":troop", 50),
					(troop_set_slot, ":troop", slot_troop_leaded_party, 0),
				(try_end),
			(try_end),
			(faction_set_slot, "$wm_player_fac", 1, "trp_player"),
			(party_set_slot, ":wm_player_fac_29", slot_town_tavern, "trp_player"),
			(call_script, "script_party_extra_text_for_town", ":wm_player_fac_29"),
			(play_sound, "snd_win_1"),
			(try_begin),
			(neq, "$monarch_fix", 0),
			(assign, "$monarch_fix", 0),
			(assign, "$disable_coups", 1),
			(try_end),
			(start_presentation, "prsnt_name_kingdom")
		], "."),

		("republic",
		[],
		"We will establish a republic system, with each noble having an equal say on the affairs of the state.",
		[
			(faction_get_slot, ":wm_player_fac_29", "$wm_player_fac", 29),
			(try_for_range, ":party", "p_pyongyang", "p_place_end"),
				(store_faction_of_party, ":faction_of_party_party", ":party"),
				(eq, ":faction_of_party_party", "$wm_player_fac"),
				(call_script, "script_party_army_size_execute", ":party", 50, 3),
				(call_script, "script_disaster_damage_to_build", ":party", 50),
				(call_script, "script_party_extra_text_for_town", ":party"),
			(try_end),
			(try_for_parties, ":party"),
				(party_slot_eq, ":party", slot_party_type, 1),
				(store_faction_of_party, ":faction_of_party_party", ":party"),
				(eq, ":faction_of_party_party", "$wm_player_fac"),
				(call_script, "script_party_army_size_execute", ":party", 30, 3),
			(try_end),
			(faction_set_slot, "$wm_player_fac", slot_faction_ai_object, 1),
			(faction_get_slot, ":wm_player_fac_1", "$wm_player_fac", 1),
			(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(eq, ":faction_of_troop_troop", "$wm_player_fac"),
				(store_random_in_range, ":random_in_range_0_2", 0, 2),
				(try_begin),
					(eq, ":wm_player_fac_1", ":troop"),
					(call_script, "script_lord_change_faction", ":troop"),
				(else_try),
				(neq, "$monarch_fix", 1),
					(troop_slot_eq, ":troop", slot_troop_leaded_party, 0),
					(eq, ":random_in_range_0_2", 0),
					(call_script, "script_lord_change_faction", ":troop"),
				(try_end),
				(try_begin),
					(troop_slot_ge, ":troop", 10, 1),
					(call_script, "script_change_player_relation_with_troop", ":troop", 50),
					(troop_set_slot, ":troop", slot_troop_leaded_party, 0),
				(try_end),
			(try_end),
			(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(eq, ":faction_of_troop_troop", "$wm_player_fac"),
				(call_script, "script_change_player_relation_with_troop", ":troop", 50),
			(try_end),
			(faction_set_slot, "$wm_player_fac", 1, 1),
			(party_set_slot, ":wm_player_fac_29", slot_town_tavern, "trp_player"),
			(call_script, "script_party_extra_text_for_town", ":wm_player_fac_29"),
			(play_sound, "snd_win_1"),
			(try_begin),
			(neq, "$monarch_fix", 0),
			(assign, "$monarch_fix", 0),
			(assign, "$disable_coups", 1),
			(try_end),
			(start_presentation, "prsnt_name_kingdom")
		], ".")
	]
	),

	("coup_fail", 0, "You failed the coup. Your supporters have scattered, and you've barely made it out alive.",
"none",
	[
	(assign, "$monarch_fix", 0), #Disable coup related stuff
		(play_track, "track_calm_night_2", 2),
		(set_background_mesh, "mesh_pic_defeat"),
		(assign, "$attempt_coup", 0),
		(assign, "$wm_battle_result_state", 0)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
				(play_track, "track_reset_silence", 1), #Enforces new tracks to play ASAP.
		(music_set_situation, mtf_sit_travel),
			(try_for_range, ":party", "p_pyongyang", "p_place_end"),
				(store_faction_of_party, ":faction_of_party_party", ":party"),
				(eq, ":faction_of_party_party", "$wm_player_fac"),
				(call_script, "script_party_army_size_execute", ":party", 50, 3),
				(call_script, "script_disaster_damage_to_build", ":party", 50),
				(call_script, "script_party_extra_text_for_town", ":party"),
			(try_end),
			(try_for_parties, ":party"),
				(party_slot_eq, ":party", slot_party_type, 1),
				(store_faction_of_party, ":faction_of_party_party", ":party"),
				(eq, ":faction_of_party_party", "$wm_player_fac"),
				(call_script, "script_party_army_size_execute", ":party", 60, 3),
			(try_end),
			(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(eq, ":faction_of_troop_troop", "$wm_player_fac"),
				(try_begin),
					(troop_slot_ge, ":troop", 10, 1),
					(troop_set_slot, ":troop", slot_troop_leaded_party, 0),
					(store_random_in_range, ":random_in_range_0_2", 0, 2),
					(eq, ":random_in_range_0_2", 0),
					(call_script, "script_lord_change_faction", ":troop"),
				(try_end),
			(try_end),
			(call_script, "script_abondon_country_proceed", -199),
			(call_script, "script_set_player_relation_with_faction", "$wm_player_fac", -99),
			(call_script, "script_init_main_party_core_slot"),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("coup_view", 0, "Your supporters: {reg9}^Required supporters: {reg7}^Lords Sum: {reg8}^^{s11}",
"none",
	[
		(set_background_mesh, "mesh_pic_siege_sighted"),
		(assign, "$progress_civilwar", 0),
		(assign, ":var_1", 0),
		(assign, ":var_2", 0),
		(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
			(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
			(eq, ":faction_of_troop_troop", "$wm_player_fac"),
			(val_add, ":var_1", 1),
			(try_begin),
				(troop_slot_ge, ":troop", 10, 1),
				(val_add, ":var_2", 1),
			(try_end),
		(try_end),
		(try_begin),
			(ge, ":var_1", 3),
			(store_div, ":value", ":var_1", 3),
		(else_try),
			(assign, ":value", 2),
		(try_end),
		(try_begin),
			(ge, ":var_2", 2),
			(ge, ":var_2", ":value"),
			(assign, "$progress_civilwar", 1),
		(try_end),
		(try_begin),
			(eq, "$progress_civilwar", 1),
			(str_store_string, 11, "str_can_coup"),
		(else_try),
			(str_store_string, 11, "str_cant_coup"),
		(try_end),
		(assign, reg8, ":var_1"),
		(assign, reg9, ":var_2"),
		(assign, reg7, ":value")
	],
	[
		("try_coup",
		[
			(is_between, "$wm_player_fac", "fac_kingdom_1", "fac_kingdoms_end"),
			(faction_get_slot, ":wm_player_fac_29", "$wm_player_fac", 29),
			(eq, "$g_encountered_party", ":wm_player_fac_29")
		],
		"[Attempt The Coup]",
		[
			(try_begin),
				(neq, "$progress_civilwar", 1),
				(display_message, "str_need_supporter", 0x00ff0000),
			(else_try),
				(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
				(lt, ":party_size_wo_prisoners_main_party", 8000),
				(display_message, "str_need_armyy", 0x00ff0000),
			(else_try),
				(assign, "$attempt_coup", 1),
				(jump_to_menu, "mnu_coup_progress"),
			(try_end)
		], "."),

		("back",
		[],
		"[Back]",
		[
			(jump_to_menu, "mnu_wm_town_visit")
		], ".")
	]
	),

	("coup_progress", 0, "{s12}^^Enemy commander: {s7}^^Army sizes: {reg11} allies, {reg8} enemies. ^Trained troops %: {reg12} of allied troops, {reg9} of enemy troops. ^Morale: {reg13} allies morale, {reg10} enemies morale. ^Max troops deployable at a time: {reg16}^Total troops deployed: {reg15} allies, {reg14} enemies.",
"none",
	[
		(assign, "$wm_battle_result_state", 0),
		(try_begin),
			(eq, "$attempt_coup", 1),
			(str_store_string, 12, "str_coup_step_1"),
			(party_set_faction, "p_exparty_backup", "$wm_player_fac"),
			#####Coup additions
			(try_begin),
			(neq, "$monarch_fix", 1), #If not starting as King, Doge
			(call_script, "script_party_army_size_execute", "p_exparty_backup", 4000, 5), #4000 def Potentional for coup fix
			(else_try),
			(eq, "$monarch_fix", 1), #if starting as King, Doge
			(store_random_in_range, ":first_phase", 1900, 4000),
			(call_script, "script_party_army_size_execute", "p_exparty_backup", ":first_phase", 5),
			(try_end),
			#####Coup additions
			(party_set_slot, "p_exparty_backup", slot_town_elder, 100),
			(party_set_slot, "p_exparty_backup", slot_center_player_relation, 100),
			(faction_get_slot, ":wm_player_fac_1", "$wm_player_fac", 1),
			(faction_get_slot, ":wm_player_fac_19", "$wm_player_fac", 19),
			(try_begin),
				(is_between, ":wm_player_fac_1", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(party_set_slot, "p_exparty_backup", slot_town_horse_merchant, ":wm_player_fac_1"),
			(else_try),
				(party_set_slot, "p_exparty_backup", slot_town_horse_merchant, ":wm_player_fac_19"),
			(try_end),
			(assign, "$wm_target_party", "p_exparty_backup"),
		(else_try),
			(eq, "$attempt_coup", 2),
			(str_store_string, 12, "str_coup_step_2"),
			(store_sub, ":value", "$count_player_team", "$troop_alive_player"),
			(val_mul, ":value", 100),
			(val_div, ":value", "$count_player_team"),
			(store_sub, ":value_2", 100, ":value"),
			(val_add, ":value_2", 25),
			(try_begin),
				(lt, ":value_2", 100),
				(call_script, "script_party_army_size_execute", "p_main_party", ":value_2", 3),
				(call_script, "script_moral_level_diff", "p_main_party", 15),
				(call_script, "script_train_level_diff", "p_main_party", 10),
			(try_end),
			(party_set_faction, "p_exparty_backup", "$wm_player_fac"),
			
			#####Coup additions
			(try_begin),
			(neq, "$monarch_fix", 1), #If not starting as King, Doge
			(call_script, "script_party_army_size_execute", "p_exparty_backup", 7000, 5),#7000 def Potentional for coup fix
			(else_try),
			(eq, "$monarch_fix", 1), #if starting as King, Doge
			(store_random_in_range, ":second_phase", 2300, 7000),
			(call_script, "script_party_army_size_execute", "p_exparty_backup", ":second_phase", 5),
			(try_end),
			#####Coup additions
			
			
			(party_set_slot, "p_exparty_backup", slot_town_elder, 80),
			(party_set_slot, "p_exparty_backup", slot_center_player_relation, 100),
			(faction_get_slot, ":wm_player_fac_1", "$wm_player_fac", 1),
			(faction_get_slot, ":wm_player_fac_19", "$wm_player_fac", 19),
			(try_begin),
				(is_between, ":wm_player_fac_1", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(party_set_slot, "p_exparty_backup", slot_town_horse_merchant, ":wm_player_fac_1"),
			(else_try),
				(party_set_slot, "p_exparty_backup", slot_town_horse_merchant, ":wm_player_fac_19"),
			(try_end),
			(assign, "$wm_target_party", "p_exparty_backup"),
		(else_try),
			(eq, "$attempt_coup", 3),
			(str_store_string, 12, "str_coup_step_3"),
			(store_sub, ":value", "$count_player_team", "$troop_alive_player"),
			(val_mul, ":value", 100),
			(val_div, ":value", "$count_player_team"),
			(store_sub, ":value_2", 100, ":value"),
			(val_add, ":value_2", 25),
			(try_begin),
				(lt, ":value_2", 100),
				(call_script, "script_party_army_size_execute", "p_main_party", ":value_2", 3),
				(call_script, "script_moral_level_diff", "p_main_party", 15),
				(call_script, "script_train_level_diff", "p_main_party", 10),
			(try_end),
			(party_set_faction, "p_exparty_backup", "$wm_player_fac"),
			
			#####Coup additions
			(try_begin),
			(neq, "$monarch_fix", 1), #If not starting as King, Doge
			(call_script, "script_party_army_size_execute", "p_exparty_backup", 7000, 5), #7000 def Potentional for coup fix
			(else_try),
			(eq, "$monarch_fix", 1), #if starting as King, Doge
			(store_random_in_range, ":third_phase", 2100, 7000),
			(call_script, "script_party_army_size_execute", "p_exparty_backup", ":third_phase", 5),
			(try_end),
			#####Coup additions
			
			(party_set_slot, "p_exparty_backup", slot_town_elder, 50),
			(party_set_slot, "p_exparty_backup", slot_center_player_relation, 100),
			(faction_get_slot, ":wm_player_fac_1", "$wm_player_fac", 1),
			(faction_get_slot, ":wm_player_fac_19", "$wm_player_fac", 19),
			(try_begin),
				(is_between, ":wm_player_fac_1", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(party_set_slot, "p_exparty_backup", slot_town_horse_merchant, ":wm_player_fac_1"),
			(else_try),
				(party_set_slot, "p_exparty_backup", slot_town_horse_merchant, ":wm_player_fac_19"),
			(try_end),
			(assign, "$wm_target_party", "p_exparty_backup"),
		(try_end),
		(set_background_mesh, "mesh_pic_siege_sighted"),
		(call_script, "script_party_count_fit_for_battle", "p_main_party"),
		(assign, "$player_army_size", reg0),
		(party_get_slot, "$player_train_level", "p_main_party", slot_town_elder),
		(party_get_slot, "$player_moral_level", "p_main_party", slot_center_player_relation),
		(call_script, "script_party_count_fit_for_battle", "$wm_target_party"),
		(assign, "$enemy_army_size", reg0),
		(party_get_slot, "$enemy_commander", "$wm_target_party", slot_town_horse_merchant),
		(party_get_slot, "$enemy_train_level", "$wm_target_party", slot_town_elder),
		(party_get_slot, "$enemy_moral_level", "$wm_target_party", slot_center_player_relation),
		(try_begin),
			(lt, "$enemy_commander", 3),
			(store_faction_of_party, ":faction_of_party_wm_target_party", "$wm_target_party"),
			(faction_get_slot, "$enemy_commander", ":faction_of_party_wm_target_party", 19),
		(try_end),
		(assign, reg11, "$player_army_size"),
		(assign, reg12, "$player_train_level"),
		(assign, reg13, "$player_moral_level"),
		(str_store_troop_name, 7, "$enemy_commander"),
		(assign, reg8, "$enemy_army_size"),
		(assign, reg9, "$enemy_train_level"),
		(assign, reg10, "$enemy_moral_level"),
		(call_script, "script_battle_scale_sett"),
		(store_div, ":value_3", "$enemy_spawn_num", 10),
		(val_add, ":value_3", "$enemy_spawn_num"),
		(store_div, ":value_4", "$player_spawn_num", 10),
		(val_add, ":value_4", "$player_spawn_num"),
		(assign, reg14, ":value_3"),
		(assign, reg15, ":value_4"),
		(store_mul, reg16, "$bt_army_scale", 2),
		(assign, reg17, "$player_tactics_skill"),
		(assign, reg18, "$enemy_tactics_skill"),
		(try_begin),
			(set_fixed_point_multiplier, 1000),
			(position_set_x, 0, 600),
			(position_set_y, 0, 400),
			(position_set_z, 0, 750),
			(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$enemy_commander", 0),
		(try_end),
		(call_script, "script_equip_supp_slot_export", "p_main_party"),
		(call_script, "script_equip_supp_slot_export", "$wm_target_party"),
		(faction_get_slot, "$enemy_has_horse", "$wm_player_fac", slot_faction_adjective),
		(faction_get_slot, "$enemy_has_finewood", "$wm_player_fac", 23),
		(faction_get_slot, "$enemy_has_iron", "$wm_player_fac", 24),
		(faction_get_slot, "$player_has_horse", "$wm_player_fac", slot_faction_adjective),
		(faction_get_slot, "$player_has_finewood", "$wm_player_fac", 23),
		(faction_get_slot, "$player_has_iron", "$wm_player_fac", 24)
	],
	[
		("attack_capital",
		[
			(eq, "$attempt_coup", 1)
		],
		"-Attack the Capital-",
		[
			(assign, "$player_assistant_1", 0),
			(assign, "$enemy_assistant_1", 0),
			(assign, "$enemy_assistant_2", 0),
			(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(eq, ":faction_of_troop_troop", "$wm_player_fac"),
				(try_begin),
					(troop_slot_ge, ":troop", 10, 1),
					(eq, "$player_assistant_1", 0),
					(assign, "$player_assistant_1", ":troop"),
				(try_end),
				(try_begin),
					(troop_slot_eq, ":troop", slot_troop_leaded_party, 0),
					(eq, "$enemy_assistant_1", 0),
					(assign, "$enemy_assistant_1", ":troop"),
				(try_end),
				(try_begin),
					(troop_slot_eq, ":troop", slot_troop_leaded_party, 0),
					(neq, "$enemy_assistant_1", 0),
					(eq, "$enemy_assistant_2", 0),
					(assign, "$enemy_assistant_2", ":troop"),
				(try_end),
			(try_end),
			(assign, "$wm_battle_result_state", 0),
			(assign, "$player_is_attack", 1),
			(assign, "$wm_allow_retreat", 0),
			(call_script, "script_molda_scene_culture", "$g_encountered_party"),
			(assign, ":var_3", "$town_scene_type"),
			(assign, "$molda_siege_type", 5),
			(troop_set_health, "trp_player", 100),
			(troop_set_health, "$enemy_commander", 100),
			(call_script, "script_assistant_lord_rand"),
			(modify_visitors_at_site, ":var_3"),
			(reset_visitors),
			(try_begin),
				(eq, "$town_culture_type", 9),
				(set_jump_mission, "mt_castle_attack_walls_molda_uurt"),
				(assign, "$current_mission_template", "mt_castle_attack_walls_molda_uurt"),
				(set_visitor, 1, "trp_player"),
				(set_visitor, 2, "$enemy_commander"),
				(assign, ":value", 120),
				(assign, ":value_2", 124),
			(else_try),
				(eq, "$town_culture_type", 10),
				(set_jump_mission, "mt_castle_attack_walls_molda_teepee"),
				(assign, "$current_mission_template", "mt_castle_attack_walls_molda_teepee"),
				(set_visitor, 1, "trp_player"),
				(set_visitor, 2, "$enemy_commander"),
				(assign, ":value", 120),
				(assign, ":value_2", 124),
			(else_try),
				(set_jump_mission, "mt_castle_attack_walls_inner_fight_coup_1"),
				(assign, "$current_mission_template", "mt_castle_attack_walls_inner_fight_coup_1"),
				(set_visitor, 1, "trp_player"),
				(set_visitor, 4, "$enemy_commander"),
				(assign, ":value", 0),
				(assign, ":value_2", 105),
			(try_end),
			(assign, "$bt_player_entry_1", ":value"),
			(assign, "$bt_player_entry_2", ":value"),
			(assign, "$bt_player_entry_3", ":value"),
			(assign, "$bt_player_entry_4", ":value"),
			(assign, "$bt_player_entry_5", ":value"),
			(assign, "$bt_player_entry_6", ":value"),
			(assign, "$bt_player_entry_7", ":value"),
			(assign, "$bt_player_entry_8", ":value"),
			(assign, "$bt_player_entry_9", ":value"),
			(assign, "$bt_enemy_entry_1", ":value_2"),
			(assign, "$bt_enemy_entry_2", ":value_2"),
			(assign, "$bt_enemy_entry_3", ":value_2"),
			(assign, "$bt_enemy_entry_4", ":value_2"),
			(assign, "$bt_enemy_entry_5", ":value_2"),
			(assign, "$bt_enemy_entry_6", ":value_2"),
			(assign, "$bt_enemy_entry_7", ":value_2"),
			(assign, "$bt_enemy_entry_8", ":value_2"),
			(assign, "$bt_enemy_entry_9", ":value_2"),
			(assign, "$player_start_entry", ":value"),
			(assign, "$enemy_start_entry", ":value_2"),
			(assign, "$player_retreat_entry_begin", ":value"),
			(assign, "$player_retreat_entry_end", ":value"),
			(assign, "$enemy_retreat_entry_begin", ":value_2"),
			(assign, "$enemy_retreat_entry_end", ":value_2"),
			(assign, "$player_outer_entry_1", ":value"),
			(assign, "$player_outer_entry_2", ":value"),
			(assign, "$player_outer_entry_3", ":value"),
			(assign, "$player_outer_entry_4", ":value"),
			(assign, "$player_outer_entry_5", ":value"),
			(assign, "$player_outer_entry_6", ":value"),
			(assign, "$enemy_outer_entry_1", ":value_2"),
			(assign, "$enemy_outer_entry_2", ":value_2"),
			(assign, "$enemy_outer_entry_3", ":value_2"),
			(assign, "$enemy_outer_entry_4", ":value_2"),
			(assign, "$enemy_outer_entry_5", ":value_2"),
			(assign, "$enemy_outer_entry_6", ":value_2"),
			(jump_to_scene, ":var_3"),
			(call_script, "script_rand_glob_dice"),
			(change_screen_mission)
		], "."),

		("defend_capital",
		[
			(eq, "$attempt_coup", 2)
		],
		"-Defend the Capital-",
		[
			(assign, "$player_assistant_1", 0),
			(assign, "$enemy_assistant_1", 0),
			(assign, "$enemy_assistant_2", 0),
			(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(eq, ":faction_of_troop_troop", "$wm_player_fac"),
				(try_begin),
					(troop_slot_ge, ":troop", 10, 1),
					(eq, "$player_assistant_1", 0),
					(assign, "$player_assistant_1", ":troop"),
				(try_end),
				(try_begin),
					(troop_slot_eq, ":troop", slot_troop_leaded_party, 0),
					(eq, "$enemy_assistant_1", 0),
					(assign, "$enemy_assistant_1", ":troop"),
				(try_end),
				(try_begin),
					(troop_slot_eq, ":troop", slot_troop_leaded_party, 0),
					(neq, "$enemy_assistant_1", 0),
					(eq, "$enemy_assistant_2", 0),
					(assign, "$enemy_assistant_2", ":troop"),
				(try_end),
			(try_end),
			(assign, "$wm_battle_result_state", 0),
			(assign, "$is_siege_defence", 1),
			(assign, "$player_is_attack", 0),
			(assign, "$wm_allow_retreat", 0),
			(call_script, "script_molda_scene_culture", "$g_encountered_party"),
			(assign, ":var_3", "$town_scene_type"),
			(troop_set_health, "trp_player", 100),
			(troop_set_health, "$enemy_commander", 100),
			(call_script, "script_assistant_lord_rand"),
			(modify_visitors_at_site, ":var_3"),
			(reset_visitors),
			(try_begin),
				(eq, "$town_culture_type", 9),
				(assign, "$molda_siege_type", 0),
				(set_jump_mission, "mt_castle_attack_walls_molda_uurt"),
				(assign, "$current_mission_template", "mt_castle_attack_walls_molda_uurt"),
				(set_visitor, 2, "trp_player"),
				(set_visitor, 1, "$enemy_commander"),
				(assign, ":value", 124),
				(assign, ":value_2", 120),
			(else_try),
				(eq, "$town_culture_type", 10),
				(assign, "$molda_siege_type", 0),
				(set_jump_mission, "mt_castle_attack_walls_molda_teepee"),
				(assign, "$current_mission_template", "mt_castle_attack_walls_molda_teepee"),
				(set_visitor, 2, "trp_player"),
				(set_visitor, 1, "$enemy_commander"),
				(assign, ":value", 124),
				(assign, ":value_2", 120),
			(else_try),
				(assign, "$molda_siege_type", 3),
				(set_jump_mission, "mt_castle_attack_walls_molda_ladder_two"),
				(assign, "$current_mission_template", "mt_castle_attack_walls_molda_ladder_two"),
				(set_visitor, 2, "trp_player"),
				(set_visitor, 1, "$enemy_commander"),
				(assign, ":value", 81),
				(assign, ":value_2", 80),
			(try_end),
			(assign, "$bt_player_entry_1", ":value"),
			(assign, "$bt_player_entry_2", ":value"),
			(assign, "$bt_player_entry_3", ":value"),
			(assign, "$bt_player_entry_4", ":value"),
			(assign, "$bt_player_entry_5", ":value"),
			(assign, "$bt_player_entry_6", ":value"),
			(assign, "$bt_player_entry_7", ":value"),
			(assign, "$bt_player_entry_8", ":value"),
			(assign, "$bt_player_entry_9", ":value"),
			(assign, "$bt_enemy_entry_1", ":value_2"),
			(assign, "$bt_enemy_entry_2", ":value_2"),
			(assign, "$bt_enemy_entry_3", ":value_2"),
			(assign, "$bt_enemy_entry_4", ":value_2"),
			(assign, "$bt_enemy_entry_5", ":value_2"),
			(assign, "$bt_enemy_entry_6", ":value_2"),
			(assign, "$bt_enemy_entry_7", ":value_2"),
			(assign, "$bt_enemy_entry_8", ":value_2"),
			(assign, "$bt_enemy_entry_9", ":value_2"),
			(assign, "$player_start_entry", ":value"),
			(assign, "$enemy_start_entry", ":value_2"),
			(assign, "$player_retreat_entry_begin", ":value"),
			(assign, "$player_retreat_entry_end", ":value"),
			(assign, "$enemy_retreat_entry_begin", ":value_2"),
			(assign, "$enemy_retreat_entry_end", ":value_2"),
			(assign, "$player_outer_entry_1", ":value"),
			(assign, "$player_outer_entry_2", ":value"),
			(assign, "$player_outer_entry_3", ":value"),
			(assign, "$player_outer_entry_4", ":value"),
			(assign, "$player_outer_entry_5", ":value"),
			(assign, "$player_outer_entry_6", ":value"),
			(assign, "$enemy_outer_entry_1", ":value_2"),
			(assign, "$enemy_outer_entry_2", ":value_2"),
			(assign, "$enemy_outer_entry_3", ":value_2"),
			(assign, "$enemy_outer_entry_4", ":value_2"),
			(assign, "$enemy_outer_entry_5", ":value_2"),
			(assign, "$enemy_outer_entry_6", ":value_2"),
			(jump_to_scene, ":var_3"),
			(call_script, "script_rand_glob_dice"),
			(change_screen_mission)
		], "."),

		("attack_etc",
		[
			(eq, "$attempt_coup", 3)
		],
		"Attack the last of the resistance",
		[
			(assign, "$player_assistant_1", 0),
			(assign, "$enemy_assistant_1", 0),
			(assign, "$enemy_assistant_2", 0),
			(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(eq, ":faction_of_troop_troop", "$wm_player_fac"),
				(try_begin),
					(troop_slot_ge, ":troop", 10, 1),
					(eq, "$player_assistant_1", 0),
					(assign, "$player_assistant_1", ":troop"),
				(try_end),
				(try_begin),
					(troop_slot_eq, ":troop", slot_troop_leaded_party, 0),
					(eq, "$enemy_assistant_1", 0),
					(assign, "$enemy_assistant_1", ":troop"),
				(try_end),
				(try_begin),
					(troop_slot_eq, ":troop", slot_troop_leaded_party, 0),
					(neq, "$enemy_assistant_1", 0),
					(eq, "$enemy_assistant_2", 0),
					(assign, "$enemy_assistant_2", ":troop"),
				(try_end),
			(try_end),
			(assign, "$wm_battle_result_state", 0),
			(assign, "$player_is_attack", 1),
			(assign, "$wm_allow_retreat", 0),
			(call_script, "script_molda_scene_culture", "$g_encountered_party"),
			(assign, ":var_3", "$town_scene_village"),
			(assign, ":var_4", "mt_coup_last_battle"),
			(set_jump_mission, ":var_4"),
			(assign, "$current_mission_template", ":var_4"),
			(modify_visitors_at_site, ":var_3"),
			(reset_visitors),
			(jump_to_scene, ":var_3"),
			(assign, "$molda_battle_scn_vari", -1),
			(troop_set_health, "trp_player", 100),
			(troop_set_health, "$enemy_commander", 100),
			(call_script, "script_assistant_lord_rand"),
			(set_visitor, 1, "trp_player"),
			(set_visitor, 3, "$enemy_commander"),
			(assign, ":var_5", 0),
			(assign, ":var_6", 4),
			(assign, "$bt_player_entry_1", ":var_5"),
			(assign, "$bt_player_entry_2", ":var_5"),
			(assign, "$bt_player_entry_3", ":var_5"),
			(assign, "$bt_player_entry_4", ":var_5"),
			(assign, "$bt_player_entry_5", ":var_5"),
			(assign, "$bt_player_entry_6", ":var_5"),
			(assign, "$bt_player_entry_7", ":var_5"),
			(assign, "$bt_player_entry_8", ":var_5"),
			(assign, "$bt_player_entry_9", ":var_5"),
			(assign, "$bt_enemy_entry_1", ":var_6"),
			(assign, "$bt_enemy_entry_2", ":var_6"),
			(assign, "$bt_enemy_entry_3", ":var_6"),
			(assign, "$bt_enemy_entry_4", ":var_6"),
			(assign, "$bt_enemy_entry_5", ":var_6"),
			(assign, "$bt_enemy_entry_6", ":var_6"),
			(assign, "$bt_enemy_entry_7", ":var_6"),
			(assign, "$bt_enemy_entry_8", ":var_6"),
			(assign, "$bt_enemy_entry_9", ":var_6"),
			(assign, "$player_retreat_entry_begin", ":var_5"),
			(assign, "$player_retreat_entry_end", ":var_5"),
			(assign, "$enemy_retreat_entry_begin", ":var_6"),
			(assign, "$enemy_retreat_entry_end", ":var_6"),
			(assign, "$player_outer_entry_1", ":var_5"),
			(assign, "$player_outer_entry_2", ":var_5"),
			(assign, "$player_outer_entry_3", ":var_5"),
			(assign, "$player_outer_entry_4", ":var_5"),
			(assign, "$player_outer_entry_5", ":var_5"),
			(assign, "$player_outer_entry_6", ":var_5"),
			(assign, "$enemy_outer_entry_1", ":var_6"),
			(assign, "$enemy_outer_entry_2", ":var_6"),
			(assign, "$enemy_outer_entry_3", ":var_6"),
			(assign, "$enemy_outer_entry_4", ":var_6"),
			(assign, "$enemy_outer_entry_5", ":var_6"),
			(assign, "$enemy_outer_entry_6", ":var_6"),
			(assign, "$player_start_entry", ":var_5"),
			(assign, "$enemy_start_entry", ":var_6"),
			(call_script, "script_rand_glob_dice"),
			(change_screen_mission)
		], ".")
	]
	),

	("sexual_report", 0, "^Sexual desire : {reg11}/100^Sexual intercourse : {reg12}^Prostitution : {reg13}^Rape (or raped) : {reg14}^Lady : {reg18}/{reg19}^Lord : {reg16}/{reg17}^Blow job : {reg20}^Virgin Break : {reg15}^First partner : {s5}",
"none",
	[
		(set_background_mesh, "mesh_pic_meetlady2"),
		(try_begin),
			(troop_slot_eq, "trp_player", slot_troop_last_persuasion_time, 0),
			(gt, "$Virgin_breaker", 0),
			(str_store_troop_name, 5, "$Virgin_breaker"),
		(else_try),
			(troop_slot_eq, "trp_player", slot_troop_last_persuasion_time, 0),
			(str_store_string, 5, "str_s_state_unkown"),
		(else_try),
			(troop_slot_eq, "trp_player", slot_troop_last_persuasion_time, 1),
			(str_store_string, 5, "str_s_state_notyet"),
		(try_end),
		(assign, reg11, "$Sexual_desire"),
		(assign, reg12, "$Sex_num"),
		(assign, reg13, "$Meruru_num"),
		(assign, reg14, "$Rape_num"),
		(assign, reg15, "$virgin_break"),
		(assign, ":var_1", 0),
		(assign, ":var_2", 0),
		(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
			(try_begin),
				(troop_slot_eq, ":troop", slot_troop_last_comment_time, 74),
				(val_add, ":var_1", 1),
			(try_end),
			(val_add, ":var_2", 1),
		(try_end),
		(assign, reg16, ":var_1"),
		(assign, reg17, ":var_2"),
		(assign, ":var_4", 0),
		(assign, ":var_5", 0),
		(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(try_begin),
				(troop_slot_eq, ":troop", slot_troop_last_comment_time, 74),
				(val_add, ":var_5", 1),
			(try_end),
			(val_add, ":var_4", 1),
		(try_end),
		(assign, reg18, ":var_5"),
		(assign, reg19, ":var_4"),
		(assign, reg20, "$Sex_num_blow")
	],
	[
		("back",
		[],
		"[Back]",
		[
			(jump_to_menu, "mnu_reports")
		], ".")
	]
	),

	("wm_option_menu", 0, "Option menu",
"none",
	[
		(set_background_mesh, "mesh_pic_camp")
	],
	[
		("back",
		[],
		"[Back]",
		[
			(jump_to_menu, "mnu_reports")
		], ".")
	]
	),

	("mess_we_know", 0, "You have found an odd piece of paper in your pockets. You have no recollection of how it got there.",
"none",
	[
		(set_background_mesh, "mesh_pic_weknow")
	],
	[
		("continue",
		[],
		"Continue.",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

		("we_know_assassination", 0, "You wake up with a start. Black-clad men are approaching!",
"none",
	[
		(set_background_mesh, "mesh_pic_weknow")
	],
	[
		("assassination",
		[],
		"Continue.",
		[
			(assign, ":var_1", "scn_camp_assassination"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(assign, ":value", 0),
			(try_begin),
				(this_or_next|party_slot_eq, "$last_visit_town", slot_town_claimed_by_player, 8),
				(this_or_next|party_slot_eq, "$last_visit_town", slot_town_claimed_by_player, 9),
				(this_or_next|party_slot_eq, "$last_visit_town", slot_town_claimed_by_player, 10),
				(this_or_next|party_slot_eq, "$last_visit_town", slot_town_claimed_by_player, 11),
				(this_or_next|party_slot_eq, "$last_visit_town", slot_town_claimed_by_player, 12),
				(this_or_next|party_slot_eq, "$last_visit_town", slot_town_claimed_by_player, 13),
				(party_slot_eq, "$last_visit_town", slot_town_claimed_by_player, 15),
				(assign, ":value", 1),
			(try_end),
			(try_begin),
				(eq, ":value", 1),
				(troop_slot_eq, "trp_tt_lady_ex_12", 15, 0),
				(neg|troop_slot_ge, "trp_player", 13, 0),
				(set_visitor, 1, "trp_jj_a_5_2"),
				(set_visitor, 3, "trp_tt_lady_ex_12"),
			(else_try),
				(eq, ":value", 1),
				(set_visitor, 1, "trp_jj_a_5_2"),
				(set_visitor, 3, "trp_jj_a_5_2"),
			(else_try),
				(troop_slot_eq, "trp_npc14", 15, 0),
				(neg|troop_slot_ge, "trp_player", 13, 0),
				(set_visitor, 1, "trp_ww_a_5_2"),
				(set_visitor, 3, "trp_npc14"),
			(else_try),
				(set_visitor, 1, "trp_ww_a_5_2"),
				(set_visitor, 3, "trp_ww_a_5_2"),
			(try_end),
			(try_begin),
				(call_script, "script_wm_main_party_has_troop_sc", "trp_npc14"),
				(eq, "$wm_comp_continue", 1),
				(set_visitor, 10, "trp_npc14"),
			(else_try),
				(call_script, "script_wm_main_party_has_troop_sc", "trp_tt_lady_ex_12"),
				(eq, "$wm_comp_continue", 1),
				(set_visitor, 10, "trp_tt_lady_ex_12"),
			(try_end),
			(set_jump_mission, "mt_camp_assassination"),
			(assign, "$current_mission_template", "mt_camp_assassination"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], ".")
	]
	),

	("molda_map_talk", 0, "      ",
"none",
	[
		(try_begin),
			(gt, "$molda_start_map_conversation", 0),
			(call_script, "script_setup_troop_meeting", "$molda_start_map_conversation", -1),
			(assign, "$molda_start_map_conversation", -1),
		(else_try),
			(le, "$molda_start_map_conversation", 0),
			(assign, "$molda_start_map_conversation", -1),
			(jump_to_menu, "mnu_wm_pst_map_return"),
		(try_end)
	],
	[]
	),

	("wm_quest_menu", 0, "{s17}",
"none",
	[
		(assign, "$attempt_coup", 0),
		(assign, "$molda_siege_type", 0),
		(assign, "$player_has_ally", 0),
		(assign, "$enemy_has_ally", 0),
		(assign, "$wm_duel_won", 0),
		(assign, "$wm_battle_result_state", 0),
		(assign, ":value", 0),
		(try_begin),
			(this_or_next|eq, "$wm_quest_result", 1),
			(eq, "$wm_quest_result", 2),
			(this_or_next|party_slot_eq, "$g_encountered_party", 15, 29),
			(this_or_next|party_slot_eq, "$g_encountered_party", 15, 27),
			(this_or_next|party_slot_eq, "$g_encountered_party", 15, 28),
			(this_or_next|party_slot_eq, "$g_encountered_party", 15, 41),
			(party_slot_eq, "$g_encountered_party", 15, 40),
			(call_script, "script_dead_num_slot_process"),
			(store_sub, ":value_2", "$count_player_team", "$troop_alive_player"),
			(val_mul, ":value_2", 100),
			(val_div, ":value_2", "$count_player_team"),
			(store_sub, ":value_3", 100, ":value_2"),
			(val_add, ":value_3", 10),
			(try_begin),
				(gt, ":value_3", 100),
				(assign, ":value_3", 100),
			(try_end),
			(try_begin),
				(lt, ":value_3", 0),
				(assign, ":value_3", 0),
			(try_end),
			(call_script, "script_party_army_size_execute", "p_main_party", ":value_3", 3),
		(try_end),
		(try_begin),
			(eq, "$wm_quest_result", 1),
			(set_background_mesh, "mesh_st_pic_mount"),
			(assign, reg17, "$wm_quest_reward_btexp"),
			(assign, reg18, "$wm_quest_reward_money"),
			(play_sound, "snd_quest_succeeded"),
			(try_begin),
				(neq, "$wm_quest_reward_honor", 0),
				(call_script, "script_wm_honor_change_diff", "trp_player", "$wm_quest_reward_honor", 87),
				(call_script, "script_town_relation_diff", "$g_encountered_party", "$wm_quest_reward_honor"),
			(try_end),
			(try_begin),
				(lt, "$wm_quest_reward_honor", 0),
				(store_random_in_range, ":random_in_range_0_40", 0, 40),
				(eq, ":random_in_range_0_40", 0),
				(assign, "$dark_quest_we_know", 1),
				(display_message, "str_we_know_start"),
			(try_end),
			(try_begin),
				(gt, "$wm_quest_reward_btexp", 0),
				(store_sub, ":value_4", "$wm_quest_reward_btexp", 2),
				(call_script, "script_exp_reward_for_common_troop", ":value_4"),
				(call_script, "script_battle_exp_diff", "$wm_quest_reward_btexp", 87),
				(call_script, "script_adv_exp_diff", 100, 87),
				(call_script, "script_wm_after_battle_progress", 500),
			(else_try),
				(gt, "$wm_quest_reward_btexp", 0),
				(call_script, "script_exp_reward_for_common_troop", "$wm_quest_reward_btexp"),
				(call_script, "script_wm_after_battle_progress", 250),
				(call_script, "script_adv_exp_diff", "$wm_quest_reward_btexp", 87),
			(try_end),
			(try_begin),
				(gt, "$wm_quest_reward_money", 0),
				(assign, ":var_6", "$wm_quest_reward_money"),
				(try_begin),
					(lt, "$wm_quest_reward_honor", 0),
					(eq, "$r_player_class", 4),
					(val_mul, ":var_6", 2),
				(try_end),
				(call_script, "script_party_money_level_diff", "p_main_party", ":var_6", 87),
				(try_begin),
					(neq, "$wm_quest_reward_honor", 0),
					(gt, ":var_6", 0),
					(val_div, ":var_6", 2),
					(add_xp_to_troop, ":var_6", "trp_player"),
				(try_end),
			(try_end),
			(assign, "$wm_quest_reward_honor", 0),
			(assign, "$wm_quest_reward_btexp", 0),
			(assign, "$wm_quest_reward_money", 0),
			(assign, "$wm_quest_reward_debt", 0),
			(str_store_string, 17, "$wm_quest_end_string_succ"),
			(assign, "$wm_quest_mission_anti_skip_menu", 0),
			(party_set_slot, "$g_encountered_party", 15, 0),
			(assign, "$wm_quest_result", 0),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 8),
				(party_set_slot, "$g_encountered_party", slot_town_merchant, 0),
				(party_set_slot, "$g_encountered_party", 15, 0),
				(party_set_flags, "$g_encountered_party", 256, 1),
			(try_end),
		(else_try),
			(eq, "$wm_quest_result", 2),
			(set_background_mesh, "mesh_st_pic_mount"),
			(assign, reg19, "$wm_quest_reward_debt"),
			(play_sound, "snd_quest_failed"),
			(try_begin),
				(gt, "$wm_quest_reward_honor", 0),
				(call_script, "script_wm_honor_change_diff", "trp_player", "$wm_quest_reward_honor", 34),
			(try_end),
			(try_begin),
				(gt, "$wm_quest_reward_debt", 0),
				(call_script, "script_party_money_level_diff", "p_main_party", "$wm_quest_reward_debt", 34),
			(try_end),
			(assign, "$wm_quest_reward_honor", 0),
			(assign, "$wm_quest_reward_btexp", 0),
			(assign, "$wm_quest_reward_money", 0),
			(assign, "$wm_quest_reward_debt", 0),
			(str_store_string, 17, "$wm_quest_end_string_fail"),
			(assign, "$wm_quest_mission_anti_skip_menu", 0),
			(party_set_slot, "$g_encountered_party", 15, 0),
			(assign, "$wm_quest_result", 0),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 8),
				(party_set_slot, "$g_encountered_party", slot_town_merchant, 0),
				(party_set_slot, "$g_encountered_party", 15, 0),
				(party_set_flags, "$g_encountered_party", 256, 1),
			(try_end),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 23),
			(assign, "$wm_quest_reward_honor", 1),
			(assign, "$wm_quest_reward_btexp", 50),
			(store_mul, "$wm_quest_reward_money", 300, 7),
			(assign, "$wm_quest_reward_debt", 0),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_01"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_01"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_prisoner_fem"),
			(str_store_string, 17, "str_wm_qst_text_menu_01"),
			(assign, ":value", 1),
			(auto_save),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 21),
			(assign, "$wm_quest_reward_honor", 1),
			(assign, "$wm_quest_reward_btexp", 50),
			(store_mul, "$wm_quest_reward_money", 300, 8),
			(assign, "$wm_quest_reward_debt", 0),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_01"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_01"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_bandits"),
			(str_store_string, 17, "str_wm_qst_text_menu_02"),
			(assign, ":value", 1),
			(auto_save),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 22),
			(assign, "$wm_quest_reward_honor", 1),
			(assign, "$wm_quest_reward_btexp", 50),
			(store_mul, "$wm_quest_reward_money", 300, 8),
			(assign, "$wm_quest_reward_debt", 0),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_01"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_01"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_sea_raiders"),
			(str_store_string, 17, "str_wm_qst_text_menu_03"),
			(assign, ":value", 1),
			(auto_save),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 25),
			(assign, "$wm_quest_reward_honor", 1),
			(assign, "$wm_quest_reward_btexp", 50),
			(store_mul, "$wm_quest_reward_money", 300, 7),
			(assign, "$wm_quest_reward_debt", 500),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_01"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_01"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_mountain_bandits"),
			(str_store_string, 17, "str_wm_qst_text_menu_04"),
			(assign, ":value", 1),
			(auto_save),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 6),
			(assign, "$wm_quest_reward_honor", 2),
			(assign, "$wm_quest_reward_btexp", 100),
			(store_mul, "$wm_quest_reward_money", 500, 10),
			(assign, "$wm_quest_reward_debt", 0),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_01"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_01"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_siege_sighted"),
			(str_store_string, 17, "str_wm_qst_text_menu_05"),
			(assign, ":value", 1),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 2),
			(assign, "$wm_quest_reward_honor", 1),
			(assign, "$wm_quest_reward_btexp", 50),
			(store_mul, "$wm_quest_reward_money", 300, 8),
			(assign, "$wm_quest_reward_debt", 300),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_auto_01"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_auto_01"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_town1"),
			(str_store_string, 17, "str_wm_qst_text_menu_07"),
			(assign, ":value", 1),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 31),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_village_p"),
			(str_store_string, 17, "str_wm_qst_text_menu_08"),
			(assign, ":value", 0),
			(auto_save),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 30),
			(assign, "$wm_quest_reward_honor", 5),
			(assign, "$wm_quest_reward_btexp", 100),
			(store_mul, "$wm_quest_reward_money", 1000, 7),
			(assign, "$wm_quest_reward_debt", 0),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_01"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_01"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_wounded_fem"),
			(str_store_string, 17, "str_wm_qst_text_menu_19"),
			(assign, ":value", 1),
			(auto_save),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 7),
			(assign, "$wm_quest_reward_honor", -2),
			(assign, "$wm_quest_reward_btexp", 0),
			(store_mul, "$wm_quest_reward_money", 300, 6),
			(assign, "$wm_quest_reward_debt", 300),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_02"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_02"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_meetlady3"),
			(str_store_string, 17, "str_wm_qst_text_menu_09"),
			(assign, ":value", 2),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 1),
			(assign, "$wm_quest_reward_honor", -2),
			(assign, "$wm_quest_reward_btexp", 0),
			(store_mul, "$wm_quest_reward_money", 300, 4),
			(assign, "$wm_quest_reward_debt", 300),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_02"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_02"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_meetlady2"),
			(str_store_string, 17, "str_wm_qst_text_menu_10"),
			(assign, ":value", 2),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 8),
			(assign, "$wm_quest_reward_honor", -1),
			(assign, "$wm_quest_reward_btexp", 0),
			(store_mul, "$wm_quest_reward_money", 300, 4),
			(assign, "$wm_quest_reward_debt", 300),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_02"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_02"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_meetlady"),
			(str_store_string, 17, "str_wm_qst_text_menu_11"),
			(assign, ":value", 2),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 4),
			(assign, "$wm_quest_reward_honor", -2),
			(assign, "$wm_quest_reward_btexp", 100),
			(store_mul, "$wm_quest_reward_money", 500, 5),
			(assign, "$wm_quest_reward_debt", 0),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_02"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_02"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_escape_1_fem"),
			(str_store_string, 17, "str_wm_qst_text_menu_13"),
			(assign, ":value", 2),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 5),
			(assign, "$wm_quest_reward_honor", -2),
			(assign, "$wm_quest_reward_btexp", 0),
			(store_mul, "$wm_quest_reward_money", 1000, 6),
			(assign, "$wm_quest_reward_debt", 0),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_02"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_02"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_weknow"),
			(str_store_string, 17, "str_wm_qst_text_menu_15"),
			(assign, ":value", 2),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 3),
			(assign, "$wm_quest_reward_honor", -1),
			(assign, "$wm_quest_reward_btexp", 100),
			(store_mul, "$wm_quest_reward_money", 500, 6),
			(assign, "$wm_quest_reward_debt", 500),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_02"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_02"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_towndes"),
			(str_store_string, 17, "str_wm_qst_text_menu_16"),
			(assign, ":value", 2),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 27),
			(assign, "$wm_quest_reward_honor", 1),
			(assign, "$wm_quest_reward_btexp", 100),
			(val_add, "$wm_quest_reward_btexp", 20),
			(store_mul, "$wm_quest_reward_money", 1000, 10),
			(assign, "$wm_quest_reward_debt", 1500),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_01"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_01"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_townriot"),
			(str_store_string, 17, "str_wm_qst_text_menu_17"),
			(assign, ":value", 1),
			(auto_save),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 28),
			(assign, "$wm_quest_reward_honor", 2),
			(assign, "$wm_quest_reward_btexp", 100),
			(val_add, "$wm_quest_reward_btexp", 20),
			(store_mul, "$wm_quest_reward_money", 1000, 10),
			(assign, "$wm_quest_reward_debt", 1500),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_01"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_01"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_looted_village"),
			(str_store_string, 17, "str_wm_qst_text_menu_18"),
			(assign, ":value", 1),
			(auto_save),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 29),
			(assign, "$wm_quest_reward_honor", 1),
			(assign, "$wm_quest_reward_btexp", 100),
			(val_add, "$wm_quest_reward_btexp", 20),
			(store_mul, "$wm_quest_reward_money", 1000, 10),
			(assign, "$wm_quest_reward_debt", 1500),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_01"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_01"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_pic_steppe_bandits"),
			(str_store_string, 17, "str_wm_qst_text_menu_20"),
			(assign, ":value", 1),
			(auto_save),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 40),
			(assign, "$wm_quest_reward_honor", 2),
			(assign, "$wm_quest_reward_btexp", 70),
			(store_mul, "$wm_quest_reward_money", 1000, 6),
			(assign, "$wm_quest_reward_debt", 500),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_03"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_03"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_encounter5pirate"),
			(str_store_string, 17, "str_wm_qst_text_menu_30"),
			(assign, ":value", 0),
			(auto_save),
		(else_try),
			(party_slot_eq, "$g_encountered_party", 15, 41),
			(assign, "$wm_quest_reward_honor", -2),
			(assign, "$wm_quest_reward_btexp", 70),
			(store_mul, "$wm_quest_reward_money", 1000, 5),
			(assign, "$wm_quest_reward_debt", 0),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_03"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_03"),
			(assign, reg8, "$wm_quest_reward_money"),
			(set_background_mesh, "mesh_st_pic_sea"),
			(str_store_string, 17, "str_wm_qst_text_menu_31"),
			(assign, ":value", 0),
			(auto_save),
		(try_end),
		(try_begin),
			(gt, ":value", 0),
			(call_script, "script_wm_every_global_sett_depend_faction", "$g_encountered_party"),
			(set_fixed_point_multiplier, 1000),
			(position_set_x, 0, 600),
			(position_set_y, 0, 400),
			(position_set_z, 0, 750),
			(try_begin),
				(eq, ":value", 1),
				(assign, ":value_5", "$wm_npc_light_guild_npc"),
			(else_try),
				(assign, ":value_5", "$wm_npc_dark_guild_npc"),
			(try_end),
			(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", ":value_5", 0),
		(try_end),
		(try_begin),
			(eq, "$auto_event_enter", 1),
			(assign, "$wm_talk_state", 0),
			(call_script, "script_molda_scene_culture", "$g_encountered_party"),
			(assign, ":var_8", "$town_scene_tavern"),
			(set_jump_mission, "mt_kill_druken_thug"),
			(assign, "$current_mission_template", "mt_kill_druken_thug"),
			(jump_to_scene, ":var_8"),
			(modify_visitors_at_site, ":var_8"),
			(reset_visitors),
			(call_script, "script_wm_every_global_sett_depend_faction", "$g_encountered_party"),
			(set_visitor, 9, "$wm_npc_tavernkeeper"),
			(assign, ":var_9", 17),
			(try_begin),
				(set_visitors, ":var_9", "trp_raid_bandit_brigand", 4),
			(try_end),
			(change_screen_mission),
			(assign, "$auto_event_enter", 0),
		(try_end)
	],
	[
		("protect_caravan",
		[
			(party_slot_eq, "$g_encountered_party", 15, 25),
				#####Terrain Detector Begin Range SP ALL.
	#####MUSICBOX
	(try_begin),
	(eq, "$additional_music", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
	(music_set_situation, mtf_sit_encounter_hostile),
	#(play_track, "track_silence", 1), #Stop module track.
	##(stop_all_sounds, 1), #Used to be value of 1
	(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
	(try_begin),
	(this_or_next|eq, ":current_terrain_main_party", rt_mountain),
	(this_or_next|eq, ":current_terrain_main_party", rt_steppe),
	(eq, ":current_terrain_main_party", rt_steppe_forest),
	(store_random_in_range, ":random_steppe", 1, 6),
	(try_begin),
	(eq, ":random_steppe", 1),
	(play_track, "track_medm1", 1),
	(else_try),
	(eq, ":random_steppe", 2),
	(play_track, "track_medm2", 1),
	(else_try),
	(eq, ":random_steppe", 3),
	(play_track, "track_medm3", 1),
	(else_try),
	(eq, ":random_steppe", 4),
	(play_track, "track_medm4", 1),
	(else_try),
	(eq, ":random_steppe", 5),
	(play_track, "track_medm5", 1),
	(try_end),
	
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_plain),
	(this_or_next|eq, ":current_terrain_main_party", rt_forest),
	(eq, ":current_terrain_main_party", rt_mountain_forest),
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow_forest),
	(eq, ":current_terrain_main_party", rt_bridge), #No idea
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_desert),
	(eq, ":current_terrain_main_party", rt_desert_forest),
	(store_random_in_range, ":random_arab", 1, 7),
	(try_begin),
	(eq, ":random_arab", 1),
	(play_track, "track_arabt1", 1),
	(else_try),
		(eq, ":random_arab", 2),
	(play_track, "track_arabt2", 1),
	(else_try),
		(eq, ":random_arab", 3),
	(play_track, "track_arabt3", 1),
	(else_try),
		(eq, ":random_arab", 4),
	(play_track, "track_arabt4", 1),
	(else_try),
		(eq, ":random_arab", 5),
	(play_track, "track_arabt5", 1),
	(else_try),
		(eq, ":random_arab", 6),
	(play_track, "track_arabt6", 1),
	(try_end),
	(try_end),
	(try_end),
	
	#####Terrain Detector End Range SP ALL.
		],
		"(+)Protect caravan.",
		[
			(assign, "$wm_talk_state", 0),
			(assign, ":var_1", "scn_protect_caravan"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 1, "trp_raid_bandit_boss_mounted"),
			(set_visitor, 0, "trp_player"),
			(set_jump_mission, "mt_protect_caravan"),
			(assign, "$current_mission_template", "mt_protect_caravan"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("attack_caravan",
		[
			(party_slot_eq, "$g_encountered_party", 15, 25),
				#####Terrain Detector Begin Range SP ALL.
	#####MUSICBOX
	(try_begin),
	(eq, "$additional_music", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
	(music_set_situation, mtf_sit_encounter_hostile),
	#(play_track, "track_silence", 1), #Stop module track.
	##(stop_all_sounds, 1), #Used to be value of 1
	(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
	(try_begin),
	(this_or_next|eq, ":current_terrain_main_party", rt_mountain),
	(this_or_next|eq, ":current_terrain_main_party", rt_steppe),
	(eq, ":current_terrain_main_party", rt_steppe_forest),
	(store_random_in_range, ":random_steppe", 1, 6),
	(try_begin),
	(eq, ":random_steppe", 1),
	(play_track, "track_medm1", 1),
	(else_try),
	(eq, ":random_steppe", 2),
	(play_track, "track_medm2", 1),
	(else_try),
	(eq, ":random_steppe", 3),
	(play_track, "track_medm3", 1),
	(else_try),
	(eq, ":random_steppe", 4),
	(play_track, "track_medm4", 1),
	(else_try),
	(eq, ":random_steppe", 5),
	(play_track, "track_medm5", 1),
	(try_end),
	
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_plain),
	(this_or_next|eq, ":current_terrain_main_party", rt_forest),
	(eq, ":current_terrain_main_party", rt_mountain_forest),
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow_forest),
	(eq, ":current_terrain_main_party", rt_bridge), #No idea
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_desert),
	(eq, ":current_terrain_main_party", rt_desert_forest),
	(store_random_in_range, ":random_arab", 1, 7),
	(try_begin),
	(eq, ":random_arab", 1),
	(play_track, "track_arabt1", 1),
	(else_try),
		(eq, ":random_arab", 2),
	(play_track, "track_arabt2", 1),
	(else_try),
		(eq, ":random_arab", 3),
	(play_track, "track_arabt3", 1),
	(else_try),
		(eq, ":random_arab", 4),
	(play_track, "track_arabt4", 1),
	(else_try),
		(eq, ":random_arab", 5),
	(play_track, "track_arabt5", 1),
	(else_try),
		(eq, ":random_arab", 6),
	(play_track, "track_arabt6", 1),
	(try_end),
	(try_end),
	(try_end),
	
	#####Terrain Detector End Range SP ALL.
		],
		"(-)Attack the caravan.",
		[
			(party_set_slot, "$g_encountered_party", 15, 26),
			(assign, "$wm_quest_reward_honor", -1),
			(assign, "$wm_quest_reward_btexp", 50),
			(store_mul, "$wm_quest_reward_money", 300, 8),
			(assign, "$wm_quest_reward_debt", 0),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_02"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_02"),
			(assign, "$wm_talk_state", 0),
			(assign, ":var_1", "scn_protect_caravan"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(store_random_in_range, ":random_in_range_0_10", 0, 10),
			(try_begin),
				(eq, ":random_in_range_0_10", 0),
				(set_visitor, 0, "trp_adventurer_3"),
			(else_try),
				(this_or_next|eq, ":random_in_range_0_10", 1),
				(this_or_next|eq, ":random_in_range_0_10", 2),
				(eq, ":random_in_range_0_10", 3),
				(set_visitor, 0, "trp_adventurer_2"),
			(else_try),
				(set_visitor, 0, "trp_adventurer_1"),
			(try_end),
			(set_visitor, 1, "trp_player"),
			(set_jump_mission, "mt_protect_caravan"),
			(assign, "$current_mission_template", "mt_protect_caravan"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("duelist",
		[
			(party_slot_eq, "$g_encountered_party", 15, 6),
				#####Terrain Detector Begin Range SP ALL.
	#####MUSICBOX
	(try_begin),
	(eq, "$additional_music", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
	(music_set_situation, mtf_sit_encounter_hostile),
	#(play_track, "track_silence", 1), #Stop module track.
	##(stop_all_sounds, 1), #Used to be value of 1
	(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
	(try_begin),
	(this_or_next|eq, ":current_terrain_main_party", rt_mountain),
	(this_or_next|eq, ":current_terrain_main_party", rt_steppe),
	(eq, ":current_terrain_main_party", rt_steppe_forest),
	(store_random_in_range, ":random_steppe", 1, 6),
	(try_begin),
	(eq, ":random_steppe", 1),
	(play_track, "track_medm1", 1),
	(else_try),
	(eq, ":random_steppe", 2),
	(play_track, "track_medm2", 1),
	(else_try),
	(eq, ":random_steppe", 3),
	(play_track, "track_medm3", 1),
	(else_try),
	(eq, ":random_steppe", 4),
	(play_track, "track_medm4", 1),
	(else_try),
	(eq, ":random_steppe", 5),
	(play_track, "track_medm5", 1),
	(try_end),
	
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_plain),
	(this_or_next|eq, ":current_terrain_main_party", rt_forest),
	(eq, ":current_terrain_main_party", rt_mountain_forest),
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow_forest),
	(eq, ":current_terrain_main_party", rt_bridge), #No idea
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_desert),
	(eq, ":current_terrain_main_party", rt_desert_forest),
	(store_random_in_range, ":random_arab", 1, 7),
	(try_begin),
	(eq, ":random_arab", 1),
	(play_track, "track_arabt1", 1),
	(else_try),
		(eq, ":random_arab", 2),
	(play_track, "track_arabt2", 1),
	(else_try),
		(eq, ":random_arab", 3),
	(play_track, "track_arabt3", 1),
	(else_try),
		(eq, ":random_arab", 4),
	(play_track, "track_arabt4", 1),
	(else_try),
		(eq, ":random_arab", 5),
	(play_track, "track_arabt5", 1),
	(else_try),
		(eq, ":random_arab", 6),
	(play_track, "track_arabt6", 1),
	(try_end),
	(try_end),
	(try_end),
	
	#####Terrain Detector End Range SP ALL.
		],
		"(+)Start Duel.",
		[
			(assign, "$wm_duel_persnal", 0),
			(assign, "$wm_battle_result_state", 0),
			(assign, "$wm_duel_won", 0),
			(assign, "$wm_talk_state", 0),
			(assign, "$wm_quest_mission_anti_skip_menu", 1),
			(assign, "$molda_start_map_conversation", -1),
			(call_script, "script_molda_scene_culture", "$g_encountered_party"),
			(assign, ":var_1", "$town_scene_arena"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(store_random_in_range, ":random_in_range_0_10", 0, 10),
			(try_begin),
				(this_or_next|eq, "$start_age", 1573),
				(eq, "$start_age", 0),
				(party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 8),
				(troop_slot_eq, "trp_npc13", 15, 0),
				(set_visitor, 41, "trp_npc13"),
			(else_try),
				(eq, ":random_in_range_0_10", 0),
				(set_visitor, 41, "trp_adventurer_3"),
			(else_try),
				(this_or_next|eq, ":random_in_range_0_10", 1),
				(this_or_next|eq, ":random_in_range_0_10", 2),
				(eq, ":random_in_range_0_10", 3),
				(set_visitor, 41, "trp_adventurer_2"),
			(else_try),
				(set_visitor, 41, "trp_adventurer_1"),
			(try_end),
			(set_visitor, 0, "trp_player"),
			(set_jump_mission, "mt_arena_mission"),
			(assign, "$current_mission_template", "mt_arena_mission"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("subdue_pirate",
		[
			(party_slot_eq, "$g_encountered_party", 15, 40),
				#####Terrain Detector Begin Range SP ALL.
	#####MUSICBOX
	(try_begin),
	(eq, "$additional_music", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
	(music_set_situation, mtf_sit_encounter_hostile),
	#(play_track, "track_silence", 1), #Stop module track.
	##(stop_all_sounds, 1), #Used to be value of 1
	(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
	(try_begin),
	(this_or_next|eq, ":current_terrain_main_party", rt_mountain),
	(this_or_next|eq, ":current_terrain_main_party", rt_steppe),
	(eq, ":current_terrain_main_party", rt_steppe_forest),
	(store_random_in_range, ":random_steppe", 1, 6),
	(try_begin),
	(eq, ":random_steppe", 1),
	(play_track, "track_medm1", 1),
	(else_try),
	(eq, ":random_steppe", 2),
	(play_track, "track_medm2", 1),
	(else_try),
	(eq, ":random_steppe", 3),
	(play_track, "track_medm3", 1),
	(else_try),
	(eq, ":random_steppe", 4),
	(play_track, "track_medm4", 1),
	(else_try),
	(eq, ":random_steppe", 5),
	(play_track, "track_medm5", 1),
	(try_end),
	
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_plain),
	(this_or_next|eq, ":current_terrain_main_party", rt_forest),
	(eq, ":current_terrain_main_party", rt_mountain_forest),
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow_forest),
	(eq, ":current_terrain_main_party", rt_bridge), #No idea
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_desert),
	(eq, ":current_terrain_main_party", rt_desert_forest),
	(store_random_in_range, ":random_arab", 1, 7),
	(try_begin),
	(eq, ":random_arab", 1),
	(play_track, "track_arabt1", 1),
	(else_try),
		(eq, ":random_arab", 2),
	(play_track, "track_arabt2", 1),
	(else_try),
		(eq, ":random_arab", 3),
	(play_track, "track_arabt3", 1),
	(else_try),
		(eq, ":random_arab", 4),
	(play_track, "track_arabt4", 1),
	(else_try),
		(eq, ":random_arab", 5),
	(play_track, "track_arabt5", 1),
	(else_try),
		(eq, ":random_arab", 6),
	(play_track, "track_arabt6", 1),
	(try_end),
	(try_end),
	(try_end),
	
	#####Terrain Detector End Range SP ALL.
		],
		"(+)Attack the pirates.",
		[
			(assign, "$wm_quest_mission_anti_skip_menu", 1),
			(call_script, "script_party_count_fit_for_battle", "p_main_party"),
			(assign, "$player_army_size", reg0),
			(store_random_in_range, "$enemy_army_size", 1000, 1500),
			(assign, "$wm_target_party", "$g_encountered_party"),
			(call_script, "script_sea_battle_setting")
		], "."),

		("attack_sea_trader",
		[
			(party_slot_eq, "$g_encountered_party", 15, 41),
				#####Terrain Detector Begin Range SP ALL.
	#####MUSICBOX
	(try_begin),
	(eq, "$additional_music", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
	(music_set_situation, mtf_sit_encounter_hostile),
	#(play_track, "track_silence", 1), #Stop module track.
	##(stop_all_sounds, 1), #Used to be value of 1
	(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
	(try_begin),
	(this_or_next|eq, ":current_terrain_main_party", rt_mountain),
	(this_or_next|eq, ":current_terrain_main_party", rt_steppe),
	(eq, ":current_terrain_main_party", rt_steppe_forest),
	(store_random_in_range, ":random_steppe", 1, 6),
	(try_begin),
	(eq, ":random_steppe", 1),
	(play_track, "track_medm1", 1),
	(else_try),
	(eq, ":random_steppe", 2),
	(play_track, "track_medm2", 1),
	(else_try),
	(eq, ":random_steppe", 3),
	(play_track, "track_medm3", 1),
	(else_try),
	(eq, ":random_steppe", 4),
	(play_track, "track_medm4", 1),
	(else_try),
	(eq, ":random_steppe", 5),
	(play_track, "track_medm5", 1),
	(try_end),
	
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_plain),
	(this_or_next|eq, ":current_terrain_main_party", rt_forest),
	(eq, ":current_terrain_main_party", rt_mountain_forest),
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow_forest),
	(eq, ":current_terrain_main_party", rt_bridge), #No idea
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_desert),
	(eq, ":current_terrain_main_party", rt_desert_forest),
	(store_random_in_range, ":random_arab", 1, 7),
	(try_begin),
	(eq, ":random_arab", 1),
	(play_track, "track_arabt1", 1),
	(else_try),
		(eq, ":random_arab", 2),
	(play_track, "track_arabt2", 1),
	(else_try),
		(eq, ":random_arab", 3),
	(play_track, "track_arabt3", 1),
	(else_try),
		(eq, ":random_arab", 4),
	(play_track, "track_arabt4", 1),
	(else_try),
		(eq, ":random_arab", 5),
	(play_track, "track_arabt5", 1),
	(else_try),
		(eq, ":random_arab", 6),
	(play_track, "track_arabt6", 1),
	(try_end),
	(try_end),
	(try_end),
	
	#####Terrain Detector End Range SP ALL.
		],
		"(-)Attack the sea traders.",
		[
			(assign, "$wm_quest_mission_anti_skip_menu", 1),
			(call_script, "script_party_count_fit_for_battle", "p_main_party"),
			(assign, "$player_army_size", reg0),
			(store_random_in_range, "$enemy_army_size", 500, 700),
			(assign, "$wm_target_party", "$g_encountered_party"),
			(call_script, "script_sea_battle_setting")
		], "."),

		("subdue_barbarian",
		[
			(party_slot_eq, "$g_encountered_party", 15, 28),
				#####Terrain Detector Begin Range SP ALL.
	#####MUSICBOX
	(try_begin),
	(eq, "$additional_music", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
	(music_set_situation, mtf_sit_encounter_hostile),
	#(play_track, "track_silence", 1), #Stop module track.
	##(stop_all_sounds, 1), #Used to be value of 1
	(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
	(try_begin),
	(this_or_next|eq, ":current_terrain_main_party", rt_mountain),
	(this_or_next|eq, ":current_terrain_main_party", rt_steppe),
	(eq, ":current_terrain_main_party", rt_steppe_forest),
	(store_random_in_range, ":random_steppe", 1, 6),
	(try_begin),
	(eq, ":random_steppe", 1),
	(play_track, "track_medm1", 1),
	(else_try),
	(eq, ":random_steppe", 2),
	(play_track, "track_medm2", 1),
	(else_try),
	(eq, ":random_steppe", 3),
	(play_track, "track_medm3", 1),
	(else_try),
	(eq, ":random_steppe", 4),
	(play_track, "track_medm4", 1),
	(else_try),
	(eq, ":random_steppe", 5),
	(play_track, "track_medm5", 1),
	(try_end),
	
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_plain),
	(this_or_next|eq, ":current_terrain_main_party", rt_forest),
	(eq, ":current_terrain_main_party", rt_mountain_forest),
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow_forest),
	(eq, ":current_terrain_main_party", rt_bridge), #No idea
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_desert),
	(eq, ":current_terrain_main_party", rt_desert_forest),
	(store_random_in_range, ":random_arab", 1, 7),
	(try_begin),
	(eq, ":random_arab", 1),
	(play_track, "track_arabt1", 1),
	(else_try),
		(eq, ":random_arab", 2),
	(play_track, "track_arabt2", 1),
	(else_try),
		(eq, ":random_arab", 3),
	(play_track, "track_arabt3", 1),
	(else_try),
		(eq, ":random_arab", 4),
	(play_track, "track_arabt4", 1),
	(else_try),
		(eq, ":random_arab", 5),
	(play_track, "track_arabt5", 1),
	(else_try),
		(eq, ":random_arab", 6),
	(play_track, "track_arabt6", 1),
	(try_end),
	(try_end),
	(try_end),
	
	#####Terrain Detector End Range SP ALL.
		],
		"(+)Attack the Armed Group.",
		[
			(try_begin),
				(assign, "$player_assistant_1", 0),
				(assign, "$enemy_assistant_1", 0),
				(assign, "$enemy_assistant_2", 0),
				(assign, "$wm_talk_state", 0),
				(assign, ":var_1", "scn_rebel_wooden_fort"),
				(modify_visitors_at_site, ":var_1"),
				(reset_visitors),
				(call_script, "script_wm_troop_type_depend_train", "$g_encountered_party", 50),
				(store_random_in_range, ":random_in_range_6_9", 6, 9),
				(assign, ":var_3", ":random_in_range_6_9"),
				(set_visitors, 2, "$temp_party_troop_03", ":var_3"),
				(set_visitors, 3, "$temp_party_troop_02", ":var_3"),
				(set_visitors, 4, "$temp_party_troop_03", ":var_3"),
				(set_visitors, 5, "$temp_party_troop_04", ":var_3"),
				(set_visitors, 6, "$temp_party_troop_03", ":var_3"),
				(set_visitors, 7, "$temp_party_troop_05", ":var_3"),
				(set_visitors, 8, "$temp_party_troop_04", ":var_3"),
				(set_visitors, 9, "$temp_party_troop_02", ":var_3"),
				(set_visitors, 10, "$temp_party_troop_06", ":var_3"),
				(set_visitor, 11, "trp_raid_bandit_boss", 1),
				(set_visitor, 1, "trp_player"),
				(set_jump_mission, "mt_raid_rebel_fort"),
				(assign, "$current_mission_template", "mt_raid_rebel_fort"),
				(jump_to_scene, ":var_1"),
				(change_screen_mission),
			(try_end)
		], "."),

		("raid_rebel_fort",
		[
			(party_slot_eq, "$g_encountered_party", 15, 27),
				#####Terrain Detector Begin Range SP ALL.
	#####MUSICBOX
	(try_begin),
	(eq, "$additional_music", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
	(music_set_situation, mtf_sit_encounter_hostile),
	#(play_track, "track_silence", 1), #Stop module track.
	##(stop_all_sounds, 1), #Used to be value of 1
	(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
	(try_begin),
	(this_or_next|eq, ":current_terrain_main_party", rt_mountain),
	(this_or_next|eq, ":current_terrain_main_party", rt_steppe),
	(eq, ":current_terrain_main_party", rt_steppe_forest),
	(store_random_in_range, ":random_steppe", 1, 6),
	(try_begin),
	(eq, ":random_steppe", 1),
	(play_track, "track_medm1", 1),
	(else_try),
	(eq, ":random_steppe", 2),
	(play_track, "track_medm2", 1),
	(else_try),
	(eq, ":random_steppe", 3),
	(play_track, "track_medm3", 1),
	(else_try),
	(eq, ":random_steppe", 4),
	(play_track, "track_medm4", 1),
	(else_try),
	(eq, ":random_steppe", 5),
	(play_track, "track_medm5", 1),
	(try_end),
	
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_plain),
	(this_or_next|eq, ":current_terrain_main_party", rt_forest),
	(eq, ":current_terrain_main_party", rt_mountain_forest),
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow_forest),
	(eq, ":current_terrain_main_party", rt_bridge), #No idea
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_desert),
	(eq, ":current_terrain_main_party", rt_desert_forest),
	(store_random_in_range, ":random_arab", 1, 7),
	(try_begin),
	(eq, ":random_arab", 1),
	(play_track, "track_arabt1", 1),
	(else_try),
		(eq, ":random_arab", 2),
	(play_track, "track_arabt2", 1),
	(else_try),
		(eq, ":random_arab", 3),
	(play_track, "track_arabt3", 1),
	(else_try),
		(eq, ":random_arab", 4),
	(play_track, "track_arabt4", 1),
	(else_try),
		(eq, ":random_arab", 5),
	(play_track, "track_arabt5", 1),
	(else_try),
		(eq, ":random_arab", 6),
	(play_track, "track_arabt6", 1),
	(try_end),
	(try_end),
	(try_end),
	
	#####Terrain Detector End Range SP ALL.
		],
		"(+)Attack the rebels fort.",
		[
			(try_begin),
				(assign, "$player_assistant_1", 0),
				(assign, "$enemy_assistant_1", 0),
				(assign, "$enemy_assistant_2", 0),
				(assign, ":var_1", "trp_rebels_fort_peasant"),
				(assign, ":var_2", "trp_rebels_fort_leader"),
				(assign, "$wm_talk_state", 0),
				(assign, ":var_3", "scn_rebel_wooden_fort"),
				(modify_visitors_at_site, ":var_3"),
				(reset_visitors),
				(call_script, "script_wm_troop_type_depend_train", "$g_encountered_party", 50),
				(store_random_in_range, ":random_in_range_6_11", 6, 11),
				(assign, ":var_5", ":random_in_range_6_11"),
				(set_visitors, 2, ":var_1", ":var_5"),
				(set_visitors, 3, "$temp_party_troop_02", ":var_5"),
				(set_visitors, 4, "$temp_party_troop_03", ":var_5"),
				(set_visitors, 5, "$temp_party_troop_01", ":var_5"),
				(set_visitors, 6, ":var_1", ":var_5"),
				(set_visitors, 7, "$temp_party_troop_03", ":var_5"),
				(set_visitors, 8, "$temp_party_troop_01", ":var_5"),
				(set_visitors, 9, "$temp_party_troop_02", ":var_5"),
				(set_visitors, 10, ":var_1", ":var_5"),
				(set_visitor, 11, ":var_2", 1),
				(set_visitor, 1, "trp_player"),
				(set_jump_mission, "mt_raid_rebel_fort"),
				(assign, "$current_mission_template", "mt_raid_rebel_fort"),
				(jump_to_scene, ":var_3"),
				(change_screen_mission),
			(try_end)
		], "."),

		("subdue_nomad",
		[
			(party_slot_eq, "$g_encountered_party", 15, 29),
				#####Terrain Detector Begin Range SP ALL.
	#####MUSICBOX
	(try_begin),
	(eq, "$additional_music", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
	(music_set_situation, mtf_sit_encounter_hostile),
	#(play_track, "track_silence", 1), #Stop module track.
	##(stop_all_sounds, 1), #Used to be value of 1
	(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
	(try_begin),
	(this_or_next|eq, ":current_terrain_main_party", rt_mountain),
	(this_or_next|eq, ":current_terrain_main_party", rt_steppe),
	(eq, ":current_terrain_main_party", rt_steppe_forest),
	(store_random_in_range, ":random_steppe", 1, 6),
	(try_begin),
	(eq, ":random_steppe", 1),
	(play_track, "track_medm1", 1),
	(else_try),
	(eq, ":random_steppe", 2),
	(play_track, "track_medm2", 1),
	(else_try),
	(eq, ":random_steppe", 3),
	(play_track, "track_medm3", 1),
	(else_try),
	(eq, ":random_steppe", 4),
	(play_track, "track_medm4", 1),
	(else_try),
	(eq, ":random_steppe", 5),
	(play_track, "track_medm5", 1),
	(try_end),
	
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_plain),
	(this_or_next|eq, ":current_terrain_main_party", rt_forest),
	(eq, ":current_terrain_main_party", rt_mountain_forest),
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow),
	(this_or_next|eq, ":current_terrain_main_party", rt_snow_forest),
	(eq, ":current_terrain_main_party", rt_bridge), #No idea
	(store_random_in_range, ":random_euro", 1, 12),
	(try_begin),
		(eq, ":random_euro", 1),
	(play_track, "track_eurottt1", 1),
	(else_try),
		(eq, ":random_euro", 2),
	(play_track, "track_eurottt2", 1),
	(else_try),
		(eq, ":random_euro", 3),
	(play_track, "track_eurottt3", 1),
	(else_try),
		(eq, ":random_euro", 4),
	(play_track, "track_eurottt4", 1),
	(else_try),
	(eq, ":random_euro", 5),
	(play_track, "track_eurottt5", 1),
	(else_try),
		(eq, ":random_euro", 6),
	(play_track, "track_eurottt6", 1),
	(else_try),
		(eq, ":random_euro", 7),
	(play_track, "track_eurottt7", 1),
	(else_try),
		(eq, ":random_euro", 8),
	(play_track, "track_eurottt8", 1),
	(else_try),
	(eq, ":random_euro", 9),
	(play_track, "track_eurottt9", 1),
	(else_try),
		(eq, ":random_euro", 10),
	(play_track, "track_eurottt10", 1),
	(else_try),
		(eq, ":random_euro", 11),
	(play_track, "track_eurottt11", 1),
	(try_end),
	(else_try),
	(this_or_next|eq, ":current_terrain_main_party", rt_desert),
	(eq, ":current_terrain_main_party", rt_desert_forest),
	(store_random_in_range, ":random_arab", 1, 7),
	(try_begin),
	(eq, ":random_arab", 1),
	(play_track, "track_arabt1", 1),
	(else_try),
		(eq, ":random_arab", 2),
	(play_track, "track_arabt2", 1),
	(else_try),
		(eq, ":random_arab", 3),
	(play_track, "track_arabt3", 1),
	(else_try),
		(eq, ":random_arab", 4),
	(play_track, "track_arabt4", 1),
	(else_try),
		(eq, ":random_arab", 5),
	(play_track, "track_arabt5", 1),
	(else_try),
		(eq, ":random_arab", 6),
	(play_track, "track_arabt6", 1),
	(try_end),
	(try_end),
	(try_end),
	
	#####Terrain Detector End Range SP ALL.
		],
		"(+)Attack the nomad looter.",
		[
			(try_begin),
				(assign, "$player_assistant_1", 0),
				(assign, "$enemy_assistant_1", 0),
				(assign, "$enemy_assistant_2", 0),
				(assign, "$wm_talk_state", 0),
				(call_script, "script_molda_scene_culture", "$g_encountered_party"),
				(assign, ":var_1", "$town_scene_village"),
				(modify_visitors_at_site, ":var_1"),
				(reset_visitors),
				(party_set_slot, "$g_encountered_party", slot_town_center, "fac_kingdom_30"),
				(call_script, "script_wm_troop_type_depend_train", "$g_encountered_party", 100),
				(store_random_in_range, ":random_in_range_5_11", 5, 11),
				(assign, ":var_3", ":random_in_range_5_11"),
				(set_visitors, 2, "$temp_party_troop_01", ":var_3"),
				(set_visitors, 2, "$temp_party_troop_01", ":var_3"),
				(set_visitors, 2, "$temp_party_troop_01", ":var_3"),
				(set_visitors, 2, "$temp_party_troop_02", ":var_3"),
				(set_visitors, 2, "$temp_party_troop_02", ":var_3"),
				(set_visitors, 2, "$temp_party_troop_03", ":var_3"),
				(set_visitors, 2, "$temp_party_troop_04", ":var_3"),
				(set_visitors, 2, "$temp_party_troop_05", ":var_3"),
				(set_visitors, 2, "$temp_party_troop_06", ":var_3"),
				(set_visitor, 1, "trp_player"),
				(set_jump_mission, "mt_subdue_nomad"),
				(assign, "$current_mission_template", "mt_subdue_nomad"),
				(jump_to_scene, ":var_1"),
				(change_screen_mission),
			(try_end)
		], "."),

		("steal_mission",
		[
			(party_slot_eq, "$g_encountered_party", 15, 3)
		],
		"(-)Steal gem.",
		[
			(assign, "$wm_quest_mission_anti_skip_menu", 1),
			(assign, "$wm_talk_state", 4),
			(call_script, "script_molda_scene_culture", "$g_encountered_party"),
			(assign, ":var_1", "$town_scene_type"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(call_script, "script_wm_troop_type_depend_train", "$g_encountered_party", 0),
			(assign, ":var_2", "$temp_party_troop_06"),
			(assign, ":var_3", "$temp_party_troop_06"),
			(assign, ":var_4", "$temp_party_troop_03"),
			(assign, ":var_5", "$temp_party_troop_04"),
			(set_visitor, 23, ":var_3"),
			(set_visitor, 24, ":var_2"),
			(assign, reg0, ":var_5"),
			(assign, reg1, ":var_5"),
			(assign, reg2, ":var_4"),
			(assign, reg3, ":var_4"),
			(shuffle_range, 0, 4),
			(set_visitor, 25, reg0),
			(set_visitor, 26, reg1),
			(set_visitor, 27, reg2),
			(set_visitor, 28, reg3),
			(set_visitor, 42, "$temp_party_troop_03"),
			(set_visitor, 43, "$temp_party_troop_03"),
			(set_visitor, 44, "$temp_party_troop_05"),
			(set_visitor, 45, "$temp_party_troop_05"),
			(call_script, "script_wm_every_global_sett_depend_faction", "$g_encountered_party"),
			(set_visitors, 32, "$wm_npc_walker_m", 2),
			(set_visitors, 33, "$wm_npc_walker_f", 2),
			(set_visitors, 34, "$wm_npc_walker_m", 2),
			(set_visitors, 35, "$wm_npc_walker_f", 2),
			(set_visitors, 36, "$wm_npc_walker_m", 2),
			(set_visitors, 37, "$wm_npc_walker_f", 2),
			(set_visitors, 38, "$wm_npc_walker_m", 2),
			(set_visitors, 39, "$wm_npc_walker_f", 2),
			(set_visitor, 9, "$wm_npc_armorer"),
			(set_visitor, 10, "$wm_npc_merchant"),
			(set_visitor, 11, "$wm_npc_religionist"),
			(try_begin),
				(neg|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 15),
				(neg|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 16),
				(neg|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 17),
				(neg|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 18),
				(neg|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 24),
				(set_visitor, 12, "$wm_npc_horse_merchant"),
			(try_end),
			(set_jump_mission, "mt_town_center"),
			(assign, "$current_mission_template", "mt_town_center"),
			(assign, ":var_6", 256),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 0, ":var_6"),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 2, ":var_6"),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 3, ":var_6"),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 4, ":var_6"),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 5, ":var_6"),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 6, ":var_6"),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 7, ":var_6"),
			(set_jump_entry, 1),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("assassinate_mission_start",
		[
			(party_slot_eq, "$g_encountered_party", 15, 5)
		],
		"(-)Sniping. Aim the lower body.",
		[
			(assign, "$assassinate_arrow_chance", 3),
			(assign, "$assassinate_witness", 0),
			(assign, "$wm_quest_mission_anti_skip_menu", 1),
			(assign, "$wm_talk_state", 4),
			(call_script, "script_molda_scene_culture", "$g_encountered_party"),
			(assign, ":var_1", "$town_scene_type"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(call_script, "script_wm_troop_type_depend_train", "$g_encountered_party", 0),
			(assign, ":var_2", "$temp_party_troop_06"),
			(assign, ":var_3", "$temp_party_troop_06"),
			(assign, ":var_4", "$temp_party_troop_03"),
			(assign, ":var_5", "$temp_party_troop_04"),
			(set_visitor, 23, ":var_3"),
			(set_visitor, 24, ":var_2"),
			(assign, reg0, ":var_5"),
			(assign, reg1, ":var_5"),
			(assign, reg2, ":var_4"),
			(assign, reg3, ":var_4"),
			(shuffle_range, 0, 4),
			(set_visitor, 25, reg0),
			(set_visitor, 26, reg1),
			(set_visitor, 27, reg2),
			(set_visitor, 28, reg3),
			(set_visitor, 42, "$temp_party_troop_03"),
			(set_visitor, 43, "$temp_party_troop_03"),
			(set_visitor, 44, "$temp_party_troop_05"),
			(set_visitor, 45, "$temp_party_troop_05"),
			(call_script, "script_wm_every_global_sett_depend_faction", "$g_encountered_party"),
			(set_visitors, 32, "$wm_npc_walker_m", 1),
			(set_visitors, 34, "$wm_npc_walker_m", 1),
			(set_visitors, 37, "$wm_npc_walker_f", 1),
			(set_visitors, 39, "$wm_npc_walker_f", 1),
			(store_random_in_range, ":random_in_range_0_4", 0, 4),
			(try_begin),
				(eq, ":random_in_range_0_4", 0),
				(assign, "$assasin_mission_rand_target", "$wm_npc_armorer"),
			(else_try),
				(eq, ":random_in_range_0_4", 1),
				(assign, "$assasin_mission_rand_target", "$wm_npc_merchant"),
			(else_try),
				(eq, ":random_in_range_0_4", 2),
				(assign, "$assasin_mission_rand_target", "$wm_npc_religionist"),
			(else_try),
				(assign, "$assasin_mission_rand_target", "$wm_npc_horse_merchant"),
			(try_end),
			(store_random_in_range, ":random_in_range_32_39", 32, 39),
			(set_visitor, ":random_in_range_32_39", "$assasin_mission_rand_target"),
			(str_store_troop_name, 15, "$assasin_mission_rand_target"),
			(display_message, "str_wm_qst_assasin_target", 0x00ffff00),
			(set_jump_mission, "mt_town_center"),
			(assign, "$current_mission_template", "mt_town_center"),
			(assign, ":value", 256),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 0, ":value"),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 2, ":value"),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 3, ":value"),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 4, ":value"),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 5, ":value"),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 6, ":value"),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 7, ":value"),
			(assign, ":value", 511),
			(mission_tpl_entry_set_override_flags, "mt_town_center", 1, ":value"),
			(mission_tpl_entry_clear_override_items, "mt_town_center", 1),
			(mission_tpl_entry_add_override_item, "mt_town_center", 1, 1435),
			(mission_tpl_entry_add_override_item, "mt_town_center", 1, 1366),
			(mission_tpl_entry_add_override_item, "mt_town_center", 1, 201),
			(mission_tpl_entry_add_override_item, "mt_town_center", 1, 202),
			(set_jump_entry, 1),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("kidnapping",
		[
			(party_slot_eq, "$g_encountered_party", 15, 4)
		],
		"(-)Kidnapping.",
		[
			(assign, "$wm_quest_mission_anti_skip_menu", 1),
			(assign, "$wm_talk_state", 4),
			(call_script, "script_molda_scene_culture", "$g_encountered_party"),
			(assign, ":var_1", "$town_scene_village"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(call_script, "script_wm_every_global_sett_depend_faction", "$g_encountered_party"),
			(set_visitors, 32, "$wm_npc_walker_m", 2),
			(set_visitors, 33, "$wm_npc_walker_f", 2),
			(set_visitors, 34, "$wm_npc_walker_m", 2),
			(set_visitors, 35, "$wm_npc_walker_f", 2),
			(set_visitors, 36, "$wm_npc_walker_m", 2),
			(set_visitors, 37, "$wm_npc_walker_f", 2),
			(set_visitors, 38, "$wm_npc_walker_m", 2),
			(set_visitors, 39, "$wm_npc_walker_f", 2),
			(set_jump_mission, "mt_village_center"),
			(assign, "$current_mission_template", "mt_village_center"),
			(set_jump_entry, 1),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("kidnapped_rescue",
		[
			(party_slot_eq, "$g_encountered_party", 15, 23)
		],
		"(+)Rescue.",
		[
			(assign, "$wm_talk_state", 0),
			(assign, ":var_1", "trp_kidnapper_fight"),
			(assign, ":var_2", "trp_kidnapper_rape"),
			(call_script, "script_wm_every_global_sett_depend_faction", "$g_encountered_party"),
			(assign, ":var_3", "scn_kidnapper_fight"),
			(modify_visitors_at_site, ":var_3"),
			(reset_visitors),
			(store_character_level, ":character_level_player", "trp_player"),
			(store_add, ":value", 5, ":character_level_player"),
			(val_div, ":value", 3),
			(try_for_range, ":unused", 0, ":value"),
				(store_random_in_range, ":random_in_range_2_11", 2, 11),
				(set_visitor, ":random_in_range_2_11", ":var_1", 1),
			(try_end),
			(set_visitor, 11, ":var_2", 1),
			(set_visitor, 12, ":var_2", 1),
			(set_visitor, 13, ":var_2", 1),
			(set_visitor, 14, ":var_2", 1),
			(set_visitor, 15, "$wm_npc_walker_f", 1),
			(set_visitor, 16, "$wm_npc_walker_f", 1),
			(set_visitor, 17, "$wm_npc_walker_f", 1),
			(set_visitor, 0, "trp_player"),
			(set_jump_mission, "mt_rescue_mission"),
			(assign, "$current_mission_template", "mt_rescue_mission"),
			(jump_to_scene, ":var_3"),
			(change_screen_mission)
		], "."),

		("raid_bandits_hideout",
		[
			(party_slot_eq, "$g_encountered_party", 15, 21)
		],
		"(+)Attack the hideout.",
		[
			(assign, "$wm_talk_state", 0),
			(assign, ":var_1", "trp_raid_bandit_brigand"),
			(assign, ":var_2", "trp_raid_bandit_boss"),
			(call_script, "script_wm_every_global_sett_depend_faction", "$g_encountered_party"),
			(assign, ":var_3", "scn_kidnapper_fight"),
			(modify_visitors_at_site, ":var_3"),
			(reset_visitors),
			(store_character_level, ":character_level_player", "trp_player"),
			(store_add, ":value", 5, ":character_level_player"),
			(val_div, ":value", 3),
			(try_for_range, ":unused", 0, ":value"),
				(store_random_in_range, ":random_in_range_2_11", 2, 11),
				(set_visitor, ":random_in_range_2_11", ":var_1", 1),
			(try_end),
			(set_visitor, 11, ":var_2", 1),
			(set_visitor, 0, "trp_player"),
			(set_jump_mission, "mt_raid_bandits_hideout"),
			(assign, "$current_mission_template", "mt_raid_bandits_hideout"),
			(jump_to_scene, ":var_3"),
			(change_screen_mission)
		], "."),

		("bandit_leader_hideout_attack",
		[
			(party_slot_eq, "$g_encountered_party", 15, 22)
		],
		"(+)Attack the bandit leader hideout.",
		[
			(assign, "$wm_talk_state", 0),
			(assign, ":var_1", "scn_bandit_leader_hideout"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "trp_raid_bandit_looter"),
			(set_visitor, 3, "trp_kidnapper_rape"),
			(set_visitor, 10, "trp_raid_bandit_looter"),
			(set_visitor, 12, "trp_kidnapper_fight"),
			(set_visitor, 20, "trp_raid_bandit_looter"),
			(set_visitor, 22, "trp_raid_bandit_brigand"),
			(set_visitor, 30, "trp_raid_bandit_boss"),
			(set_jump_mission, "mt_bandit_leader_hideout"),
			(assign, "$current_mission_template", "mt_bandit_leader_hideout"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("defence_bandit_hideout",
		[
			(this_or_next|party_slot_eq, "$g_encountered_party", 15, 23),
			(this_or_next|party_slot_eq, "$g_encountered_party", 15, 21),
			(party_slot_eq, "$g_encountered_party", 15, 22)
		],
		"(-)Defence bandit hideout.",
		[
			(party_set_slot, "$g_encountered_party", 15, 24),
			(assign, "$wm_quest_reward_honor", -1),
			(assign, "$wm_quest_reward_btexp", 100),
			(store_mul, "$wm_quest_reward_money", 500, 7),
			(assign, "$wm_quest_reward_debt", 300),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_02"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_02"),
			(assign, "$wm_talk_state", 0),
			(assign, ":var_1", "scn_bandit_leader_hideout"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(store_random_in_range, ":random_in_range_0_10", 0, 10),
			(try_begin),
				(eq, ":random_in_range_0_10", 0),
				(set_visitor, 0, "trp_adventurer_3"),
			(else_try),
				(this_or_next|eq, ":random_in_range_0_10", 1),
				(this_or_next|eq, ":random_in_range_0_10", 2),
				(eq, ":random_in_range_0_10", 3),
				(set_visitor, 0, "trp_adventurer_2"),
			(else_try),
				(set_visitor, 0, "trp_adventurer_1"),
			(try_end),
			(set_visitor, 1, "trp_raid_bandit_looter"),
			(set_visitor, 2, "trp_raid_bandit_looter"),
			(set_visitor, 3, "trp_raid_bandit_looter"),
			(set_visitor, 10, "trp_kidnapper_fight"),
			(set_visitor, 11, "trp_kidnapper_fight"),
			(set_visitor, 12, "trp_kidnapper_fight"),
			(set_visitor, 20, "trp_raid_bandit_brigand"),
			(set_visitor, 21, "trp_raid_bandit_brigand"),
			(set_visitor, 22, "trp_player"),
			(set_visitor, 30, "trp_raid_bandit_boss"),
			(set_jump_mission, "mt_defence_bandit_hideout"),
			(assign, "$current_mission_template", "mt_defence_bandit_hideout"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("protect_family_start",
		[
			(party_slot_eq, "$g_encountered_party", 15, 31)
		],
		"(+)Protect family.",
		[
			(party_set_slot, "$g_encountered_party", 15, 33),
			(assign, "$wm_quest_reward_honor", 1),
			(assign, "$wm_quest_reward_btexp", 50),
			(store_mul, "$wm_quest_reward_money", 500, 7),
			(assign, "$wm_quest_reward_debt", 0),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_01"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_01"),
			(assign, "$wm_talk_state", 0),
			(assign, ":var_1", "scn_protect_family_house"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "trp_protect_family_1"),
			(set_visitor, 2, "trp_protect_family_2"),
			(set_visitor, 3, "trp_protect_family_3"),
			(set_visitor, 4, "trp_protect_family_4"),
			(set_jump_mission, "mt_protect_family"),
			(assign, "$current_mission_template", "mt_protect_family"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("ffarm_defence",
		[
			(party_slot_eq, "$g_encountered_party", 15, 31)
		],
		"(+)Farm defence",
		[
			(party_set_slot, "$g_encountered_party", 15, 32),
			(assign, "$wm_quest_reward_honor", 1),
			(assign, "$wm_quest_reward_btexp", 50),
			(store_mul, "$wm_quest_reward_money", 500, 6),
			(assign, "$wm_quest_reward_debt", 0),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_01"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_01"),
			(assign, "$minimap_number_farmdef", 1),
			(assign, "$wm_talk_state", 0),
			(assign, ":var_1", "scn_farm_defence"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_jump_mission, "mt_farm_defence"),
			(assign, "$current_mission_template", "mt_farm_defence"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("ffarm_defence_hard",
		[
			(party_slot_eq, "$g_encountered_party", 15, 31)
		],
		"(+)Farm defence (Hard mode)",
		[
			(party_set_slot, "$g_encountered_party", 15, 32),
			(assign, "$wm_quest_reward_honor", 2),
			(assign, "$wm_quest_reward_btexp", 70),
			(store_mul, "$wm_quest_reward_money", 1000, 5),
			(assign, "$wm_quest_reward_debt", 0),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_01"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_01"),
			(assign, "$minimap_number_farmdef", 1),
			(assign, "$wm_talk_state", 0),
			(assign, ":var_1", "scn_farm_defence"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_jump_mission, "mt_farm_defence_hardmode"),
			(assign, "$current_mission_template", "mt_farm_defence_hardmode"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("family_exterminate_start",
		[
			(party_slot_eq, "$g_encountered_party", 15, 31)
		],
		"(-)Attack the farmhouse.",
		[
			(party_set_slot, "$g_encountered_party", 15, 34),
			(assign, "$wm_quest_reward_honor", -2),
			(assign, "$wm_quest_reward_btexp", 100),
			(store_mul, "$wm_quest_reward_money", 500, 8),
			(assign, "$wm_quest_reward_debt", 0),
			(assign, "$wm_quest_end_string_succ", "str_wm_qst_text_succ_02"),
			(assign, "$wm_quest_end_string_fail", "str_wm_qst_text_fail_02"),
			(assign, "$wm_talk_state", 0),
			(assign, ":var_1", "scn_family_exterminate_house"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(store_random_in_range, ":random_in_range_0_10", 0, 10),
			(try_begin),
				(eq, ":random_in_range_0_10", 0),
				(set_visitor, 0, "trp_adventurer_3"),
			(else_try),
				(this_or_next|eq, ":random_in_range_0_10", 1),
				(this_or_next|eq, ":random_in_range_0_10", 2),
				(eq, ":random_in_range_0_10", 3),
				(set_visitor, 0, "trp_adventurer_2"),
			(else_try),
				(set_visitor, 0, "trp_adventurer_1"),
			(try_end),
			(set_visitor, 1, "trp_protect_family_1"),
			(set_visitor, 2, "trp_protect_family_2"),
			(set_visitor, 3, "trp_protect_family_3"),
			(set_visitor, 4, "trp_protect_family_4"),
			(set_visitor, 10, "trp_player"),
			(set_jump_mission, "mt_family_exterminate"),
			(assign, "$current_mission_template", "mt_family_exterminate"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("insult_woman",
		[
			(party_slot_eq, "$g_encountered_party", 15, 7)
		],
		"(-)Infiltration.",
		[
			(assign, "$wm_talk_state", 0),
			(assign, "$wm_quest_mission_anti_skip_menu", 1),
			(assign, ":var_1", "scn_insult_woman"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "trp_private_guard"),
			(set_visitor, 2, "trp_private_guard"),
			(set_visitor, 10, "trp_noble_woman"),
			(set_jump_mission, "mt_insult_woman"),
			(assign, "$current_mission_template", "mt_insult_woman"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("insult_tavern_master",
		[
			(party_slot_eq, "$g_encountered_party", 15, 1)
		],
		"(-)Insult tavern master",
		[
			(assign, "$wm_quest_mission_anti_skip_menu", 1),
			(assign, "$wm_talk_state", 3),
			(call_script, "script_molda_scene_culture", "$g_encountered_party"),
			(assign, ":var_1", "$town_scene_tavern"),
			(set_jump_mission, "mt_tavern_mission"),
			(assign, "$current_mission_template", "mt_tavern_mission"),
			(mission_tpl_entry_set_override_flags, "mt_tavern_mission", 0, 256),
			(jump_to_scene, ":var_1"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(call_script, "script_wm_every_global_sett_depend_faction", "$g_encountered_party"),
			(set_visitor, 9, "$wm_npc_tavernkeeper"),
			(change_screen_mission)
		], "."),

		("player_prosti",
		[
			(party_slot_eq, "$g_encountered_party", 15, 8)
		],
		"(-)Enter the noble villa.",
		[
			(assign, "$wm_talk_state", 0),
			(assign, "$wm_quest_mission_anti_skip_menu", 1),
			(assign, ":var_1", "scn_insult_woman"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "trp_private_guard"),
			(set_visitor, 2, "trp_private_guard"),
			(set_visitor, 10, "trp_noble_man"),
			(set_jump_mission, "mt_nofight_noble_villa"),
			(assign, "$current_mission_template", "mt_nofight_noble_villa"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("rescue_lady_attack",
		[
			(party_slot_eq, "$g_encountered_party", 15, 30),
			(assign, "$pst_target_no", 0),
			(party_get_slot, ":g_encountered_party_town_center", "$g_encountered_party", slot_town_center),
			(call_script, "script_temp_save_number11_initialize"),
			(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(eq, ":faction_of_troop_troop", ":g_encountered_party_town_center"),
				(neg|troop_slot_eq, ":troop", slot_troop_leaded_party, 3),
				(neg|troop_slot_eq, "trp_player", slot_troop_state, ":troop"),
				(call_script, "script_temp_save_number11_inject", ":troop"),
			(try_end),
			(call_script, "script_temp_save_number11_choice_rand"),
			(try_begin),
				(is_between, "$wm_target_number11", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(assign, "$pst_target_no", "$wm_target_number11"),
			(try_end),
			(is_between, "$pst_target_no", "trp_tt_lady_01_01", "trp_tt_lady_end")
		],
		"(+)Rescue lady",
		[
			(assign, "$wm_talk_state", 0),
			(assign, ":var_1", "scn_fortress_ruins"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "trp_kidnapper_rape"),
			(set_visitor, 2, "trp_kidnapper_rape"),
			(set_visitor, 3, "trp_kidnapper_rape"),
			(set_visitor, 4, "trp_kidnapper_rape"),
			(set_visitor, 5, "trp_kidnapper_rape"),
			(set_visitor, 6, "trp_kidnapper_rape"),
			(set_visitor, 7, "trp_kidnapper_rape"),
			(set_visitor, 8, "trp_kidnapper_rape"),
			(set_visitor, 9, "trp_kidnapper_rape"),
			(set_visitor, 10, "trp_kidnapper_fight"),
			(set_visitor, 11, "trp_kidnapper_fight"),
			(set_visitor, 12, "trp_kidnapper_fight"),
			(set_visitor, 13, "trp_kidnapper_fight"),
			(set_visitor, 14, "trp_kidnapper_fight"),
			(set_visitor, 15, "trp_kidnapper_fight"),
			(set_visitor, 16, "trp_kidnapper_fight"),
			(set_visitor, 17, "trp_kidnapper_fight"),
			(set_visitor, 18, "trp_kidnapper_fight"),
			(set_visitor, 19, "trp_raid_bandit_boss"),
			(store_random_in_range, ":random_in_range_20_25", 20, 25),
			(set_visitor, ":random_in_range_20_25", "$pst_target_no"),
			(set_jump_mission, "mt_rescue_lady"),
			(assign, "$current_mission_template", "mt_rescue_lady"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
				(play_track, "track_reset_silence", 1), #Enforces new tracks to play ASAP.
		(music_set_situation, mtf_sit_travel),
			(assign, "$wm_quest_mission_anti_skip_menu", 0),
			(assign, "$minimap_number_farmdef", 0),
			(jump_to_menu, "mnu_wm_pst_map_return"),
			#####MUSICBOX
		(try_begin),
		(eq, "$additional_music", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
		(eq, "$additional_music_stop", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
		(assign, "$additional_music_stop", 0), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
		(music_set_situation, mtf_sit_travel),
		(play_track, "track_reset_silence", 1),
		(try_end),
		#(stop_all_sounds, 1), #Used to be value of 1
		], ".")
	]
	),

	("wm_field_encounter", 0, ">{s9}<^{s10}^-{s11}-",
"none",
	[
		(party_get_slot, ":g_encountered_party_town_horse_merchant", "$g_encountered_party", slot_town_horse_merchant),
		(try_begin),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 1),
			(assign, "$wm_talk_state", 0),
			(call_script, "script_setup_troop_meeting", ":g_encountered_party_town_horse_merchant", -1),
		(else_try),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 4),
			(assign, "$wm_talk_state", 0),
			(call_script, "script_setup_troop_meeting", ":g_encountered_party_town_horse_merchant", -1),
		(else_try),
			(try_begin),
				(set_fixed_point_multiplier, 1000),
				(position_set_x, 0, 600),
				(position_set_y, 0, 400),
				(position_set_z, 0, 750),
				(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", ":g_encountered_party_town_horse_merchant", 0),
			(try_end),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(str_store_faction_name, 9, ":faction_of_party_g_encountered_party"),
			(str_store_party_name, 10, "$g_encountered_party"),
			(str_store_troop_name, 11, ":g_encountered_party_town_horse_merchant"),
			(store_random_in_range, ":random_in_range_0_2", 0, 2),
			(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
			(try_begin),
				(this_or_next|eq, ":current_terrain_main_party", 7),
				(eq, ":current_terrain_main_party", 2),
				(set_background_mesh, "mesh_st_pic_sea"),
			(else_try),
				(eq, ":current_terrain_main_party", 5),
				(set_background_mesh, "mesh_st_pic_desert"),
			(else_try),
				(eq, ":current_terrain_main_party", 4),
				(set_background_mesh, "mesh_st_pic_snow"),
			(else_try),
				(eq, ":random_in_range_0_2", 0),
				(set_background_mesh, "mesh_st_pic_mount"),
			(else_try),
				(set_background_mesh, "mesh_st_pic_plain"),
			(try_end),
		(try_end),
#			#####MUSICBOX
#	(try_begin),
#	(eq, "$additional_music", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
#	(music_set_situation, mtf_sit_encounter_hostile),
#	#(play_track, "track_silence", 1), #Stop module track.
#	##(stop_all_sounds, 1), #Used to be value of 1
#	(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
#	(try_begin),
#	(this_or_next|eq, ":current_terrain_main_party", rt_mountain),
#	(this_or_next|eq, ":current_terrain_main_party", rt_steppe),
#	(eq, ":current_terrain_main_party", rt_steppe_forest),
#	(store_random_in_range, ":random_steppe", 1, 6),
#	(try_begin),
#	(eq, ":random_steppe", 1),
#	(play_track, "track_medm1", 1),
#	(else_try),
#	(eq, ":random_steppe", 2),
#	(play_track, "track_medm2", 1),
#	(else_try),
#	(eq, ":random_steppe", 3),
#	(play_track, "track_medm3", 1),
#	(else_try),
#	(eq, ":random_steppe", 4),
#	(play_track, "track_medm4", 1),
#	(else_try),
#	(eq, ":random_steppe", 5),
#	(play_track, "track_medm5", 1),
#	(try_end),
#	
#	(else_try),
#	(this_or_next|eq, ":current_terrain_main_party", rt_plain),
#	(this_or_next|eq, ":current_terrain_main_party", rt_forest),
#	(eq, ":current_terrain_main_party", rt_mountain_forest),
#	(store_random_in_range, ":random_euro", 1, 12),
#	(try_begin),
#		(eq, ":random_euro", 1),
#	(play_track, "track_eurottt1", 1),
#	(else_try),
#		(eq, ":random_euro", 2),
#	(play_track, "track_eurottt2", 1),
#	(else_try),
#		(eq, ":random_euro", 3),
#	(play_track, "track_eurottt3", 1),
#	(else_try),
#		(eq, ":random_euro", 4),
#	(play_track, "track_eurottt4", 1),
#	(else_try),
#	(eq, ":random_euro", 5),
#	(play_track, "track_eurottt5", 1),
#	(else_try),
#		(eq, ":random_euro", 6),
#	(play_track, "track_eurottt6", 1),
#	(else_try),
#		(eq, ":random_euro", 7),
#	(play_track, "track_eurottt7", 1),
#	(else_try),
#		(eq, ":random_euro", 8),
#	(play_track, "track_eurottt8", 1),
#	(else_try),
#	(eq, ":random_euro", 9),
#	(play_track, "track_eurottt9", 1),
#	(else_try),
#		(eq, ":random_euro", 10),
#	(play_track, "track_eurottt10", 1),
#	(else_try),
#		(eq, ":random_euro", 11),
#	(play_track, "track_eurottt11", 1),
#	(try_end),
#	(else_try),
#	(this_or_next|eq, ":current_terrain_main_party", rt_snow),
#	(this_or_next|eq, ":current_terrain_main_party", rt_snow_forest),
#	(eq, ":current_terrain_main_party", rt_bridge), #No idea
#	(store_random_in_range, ":random_euro", 1, 12),
#	(try_begin),
#		(eq, ":random_euro", 1),
#	(play_track, "track_eurottt1", 1),
#	(else_try),
#		(eq, ":random_euro", 2),
#	(play_track, "track_eurottt2", 1),
#	(else_try),
#		(eq, ":random_euro", 3),
#	(play_track, "track_eurottt3", 1),
#	(else_try),
#		(eq, ":random_euro", 4),
#	(play_track, "track_eurottt4", 1),
#	(else_try),
#	(eq, ":random_euro", 5),
#	(play_track, "track_eurottt5", 1),
#	(else_try),
#		(eq, ":random_euro", 6),
#	(play_track, "track_eurottt6", 1),
#	(else_try),
#		(eq, ":random_euro", 7),
#	(play_track, "track_eurottt7", 1),
#	(else_try),
#		(eq, ":random_euro", 8),
#	(play_track, "track_eurottt8", 1),
#	(else_try),
#	(eq, ":random_euro", 9),
#	(play_track, "track_eurottt9", 1),
#	(else_try),
#		(eq, ":random_euro", 10),
#	(play_track, "track_eurottt10", 1),
#	(else_try),
#		(eq, ":random_euro", 11),
#	(play_track, "track_eurottt11", 1),
#	(try_end),
#	(else_try),
#	(this_or_next|eq, ":current_terrain_main_party", rt_desert),
#	(eq, ":current_terrain_main_party", rt_desert_forest),
#	(store_random_in_range, ":random_arab", 1, 7),
#	(try_begin),
#	(eq, ":random_arab", 1),
#	(play_track, "track_arabt1", 1),
#	(else_try),
#		(eq, ":random_arab", 2),
#	(play_track, "track_arabt2", 1),
#	(else_try),
#		(eq, ":random_arab", 3),
#	(play_track, "track_arabt3", 1),
#	(else_try),
#		(eq, ":random_arab", 4),
#	(play_track, "track_arabt4", 1),
#	(else_try),
#		(eq, ":random_arab", 5),
#	(play_track, "track_arabt5", 1),
#	(else_try),
#		(eq, ":random_arab", 6),
#	(play_track, "track_arabt6", 1),
#	(try_end),
#	(try_end),
#	(try_end),
	],
	[
		("caravan_trade",
		[
			(party_slot_eq, "$g_encountered_party", slot_party_type, 4)
		],
		"Deal with traders",
		[
			(try_begin),
				(call_script, "script_wm_merchant_items_reset", "trp_town_1_merchant"),
				(party_get_slot, "$prev_encountered_party_culture", "$g_encountered_party", slot_town_claimed_by_player),
			(try_end),
			(try_begin),
				(assign, "$goods_sell_Horse", 3),
				(assign, "$goods_sell_Fine_wood", 3),
				(assign, "$goods_sell_Iron", 3),
				(assign, "$goods_sell_Elephant", 3),
				(assign, "$goods_sell_Whale", 3),
				(assign, "$goods_sell_Fish", 3),
				(assign, "$goods_sell_Maize", 3),
				(assign, "$goods_sell_Copper", 3),
				(assign, "$goods_sell_Marble", 3),
				(assign, "$goods_sell_Pearl", 3),
				(assign, "$goods_sell_Gem", 3),
				(assign, "$goods_sell_Ceramic", 3),
				(assign, "$goods_sell_Gold", 3),
				(assign, "$goods_sell_Silver", 3),
				(assign, "$goods_sell_Ivory", 3),
				(assign, "$goods_sell_Coffee", 3),
				(assign, "$goods_sell_Cacao", 3),
				(assign, "$goods_sell_Silk", 3),
				(assign, "$goods_sell_Nutmeg", 3),
				(assign, "$goods_sell_Allspice", 3),
				(assign, "$goods_sell_Cinnamon", 3),
				(assign, "$goods_sell_Clove", 3),
				(assign, "$goods_sell_Pepper", 3),
				(assign, "$goods_sell_Tabaco", 3),
				(assign, "$goods_sell_Tea", 3),
			(try_end),
			(val_mul, "$goods_sell_Horse", 100),
			(val_mul, "$goods_sell_Fine_wood", 100),
			(val_mul, "$goods_sell_Iron", 100),
			(val_mul, "$goods_sell_Elephant", 100),
			(val_mul, "$goods_sell_Whale", 100),
			(val_mul, "$goods_sell_Fish", 100),
			(val_mul, "$goods_sell_Maize", 100),
			(val_mul, "$goods_sell_Copper", 100),
			(val_mul, "$goods_sell_Marble", 100),
			(val_mul, "$goods_sell_Pearl", 100),
			(val_mul, "$goods_sell_Gem", 100),
			(val_mul, "$goods_sell_Ceramic", 100),
			(val_mul, "$goods_sell_Gold", 100),
			(val_mul, "$goods_sell_Silver", 100),
			(val_mul, "$goods_sell_Ivory", 100),
			(val_mul, "$goods_sell_Coffee", 100),
			(val_mul, "$goods_sell_Cacao", 100),
			(val_mul, "$goods_sell_Silk", 100),
			(val_mul, "$goods_sell_Nutmeg", 100),
			(val_mul, "$goods_sell_Allspice", 100),
			(val_mul, "$goods_sell_Cinnamon", 100),
			(val_mul, "$goods_sell_Clove", 100),
			(val_mul, "$goods_sell_Pepper", 100),
			(val_mul, "$goods_sell_Tabaco", 100),
			(val_mul, "$goods_sell_Tea", 100),
			(start_presentation, "prsnt_wm_item_trade")
		], "."),

		("caravan_attack",
		[
			(party_slot_eq, "$g_encountered_party", slot_party_type, 4),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(neq, ":faction_of_party_g_encountered_party", "$wm_player_fac"),
			(neq, ":faction_of_party_g_encountered_party", "$contract_fac"),
			(assign, ":value", 0),
			(try_begin),
				(troop_slot_ge, "trp_player", 18, 11),
				(store_relation, ":relation_faction_of_party_g_encountered_party_wm_player_fac", ":faction_of_party_g_encountered_party", "$wm_player_fac"),
				(lt, ":relation_faction_of_party_g_encountered_party_wm_player_fac", 0),
				(assign, ":value", 1),
			(else_try),
				(neg|troop_slot_ge, "trp_player", 18, 11),
				(is_between, "$contract_fac", "fac_kingdom_1", "fac_kingdoms_end"),
				(store_relation, ":relation_faction_of_party_g_encountered_party_wm_player_fac", ":faction_of_party_g_encountered_party", "$contract_fac"),
				(lt, ":relation_faction_of_party_g_encountered_party_wm_player_fac", 0),
				(assign, ":value", 1),
			(else_try),
				(neg|troop_slot_ge, "trp_player", 18, 11),
				(neg|is_between, "$contract_fac", "fac_kingdom_1", "fac_kingdoms_end"),
				(assign, ":value", 1),
			(try_end),
			(eq, ":value", 1),
#				#####MUSICBOX
#	(try_begin),
#	(eq, "$additional_music", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
#	(music_set_situation, mtf_sit_encounter_hostile),
#	#(play_track, "track_silence", 1), #Stop module track.
#	##(stop_all_sounds, 1), #Used to be value of 1
#	(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
#	(try_begin),
#	(this_or_next|eq, ":current_terrain_main_party", rt_mountain),
#	(this_or_next|eq, ":current_terrain_main_party", rt_steppe),
#	(eq, ":current_terrain_main_party", rt_steppe_forest),
#	(store_random_in_range, ":random_steppe", 1, 6),
#	(try_begin),
#	(eq, ":random_steppe", 1),
#	(play_track, "track_medm1", 1),
#	(else_try),
#	(eq, ":random_steppe", 2),
#	(play_track, "track_medm2", 1),
#	(else_try),
#	(eq, ":random_steppe", 3),
#	(play_track, "track_medm3", 1),
#	(else_try),
#	(eq, ":random_steppe", 4),
#	(play_track, "track_medm4", 1),
#	(else_try),
#	(eq, ":random_steppe", 5),
#	(play_track, "track_medm5", 1),
#	(try_end),
#	
#	(else_try),
#	(this_or_next|eq, ":current_terrain_main_party", rt_plain),
#	(this_or_next|eq, ":current_terrain_main_party", rt_forest),
#	(eq, ":current_terrain_main_party", rt_mountain_forest),
#	(store_random_in_range, ":random_euro", 1, 12),
#	(try_begin),
#		(eq, ":random_euro", 1),
#	(play_track, "track_eurottt1", 1),
#	(else_try),
#		(eq, ":random_euro", 2),
#	(play_track, "track_eurottt2", 1),
#	(else_try),
#		(eq, ":random_euro", 3),
#	(play_track, "track_eurottt3", 1),
#	(else_try),
#		(eq, ":random_euro", 4),
#	(play_track, "track_eurottt4", 1),
#	(else_try),
#	(eq, ":random_euro", 5),
#	(play_track, "track_eurottt5", 1),
#	(else_try),
#		(eq, ":random_euro", 6),
#	(play_track, "track_eurottt6", 1),
#	(else_try),
#		(eq, ":random_euro", 7),
#	(play_track, "track_eurottt7", 1),
#	(else_try),
#		(eq, ":random_euro", 8),
#	(play_track, "track_eurottt8", 1),
#	(else_try),
#	(eq, ":random_euro", 9),
#	(play_track, "track_eurottt9", 1),
#	(else_try),
#		(eq, ":random_euro", 10),
#	(play_track, "track_eurottt10", 1),
#	(else_try),
#		(eq, ":random_euro", 11),
#	(play_track, "track_eurottt11", 1),
#	(try_end),
#	(else_try),
#	(this_or_next|eq, ":current_terrain_main_party", rt_snow),
#	(this_or_next|eq, ":current_terrain_main_party", rt_snow_forest),
#	(eq, ":current_terrain_main_party", rt_bridge), #No idea
#	(store_random_in_range, ":random_euro", 1, 12),
#	(try_begin),
#		(eq, ":random_euro", 1),
#	(play_track, "track_eurottt1", 1),
#	(else_try),
#		(eq, ":random_euro", 2),
#	(play_track, "track_eurottt2", 1),
#	(else_try),
#		(eq, ":random_euro", 3),
#	(play_track, "track_eurottt3", 1),
#	(else_try),
#		(eq, ":random_euro", 4),
#	(play_track, "track_eurottt4", 1),
#	(else_try),
#	(eq, ":random_euro", 5),
#	(play_track, "track_eurottt5", 1),
#	(else_try),
#		(eq, ":random_euro", 6),
#	(play_track, "track_eurottt6", 1),
#	(else_try),
#		(eq, ":random_euro", 7),
#	(play_track, "track_eurottt7", 1),
#	(else_try),
#		(eq, ":random_euro", 8),
#	(play_track, "track_eurottt8", 1),
#	(else_try),
#	(eq, ":random_euro", 9),
#	(play_track, "track_eurottt9", 1),
#	(else_try),
#		(eq, ":random_euro", 10),
#	(play_track, "track_eurottt10", 1),
#	(else_try),
#		(eq, ":random_euro", 11),
#	(play_track, "track_eurottt11", 1),
#	(try_end),
#	(else_try),
#	(this_or_next|eq, ":current_terrain_main_party", rt_desert),
#	(eq, ":current_terrain_main_party", rt_desert_forest),
#	(store_random_in_range, ":random_arab", 1, 7),
#	(try_begin),
#	(eq, ":random_arab", 1),
#	(play_track, "track_arabt1", 1),
#	(else_try),
#		(eq, ":random_arab", 2),
#	(play_track, "track_arabt2", 1),
#	(else_try),
#		(eq, ":random_arab", 3),
#	(play_track, "track_arabt3", 1),
#	(else_try),
#		(eq, ":random_arab", 4),
#	(play_track, "track_arabt4", 1),
#	(else_try),
#		(eq, ":random_arab", 5),
#	(play_track, "track_arabt5", 1),
#	(else_try),
#		(eq, ":random_arab", 6),
#	(play_track, "track_arabt6", 1),
#	(try_end),
#	(try_end),
#	(try_end),
		],
		"Attack the traders",
		[
			(assign, "$wm_target_party", "$g_encountered_party"),
			(jump_to_menu, "mnu_low_encounter")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
				(play_track, "track_reset_silence", 1), #Enforces new tracks to play ASAP.
		(music_set_situation, mtf_sit_travel),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("blank_encounter", 0, "You are watching a battle unfold as a neutral third party. What will you do?",
"none",
	[
		(store_random_in_range, ":random_in_range_0_2", 0, 2),
		(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
		(try_begin),
			(this_or_next|eq, ":current_terrain_main_party", 7),
			(eq, ":current_terrain_main_party", 2),
			(set_background_mesh, "mesh_st_pic_sea"),
		(else_try),
			(eq, ":current_terrain_main_party", 5),
			(set_background_mesh, "mesh_st_pic_desert"),
		(else_try),
			(eq, ":current_terrain_main_party", 4),
			(set_background_mesh, "mesh_st_pic_snow"),
		(else_try),
			(eq, ":random_in_range_0_2", 0),
			(set_background_mesh, "mesh_st_pic_mount"),
		(else_try),
			(set_background_mesh, "mesh_st_pic_plain"),
		(try_end),
#			#####MUSICBOX
#	(try_begin),
#	(eq, "$additional_music", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
#	(music_set_situation, mtf_sit_encounter_hostile),
#	#(play_track, "track_silence", 1), #Stop module track.
#	##(stop_all_sounds, 1), #Used to be value of 1
#	(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
#	(try_begin),
#	(this_or_next|eq, ":current_terrain_main_party", rt_mountain),
#	(this_or_next|eq, ":current_terrain_main_party", rt_steppe),
#	(eq, ":current_terrain_main_party", rt_steppe_forest),
#	(store_random_in_range, ":random_steppe", 1, 6),
#	(try_begin),
#	(eq, ":random_steppe", 1),
#	(play_track, "track_medm1", 1),
#	(else_try),
#	(eq, ":random_steppe", 2),
#	(play_track, "track_medm2", 1),
#	(else_try),
#	(eq, ":random_steppe", 3),
#	(play_track, "track_medm3", 1),
#	(else_try),
#	(eq, ":random_steppe", 4),
#	(play_track, "track_medm4", 1),
#	(else_try),
#	(eq, ":random_steppe", 5),
#	(play_track, "track_medm5", 1),
#	(try_end),
#	
#	(else_try),
#	(this_or_next|eq, ":current_terrain_main_party", rt_plain),
#	(this_or_next|eq, ":current_terrain_main_party", rt_forest),
#	(eq, ":current_terrain_main_party", rt_mountain_forest),
#	(store_random_in_range, ":random_euro", 1, 12),
#	(try_begin),
#		(eq, ":random_euro", 1),
#	(play_track, "track_eurottt1", 1),
#	(else_try),
#		(eq, ":random_euro", 2),
#	(play_track, "track_eurottt2", 1),
#	(else_try),
#		(eq, ":random_euro", 3),
#	(play_track, "track_eurottt3", 1),
#	(else_try),
#		(eq, ":random_euro", 4),
#	(play_track, "track_eurottt4", 1),
#	(else_try),
#	(eq, ":random_euro", 5),
#	(play_track, "track_eurottt5", 1),
#	(else_try),
#		(eq, ":random_euro", 6),
#	(play_track, "track_eurottt6", 1),
#	(else_try),
#		(eq, ":random_euro", 7),
#	(play_track, "track_eurottt7", 1),
#	(else_try),
#		(eq, ":random_euro", 8),
#	(play_track, "track_eurottt8", 1),
#	(else_try),
#	(eq, ":random_euro", 9),
#	(play_track, "track_eurottt9", 1),
#	(else_try),
#		(eq, ":random_euro", 10),
#	(play_track, "track_eurottt10", 1),
#	(else_try),
#		(eq, ":random_euro", 11),
#	(play_track, "track_eurottt11", 1),
#	(try_end),
#	(else_try),
#	(this_or_next|eq, ":current_terrain_main_party", rt_snow),
#	(this_or_next|eq, ":current_terrain_main_party", rt_snow_forest),
#	(eq, ":current_terrain_main_party", rt_bridge), #No idea
#	(store_random_in_range, ":random_euro", 1, 12),
#	(try_begin),
#		(eq, ":random_euro", 1),
#	(play_track, "track_eurottt1", 1),
#	(else_try),
#		(eq, ":random_euro", 2),
#	(play_track, "track_eurottt2", 1),
#	(else_try),
#		(eq, ":random_euro", 3),
#	(play_track, "track_eurottt3", 1),
#	(else_try),
#		(eq, ":random_euro", 4),
#	(play_track, "track_eurottt4", 1),
#	(else_try),
#	(eq, ":random_euro", 5),
#	(play_track, "track_eurottt5", 1),
#	(else_try),
#		(eq, ":random_euro", 6),
#	(play_track, "track_eurottt6", 1),
#	(else_try),
#		(eq, ":random_euro", 7),
#	(play_track, "track_eurottt7", 1),
#	(else_try),
#		(eq, ":random_euro", 8),
#	(play_track, "track_eurottt8", 1),
#	(else_try),
#	(eq, ":random_euro", 9),
#	(play_track, "track_eurottt9", 1),
#	(else_try),
#		(eq, ":random_euro", 10),
#	(play_track, "track_eurottt10", 1),
#	(else_try),
#		(eq, ":random_euro", 11),
#	(play_track, "track_eurottt11", 1),
#	(try_end),
#	(else_try),
#	(this_or_next|eq, ":current_terrain_main_party", rt_desert),
#	(eq, ":current_terrain_main_party", rt_desert_forest),
#	(store_random_in_range, ":random_arab", 1, 7),
#	(try_begin),
#	(eq, ":random_arab", 1),
#	(play_track, "track_arabt1", 1),
#	(else_try),
#		(eq, ":random_arab", 2),
#	(play_track, "track_arabt2", 1),
#	(else_try),
#		(eq, ":random_arab", 3),
#	(play_track, "track_arabt3", 1),
#	(else_try),
#		(eq, ":random_arab", 4),
#	(play_track, "track_arabt4", 1),
#	(else_try),
#		(eq, ":random_arab", 5),
#	(play_track, "track_arabt5", 1),
#	(else_try),
#		(eq, ":random_arab", 6),
#	(play_track, "track_arabt6", 1),
#	(try_end),
#	(try_end),
#	(try_end),
	],
	[
		("attack_en11",
		[
			(neg|party_slot_eq, "$g_encountered_party", slot_party_type, 1),
			(neg|is_between, "$g_encountered_party", "p_pyongyang", "p_place_end"),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(store_relation, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", ":faction_of_party_g_encountered_party", "fac_player_supporters_faction"),
			(lt, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", 0),
			(str_store_party_name, 1, "$g_encountered_party")
		],
		"Attack the {s1}",
		[
			(assign, "$wm_target_party", "$g_encountered_party"),
			(jump_to_menu, "mnu_low_encounter")
		], "."),

		("attack_en22",
		[
			(neg|party_slot_eq, "$g_encountered_party_2", slot_party_type, 1),
			(neg|is_between, "$g_encountered_party_2", "p_pyongyang", "p_place_end"),
			(store_faction_of_party, ":faction_of_party_g_encountered_party_2", "$g_encountered_party_2"),
			(store_relation, ":relation_faction_of_party_g_encountered_party_2_player_supporters_faction", ":faction_of_party_g_encountered_party_2", "fac_player_supporters_faction"),
			(lt, ":relation_faction_of_party_g_encountered_party_2_player_supporters_faction", 0),
			(str_store_party_name, 2, "$g_encountered_party_2")
		],
		"Attack the {s2}",
		[
			(assign, "$wm_target_party", "$g_encountered_party_2"),
			(jump_to_menu, "mnu_low_encounter")
		], "."),

		("attack_en1",
		[
			(party_slot_eq, "$g_encountered_party", slot_party_type, 1),
			(neg|is_between, "$g_encountered_party", "p_pyongyang", "p_place_end"),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(store_relation, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", ":faction_of_party_g_encountered_party", "fac_player_supporters_faction"),
			(lt, ":relation_faction_of_party_g_encountered_party_player_supporters_faction", 0),
			(str_store_party_name, 1, "$g_encountered_party")
		],
		"Attack the {s1}",
		[
			(assign, "$wm_target_party", "$g_encountered_party"),
			(store_faction_of_party, ":faction_of_party_wm_target_party", "$wm_target_party"),
			(call_script, "script_wm_fac_relation_diff", "$wm_player_fac", ":faction_of_party_wm_target_party", -10),
			(party_get_slot, ":wm_target_party_town_horse_merchant", "$wm_target_party", slot_town_horse_merchant),
			(try_begin),
				(is_between, ":wm_target_party_town_horse_merchant", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(call_script, "script_change_player_relation_with_troop", ":wm_target_party_town_horse_merchant", -15),
			(try_end),
			(store_faction_of_party, ":faction_of_party_g_encountered_party_2", "$g_encountered_party_2"),
			(call_script, "script_wm_fac_relation_diff", "$wm_player_fac", ":faction_of_party_g_encountered_party_2", 10),
			(party_get_slot, ":wm_target_party_town_horse_merchant", "$g_encountered_party_2", slot_town_horse_merchant),
			(try_begin),
				(is_between, ":wm_target_party_town_horse_merchant", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(call_script, "script_change_player_relation_with_troop", ":wm_target_party_town_horse_merchant", 10),
			(try_end),
			(jump_to_menu, "mnu_wm_attack_menu")
		], "."),

		("attack_en2",
		[
			(party_slot_eq, "$g_encountered_party_2", slot_party_type, 1),
			(neg|is_between, "$g_encountered_party_2", "p_pyongyang", "p_place_end"),
			(store_faction_of_party, ":faction_of_party_g_encountered_party_2", "$g_encountered_party_2"),
			(store_relation, ":relation_faction_of_party_g_encountered_party_2_player_supporters_faction", ":faction_of_party_g_encountered_party_2", "fac_player_supporters_faction"),
			(lt, ":relation_faction_of_party_g_encountered_party_2_player_supporters_faction", 0),
			(str_store_party_name, 2, "$g_encountered_party_2")
		],
		"Attack the {s2}",
		[
			(assign, "$wm_target_party", "$g_encountered_party_2"),
			(store_faction_of_party, ":faction_of_party_wm_target_party", "$wm_target_party"),
			(call_script, "script_wm_fac_relation_diff", "$wm_player_fac", ":faction_of_party_wm_target_party", -10),
			(party_get_slot, ":wm_target_party_town_horse_merchant", "$wm_target_party", slot_town_horse_merchant),
			(try_begin),
				(is_between, ":wm_target_party_town_horse_merchant", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(call_script, "script_change_player_relation_with_troop", ":wm_target_party_town_horse_merchant", -15),
			(try_end),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(call_script, "script_wm_fac_relation_diff", "$wm_player_fac", ":faction_of_party_g_encountered_party", 10),
			(party_get_slot, ":wm_target_party_town_horse_merchant", "$g_encountered_party", slot_town_horse_merchant),
			(try_begin),
				(is_between, ":wm_target_party_town_horse_merchant", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(call_script, "script_change_player_relation_with_troop", ":wm_target_party_town_horse_merchant", 10),
			(try_end),
			(jump_to_menu, "mnu_wm_attack_menu")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
		#####MUSICBOX
				(play_track, "track_reset_silence", 1), #Enforces new tracks to play ASAP.
		(music_set_situation, mtf_sit_travel),
			(jump_to_menu, "mnu_wm_pst_map_return"),
			


		], ".")
	]
	),

	("wm_attack_menu", 0, "     ",
"none",
	[
		(assign, "$attempt_coup", 0),
		(assign, "$molda_siege_type", 0),
		(assign, "$player_has_ally", 0),
		(assign, "$enemy_has_ally", 0),
		(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
		(call_script, "script_encounter_party_faction_slot_init"),
		(call_script, "script_encounter_lord_slot_init"),
		(try_begin),
			(call_script, "script_party_count_fit_for_battle", "p_main_party"),
			(assign, "$player_army_size", reg0),
			(party_get_slot, "$player_train_level", "p_main_party", slot_town_elder),
			(party_get_slot, "$player_moral_level", "p_main_party", slot_center_player_relation),
			(assign, ":value", "$wm_player_fac"),
			(try_begin),
				(gt, "$contract_time", 0),
				(is_between, "$contract_fac", "fac_kingdom_1", "fac_kingdoms_end"),
				(neg|troop_slot_ge, "trp_player", 18, 11),
				(assign, ":value", "$contract_fac"),
			(try_end),
			(try_for_range, ":number", 56, 76),
				(faction_get_slot, ":value_number", ":value", ":number"),
				(gt, ":value_number", 0),
				(party_is_active, ":value_number"),
				(neg|is_between, ":value_number", "p_temp_party", "p_reserved_5"),
				(neq, ":value_number", "p_reserved_5"),
				(party_slot_eq, ":value_number", slot_party_type, 1),
				(store_faction_of_party, ":faction_of_party_value_number", ":value_number"),
				(eq, ":faction_of_party_value_number", ":value"),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_value_number_main_party", ":value_number", "p_main_party"),
				(le, ":distance_to_party_from_party_value_number_main_party", "$battle_join_dist"),
				(str_store_party_name, 1, ":value_number"),
				(assign, "$player_has_ally", 1),
				(display_message, "str_s1_joined_battle_friend", 0x0000ff00),
				(call_script, "script_faction_army_list_inject", "fac_ally_faction_for_slot", ":value_number"),
				(call_script, "script_party_count_fit_for_battle", ":value_number"),
				(val_add, "$player_army_size", reg0),
				(party_get_slot, ":value_number_town_horse_merchant", ":value_number", slot_town_horse_merchant),
				(call_script, "script_faction_lord_list_slot_quence", "fac_ally_faction_for_slot", ":value_number_town_horse_merchant"),
				(party_get_slot, ":value_number_town_elder", ":value_number", slot_town_elder),
				(party_get_slot, ":value_number_center_player_relation", ":value_number", slot_center_player_relation),
				(try_begin),
					(gt, ":value_number_town_elder", "$player_train_level"),
					(assign, "$player_train_level", ":value_number_town_elder"),
				(try_end),
				(try_begin),
					(gt, ":value_number_center_player_relation", "$player_moral_level"),
					(assign, "$player_moral_level", ":value_number_town_elder"),
				(try_end),
			(try_end),
			(store_faction_of_party, ":faction_of_party_wm_target_party", "$wm_target_party"),
			(try_for_range, ":faction", "fac_kingdom_1", "fac_undeads"),
				(neq, ":faction", "fac_kingdoms_end"),
				(neq, ":faction", ":value"),
				(neq, ":faction", ":faction_of_party_wm_target_party"),
				(store_relation, ":relation_faction_faction_of_party_wm_target_party", ":faction", ":faction_of_party_wm_target_party"),
				(lt, ":relation_faction_faction_of_party_wm_target_party", 0),
				(store_relation, ":relation_faction_value", ":faction", ":value"),
				(ge, ":relation_faction_value", 0),
				(try_for_range, ":number", 56, 76),
					(faction_get_slot, ":value_number", ":faction", ":number"),
					(gt, ":value_number", 0),
					(party_is_active, ":value_number"),
					(neg|is_between, ":value_number", "p_temp_party", "p_reserved_5"),
					(neq, ":value_number", "p_reserved_5"),
					(party_slot_eq, ":value_number", slot_party_type, 1),
					(store_faction_of_party, ":faction_of_party_value_number", ":value_number"),
					(eq, ":faction_of_party_value_number", ":faction"),
					(store_distance_to_party_from_party, ":distance_to_party_from_party_value_number_main_party", ":value_number", "p_main_party"),
					(le, ":distance_to_party_from_party_value_number_main_party", "$battle_join_dist"),
					(str_store_party_name, 1, ":value_number"),
					(assign, "$player_has_ally", 1),
					(display_message, "str_s1_joined_battle_friend", 0x0000ff00),
					(call_script, "script_faction_army_list_inject", "fac_ally_faction_for_slot", ":value_number"),
					(call_script, "script_party_count_fit_for_battle", ":value_number"),
					(val_add, "$player_army_size", reg0),
					(party_get_slot, ":value_number_town_horse_merchant", ":value_number", slot_town_horse_merchant),
					(call_script, "script_faction_lord_list_slot_quence", "fac_ally_faction_for_slot", ":value_number_town_horse_merchant"),
					(party_get_slot, ":value_number_town_elder", ":value_number", slot_town_elder),
					(party_get_slot, ":value_number_center_player_relation", ":value_number", slot_center_player_relation),
					(try_begin),
						(gt, ":value_number_town_elder", "$player_train_level"),
						(assign, "$player_train_level", ":value_number_town_elder"),
					(try_end),
					(try_begin),
						(gt, ":value_number_center_player_relation", "$player_moral_level"),
						(assign, "$player_moral_level", ":value_number_town_elder"),
					(try_end),
				(try_end),
			(try_end),
			(try_begin),
				(eq, "$is_siege_defence", 1),
				(is_between, "$g_encountered_party", "p_pyongyang", "p_place_end"),
				(assign, ":value_number", "$g_encountered_party"),
				(store_faction_of_party, ":faction_of_party_value_number", ":value_number"),
				(eq, ":faction_of_party_value_number", ":value"),
				(str_store_party_name, 1, ":value_number"),
				(display_message, "str_s1_joined_battle_friend", 0x0000ff00),
				(call_script, "script_party_count_fit_for_battle", ":value_number"),
				(val_add, "$player_army_size", reg0),
				(party_get_slot, ":value_number_town_horse_merchant", ":value_number", slot_town_horse_merchant),
				(call_script, "script_faction_lord_list_slot_quence", "fac_ally_faction_for_slot", ":value_number_town_horse_merchant"),
				(party_get_slot, ":value_number_town_elder", ":value_number", slot_town_elder),
				(party_get_slot, ":value_number_center_player_relation", ":value_number", slot_center_player_relation),
				(try_begin),
					(gt, ":value_number_town_elder", "$player_train_level"),
					(assign, "$player_train_level", ":value_number_town_elder"),
				(try_end),
				(try_begin),
					(gt, ":value_number_center_player_relation", "$player_moral_level"),
					(assign, "$player_moral_level", ":value_number_town_elder"),
				(try_end),
			(try_end),
			(call_script, "script_party_count_fit_for_battle", "$wm_target_party"),
			(assign, "$enemy_army_size", reg0),
			(party_get_slot, "$enemy_train_level", "$wm_target_party", slot_town_elder),
			(party_get_slot, "$enemy_moral_level", "$wm_target_party", slot_center_player_relation),
			(store_faction_of_party, ":faction_of_party_wm_target_party", "$wm_target_party"),
			(try_for_range, ":number", 56, 76),
				(faction_get_slot, ":value_number", ":faction_of_party_wm_target_party", ":number"),
				(gt, ":value_number", 0),
				(party_is_active, ":value_number"),
				(neg|is_between, ":value_number", "p_temp_party", "p_reserved_5"),
				(neq, ":value_number", "p_reserved_5"),
				(party_slot_eq, ":value_number", slot_party_type, 1),
				(neq, ":value_number", "$wm_target_party"),
				(store_faction_of_party, ":faction_of_party_value_number", ":value_number"),
				(eq, ":faction_of_party_value_number", ":faction_of_party_wm_target_party"),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_value_number_main_party", ":value_number", "$wm_target_party"),
				(le, ":distance_to_party_from_party_value_number_main_party", "$battle_join_dist"),
				(str_store_party_name, 1, ":value_number"),
				(assign, "$enemy_has_ally", 1),
				(display_message, "str_s1_joined_battle_enemy", 0x00ffff00),
				(call_script, "script_faction_army_list_inject", "fac_enemy_faction_for_slot", ":value_number"),
				(call_script, "script_party_count_fit_for_battle", ":value_number"),
				(val_add, "$enemy_army_size", reg0),
				(party_get_slot, ":value_number_town_horse_merchant", ":value_number", slot_town_horse_merchant),
				(call_script, "script_faction_lord_list_slot_quence", "fac_enemy_faction_for_slot", ":value_number_town_horse_merchant"),
				(party_get_slot, ":value_number_town_elder", ":value_number", slot_town_elder),
				(party_get_slot, ":value_number_center_player_relation", ":value_number", slot_center_player_relation),
				(try_begin),
					(gt, ":value_number_town_elder", "$enemy_train_level"),
					(assign, "$enemy_train_level", ":value_number_town_elder"),
				(try_end),
				(try_begin),
					(gt, ":value_number_center_player_relation", "$enemy_moral_level"),
					(assign, "$enemy_moral_level", ":value_number_town_elder"),
				(try_end),
			(try_end),
			(store_faction_of_party, ":faction_of_party_wm_target_party", "$wm_target_party"),
			(try_for_range, ":faction", "fac_kingdom_1", "fac_undeads"),
				(neq, ":faction", "fac_kingdoms_end"),
				(neq, ":faction", ":value"),
				(neq, ":faction", ":faction_of_party_wm_target_party"),
				(store_relation, ":relation_faction_faction_of_party_wm_target_party", ":faction", ":faction_of_party_wm_target_party"),
				(ge, ":relation_faction_faction_of_party_wm_target_party", 0),
				(store_relation, ":relation_faction_value", ":faction", ":value"),
				(lt, ":relation_faction_value", 0),
				(try_for_range, ":number", 56, 76),
					(faction_get_slot, ":value_number", ":faction", ":number"),
					(gt, ":value_number", 0),
					(party_is_active, ":value_number"),
					(neg|is_between, ":value_number", "p_temp_party", "p_reserved_5"),
					(neq, ":value_number", "p_reserved_5"),
					(party_slot_eq, ":value_number", slot_party_type, 1),
					(store_faction_of_party, ":faction_of_party_value_number", ":value_number"),
					(eq, ":faction_of_party_value_number", ":faction"),
					(store_distance_to_party_from_party, ":distance_to_party_from_party_value_number_main_party", ":value_number", "p_main_party"),
					(le, ":distance_to_party_from_party_value_number_main_party", "$battle_join_dist"),
					(str_store_party_name, 1, ":value_number"),
					(assign, "$enemy_has_ally", 1),
					(display_message, "str_s1_joined_battle_enemy", 0x00ffff00),
					(call_script, "script_faction_army_list_inject", "fac_enemy_faction_for_slot", ":value_number"),
					(call_script, "script_party_count_fit_for_battle", ":value_number"),
					(val_add, "$enemy_army_size", reg0),
					(party_get_slot, ":value_number_town_horse_merchant", ":value_number", slot_town_horse_merchant),
					(call_script, "script_faction_lord_list_slot_quence", "fac_enemy_faction_for_slot", ":value_number_town_horse_merchant"),
					(party_get_slot, ":value_number_town_elder", ":value_number", slot_town_elder),
					(party_get_slot, ":value_number_center_player_relation", ":value_number", slot_center_player_relation),
					(try_begin),
						(gt, ":value_number_town_elder", "$enemy_train_level"),
						(assign, "$enemy_train_level", ":value_number_town_elder"),
					(try_end),
					(try_begin),
						(gt, ":value_number_center_player_relation", "$enemy_moral_level"),
						(assign, "$enemy_moral_level", ":value_number_town_elder"),
					(try_end),
				(try_end),
			(try_end),
		(try_end),
		(party_get_slot, "$enemy_commander", "$wm_target_party", slot_town_horse_merchant),
		(try_begin),
			(neg|encountered_party_is_attacker),
			(assign, "$player_is_attack", 1),
			(assign, "$wm_allow_retreat", 1),
		(else_try),
			(assign, "$player_is_attack", 0),
			(assign, "$wm_allow_retreat", 1),
		(try_end),
		(call_script, "script_battle_scale_sett"),
		(troop_get_slot, "$player_strategy_skill", "trp_player", slot_troop_spouse),
		(troop_get_slot, "$enemy_strategy_skill", "$enemy_commander", slot_troop_spouse),
		(troop_get_slot, "$player_tactics_skill", "trp_player", slot_troop_spawned_before),
		(troop_get_slot, "$enemy_tactics_skill", "$enemy_commander", slot_troop_spawned_before),
		(troop_get_slot, "$player_leadership_skill", "trp_player", slot_troop_last_comment_slot),
		(troop_get_slot, "$enemy_leadership_skill", "$enemy_commander", slot_troop_last_comment_slot),
		(troop_get_slot, "$player_naval_skill", "trp_player", slot_troop_father),
		(troop_get_slot, "$enemy_naval_skill", "$enemy_commander", slot_troop_father),
		(call_script, "script_equip_supp_slot_export", "p_main_party"),
		(call_script, "script_equip_supp_slot_export", "$wm_target_party"),
		(store_faction_of_party, ":faction_of_party_wm_target_party", "$wm_target_party"),
		(faction_get_slot, "$enemy_has_horse", ":faction_of_party_wm_target_party", slot_faction_adjective),
		(faction_get_slot, "$enemy_has_finewood", ":faction_of_party_wm_target_party", 23),
		(faction_get_slot, "$enemy_has_iron", ":faction_of_party_wm_target_party", 24),
		(try_begin),
			(troop_slot_ge, "trp_player", 18, 11),
			(faction_get_slot, "$player_has_horse", "$wm_player_fac", slot_faction_adjective),
			(faction_get_slot, "$player_has_finewood", "$wm_player_fac", 23),
			(faction_get_slot, "$player_has_iron", "$wm_player_fac", 24),
		(else_try),
			(neg|troop_slot_ge, "trp_player", 18, 11),
			(is_between, "$contract_fac", "fac_kingdom_1", "fac_kingdoms_end"),
			(faction_get_slot, "$player_has_horse", "$contract_fac", slot_faction_adjective),
			(faction_get_slot, "$player_has_finewood", "$contract_fac", 23),
			(faction_get_slot, "$player_has_iron", "$contract_fac", 24),
		(else_try),
			(assign, "$player_has_horse", 0),
			(assign, "$player_has_finewood", 0),
			(assign, "$player_has_iron", 0),
		(try_end),
		(try_begin),
			(this_or_next|is_between, "$g_encountered_party", "p_pyongyang", "p_place_end"),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 1),
			(ge, "$enemy_army_size", 1000),
			(le, "$player_army_size", 300),
			(assign, "$player_cant_fight", 1),
			(try_begin),
				(is_between, "$g_encountered_party", "p_pyongyang", "p_place_end"),
				(assign, "$battle_tile_type", 101),
				(assign, "$battle_tile_menu_pop", 1),
				(jump_to_menu, "mnu_pst_battle_tile"),
			(else_try),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 1),
				(neq, ":current_terrain_main_party", 7),
				(neq, ":current_terrain_main_party", 2),
				(assign, "$battle_tile_type", 0),
				(assign, "$battle_tile_menu_pop", 1),
				(jump_to_menu, "mnu_pst_battle_tile"),
			(else_try),
				(party_slot_eq, "$g_encountered_party", slot_party_type, 1),
				(assign, "$battle_tile_type", 51),
				(assign, "$battle_tile_menu_pop", 1),
				(jump_to_menu, "mnu_pst_battle_tile"),
			(try_end),
		(else_try),
			(neg|is_between, "$g_encountered_party", "p_pyongyang", "p_place_end"),
			(neq, ":current_terrain_main_party", 7),
			(neq, ":current_terrain_main_party", 2),
			(try_begin),
				(ge, "$random_succ_100_trand", 94),
				(assign, "$battle_tile_type", 8),
				(assign, "$battle_tile_menu_pop", 1),
				(jump_to_menu, "mnu_pst_battle_tile"),
			(else_try),
				(ge, "$random_succ_100_trand", 81),
				(assign, "$battle_tile_type", 7),
				(assign, "$battle_tile_menu_pop", 1),
				(jump_to_menu, "mnu_pst_battle_tile"),
			(else_try),
				(assign, "$battle_tile_type", 0),
				(assign, "$battle_tile_menu_pop", 1),
				(jump_to_menu, "mnu_pst_battle_tile"),
			(try_end),
		(else_try),
			(neg|is_between, "$g_encountered_party", "p_pyongyang", "p_place_end"),
			(this_or_next|eq, ":current_terrain_main_party", 7),
			(eq, ":current_terrain_main_party", 2),
			(try_begin),
				(assign, "$battle_tile_type", 51),
				(assign, "$battle_tile_menu_pop", 1),
				(jump_to_menu, "mnu_pst_battle_tile"),
			(try_end),
		(else_try),
			(is_between, "$g_encountered_party", "p_pyongyang", "p_place_end"),
			(call_script, "script_molda_scene_culture", "$wm_target_party"),
			(party_get_slot, ":wm_target_party_village_player_can_not_steal_cattle", "$wm_target_party", slot_village_player_can_not_steal_cattle),
			(try_begin),
				(eq, "$is_siege_defence", 0),
				(try_begin),
					(eq, ":wm_target_party_village_player_can_not_steal_cattle", 13),
					(neq, "$town_culture_type", 8),
					(neq, "$town_culture_type", 9),
					(neq, "$town_culture_type", 10),
					(assign, "$battle_tile_type", 105),
					(assign, "$battle_tile_menu_pop", 1),
					(jump_to_menu, "mnu_pst_battle_tile"),
				(else_try),
					(eq, ":wm_target_party_village_player_can_not_steal_cattle", 12),
					(neq, "$town_culture_type", 8),
					(neq, "$town_culture_type", 9),
					(neq, "$town_culture_type", 10),
					(assign, "$battle_tile_type", 104),
					(assign, "$battle_tile_menu_pop", 1),
					(jump_to_menu, "mnu_pst_battle_tile"),
				(else_try),
					(eq, ":wm_target_party_village_player_can_not_steal_cattle", 11),
					(neq, "$town_culture_type", 8),
					(neq, "$town_culture_type", 9),
					(neq, "$town_culture_type", 10),
					(assign, "$battle_tile_type", 103),
					(assign, "$battle_tile_menu_pop", 1),
					(jump_to_menu, "mnu_pst_battle_tile"),
				(else_try),
					(this_or_next|eq, "$town_culture_type", 8),
					(this_or_next|eq, "$town_culture_type", 9),
					(eq, "$town_culture_type", 10),
					(assign, "$battle_tile_type", 102),
					(assign, "$battle_tile_menu_pop", 1),
					(jump_to_menu, "mnu_pst_battle_tile"),
				(else_try),
					(assign, "$battle_tile_type", 101),
					(assign, "$battle_tile_menu_pop", 1),
					(jump_to_menu, "mnu_pst_battle_tile"),
				(try_end),
			(else_try),
				(eq, "$is_siege_defence", 1),
				(try_begin),
					(eq, ":wm_target_party_village_player_can_not_steal_cattle", 13),
					(neq, "$town_culture_type", 8),
					(neq, "$town_culture_type", 9),
					(neq, "$town_culture_type", 10),
					(assign, "$battle_tile_type", 115),
					(assign, "$battle_tile_menu_pop", 1),
					(jump_to_menu, "mnu_pst_battle_tile"),
				(else_try),
					(eq, ":wm_target_party_village_player_can_not_steal_cattle", 12),
					(neq, "$town_culture_type", 8),
					(neq, "$town_culture_type", 9),
					(neq, "$town_culture_type", 10),
					(assign, "$battle_tile_type", 114),
					(assign, "$battle_tile_menu_pop", 1),
					(jump_to_menu, "mnu_pst_battle_tile"),
				(else_try),
					(eq, ":wm_target_party_village_player_can_not_steal_cattle", 11),
					(neq, "$town_culture_type", 8),
					(neq, "$town_culture_type", 9),
					(neq, "$town_culture_type", 10),
					(assign, "$battle_tile_type", 113),
					(assign, "$battle_tile_menu_pop", 1),
					(jump_to_menu, "mnu_pst_battle_tile"),
				(else_try),
					(this_or_next|eq, "$town_culture_type", 8),
					(this_or_next|eq, "$town_culture_type", 9),
					(eq, "$town_culture_type", 10),
					(assign, "$battle_tile_type", 112),
					(assign, "$battle_tile_menu_pop", 1),
					(jump_to_menu, "mnu_pst_battle_tile"),
				(else_try),
					(assign, "$battle_tile_type", 111),
					(assign, "$battle_tile_menu_pop", 1),
					(jump_to_menu, "mnu_pst_battle_tile"),
				(try_end),
			(try_end),
		(try_end)
	],
	[
		("back",
		[],
		"[Back]",
		[
			(change_screen_map)
		], ".")
	]
	),

	("wm_battle_debrief", 0, "{s7}^^Ally {reg11}%  -  Enemy {reg12}%^^-Kill count-^Player {reg13} / Companion {reg14}^Our Infantry:{reg16} / Archer {reg17} / Cavalry {reg18}^Enemy leader {reg15}^Enemy Infantry {reg19} / Archer {reg20} / Cavalry {reg21}",
"none",
	[
		(call_script, "script_dead_num_slot_process"),
		(assign, "$ply_loot_1", 0),
		(assign, "$ply_loot_2", 0),
		(assign, "$ply_loot_3", 0),
		(assign, "$ply_loot_4", 0),
		(assign, "$ply_loot_5", 0),
		(assign, "$is_prisoner", 0),
		(assign, "$succed_siege_strategy", 0),
		(assign, "$pre_battle_result_save", 0),
		(set_background_mesh, "mesh_pic_victory"),
		(try_begin),
			(eq, "$wm_battle_result_state", 1),
			(assign, "$pre_battle_result_save", 1),
			(call_script, "script_wm_troop_type_depend_train", "$wm_target_party", 100),
			(store_random_in_range, ":random_in_range_0_7", 0, 7),
			(try_begin),
				(eq, ":random_in_range_0_7", 0),
				(assign, ":value", "$temp_party_troop_04"),
			(else_try),
				(eq, ":random_in_range_0_7", 1),
				(assign, ":value", "$temp_party_troop_05"),
			(else_try),
				(eq, ":random_in_range_0_7", 2),
				(assign, ":value", "$temp_party_troop_06"),
			(else_try),
				(eq, ":random_in_range_0_7", 3),
				(assign, ":value", "$temp_party_troop_07"),
			(else_try),
				(eq, ":random_in_range_0_7", 4),
				(assign, ":value", "$temp_party_troop_08"),
			(else_try),
				(eq, ":random_in_range_0_7", 5),
				(assign, ":value", "$temp_party_troop_09"),
			(else_try),
				(assign, ":value", "$temp_party_troop_10"),
			(try_end),
			(troop_get_inventory_capacity, ":inventory_capacity_value", ":value"),
			(try_for_range, ":localvariable", 0, ":inventory_capacity_value"),
				(troop_get_inventory_slot, ":inventory_slot_value_localvariable", ":value", ":localvariable"),
				(gt, ":inventory_slot_value_localvariable", 0),
				(store_random_in_range, ":random_in_range_0_2", 0, 2),
				(eq, ":random_in_range_0_2", 0),
				(try_begin),
					(eq, "$ply_loot_1", 0),
					(assign, "$ply_loot_1", ":inventory_slot_value_localvariable"),
				(else_try),
					(eq, "$ply_loot_2", 0),
					(assign, "$ply_loot_2", ":inventory_slot_value_localvariable"),
				(else_try),
					(eq, "$ply_loot_3", 0),
					(assign, "$ply_loot_3", ":inventory_slot_value_localvariable"),
				(else_try),
					(eq, "$ply_loot_4", 0),
					(assign, "$ply_loot_4", ":inventory_slot_value_localvariable"),
				(else_try),
					(eq, "$ply_loot_5", 0),
					(assign, "$ply_loot_5", ":inventory_slot_value_localvariable"),
				(try_end),
			(try_end),
			(store_random_in_range, ":random_in_range_6_11", 6, 11),
			(try_begin),
				(eq, ":random_in_range_6_11", 0),
				(assign, ":value_2", 1),
			(else_try),
				(eq, ":random_in_range_6_11", 1),
				(assign, ":value_2", 21),
			(else_try),
				(eq, ":random_in_range_6_11", 2),
				(assign, ":value_2", 2),
			(else_try),
				(eq, ":random_in_range_6_11", 3),
				(assign, ":value_2", 22),
			(else_try),
				(eq, ":random_in_range_6_11", 4),
				(assign, ":value_2", 5),
			(else_try),
				(eq, ":random_in_range_6_11", 5),
				(assign, ":value_2", 7),
			(else_try),
				(eq, ":random_in_range_6_11", 6),
				(assign, ":value_2", 24),
			(else_try),
				(eq, ":random_in_range_6_11", 7),
				(assign, ":value_2", 25),
			(else_try),
				(eq, ":random_in_range_6_11", 8),
				(assign, ":value_2", 26),
			(else_try),
				(eq, ":random_in_range_6_11", 9),
				(assign, ":value_2", 27),
			(else_try),
				(assign, ":value_2", 29),
			(try_end),
			(assign, "$ply_loot_modi_for_armor", ":value_2"),
			(store_random_in_range, ":random_in_range_6_11", 2, 4),
			(try_begin),
				(eq, ":random_in_range_6_11", 0),
				(assign, ":value_2", 1),
			(else_try),
				(eq, ":random_in_range_6_11", 1),
				(assign, ":value_2", 5),
			(else_try),
				(eq, ":random_in_range_6_11", 2),
				(assign, ":value_2", 25),
			(else_try),
				(assign, ":value_2", 27),
			(try_end),
			(assign, "$ply_loot_modi_for_shield", ":value_2"),
			(store_random_in_range, ":random_in_range_6_11", 4, 9),
			(try_begin),
				(eq, ":random_in_range_6_11", 0),
				(assign, ":value_2", 1),
			(else_try),
				(eq, ":random_in_range_6_11", 1),
				(assign, ":value_2", 3),
			(else_try),
				(eq, ":random_in_range_6_11", 2),
				(assign, ":value_2", 2),
			(else_try),
				(eq, ":random_in_range_6_11", 3),
				(assign, ":value_2", 4),
			(else_try),
				(eq, ":random_in_range_6_11", 4),
				(assign, ":value_2", 18),
			(else_try),
				(eq, ":random_in_range_6_11", 5),
				(assign, ":value_2", 13),
			(else_try),
				(eq, ":random_in_range_6_11", 6),
				(assign, ":value_2", 19),
			(else_try),
				(eq, ":random_in_range_6_11", 7),
				(assign, ":value_2", 14),
			(else_try),
				(assign, ":value_2", 17),
			(try_end),
			(assign, "$ply_loot_modi_for_weapon", ":value_2"),
			(store_random_in_range, ":random_in_range_6_11", 1, 2),
			(try_begin),
				(eq, ":random_in_range_6_11", 0),
				(assign, ":value_2", 3),
			(else_try),
				(assign, ":value_2", 42),
			(try_end),
			(assign, "$ply_loot_modi_for_ammo", ":value_2"),
			(store_random_in_range, ":random_in_range_6_11", 3, 6),
			(try_begin),
				(eq, ":random_in_range_6_11", 0),
				(assign, ":value_2", 30),
			(else_try),
				(eq, ":random_in_range_6_11", 1),
				(assign, ":value_2", 31),
			(else_try),
				(eq, ":random_in_range_6_11", 2),
				(assign, ":value_2", 32),
			(else_try),
				(eq, ":random_in_range_6_11", 3),
				(assign, ":value_2", 18),
			(else_try),
				(eq, ":random_in_range_6_11", 4),
				(assign, ":value_2", 35),
			(else_try),
				(assign, ":value_2", 36),
			(try_end),
			(assign, "$ply_loot_modi_for_horse", ":value_2"),
			(try_begin),
				(eq, "$qquest_type", 13),
				(party_slot_eq, "$wm_target_party", slot_party_type, 1),
				(assign, "$qquest_progress", 1),
				(display_message, "str_questsucc", 0x00ffff00),
				(play_sound, "snd_quest_succeeded"),
			(try_end),
			(try_begin),
				(eq, "$qquest_type", 14),
				(this_or_next|party_slot_eq, "$wm_target_party", slot_party_type, 1),
				(party_slot_eq, "$wm_target_party", slot_party_type, 4),
				(store_faction_of_party, ":faction_of_party_wm_target_party", "$wm_target_party"),
				(eq, "$qquest_target_faction", ":faction_of_party_wm_target_party"),
				(assign, "$qquest_progress", 1),
				(display_message, "str_questsucc", 0x00ffff00),
				(play_sound, "snd_quest_succeeded"),
			(try_end),
			(try_begin),
				(is_between, "$enemy_commander", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(troop_set_slot, "$enemy_commander", slot_troop_last_persuasion_time, 11),
				(troop_set_slot, "$enemy_commander", slot_troop_last_quest, 720),
			(try_end),
			(try_begin),
				(party_slot_eq, "$wm_target_party", slot_party_type, 7),
				(party_get_slot, ":wm_target_party_town_tavern", "$wm_target_party", slot_town_tavern),
				(is_between, ":wm_target_party_town_tavern", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(troop_set_slot, ":wm_target_party_town_tavern", slot_troop_last_persuasion_time, 12),
				(troop_set_slot, ":wm_target_party_town_tavern", slot_troop_last_quest, 720),
			(try_end),
			(try_begin),
				(this_or_next|party_slot_eq, "$wm_target_party", slot_party_type, 1),
				(party_slot_eq, "$wm_target_party", slot_party_type, 7),
				(call_script, "script_wm_troop_type_depend_train", "$wm_target_party", 0),
				(store_random_in_range, ":random_in_range_0_7", 5, 15),
				(party_add_prisoners, "p_main_party", "$temp_party_troop_01", ":random_in_range_0_7"),
				(store_sub, ":value_3", 20, ":random_in_range_0_7"),
				(party_add_prisoners, "p_main_party", "$temp_party_troop_02", ":value_3"),
				(store_random_in_range, ":random_in_range_0_7", 5, 15),
				(party_add_prisoners, "p_main_party", "$temp_party_troop_03", ":random_in_range_0_7"),
				(store_sub, ":value_3", 20, ":random_in_range_0_7"),
				(party_add_prisoners, "p_main_party", "$temp_party_troop_04", ":value_3"),
				(store_random_in_range, ":random_in_range_0_7", 5, 15),
				(party_add_prisoners, "p_main_party", "$temp_party_troop_05", ":random_in_range_0_7"),
				(store_sub, ":value_3", 20, ":random_in_range_0_7"),
				(party_add_prisoners, "p_main_party", "$temp_party_troop_06", ":value_3"),
				(store_random_in_range, ":random_in_range_0_7", 5, 15),
				(party_add_prisoners, "p_main_party", "$temp_party_troop_07", ":random_in_range_0_7"),
				(store_sub, ":value_3", 20, ":random_in_range_0_7"),
				(party_add_prisoners, "p_main_party", "$temp_party_troop_08", ":value_3"),
				(store_random_in_range, ":random_in_range_0_7", 5, 15),
				(party_add_prisoners, "p_main_party", "$temp_party_troop_09", ":random_in_range_0_7"),
				(store_sub, ":value_3", 20, ":random_in_range_0_7"),
				(party_add_prisoners, "p_main_party", "$temp_party_troop_10", ":value_3"),
			(else_try),
				(call_script, "script_wm_troop_type_depend_train", "$wm_target_party", 0),
				(store_add, ":value_4", "$enemy_army_size", 3),
				(val_div, ":value_4", 3),
				(party_add_prisoners, "p_main_party", "$temp_party_troop_01", ":value_4"),
			(try_end),
			(try_begin),
				(party_slot_eq, "$wm_target_party", slot_party_type, 3),
				(party_get_slot, ":wm_target_party_town_horse_merchant", "$wm_target_party", slot_town_horse_merchant),
				(try_begin),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_020"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_021"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_022"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_023"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_024"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_025"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_026"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_027"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_028"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_029"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_030"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_031"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_032"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_033"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_034"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_035"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_036"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_037"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_038"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_044"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_045"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_046"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_047"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_048"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_049"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_050"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_051"),
					(this_or_next|eq, "$enemy_commander", "trp_ex_npc_052"),
					(eq, "$enemy_commander", "trp_ex_npc_053"),
					(try_begin),
						(eq, "$qquest_type", 31),
						(eq, "$qquest_target_troop", "$enemy_commander"),
						(play_sound, "snd_quest_succeeded"),
						(assign, "$qquest_progress", 1),
						(store_random_in_range, ":random_in_range_0_100", 0, 100),
						(try_begin),
							(gt, "$policy_tracker", 0),
							(le, "$policy_tracker", 5),
							(store_mul, ":value_5", "$policy_tracker", 6),
							(val_sub, ":random_in_range_0_100", ":value_5"),
						(try_end),
						(try_begin),
							(lt, ":random_in_range_0_100", 50),
							(str_store_troop_name, 8, "$enemy_commander"),
							(display_message, "str_captured_pirate_comment", 0x00ffff00),
							(party_force_add_prisoners, "p_main_party", "$enemy_commander", 1),
						(try_end),
						(display_message, "str_questsucc", 0x00ffff00),
					(try_end),
					(try_begin),
						(eq, "$pirate_king", 0),
						(troop_get_slot, ":enemy_commander_last_persuasion_time", "$enemy_commander", slot_troop_last_persuasion_time),
						(lt, ":enemy_commander_last_persuasion_time", 3),
						(val_add, ":enemy_commander_last_persuasion_time", 1),
						(troop_set_slot, "$enemy_commander", slot_troop_last_persuasion_time, ":enemy_commander_last_persuasion_time"),
					(try_end),
				(try_end),
			(try_end),
			(str_store_string, 7, "str_debrif_victory"),
		(else_try),
			(eq, "$wm_battle_result_state", 2),
			(assign, "$pre_battle_result_save", 2),
			(str_store_string, 7, "str_debrif_defeat"),
			(call_script, "script_main_party_escape_pos_set"),
			(call_script, "script_remove_all_prisoners"),
		(else_try),
			(eq, "$wm_battle_result_state", 3),
			(assign, "$pre_battle_result_save", 3),
			(try_begin),
				(is_between, "$enemy_commander", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(troop_set_slot, "$enemy_commander", slot_troop_last_persuasion_time, 13),
				(troop_set_slot, "$enemy_commander", slot_troop_last_quest, 720),
			(try_end),
			(str_store_string, 7, "str_debrif_retreat"),
			(call_script, "script_main_party_escape_pos_set"),
			(call_script, "script_remove_all_prisoners"),
		(else_try),
			(eq, "$wm_battle_result_state", 4),
			(assign, "$pre_battle_result_save", 4),
			(str_store_string, 7, "str_debrif_ai_retreat"),
			(try_begin),
				(party_slot_eq, "$wm_target_party", slot_party_type, 1),
				(party_get_position, 11, "p_main_party"),
				(map_get_land_position_around_position, 12, 11, 12),
				(party_set_position, "$wm_target_party", 12),
			(try_end),
		(try_end),
		(try_begin),
			(eq, "$wm_battle_result_state", 1),
			(is_between, "$player_assistant_1", "trp_tt_lord_01_00", "trp_tt_lord_end"),
			(try_begin),
				(party_slot_eq, "$wm_target_party", slot_party_type, 1),
				(troop_set_slot, "$player_assistant_1", slot_troop_last_persuasion_time, 1),
				(troop_set_slot, "$player_assistant_1", slot_troop_last_quest, 120),
			(else_try),
				(party_slot_eq, "$wm_target_party", slot_party_type, 7),
				(troop_set_slot, "$player_assistant_1", slot_troop_last_persuasion_time, 2),
				(troop_set_slot, "$player_assistant_1", slot_troop_last_quest, 120),
			(try_end),
		(try_end),
		(try_begin),
			(eq, "$player_has_ally", 1),
			(try_for_range, ":number", 56, 76),
				(faction_get_slot, ":ally_faction_for_slot_number", "fac_ally_faction_for_slot", ":number"),
				(gt, ":ally_faction_for_slot_number", 0),
				(party_is_active, ":ally_faction_for_slot_number"),
				(neg|is_between, ":ally_faction_for_slot_number", "p_temp_party", "p_reserved_5"),
				(neq, ":ally_faction_for_slot_number", "p_reserved_5"),
				(party_slot_eq, ":ally_faction_for_slot_number", slot_party_type, 1),
				(store_faction_of_party, ":faction_of_party_ally_faction_for_slot_number", ":ally_faction_for_slot_number"),
				(eq, ":faction_of_party_ally_faction_for_slot_number", "$wm_player_fac"),
				(party_get_slot, ":wm_target_party_town_horse_merchant", ":ally_faction_for_slot_number", slot_town_horse_merchant),
				(store_div, ":value_6", "$enemy_army_size", 2),
				(try_begin),
					(this_or_next|eq, "$wm_battle_result_state", 1),
					(eq, "$wm_battle_result_state", 4),
					(try_begin),
						(eq, "$player_assist_lord", 1),
						(gt, "$player_army_size", ":value_6"),
						(party_slot_eq, "$wm_target_party", slot_party_type, 1),
						(neg|troop_slot_eq, ":wm_target_party_town_horse_merchant", slot_troop_player_order_object, 3),
						(neg|troop_slot_eq, ":wm_target_party_town_horse_merchant", slot_troop_player_order_object, 4),
						(troop_set_slot, ":wm_target_party_town_horse_merchant", slot_troop_last_persuasion_time, 5),
						(troop_set_slot, ":wm_target_party_town_horse_merchant", slot_troop_last_quest, 2),
					(else_try),
						(eq, "$player_assist_lord", 1),
						(party_slot_eq, "$wm_target_party", slot_party_type, 1),
						(troop_set_slot, ":wm_target_party_town_horse_merchant", slot_troop_last_persuasion_time, 4),
						(troop_set_slot, ":wm_target_party_town_horse_merchant", slot_troop_last_quest, 2),
					(else_try),
						(party_slot_eq, "$wm_target_party", slot_party_type, 1),
						(troop_set_slot, ":wm_target_party_town_horse_merchant", slot_troop_last_persuasion_time, 1),
						(troop_set_slot, ":wm_target_party_town_horse_merchant", slot_troop_last_quest, 120),
					(else_try),
						(party_slot_eq, "$wm_target_party", slot_party_type, 7),
						(troop_set_slot, ":wm_target_party_town_horse_merchant", slot_troop_last_persuasion_time, 2),
						(troop_set_slot, ":wm_target_party_town_horse_merchant", slot_troop_last_quest, 120),
					(try_end),
				(else_try),
					(eq, "$wm_battle_result_state", 3),
					(try_begin),
						(party_slot_eq, "$wm_target_party", slot_party_type, 1),
						(troop_set_slot, ":wm_target_party_town_horse_merchant", slot_troop_last_persuasion_time, 3),
						(troop_set_slot, ":wm_target_party_town_horse_merchant", slot_troop_last_quest, 120),
					(else_try),
						(party_slot_eq, "$wm_target_party", slot_party_type, 7),
						(troop_set_slot, ":wm_target_party_town_horse_merchant", slot_troop_last_persuasion_time, 3),
						(troop_set_slot, ":wm_target_party_town_horse_merchant", slot_troop_last_quest, 120),
					(try_end),
				(try_end),
			(try_end),
		(try_end),
		(store_sub, ":value_7", "$count_player_team", "$troop_alive_player"),
		(val_mul, ":value_7", 100),
		(val_div, ":value_7", "$count_player_team"),
		(store_sub, ":value_8", 100, ":value_7"),
		(store_sub, ":value_9", "$count_enemy_team", "$troop_alive_enemy"),
		(val_mul, ":value_9", 100),
		(val_div, ":value_9", "$count_enemy_team"),
		(store_sub, ":value_10", 100, ":value_9"),
		(try_begin),
			(gt, ":value_8", 100),
			(assign, ":value_8", 100),
		(try_end),
		(try_begin),
			(gt, ":value_10", 100),
			(assign, ":value_10", 100),
		(try_end),
		(try_begin),
			(lt, ":value_8", 0),
			(assign, ":value_8", 0),
		(try_end),
		(try_begin),
			(lt, ":value_10", 0),
			(assign, ":value_10", 0),
		(try_end),
		(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
		(try_begin),
			(eq, "$wm_battle_result_state", 1),
			(eq, "$low_encounter_battle", 1),
			(gt, ":party_size_wo_prisoners_main_party", 300),
			(assign, ":value_10", 0),
			(try_begin),
				(lt, ":value_8", 90),
				(assign, ":value_8", 90),
			(try_end),
		(else_try),
			(eq, "$wm_battle_result_state", 1),
			(assign, ":value_10", 0),
		(else_try),
			(eq, "$wm_battle_result_state", 2),
			(eq, "$low_encounter_battle", 1),
			(gt, ":party_size_wo_prisoners_main_party", 300),
			(assign, ":value_8", 75),
		(else_try),
			(eq, "$wm_battle_result_state", 2),
			(assign, ":value_8", 0),
		(try_end),
		(store_sub, ":value_11", 100, ":value_8"),
		(val_mul, ":value_11", 24),
		(try_begin),
			(eq, "$wm_battle_result_state", 1),
			(lt, ":value_8", 100),
			(val_mul, ":value_11", 2),
			(val_div, ":value_11", 10),
			(call_script, "script_exp_reward_for_common_troop", 48),
			(call_script, "script_exp_reward_for_common_troop", ":value_11"),
		(else_try),
			(eq, "$wm_battle_result_state", 2),
			(call_script, "script_exp_reward_for_common_troop", 48),
		(else_try),
			(eq, "$wm_battle_result_state", 4),
			(lt, ":value_8", 100),
			(val_mul, ":value_11", 2),
			(val_div, ":value_11", 10),
			(call_script, "script_exp_reward_for_common_troop", 48),
			(call_script, "script_exp_reward_for_common_troop", ":value_11"),
		(try_end),
		(store_mul, ":value_12", "$player_army_size", ":value_7"),
		(try_begin),
			(ge, ":value_12", 100),
			(val_div, ":value_12", 100),
		(else_try),
			(assign, ":value_12", 0),
		(try_end),
		(store_mul, ":value_13", "$enemy_army_size", ":value_9"),
		(try_begin),
			(ge, ":value_13", 100),
			(val_div, ":value_13", 100),
		(else_try),
			(assign, ":value_13", 0),
		(try_end),
		(store_faction_of_party, ":faction_of_party_wm_target_party_2", "$wm_target_party"),
		(assign, "$loot_reward_money", 0),
		(assign, "$loot_reward_contri", 0),
		(assign, "$loot_reward_honor", 0),
		(assign, "$loot_reward_battle_exp", 0),
		(assign, "$loot_reward_adv_exp", 0),
		(try_begin),
			(eq, "$wm_battle_result_state", 1),
			(call_script, "script_wm_fac_relation_diff", "$wm_player_fac", ":faction_of_party_wm_target_party_2", -20),
			(try_begin),
				(this_or_next|is_between, "$wm_target_party", "p_pyongyang", "p_place_end"),
				(party_slot_eq, "$wm_target_party", slot_party_type, 1),
				(try_begin),
					(gt, ":value_13", 0),
					(store_mul, ":value_14", ":value_13", 1),
					(val_sub, ":value_14", ":value_12"),
					(gt, ":value_14", 0),
					(call_script, "script_party_money_level_diff", "p_main_party", ":value_14", 87),
					(assign, "$loot_reward_money", ":value_14"),
				(try_end),
				(try_begin),
					(party_slot_eq, "$wm_target_party", slot_party_type, 1),
					(gt, ":value_13", 0),
					(store_mul, ":value_15", ":value_13", 3),
					(val_sub, ":value_15", ":value_12"),
					(gt, ":value_15", 0),
					(call_script, "script_party_food_level_diff", "p_main_party", ":value_15", 87),
				(try_end),
			(try_end),
			(try_begin),
				(is_between, "$wm_target_party", "p_pyongyang", "p_place_end"),
				(assign, "$loot_reward_contri", 45),
				(assign, "$loot_reward_honor", 3),
				(assign, "$loot_reward_battle_exp", 200),
				(assign, "$loot_reward_adv_exp", 100),
				(call_script, "script_troop_contribution_diff", "trp_player", 15, 87),
				(call_script, "script_wm_honor_change_diff", "trp_player", 1, 87),
				(call_script, "script_battle_exp_diff", 100, 87),
				(call_script, "script_adv_exp_diff", 35, 87),
				(party_get_slot, ":wm_target_party_town_store", "$wm_target_party", slot_town_store),
				(try_begin),
					(gt, ":wm_target_party_town_store", 0),
					(store_mul, ":value_14", ":wm_target_party_town_store", 200),
					(call_script, "script_party_money_level_diff", "p_main_party", ":value_14", 87),
				(try_end),
				(call_script, "script_wm_after_battle_progress", 1500),
			(else_try),
				(party_slot_eq, "$wm_target_party", slot_party_type, 1),
				(assign, "$loot_reward_contri", 40),
				(assign, "$loot_reward_honor", 2),
				(assign, "$loot_reward_battle_exp", 200),
				(assign, "$loot_reward_adv_exp", 100),
				(call_script, "script_troop_contribution_diff", "trp_player", 10, 87),
				(call_script, "script_wm_honor_change_diff", "trp_player", 1, 87),
				(call_script, "script_battle_exp_diff", 100, 87),
				(call_script, "script_adv_exp_diff", 30, 87),
				(call_script, "script_wm_after_battle_progress", 1000),
			(else_try),
				(party_slot_eq, "$wm_target_party", slot_party_type, 4),
				(assign, "$loot_reward_battle_exp", 100),
				(assign, "$loot_reward_adv_exp", 50),
				(call_script, "script_wm_honor_change_diff", "trp_player", 2, 34),
				(call_script, "script_battle_exp_diff", 100, 87),
				(call_script, "script_adv_exp_diff", 25, 87),
				(store_mul, ":value_16", 1000, 2),
				(store_mul, ":value_17", 1000, 5),
				(store_random_in_range, ":value_14", ":value_16", ":value_17"),
				(try_begin),
					(eq, "$r_player_class", 5),
					(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
					(this_or_next|eq, ":current_terrain_main_party", 7),
					(eq, ":current_terrain_main_party", 2),
					(val_mul, ":value_14", 2),
				(else_try),
					(eq, "$r_player_class", 4),
					(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
					(neq, ":current_terrain_main_party", 7),
					(neq, ":current_terrain_main_party", 2),
					(val_mul, ":value_14", 2),
				(try_end),
				(call_script, "script_party_money_level_diff", "p_main_party", ":value_14", 87),
				(call_script, "script_wm_after_battle_progress", 400),
			(else_try),
				(assign, "$loot_reward_honor", 1),
				(assign, "$loot_reward_battle_exp", 100),
				(assign, "$loot_reward_adv_exp", 50),
				(call_script, "script_wm_honor_change_diff", "trp_player", 1, 87),
				(call_script, "script_battle_exp_diff", 100, 87),
				(call_script, "script_adv_exp_diff", 25, 87),
				(store_mul, ":value_16", 1000, 1),
				(store_mul, ":value_17", 1000, 4),
				(store_random_in_range, ":value_14", ":value_16", ":value_17"),
				(call_script, "script_party_money_level_diff", "p_main_party", ":value_14", 87),
				(call_script, "script_wm_after_battle_progress", 400),
			(try_end),
			(try_begin),
				(is_between, "$enemy_commander", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(call_script, "script_battle_count_won", "trp_player"),
			(try_end),
			(call_script, "script_battle_count_lose", "$enemy_commander"),
		(else_try),
			(eq, "$wm_battle_result_state", 2),
			(call_script, "script_wm_fac_relation_diff", "$wm_player_fac", ":faction_of_party_wm_target_party_2", -20),
			(call_script, "script_troop_contribution_diff", "trp_player", 100, 34),
			(call_script, "script_wm_honor_change_diff", "trp_player", 2, 34),
			(call_script, "script_battle_exp_diff", 1000, 34),
			(call_script, "script_adv_exp_diff", 1000, 34),
			(call_script, "script_battle_count_lose", "trp_player"),
			(call_script, "script_battle_count_won", "$enemy_commander"),
			(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
			(try_begin),
				(this_or_next|eq, ":current_terrain_main_party", 7),
				(eq, ":current_terrain_main_party", 2),
				(call_script, "script_ship_rand_lost"),
				(call_script, "script_ship_rand_lost"),
			(try_end),
			(store_random_in_range, ":random_in_range_0_7", 0, 100),
			(try_begin),
				(ge, ":random_in_range_0_7", 50),
				(assign, "$is_prisoner", 1),
			(try_end),
			(try_begin),
				(eq, "$low_encounter_battle", 1),
				(gt, ":party_size_wo_prisoners_main_party", 300),
				(assign, "$is_prisoner", 0),
			(try_end),
			(call_script, "script_wm_after_battle_health_result"),
			(try_begin),
				(eq, "$low_encounter_battle", 1),
				(gt, ":party_size_wo_prisoners_main_party", 300),
				(call_script, "script_stack_kill_sc", 25, 0, 0, 0),
			(else_try),
				(call_script, "script_stack_kill_sc", 50, 0, 0, 0),
			(try_end),
		(else_try),
			(eq, "$wm_battle_result_state", 3),
			(call_script, "script_wm_fac_relation_diff", "$wm_player_fac", ":faction_of_party_wm_target_party_2", -20),
			(call_script, "script_wm_after_battle_health_result"),
			(try_begin),
				(eq, "$low_encounter_battle", 1),
				(gt, ":party_size_wo_prisoners_main_party", 300),
				(call_script, "script_stack_kill_sc", 15, 0, 2, 0),
			(else_try),
				(call_script, "script_stack_kill_sc", 35, 0, 2, 0),
			(try_end),
			(call_script, "script_party_equip_divide", "p_main_party", 66),
		(else_try),
			(eq, "$wm_battle_result_state", 4),
			(call_script, "script_wm_fac_relation_diff", "$wm_player_fac", ":faction_of_party_wm_target_party_2", -20),
			(call_script, "script_party_equip_divide", "$wm_player_fac", 66),
			(party_get_slot, ":wm_target_party_town_prison", "$wm_target_party", slot_town_prison),
			(call_script, "script_new_party_ai", "$wm_target_party", 6, ":wm_target_party_town_prison"),
			(try_begin),
				(gt, ":value_13", 0),
				(store_mul, ":value_14", ":value_13", 1),
				(val_sub, ":value_14", ":value_12"),
				(gt, ":value_14", 0),
				(call_script, "script_party_money_level_diff", "p_main_party", ":value_14", 87),
			(try_end),
			(try_begin),
				(gt, ":value_13", 0),
				(store_mul, ":value_15", ":value_13", 2),
				(val_sub, ":value_15", ":value_12"),
				(gt, ":value_15", 0),
				(call_script, "script_party_food_level_diff", "p_main_party", ":value_15", 87),
			(try_end),
		(try_end),
		(try_begin),
			(gt, ":value_8", 0),
			(lt, ":value_8", 70),
			(store_add, ":value_18", ":value_8", 30),
			(call_script, "script_party_equip_divide", "p_main_party", ":value_18"),
		(try_end),
		(try_begin),
			(lt, ":value_8", 100),
			(call_script, "script_party_army_size_execute", "p_main_party", ":value_8", 3),
		(try_end),
		(try_begin),
			(eq, "$player_has_ally", 1),
			(try_for_range, ":number", 56, 76),
				(faction_get_slot, ":ally_faction_for_slot_number", "fac_ally_faction_for_slot", ":number"),
				(gt, ":ally_faction_for_slot_number", 0),
				(party_is_active, ":ally_faction_for_slot_number"),
				(neg|is_between, ":ally_faction_for_slot_number", "p_temp_party", "p_reserved_5"),
				(neq, ":ally_faction_for_slot_number", "p_reserved_5"),
				(party_slot_eq, ":ally_faction_for_slot_number", slot_party_type, 1),
				(store_faction_of_party, ":faction_of_party_ally_faction_for_slot_number", ":ally_faction_for_slot_number"),
				(eq, ":faction_of_party_ally_faction_for_slot_number", "$wm_player_fac"),
				(call_script, "script_party_army_size_execute", ":ally_faction_for_slot_number", ":value_8", 3),
				(try_begin),
					(eq, "$wm_battle_result_state", 2),
					(neg|is_between, ":ally_faction_for_slot_number", "p_temp_party", "p_reserved_5"),
					(neq, ":ally_faction_for_slot_number", "p_reserved_5"),
					(call_script, "script_ai_army_initialize", ":ally_faction_for_slot_number"),
				(else_try),
				(try_end),
			(try_end),
		(try_end),
		(call_script, "script_party_army_size_execute", "$wm_target_party", ":value_10", 3),
		(try_begin),
			(eq, "$enemy_has_ally", 1),
			(try_for_range, ":number", 56, 76),
				(faction_get_slot, ":ally_faction_for_slot_number", "fac_enemy_faction_for_slot", ":number"),
				(gt, ":ally_faction_for_slot_number", 0),
				(party_is_active, ":ally_faction_for_slot_number"),
				(neg|is_between, ":ally_faction_for_slot_number", "p_temp_party", "p_reserved_5"),
				(neq, ":ally_faction_for_slot_number", "p_reserved_5"),
				(party_slot_eq, ":ally_faction_for_slot_number", slot_party_type, 1),
				(store_faction_of_party, ":faction_of_party_ally_faction_for_slot_number", ":ally_faction_for_slot_number"),
				(eq, ":faction_of_party_ally_faction_for_slot_number", ":faction_of_party_wm_target_party_2"),
				(call_script, "script_party_army_size_execute", ":ally_faction_for_slot_number", ":value_10", 3),
				(try_begin),
					(eq, "$wm_battle_result_state", 1),
					(neg|is_between, ":ally_faction_for_slot_number", "p_temp_party", "p_reserved_5"),
					(neq, ":ally_faction_for_slot_number", "p_reserved_5"),
					(call_script, "script_ai_army_initialize", ":ally_faction_for_slot_number"),
				(else_try),
				(try_end),
			(try_end),
		(try_end),
		(try_begin),
			(eq, "$wm_battle_result_state", 1),
			(try_begin),
				(this_or_next|party_slot_eq, "$wm_target_party", slot_party_type, 2),
				(this_or_next|party_slot_eq, "$wm_target_party", slot_party_type, 3),
				(party_slot_eq, "$wm_target_party", slot_party_type, 4),
				(try_begin),
					(gt, "$workshop_target_party", 0),
					(store_party_size_wo_prisoners, ":party_size_wo_prisoners_wm_target_party", "$wm_target_party"),
					(gt, ":party_size_wo_prisoners_wm_target_party", 6),
					(val_div, ":party_size_wo_prisoners_wm_target_party", 3),
					(val_add, "$workshop_slave", ":party_size_wo_prisoners_wm_target_party"),
					(try_begin),
						(gt, "$workshop_slave", 400),
						(assign, "$workshop_slave", 400),
					(try_end),
					(assign, reg8, "$workshop_slave"),
					(display_message, "str_cur_slave", 0x00ff9000),
				(try_end),
				(call_script, "script_ai_army_initialize", "$wm_target_party"),
			(else_try),
				(party_slot_eq, "$wm_target_party", slot_party_type, 1),
				(call_script, "script_ai_army_initialize", "$wm_target_party"),
			(else_try),
				(is_between, "$wm_target_party", "p_pyongyang", "p_place_end"),
				(store_random_in_range, ":random_in_range_0_100", 0, 100),
				(try_begin),
					(gt, "$policy_lascivious", 0),
					(le, "$policy_lascivious", 5),
					(store_mul, ":value_5", "$policy_lascivious", 6),
					(val_sub, ":random_in_range_0_100", ":value_5"),
				(try_end),
				(try_begin),
					(lt, ":random_in_range_0_100", 50),
					(party_get_slot, ":wm_target_party_town_tavern", "$wm_target_party", slot_town_tavern),
					(try_begin),
						(is_between, ":wm_target_party_town_tavern", "trp_tt_lord_01_00", "trp_tt_lord_end"),
						(call_script, "script_temp_save_number11_initialize"),
						(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
							(neg|troop_slot_eq, "trp_player", slot_troop_state, ":troop"),
							(neg|troop_slot_eq, ":troop", slot_troop_leaded_party, 3),
							(troop_slot_eq, ":wm_target_party_town_tavern", slot_troop_state, ":troop"),
							(troop_slot_eq, ":troop", slot_troop_state, ":wm_target_party_town_tavern"),
							(call_script, "script_temp_save_number11_inject", ":troop"),
						(try_end),
						(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
							(neg|troop_slot_eq, "trp_player", slot_troop_state, ":troop"),
							(neg|troop_slot_eq, ":troop", slot_troop_leaded_party, 3),
							(troop_slot_eq, ":troop", slot_troop_last_talk_time, ":wm_target_party_town_tavern"),
							(call_script, "script_temp_save_number11_inject", ":troop"),
						(try_end),
						(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
							(neg|troop_slot_eq, "trp_player", slot_troop_state, ":troop"),
							(neg|troop_slot_eq, ":troop", slot_troop_leaded_party, 3),
							(troop_slot_eq, ":troop", slot_troop_party_template, ":wm_target_party_town_tavern"),
							(call_script, "script_temp_save_number11_inject", ":troop"),
						(try_end),
						(call_script, "script_temp_save_number11_choice_rand"),
						(is_between, "$wm_target_number11", "trp_tt_lady_01_01", "trp_tt_lady_end"),
						(assign, "$molda_start_map_conversation", "$wm_target_number11"),
						(str_store_troop_name, 3, "$molda_start_map_conversation"),
						(display_message, "str_ply_capture_lady", 0x00ff9000),
					(try_end),
				(try_end),
				(call_script, "script_defeat_town_capture_execute", "$wm_target_party", "$wm_player_fac"),
			(try_end),
		(else_try),
			(eq, "$wm_battle_result_state", 2),
			(try_begin),
				(eq, "$is_siege_defence", 1),
				(is_between, "$g_encountered_party", "p_pyongyang", "p_place_end"),
				(store_faction_of_party, ":faction_of_party_wm_target_party_2", "$wm_target_party"),
				(call_script, "script_defeat_town_capture_execute", "$g_encountered_party", ":faction_of_party_wm_target_party_2"),
			(try_end),
		(try_end),
		(assign, "$wm_battle_result_state", 0),
		(assign, reg11, ":value_8"),
		(assign, reg12, ":value_10"),
		(assign, reg13, "$bt_kill_count_player"),
		(assign, reg14, "$bt_kill_count_ally_hero"),
		(assign, reg15, "$bt_kill_count_enemy_hero"),
		(assign, reg16, "$bt_kill_count_ply_inf"),
		(assign, reg17, "$bt_kill_count_ply_arc"),
		(assign, reg18, "$bt_kill_count_ply_cav"),
		(assign, reg19, "$bt_kill_count_ene_inf"),
		(assign, reg20, "$bt_kill_count_ene_arc"),
		(assign, reg21, "$bt_kill_count_ene_cav"),
		(jump_to_menu, "mnu_pst_debrif"),
		#####MUSICBOX
		(try_begin),
		(eq, "$additional_music", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
		(eq, "$additional_music_stop", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
		(assign, "$additional_music_stop", 0), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
		(music_set_situation, mtf_sit_travel),
		(play_track, "track_reset_silence", 1),
		(try_end),
	],
	[
		("wm_back_to_map",
		[],
		"[Continue]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return"),
			#####MUSICBOX
		(try_begin),
		(eq, "$additional_music", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
		(eq, "$additional_music_stop", 1), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
		(assign, "$additional_music_stop", 0), #Obtained from Mod Options, affects mission templates, range: ALL SP Hostile music.
		(music_set_situation, mtf_sit_travel),
		(play_track, "track_reset_silence", 1),
		(try_end),

		], ".")
	]
	),

	("wm_player_prisoner", 0, "The enemy has imprisoned you.^They are offering you a choice.",
"none",
	[
							#####Wounded OSP Begin
				   (try_begin),
	   (eq, "$hardcore_mode", 1),
      (call_script, "script_rr6"),#
	  (try_end),
	  	   #####Wounded OSP End
	
		(assign, "$is_prisoner", 0),
		(set_background_mesh, "mesh_pic_prisoner_man"),
				#player execution begin
		(store_random_in_range, ":var2", 1, 100),
        #(store_faction_of_party, ":var3", "$capturer_party"),
		  (try_begin),
          (le, ":var2", "$g_player_death"),
          (neq, "$g_player_death", 0),
          #(neq, ":var3", "fac_outlaws"),
          (set_show_messages, 0),
          (jump_to_menu, "mnu_death_game_over"),
          (play_sound, "snd_decapitation"),
          #(play_track, "track_ext_player_death", 1), #Better to play tracks in the menu rather.
          (troop_get_type, ":var4", "trp_player"),
          (try_begin),
          (eq, ":var4", 0),
          (play_sound, "snd_man_die"),
          (else_try),
          (play_sound, "snd_woman_die"),
          (try_end),
          (else_try),
		#player execution end
		
	],
	[
		("wm_bribe_capture",
		[],
		"Negotiate : Pay 3/4 of your wealth.",
		[
			(store_mul, ":value", 500, 10),
			(try_begin),
				(call_script, "script_party_money_level_ge", "p_main_party", ":value"),
				(eq, "$wm_mo_continue", 1),
				(call_script, "script_party_money_level_set_percent", "p_main_party", 25),
				(call_script, "script_initialize_main_party"),
				(display_message, "str_ply_capture_nego", 0x00ffff00),
				(set_show_messages, 0),
				(troop_get_inventory_capacity, ":inventory_capacity_player", "trp_player"),
				(try_for_range, ":localvariable", 0, ":inventory_capacity_player"),
					(troop_get_inventory_slot, ":inventory_slot_player_localvariable", "trp_player", ":localvariable"),
					(is_between, ":inventory_slot_player_localvariable", 92, 117),
					(troop_inventory_slot_get_item_amount, ":troop_inventory_slot_item_amount_player_localvariable", "trp_player", ":localvariable"),
					(troop_remove_items, "trp_player", ":inventory_slot_player_localvariable", ":troop_inventory_slot_item_amount_player_localvariable"),
				(try_end),
				(set_show_messages, 1),
				(call_script, "script_adv_exp_diff", 1000, 34),
				(call_script, "script_battle_exp_diff", 1000, 34),
				(call_script, "script_troop_contribution_diff", "trp_player", 100, 34),
				(try_begin),
					(troop_slot_ge, "trp_player", 13, 2),
					(call_script, "script_wm_honor_change_diff", "trp_player", 2, 34),
				(try_end),
				(call_script, "script_main_party_escape_pos_set"),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(display_message, "str_money_too_little", 0x00ff0000),
			(try_end)
		], "."),

		("wm_loooted",
		[],
		"Surrender : Surrender all your valuable equipment.",
		[
			(try_begin),
				(call_script, "script_party_money_level_set_percent", "p_main_party", 25),
				(call_script, "script_initialize_main_party"),
				(set_show_messages, 0),
				(troop_get_inventory_capacity, ":inventory_capacity_player", "trp_player"),
				(try_for_range, ":localvariable", 0, ":inventory_capacity_player"),
					(troop_get_inventory_slot, ":inventory_slot_player_localvariable", "trp_player", ":localvariable"),
					(is_between, ":inventory_slot_player_localvariable", 92, 117),
					(troop_inventory_slot_get_item_amount, ":troop_inventory_slot_item_amount_player_localvariable", "trp_player", ":localvariable"),
					(troop_remove_items, "trp_player", ":inventory_slot_player_localvariable", ":troop_inventory_slot_item_amount_player_localvariable"),
				(try_end),
				(set_show_messages, 1),
				(call_script, "script_adv_exp_diff", 1000, 34),
				(call_script, "script_battle_exp_diff", 1000, 34),
				(call_script, "script_troop_contribution_diff", "trp_player", 100, 34),
				(try_begin),
					(troop_slot_ge, "trp_player", 13, 2),
					(call_script, "script_wm_honor_change_diff", "trp_player", 2, 34),
				(try_end),
				(call_script, "script_wm_loot_progress", 0, 1, 6),
				(call_script, "script_wm_loot_progress", "trp_elite_troops_01", "trp_elite_troops_end", 20),
				(call_script, "script_main_party_escape_pos_set"),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(try_end)
		], "."),

		("wm_join_enemy_fac",
		[
			(troop_slot_ge, "trp_player", 18, 11),
			(party_slot_eq, "$wm_target_party", slot_party_type, 1),
			(store_faction_of_party, ":faction_of_party_wm_target_party", "$wm_target_party"),
			(is_between, ":faction_of_party_wm_target_party", "fac_kingdom_1", "fac_kingdoms_end"),
			(call_script, "script_check_faction_lord_list15_number", ":faction_of_party_wm_target_party"),
			(eq, "$wm_stp_continue", 1),
			(is_between, "$wm_player_fac", "fac_kingdom_1", "fac_kingdoms_end"),
			(neg|faction_slot_eq, "$wm_player_fac", 1, "trp_player")
		],
		"Betrayal : Join the enemy faction.",
		[
			(jump_to_menu, "mnu_betray_fac_menu")
		], ".")
	]
	),

	("wm_visit_port", 0, "--{s11}--^^Relation: {reg17}",
"none",
	[
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", slot_town_prosperity, 1),
			(party_set_flags, "$g_encountered_party", 16384, 1),
			(party_set_slot, "$g_encountered_party", slot_town_prosperity, 1),
		(try_end),
		(party_get_slot, reg17, "$g_encountered_party", slot_town_prison),
		(str_store_party_name, 11, "$g_encountered_party"),
		(set_background_mesh, "mesh_pic_xex8"),
		(try_begin),
			(eq, "$m_ship_type_1", 1401),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_caravel"),
		(else_try),
			(eq, "$m_ship_type_1", 1402),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_carrack"),
		(else_try),
			(eq, "$m_ship_type_1", 1403),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_xebec"),
		(else_try),
			(eq, "$m_ship_type_1", 1404),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_galley"),
		(else_try),
			(eq, "$m_ship_type_1", 1405),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_galleon"),
		(else_try),
			(eq, "$m_ship_type_1", 1406),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_turship"),
		(else_try),
			(eq, "$m_ship_type_1", 1407),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_junkship"),
		(else_try),
			(eq, "$m_ship_type_1", 1408),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_panship"),
		(else_try),
			(eq, "$m_ship_type_1", 1409),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_galleon"),
		(else_try),
			(eq, "$m_ship_type_1", 1410),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_dragonship"),
		(else_try),
			(eq, "$m_ship_type_1", 1411),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_galleas"),
		(else_try),
			(eq, "$m_ship_type_1", 1412),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_black_ship"),
		(else_try),
			(eq, "$m_ship_type_1", 1413),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_black_ship"),
		(else_try),
			(eq, "$m_ship_type_1", 1414),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_antecship"),
		(else_try),
			(eq, "$m_ship_type_1", 1415),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_nugakship"),
		(else_try),
			(eq, "$m_ship_type_1", 1416),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_panokship"),
		(else_try),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_ship"),
		(try_end),
		(try_begin),
			(is_between, "$g_encountered_party", "p_tradeport1", "p_tradeport_end"),
			(set_show_messages, 0),
			(party_get_slot, ":main_party_center_siege_with_belfry", "p_main_party", slot_center_siege_with_belfry),
			(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
			(val_mul, ":party_size_wo_prisoners_main_party", 3),
			(val_div, ":party_size_wo_prisoners_main_party", 2),
			(set_show_messages, 1),
			(lt, ":main_party_center_siege_with_belfry", ":party_size_wo_prisoners_main_party"),
			(set_show_messages, 0),
			(store_sub, ":value", ":party_size_wo_prisoners_main_party", ":main_party_center_siege_with_belfry"),
			(store_div, ":value_2", ":value", 10),
			(party_get_slot, ":main_party_29", "p_main_party", 29),
			(val_div, ":main_party_29", 37),
			(set_show_messages, 1),
			(ge, ":main_party_29", ":value_2"),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value_2", 34),
			(call_script, "script_party_food_level_diff", "p_main_party", ":value", 87),
			(display_message, "str_food_compl", 0x0000ff00),
		(try_end)
	],
	[
		("main_q_massawa_63",
		[
			(eq, "$g_encountered_party", "p_tradeport97"),
			(this_or_next|eq, "$main_q_step", 63),
			(eq, "$main_q_step", 64)
		],
		"[Find the clue about the Catholic Kingdom.]",
		[
			(assign, "$main_q_step", 64),
			(jump_to_menu, "mnu_main_quest_menu")
		], "."),

		("main_q_abadan_67",
		[
			(eq, "$g_encountered_party", "p_tradeport71"),
			(eq, "$main_q_step", 67)
		],
		"[Wait until the courier tries to contact.]",
		[
			(assign, "$main_q_step", 68),
			(jump_to_menu, "mnu_wm_pst_map_return"),
			(rest_for_hours, 24, 5, 0)
		], "."),

		("main_q_abadan_68",
		[
			(eq, "$g_encountered_party", "p_tradeport71"),
			(eq, "$main_q_step", 68)
		],
		"[No one approach to you.]",
		[
			(assign, "$main_q_step", 69),
			(assign, "$main_q_day", 30),
			(display_message, "str_mq_1_68mess"),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("named_pirate",
		[
			(eq, "$qquest_type", 0),
			(assign, "$temp_num_01", 0),
			(assign, "$temp_num_02", 0),
			(try_for_parties, ":var_1"),
				(neq, ":var_1", "p_main_party"),
				(neg|is_between, ":var_1", "p_temp_party", "p_reserved_5"),
				(neq, ":var_1", "p_reserved_5"),
				(party_is_active, ":var_1"),
				(party_slot_eq, ":var_1", slot_party_type, 3),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_var_1_g_encountered_party", ":var_1", "$g_encountered_party"),
				(le, ":distance_to_party_from_party_var_1_g_encountered_party", 65),
				(party_stack_get_troop_id, ":party_stack_troop_id_var_1_0", ":var_1", 0),
				(is_between, ":party_stack_troop_id_var_1_0", "trp_ex_npc_020", "trp_ex_npc_054"),
				(neq, ":party_stack_troop_id_var_1_0", "trp_ex_npc_039"),
				(neq, ":party_stack_troop_id_var_1_0", "trp_ex_npc_040"),
				(neq, ":party_stack_troop_id_var_1_0", "trp_ex_npc_041"),
				(neq, ":party_stack_troop_id_var_1_0", "trp_ex_npc_042"),
				(neq, ":party_stack_troop_id_var_1_0", "trp_ex_npc_043"),
				(assign, "$temp_num_01", ":party_stack_troop_id_var_1_0"),
				(assign, "$temp_num_02", ":var_1"),
			(try_end),
			(gt, "$temp_num_01", 0),
			(gt, "$temp_num_02", 0),
			(str_store_troop_name, 8, "$temp_num_01")
		],
		"Wanted: Pirate {s8}",
		[
			(jump_to_menu, "mnu_wanted_named_pirate")
		], "."),

		("named_pirate_reward",
		[
			(eq, "$qquest_type", 31),
			(eq, "$qquest_report_party", "$g_encountered_party"),
			(eq, "$qquest_progress", 1)
		],
		"Reward: pirate hunting",
		[
			(assign, ":value", 7500),
			(party_get_num_prisoner_stacks, ":num_prisoner_stacks_main_party", "p_main_party"),
			(try_for_range, ":localvariable", 0, ":num_prisoner_stacks_main_party"),
				(party_prisoner_stack_get_troop_id, ":party_prisoner_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
				(try_begin),
					(eq, ":party_prisoner_stack_troop_id_main_party_localvariable", "$qquest_target_troop"),
					(party_remove_prisoners, "p_main_party", "$qquest_target_troop", 1),
					(assign, ":value", 15000),
				(try_end),
			(try_end),
			(party_remove_prisoners, "p_main_party", "$qquest_target_troop", 1),
			(call_script, "script_town_relation_diff", "$g_encountered_party", 10),
			(call_script, "script_wm_after_battle_progress", 1000),
			(call_script, "script_exp_reward_for_common_troop", 72),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
			(call_script, "script_qquest_initialize"),
			(play_sound, "snd_experience_gained"),
			(display_message, "str_named_pirate_harbor_master_g"),
			(display_message, "str_questcomp"),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("named_pirate_cancel",
		[
			(eq, "$qquest_type", 31),
			(eq, "$qquest_report_party", "$g_encountered_party"),
			(neq, "$qquest_progress", 1)
		],
		"Quest Cancel: pirate hunting",
		[
			(call_script, "script_town_relation_diff", "$g_encountered_party", -3),
			(call_script, "script_qquest_initialize"),
			(display_message, "str_named_pirate_harbor_master_b"),
			(play_sound, "snd_quest_failed"),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("port_quest",
		[
			(party_slot_ge, "$g_encountered_party", 40, 1),
			(try_begin),
				(party_slot_eq, "$g_encountered_party", 15, 40),
				(str_store_string, 17, "str_wm_qst_text_30"),
			(else_try),
				(party_slot_eq, "$g_encountered_party", 15, 41),
				(str_store_string, 17, "str_wm_qst_text_31"),
			(try_end)
		],
		"Quest: {s17}",
		[
			(assign, "$wm_quest_result", 0),
			(jump_to_menu, "mnu_wm_quest_menu")
		], "."),

		("hire_pirates",
		[
			(eq, "$r_player_class", 5),
			(call_script, "script_party_money_level_ge", "p_main_party", 300),
			(eq, "$wm_mo_continue", 1),
			(assign, ":var_1", 0),
			(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_main_party"),
				(party_stack_get_troop_id, ":party_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
				(gt, ":party_stack_troop_id_main_party_localvariable", "trp_army_size_troop"),
				(neg|troop_is_hero, ":party_stack_troop_id_main_party_localvariable"),
				(party_stack_get_size, ":party_stack_size_main_party_localvariable", "p_main_party", ":localvariable"),
				(val_add, ":var_1", ":party_stack_size_main_party_localvariable"),
			(try_end),
			(lt, ":var_1", 100),
			(party_get_slot, ":g_encountered_party_town_claimed_by_player", "$g_encountered_party", slot_town_claimed_by_player),
			(call_script, "script_pirate_troop_and_ship_type", ":g_encountered_party_town_claimed_by_player"),
			(str_store_troop_name, 8, "$temp_num_01")
		],
		"Hire: {s8}",
		[
			(party_get_slot, ":g_encountered_party_town_claimed_by_player", "$g_encountered_party", slot_town_claimed_by_player),
			(call_script, "script_pirate_troop_and_ship_type", ":g_encountered_party_town_claimed_by_player"),
			(party_add_members, "p_main_party", "$temp_num_01", 1),
			(call_script, "script_party_money_level_diff", "p_main_party", 300, 34)
		], "."),

		("vis_trading_port",
		[],
		"Visit Trading port",
		[
			(try_begin),
				(neg|party_slot_ge, "$g_encountered_party", 12, 0),
				(display_message, "str_place_repu_bad", 0x00ff9000),
			(else_try),
				(call_script, "script_wm_trade_price_export", "$g_encountered_party", 0),
				(call_script, "script_wm_trader_items_reset", "trp_town_1_merchant"),
				(start_presentation, "prsnt_wm_item_trade"),
			(try_end)
		], "."),

		("goto_shipyard",
		[],
		"Visit Shipyard",
		[
			(try_begin),
				(neg|party_slot_ge, "$g_encountered_party", 12, 0),
				(display_message, "str_place_repu_bad", 0x00ff9000),
			(else_try),
				(play_sound, "snd_wood_cuttt"),
				(start_presentation, "prsnt_wm_shipyard_pst"),
			(try_end)
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

		("wm_visit_tradeguild", 0, "The trade guild has provided you with information. For this job, you will need a bit of wealth.^1. Click [Trade Info]^2. Return to world map^3. Castle right-click menu^4. Click -Trade Info-",
"none",
	[
		(set_background_mesh, "mesh_pic_bank_back")
	],
	[
		("main_q_8_talk",
		[
			(eq, "$main_q_step", 8)
		],
			"Talk to the master about the slaves.",
		[
			(assign, "$main_q_step", 9),
			(display_message, "str_mq_1_8n")
		], "."),

		("main_q_9_talk",
		[
			(eq, "$main_q_step", 9)
		],
		"Talk to the master about your sister.",
		[
			(troop_get_slot, ":player_42", "trp_player", 42),
			(try_begin),
				(neq, ":player_42", "p_main_party"),
				(neg|is_between, ":player_42", "p_temp_party", "p_reserved_5"),
				(neq, ":player_42", "p_reserved_5"),
				(party_is_active, ":player_42"),
				(party_slot_eq, ":player_42", slot_party_type, 5),
				(assign, "$main_q_step", 10),
				(jump_to_menu, "mnu_main_quest_menu"),
			(else_try),
				(display_message, "str_mq_1_8n"),
			(try_end)
		], "."),

		("create_traders_par",
		[],
		"[Contract with the traders.]",
		[
			(jump_to_menu, "mnu_caravan_info")
		], "."),

		("tradeinfo",
		[
			(call_script, "script_party_money_level_ge", "p_main_party", 100),
			(eq, "$wm_mo_continue", 1)
		],
		"[Trade Info] (100d)",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 100, 34),
			(assign, "$trade_guild_info_on", 1),
			(display_message, "str_trade_guild_master_info", 0x00ff9000),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
		
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("wm_town_visit", 0, "     ",
"none",
	[
		(assign, "$last_visit_town", "$g_encountered_party"),
		#(call_script, "script_molda_music_box", 1, "$g_encountered_party"),
		(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
		(store_relation, ":relation_faction_of_party_g_encountered_party_wm_player_fac", ":faction_of_party_g_encountered_party", "$wm_player_fac"),
		(try_begin),
			(is_between, "$g_encountered_party", "p_pyongyang", "p_place_end"),
			(ge, ":relation_faction_of_party_g_encountered_party_wm_player_fac", 0),
			(set_show_messages, 0),
			(party_get_slot, ":main_party_center_siege_with_belfry", "p_main_party", slot_center_siege_with_belfry),
			(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
			(val_mul, ":party_size_wo_prisoners_main_party", 3),
			(val_div, ":party_size_wo_prisoners_main_party", 2),
			(set_show_messages, 1),
			(lt, ":main_party_center_siege_with_belfry", ":party_size_wo_prisoners_main_party"),
			(set_show_messages, 0),
			(store_sub, ":value", ":party_size_wo_prisoners_main_party", ":main_party_center_siege_with_belfry"),
			(store_div, ":value_2", ":value", 10),
			(party_get_slot, ":main_party_29", "p_main_party", 29),
			(val_div, ":main_party_29", 37),
			(set_show_messages, 1),
			(ge, ":main_party_29", ":value_2"),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value_2", 34),
			(call_script, "script_party_food_level_diff", "p_main_party", ":value", 87),
			(display_message, "str_food_compl", 0x0000ff00),
		(try_end),
		(try_begin),
			(eq, "$manage_troop_pst_restart", 1),
			(assign, "$manage_troop_pst_restart", 0),
			(start_presentation, "prsnt_manage_troops"),
		(else_try),
			(neg|is_between, "$wm_player_fac", "fac_kingdom_1", "fac_kingdoms_end"),
			(lt, ":relation_faction_of_party_g_encountered_party_wm_player_fac", 0),
			(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
			(gt, ":party_size_wo_prisoners_main_party", 200),
			(jump_to_menu, "mnu_wm_pst_map_return"),
			(display_message, "str_outlaw_cant_enter_city", 0x00ffff00),
		(else_try),
			(assign, "$clicked_tile_num", 0),
			(start_presentation, "prsnt_town_encounter"),
		(try_end)
	],
	[
		("visit_scene_menu",
		[],
		"-Take a walk around-",
		[
			(jump_to_menu, "mnu_visit_scene_menu")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("wm_pst_map_return", 0, "     ",
"none",
	[
		(change_screen_map)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("start_character_choose_culture", 0, ".....",
"none",
	[
		(assign, "$kingdom_pick_start_faction", "fac_kingdom_18"),
		(start_presentation, "prsnt_choose_kingdom_pst")
	],
	[
		("go_back",
		[],
		"Go back",
		[
			(jump_to_menu, "mnu_start_game_0")
		], ".")
	]
	),

	("start_character_5", 0, "What is your religion?",
"none",
	[
		(set_background_mesh, "mesh_pic_xex11")
	],
	[
		("r_follow_kingdom_rel",
		[],
		"Religion of the selected culture.",
		[
			(faction_get_slot, ":kingdom_pick_start_faction_27", "$kingdom_pick_start_faction", 27),
			(troop_set_slot, "trp_player", 23, ":kingdom_pick_start_faction_27"),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_no_god",
		[],
		"God is dead.",
		[
			(troop_set_slot, "trp_player", 23, 0),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_Catholic",
		[],
		"Catholic.",
		[
			(troop_set_slot, "trp_player", 23, 1),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_orthodox",
		[],
		"Orthodoxy",
		[
			(troop_set_slot, "trp_player", 23, 2),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_Islam",
		[],
		"Islam.",
		[
			(troop_set_slot, "trp_player", 23, 3),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_Buddhism",
		[],
		"Buddhism.",
		[
			(troop_set_slot, "trp_player", 23, 4),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_Confucianism",
		[],
		"Confucianism.",
		[
			(troop_set_slot, "trp_player", 23, 5),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_Zoroastrianism",
		[],
		"Zoroastrianism.",
		[
			(troop_set_slot, "trp_player", 23, 6),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_Hinduism",
		[],
		"Hinduism.",
		[
			(troop_set_slot, "trp_player", 23, 7),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_Tengri",
		[],
		"Tengrism.",
		[
			(troop_set_slot, "trp_player", 23, 8),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_Hellenism",
		[],
		"Hellenism.",
		[
			(troop_set_slot, "trp_player", 23, 9),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_Norse_mythology",
		[],
		"Norse mythology.",
		[
			(troop_set_slot, "trp_player", 23, 10),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_American_Shamanism",
		[],
		"American Shamanism.",
		[
			(troop_set_slot, "trp_player", 23, 11),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_Aztec_mythology",
		[],
		"Aztec mythology.",
		[
			(troop_set_slot, "trp_player", 23, 12),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_Inca_Sun_worship",
		[],
		"Inca Sun worship.",
		[
			(troop_set_slot, "trp_player", 23, 13),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_shinto",
		[],
		"Shintoism.",
		[
			(troop_set_slot, "trp_player", 23, 15),
			(jump_to_menu, "mnu_choose_skill")
		], "."),

		("r_African_Shamanism",
		[],
		"African Animism.",
		[
			(troop_set_slot, "trp_player", 23, 14),
			(jump_to_menu, "mnu_choose_skill")
		], ".")
	]
	),

	("mt_male_p_fuck_civil_trade", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_male_player_instant_fuck", 0, 2),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("mt_male_p_fuck_rape", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_male_player_instant_fuck", 1, 0),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("mt_male_p_fuck_normal", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_male_player_instant_fuck", 0, 0),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("mt_male_p_fuck_gay", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_male_player_gay_fuck", 0, 1),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("mt_female_p_fuck_civil_prosti", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_female_player_fucked_init", 0, 2),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("mt_female_p_fuck_prosti", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_female_player_fucked_init", 0, 1),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("mt_female_p_fuck_reln", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_female_player_fucked_init", 0, 0),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("mt_female_p_fuck_rape", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_female_player_fucked_init", 1, 0),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("mt_girl_player_1girl_2man_three_some_raped", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_girl_player_1girl_2man_three_some", 1, 0),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("mt_girl_player_1girl_2man_three_some", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_girl_player_1girl_2man_three_some", 0, 0),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("mt_girl_player_2girl_1man_three_some", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_girl_player_2girl_1man_three_some", 0, 0),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("mt_male_player_2girl_1man_threesome", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_male_player_2girl_1man_three_some", 0, 0),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("mt_male_player_1girl_2man_threesome", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_male_player_1girl_2man_three_some", 0, 0),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("mt_fuck_process_normal", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_fuck_pst_init", 0),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("mt_fuck_process_prosti", 0, "          ",
"none",
	[
		(try_begin),
			(eq, "$mt_action_on", 1),
			(call_script, "script_fuck_pst_init", 1),
			(assign, "$mt_action_on", 0),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("pst_lord_info", 0, "          ",
"none",
	[
		(str_clear, 21),
		(str_clear, 22),
		(str_clear, 23),
		(str_clear, 24),
		(str_clear, 25),
		(str_clear, 26),
		(str_clear, 27),
		(str_clear, 28),
		(str_clear, 29),
		(str_clear, 30),
		(str_clear, 31),
		(str_clear, 32),
		(str_clear, 33),
		(str_clear, 34),
		(str_clear, 35),
		(str_clear, 36),
		(str_clear, 37),
		(str_clear, 38),
		(str_clear, 39),
		(str_clear, 40),
		(str_clear, 41),
		(str_clear, 42),
		(str_clear, 43),
		(str_clear, 44),
		(str_clear, 45),
		(str_clear, 46),
		(str_clear, 47),
		(str_clear, 48),
		(str_clear, 49),
		(str_clear, 50),
		(start_presentation, "prsnt_pst_lord_info")
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("pst_faction_info", 0, "          ",
"none",
	[
		(str_clear, 20),
		(str_clear, 21),
		(str_clear, 22),
		(str_clear, 23),
		(str_clear, 24),
		(str_clear, 25),
		(str_clear, 26),
		(str_clear, 27),
		(str_clear, 28),
		(str_clear, 29),
		(str_clear, 30),
		(str_clear, 31),
		(str_clear, 32),
		(str_clear, 33),
		(str_clear, 34),
		(str_clear, 35),
		(str_clear, 36),
		(str_clear, 37),
		(str_clear, 38),
		(str_clear, 39),
		(str_clear, 40),
		(str_clear, 41),
		(str_clear, 42),
		(str_clear, 43),
		(str_clear, 44),
		(str_clear, 45),
		(str_clear, 46),
		(str_clear, 47),
		(str_clear, 48),
		(str_clear, 49),
		(str_clear, 50),
		(start_presentation, "prsnt_pst_faction_info")
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("pst_workshop", 0, "          ",
"none",
	[
		(start_presentation, "prsnt_pst_workshop")
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("pst_battle_tile", 0, "   ",
"none",
	[
		(try_begin),
			(this_or_next|eq, "$wm_duel_won", 1),
			(eq, "$wm_duel_won", 2),
			(try_begin),
				(eq, "$wm_duel_won", 1),
				(display_message, "str_duel_win_mess", 0x00ffff00),
				(val_sub, "$enemy_moral_level", 50),
				(val_clamp, "$enemy_moral_level", 30, 101),
			(else_try),
				(eq, "$wm_duel_won", 2),
				(display_message, "str_duel_lose_mess", 0x00ff0000),
				(val_sub, "$player_moral_level", 50),
				(val_clamp, "$player_moral_level", 30, 101),
			(try_end),
			(assign, "$wm_duel_won", 0),
			(assign, "$wm_battle_result_state", 0),
			(start_presentation, "prsnt_battle_tile_pst"),
		(else_try),
			(eq, "$battle_tile_menu_pop", 1),
			(assign, "$bt_player_entry_1", 1),
			(assign, "$bt_player_entry_2", 2),
			(assign, "$bt_player_entry_3", 3),
			(assign, "$bt_player_entry_4", 4),
			(assign, "$bt_player_entry_5", 5),
			(assign, "$bt_player_entry_6", 6),
			(assign, "$bt_player_entry_7", 7),
			(assign, "$bt_player_entry_8", 8),
			(assign, "$bt_player_entry_9", 9),
			(assign, "$bt_enemy_entry_1", 31),
			(assign, "$bt_enemy_entry_2", 32),
			(assign, "$bt_enemy_entry_3", 33),
			(assign, "$bt_enemy_entry_4", 34),
			(assign, "$bt_enemy_entry_5", 35),
			(assign, "$bt_enemy_entry_6", 36),
			(assign, "$bt_enemy_entry_7", 37),
			(assign, "$bt_enemy_entry_8", 38),
			(assign, "$bt_enemy_entry_9", 39),
			(assign, "$player_start_entry", 0),
			(assign, "$enemy_start_entry", 40),
			(assign, "$player_retreat_entry_begin", 112),
			(assign, "$player_retreat_entry_end", 116),
			(assign, "$enemy_retreat_entry_begin", 122),
			(assign, "$enemy_retreat_entry_end", 126),
			(assign, "$player_outer_entry_1", 111),
			(assign, "$player_outer_entry_2", 112),
			(assign, "$player_outer_entry_3", 113),
			(assign, "$player_outer_entry_4", 114),
			(assign, "$player_outer_entry_5", 115),
			(assign, "$player_outer_entry_6", 116),
			(assign, "$enemy_outer_entry_1", 121),
			(assign, "$enemy_outer_entry_2", 122),
			(assign, "$enemy_outer_entry_3", 123),
			(assign, "$enemy_outer_entry_4", 124),
			(assign, "$enemy_outer_entry_5", 125),
			(assign, "$enemy_outer_entry_6", 126),
			(assign, "$battle_tile_menu_pop", 0),
			(assign, "$battle_tactics_type", 0),
			(assign, "$battle_type_select_pre", 0),
			(assign, "$bt_terrain_strategy_state", 0),
			(assign, "$bt_terrain_strategy_dmg_start", 0),
			(assign, "$molda_battle_scn_prop_pos_dmg_timer", 0),
			(assign, "$succed_siege_strategy", 0),
			(assign, "$wm_battle_result_state", 0),
			(assign, "$town_gate_destroyed", 0),
			(assign, "$molda_siege_type", 0),
			(assign, "$surrender_yes_or_no", 0),
			(assign, "$withdawal_yes_or_no", 0),
			(assign, "$ai_suggest_duel_yes_or_no", 0),
			(assign, "$bt_cant_withdrawal", 0),
			(try_begin),
				(is_between, "$enemy_commander", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(troop_slot_eq, "$enemy_commander", 41, 3),
				(display_message, "str_revengeful_warning", 0x00ff9000),
			(try_end),
			(try_begin),
				(is_between, "$enemy_commander", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(store_attribute_level, ":attribute_level_enemy_commander_0", "$enemy_commander", 0),
				(store_random_in_range, ":random_in_range_0_100", 0, 100),
				(try_begin),
					(ge, ":attribute_level_enemy_commander_0", 225),
					(assign, ":value", 20),
				(else_try),
					(ge, ":attribute_level_enemy_commander_0", 175),
					(assign, ":value", 15),
				(else_try),
					(ge, ":attribute_level_enemy_commander_0", 125),
					(assign, ":value", 10),
				(else_try),
					(assign, ":value", 5),
				(try_end),
				(le, ":random_in_range_0_100", ":value"),
				(assign, "$ai_suggest_duel_yes_or_no", 1),
			(try_end),
			(try_begin),
				(eq, "$battle_tile_type", 51),
				(start_presentation, "prsnt_battle_tile_pst"),
			(else_try),
				(this_or_next|eq, "$battle_tile_type", 112),
				(this_or_next|eq, "$battle_tile_type", 111),
				(this_or_next|eq, "$battle_tile_type", 102),
				(this_or_next|eq, "$battle_tile_type", 103),
				(this_or_next|eq, "$battle_tile_type", 113),
				(this_or_next|eq, "$battle_tile_type", 104),
				(this_or_next|eq, "$battle_tile_type", 114),
				(this_or_next|eq, "$battle_tile_type", 105),
				(this_or_next|eq, "$battle_tile_type", 115),
				(eq, "$battle_tile_type", 101),
				(start_presentation, "prsnt_battle_tile_pst"),
			(else_try),
				(eq, "$battle_tile_type", 10),
				(try_begin),
					(eq, "$player_is_attack", 0),
					(assign, "$bt_player_entry_1", 11),
					(assign, "$bt_player_entry_2", 12),
					(assign, "$bt_player_entry_3", 13),
					(assign, "$bt_player_entry_4", 14),
					(assign, "$bt_player_entry_5", 15),
					(assign, "$bt_player_entry_6", 16),
					(assign, "$bt_player_entry_7", 17),
					(assign, "$bt_player_entry_8", 18),
					(assign, "$bt_player_entry_9", 19),
					(assign, "$bt_enemy_entry_1", 41),
					(assign, "$bt_enemy_entry_2", 42),
					(assign, "$bt_enemy_entry_3", 43),
					(assign, "$bt_enemy_entry_4", 44),
					(assign, "$bt_enemy_entry_5", 45),
					(assign, "$bt_enemy_entry_6", 46),
					(assign, "$bt_enemy_entry_7", 47),
					(assign, "$bt_enemy_entry_8", 48),
					(assign, "$bt_enemy_entry_9", 49),
					(assign, "$player_start_entry", 40),
					(assign, "$enemy_start_entry", 0),
				(else_try),
					(assign, "$bt_player_entry_1", 1),
					(assign, "$bt_player_entry_2", 2),
					(assign, "$bt_player_entry_3", 3),
					(assign, "$bt_player_entry_4", 4),
					(assign, "$bt_player_entry_5", 5),
					(assign, "$bt_player_entry_6", 6),
					(assign, "$bt_player_entry_7", 7),
					(assign, "$bt_player_entry_8", 8),
					(assign, "$bt_player_entry_9", 9),
					(assign, "$bt_enemy_entry_1", 31),
					(assign, "$bt_enemy_entry_2", 32),
					(assign, "$bt_enemy_entry_3", 33),
					(assign, "$bt_enemy_entry_4", 34),
					(assign, "$bt_enemy_entry_5", 35),
					(assign, "$bt_enemy_entry_6", 36),
					(assign, "$bt_enemy_entry_7", 37),
					(assign, "$bt_enemy_entry_8", 38),
					(assign, "$bt_enemy_entry_9", 39),
					(assign, "$player_start_entry", 0),
					(assign, "$enemy_start_entry", 40),
				(try_end),
				(start_presentation, "prsnt_battle_tile_pst"),
			(else_try),
				(this_or_next|eq, "$battle_tile_type", 9),
				(eq, "$battle_tile_type", 2),
				(start_presentation, "prsnt_battle_tile_pst"),
			(else_try),
				(this_or_next|eq, "$battle_tile_type", 5),
				(this_or_next|eq, "$battle_tile_type", 6),
				(this_or_next|eq, "$battle_tile_type", 4),
				(this_or_next|eq, "$battle_tile_type", 3),
				(this_or_next|eq, "$battle_tile_type", 7),
				(eq, "$battle_tile_type", 8),
				(store_random_in_range, ":random_in_range_0_2", 0, 2),
				(try_begin),
					(eq, ":random_in_range_0_2", 0),
					(assign, "$bt_player_entry_1", 1),
					(assign, "$bt_player_entry_2", 2),
					(assign, "$bt_player_entry_3", 3),
					(assign, "$bt_player_entry_4", 4),
					(assign, "$bt_player_entry_5", 5),
					(assign, "$bt_player_entry_6", 6),
					(assign, "$bt_player_entry_7", 7),
					(assign, "$bt_player_entry_8", 8),
					(assign, "$bt_player_entry_9", 9),
					(assign, "$bt_enemy_entry_1", 31),
					(assign, "$bt_enemy_entry_2", 32),
					(assign, "$bt_enemy_entry_3", 33),
					(assign, "$bt_enemy_entry_4", 34),
					(assign, "$bt_enemy_entry_5", 35),
					(assign, "$bt_enemy_entry_6", 36),
					(assign, "$bt_enemy_entry_7", 37),
					(assign, "$bt_enemy_entry_8", 38),
					(assign, "$bt_enemy_entry_9", 39),
					(assign, "$player_start_entry", 0),
					(assign, "$enemy_start_entry", 40),
					(assign, "$player_retreat_entry_begin", 1),
					(assign, "$player_retreat_entry_end", 9),
					(assign, "$enemy_retreat_entry_begin", 31),
					(assign, "$enemy_retreat_entry_end", 39),
					(assign, "$player_outer_entry_1", 1),
					(assign, "$player_outer_entry_2", 2),
					(assign, "$player_outer_entry_3", 3),
					(assign, "$player_outer_entry_4", 4),
					(assign, "$player_outer_entry_5", 5),
					(assign, "$player_outer_entry_6", 6),
					(assign, "$enemy_outer_entry_1", 31),
					(assign, "$enemy_outer_entry_2", 32),
					(assign, "$enemy_outer_entry_3", 33),
					(assign, "$enemy_outer_entry_4", 34),
					(assign, "$enemy_outer_entry_5", 35),
					(assign, "$enemy_outer_entry_6", 36),
				(else_try),
					(assign, "$bt_player_entry_1", 31),
					(assign, "$bt_player_entry_2", 32),
					(assign, "$bt_player_entry_3", 33),
					(assign, "$bt_player_entry_4", 34),
					(assign, "$bt_player_entry_5", 35),
					(assign, "$bt_player_entry_6", 36),
					(assign, "$bt_player_entry_7", 37),
					(assign, "$bt_player_entry_8", 38),
					(assign, "$bt_player_entry_9", 39),
					(assign, "$bt_enemy_entry_1", 1),
					(assign, "$bt_enemy_entry_2", 2),
					(assign, "$bt_enemy_entry_3", 3),
					(assign, "$bt_enemy_entry_4", 4),
					(assign, "$bt_enemy_entry_5", 5),
					(assign, "$bt_enemy_entry_6", 6),
					(assign, "$bt_enemy_entry_7", 7),
					(assign, "$bt_enemy_entry_8", 8),
					(assign, "$bt_enemy_entry_9", 9),
					(assign, "$player_start_entry", 40),
					(assign, "$enemy_start_entry", 0),
					(assign, "$player_retreat_entry_begin", 31),
					(assign, "$player_retreat_entry_end", 39),
					(assign, "$enemy_retreat_entry_begin", 1),
					(assign, "$enemy_retreat_entry_end", 9),
					(assign, "$player_outer_entry_1", 31),
					(assign, "$player_outer_entry_2", 32),
					(assign, "$player_outer_entry_3", 33),
					(assign, "$player_outer_entry_4", 34),
					(assign, "$player_outer_entry_5", 35),
					(assign, "$player_outer_entry_6", 36),
					(assign, "$enemy_outer_entry_1", 1),
					(assign, "$enemy_outer_entry_2", 2),
					(assign, "$enemy_outer_entry_3", 3),
					(assign, "$enemy_outer_entry_4", 4),
					(assign, "$enemy_outer_entry_5", 5),
					(assign, "$enemy_outer_entry_6", 6),
				(try_end),
				(start_presentation, "prsnt_battle_tile_pst"),
			(else_try),
				(eq, "$battle_tile_type", 0),
				(store_random_in_range, ":random_in_range_0_2", 0, 2),
				(try_begin),
					(eq, ":random_in_range_0_2", 0),
					(assign, "$bt_player_entry_1", 1),
					(assign, "$bt_player_entry_2", 2),
					(assign, "$bt_player_entry_3", 3),
					(assign, "$bt_player_entry_4", 4),
					(assign, "$bt_player_entry_5", 5),
					(assign, "$bt_player_entry_6", 6),
					(assign, "$bt_player_entry_7", 7),
					(assign, "$bt_player_entry_8", 8),
					(assign, "$bt_player_entry_9", 9),
					(assign, "$bt_enemy_entry_1", 31),
					(assign, "$bt_enemy_entry_2", 32),
					(assign, "$bt_enemy_entry_3", 33),
					(assign, "$bt_enemy_entry_4", 34),
					(assign, "$bt_enemy_entry_5", 35),
					(assign, "$bt_enemy_entry_6", 36),
					(assign, "$bt_enemy_entry_7", 37),
					(assign, "$bt_enemy_entry_8", 38),
					(assign, "$bt_enemy_entry_9", 39),
					(assign, "$player_start_entry", 0),
					(assign, "$enemy_start_entry", 40),
					(assign, "$player_retreat_entry_begin", 112),
					(assign, "$player_retreat_entry_end", 116),
					(assign, "$enemy_retreat_entry_begin", 122),
					(assign, "$enemy_retreat_entry_end", 126),
					(assign, "$player_outer_entry_1", 111),
					(assign, "$player_outer_entry_2", 112),
					(assign, "$player_outer_entry_3", 113),
					(assign, "$player_outer_entry_4", 114),
					(assign, "$player_outer_entry_5", 115),
					(assign, "$player_outer_entry_6", 116),
					(assign, "$enemy_outer_entry_1", 121),
					(assign, "$enemy_outer_entry_2", 122),
					(assign, "$enemy_outer_entry_3", 123),
					(assign, "$enemy_outer_entry_4", 124),
					(assign, "$enemy_outer_entry_5", 125),
					(assign, "$enemy_outer_entry_6", 126),
				(else_try),
					(assign, "$bt_player_entry_1", 31),
					(assign, "$bt_player_entry_2", 32),
					(assign, "$bt_player_entry_3", 33),
					(assign, "$bt_player_entry_4", 34),
					(assign, "$bt_player_entry_5", 35),
					(assign, "$bt_player_entry_6", 36),
					(assign, "$bt_player_entry_7", 37),
					(assign, "$bt_player_entry_8", 38),
					(assign, "$bt_player_entry_9", 39),
					(assign, "$bt_enemy_entry_1", 1),
					(assign, "$bt_enemy_entry_2", 2),
					(assign, "$bt_enemy_entry_3", 3),
					(assign, "$bt_enemy_entry_4", 4),
					(assign, "$bt_enemy_entry_5", 5),
					(assign, "$bt_enemy_entry_6", 6),
					(assign, "$bt_enemy_entry_7", 7),
					(assign, "$bt_enemy_entry_8", 8),
					(assign, "$bt_enemy_entry_9", 9),
					(assign, "$player_start_entry", 40),
					(assign, "$enemy_start_entry", 0),
					(assign, "$player_retreat_entry_begin", 122),
					(assign, "$player_retreat_entry_end", 126),
					(assign, "$enemy_retreat_entry_begin", 112),
					(assign, "$enemy_retreat_entry_end", 116),
					(assign, "$player_outer_entry_1", 126),
					(assign, "$player_outer_entry_2", 125),
					(assign, "$player_outer_entry_3", 124),
					(assign, "$player_outer_entry_4", 123),
					(assign, "$player_outer_entry_5", 122),
					(assign, "$player_outer_entry_6", 121),
					(assign, "$enemy_outer_entry_1", 116),
					(assign, "$enemy_outer_entry_2", 115),
					(assign, "$enemy_outer_entry_3", 114),
					(assign, "$enemy_outer_entry_4", 113),
					(assign, "$enemy_outer_entry_5", 112),
					(assign, "$enemy_outer_entry_6", 111),
				(try_end),
				(start_presentation, "prsnt_battle_tile_pst"),
			(try_end),
		(else_try),
			(change_screen_map),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(change_screen_map)
		], ".")
	]
	),

	("betray_fac_menu", 0, "Are you sure?",
"none",
	[],
	[
		("betray_fac",
		[],
		"Betray : Join the enemy faction.",
		[
			(store_faction_of_party, ":faction_of_party_wm_target_party", "$wm_target_party"),
			(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(try_begin),
					(eq, "$wm_player_fac", ":faction_of_troop_troop"),
					(troop_set_slot, ":troop", slot_troop_last_persuasion_time, 8),
					(troop_set_slot, ":troop", slot_troop_last_quest, 1080),
					(call_script, "script_change_player_relation_with_troop", ":troop", -99),
					(call_script, "script_change_player_relation_with_troop", ":troop", -99),
				(try_end),
			(try_end),
			(try_for_range, ":party", "p_pyongyang", "p_place_end"),
				(try_begin),
					(party_slot_eq, ":party", slot_town_tavern, "trp_player"),
					(faction_get_slot, ":wm_player_fac_19", "$wm_player_fac", 19),
					(party_set_slot, ":party", slot_town_horse_merchant, ":wm_player_fac_19"),
					(party_set_slot, ":party", slot_town_tavern, ":wm_player_fac_19"),
					(call_script, "script_party_extra_text_for_town", ":party"),
				(try_end),
			(try_end),
			(assign, "$wm_player_fac", ":faction_of_party_wm_target_party"),
			(troop_set_faction, "trp_player", "$wm_player_fac"),
			(try_for_range, ":unused", 0, 30),
				(try_begin),
					(troop_slot_ge, "trp_player", 13, -25),
					(call_script, "script_wm_honor_change_diff", "trp_player", 5, 34),
				(try_end),
			(try_end),
			(try_for_range, ":faction", "fac_kingdom_1", "fac_undeads"),
				(neq, ":faction", "fac_kingdoms_end"),
				(store_relation, ":relation_faction_wm_player_fac", ":faction", "$wm_player_fac"),
				(call_script, "script_set_player_relation_with_faction_no_mess", ":faction", ":relation_faction_wm_player_fac"),
			(try_end),
			(assign, "$need_meeting_for_ai", 0),
			(assign, "$need_meeting_loose", 0),
			(call_script, "script_initialize_main_party"),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("back",
		[],
		"[Back]",
		[
			(jump_to_menu, "mnu_wm_player_prisoner")
		], ".")
	]
	),

	("night_market", 0, "It is night market.",
"none",
	[],
	[
		("buy_nm_2",
		[
			(eq, "$g_encountered_party", "p_timbuktu"),
			(store_mul, ":value", 1000, 20),
			(call_script, "script_party_money_level_ge", "p_main_party", ":value"),
			(eq, "$wm_mo_continue", 1)
		],
		"Buy Holyknight sword (20000)",
		[
			(assign, ":var_1", 953),
			(troop_add_item, "trp_player", ":var_1", 0),
			(jump_to_menu, "mnu_night_market")
		], "."),

		("buy_cat",
		[
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 6),
			(party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 7),
			(call_script, "script_party_money_level_ge", "p_main_party", 10000),
			(eq, "$wm_mo_continue", 1),
			(neg|player_has_item, 1438)
		],
		"Buy Cat (10000)",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 10000, 34),
			(troop_add_item, "trp_player", 1438, 0),
			(jump_to_menu, "mnu_night_market")
		], "."),

		("buy_juice",
		[
			(call_script, "script_party_money_level_ge", "p_main_party", 1000),
			(eq, "$wm_mo_continue", 1)
		],
		"Buy Juice (1000)",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34),
			(troop_add_item, "trp_player", 1439, 0),
			(jump_to_menu, "mnu_night_market")
		], "."),

		("buy_sextant",
		[
			(this_or_next|eq, "$start_age", 1573),
			(eq, "$start_age", 0),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 1),
			(party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 2),
			(call_script, "script_party_money_level_ge", "p_main_party", 40000),
			(eq, "$wm_mo_continue", 1),
			(neg|player_has_item, 1440)
		],
		"Buy Sextant (40000)",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 40000, 34),
			(troop_add_item, "trp_player", 1440, 0),
			(jump_to_menu, "mnu_night_market")
		], "."),

		("buy_herb_1",
		[
			(eq, "$adult_content", 1),
			(call_script, "script_party_money_level_ge", "p_main_party", 5000),
			(eq, "$wm_mo_continue", 1)
		],
		"Buy big boob herb (5000)",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 5000, 34),
			(troop_add_item, "trp_player", 1432, 0),
			(jump_to_menu, "mnu_night_market")
		], "."),

		("buy_herb_2",
		[
			(eq, "$adult_content", 1),
			(call_script, "script_party_money_level_ge", "p_main_party", 5000),
			(eq, "$wm_mo_continue", 1)
		],
		"Buy small boob herb (5000)",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 5000, 34),
			(troop_add_item, "trp_player", 1431, 0),
			(jump_to_menu, "mnu_night_market")
		], "."),

		("buy_herb_3",
		[
			(eq, "$adult_content", 1),
			(call_script, "script_party_money_level_ge", "p_main_party", 5000),
			(eq, "$wm_mo_continue", 1)
		],
		"Buy king penis herb (5000)",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 5000, 34),
			(troop_add_item, "trp_player", 1434, 0),
			(jump_to_menu, "mnu_night_market")
		], "."),

		("buy_herb_4",
		[
			(eq, "$adult_content", 1),
			(call_script, "script_party_money_level_ge", "p_main_party", 5000),
			(eq, "$wm_mo_continue", 1)
		],
		"Buy pawn penis herb (5000)",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 5000, 34),
			(troop_add_item, "trp_player", 1433, 0),
			(jump_to_menu, "mnu_night_market")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_town_visit")
		], ".")
	]
	),

	("visit_scene_menu", 0, "   ",
"none",
	[],
	[
		("back",
		[],
		"[Back]",
		[
			(jump_to_menu, "mnu_wm_town_visit")
		], ".")
	]
	),

	("low_encounter", 0, "    ",
"none",
	[
		(assign, "$attempt_coup", 0),
		(assign, "$molda_siege_type", 0),
		(assign, "$player_has_ally", 0),
		(assign, "$enemy_has_ally", 0),
		(call_script, "script_encounter_party_faction_slot_init"),
		(call_script, "script_encounter_lord_slot_init"),
		(try_begin),
			(neg|encountered_party_is_attacker),
			(assign, "$player_is_attack", 1),
			(assign, "$wm_allow_retreat", 1),
		(else_try),
			(assign, "$player_is_attack", 0),
			(assign, "$wm_allow_retreat", 1),
		(try_end),
		(call_script, "script_party_count_fit_for_battle", "p_main_party"),
		(assign, "$player_army_size", reg0),
		(party_get_slot, "$player_train_level", "p_main_party", slot_town_elder),
		(party_get_slot, "$player_moral_level", "p_main_party", slot_center_player_relation),
		(call_script, "script_party_count_fit_for_battle", "$wm_target_party"),
		(assign, "$enemy_army_size", reg0),
		(party_get_slot, "$enemy_commander", "$wm_target_party", slot_town_horse_merchant),
		(party_get_slot, "$enemy_train_level", "$wm_target_party", slot_town_elder),
		(party_get_slot, "$enemy_moral_level", "$wm_target_party", slot_center_player_relation),
		(troop_get_slot, "$player_strategy_skill", "trp_player", slot_troop_spouse),
		(troop_get_slot, "$enemy_strategy_skill", "$enemy_commander", slot_troop_spouse),
		(troop_get_slot, "$player_tactics_skill", "trp_player", slot_troop_spawned_before),
		(troop_get_slot, "$enemy_tactics_skill", "$enemy_commander", slot_troop_spawned_before),
		(troop_get_slot, "$player_leadership_skill", "trp_player", slot_troop_last_comment_slot),
		(troop_get_slot, "$enemy_leadership_skill", "$enemy_commander", slot_troop_last_comment_slot),
		(troop_get_slot, "$player_naval_skill", "trp_player", slot_troop_father),
		(troop_get_slot, "$enemy_naval_skill", "$enemy_commander", slot_troop_father),
		(call_script, "script_battle_scale_sett"),
		(assign, "$enemy_spawn_num", "$enemy_army_size"),
		(call_script, "script_equip_supp_slot_export", "p_main_party"),
		(call_script, "script_equip_supp_slot_export", "$wm_target_party"),
		(store_faction_of_party, ":faction_of_party_wm_target_party", "$wm_target_party"),
		(faction_get_slot, "$enemy_has_horse", ":faction_of_party_wm_target_party", slot_faction_adjective),
		(faction_get_slot, "$enemy_has_finewood", ":faction_of_party_wm_target_party", 23),
		(faction_get_slot, "$enemy_has_iron", ":faction_of_party_wm_target_party", 24),
		(try_begin),
			(troop_slot_ge, "trp_player", 18, 11),
			(faction_get_slot, "$player_has_horse", "$wm_player_fac", slot_faction_adjective),
			(faction_get_slot, "$player_has_finewood", "$wm_player_fac", 23),
			(faction_get_slot, "$player_has_iron", "$wm_player_fac", 24),
		(else_try),
			(neg|troop_slot_ge, "trp_player", 18, 11),
			(is_between, "$contract_fac", "fac_kingdom_1", "fac_kingdoms_end"),
			(faction_get_slot, "$player_has_horse", "$contract_fac", slot_faction_adjective),
			(faction_get_slot, "$player_has_finewood", "$contract_fac", 23),
			(faction_get_slot, "$player_has_iron", "$contract_fac", 24),
		(else_try),
			(assign, "$player_has_horse", 0),
			(assign, "$player_has_finewood", 0),
			(assign, "$player_has_iron", 0),
		(try_end),
		(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
		(try_begin),
			(neq, ":current_terrain_main_party", 7),
			(neq, ":current_terrain_main_party", 2),
			(assign, "$low_encounter_battle", 1),
			(display_message, "str_cantfollow22", 0x00ffff00),
			(try_begin),
				(ge, "$random_succ_100_trand", 90),
				(assign, "$battle_tile_type", 8),
				(assign, "$battle_tile_menu_pop", 1),
				(jump_to_menu, "mnu_pst_battle_tile"),
			(else_try),
				(ge, "$random_succ_100_trand", 70),
				(assign, "$battle_tile_type", 7),
				(assign, "$battle_tile_menu_pop", 1),
				(jump_to_menu, "mnu_pst_battle_tile"),
			(else_try),
				(assign, "$battle_tile_type", 0),
				(assign, "$battle_tile_menu_pop", 1),
				(jump_to_menu, "mnu_pst_battle_tile"),
			(try_end),
		(else_try),
			(assign, "$low_encounter_battle", 1),
			(try_begin),
				(assign, "$battle_tile_type", 51),
				(assign, "$battle_tile_menu_pop", 1),
				(jump_to_menu, "mnu_pst_battle_tile"),
			(try_end),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(change_screen_map)
		], ".")
	]
	),

	("wm_tournament", 0, "{s11}",
"none",
	[
		(set_background_mesh, "mesh_pic_visit_train"),
		(assign, "$wm_duel_persnal", 0),
		(try_begin),
			(eq, "$g_enter_arena", 0),
			(try_begin),
				(eq, "$tournament_phase", 0),
				(play_sound, "snd_good_news_2"),
				(try_begin),
					(party_slot_ge, "$g_encountered_party", 8, 1),
					(party_get_slot, ":g_encountered_party_ai_substate", "$g_encountered_party", slot_party_ai_substate),
					(troop_add_item, "trp_player", ":g_encountered_party_ai_substate", 0),
					(str_store_item_name, 6, ":g_encountered_party_ai_substate"),
					(party_set_slot, "$g_encountered_party", slot_party_ai_substate, 0),
					(display_message, "str_celebratettttt", 0x00ffff00),
				(try_end),
				(try_begin),
					(gt, "$tournament_bet_money", 0),
					(val_mul, "$tournament_bet_money", 3),
				(try_end),
				(val_add, "$tournament_bet_money", 1000),
				(val_add, "$tournament_bet_money", 1000),
				(val_add, "$tournament_bet_money", 1000),
				(val_add, "$tournament_bet_money", 1000),
				(store_mul, ":value", 1000, 10),
				(add_xp_to_troop, ":value", "trp_player"),
				(call_script, "script_wm_honor_change_diff", "trp_player", 5, 87),
				(call_script, "script_adv_exp_diff", 300, 87),
				(call_script, "script_party_money_level_diff", "p_main_party", "$tournament_bet_money", 87),
				(assign, reg9, "$tournament_bet_money"),
				(str_store_party_name, 3, "$g_encountered_party"),
				(str_store_string, 11, "str_won_tournament"),
			(else_try),
				(eq, "$tournament_phase", -1),
				(str_store_string, 11, "str_lose_tournament"),
			(else_try),
				(eq, "$tournament_phase", 1),
				(str_store_string, 11, "str_pre_tournament"),
			(else_try),
				(this_or_next|eq, "$tournament_phase", 2),
				(eq, "$tournament_phase", 3),
				(eq, "$tournament_begging", 1),
				(str_store_string, 11, "str_tour_chance"),
			(else_try),
				(this_or_next|eq, "$tournament_phase", 2),
				(eq, "$tournament_phase", 3),
				(str_store_string, 11, "str_tour_vic"),
			(try_end),
		(else_try),
			(try_begin),
				(eq, "$tournament_phase", 0),
				(play_sound, "snd_good_news_2"),
				(str_store_string, 11, "str_won_arena"),
				(call_script, "script_party_money_level_diff", "p_main_party", 2500, 87),
			(else_try),
				(eq, "$tournament_phase", -1),
				(str_store_string, 11, "str_lose_arena"),
			(else_try),
				(eq, "$tournament_phase", 1),
				(str_store_string, 11, "str_pre_arena"),
			(else_try),
				(this_or_next|eq, "$tournament_phase", 2),
				(eq, "$tournament_phase", 3),
				(eq, "$tournament_begging", 1),
				(str_store_string, 11, "str_tour_chance"),
			(else_try),
				(this_or_next|eq, "$tournament_phase", 2),
				(eq, "$tournament_phase", 3),
				(str_store_string, 11, "str_tour_vic"),
			(try_end),
		(try_end)
	],
	[
		("free_fight",
		[
			(gt, "$tournament_phase", 0),
			(assign, reg7, "$tournament_phase")
		],
		"Participate in the fight (Round {reg7}/3)",
		[
			(assign, "$wm_duel_persnal", 0),
			(assign, "$wm_battle_result_state", 0),
			(assign, "$wm_duel_won", 0),
			(assign, "$wm_talk_state", 0),
			(assign, "$wm_quest_mission_anti_skip_menu", 0),
			(assign, "$molda_start_map_conversation", -1),
			(call_script, "script_molda_scene_culture", "$g_encountered_party"),
			(assign, ":var_1", "$town_scene_arena"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(assign, "$ply_tournament_kill_num", 0),
			(assign, "$tournament_begging", 0),
			(call_script, "script_wm_troop_type_depend_train", "$g_encountered_party", 100),
			(assign, ":value", "$temp_party_troop_05"),
			(assign, ":value_2", "$temp_party_troop_10"),
			(assign, ":value_3", "$temp_party_troop_07"),
			(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
			(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
				(eq, ":faction_of_troop_troop", ":faction_of_party_g_encountered_party"),
				(store_random_in_range, ":random_in_range_0_6", 0, 6),
				(try_begin),
					(eq, ":random_in_range_0_6", 0),
					(assign, ":value", ":troop"),
				(else_try),
					(eq, ":random_in_range_0_6", 1),
					(assign, ":value_2", ":troop"),
				(else_try),
					(eq, ":random_in_range_0_6", 2),
					(assign, ":value_3", ":troop"),
				(try_end),
			(try_end),
			(try_begin),
				(le, "$tournament_phase", 3),
				(set_visitor, 1, "trp_player"),
				(set_visitor, 11, ":value"),
				(set_visitor, 21, ":value_2"),
				(set_visitor, 31, ":value_3"),
			(try_end),
			(try_begin),
				(le, "$tournament_phase", 2),
				(set_visitor, 2, "$temp_party_troop_10"),
				(set_visitor, 3, "$temp_party_troop_09"),
				(set_visitor, 4, "$temp_party_troop_08"),
				(set_visitor, 5, "$temp_party_troop_07"),
				(set_visitor, 12, "$temp_party_troop_10"),
				(set_visitor, 13, "$temp_party_troop_09"),
				(set_visitor, 14, "$temp_party_troop_08"),
				(set_visitor, 15, "$temp_party_troop_07"),
				(set_visitor, 22, "$temp_party_troop_10"),
				(set_visitor, 23, "$temp_party_troop_09"),
				(set_visitor, 24, "$temp_party_troop_08"),
				(set_visitor, 25, "$temp_party_troop_07"),
				(set_visitor, 32, "$temp_party_troop_10"),
				(set_visitor, 33, "$temp_party_troop_09"),
				(set_visitor, 34, "$temp_party_troop_08"),
				(set_visitor, 35, "$temp_party_troop_07"),
			(try_end),
			(try_begin),
				(eq, "$tournament_phase", 1),
				(set_visitor, 6, "$temp_party_troop_06"),
				(set_visitor, 7, "$temp_party_troop_05"),
				(set_visitor, 8, "$temp_party_troop_04"),
				(set_visitor, 9, "$temp_party_troop_03"),
				(set_visitor, 10, "$temp_party_troop_02"),
				(set_visitor, 16, "$temp_party_troop_06"),
				(set_visitor, 17, "$temp_party_troop_05"),
				(set_visitor, 18, "$temp_party_troop_04"),
				(set_visitor, 19, "$temp_party_troop_03"),
				(set_visitor, 20, "$temp_party_troop_02"),
				(set_visitor, 26, "$temp_party_troop_06"),
				(set_visitor, 27, "$temp_party_troop_05"),
				(set_visitor, 28, "$temp_party_troop_04"),
				(set_visitor, 29, "$temp_party_troop_03"),
				(set_visitor, 30, "$temp_party_troop_02"),
				(set_visitor, 36, "$temp_party_troop_06"),
				(set_visitor, 37, "$temp_party_troop_05"),
				(set_visitor, 38, "$temp_party_troop_04"),
				(set_visitor, 39, "$temp_party_troop_03"),
				(set_visitor, 40, "$temp_party_troop_02"),
			(try_end),
			(set_jump_mission, "mt_arena_mission"),
			(assign, "$current_mission_template", "mt_arena_mission"),
			(try_begin),
				(eq, "$tournament_type", 1),
			(else_try),
				(eq, "$tournament_type", 2),
				(try_for_range, ":number", 1, 41),
					(mission_tpl_entry_add_override_item, "mt_arena_mission", ":number", 153),
				(try_end),
			(try_end),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("bettt_1",
		[
			(eq, "$g_enter_arena", 0),
			(gt, "$tournament_phase", 0),
			(eq, "$tournament_bet_money", 0),
			(store_mul, ":value", 1000, 3),
			(call_script, "script_party_money_level_ge", "p_main_party", ":value"),
			(eq, "$wm_mo_continue", 1)
		],
		"[Bet: 3000]",
		[
			(store_mul, ":value", 1000, 3),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 34),
			(val_add, "$tournament_bet_money", ":value"),
			(jump_to_menu, "mnu_wm_tournament")
		], "."),

		("bettt_2",
		[
			(eq, "$g_enter_arena", 0),
			(gt, "$tournament_phase", 0),
			(eq, "$tournament_bet_money", 0),
			(store_mul, ":value", 1000, 2),
			(call_script, "script_party_money_level_ge", "p_main_party", ":value"),
			(eq, "$wm_mo_continue", 1)
		],
		"[Bet: 2000]",
		[
			(store_mul, ":value", 1000, 2),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 34),
			(val_add, "$tournament_bet_money", ":value"),
			(jump_to_menu, "mnu_wm_tournament")
		], "."),

		("bettt_3",
		[
			(eq, "$g_enter_arena", 0),
			(gt, "$tournament_phase", 0),
			(eq, "$tournament_bet_money", 0),
			(store_mul, ":value", 1000, 1),
			(call_script, "script_party_money_level_ge", "p_main_party", ":value"),
			(eq, "$wm_mo_continue", 1),
		],
		"[Bet: 1000]",
		[
			(store_mul, ":value", 1000, 1),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 34),
			(val_add, "$tournament_bet_money", ":value"),
			(jump_to_menu, "mnu_wm_tournament"),
		], "."),

		("back",
		[],
		"[Back]",
		[
			(jump_to_menu, "mnu_wm_town_visit"),
		], "."),
	]
	),

	("wm_troop_clear", 0, "[Size initialize]: All troops in the army will be dismissed; with the exception of companions and elites soldiers.",
"none",
	[],
	[
		("troop_clear",
		[],
		"[Dismiss entire main army]",
		[
			(call_script, "script_wm_simp_tr_init"),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("troop_clear2",
		[
			(is_between, "$ply_staying_party_no", "p_pyongyang", "p_place_end")
		],
		"[Initialize stationed army]",
		[
			(assign, "$ply_staying_party_no", 0),
			(assign, "$ply_staying_army_size", 0),
			(assign, "$ply_staying_army_recruit_on", 0),
			(display_message, "str_t_armystay_disband", 0x00ff0000),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("back",
		[],
		"[Back]",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),

	("wm_wastland", 0, "The land here is barren. Building a new village will require 50 000 people and 25 000 denars.^^Current Population {reg7}/50000",
"none",
	[
		(store_random_in_range, ":random_in_range_0_2", 0, 2),
		(party_get_current_terrain, ":current_terrain_main_party", "p_main_party"),
		(try_begin),
			(this_or_next|eq, ":current_terrain_main_party", 7),
			(eq, ":current_terrain_main_party", 2),
			(set_background_mesh, "mesh_st_pic_sea"),
		(else_try),
			(eq, ":current_terrain_main_party", 5),
			(set_background_mesh, "mesh_st_pic_desert"),
		(else_try),
			(eq, ":current_terrain_main_party", 4),
			(set_background_mesh, "mesh_st_pic_snow"),
		(else_try),
			(eq, ":random_in_range_0_2", 0),
			(set_background_mesh, "mesh_st_pic_mount"),
		(else_try),
			(set_background_mesh, "mesh_st_pic_plain"),
		(try_end),
		(party_get_slot, reg7, "$g_encountered_party", slot_town_prosperity)
	],
	[
		("pioneer_count",
		[
			(neq, "$start_age", 1184),
			(troop_slot_ge, "trp_player", 18, 11),
			(store_mul, ":value", 1000, 50),
			(neg|party_slot_ge, "$g_encountered_party", 50, ":value"),
			(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
			(gt, ":party_size_wo_prisoners_main_party", 1000)
		],
		"Populate the settlements.",
		[
			(call_script, "script_add_spawn_count"),
			(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
			(val_sub, ":party_size_wo_prisoners_main_party", "$ply_full_spawn"),
			(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
			(assign, ":var_3", 0),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_main_party"),
				(party_stack_get_troop_id, ":party_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
				(gt, ":party_stack_troop_id_main_party_localvariable", "trp_army_size_troop"),
				(neg|troop_is_hero, ":party_stack_troop_id_main_party_localvariable"),
				(party_stack_get_size, ":party_stack_size_main_party_localvariable", "p_main_party", ":localvariable"),
				(try_begin),
					(gt, ":party_stack_size_main_party_localvariable", 0),
					(val_add, ":var_3", ":party_stack_size_main_party_localvariable"),
				(try_end),
			(try_end),
			(val_sub, ":party_size_wo_prisoners_main_party", ":var_3"),
			(try_begin),
				(gt, ":party_size_wo_prisoners_main_party", 0),
				(party_get_slot, ":g_encountered_party_town_prosperity", "$g_encountered_party", slot_town_prosperity),
				(val_add, ":g_encountered_party_town_prosperity", ":party_size_wo_prisoners_main_party"),
				(party_set_slot, "$g_encountered_party", slot_town_prosperity, ":g_encountered_party_town_prosperity"),
				(call_script, "script_party_army_size_execute", "p_main_party", "$ply_full_spawn", 5),
			(try_end),
			(jump_to_menu, "mnu_wm_wastland")
		], "."),

		("settlement_complete",
		[
			(troop_slot_ge, "trp_player", 18, 11),
			(store_mul, ":value", 1000, 50),
			(party_slot_ge, "$g_encountered_party", 50, ":value"),
			(store_mul, ":value_2", 1000, 25),
			(call_script, "script_party_money_level_ge", "p_main_party", ":value_2"),
			(eq, "$wm_mo_continue", 1)
		],
		"[Finalize the settlement]",
		[
			(play_sound, "snd_good_news_2"),
			(store_mul, ":value", 1000, 25),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 34),
			(try_begin),
				(eq, "$g_encountered_party", "p_wasteland1"),
				(assign, ":value_2", "p_santo_domingo"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_la_romana"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland2"),
				(assign, ":value_2", "p_south_hedland"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_karratha"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland3"),
				(assign, ":value_2", "p_darwin"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_kakadu"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland4"),
				(assign, ":value_2", "p_nashville"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_huntsville"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland5"),
				(assign, ":value_2", "p_wilmington"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_fayetteville"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland6"),
				(assign, ":value_2", "p_saint_augustine"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_lakeland"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland7"),
				(assign, ":value_2", "p_oklahoma"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_tulsa"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland8"),
				(assign, ":value_2", "p_kansas"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_omaha"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland9"),
				(assign, ":value_2", "p_hauston"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_san_antonio"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland10"),
				(assign, ":value_2", "p_santa_clara"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_bayamo"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland11"),
				(assign, ":value_2", "p_new_orleans"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_mobile"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland12"),
				(assign, ":value_2", "p_rio_de_janeiro"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_santos"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland13"),
				(assign, ":value_2", "p_salvador"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_porto_seguro"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland14"),
				(assign, ":value_2", "p_reykjabik"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_arborg"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland15"),
				(assign, ":value_2", "p_vinland"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_vinland_village"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(else_try),
				(eq, "$g_encountered_party", "p_wasteland16"),
				(assign, ":value_2", "p_brattalid"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
				(assign, ":value_2", "p_brattalid_village"),
				(party_set_flags, ":value_2", 256, 0),
				(call_script, "script_defeat_town_capture_execute", ":value_2", "$wm_player_fac"),
				(party_set_slot, ":value_2", slot_town_tavern, "trp_player"),
			(try_end),
			(call_script, "script_troop_contribution_diff", "trp_player", 100, 87),
			(party_set_flags, "$g_encountered_party", 256, 1),
			(jump_to_menu, "mnu_wm_pst_map_return"),
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("wm_workshop", 0, "-{s3}-^^(Number of Slaves: {reg11}) (Work Level: {reg14}%) = Productivity: {reg12} per day^^Products: [{s11}]   {reg17}/{reg15}   Stock Number: {reg16}",
"none",
	[
		(set_background_mesh, "mesh_pic_recruits"),
		(str_store_party_name, 3, "$g_encountered_party"),
		(assign, reg11, "$workshop_slave"),
		(store_mul, reg12, reg11, "$workshop_work_level"),
		(val_div, reg12, 100),
		(str_store_item_name, 11, "$workshop_target_product"),
		(assign, reg13, "$workshop_target_price"),
		(assign, reg14, "$workshop_work_level"),
		(assign, reg15, "$workshop_target_price"),
		(assign, reg17, "$workshop_product_cur"),
		(assign, reg16, "$workshop_product_stock")
	],
	[
		("give_product",
		[
			(gt, "$workshop_product_stock", 0)
		],
		"Pick an item from stock",
		[
			(set_show_messages, 0),
			(assign, ":var_1", 0),
			(troop_get_inventory_capacity, ":inventory_capacity_player", "trp_player"),
			(try_for_range, ":localvariable", 0, ":inventory_capacity_player"),
				(troop_get_inventory_slot, ":inventory_slot_player_localvariable", "trp_player", ":localvariable"),
				(is_between, ":inventory_slot_player_localvariable", 92, 117),
				(troop_inventory_slot_get_item_amount, ":troop_inventory_slot_item_amount_player_localvariable", "trp_player", ":localvariable"),
				(val_add, ":troop_inventory_slot_item_amount_player_localvariable", 1),
				(val_add, ":var_1", ":troop_inventory_slot_item_amount_player_localvariable"),
			(try_end),
			(set_show_messages, 1),
			(try_begin),
				(ge, ":var_1", 20),
				(assign, reg8, ":var_1"),
				(display_message, "str_ginventoryfull"),
			(else_try),
				(store_free_inventory_capacity, ":free_inventory_capacity_player", "trp_player"),
				(le, ":free_inventory_capacity_player", 0),
				(display_message, "str_inventoryfull"),
			(else_try),
				(val_sub, "$workshop_product_stock", 1),
				(troop_add_item, "trp_player", "$workshop_target_product"),
			(try_end),
			(jump_to_menu, "mnu_wm_workshop")
		], "."),

		("work_level",
		[],
		"[Adjust work level]",
		[
			(store_mul, ":value", 25, 5),
			(try_begin),
				(eq, "$workshop_work_level", ":value"),
				(assign, "$workshop_work_level", 75),
			(else_try),
				(eq, "$workshop_work_level", 100),
				(assign, "$workshop_work_level", ":value"),
			(else_try),
				(eq, "$workshop_work_level", 75),
				(assign, "$workshop_work_level", 100),
			(try_end),
			(display_message, "str_worklevc"),
			(jump_to_menu, "mnu_wm_workshop")
		], "."),

		("demolish_ws",
		[],
		"-Demolish-",
		[
			(jump_to_menu, "mnu_demolish_ws")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("demolish_ws", 0, "Are you sure?",
"none",
	[],
	[
		("demolish_ws_y",
		[],
		"-Demolish-",
		[
			(str_store_party_name, 7, "p_workshop_party"),
			(assign, "$workshop_target_party", 0),
			(assign, "$workshop_slave", 0),
			(party_set_flags, "p_workshop_party", 256, 1),
			(display_message, "str_demolish_wsm"),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("wm_game_over", 0, "Your head is falling towards the ground. You can't see the darkness. You can't even think about it.^(System: The enemy commander is one of your foes. If you are defeated in battle and fail to escape, you will die.)",
"none",
	[
		(play_track, "track_calm_night_2", 2),
		(set_background_mesh, "mesh_pic_gameover")
	],
	[
		("game_overr",
		[],
		"-End-",
		[
			(display_message, "str_game_overr", 0x00ff9000)
		], ".")
	]
	),

	("caravan_info", 0, "Current Target A: [{s7}]^Current Target B: [{s8}]^^Traders A: [{s9}] and [{s10}]^Traders B: [{s11}] and [{s12}](Merchant only)",
"none",
	[
		(set_background_mesh, "mesh_pic_bank_back"),
		(str_clear, 7),
		(str_clear, 8),
		(str_clear, 9),
		(str_clear, 10),
		(str_clear, 11),
		(str_clear, 12),
		(try_begin),
			(is_between, "$rt_target_set_a", "p_pyongyang", "p_place_end"),
			(str_store_party_name, 7, "$rt_target_set_a"),
		(try_end),
		(try_begin),
			(is_between, "$rt_target_set_b", "p_pyongyang", "p_place_end"),
			(str_store_party_name, 8, "$rt_target_set_b"),
		(try_end),
		(troop_get_slot, ":player_42", "trp_player", 42),
		(try_begin),
			(neq, ":player_42", "p_main_party"),
			(neg|is_between, ":player_42", "p_temp_party", "p_reserved_5"),
			(neq, ":player_42", "p_reserved_5"),
			(party_is_active, ":player_42"),
			(party_get_slot, ":player_42_town_tavern", ":player_42", slot_town_tavern),
			(party_get_slot, ":player_42_town_store", ":player_42", slot_town_store),
			(str_store_party_name, 9, ":player_42_town_tavern"),
			(str_store_party_name, 10, ":player_42_town_store"),
		(try_end),
		(troop_get_slot, ":player_42", "trp_player", 43),
		(try_begin),
			(neq, ":player_42", "p_main_party"),
			(neg|is_between, ":player_42", "p_temp_party", "p_reserved_5"),
			(neq, ":player_42", "p_reserved_5"),
			(party_is_active, ":player_42"),
			(party_get_slot, ":player_42_town_tavern", ":player_42", slot_town_tavern),
			(party_get_slot, ":player_42_town_store", ":player_42", slot_town_store),
			(str_store_party_name, 11, ":player_42_town_tavern"),
			(str_store_party_name, 12, ":player_42_town_store"),
		(try_end)
	],
	[
		("create_traders_a",
		[
			(is_between, "$rt_target_set_a", "p_pyongyang", "p_place_end"),
			(is_between, "$rt_target_set_b", "p_pyongyang", "p_place_end"),
			(neq, "$rt_target_set_a", "$rt_target_set_b"),
			(store_mul, ":value", 500, 10),
			(call_script, "script_party_money_level_ge", "p_main_party", ":value"),
			(eq, "$wm_mo_continue", 1),
			(neq, "$trade_contract_a", 1)
		],
		"[Traders Group A] (5000d)",
		[
			(assign, "$trade_contract_a", 1),
			(call_script, "script_create_player_traders_party", "$rt_target_set_a", "$rt_target_set_b", 42),
			(store_mul, ":value", 500, 10),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 34),
			(display_message, "str_caravan_created", 0x00ff9000),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("create_traders_a_p",
		[
			(eq, "$trade_contract_a", 1)
		],
		"[Disband: Traders Group A]",
		[
			(assign, "$trade_contract_a", 0),
			(call_script, "script_player_traders_disband", 42),
			(display_message, "str_contract_endd", 0x00ff9000),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("create_traders_b",
		[
			(eq, "$r_player_class", 1),
			(is_between, "$rt_target_set_a", "p_pyongyang", "p_place_end"),
			(is_between, "$rt_target_set_b", "p_pyongyang", "p_place_end"),
			(neq, "$rt_target_set_a", "$rt_target_set_b"),
			(store_mul, ":value", 500, 10),
			(call_script, "script_party_money_level_ge", "p_main_party", ":value"),
			(eq, "$wm_mo_continue", 1),
			(neq, "$trade_contract_b", 1)
		],
		"[Traders Group B] (5000d)",
		[
			(assign, "$trade_contract_b", 1),
			(call_script, "script_create_player_traders_party", "$rt_target_set_a", "$rt_target_set_b", 43),
			(store_mul, ":value", 500, 10),
			(call_script, "script_party_money_level_diff", "p_main_party", ":value", 34),
			(display_message, "str_caravan_created", 0x00ff9000),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("create_traders_b_p",
		[
			(eq, "$trade_contract_b", 1)
		],
		"[Disband: Traders Group B]",
		[
			(assign, "$trade_contract_b", 0),
			(call_script, "script_player_traders_disband", 43),
			(display_message, "str_contract_endd", 0x00ff9000),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("demolish_hideout", 0, "Are you sure?",
"none",
	[],
	[
		("demolish_hideout",
		[],
		">Demolish the Secret mansion<",
		[
			(str_store_party_name, 7, "p_ply_hideout"),
			(display_message, "str_demolish_wsm"),
			(assign, "$hidout_target_party", 0),
			(assign, "$hideout_build_prison", 0),
			(assign, "$hideout_build_torture", 0),
			(party_set_flags, "p_ply_hideout", 256, 1),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("wm_ply_hideout", 0, "This is your hidden mansion.",
"none",
	[
		(set_background_mesh, "mesh_pic_xex14"),
		(assign, "$need_quit_mission", 0),
		(try_begin),
			(eq, "$restart_cur_mission", 1),
			(call_script, "script_mt_torture_room"),
			(assign, "$restart_cur_mission", 0),
		(try_end)
	],
	[
		("hideout_bed",
		[],
		"Bed room",
		[
			(play_track, "track_calm_night_2", 2),
			(assign, "$wm_talk_state", 5),
			(set_jump_mission, "mt_hideout_mission"),
			(assign, "$current_mission_template", "mt_hideout_mission"),
			(assign, ":var_1", "scn_hideout_bed"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(try_begin),
				(troop_get_slot, ":player_state", "trp_player", slot_troop_state),
				(this_or_next|is_between, ":player_state", "trp_tt_lord_01_00", "trp_tt_lord_end"),
				(is_between, ":player_state", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(troop_slot_eq, "trp_player", slot_troop_state, ":player_state"),
				(troop_slot_eq, ":player_state", slot_troop_state, "trp_player"),
				(set_visitor, 1, ":player_state"),
			(try_end),
			(set_jump_entry, 0),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("hideout_guest",
		[],
		"Guest room",
		[
			#(call_script, "script_molda_music_box", 7, 0),
			(assign, "$wm_talk_state", 21),
			(set_jump_mission, "mt_hideout_mission"),
			(assign, "$current_mission_template", "mt_hideout_mission"),
			(assign, ":var_1", "scn_hideout_comp"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(troop_get_slot, ":player_state", "trp_player", slot_troop_state),
			(assign, "$temp_num_01", 0),
			(assign, "$temp_num_02", 0),
			(store_random_in_range, ":random_in_range_0_100", 0, 100),
			(try_begin),
				(eq, ":random_in_range_0_100", 0),
				(call_script, "script_temp_save_number11_initialize"),
				(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
					(neq, ":troop", ":player_state"),
					(call_script, "script_wm_main_party_has_troop_sc", ":troop"),
					(eq, "$wm_comp_continue", 1),
					(call_script, "script_temp_save_number11_inject", ":troop"),
				(try_end),
				(call_script, "script_temp_save_number11_choice_rand"),
				(is_between, "$wm_target_number11", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(assign, "$temp_num_01", "$wm_target_number11"),
				(call_script, "script_temp_save_number11_initialize"),
				(try_for_range, ":troop", "trp_npc1", "trp_kingdom_1_lord"),
					(call_script, "script_wm_main_party_has_troop_sc", ":troop"),
					(eq, "$wm_comp_continue", 1),
					(call_script, "script_temp_save_number11_inject", ":troop"),
				(try_end),
				(call_script, "script_temp_save_number11_choice_rand"),
				(is_between, "$wm_target_number11", "trp_npc1", "trp_kingdom_1_lord"),
				(assign, "$temp_num_02", "$wm_target_number11"),
				(set_visitor, 8, "$temp_num_01"),
				(set_visitor, 9, "$temp_num_02"),
			(try_end),
			(assign, ":value", "$wm_comp_id_1"),
			(try_begin),
				(gt, ":value", 0),
				(neq, ":value", ":player_state"),
				(neq, ":value", "$temp_num_01"),
				(neq, ":value", "$temp_num_02"),
				(set_visitor, 1, ":value"),
			(try_end),
			(assign, ":value", "$wm_comp_id_2"),
			(try_begin),
				(gt, ":value", 0),
				(neq, ":value", ":player_state"),
				(neq, ":value", "$temp_num_01"),
				(neq, ":value", "$temp_num_02"),
				(set_visitor, 2, ":value"),
			(try_end),
			(assign, ":value", "$wm_comp_id_3"),
			(try_begin),
				(gt, ":value", 0),
				(neq, ":value", ":player_state"),
				(neq, ":value", "$temp_num_01"),
				(neq, ":value", "$temp_num_02"),
				(set_visitor, 3, ":value"),
			(try_end),
			(assign, ":value", "$wm_comp_id_4"),
			(try_begin),
				(gt, ":value", 0),
				(neq, ":value", ":player_state"),
				(neq, ":value", "$temp_num_01"),
				(neq, ":value", "$temp_num_02"),
				(set_visitor, 4, ":value"),
			(try_end),
			(assign, ":value", "$wm_comp_id_5"),
			(try_begin),
				(gt, ":value", 0),
				(neq, ":value", ":player_state"),
				(neq, ":value", "$temp_num_01"),
				(neq, ":value", "$temp_num_02"),
				(set_visitor, 5, ":value"),
			(try_end),
			(assign, ":value", "$wm_comp_id_standby"),
			(try_begin),
				(gt, ":value", 0),
				(neq, ":value", ":player_state"),
				(neq, ":value", "$temp_num_01"),
				(neq, ":value", "$temp_num_02"),
				(set_visitor, 6, ":value"),
			(try_end),
			(try_begin),
				(is_between, "$wm_slave_dancer", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(troop_slot_eq, "$wm_slave_dancer", slot_troop_leaded_party, 3),
				(set_visitor, 7, "$wm_slave_dancer"),
			(else_try),
				(set_visitor, 7, "trp_hideout_dancer"),
			(try_end),
			(set_visitor, 10, "trp_hideout_chef"),
			(try_begin),
				(is_between, "$wm_player_fac", "fac_kingdom_1", "fac_kingdoms_end"),
				(assign, ":var_6", 11),
				(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
					(neq, ":troop", ":player_state"),
					(le, ":var_6", 13),
					(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
					(eq, ":faction_of_troop_troop", "$wm_player_fac"),
					(troop_slot_eq, ":troop", slot_troop_cur_center, 0),
					(troop_get_slot, ":troop_occupation", ":troop", slot_troop_occupation),
					(gt, ":troop_occupation", 30),
					(store_random_in_range, ":random_in_range_0_100", 0, 3),
					(eq, ":random_in_range_0_100", 0),
					(set_visitor, ":var_6", ":troop"),
					(val_add, ":var_6", 1),
				(try_end),
			(try_end),
			(set_jump_entry, 0),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("hideout_slave_b",
		[
			(eq, "$adult_content", 1),
			(eq, "$hideout_build_prison", 0),
			(store_mul, ":value", 1000, 5),
			(call_script, "script_party_money_level_ge", "p_main_party", ":value"),
			(eq, "$wm_mo_continue", 1)
		],
		"-Build Prison (5000)-",
		[
			(assign, "$hideout_build_prison", 1),
			(jump_to_menu, "mnu_wm_ply_hideout")
		], "."),

		("hideout_slave",
		[
			(eq, "$adult_content", 1),
			(eq, "$hideout_build_prison", 1)
		],
		"Prison",
		[
			(play_track, "track_tavern_2", 2),
			(assign, "$wm_talk_state", 9),
			(set_jump_mission, "mt_hideout_mission"),
			(assign, "$current_mission_template", "mt_hideout_mission"),
			(assign, ":var_1", "scn_hideout_slave"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 41, "trp_hideout_warder"),
			(assign, ":var_2", 1),
			(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(le, ":var_2", 40),
				(troop_slot_eq, ":troop", slot_troop_leaded_party, 3),
				(call_script, "script_wm_main_party_has_troop_sc", ":troop"),
				(neq, "$wm_comp_continue", 1),
				(neq, "$wm_slave_dancer", ":troop"),
				(neq, "$torture_troop_1", ":troop"),
				(neq, "$torture_troop_2", ":troop"),
				(neq, "$torture_troop_3", ":troop"),
				(set_visitor, ":var_2", ":troop"),
				(val_add, ":var_2", 1),
			(try_end),
			(set_jump_entry, 0),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("hideout_torture_b",
		[
			(eq, "$adult_content", 1),
			(eq, "$hideout_build_torture", 0),
			(store_mul, ":value", 1000, 5),
			(call_script, "script_party_money_level_ge", "p_main_party", ":value"),
			(eq, "$wm_mo_continue", 1)
		],
		"-Build Torture room (5000)-",
		[
			(assign, "$hideout_build_torture", 1),
			(jump_to_menu, "mnu_wm_ply_hideout")
		], "."),

		("hideout_torture",
		[
			(eq, "$adult_content", 1),
			(eq, "$hideout_build_torture", 1)
		],
		"Torture room",
		[
			(play_track, "track_tavern_2", 2),
			(call_script, "script_mt_torture_room")
		], "."),

		("demolish_hideout",
		[],
		">Demolish the Secret mansion<",
		[
			(jump_to_menu, "mnu_demolish_hideout")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("demolish_brothel", 0, "Are you sure?",
"none",
	[],
	[
		("demolish_br_y",
		[],
		"-Demolish-",
		[
			(str_store_party_name, 7, "p_brothel_party"),
			(assign, "$brothel_target_party", 0),
			(assign, "$brothel_prev_income", 0),
			(party_set_flags, "p_brothel_party", 256, 1),
			(display_message, "str_demolish_wsm"),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("wm_brothel", 0, "Income previous month: {reg11}^Member List:^ {s11}^ {s12}^ {s13}^ {s14}^ {s15}^ {s16}^ {s17}",
"none",
	[
		(play_track, "track_calm_night_2", 2),
		(set_background_mesh, "mesh_pic_xex14"),
		(assign, "$need_quit_mission", 0),
		(str_clear, 11),
		(str_clear, 12),
		(str_clear, 13),
		(str_clear, 14),
		(str_clear, 15),
		(str_clear, 16),
		(str_clear, 17),
		(assign, reg11, "$brothel_prev_income"),
		(assign, ":value", "$brothel_member_1"),
		(try_begin),
			(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
			(str_store_troop_name, 11, ":value"),
		(try_end),
		(assign, ":value", "$brothel_member_2"),
		(try_begin),
			(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
			(str_store_troop_name, 12, ":value"),
		(try_end),
		(assign, ":value", "$brothel_member_3"),
		(try_begin),
			(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
			(str_store_troop_name, 13, ":value"),
		(try_end),
		(assign, ":value", "$brothel_member_4"),
		(try_begin),
			(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
			(str_store_troop_name, 14, ":value"),
		(try_end),
		(assign, ":value", "$brothel_member_5"),
		(try_begin),
			(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
			(str_store_troop_name, 15, ":value"),
		(try_end),
		(assign, ":value", "$brothel_member_6"),
		(try_begin),
			(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
			(str_store_troop_name, 16, ":value"),
		(try_end),
		(assign, ":value", "$brothel_member_7"),
		(try_begin),
			(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
			(str_store_troop_name, 17, ":value"),
		(try_end)
	],
	[
		("brothel_enter",
		[],
		"Entrance",
		[
			(assign, "$wm_talk_state", 11),
			(set_jump_mission, "mt_hideout_mission"),
			(assign, "$current_mission_template", "mt_hideout_mission"),
			(assign, ":var_1", "scn_brothel"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 41, "trp_brothel_manager"),
			(call_script, "script_wm_every_global_sett_depend_faction", "$brothel_target_party"),
			(assign, ":value", "$brothel_member_1"),
			(try_begin),
				(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
				(set_visitor, 1, ":value"),
				(set_visitor, 11, "$wm_npc_light_guild_npc"),
			(try_end),
			(assign, ":value", "$brothel_member_2"),
			(try_begin),
				(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
				(set_visitor, 2, ":value"),
				(set_visitor, 12, "$wm_npc_light_guild_npc"),
			(try_end),
			(assign, ":value", "$brothel_member_3"),
			(try_begin),
				(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
				(set_visitor, 3, ":value"),
				(set_visitor, 13, "$wm_npc_arena_master"),
				(set_visitor, 22, "$wm_npc_walker_m"),
			(try_end),
			(assign, ":value", "$brothel_member_4"),
			(try_begin),
				(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
				(set_visitor, 4, ":value"),
				(set_visitor, 14, "$wm_npc_arena_master"),
			(try_end),
			(assign, ":value", "$brothel_member_5"),
			(try_begin),
				(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
				(set_visitor, 5, ":value"),
				(set_visitor, 15, "$wm_npc_light_guild_npc"),
				(set_visitor, 23, "$wm_npc_walker_m"),
				(set_visitor, 24, "$wm_npc_walker_m"),
				(set_visitor, 25, "$wm_npc_walker_m"),
			(try_end),
			(assign, ":value", "$brothel_member_6"),
			(try_begin),
				(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
				(set_visitor, 6, ":value"),
				(set_visitor, 16, "$wm_npc_walker_m"),
				(set_visitor, 21, "$wm_npc_walker_m"),
			(try_end),
			(assign, ":value", "$brothel_member_7"),
			(try_begin),
				(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
				(set_visitor, 7, ":value"),
				(set_visitor, 17, "$wm_npc_arena_master"),
			(try_end),
			(set_jump_entry, 0),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("demolish_brothel",
		[
			(eq, "$adult_content", 1)
		],
		"-Demolish-",
		[
			(jump_to_menu, "mnu_demolish_brothel")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("demolish_fightpit", 0, "Are you sure?",
"none",
	[],
	[
		("demolish_fi_y",
		[],
		"-Demolish-",
		[
			(str_store_party_name, 7, "p_nakepit_party"),
			(assign, "$nakepit_target_party", 0),
			(assign, "$nakepit_prev_income", 0),
			(party_set_flags, "p_nakepit_party", 256, 1),
			(display_message, "str_demolish_wsm"),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("wm_nakepit", 0, "Member List:^ {s11}^ {s12}^ {s13}^ {s14}",
"none",
	[
		(set_background_mesh, "mesh_pic_xex14"),
		(assign, "$need_quit_mission", 0),
		(str_clear, 11),
		(str_clear, 12),
		(str_clear, 13),
		(str_clear, 14),
		(assign, reg11, "$nakepit_prev_income"),
		(assign, ":value", "$nakepit_member_1"),
		(try_begin),
			(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
			(str_store_troop_name, 11, ":value"),
		(try_end),
		(assign, ":value", "$nakepit_member_2"),
		(try_begin),
			(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
			(str_store_troop_name, 12, ":value"),
		(try_end),
		(assign, ":value", "$nakepit_member_3"),
		(try_begin),
			(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
			(str_store_troop_name, 13, ":value"),
		(try_end),
		(assign, ":value", "$nakepit_member_4"),
		(try_begin),
			(is_between, ":value", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(troop_slot_eq, ":value", slot_troop_leaded_party, 3),
			(str_store_troop_name, 14, ":value"),
		(try_end)
	],
	[
		("nakepit_enter",
		[
			(eq, "$adult_content", 1)
		],
		"Entrance",
		[
			#(call_script, "script_molda_music_box", 4, 0),
			(call_script, "script_go_fight_pit_mission")
		], "."),

		("demolish_fightpit",
		[],
		"-Demolish-",
		[
			(jump_to_menu, "mnu_demolish_fightpit")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("lord_talk_duel_menu_jump", 0, "     ",
"none",
	[
		(set_background_mesh, "mesh_pic_visit_train")
	],
	[
		("start_duel",
		[],
		"Start practice duel",
		[
			(call_script, "script_lord_talk_duel_execute")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("wm_pre_battle_talk", 0, "text",
"none",
	[
		(party_get_slot, "$enemy_commander", "$wm_target_party", slot_town_horse_merchant),
		(assign, "$wm_talk_state", 15),
		(call_script, "script_setup_troop_meeting", "$enemy_commander", -1)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
						(play_track, "track_reset_silence", 1), #Enforces new tracks to play ASAP.
		(music_set_situation, mtf_sit_travel),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("trade_caravan_field", 0, "    ",
"none",
	[
		(try_begin),
			(call_script, "script_wm_merchant_items_reset", "trp_town_1_merchant"),
			(party_get_slot, "$prev_encountered_party_culture", "$g_encountered_party", slot_town_claimed_by_player),
		(try_end),
		(try_begin),
			(assign, "$goods_sell_Horse", 3),
			(assign, "$goods_sell_Fine_wood", 3),
			(assign, "$goods_sell_Iron", 3),
			(assign, "$goods_sell_Elephant", 3),
			(assign, "$goods_sell_Whale", 3),
			(assign, "$goods_sell_Fish", 3),
			(assign, "$goods_sell_Maize", 3),
			(assign, "$goods_sell_Copper", 3),
			(assign, "$goods_sell_Marble", 3),
			(assign, "$goods_sell_Pearl", 3),
			(assign, "$goods_sell_Gem", 3),
			(assign, "$goods_sell_Ceramic", 3),
			(assign, "$goods_sell_Gold", 3),
			(assign, "$goods_sell_Silver", 3),
			(assign, "$goods_sell_Ivory", 3),
			(assign, "$goods_sell_Coffee", 3),
			(assign, "$goods_sell_Cacao", 3),
			(assign, "$goods_sell_Silk", 3),
			(assign, "$goods_sell_Nutmeg", 3),
			(assign, "$goods_sell_Allspice", 3),
			(assign, "$goods_sell_Cinnamon", 3),
			(assign, "$goods_sell_Clove", 3),
			(assign, "$goods_sell_Pepper", 3),
			(assign, "$goods_sell_Tabaco", 3),
			(assign, "$goods_sell_Tea", 3),
		(try_end),
		(val_mul, "$goods_sell_Horse", 100),
		(val_mul, "$goods_sell_Fine_wood", 100),
		(val_mul, "$goods_sell_Iron", 100),
		(val_mul, "$goods_sell_Elephant", 100),
		(val_mul, "$goods_sell_Whale", 100),
		(val_mul, "$goods_sell_Fish", 100),
		(val_mul, "$goods_sell_Maize", 100),
		(val_mul, "$goods_sell_Copper", 100),
		(val_mul, "$goods_sell_Marble", 100),
		(val_mul, "$goods_sell_Pearl", 100),
		(val_mul, "$goods_sell_Gem", 100),
		(val_mul, "$goods_sell_Ceramic", 100),
		(val_mul, "$goods_sell_Gold", 100),
		(val_mul, "$goods_sell_Silver", 100),
		(val_mul, "$goods_sell_Ivory", 100),
		(val_mul, "$goods_sell_Coffee", 100),
		(val_mul, "$goods_sell_Cacao", 100),
		(val_mul, "$goods_sell_Silk", 100),
		(val_mul, "$goods_sell_Nutmeg", 100),
		(val_mul, "$goods_sell_Allspice", 100),
		(val_mul, "$goods_sell_Cinnamon", 100),
		(val_mul, "$goods_sell_Clove", 100),
		(val_mul, "$goods_sell_Pepper", 100),
		(val_mul, "$goods_sell_Tabaco", 100),
		(val_mul, "$goods_sell_Tea", 100),
		(start_presentation, "prsnt_wm_item_trade")
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("pirate_king", 0, "You've conquered all the seas of the world. ^^Bonus:^Sea battle ship spawn +1^Ship maintenance cost -66%^Blackship blueprint^Pirate king pistol",
"none",
	[
		(set_background_mesh, "mesh_pic_xex9")
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(troop_add_item, "trp_player", 1353, 0),
			(troop_add_item, "trp_player", 1421, 0),
			(display_message, "str_bluep_black", 0x00ffff00),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("pst_people_info", 0, "          ",
"none",
	[
		(str_clear, 20),
		(str_clear, 21),
		(str_clear, 22),
		(str_clear, 23),
		(str_clear, 24),
		(str_clear, 25),
		(str_clear, 26),
		(str_clear, 27),
		(str_clear, 28),
		(str_clear, 29),
		(str_clear, 30),
		(str_clear, 31),
		(str_clear, 32),
		(str_clear, 33),
		(str_clear, 34),
		(str_clear, 35),
		(str_clear, 36),
		(str_clear, 37),
		(str_clear, 38),
		(str_clear, 39),
		(str_clear, 40),
		(str_clear, 41),
		(str_clear, 42),
		(str_clear, 43),
		(str_clear, 44),
		(str_clear, 45),
		(str_clear, 46),
		(str_clear, 47),
		(str_clear, 48),
		(str_clear, 49),
		(str_clear, 50),
		(start_presentation, "prsnt_pst_faction_hero_info")
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("for_quest_villa", 0, "This is the villa of a noble.",
"none",
	[
		(set_background_mesh, "mesh_pic_xex14")
	],
	[
		("try_lady_beat",
		[
			(eq, "$qquest_type", 23),
			(eq, "$qquest_progress", 0)
		],
		"Disguise and infiltration",
		[
			(assign, "$wm_talk_state", 0),
			(assign, "$wm_quest_mission_anti_skip_menu", 1),
			(assign, ":var_1", "scn_insult_woman"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 1, "trp_nurse_for_lady"),
			(set_visitor, 10, "$qquest_target_troop"),
			(set_jump_mission, "mt_beat_lady"),
			(assign, "$current_mission_template", "mt_beat_lady"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("wanted_named_pirate", 0, "-Wanted-^Dead or Alive^Sea looters. Fearsome pirates. {s8}.^Reward: Alive 15000 / Dead 7500 denars^^by the name of the Harbor master",
"none",
	[
		(set_fixed_point_multiplier, 1000),
		(position_set_x, 0, 200),
		(position_set_y, 0, 275),
		(position_set_z, 0, 750),
		(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$temp_num_01", 0)
	],
	[
		("wanted_accept",
		[],
		"Register that you've taken on the bounty.",
		[
			(assign, "$qquest_type", 31),
			(assign, "$qquest_progress", 0),
			(assign, "$qquest_report_party", "$g_encountered_party"),
			(assign, "$qquest_report_troop", 0),
			(assign, "$qquest_target_party", 0),
			(assign, "$qquest_target_troop", "$temp_num_01"),
			(assign, "$qquest_target_faction", 0),
			(assign, "$qquest_time_day", 15),
			(play_sound, "snd_quest_taken"),
			(display_message, "str_questget", 0x00ffff00),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("jailbreak_enter", 0, "You got the key to the prison.",
"none",
	[
		(set_background_mesh, "mesh_pic_prisoner_man")
	],
	[
		("enter_prison",
		[],
		"Enter the prison.",
		[
			(call_script, "script_wm_troop_type_depend_train", "$g_encountered_party", 100),
			(call_script, "script_molda_scene_culture", "$g_encountered_party"),
			(assign, ":var_1", "$town_scene_prison"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(set_visitor, 16, "$temp_party_troop_10"),
			(set_visitor, 17, "$temp_party_troop_09"),
			(set_visitor, 20, "$qquest_target_troop"),
			(set_jump_mission, "mt_jailbreak"),
			(assign, "$current_mission_template", "mt_jailbreak"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], ".")
	]
	),

	("pst_debrif", 0, "text",
"none",
	[
		(start_presentation, "prsnt_pst_debrif")
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
		#####MUSICBOX battle debrief
						(play_track, "track_reset_silence", 1), #Enforces new tracks to play ASAP.
		(music_set_situation, mtf_sit_travel),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("start_select_age", 0, ".....",
"none",
	[
		(assign, "$start_age", 1184),
		(start_presentation, "prsnt_start_select_age")
	],
	[
		("go_back",
		[],
		"Go back",
		[
			(jump_to_menu, "mnu_start_character_choose_culture")
		], ".")
	]
	),

	("ply_rel_nogod", 0, "Relinquish your religion. Are you sure?",
"none",
	[],
	[
		("ply_rel_nogod_yes",
		[],
		"Abandon the religion",
		[
			(troop_set_slot, "trp_player", 23, 0),
			(display_message, "str_abandon_rel"),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("random_event_in_move", 0, "{s11}",
"none",
	[
		(try_begin),
			(eq, "$rand_event_type", 1),
			(assign, ":value", "str_rand_event_coin"),
			(set_background_mesh, "mesh_pic_payment"),
		(else_try),
			(eq, "$rand_event_type", 2),
			(assign, ":value", "str_rand_event_book"),
			(set_background_mesh, "mesh_pic_library"),
		(else_try),
			(eq, "$rand_event_type", 3),
			(assign, ":value", "str_rand_event_wanderer"),
			(set_background_mesh, "mesh_pic_cla_adventurer"),
		(else_try),
			(eq, "$rand_event_type", 4),
			(assign, ":value", "str_rand_event_freeship"),
			(set_background_mesh, "mesh_pic_xex8"),
		(else_try),
			(eq, "$rand_event_type", 5),
			(assign, ":value", "str_rand_event_insult"),
			(set_background_mesh, "mesh_pic_gameover"),
		(else_try),
			(eq, "$rand_event_type", 6),
			(assign, ":value", "str_rand_event_facination"),
		(else_try),
			(eq, "$rand_event_type", 7),
			(assign, ":value", "str_rand_event_widow"),
		(else_try),
			(eq, "$rand_event_type", 8),
			(assign, ":value", "str_rand_event_meruru"),
		(else_try),
			(eq, "$rand_event_type", 9),
			(assign, ":value", "str_rand_event_catdie"),
			(set_background_mesh, "mesh_pic_camp"),
		(else_try),
			(eq, "$rand_event_type", 10),
			(assign, ":value", "str_rand_event_woman_bath"),
			(set_background_mesh, "mesh_pic_camp"),
		(else_try),
			(eq, "$rand_event_type", 11),
			(str_store_troop_name, 8, "$g_sex_troop_id"),
			(assign, ":value", "str_rand_event_man_comp"),
		(else_try),
			(eq, "$rand_event_type", 12),
			(str_store_troop_name, 8, "$g_sex_troop_id"),
			(str_store_troop_name, 9, "$2nd_sex_troop_id"),
			(assign, ":value", "str_rand_event_man_comp2"),
		(else_try),
			(eq, "$rand_event_type", 13),
			(assign, ":value", "str_rand_event_invest"),
			(set_background_mesh, "mesh_pic_bank_back"),
		(else_try),
			(eq, "$rand_event_type", 14),
			(assign, ":value", "str_rand_event_orphan"),
			(set_background_mesh, "mesh_pic_looted_village"),
		(else_try),
			(assign, ":value", "str_empty_string"),
			(set_background_mesh, "mesh_pic_camp"),
		(try_end),
		(assign, ":value_2", 0),
		(try_begin),
			(this_or_next|eq, "$rand_event_type", 6),
			(eq, "$rand_event_type", 7),
			(call_script, "script_wm_every_global_sett_depend_faction", "$last_visit_town"),
			(assign, "$g_sex_troop_id", "$wm_npc_walker_f"),
			(assign, ":value_2", "$g_sex_troop_id"),
		(else_try),
			(eq, "$rand_event_type", 8),
			(assign, "$g_sex_troop_id", "trp_spy_walker_2"),
			(assign, ":value_2", "$g_sex_troop_id"),
		(else_try),
			(this_or_next|eq, "$rand_event_type", 12),
			(eq, "$rand_event_type", 11),
			(assign, ":value_2", "$g_sex_troop_id"),
		(else_try),
			(eq, "$rand_event_type", 14),
			(assign, ":value_2", "trp_tt_lady_orphan_01"),
		(try_end),
		(try_begin),
			(gt, ":value_2", 0),
			(set_fixed_point_multiplier, 1000),
			(position_set_x, 0, 600),
			(position_set_y, 0, 400),
			(position_set_z, 0, 750),
			(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", ":value_2", 0),
		(try_end),
		(str_store_string, 11, ":value")
	],
	[
		("coin_choice_1",
		[
			(eq, "$rand_event_type", 1)
		],
		"I will distribute the money evenly between myself and my companions.",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 500, 87),
			(call_script, "script_companion_relation_level", 5),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("coin_choice_2",
		[
			(eq, "$rand_event_type", 1)
		],
		"I will spend the money myself.",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 3000, 87),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("book_choice_1",
		[
			(eq, "$rand_event_type", 2),
			(call_script, "script_party_money_level_ge", "p_main_party", 1000),
			(eq, "$wm_mo_continue", 1)
		],
		"I will buy the book.",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34),
			(store_random_in_range, ":random_in_range_1081_1252", 1081, 1252),
			(troop_add_item, "trp_player", ":random_in_range_1081_1252"),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("book_choice_2",
		[
			(eq, "$rand_event_type", 2)
		],
		"Kill the old man, and take the book.",
		[
			(call_script, "script_wm_honor_change_diff", "trp_player", 5, 34),
			(store_random_in_range, ":random_in_range_1081_1252", 1081, 1252),
			(troop_add_item, "trp_player", ":random_in_range_1081_1252"),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("book_choice_3",
		[
			(eq, "$rand_event_type", 2)
		],
		"I don't care for it.",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("wanderer_choice_1",
		[
			(eq, "$rand_event_type", 3)
		],
		"Front side.",
		[
			(store_random_in_range, ":random_in_range_0_2", 0, 2),
			(try_begin),
				(eq, ":random_in_range_0_2", 0),
				(call_script, "script_new_troop_add_sc", "trp_event_wanderer", 1),
				(display_message, "str_rand_event_wanderer_1g"),
			(else_try),
				(display_message, "str_rand_event_wanderer_1b"),
			(try_end),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("wanderer_choice_2",
		[
			(eq, "$rand_event_type", 3)
		],
		"Back side.",
		[
			(store_random_in_range, ":random_in_range_0_2", 0, 2),
			(try_begin),
				(eq, ":random_in_range_0_2", 0),
				(call_script, "script_new_troop_add_sc", "trp_event_wanderer", 1),
				(display_message, "str_rand_event_wanderer_1g"),
			(else_try),
				(display_message, "str_rand_event_wanderer_1b"),
			(try_end),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("freeship_choice_1",
		[
			(eq, "$rand_event_type", 4)
		],
		"I will take the ship.",
		[
			(assign, "$m_ship_type_1", 1404),
			(party_set_slot, "p_main_party", slot_party_ai_substate, "icon_galley"),
			(party_get_slot, ":main_party_ai_substate", "p_main_party", slot_party_ai_substate),
			(party_set_icon, "p_main_party", ":main_party_ai_substate"),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("freeship_choice_2",
		[
			(eq, "$rand_event_type", 4)
		],
		"This ship has a sinister feeling. I'll discard this one.",
		[
			(call_script, "script_wm_honor_change_diff", "trp_player", 5, 87),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("insult_choice_1",
		[
			(eq, "$rand_event_type", 5)
		],
		"Retaliate with humor!",
		[
			(store_random_in_range, ":random_in_range_0_100", 0, 100),
			(store_attribute_level, ":attribute_level_player_3", "trp_player", 3),
			(val_add, ":random_in_range_0_100", ":attribute_level_player_3"),
			(try_begin),
				(lt, ":random_in_range_0_100", 50),
				(call_script, "script_moral_level_diff", "p_main_party", -25),
				(call_script, "script_wm_honor_change_diff", "trp_player", 5, 34),
				(display_message, "str_rand_event_insult_b"),
			(else_try),
				(call_script, "script_moral_level_diff", "p_main_party", 25),
				(call_script, "script_wm_honor_change_diff", "trp_player", 5, 87),
				(display_message, "str_rand_event_insult_g"),
			(try_end),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("insult_choice_2",
		[
			(eq, "$rand_event_type", 5),
		],
		"I make a challenge for a duel to defend my honour.",
		[
			(assign, "$wm_duel_persnal", 1),
			(assign, "$wm_battle_result_state", 0),
			(assign, "$wm_duel_won", 0),
			(assign, "$wm_talk_state", 0),
			(assign, "$wm_quest_mission_anti_skip_menu", 1),
			(assign, "$molda_start_map_conversation", -1),
			(call_script, "script_molda_scene_culture", "$last_visit_town"),
			(assign, ":var_1", "$town_scene_arena"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(party_get_num_companion_stacks, ":num_companion_stacks_main_party", "p_main_party"),
			(assign, ":value", "trp_hh_m_1"),
			(try_for_range, ":localvariable", 0, ":num_companion_stacks_main_party"),
				(party_stack_get_troop_id, ":party_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
				(gt, ":party_stack_troop_id_main_party_localvariable", "trp_army_size_troop"),
				(neg|troop_is_hero, ":party_stack_troop_id_main_party_localvariable"),
				(party_stack_get_size, ":party_stack_size_main_party_localvariable", "p_main_party", ":localvariable"),
				(gt, ":party_stack_size_main_party_localvariable", 0),
				(store_character_level, ":character_level_party_stack_troop_id_main_party_localvariable", ":party_stack_troop_id_main_party_localvariable"),
				(store_character_level, ":character_level_value", ":value"),
				(try_begin),
					(eq, ":value", "trp_hh_m_1"),
					(assign, ":value", ":party_stack_troop_id_main_party_localvariable"),
				(else_try),
					(gt, ":character_level_party_stack_troop_id_main_party_localvariable", ":character_level_value"),
					(assign, ":value", ":party_stack_troop_id_main_party_localvariable"),
				(try_end),
			(try_end),
			(party_remove_members, "p_main_party", ":value", 1),
			(set_visitor, 41, ":value"),
			(set_visitor, 0, "trp_player"),
			(set_jump_mission, "mt_arena_mission"),
			(assign, "$current_mission_template", "mt_arena_mission"),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("insult_choice_3",
		[
			(eq, "$rand_event_type", 5)
		],
		"Ignore it.",
		[
			(call_script, "script_moral_level_diff", "p_main_party", -50),
			(call_script, "script_wm_honor_change_diff", "trp_player", 7, 34),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("facination_choice_1",
		[
			(eq, "$rand_event_type", 6)
		],
		"Persuasion through dialogue.",
		[
			(store_random_in_range, ":random_in_range_0_10", 0, 10),
			(troop_get_slot, ":player_betrothal_time", "trp_player", slot_troop_betrothal_time),
			(val_add, ":random_in_range_0_10", ":player_betrothal_time"),
			(try_begin),
				(ge, ":random_in_range_0_10", 3),
				(assign, "$mt_action_on", 1),
				(display_message, "str_rand_event_facination_1_y"),
				(jump_to_menu, "mnu_mt_male_p_fuck_normal"),
			(else_try),
				(display_message, "str_rand_event_facination_1_n"),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(try_end)
		], "."),

		("facination_choice_2",
		[
			(eq, "$rand_event_type", 6)
		],
		"Tries prostitution.",
		[
			(store_random_in_range, ":random_in_range_0_10", 0, 10),
			(troop_get_slot, ":player_betrothal_time", "trp_player", slot_troop_betrothal_time),
			(val_add, ":random_in_range_0_10", ":player_betrothal_time"),
			(try_begin),
				(ge, ":random_in_range_0_10", 3),
				(assign, "$mt_action_on", 1),
				(display_message, "str_rand_event_facination_2_y"),
				(jump_to_menu, "mnu_mt_male_p_fuck_civil_trade"),
			(else_try),
				(display_message, "str_rand_event_facination_2_n"),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(try_end)
		], "."),

		("facination_choice_3",
		[
			(eq, "$rand_event_type", 6)
		],
		"Rape her.",
		[
			(assign, "$mt_action_on", 1),
			(display_message, "str_rand_event_facination_3"),
			(call_script, "script_wm_honor_change_diff", "trp_player", 5, 34),
			(jump_to_menu, "mnu_mt_male_p_fuck_rape")
		], "."),

		("facination_choice_4",
		[
			(eq, "$rand_event_type", 6)
		],
		"Think about past family.",
		[
			(call_script, "script_troop_type_sett", "trp_player"),
			(try_begin),
				(gt, "$troop_gender_type", 10),
				(play_sound, "snd_cryyy_female"),
			(else_try),
				(play_sound, "snd_man_sad_cry"),
			(try_end),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("widow_choice_1",
		[
			(eq, "$rand_event_type", 7)
		],
		"Embracing her.",
		[
			(assign, "$mt_action_on", 1),
			(jump_to_menu, "mnu_mt_male_p_fuck_normal")
		], "."),

		("widow_choice_2",
		[
			(eq, "$rand_event_type", 7)
		],
		"Close the door.",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("meruru_choice_1",
		[
			(eq, "$rand_event_type", 8),
			(call_script, "script_party_money_level_ge", "p_main_party", 10),
			(eq, "$wm_mo_continue", 1)
		],
		"Give the money to her.",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 10, 34),
			(assign, "$mt_action_on", 1),
			(display_message, "str_rand_event_meruru_1"),
			(jump_to_menu, "mnu_mt_male_p_fuck_normal")
		], "."),

		("meruru_choice_2",
		[
			(eq, "$rand_event_type", 8)
		],
		"Expelled her.",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("catdie_cont",
		[
			(eq, "$rand_event_type", 9)
		],
		"Continue...",
		[
			(call_script, "script_troop_type_sett", "trp_player"),
			(try_begin),
				(gt, "$troop_gender_type", 10),
				(play_sound, "snd_cryyy_female"),
			(else_try),
				(play_sound, "snd_man_sad_cry"),
			(try_end),
			(troop_remove_items, "trp_player", 1438, 1),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("woman_bath_choice_1",
		[
			(eq, "$rand_event_type", 10)
		],
		"Masturbate while watching.",
		[
			(assign, "$wm_talk_state", 13),
			(assign, ":var_1", "scn_public_bath"),
			(modify_visitors_at_site, ":var_1"),
			(reset_visitors),
			(try_begin),
				(assign, ":var_2", 16),
				(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
					(call_script, "script_wm_main_party_has_troop_sc", ":troop"),
					(eq, "$wm_comp_continue", 1),
					(neg|troop_slot_eq, "trp_player", slot_troop_state, ":troop"),
					(set_visitor, ":var_2", ":troop"),
					(val_add, ":var_2", 1),
				(try_end),
			(try_end),
			(set_jump_mission, "mt_camp_mission"),
			(assign, "$current_mission_template", "mt_camp_mission"),
			(set_jump_entry, 9),
			(jump_to_scene, ":var_1"),
			(change_screen_mission)
		], "."),

		("woman_bath_choice_2",
		[
			(eq, "$rand_event_type", 10)
		],
		"I don't care.",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("mancomp_choice_1",
		[
			(eq, "$rand_event_type", 11)
		],
		"Allow your body to him.",
		[
			(call_script, "script_change_player_relation_with_troop", "$g_sex_troop_id", 15),
			(assign, "$mt_action_on", 1),
			(jump_to_menu, "mnu_mt_female_p_fuck_reln")
		], "."),

		("mancomp_choice_2",
		[
			(eq, "$rand_event_type", 11)
		],
		"Threw him out.",
		[
			(store_random_in_range, ":random_in_range_0_4", 0, 4),
			(try_begin),
				(eq, ":random_in_range_0_4", 0),
				(call_script, "script_change_player_relation_with_troop", "$g_sex_troop_id", -15),
				(display_message, "str_rand_event_man_comp_r"),
				(assign, "$mt_action_on", 1),
				(jump_to_menu, "mnu_mt_female_p_fuck_rape"),
			(else_try),
				(display_message, "str_rand_event_man_comp_s"),
				(call_script, "script_change_player_relation_with_troop", "$g_sex_troop_id", -3),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(try_end)
		], "."),

		("2mancomp_choice_1",
		[
			(eq, "$rand_event_type", 12)
		],
		"Allow your body to them.",
		[
			(call_script, "script_change_player_relation_with_troop", "$g_sex_troop_id", 15),
			(call_script, "script_change_player_relation_with_troop", "$2nd_sex_troop_id", 15),
			(assign, "$mt_action_on", 1),
			(jump_to_menu, "mnu_mt_girl_player_1girl_2man_three_some")
		], "."),

		("2mancomp_choice_2",
		[
			(eq, "$rand_event_type", 12)
		],
		"Threw them out.",
		[
			(store_random_in_range, ":random_in_range_0_4", 0, 4),
			(try_begin),
				(eq, ":random_in_range_0_4", 0),
				(call_script, "script_change_player_relation_with_troop", "$g_sex_troop_id", -15),
				(call_script, "script_change_player_relation_with_troop", "$2nd_sex_troop_id", -15),
				(display_message, "str_rand_event_man_comp_r"),
				(assign, "$mt_action_on", 1),
				(jump_to_menu, "mnu_mt_girl_player_1girl_2man_three_some_raped"),
			(else_try),
				(display_message, "str_rand_event_man_comp_s"),
				(call_script, "script_change_player_relation_with_troop", "$g_sex_troop_id", -3),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(try_end)
		], "."),

		("invest_choice_1",
		[
			(eq, "$rand_event_type", 13),
			(call_script, "script_party_money_level_ge", "p_main_party", 5000),
			(eq, "$wm_mo_continue", 1)
		],
		"Invest to him (5000)",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 5000, 34),
			(store_random_in_range, ":random_in_range_0_2", 0, 2),
			(try_begin),
				(eq, ":random_in_range_0_2", 0),
				(call_script, "script_party_money_level_diff", "p_main_party", 20000, 87),
				(display_message, "str_rand_event_invest_g"),
			(else_try),
				(call_script, "script_troop_type_sett", "trp_player"),
				(try_begin),
					(gt, "$troop_gender_type", 10),
					(play_sound, "snd_cryyy_female"),
				(else_try),
					(play_sound, "snd_man_sad_cry"),
				(try_end),
				(display_message, "str_rand_event_invest_b"),
			(try_end),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("invest_choice_2",
		[
			(eq, "$rand_event_type", 13)
		],
		"no investment.",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("orphan_choice_1",
		[
			(eq, "$rand_event_type", 14)
		],
		"Adopt her.",
		[
			(troop_set_slot, "trp_tt_lady_orphan_01", slot_troop_last_persuasion_time, 1),
			(troop_set_slot, "trp_tt_lady_orphan_02", slot_troop_last_persuasion_time, 1),
			(troop_set_slot, "trp_tt_lady_orphan_03", slot_troop_last_persuasion_time, 1),
			(troop_set_slot, "trp_tt_lady_orphan_04", slot_troop_last_persuasion_time, 1),
			(troop_set_slot, "trp_tt_lady_orphan_05", slot_troop_last_persuasion_time, 1),
			(troop_set_slot, "trp_tt_lady_orphan_01", slot_troop_last_quest_betrayed, 5),
			(troop_set_slot, "trp_tt_lady_orphan_02", slot_troop_last_quest_betrayed, 5),
			(troop_set_slot, "trp_tt_lady_orphan_03", slot_troop_last_quest_betrayed, 5),
			(troop_set_slot, "trp_tt_lady_orphan_04", slot_troop_last_quest_betrayed, 5),
			(troop_set_slot, "trp_tt_lady_orphan_05", slot_troop_last_quest_betrayed, 5),
			(troop_set_slot, "trp_tt_lady_orphan_01", 15, 1),
			(troop_set_slot, "trp_tt_lady_orphan_02", 15, 1),
			(troop_set_slot, "trp_tt_lady_orphan_03", 15, 1),
			(troop_set_slot, "trp_tt_lady_orphan_04", 15, 1),
			(troop_set_slot, "trp_tt_lady_orphan_05", 15, 1),
			(assign, "$orphan_girl_troop_id", "trp_tt_lady_orphan_01"),
			(assign, "$orphan_grown_count", 0),
			(assign, "$orphan_train_type", 0),
			(display_message, "str_rand_event_orphan_pre"),
			(display_message, "str_rand_event_orphan_tip"),
			(jump_to_menu, "mnu_orphan_pre_sett")
		], "."),

		("orphan_choice_2",
		[
			(eq, "$rand_event_type", 14)
		],
		"Sorry. I can't.",
		[
			(jump_to_menu, "mnu_orphan_no_sure")
		], "."),

		("event_zero_return",
		[
			(eq, "$rand_event_type", 0)
		],
		"I don't care.",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("orphan_pre_sett", 0, "War orphan Fabia. now she is your companion. You can meet Fabia in camp.^ she does not participate combat for a 120 month. After 120 month, she will grown to be adult. ^She need training till grown up. ^You need talk with her for choice training category.",
"none",
	[
		(set_fixed_point_multiplier, 1000),
		(position_set_x, 0, 600),
		(position_set_y, 0, 400),
		(position_set_z, 0, 750),
		(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "trp_tt_lady_orphan_01", 0)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("orphan_no_sure", 0, "adopt orphan is disabled permanently. are you sure?",
"none",
	[
		(set_fixed_point_multiplier, 1000),
		(position_set_x, 0, 600),
		(position_set_y, 0, 400),
		(position_set_z, 0, 750),
		(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "trp_tt_lady_orphan_01", 0)
	],
	[
		("orphan_sure",
		[],
		"Go back.",
		[
			(jump_to_menu, "mnu_random_event_in_move")
		], "."),

		("orphan_sure",
		[],
		"Sorry. I can't.",
		[
			(assign, "$orphan_girl_troop_id", -1),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("pst_holywar", 0, "text",
"none",
	[
		(assign, "$holywar_ply_opinion", 0),
		(assign, "$holy_war_agreed", 0),
		(start_presentation, "prsnt_pst_holywar")
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("opt_face_and_gender_change", 0, "Caution!!!^If you change to different gender, it will cause of bug.",
"none",
	[],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("start_male11",
		[],
		"Male",
		[
			(troop_set_type, "trp_player", 0),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 1),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("start_male22",
		[],
		"Male (Iboltax Changed meshe)",
		[
			(troop_set_type, "trp_player", 2),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 1),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("start_other_rom",
		[],
		"Male (dark skin)",
		[
			(troop_set_type, "trp_player", 8),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 3),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("start_male44",
		[],
		"Male (more dark)",
		[
			(troop_set_type, "trp_player", 6),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 3),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("start_female11",
		[],
		"Female",
		[
			(troop_set_type, "trp_player", 1),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 4),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("start_female44",
		[],
		"Female (Corprus meshe)",
		[
			(troop_set_type, "trp_player", 7),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 6),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("start_female22",
		[],
		"Female (ROK meshe)",
		[
			(troop_set_type, "trp_player", 3),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 2),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("start_other_row",
		[],
		"Female (dark skin)",
		[
			(troop_set_type, "trp_player", 14),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 3),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("start_other_dark",
		[],
		"Female (ROK dark skin)",
		[
			(troop_set_type, "trp_player", 15),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 3),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("start_other_11",
		[],
		"Female (More dark)",
		[
			(troop_set_type, "trp_player", 13),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 14),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("start_female33",
		[],
		"Female Western (Npc only meshe)",
		[
			(troop_set_type, "trp_player", 5),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 6),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("start_other_33",
		[],
		"Female Orient (Npc only meshe)",
		[
			(troop_set_type, "trp_player", 10),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 2),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("start_other_34",
		[],
		"Female Short height Western (Npc only meshe)",
		[
			(troop_set_type, "trp_player", 11),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 1),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("start_other_434",
		[],
		"Female Short height Orient (Npc only meshe)",
		[
			(troop_set_type, "trp_player", 12),
			(troop_set_slot, "trp_player", slot_troop_last_quest_betrayed, 3),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("stay_army_dispose_sure", 0, "Your army of {s10} will be disbanded. are you sure?",
"none",
	[
		(set_background_mesh, "mesh_pic_camp"),
		(str_store_party_name, 10, "$ply_staying_party_no")
	],
	[
		("stay_army_disband_y",
		[],
		"Disband old army and recruit for new army",
		[
			(assign, "$ply_staying_party_no", 0),
			(assign, "$ply_staying_army_size", 0),
			(assign, "$ply_staying_army_recruit_on", 0),
			(display_message, "str_t_armystay_disband", 0x00ff0000),
			(assign, "$player_recruit_train_start", 1),
			(rest_for_hours_interactive, 8760, 6, 0),
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("stay_army_disband_n",
		[],
		"[Back]",
		[
			(jump_to_menu, "mnu_wm_town_visit")
		], ".")
	]
	),

	("main_quest_menu", 0, "{s11}",
"none",
	[
		(try_begin),
			(lt, "$main_q_step", 1),
			(str_store_string, 11, "str_mq_1_1"),
			(set_background_mesh, "mesh_pic_prisoner_wilderness"),
		(else_try),
			(eq, "$main_q_step", 3),
			(set_background_mesh, "mesh_pic_messenger"),
			(call_script, "script_check_faction_border_faction"),
			(assign, "$main_q_faction", 0),
			(try_for_range, ":number", 31, 40),
				(faction_get_slot, ":kingdom_pick_start_faction_number", "$kingdom_pick_start_faction", ":number"),
				(this_or_next|is_between, ":kingdom_pick_start_faction_number", "fac_pioneers", "fac_undeads"),
				(is_between, ":kingdom_pick_start_faction_number", "fac_kingdom_1", "fac_kingdoms_end"),
				(neq, ":kingdom_pick_start_faction_number", "$kingdom_pick_start_faction"),
				(neq, ":kingdom_pick_start_faction_number", "$start_enemy_fac"),
				(try_begin),
					(eq, "$main_q_faction", 0),
					(assign, "$main_q_faction", ":kingdom_pick_start_faction_number"),
				(else_try),
					(store_random_in_range, ":random_in_range_0_3", 0, 3),
					(neq, ":random_in_range_0_3", 0),
					(assign, "$main_q_faction", ":kingdom_pick_start_faction_number"),
				(try_end),
			(try_end),
			(try_begin),
				(eq, "$main_q_faction", 0),
				(assign, "$main_q_faction", "$start_enemy_fac"),
			(try_end),
			(str_store_faction_name, 12, "$main_q_faction"),
			(str_store_string, 11, "str_mq_1_3"),
		(else_try),
			(eq, "$main_q_step", 7),
			(str_store_string, 11, "str_mq_1_7"),
			(set_background_mesh, "mesh_pic_steppe_bandits"),
		(else_try),
			(eq, "$main_q_step", 8),
			(party_set_flags, "p_ruin_dummy_5", 256, 1),
			(assign, "$main_q_party", 0),
			(try_for_range, ":party", "p_tradeguild1", "p_tradeguild_end"),
				(store_distance_to_party_from_party, ":distance_to_party_from_party_party_main_party", ":party", "p_main_party"),
				(try_begin),
					(eq, "$main_q_party", 0),
					(assign, "$main_q_party", ":party"),
				(else_try),
					(store_distance_to_party_from_party, ":distance_to_party_from_party_main_q_party_main_party", "$main_q_party", "p_main_party"),
					(lt, ":distance_to_party_from_party_party_main_party", ":distance_to_party_from_party_main_q_party_main_party"),
					(assign, "$main_q_party", ":party"),
				(try_end),
			(try_end),
			(str_store_party_name, 10, "$main_q_party"),
			(str_store_string, 11, "str_mq_1_8"),
			(set_background_mesh, "mesh_pic_sally_out"),
		(else_try),
			(eq, "$main_q_step", 10),
			(assign, "$main_q_party", 0),
			(try_for_range, ":party", "p_pyongyang", "p_place_end"),
				(this_or_next|party_slot_eq, ":party", slot_town_claimed_by_player, 6),
				(party_slot_eq, ":party", slot_town_claimed_by_player, 7),
				(try_begin),
					(eq, "$main_q_party", 0),
					(assign, "$main_q_party", ":party"),
				(else_try),
					(store_random_in_range, ":random_in_range_0_3", 0, 15),
					(eq, ":random_in_range_0_3", 0),
					(assign, "$main_q_party", ":party"),
				(try_end),
			(try_end),
			(str_store_party_name, 10, "$main_q_party"),
			(str_store_string, 11, "str_mq_1_10"),
			(set_background_mesh, "mesh_pic_bank_back"),
		(else_try),
			(eq, "$main_q_step", 14),
			(set_background_mesh, "mesh_1pic_ruin_107"),
			(str_store_string, 11, "str_mq_1_14"),
		(else_try),
			(eq, "$main_q_step", 16),
			(set_background_mesh, "mesh_pic_xex14"),
			(str_store_string, 11, "str_mq_1_16"),
		(else_try),
			(eq, "$main_q_step", 18),
			(set_background_mesh, "mesh_pic_xex14"),
			(str_store_string, 11, "str_mq_1_18"),
		(else_try),
			(eq, "$main_q_step", 19),
			(set_background_mesh, "mesh_pic_messenger"),
			(assign, "$main_q_party", 0),
			(troop_get_slot, ":player_23", "trp_player", 23),
			(assign, ":value", 3),
			(assign, "$first_comp_id", "trp_npc15"),
			(try_begin),
				(this_or_next|eq, ":player_23", 7),
				(this_or_next|eq, ":player_23", 6),
				(eq, ":player_23", 3),
				(assign, ":value", 6),
				(assign, "$first_comp_id", "trp_npc16"),
			(else_try),
				(this_or_next|eq, ":player_23", 15),
				(this_or_next|eq, ":player_23", 8),
				(this_or_next|eq, ":player_23", 5),
				(eq, ":player_23", 4),
				(assign, ":value", 8),
				(assign, "$first_comp_id", "trp_npc_17"),
			(try_end),
			(try_for_range, ":party", "p_pyongyang", "p_place_end"),
				(party_slot_eq, ":party", slot_town_claimed_by_player, ":value"),
				(try_begin),
					(eq, "$main_q_party", 0),
					(assign, "$main_q_party", ":party"),
				(else_try),
					(store_random_in_range, ":random_in_range_0_3", 0, 15),
					(eq, ":random_in_range_0_3", 0),
					(assign, "$main_q_party", ":party"),
				(try_end),
			(try_end),
			(str_store_troop_name, 14, "$first_comp_id"),
			(str_store_party_name, 10, "$main_q_party"),
			(str_store_string, 11, "str_mq_1_19"),
		(else_try),
			(eq, "$main_q_step", 21),
			(set_background_mesh, "mesh_pic_camp_meet"),
			(str_store_troop_name, 14, "$first_comp_id"),
			(str_store_string, 11, "str_mq_1_21"),
		(else_try),
			(eq, "$main_q_step", 23),
			(set_background_mesh, "mesh_pic_sea_raiders"),
			(str_store_troop_name, 14, "$first_comp_id"),
			(str_store_string, 11, "str_mq_1_23"),
		(else_try),
			(eq, "$main_q_step", 24),
			(set_background_mesh, "mesh_pic_sea_raiders"),
			(str_store_troop_name, 14, "$first_comp_id"),
			(str_store_string, 11, "str_mq_1_24"),
		(else_try),
			(eq, "$main_q_step", 25),
			(set_background_mesh, "mesh_pic_messenger"),
			(str_store_string, 11, "str_mq_1_25"),
		(else_try),
			(eq, "$main_q_step", 26),
			(set_background_mesh, "mesh_pic_forest_bandits"),
			(str_store_string, 11, "str_mq_1_26"),
		(else_try),
			(eq, "$main_q_step", 27),
			(set_background_mesh, "mesh_pic_camp"),
			(str_store_string, 11, "str_mq_1_27"),
		(else_try),
			(eq, "$main_q_step", 28),
			(set_background_mesh, "mesh_pic_recruits"),
			(str_store_string, 11, "str_mq_1_28"),
		(else_try),
			(eq, "$main_q_step", 31),
			(set_background_mesh, "mesh_pic_steppe_bandits"),
			(str_store_string, 11, "str_mq_1_31"),
		(else_try),
			(eq, "$main_q_step", 32),
			(set_background_mesh, "mesh_pic_prisoner_fem"),
			(troop_get_slot, ":player_23", "trp_player", 23),
			(assign, "$main_q_troop", "trp_tt_lady_ex_18"),
			(try_begin),
				(this_or_next|eq, ":player_23", 7),
				(this_or_next|eq, ":player_23", 6),
				(eq, ":player_23", 3),
				(assign, "$main_q_troop", "trp_tt_lady_ex_10"),
			(else_try),
				(this_or_next|eq, ":player_23", 15),
				(this_or_next|eq, ":player_23", 8),
				(this_or_next|eq, ":player_23", 5),
				(eq, ":player_23", 4),
				(assign, "$main_q_troop", "trp_tt_lady_ex_01"),
			(try_end),
			(str_store_troop_name, 14, "$main_q_troop"),
			(str_store_string, 11, "str_mq_1_32"),
		(else_try),
			(eq, "$main_q_step", 33),
			(set_background_mesh, "mesh_pic_weknow"),
			(str_store_string, 11, "str_mq_1_33"),
		(else_try),
			(eq, "$main_q_step", 35),
			(set_background_mesh, "mesh_pic_camp_meet"),
			(str_store_string, 11, "str_mq_1_35"),
		(else_try),
			(eq, "$main_q_step", 36),
			(set_background_mesh, "mesh_pic_wounded"),
			(str_store_string, 11, "str_mq_1_36"),
		(else_try),
			(eq, "$main_q_step", 37),
			(set_background_mesh, "mesh_pic_cla_merchant"),
			(str_store_string, 11, "str_mq_1_37"),
		(else_try),
			(eq, "$main_q_step", 38),
			(set_background_mesh, "mesh_pic_weknow"),
			(str_store_string, 11, "str_mq_1_33"),
		(else_try),
			(eq, "$main_q_step", 40),
			(set_background_mesh, "mesh_pic_camp_meet"),
			(str_store_string, 11, "str_mq_1_40"),
		(else_try),
			(eq, "$main_q_step", 41),
			(set_background_mesh, "mesh_pic_wounded"),
			(str_store_string, 11, "str_mq_1_41"),
		(else_try),
			(eq, "$main_q_step", 42),
			(set_background_mesh, "mesh_pic_bank_back"),
			(str_store_string, 11, "str_mq_1_42"),
		(else_try),
			(eq, "$main_q_step", 43),
			(set_background_mesh, "mesh_pic_xex14"),
			(str_store_string, 11, "str_mq_1_43"),
		(else_try),
			(eq, "$main_q_step", 45),
			(set_background_mesh, "mesh_pic_xex14"),
			(str_store_string, 11, "str_mq_1_45"),
		(else_try),
			(eq, "$main_q_step", 46),
			(set_background_mesh, "mesh_pic_xex14"),
			(str_store_string, 11, "str_mq_1_46"),
		(else_try),
			(eq, "$main_q_step", 47),
			(set_background_mesh, "mesh_pic_looted_village"),
			(str_store_string, 11, "str_mq_1_47"),
		(else_try),
			(eq, "$main_q_step", 48),
			(set_fixed_point_multiplier, 1000),
			(position_set_x, 0, 600),
			(position_set_y, 0, 400),
			(position_set_z, 0, 750),
			(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$main_q_troop", 0),
			(str_store_troop_name, 14, "$main_q_troop"),
			(str_store_string, 11, "str_mq_1_48"),
		(else_try),
			(eq, "$main_q_step", 49),
			(set_fixed_point_multiplier, 1000),
			(position_set_x, 0, 600),
			(position_set_y, 0, 400),
			(position_set_z, 0, 750),
			(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$younger_sister_id", 0),
			(str_store_string, 11, "str_mq_1_49"),
		(else_try),
			(eq, "$main_q_step", 50),
			(set_background_mesh, "mesh_pic_xex14"),
			(str_store_string, 11, "str_mq_1_50"),
		(else_try),
			(eq, "$main_q_step", 51),
			(set_fixed_point_multiplier, 1000),
			(position_set_x, 0, 600),
			(position_set_y, 0, 400),
			(position_set_z, 0, 750),
			(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$younger_sister_id", 0),
			(str_store_string, 11, "str_mq_1_51"),
		(else_try),
			(eq, "$main_q_step", 54),
			(str_store_string, 11, "str_mq_1_54"),
		(else_try),
			(eq, "$main_q_step", 55),
			(str_store_string, 11, "str_mq_1_55"),
		(else_try),
			(eq, "$main_q_step", 56),
			(str_store_string, 11, "str_mq_1_56"),
			(set_background_mesh, "mesh_pic_messenger"),
		(else_try),
			(eq, "$main_q_step", 57),
			(assign, "$main_q_party", "$last_visit_town"),
			(str_store_party_name, 10, "$main_q_party"),
			(str_store_string, 11, "str_mq_1_57"),
			(set_background_mesh, "mesh_pic_messenger"),
		(else_try),
			(eq, "$main_q_step", 58),
			(str_store_string, 11, "str_mq_1_58"),
			(set_background_mesh, "mesh_pic_siege_sighted"),
		(else_try),
			(eq, "$main_q_step", 59),
			(str_store_string, 11, "str_mq_1_59"),
			(set_background_mesh, "mesh_pic_villageriot"),
		(else_try),
			(eq, "$main_q_step", 60),
			(str_store_party_name, 10, "$main_q_party"),
			(str_store_string, 11, "str_mq_1_60"),
			(set_background_mesh, "mesh_pic_towndes"),
		(else_try),
			(eq, "$main_q_step", 61),
			(str_store_string, 11, "str_mq_1_61"),
			(set_background_mesh, "mesh_pic_messenger"),
		(else_try),
			(eq, "$main_q_step", 64),
			(str_store_string, 11, "str_mq_1_64"),
			(set_background_mesh, "mesh_pic_xex8"),
		(else_try),
			(eq, "$main_q_step", 65),
			(str_store_string, 11, "str_mq_1_65"),
			(set_background_mesh, "mesh_pic_xex12"),
		(else_try),
			(eq, "$main_q_step", 66),
			(str_store_string, 11, "str_mq_1_66"),
			(set_background_mesh, "mesh_pic_messenger"),
		(else_try),
			(eq, "$main_q_step", 69),
			(str_store_string, 11, "str_mq_1_69"),
		(else_try),
			(eq, "$main_q_step", 70),
			(str_store_string, 11, "str_mq_1_70"),
		(else_try),
			(eq, "$main_q_step", 71),
			(set_fixed_point_multiplier, 1000),
			(position_set_x, 0, 600),
			(position_set_y, 0, 400),
			(position_set_z, 0, 750),
			(set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$younger_sister_id", 0),
			(str_store_string, 11, "str_mq_1_71"),
		(else_try),
			(eq, "$main_q_step", 72),
			(str_store_string, 11, "str_mq_1_72"),
		(else_try),
			(eq, "$main_q_step", 73),
			(eq, "$g_encountered_party", "p_ruin_dummy_3"),
			(str_store_string, 11, "str_mq_1_73"),
			(set_background_mesh, "mesh_pic_looted_village"),
		(else_try),
			(eq, "$main_q_step", 74),
			(str_store_string, 11, "str_mq_1_74"),
		(else_try),
			(eq, "$main_q_step", 76),
			(str_store_string, 11, "str_mq_1_76"),
		(else_try),
			(eq, "$main_q_step", 79),
			(eq, "$g_encountered_party", "p_ruin_dummy_4"),
			(set_background_mesh, "mesh_1pic_ruin_107"),
			(str_store_string, 11, "str_mq_1_79"),
		(else_try),
			(eq, "$main_q_step", 80),
			(set_background_mesh, "mesh_1pic_ruin_107"),
			(str_store_string, 11, "str_mq_1_80"),
		(else_try),
			(eq, "$main_q_step", 81),
			(str_store_string, 11, "str_mq_1_81"),
		(else_try),
			(eq, "$main_q_step", 83),
			(set_background_mesh, "mesh_pic_xex14"),
			(str_store_string, 11, "str_mq_1_83"),
		(else_try),
			(eq, "$main_q_step", 85),
			(set_background_mesh, "mesh_pic_xex14"),
			(str_store_string, 11, "str_mq_1_85"),
		(else_try),
			(eq, "$main_q_step", 86),
			(set_background_mesh, "mesh_pic_xex14"),
			(str_store_string, 11, "str_mq_1_86"),
		(else_try),
			(eq, "$main_q_step", 87),
			(set_background_mesh, "mesh_pic_messenger"),
			(str_store_string, 11, "str_mq_1_87"),
		(else_try),
			(eq, "$main_q_step", 88),
			(set_background_mesh, "mesh_pic_rhodock"),
			(str_store_string, 11, "str_mq_1_88"),
		(else_try),
			(eq, "$main_q_step", 89),
			(set_background_mesh, "mesh_pic_siege_attack"),
			(str_store_string, 11, "str_mq_1_89"),
		(else_try),
			(eq, "$main_q_step", 90),
			(set_background_mesh, "mesh_pic_victory"),
			(str_store_string, 11, "str_mq_1_90"),
		(else_try),
			(eq, "$main_q_step", 91),
			(set_background_mesh, "mesh_pic_wounded_fem"),
			(str_store_string, 11, "str_mq_1_91"),
		(else_try),
			(eq, "$main_q_step", 92),
			(set_background_mesh, "mesh_st_pic_desert"),
			(str_store_string, 11, "str_mq_1_92"),
		(else_try),
			(eq, "$main_q_step", 93),
			(set_background_mesh, "mesh_pic_messenger"),
			(str_store_string, 11, "str_mq_1_93"),
		(else_try),
			(eq, "$main_q_step", 94),
			(set_background_mesh, "mesh_pic_xex14"),
			(str_store_string, 11, "str_mq_1_94"),
		(else_try),
			(eq, "$main_q_step", 96),
			(set_background_mesh, "mesh_pic_gameover"),
			(str_store_string, 11, "str_mq_1_96"),
		(else_try),
			(eq, "$main_q_step", 97),
			#Begin animated menu
			#(set_background_mesh, "mesh_main_menu_static"),
			#(set_background_mesh, "mesh_main_menu_move_1"),
			#End animated menu
			(set_background_mesh, "mesh_main_menu_background"), #old background menu
			(str_store_string, 11, "str_empty_string"),
		(else_try),
			(eq, "$g_encountered_party", "p_ruin_dummy_3"),
			(set_background_mesh, "mesh_pic_xex14"),
			(str_store_string, 11, "str_empty_string"),
		(else_try),
			(eq, "$g_encountered_party", "p_ruin_dummy_4"),
			(set_background_mesh, "mesh_1pic_ruin_107"),
			(str_store_string, 11, "str_empty_string"),
		(else_try),
			(str_store_string, 11, "str_empty_string"),
		(try_end)
	],
	[
		("main_q_execute",
		[
			(try_begin),
				(lt, "$main_q_step", 1),
				(str_store_string, 13, "str_mq_1_1m"),
				

				
			(else_try),
				(eq, "$main_q_step", 3),
				(str_store_faction_name, 10, "$main_q_faction"),
				(str_store_string, 13, "str_mq_1_3m"),
			(else_try),
				(eq, "$main_q_step", 7),
				(str_store_string, 13, "str_mq_1_7m"),
			(else_try),
				(eq, "$main_q_step", 8),
				(str_store_party_name, 10, "$main_q_party"),
				(str_store_string, 13, "str_mq_1_8m"),
			(else_try),
				(eq, "$main_q_step", 10),
				(str_store_party_name, 10, "$main_q_party"),
				(str_store_string, 13, "str_mq_1_10m"),
			(else_try),
				(eq, "$main_q_step", 14),
				(str_store_string, 13, "str_mq_1_14m"),
			(else_try),
				(eq, "$main_q_step", 16),
				(str_store_string, 13, "str_mq_1_16m"),
			(else_try),
				(eq, "$main_q_step", 18),
				(str_store_string, 13, "str_mq_1_18m"),
			(else_try),
				(eq, "$main_q_step", 19),
				(str_store_troop_name, 14, "$first_comp_id"),
				(str_store_party_name, 10, "$main_q_party"),
				(str_store_string, 13, "str_mq_1_19m"),
			(else_try),
				(eq, "$main_q_step", 21),
				(str_store_string, 13, "str_mq_1_21m"),
			(else_try),
				(this_or_next|eq, "$main_q_step", 23),
				(eq, "$main_q_step", 24),
				(str_store_string, 13, "str_mq_1_23m"),
			(else_try),
				(eq, "$main_q_step", 25),
				(str_store_string, 13, "str_mq_1_25m"),
			(else_try),
				(eq, "$main_q_step", 26),
				(str_store_string, 13, "str_mq_1_26m"),
			(else_try),
				(eq, "$main_q_step", 27),
				(str_store_string, 13, "str_mq_1_27m"),
			(else_try),
				(eq, "$main_q_step", 28),
				(str_store_string, 13, "str_mq_1_28m"),
			(else_try),
				(eq, "$main_q_step", 31),
				(str_store_string, 13, "str_mq_1_31m"),
			(else_try),
				(eq, "$main_q_step", 32),
				(str_store_troop_name, 14, "$main_q_troop"),
				(str_store_string, 13, "str_mq_1_32m"),
			(else_try),
				(eq, "$main_q_step", 33),
				(str_store_string, 13, "str_mq_1_33m"),
			(else_try),
				(this_or_next|eq, "$main_q_step", 35),
				(eq, "$main_q_step", 36),
				(str_store_string, 13, "str_continue_1"),
			(else_try),
				(eq, "$main_q_step", 37),
				(str_store_string, 13, "str_mq_1_37m"),
			(else_try),
				(eq, "$main_q_step", 38),
				(str_store_string, 13, "str_mq_1_33m"),
			(else_try),
				(this_or_next|eq, "$main_q_step", 40),
				(eq, "$main_q_step", 41),
				(str_store_string, 13, "str_continue_1"),
			(else_try),
				(eq, "$main_q_step", 42),
				(str_store_string, 13, "str_mq_1_42m"),
			(else_try),
				(eq, "$main_q_step", 43),
				(str_store_string, 13, "str_mq_1_43m"),
			(else_try),
				(eq, "$main_q_step", 45),
				(str_store_string, 13, "str_continue_1"),
			(else_try),
				(eq, "$main_q_step", 46),
				(str_store_string, 13, "str_mq_1_46m"),
			(else_try),
				(eq, "$main_q_step", 47),
				(str_store_string, 13, "str_mq_1_47m"),
			(else_try),
				(eq, "$main_q_step", 48),
				(str_store_troop_name, 14, "$main_q_troop"),
				(str_store_string, 13, "str_mq_1_48m"),
			(else_try),
				(eq, "$main_q_step", 49),
				(str_store_string, 13, "str_mq_1_42m"),
			(else_try),
				(eq, "$main_q_step", 50),
				(str_store_string, 13, "str_mq_1_50m"),
			(else_try),
				(eq, "$g_encountered_party", "p_ruin_dummy_3"),
				(ge, "$main_q_step", 51),
				(lt, "$main_q_step", 73),
				(str_store_string, 13, "str_mq_1_50m"),
			(else_try),
				(eq, "$main_q_step", 51),
				(str_store_string, 13, "str_mq_1_51m"),
			(else_try),
				(eq, "$main_q_step", 54),
				(str_store_string, 13, "str_mq_1_54m"),
			(else_try),
				(eq, "$main_q_step", 55),
				(str_store_string, 13, "str_mq_1_55m"),
			(else_try),
				(eq, "$main_q_step", 56),
				(str_store_string, 13, "str_continue_1"),
			(else_try),
				(eq, "$main_q_step", 57),
				(str_store_party_name, 10, "$main_q_party"),
				(str_store_string, 13, "str_mq_1_57m"),
			(else_try),
				(eq, "$main_q_step", 58),
				(str_store_string, 13, "str_mq_1_58m"),
			(else_try),
				(eq, "$main_q_step", 59),
				(str_store_string, 13, "str_mq_1_59m"),
			(else_try),
				(eq, "$main_q_step", 60),
				(str_store_string, 13, "str_mq_1_60m"),
			(else_try),
				(eq, "$main_q_step", 61),
				(str_store_string, 13, "str_mq_1_61m"),
			(else_try),
				(eq, "$main_q_step", 64),
				(str_store_string, 13, "str_mq_1_64m"),
			(else_try),
				(eq, "$main_q_step", 65),
				(str_store_string, 13, "str_mq_1_65m"),
			(else_try),
				(eq, "$main_q_step", 66),
				(str_store_string, 13, "str_mq_1_66m"),
			(else_try),
				(eq, "$main_q_step", 69),
				(str_store_string, 13, "str_mq_1_69m"),
			(else_try),
				(eq, "$main_q_step", 70),
				(str_store_string, 13, "str_mq_1_70m"),
			(else_try),
				(eq, "$main_q_step", 71),
				(str_store_string, 13, "str_continue_1"),
			(else_try),
				(eq, "$main_q_step", 72),
				(str_store_string, 13, "str_mq_1_72m"),
			(else_try),
				(eq, "$main_q_step", 73),
				(str_store_string, 13, "str_mq_1_73m"),
			(else_try),
				(eq, "$main_q_step", 74),
				(str_store_string, 13, "str_mq_1_74m"),
			(else_try),
				(eq, "$main_q_step", 76),
				(str_store_string, 13, "str_mq_1_76m"),
			(else_try),
				(eq, "$main_q_step", 79),
				(str_store_string, 13, "str_mq_1_79m"),
			(else_try),
				(eq, "$main_q_step", 80),
				(str_store_string, 13, "str_mq_1_80m"),
			(else_try),
				(eq, "$main_q_step", 81),
				(str_store_string, 13, "str_mq_1_81m"),
			(else_try),
				(eq, "$main_q_step", 83),
				(str_store_string, 13, "str_mq_1_83m"),
			(else_try),
				(eq, "$main_q_step", 85),
				(str_store_string, 13, "str_mq_1_85m"),
			(else_try),
				(eq, "$main_q_step", 86),
				(str_store_string, 13, "str_mq_1_83m"),
			(else_try),
				(eq, "$main_q_step", 87),
				(str_store_string, 13, "str_continue_1"),
			(else_try),
				(eq, "$main_q_step", 88),
				(str_store_string, 13, "str_mq_1_88m"),
			(else_try),
				(eq, "$main_q_step", 89),
				(str_store_string, 13, "str_mq_1_89m"),
			(else_try),
				(eq, "$main_q_step", 90),
				(str_store_string, 13, "str_continue_1"),
			(else_try),
				(eq, "$main_q_step", 91),
				(str_store_string, 13, "str_continue_1"),
			(else_try),
				(eq, "$main_q_step", 92),
				(str_store_string, 13, "str_continue_1"),
			(else_try),
				(eq, "$main_q_step", 93),
				(str_store_string, 13, "str_continue_1"),
			(else_try),
				(eq, "$main_q_step", 94),
				(str_store_string, 13, "str_mq_1_94m"),
			(else_try),
				(eq, "$main_q_step", 96),
				(play_track, "track_mount_and_blade_title_screen", 2),
				(str_store_string, 13, "str_continue_1"),
			(else_try),
				(eq, "$main_q_step", 97),
				(str_store_string, 13, "str_mq_1_97m"),
			(else_try),
				(str_store_string, 13, "str_back"),
			(try_end)
		],
		"{s13}",
		[
			(try_begin),
				(lt, "$main_q_step", 1),
				(assign, "$main_q_step", 1),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 3),
				(assign, "$main_q_step", 4),
				(assign, "$main_q_troop", 5),
				(assign, "$main_q_party", 0),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 7),
				(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
				(lt, ":party_size_wo_prisoners_main_party", 2000),
				(display_message, "str_mq_1_7n"),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 7),
				(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
				(ge, ":party_size_wo_prisoners_main_party", 2000),
				(try_begin),
					(assign, "$player_assistant_1", 0),
					(assign, "$enemy_assistant_1", 0),
					(assign, "$enemy_assistant_2", 0),
					(assign, "$wm_talk_state", 0),
					(assign, ":value", "scn_rebel_wooden_fort"),
					(modify_visitors_at_site, ":value"),
					(reset_visitors),
					(call_script, "script_wm_troop_type_depend_train", "$g_encountered_party", 50),
					(store_random_in_range, ":random_in_range_2_5", 2, 5),
					(assign, ":value_2", ":random_in_range_2_5"),
					(set_visitors, 2, "$temp_party_troop_03", ":value_2"),
					(set_visitors, 3, "$temp_party_troop_02", ":value_2"),
					(set_visitors, 4, "$temp_party_troop_03", ":value_2"),
					(set_visitors, 5, "$temp_party_troop_04", ":value_2"),
					(set_visitors, 6, "$temp_party_troop_03", ":value_2"),
					(set_visitors, 7, "$temp_party_troop_05", ":value_2"),
					(set_visitors, 8, "$temp_party_troop_04", ":value_2"),
					(set_visitors, 9, "$temp_party_troop_02", ":value_2"),
					(set_visitors, 10, "$temp_party_troop_06", ":value_2"),
					(set_visitor, 11, "trp_ex_npc_054", 1),
					(set_visitor, 1, "trp_player"),
					(set_jump_mission, "mt_raid_rebel_fort"),
					(assign, "$current_mission_template", "mt_raid_rebel_fort"),
					(jump_to_scene, ":value"),
					(change_screen_mission),
				(try_end),
			(else_try),
				(eq, "$main_q_step", 8),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 10),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 14),
				(eq, "$g_encountered_party", "p_ruin_dummy_4"),
				(assign, "$main_q_step", 15),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 16),
				(set_jump_mission, "mt_quest_brothel_mission"),
				(assign, "$current_mission_template", "mt_quest_brothel_mission"),
				(assign, ":value_3", "scn_brothel"),
				(modify_visitors_at_site, ":value_3"),
				(reset_visitors),
				(call_script, "script_wm_every_global_sett_depend_faction", "$main_q_party"),
				(assign, ":value_4", "trp_town_walker_2"),
				(try_begin),
					(set_visitor, 1, ":value_4"),
					(set_visitor, 11, "$wm_npc_light_guild_npc"),
				(try_end),
				(assign, ":value_4", "trp_town_walker_4"),
				(try_begin),
					(set_visitor, 2, ":value_4"),
					(set_visitor, 12, "$wm_npc_light_guild_npc"),
				(try_end),
				(assign, ":value_4", "$younger_sister_id"),
				(try_begin),
					(set_visitor, 3, ":value_4"),
					(set_visitor, 13, "$wm_npc_arena_master"),
				(try_end),
				(assign, ":value_4", "trp_town_walker_w_iber"),
				(try_begin),
					(set_visitor, 4, ":value_4"),
					(set_visitor, 14, "$wm_npc_arena_master"),
				(try_end),
				(assign, ":value_4", "trp_town_walker_w_inka"),
				(try_begin),
					(set_visitor, 5, ":value_4"),
					(set_visitor, 15, "$wm_npc_light_guild_npc"),
					(set_visitor, 23, "$wm_npc_walker_m"),
					(set_visitor, 24, "$wm_npc_walker_m"),
					(set_visitor, 25, "$wm_npc_walker_m"),
				(try_end),
				(assign, ":value_4", "trp_town_walker_w_rr"),
				(try_begin),
					(set_visitor, 6, ":value_4"),
					(set_visitor, 16, "$wm_npc_walker_m"),
					(set_visitor, 21, "$wm_npc_walker_m"),
				(try_end),
				(assign, ":value_4", "trp_town_walker_6"),
				(try_begin),
					(set_visitor, 7, ":value_4"),
					(set_visitor, 17, "$wm_npc_arena_master"),
				(try_end),
				(set_jump_entry, 0),
				(jump_to_scene, ":value_3"),
				(change_screen_mission),
			(else_try),
				(eq, "$main_q_step", 18),
				(assign, "$main_q_step", 19),
				(assign, "$main_q_day", 60),
				(party_set_flags, "p_ruin_dummy_5", 256, 1),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(rest_for_hours, 6, 5, 0),
			(else_try),
				(eq, "$main_q_step", 19),
				(assign, "$main_q_step", 20),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "$main_q_party"),
			(else_try),
				(eq, "$main_q_step", 21),
				(assign, "$main_q_step", 22),
				(assign, "$wm_talk_state", 4),
				(call_script, "script_molda_scene_culture", "$last_visit_town"),
				(assign, ":var_7", "$town_scene_type"),
				(modify_visitors_at_site, ":var_7"),
				(reset_visitors),
				(set_visitors, 10, "trp_raid_bandit_brigand", 2),
				(set_visitors, 9, "trp_raid_bandit_boss", 1),
				(set_visitor, 11, "$first_comp_id"),
				(set_jump_mission, "mt_town_center"),
				(assign, "$current_mission_template", "mt_town_center"),
				(assign, ":var_8", 256),
				(mission_tpl_entry_set_override_flags, "mt_town_center", 0, ":var_8"),
				(mission_tpl_entry_set_override_flags, "mt_town_center", 2, ":var_8"),
				(mission_tpl_entry_set_override_flags, "mt_town_center", 3, ":var_8"),
				(mission_tpl_entry_set_override_flags, "mt_town_center", 4, ":var_8"),
				(mission_tpl_entry_set_override_flags, "mt_town_center", 5, ":var_8"),
				(mission_tpl_entry_set_override_flags, "mt_town_center", 6, ":var_8"),
				(mission_tpl_entry_set_override_flags, "mt_town_center", 7, ":var_8"),
				(set_jump_entry, 1),
				(jump_to_scene, ":var_7"),
				(change_screen_mission),
			(else_try),
				(this_or_next|eq, "$main_q_step", 23),
				(eq, "$main_q_step", 24),
				(assign, "$main_q_step", 25),
				(assign, "$main_q_day", 45),
				(call_script, "script_wm_comp_in_party_slot", "$first_comp_id"),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 25),
				(assign, "$main_q_step", 26),
				(assign, "$main_q_day", 30),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 26),
				(call_script, "script_instance_battle_sett", "fac_outlaws", "trp_raid_bandit_boss", 0, 0, 60, 1),
			(else_try),
				(eq, "$main_q_step", 27),
				(assign, "$main_q_step", 28),
				(assign, "$main_q_day", 30),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 28),
				(assign, "$main_q_step", 29),
				(assign, "$main_q_party", 0),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 31),
				(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
				(lt, ":party_size_wo_prisoners_main_party", 3000),
				(display_message, "str_mq_1_7n"),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 31),
				(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
				(ge, ":party_size_wo_prisoners_main_party", 3000),
				(try_begin),
					(assign, "$player_assistant_1", 0),
					(assign, "$enemy_assistant_1", 0),
					(assign, "$enemy_assistant_2", 0),
					(assign, "$wm_talk_state", 0),
					(assign, ":value", "scn_rebel_wooden_fort"),
					(modify_visitors_at_site, ":value"),
					(reset_visitors),
					(call_script, "script_wm_troop_type_depend_train", "$g_encountered_party", 50),
					(store_random_in_range, ":random_in_range_2_5", 5, 9),
					(assign, ":value_2", ":random_in_range_2_5"),
					(set_visitors, 2, "$temp_party_troop_03", ":value_2"),
					(set_visitors, 3, "$temp_party_troop_02", ":value_2"),
					(set_visitors, 4, "$temp_party_troop_03", ":value_2"),
					(set_visitors, 5, "$temp_party_troop_04", ":value_2"),
					(set_visitors, 6, "$temp_party_troop_03", ":value_2"),
					(set_visitors, 7, "$temp_party_troop_05", ":value_2"),
					(set_visitors, 8, "$temp_party_troop_04", ":value_2"),
					(set_visitors, 9, "$temp_party_troop_02", ":value_2"),
					(set_visitors, 10, "$temp_party_troop_06", ":value_2"),
					(set_visitor, 11, "trp_ex_npc_054", 1),
					(set_visitor, 1, "trp_player"),
					(set_jump_mission, "mt_raid_rebel_fort"),
					(assign, "$current_mission_template", "mt_raid_rebel_fort"),
					(jump_to_scene, ":value"),
					(change_screen_mission),
				(try_end),
			(else_try),
				(eq, "$main_q_step", 32),
				(call_script, "script_setup_troop_meet_interior_add_vis", "trp_relative_of_merchant", "$main_q_troop", 0),
			(else_try),
				(eq, "$main_q_step", 33),
				(assign, "$main_q_step", 34),
				(assign, ":value_5", "scn_camp_assassination"),
				(modify_visitors_at_site, ":value_5"),
				(reset_visitors),
				(set_visitor, 0, "trp_player"),
				(try_begin),
					(set_visitor, 1, "trp_ww_a_5_2"),
					(set_visitor, 3, "trp_ww_a_5_2"),
				(try_end),
				(set_jump_mission, "mt_camp_assassination"),
				(assign, "$current_mission_template", "mt_camp_assassination"),
				(jump_to_scene, ":value_5"),
				(change_screen_mission),
			(else_try),
				(this_or_next|eq, "$main_q_step", 35),
				(eq, "$main_q_step", 36),
				(assign, "$main_q_step", 37),
				(assign, "$main_q_day", 15),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 37),
				(assign, "$molda_start_map_conversation", "trp_swadian_merchant"),
				(jump_to_menu, "mnu_molda_map_talk"),
			(else_try),
				(eq, "$main_q_step", 38),
				(assign, "$main_q_step", 39),
				(assign, ":value_5", "scn_camp_assassination"),
				(modify_visitors_at_site, ":value_5"),
				(reset_visitors),
				(set_visitor, 0, "trp_player"),
				(try_begin),
					(set_visitor, 1, "trp_ww_a_5_2"),
					(set_visitor, 3, "trp_ww_a_5_2"),
				(try_end),
				(set_jump_mission, "mt_camp_assassination"),
				(assign, "$current_mission_template", "mt_camp_assassination"),
				(jump_to_scene, ":value_5"),
				(change_screen_mission),
			(else_try),
				(this_or_next|eq, "$main_q_step", 40),
				(eq, "$main_q_step", 41),
				(assign, "$main_q_step", 42),
				(assign, "$main_q_day", 60),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 42),
				(assign, "$main_q_step", 43),
				(party_get_position, 11, "p_munich"),
				(map_get_land_position_around_position, 12, 11, 3),
				(assign, ":value_6", "p_ruin_dummy_3"),
				(party_set_position, ":value_6", 12),
				(party_set_icon, ":value_6", "icon_house_exn"),
				(party_set_flags, ":value_6", 256, 0),
				(party_set_flags, ":value_6", 524288, 0),
				(party_set_flags, ":value_6", 16384, 1),
				(party_set_name, ":value_6", "str_mq_noble_mansion"),
				(party_get_slot, ":munich_town_center", "p_munich", slot_town_center),
				(party_set_slot, ":value_6", slot_town_center, ":munich_town_center"),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_ruin_dummy_3"),
			(else_try),
				(eq, "$main_q_step", 43),
				(assign, "$main_q_step", 44),
				(call_script, "script_setup_troop_meet_interior_add_vis", "$younger_sister_id", "trp_vaegir_merchant", 0),
			(else_try),
				(eq, "$main_q_step", 45),
				(assign, "$main_q_step", 46),
				(party_get_position, 11, "p_main_party"),
				(map_get_land_position_around_position, 12, 11, 1),
				(assign, ":value_6", "p_ruin_dummy_5"),
				(party_set_position, ":value_6", 12),
				(party_set_icon, ":value_6", "icon_wm_town_euro_2"),
				(party_set_flags, ":value_6", 256, 0),
				(party_set_flags, ":value_6", 524288, 0),
				(party_set_flags, ":value_6", 16384, 1),
				(party_set_name, ":value_6", "str_mq_old_fort"),
				(party_get_slot, ":munich_town_center", "$last_visit_town", slot_town_center),
				(party_set_slot, ":value_6", slot_town_center, ":munich_town_center"),
				(troop_get_slot, ":player_23", "trp_player", 23),
				(assign, "$main_q_troop", "trp_tt_lady_ex_15"),
				(try_begin),
					(this_or_next|eq, ":player_23", 7),
					(this_or_next|eq, ":player_23", 6),
					(eq, ":player_23", 3),
					(assign, "$main_q_troop", "trp_tt_lady_ex_09"),
				(else_try),
					(this_or_next|eq, ":player_23", 15),
					(this_or_next|eq, ":player_23", 8),
					(this_or_next|eq, ":player_23", 5),
					(eq, ":player_23", 4),
					(assign, "$main_q_troop", "trp_tt_lady_ex_16"),
				(try_end),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 46),
				(assign, "$wm_talk_state", 0),
				(assign, ":value_5", "scn_fortress_ruins"),
				(modify_visitors_at_site, ":value_5"),
				(reset_visitors),
				(set_visitor, 0, "trp_player"),
				(set_visitor, 1, "trp_kidnapper_rape"),
				(set_visitor, 2, "trp_kidnapper_rape"),
				(set_visitor, 3, "trp_kidnapper_rape"),
				(set_visitor, 4, "trp_kidnapper_rape"),
				(set_visitor, 5, "trp_kidnapper_rape"),
				(set_visitor, 6, "trp_kidnapper_rape"),
				(set_visitor, 7, "trp_kidnapper_rape"),
				(set_visitor, 8, "trp_kidnapper_rape"),
				(set_visitor, 9, "trp_kidnapper_rape"),
				(set_visitor, 10, "trp_kidnapper_fight"),
				(set_visitor, 11, "trp_kidnapper_fight"),
				(set_visitor, 12, "trp_kidnapper_fight"),
				(set_visitor, 13, "trp_kidnapper_fight"),
				(set_visitor, 14, "trp_kidnapper_fight"),
				(set_visitor, 15, "trp_kidnapper_fight"),
				(set_visitor, 16, "trp_kidnapper_fight"),
				(set_visitor, 17, "trp_kidnapper_fight"),
				(set_visitor, 18, "trp_kidnapper_fight"),
				(set_visitor, 19, "trp_raid_bandit_boss"),
				(store_random_in_range, ":random_in_range_2_5", 20, 25),
				(set_visitor, ":random_in_range_2_5", "$main_q_troop"),
				(set_jump_mission, "mt_rescue_lady"),
				(assign, "$current_mission_template", "mt_rescue_lady"),
				(jump_to_scene, ":value_5"),
				(change_screen_mission),
			(else_try),
				(eq, "$main_q_step", 47),
				(call_script, "script_instance_battle_sett", "fac_outlaws", "trp_raid_bandit_boss", 0, 0, 60, 1),
			(else_try),
				(eq, "$main_q_step", 48),
				(call_script, "script_setup_troop_meet_interior", "$main_q_troop", -1),
			(else_try),
				(eq, "$main_q_step", 49),
				(assign, "$main_q_step", 50),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 50),
				(call_script, "script_setup_troop_meet_interior_add_vis", "$younger_sister_id", "trp_vaegir_merchant", 0),
			(else_try),
				(eq, "$g_encountered_party", "p_ruin_dummy_3"),
				(ge, "$main_q_step", 51),
				(lt, "$main_q_step", 73),
				(call_script, "script_setup_troop_meet_interior", "$younger_sister_id", -1),
			(else_try),
				(eq, "$main_q_step", 51),
				(assign, "$main_q_step", 52),
				(assign, "$main_q_party", 0),
				(display_message, "str_mq_1_52b"),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 54),
				(call_script, "script_setup_troop_meet_interior_add_vis", "trp_relative_of_merchant", "trp_tt_lord_22_00", 0),
			(else_try),
				(eq, "$main_q_step", 55),
				(assign, "$main_q_step", 56),
				(assign, "$main_q_day", 60),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 56),
				(assign, "$main_q_step", 57),
				(assign, "$main_q_day", 15),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 57),
				(assign, "$main_q_step", 58),
				(party_get_position, 11, "$main_q_party"),
				(map_get_land_position_around_position, 12, 11, 1),
				(assign, ":value_6", "p_ruin_dummy_5"),
				(party_set_position, ":value_6", 12),
				(party_set_icon, ":value_6", "icon_wm_town_barb_2"),
				(party_set_flags, ":value_6", 256, 0),
				(party_set_flags, ":value_6", 524288, 0),
				(party_set_flags, ":value_6", 16384, 1),
				(party_set_name, ":value_6", "str_mq_fort_rebel"),
				(party_get_slot, ":munich_town_center", "$last_visit_town", slot_town_center),
				(party_set_slot, ":value_6", slot_town_center, ":munich_town_center"),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 58),
				(assign, "$player_assistant_1", 0),
				(assign, "$enemy_assistant_1", 0),
				(assign, "$enemy_assistant_2", 0),
				(assign, ":var_13", "trp_rebels_fort_peasant"),
				(assign, ":var_14", "trp_rebels_fort_leader"),
				(assign, "$wm_talk_state", 0),
				(assign, ":value", "scn_rebel_wooden_fort"),
				(modify_visitors_at_site, ":value"),
				(reset_visitors),
				(call_script, "script_wm_troop_type_depend_train", "$g_encountered_party", 50),
				(store_random_in_range, ":random_in_range_2_5", 6, 9),
				(assign, ":value_2", ":random_in_range_2_5"),
				(set_visitors, 2, ":var_13", ":value_2"),
				(set_visitors, 3, "$temp_party_troop_02", ":value_2"),
				(set_visitors, 4, "$temp_party_troop_03", ":value_2"),
				(set_visitors, 5, "$temp_party_troop_01", ":value_2"),
				(set_visitors, 6, ":var_13", ":value_2"),
				(set_visitors, 7, "$temp_party_troop_03", ":value_2"),
				(set_visitors, 8, "$temp_party_troop_01", ":value_2"),
				(set_visitors, 9, "$temp_party_troop_02", ":value_2"),
				(set_visitors, 10, ":var_13", ":value_2"),
				(set_visitor, 11, ":var_14", 1),
				(set_visitor, 1, "trp_player"),
				(set_jump_mission, "mt_raid_rebel_fort"),
				(assign, "$current_mission_template", "mt_raid_rebel_fort"),
				(jump_to_scene, ":value"),
				(change_screen_mission),
			(else_try),
				(eq, "$main_q_step", 59),
				(party_set_flags, "p_ruin_dummy_5", 256, 1),
				(call_script, "script_setup_troop_meet_interior_add_vis", "trp_relative_of_merchant", "trp_rebels_fort_leader", 0),
			(else_try),
				(eq, "$main_q_step", 60),
				(call_script, "script_setup_troop_meet_interior_add_vis", "trp_relative_of_merchant", "trp_temporary_minister", 0),
			(else_try),
				(eq, "$main_q_step", 61),
				(assign, "$main_q_step", 62),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 64),
				(call_script, "script_instance_battle_siege", "fac_kingdom_13", "trp_temp_commander_fac_13", 0, 0, 7000, 0, 0, 22, "scn_battle_tile_siege_harbor", 3, 114),
			(else_try),
				(eq, "$main_q_step", 65),
				(assign, "$main_q_step", 66),
				(assign, "$main_q_day", 60),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 66),
				(assign, "$main_q_step", 67),
				(jump_to_menu, "mnu_wm_pst_map_return"),
				(assign, "$camera_focus_on", 1),
				(set_camera_follow_party, "p_tradeport71"),
			(else_try),
				(eq, "$main_q_step", 69),
				(call_script, "script_setup_troop_meet_interior_add_vis", "trp_relative_of_merchant", "trp_ww_a_5_2", "trp_swadian_merchant"),
			(else_try),
				(eq, "$main_q_step", 70),
				(call_script, "script_setup_troop_meet_interior_add_vis", "trp_relative_of_merchant", "trp_swadian_merchant", 0),
			(else_try),
				(eq, "$main_q_step", 71),
				(assign, "$main_q_step", 72),
				(assign, "$main_q_day", 30),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 72),
				(call_script, "script_setup_troop_meet_interior_add_vis", "trp_relative_of_merchant", "trp_khergit_merchant", 0),
			(else_try),
				(eq, "$main_q_step", 73),
				(set_jump_mission, "mt_quest_brothel_mission"),
				(assign, "$current_mission_template", "mt_quest_brothel_mission"),
				(assign, ":value_3", "scn_brothel"),
				(modify_visitors_at_site, ":value_3"),
				(reset_visitors),
				(call_script, "script_wm_every_global_sett_depend_faction", "p_munich"),
				(set_visitor, 11, "$wm_npc_light_guild_npc"),
				(assign, ":value_4", "$younger_sister_id"),
				(set_visitor, 3, ":value_4"),
				(set_visitor, 14, "$wm_npc_arena_master"),
				(set_visitor, 24, "$wm_npc_walker_m"),
				(set_visitor, 25, "$wm_npc_walker_m"),
				(set_visitor, 16, "$wm_npc_walker_m"),
				(set_visitor, 21, "$wm_npc_walker_m"),
				(assign, ":value_4", "trp_town_walker_6"),
				(set_visitor, 7, ":value_4"),
				(set_jump_entry, 0),
				(jump_to_scene, ":value_3"),
				(change_screen_mission),
			(else_try),
				(eq, "$main_q_step", 74),
				(assign, "$main_q_step", 75),
				(troop_add_item, "trp_player", 949, 0),
				(party_set_flags, "p_ruin_dummy_3", 256, 1),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 76),
				(assign, "$main_q_step", 77),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 79),
				(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
				(lt, ":party_size_wo_prisoners_main_party", 3000),
				(display_message, "str_mq_1_7n"),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 79),
				(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
				(ge, ":party_size_wo_prisoners_main_party", 3000),
				(call_script, "script_instance_battle_sett", "fac_kingdom_14", "trp_ex_npc_056", 0, 0, 6000, 0),
			(else_try),
				(eq, "$main_q_step", 80),
				(assign, "$main_q_step", 81),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 81),
				(assign, "$main_q_step", 82),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 83),
				(call_script, "script_setup_troop_meet_interior_add_vis", "trp_relative_of_merchant", "trp_ex_npc_057", 0),
			(else_try),
				(eq, "$main_q_step", 85),
				(party_set_flags, "p_ruin_dummy_2", 256, 1),
				(assign, "$main_q_step", 86),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 86),
				(call_script, "script_setup_troop_meet_interior_add_vis", "trp_relative_of_merchant", "trp_ex_npc_057", 0),
			(else_try),
				(eq, "$main_q_step", 87),
				(assign, "$main_q_step", 88),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 88),
				(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
				(lt, ":party_size_wo_prisoners_main_party", 3000),
				(display_message, "str_mq_1_7n"),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 88),
				(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
				(ge, ":party_size_wo_prisoners_main_party", 3000),
				(call_script, "script_instance_battle_sett", "fac_kingdom_14", "trp_ex_npc_056", 0, 0, 10000, 0),
			(else_try),
				(eq, "$main_q_step", 89),
				(call_script, "script_instance_battle_siege", "fac_kingdom_14", "trp_ex_npc_056", 0, 0, 3500, 0, 1, 2, "scn_battle_tile_siege_highland_d", 8, 105),
			(else_try),
				(eq, "$main_q_step", 90),
				(assign, "$main_q_step", 91),
				(jump_to_menu, "mnu_main_quest_menu"),
			(else_try),
				(eq, "$main_q_step", 91),
				(assign, "$main_q_step", 92),
				(jump_to_menu, "mnu_main_quest_menu"),
			(else_try),
				(eq, "$main_q_step", 92),
				(assign, "$main_q_step", 93),
				(assign, "$main_q_day", 90),
				(party_set_flags, "p_ruin_dummy_3", 256, 1),
				(party_set_flags, "p_ruin_dummy_4", 256, 1),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 93),
				(assign, "$main_q_step", 94),
				(party_get_position, 11, "p_antioch"),
				(map_get_land_position_around_position, 12, 11, 2),
				(assign, ":value_6", "p_ruin_dummy_5"),
				(party_set_position, ":value_6", 12),
				(party_set_icon, ":value_6", "icon_house_exn"),
				(party_set_flags, ":value_6", 256, 0),
				(party_set_flags, ":value_6", 524288, 0),
				(party_set_flags, ":value_6", 16384, 1),
				(party_set_name, ":value_6", "str_triangular_inn"),
				(party_get_slot, ":munich_town_center", "p_antioch", slot_town_center),
				(party_set_slot, ":value_6", slot_town_center, ":munich_town_center"),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(eq, "$main_q_step", 94),
				(assign, "$wm_talk_state", 0),
				(assign, ":var_15", "scn_8_tavern_roma_1"),
				(set_jump_mission, "mt_quest_inn"),
				(assign, "$current_mission_template", "mt_quest_inn"),
				(jump_to_scene, ":var_15"),
				(modify_visitors_at_site, ":var_15"),
				(reset_visitors),
				(try_begin),
					(set_visitor, 17, "trp_vaegir_merchant"),
					(set_visitors, 18, "trp_cru_5_m", 2),
				(try_end),
				(change_screen_mission),
			(else_try),
				(eq, "$main_q_step", 96),
				(party_set_flags, "p_ruin_dummy_5", 256, 1),
				(assign, "$main_q_step", 97),
				(jump_to_menu, "mnu_main_quest_menu"),
			(else_try),
				(eq, "$main_q_step", 97),
				(assign, "$main_q_step", 98),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(else_try),
				(jump_to_menu, "mnu_wm_pst_map_return"),
			(try_end)
		], "."),

		("return_wma",
		[
			(eq, "$g_encountered_party", "p_ruin_dummy_3"),
			(ge, "$main_q_step", 51),
			(le, "$main_q_step", 73)
		],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("return_wmb",
		[
			(this_or_next|eq, "$main_q_step", 79),
			(this_or_next|eq, "$main_q_step", 89),
			(eq, "$main_q_step", 88),
			(eq, "$g_encountered_party", "p_ruin_dummy_4")
		],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], "."),

		("return_wmc",
		[
			(this_or_next|eq, "$main_q_step", 94),
			(this_or_next|eq, "$main_q_step", 58),
			(this_or_next|eq, "$main_q_step", 47),
			(this_or_next|eq, "$main_q_step", 46),
			(this_or_next|eq, "$main_q_step", 31),
			(eq, "$main_q_step", 7),
			(eq, "$g_encountered_party", "p_ruin_dummy_5")
		],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("dummy_encount", 0, "      ",
"none",
	[
		(try_begin),
			(this_or_next|eq, "$main_q_step", 14),
			(this_or_next|eq, "$main_q_step", 16),
			(this_or_next|eq, "$main_q_step", 31),
			(this_or_next|eq, "$main_q_step", 43),
			(this_or_next|eq, "$main_q_step", 46),
			(this_or_next|eq, "$main_q_step", 47),
			(this_or_next|eq, "$main_q_step", 50),
			(this_or_next|eq, "$main_q_step", 58),
			(this_or_next|eq, "$main_q_step", 73),
			(this_or_next|eq, "$main_q_step", 79),
			(this_or_next|eq, "$main_q_step", 83),
			(this_or_next|eq, "$main_q_step", 85),
			(this_or_next|eq, "$main_q_step", 86),
			(this_or_next|eq, "$main_q_step", 88),
			(this_or_next|eq, "$main_q_step", 89),
			(this_or_next|eq, "$main_q_step", 94),
			(eq, "$main_q_step", 7),
			(jump_to_menu, "mnu_main_quest_menu"),
		(try_end)
	],
	[
		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	("menu_sample", 0, "text",
"none",
	[
		(set_background_mesh, "mesh_pic_camp")
	],
	[
		("menu_sample",
		[],
		"text",
		[
			(jump_to_menu, "mnu_menu_sample")
		], "."),

		("return_wm",
		[],
		"[Return to map]",
		[
			(jump_to_menu, "mnu_wm_pst_map_return")
		], ".")
	]
	),

	
	
	#Minor cheats
	
		("camp_cheat", 0, "Select a cheat:",
"none",
	[],
	[
		("camp_cheat_find_item",
		[],
		"Find an item...",
		[
			(jump_to_menu, "mnu_cheat_find_item")
		], "."),

		("camp_cheat_find_item",
		[],
		"Change weather..",
		[
			(jump_to_menu, "mnu_cheat_change_weather")
		], "."),

#		("camp_cheat_1",
#		[],
#		"{!}Increase player renown.",
#		[
#			(str_store_string, 1, "@Player renown is increased by 100. "),
#			#(call_script, "script_change_troop_renown", "trp_player", 100),
#			(jump_to_menu, "mnu_camp_cheat")
#		], "."),

#		("camp_cheat_2",
#		[],
#		"{!}Increase player honor.",
#		[
#			(assign, reg7, "$player_honor"),
#			(val_add, reg7, 1),
#			(display_message, "@Player honor is increased by 1 and it is now {reg7}."),
#			(val_add, "$player_honor", 1),
#			(jump_to_menu, "mnu_camp_cheat")
#		], "."),
		
				("camp_cheat_3",
		[],
		"{!}Increase player gold",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 1000, 87),
			(play_sound, "snd_money_received"),
			(jump_to_menu, "mnu_camp_cheat")
		], "."),
		
		
		("camp_cheat_4",
		[],
		"{!}Increase player contribution to faction",
		[
			(call_script, "script_troop_contribution_diff", "trp_player", 50, 87),
			(jump_to_menu, "mnu_camp_cheat")
		], "."),
		
		
						("camp_cheat_5",
		[],
		"{!}Increase player honor",
		[
			(call_script, "script_wm_honor_change_diff", "trp_player", 10, 87),
			(jump_to_menu, "mnu_camp_cheat")
		], "."),
		
								("camp_cheat_6",
		[],
		"{!}Increase player battle experience",
		[
			(call_script, "script_battle_exp_diff", 1000, 87),
			(jump_to_menu, "mnu_camp_cheat")
		], "."),
		
		
								("camp_cheat_7",
		[],
		"{!}Increase player adventure experience",
		[
			(call_script, "script_adv_exp_diff", 1000, 87),
			(jump_to_menu, "mnu_camp_cheat")
		], "."),
		
		
								("camp_cheat_8",
		[],
		"{!}Increase player policy experience",
		[
			(call_script, "script_int_exp_diff", 1000),
			(jump_to_menu, "mnu_camp_cheat")
		], "."),


		("back_to_camp_menu",
		[],
		"{!}Back to camp menu.",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),
	
	#Major cheats#
	
		("major_cheats", 0, "Select a cheat:",
"none",
	[],
	[
	
	
	
		("camp_cheat_m2",
		[],
		"Learn all battle strategies and some tactical traits to have more options during battles (this is a weaker combination of the two succeeding cheats below)",
		[
		#tactics: 6, leadership 3, strategy 6, naval 1, train 80, light/heavy/twohand/horsearmor 500.
					(troop_set_slot, "trp_player", 28, 6), #Tactics
					(troop_set_slot, "trp_player", 29, 3), #Leadership
					(troop_set_slot, "trp_player", 30, 6), #Strategy
					(troop_set_slot, "trp_player", 31, 1), #Naval
			(assign, "$bt_st_confuse", 1),
			(assign, "$bt_st_blocking_supply", 1),
			(assign, "$bt_st_lure", 1),
			(assign, "$bt_st_ambush", 1),
			(assign, "$bt_st_submerge", 1),
			(assign, "$bt_st_firework", 1),
			(assign, "$bt_st_fallrock", 1),
			(assign, "$bt_st_opengate", 1),
			(assign, "$bt_st_infiltration", 1),
			(assign, "$bt_st_sideatt", 1),
			(assign, "$bt_st_backatt", 1),
			(assign, "$bt_st_encamp", 1),
			(assign, "$bt_st_lionheart", 1),
			(assign, "$bt_st_pincer", 1),
			(assign, "$bt_st_mangudai", 1),
			(assign, "$bt_st_briver", 1),
			(assign, "$bt_st_8door", 1),
			(jump_to_menu, "mnu_major_cheats"),
		], "."),

		("camp_cheat_m1",
		[],
		"{!}Learn and max out all adventurer traits",
		[
					(troop_set_slot, "trp_player", 35, 7),
					(troop_set_slot, "trp_player", 36, 7),
					(troop_set_slot, "trp_player", 37, 7),
					(troop_set_slot, "trp_player", 38, 7),
					(troop_set_slot, "trp_player", 39, 7),
					(troop_set_slot, "trp_player", 40, 7),
					(troop_set_slot, "trp_player", 41, 7),
					(troop_set_slot, "trp_player", 28, 7),
					(troop_set_slot, "trp_player", 29, 7),
					(troop_set_slot, "trp_player", 30, 7),
					(troop_set_slot, "trp_player", 31, 7),
					(jump_to_menu, "mnu_major_cheats"),
		], "."),

#		("camp_cheatm_1",
#		[],
#		"{!}Increase player renown.",
#		[
#			(str_store_string, 1, "@Player renown is increased by 100. "),
#			#(call_script, "script_change_troop_renown", "trp_player", 100),
#			(jump_to_menu, "mnu_camp_cheat")
#		], "."),
		
				("camp_cheatm_3",
		[(neq, "$learned_battles", 1),],
		"{!}Learn all battle tactics and strategies",
		[
			(assign, "$bt_st_confuse", 1),
			(assign, "$bt_st_blocking_supply", 1),
			(assign, "$bt_st_lure", 1),
			(assign, "$bt_st_ambush", 1),
			(assign, "$bt_st_submerge", 1),
			(assign, "$bt_st_firework", 1),
			(assign, "$bt_st_fallrock", 1),
			(assign, "$bt_st_opengate", 1),
			(assign, "$bt_st_infiltration", 1),
			(assign, "$bt_st_sideatt", 1),
			(assign, "$bt_st_backatt", 1),
			(assign, "$bt_st_encamp", 1),
			(assign, "$bt_st_lionheart", 1),
			(assign, "$bt_st_pincer", 1),
			(assign, "$bt_st_mangudai", 1),
			(assign, "$bt_st_briver", 1),
			(assign, "$bt_st_8door", 1),
			(assign, "$learned_battles", 1),
			(jump_to_menu, "mnu_major_cheats"),
		], "."),
		
		
		("camp_cheatm_4",
		[(neq, "$learned_policy", 1),],
		"{!}Learn and max out all policy traits",
		[
			(assign, "$policy_tax_collect", 5),
			(assign, "$policy_supply_manage", 5),
			(assign, "$policy_trade_plan", 5),
			(assign, "$policy_frugal", 5),
			(assign, "$policy_ship_manage", 5),
			(assign, "$policy_lascivious", 5),
			(assign, "$policy_tracker", 5),
			(assign, "$learned_policy", 1),
			(jump_to_menu, "mnu_major_cheats"),
		], "."),
		
		
		#Blueprints

		
						("camp_cheatmb2",
		[(neq, "$bluepc_blackship", 1),],
		"{!}Acquire black ship blueprint.",
		[
			(assign, ":value", 1421),
			(troop_add_item, "trp_player", ":value", 0),
			(display_message, "str_bluep_black", 0x00ffff00),
			(assign, "$bluepc_blackship", 1),
			(jump_to_menu, "mnu_major_cheats"),
		], "."),
		
								("camp_cheatmb3",
		[(neq, "$bluepc_geobukseon", 1),],
		"{!}Acquire geobukseon blueprint.",
		[
			(assign, ":value", 1423),
			(troop_add_item, "trp_player", ":value", 0),
			(display_message, "str_bluep_frigate", 0x00ffff00),
			(assign, "$bluepc_geobukseon", 1),
			(jump_to_menu, "mnu_major_cheats"),
		], "."),
		
								("camp_cheatmb4",
		[(neq, "$bluepc_frigate", 1),],
		"{!}Acquire frigate blueprint.",
		[
			(assign, ":value", 1424),
			(troop_add_item, "trp_player", ":value", 0),
			(display_message, "str_bluep_turtle", 0x00ffff00),
			(assign, "$bluepc_frigate", 1),
			(jump_to_menu, "mnu_major_cheats"),
		], "."),
		
		
						("camp_cheatmb1",
		[(neq, "$bluepc_ghostship", 1),],
		"{!}Acquire ghost ship blueprint.",
		[
			(assign, ":value", 1422),
			(troop_add_item, "trp_player", ":value", 0),
			(display_message, "@You have acquired the Ghost Ship blueprint, this might be buggy so use at your own risk.", 0x00ffff00),
			(assign, "$bluepc_ghostship", 1),
			(jump_to_menu, "mnu_major_cheats"),
		], "."),
		
		#Blueprints
		
		
		
				("camp_cheatm_2",
		[],
		"{!}Increase player gold.",
		[
			(call_script, "script_party_money_level_diff", "p_main_party", 50000, 87),
			(play_sound, "snd_money_received"),
			(jump_to_menu, "mnu_major_cheats"),
		], "."),
		
		
		("back_to_camp_menu",
		[],
		"{!}Back to camp menu.",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
		
		
		
	]
	),

	("cheat_find_item", 0, "{!}Current item range: {reg5} to {reg6}",
"none",
	[
		(assign, reg5, "$cheat_find_item_range_begin"),
		(store_add, reg6, "$cheat_find_item_range_begin", 96),
		(val_min, reg6, "itm_rom_handl"),
		(val_sub, reg6, 1)
	],
	[
		("cheat_find_item_next_range",
		[],
		"{!}Move to next item range.",
		[
			(val_add, "$cheat_find_item_range_begin", 96),
			(try_begin),
				(ge, "$cheat_find_item_range_begin", "itm_rom_handl"),
				(assign, "$cheat_find_item_range_begin", 0),
			(try_end),
			(jump_to_menu, "mnu_cheat_find_item")
		], "."),

		("cheat_find_item_choose_this",
		[],
		"{!}Choose from this range.",
		[
			(troop_clear_inventory, "trp_find_item_cheat"),
			(store_add, ":value", "$cheat_find_item_range_begin", 96),
			(val_min, ":value", "itm_rom_handl"),
			(store_sub, ":value_2", ":value", "$cheat_find_item_range_begin"),
			(try_for_range, ":localvariable", 0, ":value_2"),
				(store_add, ":value_3", "$cheat_find_item_range_begin", ":localvariable"),
				(troop_add_items, "trp_find_item_cheat", ":value_3", 1),
			(try_end),
			(change_screen_trade, "trp_find_item_cheat")
		], "."),

		("camp_action_4",
		[],
		"{!}Back to camp menu.",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),

	("cheat_change_weather", 0, "{!}Current cloud amount: {reg5}^Current Fog Strength: {reg6}",
"none",
	[
		(get_global_cloud_amount, reg5),
		(get_global_haze_amount, reg6)
	],
	[
		("cheat_increase_cloud",
		[],
		"{!}Increase Cloud Amount.",
		[
			(get_global_cloud_amount, ":global_cloud_amount"),
			(val_add, ":global_cloud_amount", 5),
			(val_min, ":global_cloud_amount", 100),
			(set_global_cloud_amount, ":global_cloud_amount")
		], "."),

		("cheat_decrease_cloud",
		[],
		"{!}Decrease Cloud Amount.",
		[
			(get_global_cloud_amount, ":global_cloud_amount"),
			(val_sub, ":global_cloud_amount", 5),
			(val_max, ":global_cloud_amount", 0),
			(set_global_cloud_amount, ":global_cloud_amount")
		], "."),

		("cheat_increase_fog",
		[],
		"{!}Increase Fog Amount.",
		[
			(get_global_haze_amount, ":global_haze_amount"),
			(val_add, ":global_haze_amount", 5),
			(val_min, ":global_haze_amount", 100),
			(set_global_haze_amount, ":global_haze_amount")
		], "."),

		("cheat_decrease_fog",
		[],
		"{!}Decrease Fog Amount.",
		[
			(get_global_haze_amount, ":global_haze_amount"),
			(val_sub, ":global_haze_amount", 5),
			(val_max, ":global_haze_amount", 0),
			(set_global_haze_amount, ":global_haze_amount")
		], "."),

		("camp_action_4",
		[],
		"{!}Back to camp menu.",
		[
			(jump_to_menu, "mnu_camp")
		], ".")
	]
	),
	#Minor cheats
	
	#Major or minor cheats picker
	
		("cheats_picker", 0, "To access a cheat menu left click it. ^Powerful cheats are unbalanced, while minor cheats are customizable.^ Once you click a cheat there is no going back unless you load a previous game, however do not be discouraged. ^Feel free to experiment with the available cheats, they were made for you after all.",
"none",
	[
	],
	[
		("pick_major_cheats",
		[],
		"{!}Access the powerful cheats.",
		[
		(jump_to_menu, "mnu_major_cheats")
		], "."),

		("pick_minor_cheats",
		[],
		"{!}Access the minor cheats.",
		[
		(jump_to_menu, "mnu_camp_cheat")
		], "."),

		("go_back_cheats",
		[],
		"{!}Back to camp menu.",
		[
		(jump_to_menu, "mnu_camp")
		], ".")
	]
	),
	#Minor cheats
	
	
	## Envfix BEGIN EVENTS CODE, REMOVE IF ISSUE OCCURS, INTRODUCED V0.996B
#######################################################################

  #Random Events chief Sot
    (
    "event_01",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "A wandering ashik composed a song about your noble deeds.",
    "none",
    [
	
	],
    [
      ("choice_01_1",[],"Excellent!",
       [
		  #(call_script, "script_change_troop_renown", "trp_player", 5),
          (change_screen_return),
        ]
       ),
      ("choice_01_2",[],"Reward him with 200 denars. Let his song be played across the land.",
       [
	   ##(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		##(ge, ":gold", 200),
		##(call_script, "script_change_troop_renown", "trp_player", 20),
		##(troop_remove_gold, "trp_player", 200),
		(play_sound, "snd_hire_units"),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		##(call_script, "script_change_troop_renown", "trp_player", -5),
		(try_end),
		(change_screen_return),
        ]
       ),
      ("choice_01_3",[],"Noble deeds? A song? Bring me this fool's head!",
       [
	   #(call_script, "script_change_player_honor", -10),
	   (change_screen_return),
        ]
       ),
      ]
  ),
  

  (
    "event_02",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Tales of your honor spread throughout the country. Everywhere you go, your procession is surrounded by beggars.",
    "none",
    [
	
	],
    [
      ("choice_02_1",[],"Allocate 200 denars for an alms fund.",
       [
         # #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		##(ge, ":gold", 200),
		##(call_script, "script_change_player_honor", 5),
		##(call_script, "script_change_troop_renown", "trp_player", 10),
		##(troop_remove_gold, "trp_player", 200),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		##(call_script, "script_change_troop_renown", "trp_player", -5),
		(try_end),
		(change_screen_return),
        ]
       ),
      ("choice_02_2",[],"Ignore them.",
       [
	   #(call_script, "script_change_troop_renown", "trp_player", -5),
	   #(call_script, "script_change_player_honor", -5),
		(change_screen_return),
        ]
       ),
      ("choice_02_3",[],"Beggars huh? Release the hounds!",
       [
	   #(call_script, "script_change_player_honor", -15),
	   (change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_03",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "A young noble spreads rumors about your mother. Accusations of working in the world's oldest profession are the most delicate ones.",
    "none",
    [
	
	],
    [
      ("choice_03_1",[],"I challenge him to a duel!",
       [
	   #(call_script, "script_change_player_honor", 5),
		(display_message, "@The young noble preferred to flee rather than duel with you!"),
	   (change_screen_return),
        ]
       ),
      ("choice_03_2",[],"It's none of my business.",
       [
	   #(call_script, "script_change_player_honor", -25),
		(change_screen_return),
        ]
       ),
       ("choice_03_3",[],"Make sure he has an accidental encounter with a loose, falling brick.",
       [
		#(call_script, "script_change_troop_renown", "trp_player", -15),
	   #(call_script, "script_change_player_honor", -5),
	   (change_screen_return),
        ]
       ),
      ]
  ),


  (
    "event_04",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You encounter one of the wives of your soldiers. She begs you to release her husband from his contract. The harvest was poor this year and his wages can't feed the whole family. If he could come back and work on the field they might survive.",
    "none",
    [
	
	],
    [
      ("choice_04_1",[],"This can't be! Here take 200 denars.",
       [
		          ##(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		##(ge, ":gold", 200),
		##(call_script, "script_change_player_honor", 5),
		##(troop_remove_gold, "trp_player", 200),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		##(call_script, "script_change_troop_renown", "trp_player", -15),
		(try_end),
          (change_screen_return),
        ]
       ),
      ("choice_04_2",[],"Pacta sunt servanda!",
       [
		(change_screen_return),
        ]
       ),
      ("choice_04_3",[],"Why starve when my army could use the services of such a pretty young girl?",
       [
	   #(call_script, "script_change_player_honor", -15),
	   (change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_05",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "A local naysayer is spreading false rumors about you. While most of the stories are just pure nonsense, sooner or later people will believe those stories.",
    "none",
    [
	
	],
    [
      ("choice_05_1",[],"Let him speak what he wants. Every man has his rights.",
       [
		          ##(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		##(ge, ":gold", 100),
		#(call_script, "script_change_player_honor", -3),
		#(call_script, "script_change_troop_renown", "trp_player", -5),
          (change_screen_return),
        ]
       ),
      ("choice_05_2",[],"Tell the royal scribe to spread opposite rumors to counter his lies. (300 denars).",
       [
	    #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 300),
		#(call_script, "script_change_player_honor", 2),
		#(call_script, "script_change_troop_renown", "trp_player", 5),
		#(troop_remove_gold, "trp_player", 300),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -7),
		(try_end),
		(change_screen_return),
        ]
       ),
      ("choice_05_3",[],"Ask him to stop. 100 denars might help him forget what he's said.",
       [
	    #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 100),
		#(troop_remove_gold, "trp_player", 100),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_player_honor", -3),
		#(call_script, "script_change_troop_renown", "trp_player", -7),
		(try_end),
	   (change_screen_return),
        ]
       ),
	   ("choice_05_4",[],"Throw him into the dungeon. Insulting me is a crime.",
       [
	   #(call_script, "script_change_player_honor", -15),
	   (change_screen_return),
        ]
       ),
	   ("choice_05_5",[],"Silence him permanently and seize his properties.",
       [
	   #(call_script, "script_change_player_honor", -60),
	   #(troop_add_gold, "trp_player", 1000),
	   (change_screen_return),
        ]
       ),
      ]
  ),


   (
    "event_06",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "A mob of angry {s1} dwellers are complaining about corrupt tax collectors. They demand justice. The situation is getting worse by the minute. It looks like a riot will ensue unless you do something.",
    "none",
    [
	(assign, ":stop", 0),
	(try_for_range, ":unused", 0, 9999),
	(eq, ":stop", 0),
	(store_random_party_in_range, "$temp", "p_pyongyang", "p_place_end"),
	(neg|party_slot_eq, "$temp", slot_party_type, 2),
	(party_slot_eq, "$temp", slot_town_lord, "trp_player"),
	(assign, ":stop", 1),
	(str_store_party_name, s1, "$temp"),
	(try_end),
	],
    [
      ("choice_06_1",[],"Begin an investigation and compensate the peasants for their loss.",
       [
	 #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 300),
		#(party_get_slot, ":cur_relation", "$temp", slot_center_player_relation),
		#(val_add, ":cur_relation", 2),
		#(party_set_slot, "$temp", slot_center_player_relation, ":cur_relation"),
		#(troop_remove_gold, "trp_player", 300),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -5),
		#(party_get_slot, ":cur_relation", "$temp", slot_center_player_relation),
		#(val_sub, ":cur_relation", 5),
		#(party_set_slot, "$temp", slot_center_player_relation, ":cur_relation"),
		(try_end),
          (change_screen_return),
        ]
       ),
      ("choice_06_2",[],"Rush the town guards to control the mob from spreading and turning into a riot.",
       [
		#(party_get_slot, ":cur_relation", "$temp", slot_center_player_relation),
		#(val_sub, ":cur_relation", 5),
		#(party_set_slot, "$temp", slot_center_player_relation, ":cur_relation"),
		(change_screen_return),
        ]
       ),
      ("choice_06_3",[],"Put the peasants back in their place and collect their overdue taxes.",
       [
	   #(call_script, "script_change_player_honor", -5),
	   #(party_get_slot, ":cur_relation", "$temp", slot_center_player_relation),
		#(val_sub, ":cur_relation", 10),
		#(party_set_slot, "$temp", slot_center_player_relation, ":cur_relation"),
		#(troop_add_gold, "trp_player", 100),
	   (change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_07",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "A single rider, looking poor and unarmed, approaches your party. Intercepted by your men he presents himself as a troubadour from {s1} and requests your permission to compose an ode about your magnificence and generosity. Your men exchange glances and then look at you waiting for an answer. You...",
    "none",
    [
	(assign, ":stop", 0),
	(try_for_range, ":unused", 0, 9999),
	(eq, ":stop", 0),
	(store_random_party_in_range, "$temp", "p_pyongyang", "p_place_end"),
	(neg|party_slot_eq, "$temp", slot_party_type, 2),
	(party_slot_eq, "$temp", slot_town_lord, "trp_player"),
	(assign, ":stop", 1),
	(str_store_party_name, s1, "$temp"),
	(try_end),
	],
    [
      ("choice_07_1",[],"Grant such permission to the troubadour and cover the man with gold -300 denars-.",
       [
		#(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 300),
		#(store_random_in_range, ":rand_no", 3, 10),
		#(call_script, "script_change_troop_renown", "trp_player", ":rand_no"),
		#(party_get_slot, ":cur_relation", "$temp", slot_center_player_relation),
		#(val_add, ":cur_relation", 5),
		#(party_set_slot, "$temp", slot_center_player_relation, ":cur_relation"),
		#(troop_remove_gold, "trp_player", 300),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -2),
		(try_end),
          (change_screen_return),
        ]
       ),
      ("choice_07_2",[],"Grant permission and hand a purse with 100 denars to the man.",
       [
		#(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 100),
		#(party_get_slot, ":cur_relation", "$temp", slot_center_player_relation),
		#(val_add, ":cur_relation", 2),
		#(party_set_slot, "$temp", slot_center_player_relation, ":cur_relation"),
		#(troop_remove_gold, "trp_player", 100),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -2),
		(try_end),
		(change_screen_return),
        ]
       ),
      ("choice_07_3",[],"Allow the troubadour to compose the ode but offer him no payment.",
       [
		#(store_random_in_range, ":rand_no", -2, 2),
		#(party_get_slot, ":cur_relation", "$temp", slot_center_player_relation),
		#(val_add, ":cur_relation", ":rand_no"),
		#(party_set_slot, "$temp", slot_center_player_relation, ":cur_relation"),
	   (change_screen_return),
        ]
       ),
	   ("choice_07_4",[],"Order your men to take the beggar out of your way.",
       [
	   #(call_script, "script_change_player_honor", -2),
	   (change_screen_return),
        ]
       ),
      ]
  ),

(
    "event_08",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You spot a single man riding hard towards your party. With a gesture of your hand, your men run to meet him. Intercepted by your men he presents himself as an emissary from {s1} and without delay informs you that an influential man has died {s2} and that his family requests that you agree to declare an official day of mourning in {s1} in his honor. You...",
    "none",
    [
	(assign, ":stop", 0),
	(try_for_range, ":unused", 0, 9999),
	(eq, ":stop", 0),
	(store_random_party_in_range, "$temp", "p_pyongyang", "p_place_end"),
	(neg|party_slot_eq, "$temp", slot_party_type, 2),
#	(party_slot_eq, "$temp", slot_town_lord, "trp_player"),
	(assign, ":stop", 1),
	(str_store_party_name, s1, "$temp"),
	(try_end),
	(store_random_in_range, ":rand_no", 1, 10),
		(try_begin),
		(ge, ":rand_no", 8),
		(str_store_string , s2, "@of a fulminating disease"),
		(else_try),
		(ge, ":rand_no", 5),
		(str_store_string , s2, "@in a hunting accident"),
		(else_try),
		(ge, ":rand_no", 3),
		(str_store_string , s2, "@assassinated"),
		(else_try),
		(ge, ":rand_no", 0),
		(str_store_string , s2, "@of an indigestion"),
		(try_end),
	],
    [
      ("choice_08_1",[],"Agree to such request.",
       [
		#(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 100),
		#(party_get_slot, ":cur_relation", "$temp", slot_center_player_relation),
		#(val_add, ":cur_relation", 2),
		#(party_set_slot, "$temp", slot_center_player_relation, ":cur_relation"),
		#(troop_remove_gold, "trp_player", 100),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -1),
		(try_end),
          (change_screen_return),
        ]
       ),
      ("choice_08_2",[],"Refuse to such request.",
       [
		#(party_get_slot, ":cur_relation", "$temp", slot_center_player_relation),
		#(val_add, ":cur_relation", -2),
		#(party_set_slot, "$temp", slot_center_player_relation, ":cur_relation"),
		(change_screen_return),
        ]
       ),
      ]
  ),
#fine   
    (
    "event_09",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You are traveling and suddenly spot a wild hare, trapped in the snare. What do you do?",
    "none",
    [
	
	],
    [
      ("choice_09_1",[],"Free the animal.",
       [
		  
                  (change_screen_return),
        ]
       ),
      ("choice_09_2",[],"Clench snare and kill the animal!",
       [
            #(troop_add_item, "trp_player","itm_dried_meat",0),
	    (change_screen_return),
        ]
       ),
      ("choice_09_3",[],"Pass by the animal and ignore it.",
       [ 
	   (change_screen_return),
        ]
       ),
      ]
  ),

      (
    "event_10",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You are traveling and spot a peasant tied up to a tree, perhaps by bandits. What do you do?",
    "none",
    [
	
	],
    [
      ("choice_10_1",[],"Free the peasant.",
       [
		  #(call_script, "script_change_player_honor", 1),
                  ##(party_add_members, "p_main_party", "trp_italian_town_recruit", 1),
                  (change_screen_return),
        ]
       ),
      ("choice_10_2",[],"Pass by the peasant.",
       [
	    (change_screen_return),
        ]
       ),
      ("choice_10_3",[],"Kill the peasant",
       [
	   #(call_script, "script_change_player_honor", -1), 
	   (change_screen_return),
        ]
       ),
      ]
  ),


#tropas que se unen
        (
    "event_101",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You are a famous leader, and you received news that a group of young nobles wishes to join you. But They want more pay than the rest of your troops for their high class.",
    "none",
    [
	
	],
    [
      ("choice_101_1",[],"They are welcome.",
       [
                  #(party_add_members, "p_main_party", "trp_balt_billman", 5),
                  (change_screen_return),
        ]
       ),
      ("choice_101_2",[],"I do not need more troops.",
       [
	    (change_screen_return),
        ]
       ),
      ("choice_101_3",[],"Kill them. Surely they'll give good loot.",
       [
	   #(call_script, "script_change_player_honor", -20), 
	   #(troop_add_gold, "trp_player", 10000),
		#(call_script, "script_change_troop_renown", "trp_player", -100),
	   (change_screen_return),
        ]
       ),
      ]
  ),

        (
    "event_102",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You are a famous leader, and you received news that a group of women expresses interest in becoming camp followers.",
    "none",
    [
	
	],
    [
      ("choice_102_1",[],"They are welcome.",
       [
                  #(party_add_members, "p_main_party", "trp_euro_horse_1", 6),
                  (change_screen_return),
        ]
       ),
      ("choice_102_2",[],"I do not need more troops.",
       [
	    (change_screen_return),
        ]
       ),
      ]
  ),

        (
    "event_103",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You are a famous leader, and you received news that a group of refugees wishes to join you.",
    "none",
    [
	
	],
    [
      ("choice_103_1",[],"They are welcome.",
       [
                  #(party_add_members, "p_main_party", "trp_italian_village_recruit", 8),
                  (change_screen_return),
        ]
       ),
      ("choice_103_2",[],"I do not need more troops.",
       [
	    (change_screen_return),
        ]
       ),
      ]
  ),

#tropas acaba

        (
    "event_11",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "The kin of a soldier slain in one of your battles brings a suit against you requesting compensation of 200 denars. What do you do?",
    "none",
    [
	
	],
    [
      ("choice_11_1",[],"Pay the compensation",
       [   #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 200),
		#(troop_remove_gold, "trp_player", 200),
                (display_message, "@Compensation was paid."),
           	#(call_script, "script_change_player_honor", 2),
                #(call_script, "script_change_troop_renown", "trp_player", 5),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -10),
		(try_end),
          (change_screen_return),
        ]
       ),
      ("choice_11_2",[],"Refuse to pay",
       [
	   #(call_script, "script_change_player_honor", -12),
	    (change_screen_return),
        ]
       ),
      ("choice_11_3",[],"Refuse to answer the case at all",
       [
	   #(call_script, "script_change_player_honor", -8),
	   (change_screen_return),
        ]
       ),
      ]
  ),

          (
    "event_12",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "The kin of a noble slain by your men in the fight brings a suit against you requesting compensation of 500 denars. What do you do?",
    "none",
    [
	
	],
    [
      ("choice_12_1",[],"Pay the compensation",
       [   #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 500),
		#(troop_remove_gold, "trp_player", 500),
                (display_message, "@Compensation was paid."),
           	#(call_script, "script_change_player_honor", 3),
                #(call_script, "script_change_troop_renown", "trp_player", 5),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -15),
		(try_end),
          (change_screen_return),
        ]
       ),
      ("choice_12_2",[],"Refuse to pay",
       [
           	#(call_script, "script_change_player_honor", -15),
	    (change_screen_return),
        ]
       ),
      ("choice_12_3",[],"Refuse to answer the case at all",
       [
	   #(call_script, "script_change_player_honor", -10),
	   (change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_13",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You see an eagle circling above your party.",
    "none",
    [
	
	],
    [
      ("choice_13_1",[],"Tell to your men that the eagle symbolizes the recognition of the gods, and that the next battle you fight shall leave you victorious!",
       [
		  #(call_script, "script_change_player_party_morale", 5),
  (display_message, "@It is common knowledge that the eagle the eagle symbolizes baptised Christians, who have symbolically died and risen with Christ. Your men are impressed by your wordly knowledge, and grateful that God is with them."),
          (change_screen_return),
        ]
       ),
      ("choice_13_2",[],"Ignore it.",
       [
	(change_screen_return),
  (display_message, "@Your men pass by the bird without noticing it."),
        ]
       ),
      ("choice_13_3",[],"Tell them that although the eagles warn of a bad fortunes, you have faith in their sword arms!",
       [
	   #(call_script, "script_change_player_party_morale", -5),
	   (display_message, "@The eagle symbolizes the ascension of Christ - everyone knows that! Your lack of knowledge troubles your men, and they begin to doubt your certainty of character."),

	   (change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_14",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "A country farmer stands before you on the road, a weeping girl behind him. He points his finger accusingly at one of your men, saying that he raped his daughter and demands justice.",
    "none",
    [
	
	],
    [
      ("choice_14_1",[],"You will not tolerate indecency amongst your men! Brand the man and cast him out of your party.",
       [
		  #(call_script, "script_change_player_honor", 5),
          (change_screen_return),
        ]
       ),
      ("choice_14_2",[],"Give the accused man a lashing and consider the matter settled.",
       [
	(change_screen_return),
        ]
       ),
      ("choice_14_3",[],"It is a hard world, and a man will take what he can. Tell the farmer that he is lucky that is all the man did!",
       [
	   #(call_script, "script_change_player_honor", -5),
	   (change_screen_return),
        ]
       ),
      ]
  ),

      (
    "event_15",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You are traveling and suddenly spot a lot of mushrooms called 'porcini'. What do you do?",
    "none",
    [
	
	],
    [
      ("choice_15_1",[],"Pick them up and eat.",
       [
		  
                  (change_screen_return),
                  (display_message, "@The mushrooms were really tasty!"),
        ]
       ),
      ("choice_15_2",[],"Pick them up and give to your men.",
       [
            #(call_script, "script_change_player_party_morale", 1),
  (display_message, "@Your men are eating mushrooms while resting at camp. They seem to be happy."),

	    (change_screen_return),
        ]
       ),
      ("choice_15_3",[],"Pass by them.",
       [ 
	   (change_screen_return),
        ]
       ),
      ]
  ),

        (
    "event_16",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You are traveling and suddenly spot a lot of mushrooms called 'beautiful clavaria'. What do you do?",
    "none",
    [
	
	],
    [
      ("choice_16_1",[],"Pick them up and eat.",
       [
		   (display_message, "@The mushrooms were really tasteless. You have diarrhoea and feel very bad. Strength and agility attributes were decreased by 1."),
                (troop_raise_attribute, "trp_player",0,-1),
                   (troop_raise_attribute, "trp_player",1,-1),
                  (change_screen_return),
                 
        ]
       ),
      ("choice_16_2",[],"Pick them up and give to your men.",
       [
            #(call_script, "script_change_player_party_morale", -5),
  (display_message, "@Your men are eating mushrooms while resting at camp. Some of them have diarrhoea and feel very bad. They are angry!"),

	    (change_screen_return),
        ]
       ),
      ("choice_16_3",[],"Pass by them.",
       [ 
	   (change_screen_return),
        ]
       ),
      ]
  ),

     (
    "event_17",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You are traveling and suddenly spot a lot of mushrooms called 'angel of destruction'. What do you do?",
    "none",
    [
	
	],
    [
      ("choice_17_1",[],"Pick them up and eat.",
       [
		   (display_message, "@The mushrooms were completely tasteless. You have diarrhoea and feel very bad. Strength and agility attributes were decreased by 3."),
                (troop_raise_attribute, "trp_player",0,-2),
                   (troop_raise_attribute, "trp_player",1,-2),
                  (change_screen_return),
                 
        ]
       ),
      ("choice_17_2",[],"Pick them up and give to your men.",
       [
            #(call_script, "script_change_player_party_morale", -10),
  (display_message, "@Your men are eating mushrooms while resting at camp. Some of them have diarrhoea and feel very bad. They are really angry!"),

	    (change_screen_return),
        ]
       ),
      ("choice_17_3",[],"Pass by them.",
       [ 
	   (change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_18",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "In one of the rests of the day near a village, the elder's wife wants to see you (alone) while her husband is away.",
    "none",
    [
	
	],
    [
      ("choice_18_1",[],"You agree.",
       [
		  #(call_script, "script_change_player_honor", -15),
  (display_message, "@You spend a good time with the elder's wife, and when her husband returns, you hide in the stable."),
          (change_screen_return),
        ]
       ),
      ("choice_18_2",[],"You send one of your men in your place.",
       [
            #(call_script, "script_change_player_party_morale", 2),
		  #(call_script, "script_change_player_honor", -10),
	(change_screen_return),
        ]
       ),
      ("choice_18_3",[],"You refuse.",
       [
	   #(call_script, "script_change_player_honor", 2),
	   (change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_19",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You stumble over a group of christian priests that are being attacked by a group of muslims.",
    "none",
    [
	
	],
    [
      ("choice_19_1",[],"Rush to the aid of the priests to teach those bloody heretic bandits not to disturb the business of the holy church.",
       [
          #(call_script, "script_change_player_relation_with_faction", "fac_papacy", 15), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", 10), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", 10), #la q designemos	
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 5), #la q designemos		  

###Relation storing
#(store_relation, ":one", "fac_kingdom_20", "fac_player_faction"), #Store factions before reducing their values
#(store_relation, ":two", "fac_kingdom_25", "fac_player_faction"),

###Parameter checking & Consequences
(try_begin),
#(gt, ":one", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -10), #la q designemos
(try_end), 

(try_begin),
#(gt, ":two", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -10), #la q designemos
(try_end), 
	  
  #(call_script, "script_change_player_honor", 3),
  (display_message, "@Muslims run away when you are near!"),
          (change_screen_return),
        ]
       ),
      ("choice_19_2",[],"Aid the bandits to slaughter those sheeplike christians and bathe in their blood.",
       [
         ##(call_script, "script_change_player_relation_with_faction", "fac_papacy", -2), #la q designemos
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -2), #la q designemos
		  
###Relation storing
#(store_relation, ":one", "fac_kingdom_7", "fac_player_faction"), #Store factions before reducing their values
#(store_relation, ":two", "fac_kingdom_1", "fac_player_faction"),
#(store_relation, ":three", "fac_papacy", "fac_player_faction"),
#(store_relation, ":four", "fac_kingdom_23", "fac_player_faction"),

###Parameter checking & Consequences
(try_begin),
#(gt, ":one", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -10), #la q designemos
(try_end), 

(try_begin),
#(gt, ":two", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -10), #la q designemos
(try_end), 

(try_begin),
#(gt, ":three", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_papacy", -10), #la q designemos
(try_end), 

(try_begin),
#(gt, ":four", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -10), #la q designemos
(try_end), 
		  
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -2), #la q designemos	
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -1), #la q designemos		  		  
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", 10), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", 10), #la q designemos		  
    #(call_script, "script_change_player_honor", -5),
  (display_message, "@You kill the priests while claiming the name of Allah!"),
	(change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_20",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You happen to find a purse filled with coins.",
    "none",
    [
	
	],
    [
      ("choice_20_1",[],"You gift the purse to a hospice for abandoned children.",
       [
    #(call_script, "script_change_player_honor", 5),
          (change_screen_return),
        ]
       ),
      ("choice_20_2",[],"You keep the purse for yourself.",
       [
    #(call_script, "script_troop_add_gold", "trp_player", 100),
	(change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_21",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You come across some runaway slaves.",
    "none",
    [
	
	],
    [
      ("choice_21_1",[],"Help them on their way.",
       [
		#(call_script, "script_change_troop_renown", "trp_player", -2),
          (change_screen_return),
        ]
       ),
      ("choice_21_2",[],"Return them to their master.",
       [
		#(call_script, "script_change_troop_renown", "trp_player", 1),
    #(call_script, "script_troop_add_gold", "trp_player", 30),
	(change_screen_return),
        ]
       ),
      ]
  ),

      (
    "event_22",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You come upon bandits ambushing some merchants.",
    "none",
    [
	
	],
    [
      ("choice_22_1",[],"Chase the bandits away.",
       [
    #(call_script, "script_troop_add_gold", "trp_player", 40),
    #(call_script, "script_change_player_honor", 1),
  (display_message, "@Merchants give you some money!"),
          (change_screen_return),
        ]
       ),
      ("choice_22_2",[],"Aid the Bandits.",
       [
    #(call_script, "script_change_player_honor", -3),
    #(call_script, "script_troop_add_gold", "trp_player", 70),
	(change_screen_return),
        ]
       ),
      ]
  ),

      (
    "event_23",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Your fame and popularity has attracted young noblemen to your cause.",
    "none",
    [
	
	],
    [
      ("choice_23_1",[],"Accept them.",
       [
                  #(party_add_members, "p_main_party", "trp_merc_latin_horse", 4),
	    (change_screen_return),
        ]
       ),
      ("choice_23_2",[],"I don't need more men.",
       [
	   (change_screen_return),
        ]
       ),
      ]
  ),

      (
    "event_24",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You spot a poor man on the road, he looks tired. You send one of your men to ask him why he is in the wilderness alone. He says that men robbed him and that iff he doesn't get some money soon to buy food, he will starve. He says he served in the army once, and will make a loyal soldier.",
    "none",
    [
	
	],
    [
      ("choice_24_1",[],"Life's not fair, give him nothing.",
       [
    #(call_script, "script_change_player_honor", 6),
  (display_message, "@ The man's eyes sadly watch you while you follow your path."),
	    (change_screen_return),
        ]
       ),
      ("choice_24_2",[],"Give him money only to eat a very small meal, at least he will live.",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 100),
		#(troop_remove_gold, "trp_player", 100),
                (display_message, "@ You feel good for helping."),
           	#(call_script, "script_change_player_honor", 1),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -5),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_24_3",[],"Give him a ton! Every one deserves to eat.",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 400),
		#(troop_remove_gold, "trp_player", 400),
                (display_message, "@ You feel good for helping."),
           	#(call_script, "script_change_player_honor", 5),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -8),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_24_4",[],"Give him money and a horse, to ride home.",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 600),
		#(troop_remove_gold, "trp_player", 600),
                (display_message, "@ You feel good for helping."),
           	#(call_script, "script_change_player_honor", 10),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -10),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_24_5",[],"Pay him and suggest he join your army, he looks able after all.",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 800),
		#(troop_remove_gold, "trp_player", 800),
                (display_message, "@ When you give him armor and food, he draws a distinction in the size of a great soldier."),
                  #(party_add_members, "p_main_party", "trp_merc_latin_horse", 10),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -8),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ]
  ),

      (
    "event_25",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You encounter a small child dressed in rags and looking very hungry. It walks up to you and begs for some food; their family's crops produced no yields and they have no money.",
    "none",
    [
	
	],
    [
      ("choice_25_1",[],"Life's not fair, give them nothing.",
       [
    #(call_script, "script_change_player_honor", 6),
  (display_message, "@ The child's eyes sadly watch you while you follow your path."),
	    (change_screen_return),
        ]
       ),
      ("choice_25_2",[],"Give the child a handful of gold.",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 100),
		#(troop_remove_gold, "trp_player", 100),
                (display_message, "@ You feel good for helping."),
           	#(call_script, "script_change_player_honor", 1),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -5),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_25_3",[],"Give the child a sack of gold.",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 400),
		#(troop_remove_gold, "trp_player", 400),
                (display_message, "@ You feel good for helping."),
           	#(call_script, "script_change_player_honor", 5),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -8),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ]
  ),

      (
    "event_26",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "A group of bandits approach your camp. As your men ready their arms, the bandits put down their weapons and say they come in peace. The leader of the bandits approaches you and asks to join you.",
    "none",
    [
   (set_background_mesh, "mesh_load_window"),
	],
    [
      ("choice_26_1",[],"Of course! My party always welcomes bloodthirsty men!.",
       [
            #(call_script, "script_change_player_party_morale", -5),
		  #(call_script, "script_change_player_honor", -10),
                  #(party_add_members, "p_main_party", "trp_gaelic_infantry_1", 8),
                (display_message, "@ New troops join your party."),
	    (change_screen_return),
        ]
       ),
      ("choice_26_2",[],"I'm sorry, we have no room for your kind!.",
       [
                (display_message, "@ Bandits flee away."),
	   (change_screen_return),
        ]
       ),
      ("choice_26_3",[],"Prove yourselves worthy by raiding a village and bringing me the elder's head!",
       [
    #(call_script, "script_troop_add_gold", "trp_player", 200),
    #(call_script, "script_change_player_honor", -30),
		#(call_script, "script_change_troop_renown", "trp_player", -8),
                  #(party_add_members, "p_main_party", "trp_gaelic_spearman_1", 8),
                (display_message, "@ After tow hours the bandits return with some loot and the elder's head..."),
	   (change_screen_return),
        ]
       ),
      ("choice_26_4",[],"Kill them all!",
       [
    #(call_script, "script_troop_add_gold", "trp_player", 50),
    #(call_script, "script_change_player_honor", 1),
                (display_message, "@ Your men kill all the bandits."),
	   (change_screen_return),
        ]
       ),
      ]
  ),

            (
    "event_27",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "A christian fanatic follows your army. While he gains some converts he also creates some unrest.",
    "none",
    [
	
	],
    [
      ("choice_27_1",[],"Thank to God. Let him be!.",
       [
	   #ENVFIX Faction Keys and IDS
#	("kingdom_1", "Teutonic Order"
#	("kingdom_2", "Kingdom of Lithuania"
#	("kingdom_3", "Golden Horde"
#	("kingdom_4", "Kingdom of Denmark"
#	("kingdom_5", "Polish Principalities"
#	("kingdom_6", "Holy Roman Empire"
#	("kingdom_7", "Kingdom of Hungary"
#	("kingdom_8", "Novgorod Republic"
#	("kingdom_9", "Kingdom of England"
#	("kingdom_10", "Kingdom of France"
#	("kingdom_11", "Kingdom of Norway"
#	("kingdom_12", "Kingdom of Scotland"
#	("kingdom_13", "Gaelic Kingdoms"
#	("kingdom_14", "Kingdom of Sweden"
#	("kingdom_15", "Kingdom of Halych-Volhynia"
#	("kingdom_16", "Kingdom of Portugal"
#	("kingdom_17", "Crown of Aragon"
#	("kingdom_18", "Crown of Castile"
#	("kingdom_19", "Kingdom of Navarre"
#	("kingdom_20", "Emirate of Granada"
#	("papacy", "Papal States"
#	("kingdom_22", "Byzantine Empire"
#	("kingdom_23", "Crusader States"
#	("kingdom_24", "Kingdom of Sicily"
#	("kingdom_25", "Mamluk Sultanate"
#	("kingdom_26", "Latin Empire"
#	("kingdom_27", "Ilkhanate" 
#	("kingdom_28", "Hafsid Dynasty"
#	("kingdom_29", "Kingdom of Serbia"
#	("kingdom_30", "Bulgarian Empire"
#	("kingdom_31", "Marinid Dynasty"
#	("kingdom_32", "Republic of Venice"
#	("kingdom_33", "Yotvingians"
#	("kingdom_34", "Prussians"
#	("kingdom_35", "Curonians"
#	("kingdom_36", "Samogitians"
#	("kingdom_37", "Principality of Wales"
#	("kingdom_38", "Republic of Genoa"
#	("kingdom_39", "Republic of Pisa"
#	("kingdom_40", "Guelphs"
#	("kingdom_41", "Ghibellines"
#	("kingdom_42", "Kingdom of Bohemia"
#ENVFIX END Faction Keys & IDS
       (display_message, "@ They'll accept Christ by any means necessary!"),
	   	  #(call_script, "script_change_player_relation_with_faction", "fac_papacy", 20), #Papal States
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 5), #Teutonic Order
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", 15), #Crusader States
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_4", 10), #Kingdom of Denmark
		  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", 15), # 
		  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_9", 5), #
		  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_10", 5), #
		  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_11", 5), #
		  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_12", 5), #
		  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_17", 5), #
		  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_18", 5), #
		  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_24", 10), #
		  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_26", 10), #
		  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_38", 10), #
		  
		  #(store_relation, ":four", "fac_kingdom_20", "fac_player_faction"),
#(store_relation, ":fifth", "fac_kingdom_27", "fac_player_faction"),
#(store_relation, ":sixth", "fac_kingdom_25", "fac_player_faction"),
#(store_relation, ":seventh", "fac_kingdom_28", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":four", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -10), #la q designemos
(try_end), 

(try_begin),
#(gt, ":fifth", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_27", -10), #la q designemos
(try_end), 

(try_begin),
#(gt, ":sixth", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -10), #la q designemos
(try_end), 

(try_begin),
#(gt, ":seventh", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_28", -10), #la q designemos
(try_end), 
		  
		  
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -1), #la q designemos		  		  
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_27", -2), #la q designemos
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -2), #la q designemos			  
		  ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_28", -1), #la q designemos		  		  
	    (change_screen_return),
        ]
#       ),
#      ("choice_27_2",[],"Offer him a place in your troops!.",
#       [
#                (display_message, "@ He join you."),
#                  #(party_add_members, "p_main_party", "trp_picto_sacerdote", 1),
#          #(call_script, "script_change_player_relation_with_faction", "fac_christians", 5), #la q designemos
#          #(call_script, "script_change_player_relation_with_faction", "fac_pagans", -5), #la q designemos
#	   (change_screen_return),
#        ]
       ),
      ("choice_27_3",[],"Rat! Suppress him!",
       [
	   
	   #(store_relation, ":1st", "fac_kingdom_1", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":1st", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -10), #la q designemos
(try_end), 

#(store_relation, ":2nd", "fac_papacy", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":2nd", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_papacy", -10), #la q designemos
(try_end), 

#(store_relation, ":3rd", "fac_kingdom_23", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":3rd", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -10), #la q designemos
(try_end), 


	   
	   
         # #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -1), #la q designemos
         # #(call_script, "script_change_player_relation_with_faction", "fac_papacy", -2), #la q designemos
         # #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -2), #la q designemos	
         # #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -1), #la q designemos		  		  
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", 20), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", 15), #la q designemos		  
    #(call_script, "script_change_player_honor", -10),
            #(call_script, "script_change_player_party_morale", -2),
                (display_message, "@ The man insists too much, so you leave his body by the roadside."),
	   (change_screen_return),
        ]
       ),
      ]
  ),

# ("event_28",menu_text_color(0xFF000000)|mnf_disable_all_keys,
#    "A muslim fanatic follow your army. While he gains some converts he also creates some unrest.",
#    "none",
#    [
#	
#	],
#    [
#      ("choice_28_1",[],"Thank to Allah. Let him be!.",
#       [
#       (display_message, "@ They'll accept Islam by any means necessary!"),
#	   
#	   	   #(store_relation, ":1st", "fac_kingdom_1", "fac_player_faction"),
####Parameter checking & Consequences
#(try_begin),
#(#gt, ":1st", 15), #Only reduce if value is higher than 15.
##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -10), #la q designemos
#(try_end), 
#
#	   #(store_relation, ":2nd", "fac_papacy", "fac_player_faction"),
####Parameter checking & Consequences
#(try_begin),
##(gt, ":2nd", 15), #Only reduce if value is higher than 15.
##(call_script, "script_change_player_relation_with_faction", "fac_papacy", -10), #la q designemos
#(try_end), 
#
#	   #(store_relation, ":3rd", "fac_kingdom_7", "fac_player_faction"),
####Parameter checking & Consequences
#(try_begin),
##(gt, ":3rd", 15), #Only reduce if value is higher than 15.
##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -10), #la q designemos
#(try_end), 
#
#	   #(store_relation, ":4th", "fac_kingdom_23", "fac_player_faction"),
####Parameter checking & Consequences
#(try_begin),
##(gt, ":4th", 15), #Only reduce if value is higher than 15.
##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -10), #la q designemos
#(try_end), 
#	   
#	   
#          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -1), #la q designemos
#          ##(call_script, "script_change_player_relation_with_faction", "fac_papacy", -2), #la q designemos
#          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -1), #la q designemos	
#          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -2), #la q designemos		  		  
#          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", 20), #la q designemos
#          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", 15), #la q designemos		  
#	    (change_screen_return),
#        ]
#       ),
##      ("choice_28_2",[],"Offer him a place in your troops!.",
##       [
##                (display_message, "@ He join you."),
##                  #(party_add_members, "p_main_party", "trp_anglo_pagano", 1),
##          #(call_script, "script_change_player_relation_with_faction", "fac_christians", -5), #la q designemos
##          #(call_script, "script_change_player_relation_with_faction", "fac_pagans", 5), #la q designemos
##	   (change_screen_return),
##        ]
# #      ),
#      ("choice_28_3",[],"Rat! Suppress him!",
#       [
#          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 10), #la q designemos
#          #(call_script, "script_change_player_relation_with_faction", "fac_papacy", 10), #la q designemos
#          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", 20), #la q designemos	
#          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", 20), #la q designemos	
##(store_relation, ":1st", "fac_kingdom_25", "fac_player_faction"),
####Parameter checking & Consequences
#(try_begin),
##(gt, ":1st", 15), #Only reduce if value is higher than 15.
##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -5), #la q designemos
#(try_end), 
##(store_relation, ":2nd", "fac_kingdom_20", "fac_player_faction"),
####Parameter checking & Consequences
#(try_begin),
##(gt, ":2nd", 15), #Only reduce if value is higher than 15.
##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -5), #la q designemos
#(try_end),  
#       ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -1), #la q designemos
#       ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -1), #la q designemos		  
#       #(call_script, "script_change_player_honor", -10),
#       #(call_script, "script_change_player_party_morale", -2),
#        (display_message, "@ The man insists too much, and then you leave his body by the roadside."),
#	   (change_screen_return),
#        ]
#       ),
#      ]
#  ),

 (
    "event_29",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You come upon a Muslim mosque. The clerics are busy working or praying, none of them are armed. You see gold treasures and silver tributes glistening inside...",
    "none",
    [
	
	],
    [
      ("choice_29_1",[],"Pass by the temple!.",
       [
    #(call_script, "script_change_player_honor", -2),
	    (change_screen_return),
        ]
       ),
      ("choice_29_2",[],"Go inside, pray and pay a tribute. (200 denars).",
       [
                (display_message, "@ The clerics bless you and you continue your way ."),
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 200),
		#(troop_remove_gold, "trp_player", 200),
                (display_message, "@ You feel good for helping."),
           	#(call_script, "script_change_player_honor", 5),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
           	#(call_script, "script_change_player_honor", -3),
		#(call_script, "script_change_troop_renown", "trp_player", -5),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_29_3",[],"Loot the mosque, slaughter all the clerics and burn the place!",
       [
           	#(call_script, "script_change_player_honor", -30),
		#(call_script, "script_change_troop_renown", "trp_player", 15),
            #(call_script, "script_change_player_party_morale", -5),
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 10), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_papacy", 10), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", 5), #la q designemos	
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", 20), #la q designemos	

	   	   #(store_relation, ":1st", "fac_kingdom_25", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":1st", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -10), #la q designemos
(try_end), 

	   	   #(store_relation, ":2nd", "fac_kingdom_20", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":2nd", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -10), #la q designemos
(try_end), 
		  
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -2), #la q designemos
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -2), #la q designemos		  
    #(call_script, "script_troop_add_gold", "trp_player", 500),
                (display_message, "@ Blood and death everywhere. The clerics do not resist and you take possession of their gold."),
	   (change_screen_return),
        ]
       ),
      ]
  ),

 (
    "event_30",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You come upon a Christian monastery. The monks are busy working or praying, none of them are armed. You see gold treasures and silver tributes glistening inside...",
    "none",
    [
	
	],
    [
      ("choice_30_1",[],"Pass by the monastery!.",
       [
    #(call_script, "script_change_player_honor", -2),
	    (change_screen_return),
        ]
       ),
      ("choice_30_2",[],"Go inside, pray and pay a tribute. (200 denars).",
       [
                (display_message, "@ The monks bless you and you continue your way ."),
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 200),
		#(troop_remove_gold, "trp_player", 200),
                (display_message, "@ You feel good for helping."),
           	#(call_script, "script_change_player_honor", 5),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
           	#(call_script, "script_change_player_honor", -3),
		#(call_script, "script_change_troop_renown", "trp_player", -5),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_30_3",[],"Loot the church, slaughter all priests and burn the place!",
       [
           	#(call_script, "script_change_player_honor", -30),
		#(call_script, "script_change_troop_renown", "trp_player", 15),
            #(call_script, "script_change_player_party_morale", -5),
			
				   	   #(store_relation, ":value", "fac_kingdom_1", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -10), #la q designemos
(try_end), 

	   	   #(store_relation, ":value", "fac_papacy", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_papacy", -10), #la q designemos
(try_end), 

	   	   #(store_relation, ":value", "fac_kingdom_7", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -10), #la q designemos
(try_end), 

	   	   #(store_relation, ":value", "fac_kingdom_23", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -10), #la q designemos
(try_end), 
			
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -2), #la q designemos
          ##(call_script, "script_change_player_relation_with_faction", "fac_papacy", -2), #la q designemos
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -2), #la q designemos	
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -2), #la q designemos		  		  
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", 10), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", 10), #la q designemos		  
    #(call_script, "script_troop_add_gold", "trp_player", 500),
                (display_message, "@ With unusual fury, your pagan warriors plundered the monastery and killed all the monks. Blood covers the ground, greed shining in the eyes of the fiercest men."),
                (display_message, "@ Blood and death everywhere. The monks do not resist and you take possession of their gold. Your Christian followers do not seem very happy."),
	   (change_screen_return),
        ]
       ),
      ]
  ),

 (
    "event_31",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Some of your enemies have taken refuge in a nearby church after being defeated in battle and the rural priest have given them sanctuary.",
    "none",
    [
	
	],
    [
      ("choice_31_1",[],"Bah! They can go to the devil for all you care! You have enough prisoners and loot to satisfy yourself!.",
       [
		#(call_script, "script_change_troop_renown", "trp_player", -2),
	    (change_screen_return),
        ]
       ),
      ("choice_31_2",[],"Offer a pledge of safety to your enemies. Assure them you will treat them well. Offer a donation to the church fathers.",
       [
                (display_message, "@ The priest bless you and you continue on your way ."),

            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 100),
		#(troop_remove_gold, "trp_player", 100),
                (display_message, "@ You feel good for helping."),
           	#(call_script, "script_change_player_honor", 2),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -5),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_31_3",[],"What? Go inside and slaughter them. Kill any priest who interferes. You cannot allow these dogs to escape your justice!",
       [
           	#(call_script, "script_change_player_honor", -20),
		#(call_script, "script_change_troop_renown", "trp_player", 10),
            #(call_script, "script_change_player_party_morale", -3),
			
				   	   #(store_relation, ":value", "fac_kingdom_1", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -10), #la q designemos
(try_end), 
	   	   #(store_relation, ":value", "fac_papacy", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_papacy", -10), #la q designemos
(try_end), 
	   	   #(store_relation, ":value", "fac_kingdom_7", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -10), #la q designemos
(try_end), 
	   	   #(store_relation, ":value", "fac_kingdom_23", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -10), #la q designemos
(try_end), 
	   	   #(store_relation, ":value", "fac_kingdom_25", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -10), #la q designemos
(try_end), 
	   	   #(store_relation, ":value", "fac_kingdom_20", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -10), #la q designemos
(try_end), 
			
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -1), #la q designemos
          ##(call_script, "script_change_player_relation_with_faction", "fac_papacy", -1), #la q designemos
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -1), #la q designemos	
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -1), #la q designemos		  		  
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -1), #la q designemos
          ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -1), #la q designemos		  
    #(call_script, "script_troop_add_gold", "trp_player", 200),
                (display_message, "@ With unusual fury, your soldiers plundered the church and killed all the priests and your enemies. Blood covers the ground, greed shining in the eyes of the fiercest men."),
	   (change_screen_return),
        ]
       ),
      ]
  ),

 (
    "event_32",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You come across the grave of an old forgotten warlord.",
    "none",
    [
	
	],
    [
      ("choice_32_1",[],"Loot and pillage!.",
       [
           	#(call_script, "script_change_player_honor", -50),
		#(call_script, "script_change_troop_renown", "trp_player", -50),
            #(call_script, "script_change_player_party_morale", -20),
    #(call_script, "script_troop_add_gold", "trp_player", 100),
            #(troop_add_item, "trp_player","itm_scimitar_b",0),
            #(troop_add_item, "trp_player","itm_arabian_sword_a",0),                
                (display_message, "@ Among the remains is the sword and armor of a sultan. Magnificent equipment of high quality, once you remove the rust. Now they are yours if you do not mind the bad luck that belonged to the previous wielder."),
	    (change_screen_return),
        ]
       ),
      ("choice_32_2",[],"Pay for a new gravemarker",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 100),
		#(troop_remove_gold, "trp_player", 100),
                (display_message, "@ You feel good for helping."),
           	#(call_script, "script_change_player_honor", 10),
                (display_message, "@ Someday, perhaps, you might have the honor of being buried like a king."),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -5),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_32_3",[],"Tend to the grave and pay your respects",
       [
           	#(call_script, "script_change_player_honor", 3),
                (display_message, "@ Someday, perhaps, you might have the honor of being buried like a king."),
	   (change_screen_return),
        ]
       ),
      ]
  ),

 (
    "event_33",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "In the local tavern you come across a young monk who claims his master is chronicling the great and notable events of this land.\
He offers, at a small fee, to convince his master to overlook your notoriety for incessant pillaging and general debauchery and instead depict you as a something of a virtuous saint or a crusader for the poor and oppressed - whichever you prefer.",
    "none",
    [
	
	],
    [
      ("choice_33_1",[],"You decide to ignore him muttering that you are content to let history be the judge.",
       [
		#(call_script, "script_change_troop_renown", "trp_player", -5),
	    (change_screen_return),
        ]
       ),
      ("choice_33_2",[],"You pay the young monk what he asks for and mention that you will be back in due course to inspect the manuscript.",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 300),
		#(troop_remove_gold, "trp_player", 300),
                (display_message, "@ Fame is important."),
		#(call_script, "script_change_troop_renown", "trp_player", 5),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -2),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_33_3",[],"You gladly pay the monk his fee and some for his troubles.",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 500),
		#(troop_remove_gold, "trp_player", 500),
                (display_message, "@ Fame is important."),
		#(call_script, "script_change_troop_renown", "trp_player", 8),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -3),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_33_4",[],"After listening impatiently to the monk, you scold the monk remarking that you have never heard of a more pathetic scam in your life.",
       [
           	#(call_script, "script_change_player_honor", -3),
	   (change_screen_return),
        ]
       ),
      ]
  ),

 (
    "event_34",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You pass through a local village which appears down on its luck.\
To give the village a boost you announce that you will sponsor a sewing and embroidery contest for the gentle ladyfolk of the village and will reward handsomely the one who can produce the brightest, most fashionable yet suitably manly new tunic.",
    "none",
    [
	
	],
    [
      ("choice_34_1",[],"Reward the village well for their efforts and declare the prettiest girl in town to be the winner pointing her towards your tent.",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 500),
		#(troop_remove_gold, "trp_player", 500),
                (display_message, "@ The tunic isn't what matters, the girl is."),
		#(call_script, "script_change_troop_renown", "trp_player", 5),
            #(troop_add_item, "trp_player","itm_merchant_outfit",0),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -5),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_34_2",[],"You cast your eyes disappointingly, scold the village elder for not treating the matter seriously declaring that these rags are not fit for dishcloth, storming out of the town.",
       [
		#(call_script, "script_change_troop_renown", "trp_player", -5),
	   (change_screen_return),
        ]
       ),
      ("choice_34_3",[],"You collect various coloured tunics brought to you and amusingly think to yourself these would be good to cloth your hounds in winter or for some type of hound race derby. You compliment the village elder.",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 500),
		#(troop_remove_gold, "trp_player", 500),
                (display_message, "@ Fame is important."),
		#(call_script, "script_change_troop_renown", "trp_player", 5),
            #(troop_add_item, "trp_player","itm_ragged_cloth_b",0),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -3),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ]
  ),
#problema de espacio
 (
    "event_35",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "While reviewing the latest reconnaissance reports with your lieutenants, you whimsically remark that passing through the beautiful countryside makes you wish you could one day cast aside your sword settle down on your own land with some local buxom wench and spend the rest of your days making babies and growing stuff...\
To which one of the more smart lieutenants reports that this was hardly likely as your body odour was legendary forcing them to pay double to each lady of the night you took a fancy to and it well known that you thought that food  was made by shops and grew in boxes and urns.",
    "none",
    [
	
	],
    [
      ("choice_35_1",[],"Laugh heartily with his witty comment, while secretly making a mental note that you must send him deep into enemy territory on an 'important mission'.",
       [
           	#(call_script, "script_change_player_honor", -5),
            #(call_script, "script_change_player_party_morale", 5),
	    (change_screen_return),
        ]
       ),
      ("choice_35_2",[],"You glare at your young lieutenant and your mood turns for the worse but later on reflection you realise that he was probably right.",
       [
            #(call_script, "script_change_player_party_morale", 5),
	   (change_screen_return),
        ]
       ),
      ("choice_35_3",[],"You manage to force a smile while your comrades laughter surrounds you and when no one was looking, you give the secret wink to your bodyguard. This means that the young comedian's head will be impaled.",
       [
           	#(call_script, "script_change_player_honor", -5),
            #(call_script, "script_change_player_party_morale", -2),
		#(call_script, "script_change_troop_renown", "trp_player", 5),
	   (change_screen_return),
        ]
       ),
      ]
  ),

 (
    "event_36",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You come across what are evidently stray cattle from a nearby village",
    "none",
    [
	
	],
    [
      ("choice_36_1",[],"Return the animals to the village and ask for no reward.",
       [
           	#(call_script, "script_change_player_honor", 5),
 		#(call_script, "script_change_troop_renown", "trp_player", 10),
                (display_message, "@ The animals are essential to the survival of the village."),
	    (change_screen_return),
        ]
       ),
      ("choice_36_2",[],"Return the Animals. . . for a price.",
       [
 		#(call_script, "script_change_troop_renown", "trp_player", 10),
                #(call_script, "script_troop_add_gold", "trp_player", 250),
                (display_message, "@ You did return the animals, after all."),
	   (change_screen_return),
        ]
       ),
      ("choice_36_3",[],"Dinner!! Round up and slaughter the animals.",
       [
           	#(call_script, "script_change_player_honor", -3),
            #(call_script, "script_change_player_party_morale", 10),
                (display_message, "@ The animals were devoured on the spot."),
            #(troop_add_item, "trp_player","itm_cattle_meat",0),
	   (change_screen_return),
        ]
       ),
      ]
  ),

 (
    "event_37",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "A traveler tells you where to find a group of pilgrims on their way to Jerusalem.",
    "none",
    [
   (set_background_mesh, "mesh_load_window"),	
	],
    [
      ("choice_37_1",[],"You attack the small caravan, leaving few survivors.",
       [
           	#(call_script, "script_change_player_honor", -15),
 		#(call_script, "script_change_troop_renown", "trp_player", 2),
            #(call_script, "script_change_player_party_morale", 5),
                #(call_script, "script_troop_add_gold", "trp_player", 450),
				
#(store_relation, ":value", "fac_kingdom_1", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -10), #la q designemos
(try_end), 

#(store_relation, ":value", "fac_papacy", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_papacy", -10), #la q designemos
(try_end), 
				
					   	   #(store_relation, ":value", "fac_kingdom_7", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -10), #la q designemos
(try_end), 

	   	   #(store_relation, ":value", "fac_kingdom_23", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -10), #la q designemos
(try_end), 
				
				
       ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -2), #la q designemos
       #   #(call_script, "script_change_player_relation_with_faction", "fac_papacy", -2), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", 10), #la q designemos
      # #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -2), #la q designemos
      # #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -2), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", 10), #la q designemos	   
                (display_message, "@ With the blood of the sword falling to the elbow, you welcome the easy victory."),
	    (change_screen_return),
        ]
       ),
      ("choice_37_2",[],"Demand tribute for crossing the land. They pay and go on their way poorer than before.",
       [
           	#(call_script, "script_change_player_honor", -2),
                #(call_script, "script_troop_add_gold", "trp_player", 100),
	   (change_screen_return),
        ]
       ),
      ("choice_37_3",[],"Disperse the band and claim all their possessions as your own, leaving them only their lives.",
       [
           	#(call_script, "script_change_player_honor", -8),
            #(call_script, "script_change_player_party_morale", 2),
                #(call_script, "script_troop_add_gold", "trp_player", 250),
				#(store_relation, ":value", "fac_kingdom_1", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -10), #la q designemos
(try_end), 
#(store_relation, ":value", "fac_kingdom_23", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -10), #la q designemos
(try_end), 
#(store_relation, ":value", "fac_kingdom_7", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -10), #la q designemos
(try_end), 
#(store_relation, ":value", "fac_papacy", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_papacy", -10), #la q designemos
(try_end), 
				
				
        ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -1), #la q designemos
        #  #(call_script, "script_change_player_relation_with_faction", "fac_papacy", -1), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", 10), #la q designemos
      # #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -1), #la q designemos
     #  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -1), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", 10), #la q designemos	   
                (display_message, "@ Your soldiers get a kick out of harassing helpless pilgrims."),
            #(troop_add_item, "trp_player","itm_bread",0),
	   (change_screen_return),
        ]
       ),
      ("choice_37_4",[],"Help them on their way, giving them food and gold. They depart praising your name.",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 200),
		#(troop_remove_gold, "trp_player", 200),
                (display_message, "@ Honour and fame is important."),
		#(call_script, "script_change_troop_renown", "trp_player", 3),
           	#(call_script, "script_change_player_honor", 3),
        #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 10), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_papacy", 10), #la q designemos
		  
		  #(store_relation, ":value", "fac_kingdom_20", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -10), #la q designemos
(try_end), 

#(store_relation, ":value", "fac_kingdom_25", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -10), #la q designemos
(try_end), 
		  
         # #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -1), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", 20), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", 20), #la q designemos
      # #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -1), #la q designemos	   
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -6),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_37_5",[],"Ignore them, and let them go on their way ignorant of the danger that could have befallen them.",
       [
	   (change_screen_return),
        ]
       ),
      ]
  ),

 (
    "event_40",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "One of your soldiers rapes the daughter of a local elder.",
    "none",
    [
	
	],
    [
      ("choice_40_1",[],"Ignore the situation.",
       [
           	#(call_script, "script_change_player_honor", -15),
	    (change_screen_return),
        ]
       ),
      ("choice_40_2",[],"Punish the soldier.",
       [
           	#(call_script, "script_change_player_honor", 3),
		#(call_script, "script_change_troop_renown", "trp_player", 3),
            #(call_script, "script_change_player_party_morale", -5),
	   (change_screen_return),
        ]
       ),
      ("choice_40_3",[],"Execute the soldier and apologize for the incident.",
       [
           	#(call_script, "script_change_player_honor", 6),
            #(call_script, "script_change_player_party_morale", -10),
       #(call_script, "script_change_player_relation_with_faction", "fac_commoners", 5), #la q designemos
	   (change_screen_return),
        ]
       ),
      ("choice_40_4",[],"Pay compensation to local elder.",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 250),
		#(troop_remove_gold, "trp_player", 250),
                (display_message, "@ The girl is pregnant and the elder asks for a high compensation. To avoid rumors and problems, you pay."),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
           	#(call_script, "script_change_player_honor", -10),
		#(call_script, "script_change_troop_renown", "trp_player", -10),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ]
  ),

 (
    "event_41",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "One of your soldiers succumbs to his wounds from a previous battle.",
    "none",
    [
	
	],
    [
      ("choice_41_1",[],"Take his gear and his gold. After all, he was just a soldier - one of your pawns, and all he owns rightfully belong to you.",
       [
            #(call_script, "script_change_player_party_morale", -5),
           	#(call_script, "script_change_player_honor", -10),
                #(call_script, "script_troop_add_gold", "trp_player", 150),
                (display_message, "@ You get their meagre belongings."),
            #(troop_add_item, "trp_player","itm_berber_spear",0),
	    (change_screen_return),
        ]
       ),
      ("choice_41_2",[],"Give the soldier's belongings to his family.",
       [
           	#(call_script, "script_change_player_honor", 4),
            #(call_script, "script_change_player_party_morale", 4),
	   (change_screen_return),
        ]
       ),
      ("choice_41_3",[],"Give the soldier's belongings to his family and hold a funeral in his name.",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 250),
		#(troop_remove_gold, "trp_player", 250),
                (display_message, "@ Celebrating a funeral at your expense."),
           	#(call_script, "script_change_player_honor", 8),
            #(call_script, "script_change_player_party_morale", 8),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
           	#(call_script, "script_change_player_honor", -10),
            #(call_script, "script_change_player_party_morale", -10),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ]
  ),

 (
    "event_42",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "One of your new recruits dies from an illness. He carries both a muslim symbol and a cross. No one knows what he preferred most.",
    "none",
    [
	
	],
    [
      ("choice_42_1",[],"Do you give him a muslim funeral?",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 50),
		#(troop_remove_gold, "trp_player", 50),
                (display_message, "@ Celebrating a funeral at your expense."),
           	#(call_script, "script_change_player_honor", 1),
			
			#(store_relation, ":value", "fac_kingdom_1", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -10), #la q designemos
(try_end), 
#(store_relation, ":value", "fac_papacy", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_papacy", -10), #la q designemos
(try_end), 
#(store_relation, ":value", "fac_kingdom_7", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -10), #la q designemos
(try_end), 
#(store_relation, ":value", "fac_kingdom_23", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -10), #la q designemos
(try_end), 
			
       ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -1), #la q designemos
      #    #(call_script, "script_change_player_relation_with_faction", "fac_papacy", -1), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", 10), #la q designemos
      # #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -2), #la q designemos
     #  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -2), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", 10), #la q designemos	   
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
           	#(call_script, "script_change_player_honor", -15),
            #(call_script, "script_change_player_party_morale", -15),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_42_2",[],"Do you give him a christian funeral?",
       [
            #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 50),
		#(troop_remove_gold, "trp_player", 50),
                (display_message, "@ Celebrating a funeral at your expense."),
           	#(call_script, "script_change_player_honor", 1),
        #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 10), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_papacy", 10), #la q designemos
		  
		  #(store_relation, ":value", "fac_kingdom_20", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -10), #la q designemos
(try_end), 
#(store_relation, ":value", "fac_kingdom_25", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -10), #la q designemos
(try_end), 
		  
      #    #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -1), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", 20), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", 20), #la q designemos
     #  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -1), #la q designemos	   
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
           	#(call_script, "script_change_player_honor", -15),
            #(call_script, "script_change_player_party_morale", -15),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_42_3",[],"Just leave him lying there in fear of doing him wrong.",
       [
           	#(call_script, "script_change_player_honor", -15),
            #(call_script, "script_change_player_party_morale", -15),
	   (change_screen_return),
        ]
       ),
      ]
  ),

####random event juicios cuando eres rey chief
    (
    "event_01_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Two farmers, one very tall and lanky, the other low and stocky, were presented to you to discuss the ownership of a calf. Apparently their fields were bordering and the tall farmer had a bull that impregnated a cow belonging to the other farmer.\
The stocky farmer said the calf was his because it was his cow giving birth. The tall farmer claimed the calf to be his, being the offspring of his best bull, or at least financial compensation.",
    "none",
    [
	
	],
    [
      ("choice_01_1n",[],"The owner of the cow's right. The calf is yours, just like the cow is.",
       [
		  #(call_script, "script_change_troop_renown", "trp_player", -1),
          (change_screen_return),
        ]
       ),
      ("choice_01_2n",[],"The owner of the bull's right. The bull is his and the calf too.",
       [
		  #(call_script, "script_change_troop_renown", "trp_player", -1),
		(change_screen_return),
        ]
       ),
      ("choice_01_3n",[],"The owner of the cow keeps the calf and pays compensation of 30 denars to the owner of the bull.",
       [
	   (change_screen_return),
        ]
       ),
      ("choice_01_4n",[],"Neither is right. I'll stick with the calf and beef!",
       [
            #(troop_add_item, "trp_player","itm_dried_meat",0),
		  #(call_script, "script_change_troop_renown", "trp_player", -2),
	   (change_screen_return),
        ]
       ),
      ("choice_01_5n",[],"Neither is right. kill the calf and distribute its meat to the two farmers!",
       [
		  #(call_script, "script_change_troop_renown", "trp_player", 2),
	   (change_screen_return),
        ]
       ),
      ]
  ),
  

  (
    "event_02_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "My lord, we captured him! This is the man who attacked one of your messengers, whom is laying seriously injured on the bed. This doesn't show us in good light, the messenger was under your protection. But the attacker has an interesting story, and his wish was to tell it to you before his execution.^^\
Prisoner talk: My lord, I would have never thought of attacking your messenger... That man wished to sleep with my young daughter for the night, and of course this demand was refused for we are not barbarians! He never accepted the answer, however, and entered my house with three of his friends and violated my dear daughter, laughing that my king will never believe a commoner's word! I tried what I could think of, and I regret that I seriously injured him while he was under your protection, but what else is a father to do? Please grant mercy to your humble servant!",
    "none",
    [
	
	],
    [
      ("choice_02_1n",[],"The messenger was under my protection. You and your family will be executed at dawn, all your belongings confiscated!",
       [
	   #(troop_add_gold, "trp_player", 500),
		#(call_script, "script_change_troop_renown", "trp_player", -5),
	   #(call_script, "script_change_player_honor", -5),
		(change_screen_return),
        ]
       ),
      ("choice_02_2n",[],"The messenger is important, but I will be reasonable with you: Your family will not be punished, it is only you who will hang.",
       [
	   #(call_script, "script_change_troop_renown", "trp_player", -2),
		(change_screen_return),
        ]
       ),
      ("choice_02_3n",[],"While the messenger is important, I would have done the same. You can go, the king has spoken!",
       [
	   #(call_script, "script_change_player_honor", 1),
            #(call_script, "script_change_player_party_morale", -2),
	   (change_screen_return),
        ]
       ),
      ("choice_02_4n",[],"What? Throw that bastard out of my city! How could he abuse my loyal citizens?!",
       [
	   #(call_script, "script_change_player_honor", 1),
		#(call_script, "script_change_troop_renown", "trp_player", 2),
            #(call_script, "script_change_player_party_morale", -4),
	   (change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_03_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You summon two men to be judges over a dispute. One is a lord, while the other is a man sworn to the lord. It seems what happened is that the Lord didn't have enough tribute to pay his man, so the oath-man took his Lord's daughter to his own bed and had his way with her.",
    "none",
    [
	
	],
    [
      ("choice_03_1n",[],"Punish the oath-man, he violated his Lord's honor.",
       [
            #(call_script, "script_change_player_party_morale", -5),
		#(call_script, "script_change_troop_renown", "trp_player", 3),
	   (change_screen_return),
        ]
       ),
      ("choice_03_2n",[],"Punish the Lord, he failed in his duty as Lord.",
       [
            #(call_script, "script_change_player_party_morale", 3),
		#(call_script, "script_change_troop_renown", "trp_player", -5),
		(change_screen_return),
        ]
       ),
      ("choice_03_3n",[],"Ask to see the daughter, and when she is brought forth, you decide it was punishment enough that the oath-man had to sleep with her. Hire the oath-man for your own warband.",
       [
                  #(party_add_members, "p_main_party", "trp_scottish_village_recruit", 1),
	   #(call_script, "script_change_player_honor", -5),
	   (change_screen_return),
        ]
       ),
      ("choice_03_4n",[],"Compensate the Lord yourself for this crime, and pay the oath-man for the Lord's dereliction of duty.",
       [
		          #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 500),
		#(call_script, "script_change_player_honor", 1),
		#(troop_remove_gold, "trp_player", 500),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -15),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ]
  ),


  (
    "event_04_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "One of your sworn men approaches you. He states his fears that among the men, there is much dissatisfaction. Pertaining that you are too placid and that there is too little gold and honour to be won under your service.",
    "none",
    [
	
	],
    [
      ("choice_04_1n",[],"Pay the men and grant them rings.",
       [
		          #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 1000),
		#(troop_remove_gold, "trp_player", 1000),
            #(call_script, "script_change_player_party_morale", 4),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -15),
            #(call_script, "script_change_player_party_morale", -4),
		(try_end),
          (change_screen_return),
        ]
       ),
      ("choice_04_2n",[],"Tell the men that they are released from their oaths if they are so stupid and savage to question the wisdom of your leadership.",
       [
            #(call_script, "script_change_player_party_morale", -24),
		(change_screen_return),
        ]
       ),
      ("choice_04_3n",[],"Kill the man who approached you in front of your men and state there shall be no more talk of sedition.",
       [
	   #(call_script, "script_change_player_honor", -30),
            #(call_script, "script_change_player_party_morale", -14),
	   (change_screen_return),
        ]
       ),
      ("choice_04_4n",[],"Promise to change your manner of leadership, and announce the next big plunder is just around the corner.",
       [
	   (change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_05_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Gluttony. One of the 7 deadly sins, your majesty. After having feasted with your lords repeatedly over the last couple months, it appears your tunic no longer slips over your head. You have begun wearing open chest tunics and generally snacking on delicious fruits from the east. Dinner is of course a spiced pig roasted to perfection. Your wife abhors you but she is barren anyway and you have no lack of ladies/men willing to satisfy your flesh. Your physician however feels you have reached some sort of tipping point, and has suggested fresh air and a general course of exercise and a limited diet.",
    "none",
    [
	
	],
    [
      ("choice_05_1n",[],"Eat more food and change your physician.",
       [
            #(troop_add_item, "trp_player","itm_dried_meat",0),
             (troop_raise_attribute, "trp_player",0,-2),
             (change_screen_return),
        ]
       ),
      ("choice_05_2n",[],"Go on a pilgrimage to bath, to enjoy the turkish baths there whilst exercising regularly.",
       [
	    #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 300),
		#(troop_remove_gold, "trp_player", 300),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -7),
		(try_end),
		(change_screen_return),
        ]
       ),
      ("choice_05_3n",[],"Exist entirely on bowls of beans and lentils. Execute any man foolish enough to comment on your weight.",
       [
            #(call_script, "script_change_player_party_morale", -7),
	   (change_screen_return),
        ]
       ),
      ]
  ),


   (
    "event_06_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Your wife tarries with a youth of soft skin and curls that have an almost greek style to them. Indeed, it is rumoured your wife even calls him a young Apollo. Whilst it is fine for you to practise your sword craft among the populace, for your wife to taint your marriage in such a manner is...",
    "none",
    [
	],
    [
      ("choice_06_1n",[],"Acceptable. She is happy and you see no need to ruin such splendour.",
       [
		#(call_script, "script_change_troop_renown", "trp_player", -105),
          (change_screen_return),
        ]
       ),
      ("choice_06_2n",[],"No man cuckolds the king! Have the youth seized and castrated.",
       [
	   #(call_script, "script_change_player_honor", -15),
		(change_screen_return),
        ]
       ),
      ("choice_06_3n",[],"Have your mother move in to keep an eye on the queen.",
       [
	   (change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_07_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "The crop this year has withered miserably under the sun. As the first rain has fallen, there are many who fear the long months of winter as starvation looms. What should we do, my lord?",
    "none",
    [
	],
    [
      ("choice_07_1n",[],"I cannot spare any grain as I have to feed my household. There are feasts to be had.",
       [
		#(call_script, "script_change_troop_renown", "trp_player", -15),
	   #(call_script, "script_change_player_honor", -10),
            #(call_script, "script_change_player_party_morale", 4),
          (change_screen_return),
        ]
       ),
      ("choice_07_2n",[],"Distribute some wagons of grain to my people, as much as can be spared.",
       [
    (try_begin),
      (assign, ":var_5", 0),
	       # (assign, ":number_of_foods_player_has", 0),#Default
 #     (try_for_range, ":item", "itm_smoked_fish", "itm_siege_supply"),      
   #     (call_script, "script_cf_player_has_item_without_modifier", ":item", 41),
		        #(call_script, "script_cf_player_has_item_without_modifier", ":cur_edible", imod_rotten),#Default
        (val_add, ":var_5", 1),
		        #(val_add, ":number_of_foods_player_has", 1),#Default
      (try_end),
      (try_begin),
        (ge, ":var_5", 6),
		        #(ge, ":number_of_foods_player_has", 6), #Default
        (unlock_achievement, ACHIEVEMENT_ABUNDANT_FEAST),        
      (try_end),
    (try_end),
    (assign, ":var_7", 10),
	    #(assign, ":consumption_amount", 10), #Default
    #(assign, ":no_food_displayed", 0), #default
	   #(assign, ":value", 0), #new
    #(try_for_range, ":unused", 0, ":consumption_amount"), #Default
      #(assign, ":available_food", 0), #Default
	      (try_for_range, ":unused", 0, ":var_7"), #Default
      (assign, ":var_10", 0), #Default
 #     (try_for_range, ":item_2", "itm_smoked_fish", "itm_siege_supply"),
       # (item_set_slot, ":item_2", slot_item_is_checked, 0),
 #       (call_script, "script_cf_player_has_item_without_modifier", ":item_2", 41),
		     # (try_for_range, ":cur_food", food_begin, food_end), #Default
        #(item_set_slot, ":cur_food", slot_item_is_checked, 0), #Default
        #(call_script, "script_cf_player_has_item_without_modifier", ":cur_food", imod_rotten), #Default
        (val_add, ":var_10", 1), #Default
		        #(val_add, ":available_food", 1), #Default
      (try_end),
      (try_begin),
        (gt, ":var_10", 0),
		        #(gt, ":available_food", 0), #Default
        #(store_random_in_range, ":selected_food", 0, ":available_food"), #Default
       #(call_script, "script_consume_food", ":selected_food"), #default
		#(store_random_in_range, ":random_in_range_0_var_10", 0, ":var_10"),
  #      (call_script, "script_consume_food", ":random_in_range_0_var_10"),
	   #(call_script, "script_change_player_honor", 10),
	   #(call_script, "script_change_player_party_morale", -2),
	   (display_message, "@Part of your food was distributed.", 0xFF0000),
      (else_try),
        #(eq, ":no_food_displayed", 0), #Default
		     #   (eq, ":value", 0), #new
        (display_message, "@Your men have nothing to eat!", 0xFF0000),
        #(call_script, "script_change_player_party_morale", -18),
        #(assign, ":no_food_displayed", 1), #Default
		    #    (assign, ":value", 1),  #new
		
        (try_begin),
  #          (call_script, "script_party_count_fit_regulars", "p_main_party"),
            (gt, reg0, 0),
     #       (call_script, "script_objectionable_action", tmt_egalitarian, "str_men_hungry"),
        (try_end),
      (try_end),
    (try_end),
		(change_screen_return),
        ]
       ),
      ("choice_07_3n",[],"Import grain from Ayyubid Sultanate, let there be enough for everyone.",
       [
		#(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 1000),
		#(troop_remove_gold, "trp_player", 1000),
         	   #(call_script, "script_change_player_honor", 15),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -50),
		(try_end),
	   (change_screen_return),
        ]
       ),
	   ("choice_07_4n",[],"Let them rot! Serves them right for not tending to their crops!",
       [
	   #(call_script, "script_change_player_honor", -20),
	   (change_screen_return),
        ]
       ),
      ]
  ),

(
    "event_08_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "One of your lords approaches you stating, he has an illegitimate though favoured son who wishes to join your bodyguard. You agree to meet the boy as it would be unseemly to reject a noble. When you meet the boy, however it is clear that he is rather homely and certainly not a man of war. Faced with this plump, smiling young man do you.",
    "none",
    [
	],
    [
      ("choice_08_1n",[],"Allow him to join your bodyguard thus appalling your bodyguard.",
       [
                  #(party_add_members, "p_main_party", "trp_anatolian_village_recruit", 1),
        #(call_script, "script_change_player_party_morale", -10),
          (change_screen_return),
        ]
       ),
      ("choice_08_2n",[],"Ask for payment to grease the deal.",
       [
                  #(party_add_members, "p_main_party", "trp_anatolian_village_recruit", 1),
	   #(troop_add_gold, "trp_player", 500),
        #(call_script, "script_change_player_party_morale", -18),
		(change_screen_return),
        ]
       ),
      ("choice_08_3n",[],"Refuse outright, offending the noble.",
       [
		#(call_script, "script_change_troop_renown", "trp_player", -5),
		(change_screen_return),
        ]
       ),
      ]
  ),
#fine   
    (
    "event_09_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Two proposals come before you one day. One is a scholarly young monk with a lisp called Brother Gilchrist who proposes the building of more monasteries and a fund to be set aside to buy and maintain books of knowledge. Although his case is eloquent, the delivery is less so.\
Another man comes forward. A hulking, bearded warrior who makes Gilchrist visibly wince in his shadow. He suggests the funds are better allocated in the purchase of weapons, horses and shields, things that can be used today and are not mere decoration.",
    "none",
    [
	
	],
    [
      ("choice_09_1n",[],"Choose Gilchrist stating that a wise king has need of books far more than the sword.",
       [
		#(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 600),
		#(troop_remove_gold, "trp_player", 600),
                  (troop_raise_attribute, "trp_player",2,1),		  
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -10),
		(try_end),
                  (change_screen_return),
        ]
       ),
      ("choice_09_2n",[],"Choose the warrior, stating that books have no place in this age of war.",
       [
		#(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 600),
		#(troop_remove_gold, "trp_player", 600),
                  (troop_raise_proficiency, "trp_player",0,15),		  
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -10),
		(try_end),
	    (change_screen_return),
        ]
       ),
      ("choice_09_3n",[],"State a kingdom needs both men of knowledge and men of war.",
       [ 
		#(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 2000),
		#(troop_remove_gold, "trp_player", 2000),
                  (troop_raise_attribute, "trp_player",2,1),		  
                  (troop_raise_proficiency, "trp_player",0,15),		  
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -20),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_9_4n",[],"Decline both their offers, stating the kingdom has need of neither and that this topic does not interest you.",
       [
                  (change_screen_return),
        ]
       ),
      ]
  ),

        (
    "event_11_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "The sound of a galloping horse pierces the cold morning, and you run outside to find a scout. He tells you a ship has been shipwrecked near your coast. What do you do?",
    "none",
    [
	
	],
    [
      ("choice_11_1n",[],"Immediately send a warband to investigate and search for valuables; if there are any survivors, kill them.",
       [
           	#(call_script, "script_change_player_honor", -8),
	   #(troop_add_gold, "trp_player", 500),
          (change_screen_return),
        ]
       ),
      ("choice_11_2n",[],"Immediately send a warband to investigate and search for valuables; if there are any survivors, recruit them.",
       [
	   #(call_script, "script_change_player_honor", 2),
        #(call_script, "script_change_player_party_morale", -8),
                  #(party_add_members, "p_main_party", "trp_balt_billman", 8),
	    (change_screen_return),
        ]
       ),
      ("choice_11_3n",[],"Just another ship wreck in an age of unrest. Leave it be.",
       [
	   (change_screen_return),
        ]
       ),
      ]
  ),

          (
    "event_12_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "The runner arrives at the courtroom, and after you allow, starts to tell dire news: My lord, a village is in great danger! The populace has some kind of strange sickness, they can hardly move, sweat and vomit, and the local wise-woman has no cure for it. The lord of the village doesn't let anyone out, and is expecting your orders!",
    "none",
    [
	
	],
    [
      ("choice_12_1n",[],"Dire news indeed! The quarantine should stay, but I will send in my best surgeon to help!",
       [   #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 300),
		#(troop_remove_gold, "trp_player", 300),
           	#(call_script, "script_change_player_honor", 3),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -15),
		(try_end),
          (change_screen_return),
        ]
       ),
      ("choice_12_2n",[],"Dire news indeed! We cannot risk our best surgeon. The quarantine should stay, and we will examine the survivors when the epidemic is over!",
       [
           	#(call_script, "script_change_player_honor", -15),
	    (change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_13_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "The nuns approach you: My lord, the childbirth is not going well! We tried everything we could, but it seems that the young lady is simply not suited for pregnancy. All what is left is to pray for our dear Virgin Mary to help!.",
    "none",
    [
	
	],
    [
      ("choice_13_1n",[],"Everybody, kneel down and start praying!",
       [
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 10), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_papacy", 10), #la q designemos
		  		  #(store_relation, ":value", "fac_kingdom_25", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -10), #la q designemos
(try_end), 

		  #(store_relation, ":value", "fac_kingdom_20", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -10), #la q designemos
(try_end), 
      #    #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -1), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", 10), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", 10), #la q designemos
     #  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -1), #la q designemos	   
          (change_screen_return),
        ]
       ),
      ("choice_13_2n",[],"Hah! Your faith is good for nothing! Guards: Bring me a muslim surgeon from the village!.",
       [
	   
	   		  		  #(store_relation, ":value", "fac_kingdom_1", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -10), #la q designemos
(try_end), 
		  		  #(store_relation, ":value", "fac_papacy", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_papacy", -10), #la q designemos
(try_end), 

		  		  #(store_relation, ":value", "fac_kingdom_7", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -10), #la q designemos
(try_end), 

		  		  #(store_relation, ":value", "fac_kingdom_23", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -10), #la q designemos
(try_end), 
	   
	   
      # #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -1), #la q designemos
      #    #(call_script, "script_change_player_relation_with_faction", "fac_papacy", -1), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", 10), #la q designemos
     #  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -1), #la q designemos
    #   #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -1), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", 10), #la q designemos	   
	(change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_14_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "One day, a loyal noble warrior comes to you with a strange request. 'My lord, I am in a very bad situation. I spent all my money on proper equipment and troops, so that I can serve you well. However, my first daughter is about to marry, and I cannot give a proper present with her to the husband'.",
    "none",
    [
	
	],
    [
      ("choice_14_1n",[],"Take this small amount of gold for your faithful service.",
       [
 #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 800),
		#(troop_remove_gold, "trp_player", 800),
           	#(call_script, "script_change_player_honor", 10),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -15),
		(try_end),
 (change_screen_return),
        ]
       ),
      ("choice_14_2n",[],"Everyone should plan ahead, you should have known it was about time to marry off your daughter. I will help you now, but this is the only time.",
       [
 #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 400),
		#(troop_remove_gold, "trp_player", 400),
        #(call_script, "script_change_player_party_morale", -2),
           	#(call_script, "script_change_player_honor", 2),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -15),
		(try_end),
	(change_screen_return),
        ]
       ),
      ("choice_14_3n",[],"This is your personal issue. You should have planned better ahead.",
       [
        #(call_script, "script_change_player_party_morale", -12),
	   #(call_script, "script_change_player_honor", -15),
	   (change_screen_return),
        ]
       ),
      ]
  ),

      (
    "event_15_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "One day, your chaplain arrives at your doorstep, he seems very enthusiastic. 'My lord, I have splendid news! There is a merchant from Jerusalem in the town now, and he is willing to sell us a piece of the Holy Cross! I cannot believe that we have the opportunity to have such a famous relic!'",
    "none",
    [
	
	],
    [
      ("choice_15_1n",[],"I have seen so many parts of the Holy Cross, that it must have been at least a size of a castle! We don't pay for fake relics!",
       [
	   
	   		  		  #(store_relation, ":value", "fac_kingdom_1", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -10), #la q designemos
(try_end), 

		  		  #(store_relation, ":value", "fac_papacy", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_papacy", -10), #la q designemos
(try_end), 

		  		  #(store_relation, ":value", "fac_kingdom_7", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -10), #la q designemos
(try_end), 

		  		  #(store_relation, ":value", "fac_kingdom_23", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -10), #la q designemos
(try_end), 
	   
       ##(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -1), #la q designemos
      #    #(call_script, "script_change_player_relation_with_faction", "fac_papacy", -1), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", 10), #la q designemos
     #  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -1), #la q designemos
    #   #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -1), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", 10), #la q designemos	   
      (try_end),
                  (change_screen_return),
        ]
       ),
      ("choice_15_2n",[],"This is a very good offer indeed, but sadly we don't have that much in the coffers.",
       [
	   
	   		  		  #(store_relation, ":value", "fac_kingdom_23", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -10), #la q designemos
(try_end), 

		  		  #(store_relation, ":value", "fac_papacy", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_papacy", -10), #la q designemos
(try_end), 

		  		  #(store_relation, ":value", "fac_kingdom_1", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -10), #la q designemos
(try_end), 

		  		  #(store_relation, ":value", "fac_kingdom_7", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -10), #la q designemos
(try_end), 
	   
	   
      # #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -1), #la q designemos
     #     #(call_script, "script_change_player_relation_with_faction", "fac_papacy", -1), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", 10), #la q designemos
    #   #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -1), #la q designemos
    #   #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -1), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", 10), #la q designemos	   
      (try_end),
	    (change_screen_return),
        ]
       ),
      ("choice_15_3n",[],"We cannot let this opportunity slip!",
       [ 
 #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 5000),
		#(troop_remove_gold, "trp_player", 5000),
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 20), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_papacy", 20), #la q designemos
		  	   		  		  #(store_relation, ":value", "fac_kingdom_25", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -10), #la q designemos
(try_end), 

	   		  		  #(store_relation, ":value", "fac_kingdom_20", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -10), #la q designemos
(try_end), 
      #    #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -1), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", 20), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", 20), #la q designemos
    #   #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -1), #la q designemos	   
      (try_end),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -55),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ]
  ),

        (
    "event_16_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "You were having a feast with your companions when a messenger of the guild masters court came to your attention, 'My great King, there is a situation in the town and needs your council.' You left for the town, taking your mighty sword with you.^^\
There is a great deal of rumble among the crowd, but when you appear, silence befals the audience. An elder bows to you and ask permission to speak, which you give, and says: My lord, here is a case worthy the wisdom of a king. There are two women who claim to be the mother of this child, neither desist.^\
You inform the crowd: 'Let their faces be know and let this forgo'. Two women show up, one in plain clothes and another in rags. You say 'If neither agree, the children will be in the dead sea' You direct your guards to cut the children in half and give each half to the two women.\
Then the woman in rags scream and says 'No, please, my great king, let the other woman have the child! You stare at her and say: 'Your are the rightful mother and this child belongs to you.'. As for the other woman:",
    "none",
    [
	
	],
    [
      ("choice_16_1n",[],"Imprison her for lying, for it is the greatest sin.",
       [
	   #(call_script, "script_change_player_honor", 5),
		#(call_script, "script_change_troop_renown", "trp_player", -5),
                  (change_screen_return),
                 
        ]
       ),
      ("choice_16_2n",[],"Cut her down with your mighty sword, to show there is no mercy for liars.",
       [
	   #(call_script, "script_change_player_honor", -5),
		#(call_script, "script_change_troop_renown", "trp_player", 5),
	    (change_screen_return),
        ]
       ),
      ("choice_16_3n",[],"Give her and the crowd a speech about honesty and honour, then let her live with the memories of what happened today.",
       [ 
	   (change_screen_return),
        ]
       ),
      ]
  ),

     (
    "event_17_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Your advisor, streaked with dirt and sunburnt, arrives after inspecting the harvest. 'My Lord, the harvest is poor this year. If you do not reduce taxes there will be starvation come winter.",
    "none",
    [
	
	],
    [
      ("choice_17_1n",[],"And if I reduce taxes I will have to release men from their oaths, and our enemies would overrun us. Better an empty gut than a cut throat.",
       [
		#(call_script, "script_change_troop_renown", "trp_player", -25),
                  (change_screen_return),
                 
        ]
       ),
      ("choice_17_2n",[],"Then reduce the tax. I will compensate the loss through the treasury.",
       [
 #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 2000),
		#(troop_remove_gold, "trp_player", 2000),
		#(call_script, "script_change_troop_renown", "trp_player", 15),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -35),
		(try_end),
	    (change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_18_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "A peasant from a nearby village comes to you as a supplicant. He breathlessly reports that armed men from a nearby kingdom have raided your holdings, carrying off women, cattle and grain. He is spattered with blood and stinks of burned thatch.",
    "none",
    [
	
	],
    [
      ("choice_18_1n",[],"Gather my men! We'll avenge this insult with blood!",
       [
 #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 300),
		#(troop_remove_gold, "trp_player", 300),
		#(call_script, "script_change_troop_renown", "trp_player", 5),
		  #(call_script, "script_change_player_honor", 5),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -15),
		(try_end),
          (change_screen_return),
        ]
       ),
      ("choice_18_2n",[],"There is nothing to be done here. Away with you, mongrel!",
       [
            #(call_script, "script_change_player_party_morale", -2),
		  #(call_script, "script_change_player_honor", -10),
	(change_screen_return),
        ]
       ),
      ("choice_18_3n",[],"There will be war. You have done well to report this to me. You will be provided funds to rebuild your village.",
       [
 #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 150),
		#(troop_remove_gold, "trp_player", 150),
		#(call_script, "script_change_troop_renown", "trp_player", 1),
		  #(call_script, "script_change_player_honor", 1),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -5),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_18_4n",[],"How can I be sure it wasn't a band of bandits or pirates? There is little I can do for you. Take this to compensate some of your losses.",
       [
 #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 100),
		#(troop_remove_gold, "trp_player", 100),
		  #(call_script, "script_change_player_honor", 1),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -5),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_19_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "A prostitute is accused of witchcraft, after several oathmen sworn to your vassal report pain while relieving themselves. Your vassal backs their claim, and you suspect they have the same complaint but know better than to air it publicly.",
    "none",
    [
	
	],
    [
      ("choice_19_1n",[],"Banish the prostitute, exiling her to foreign lands.",
       [
    #(call_script, "script_change_player_honor", -1),
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 10), #la q designemos
          #(call_script, "script_change_player_relation_with_faction", "fac_papacy", 10), #la q designemos
		  	   		  		  #(store_relation, ":value", "fac_kingdom_25", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -10), #la q designemos
(try_end), 

	   		  		  #(store_relation, ":value", "fac_kingdom_20", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -10), #la q designemos
(try_end), 
       #   #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -1), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", 10), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", 10), #la q designemos
     #  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -1), #la q designemos	   
          (change_screen_return),
        ]
       ),
      ("choice_19_2n",[],"Pay a retainer to the witch and have her help you to counteract the spread of Christianity.",
       [
	   
	   	   		  		  #(store_relation, ":value", "fac_kingdom_1", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -10), #la q designemos
(try_end), 
	   		  		  #(store_relation, ":value", "fac_papacy", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_papacy", -10), #la q designemos
(try_end), 
	   		  		  #(store_relation, ":value", "fac_kingdom_7", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -10), #la q designemos
(try_end), 
	   		  		  #(store_relation, ":value", "fac_kingdom_23", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -10), #la q designemos
(try_end), 
	   
     #  #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", -1), #la q designemos
    #   #(call_script, "script_change_player_relation_with_faction", "fac_papacy", -1), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", 20), #la q designemos
    #   #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", -1), #la q designemos
    #   #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", -1), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", 20), #la q designemos	   
      (try_end),
	(change_screen_return),
        ]
       ),
      ("choice_19_3n",[],"Witches! Where there's one there's many! Kill the witch and ensure the sanctity of your god-given holdings by killing anyone else reported for witchcraft.",
       [
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 20), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_papacy", 20), #la q designemos
	   	   	   		  		  #(store_relation, ":value", "fac_kingdom_20", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -10), #la q designemos
(try_end), 

	   	   		  		  #(store_relation, ":value", "fac_kingdom_25", "fac_player_faction"),
###Parameter checking & Consequences
(try_begin),
#(gt, ":value", 15), #Only reduce if value is higher than 15.
#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -10), #la q designemos
(try_end), 
      # #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_25", -1), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_7", 20), #la q designemos
       #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_23", 20), #la q designemos
   #    #(call_script, "script_change_player_relation_with_faction", "fac_kingdom_20", -1), #la q designemos	   
      (try_end),
	(change_screen_return),
        ]
       ),
      ]
  ),

   (
    "event_21_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Your people live divided up into familial clans. One day a young clan leader comes to you with a request for justice. His clan has long suffered in the cattle raiding that exists between all clans to a stronger clan, stronger he says purely by numbers and chance. In an attempt to stem the flow of loss, this enmity between the two clans having existed for at least a hundred years, the young clan chief suggested a marriage to one of the daughters of the other clan.\
The other clan chief, a wily old man, had a surprise for the young man. Having picked his bride, all seemed to be set. It was to the young man's horror that he was presented with the younger sister of his chosen bride, the young man being a romantic at heart and as stubborn as one who believes in true love is refused outright. He then with his chosen men and brothers carried off his chosen bride in the night. The other clan chief then annexed his lands on claims of rape and theft. The young clan chief requests the return of his land and to live with his bride there.",
    "none",
    [
	
	],
    [
      ("choice_21_1n",[],"Grant the man's request.",
       [
    #(call_script, "script_change_player_honor", 2),
        #(troop_add_gold, "trp_player", 100),
          (change_screen_return),
        ]
       ),
      ("choice_21_2n",[],"Imprison the man and declare his clan forfeit and the lands given over to the bigger clan.",
       [
		#(call_script, "script_change_troop_renown", "trp_player", -5),
    #(call_script, "script_change_player_honor", -5),
        #(troop_add_gold, "trp_player", 500),
	(change_screen_return),
        ]
       ),
      ("choice_21_3n",[],"Seize the lands for yourself and exile the youth.",
       [
		#(call_script, "script_change_troop_renown", "trp_player", -10),
    #(call_script, "script_change_player_honor", -10),
        #(troop_add_gold, "trp_player", 1000),
	(change_screen_return),
        ]
       ),
      ]
  ),

      (
    "event_22_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "A woman from a nearby village comes to you claiming that one of your men who has died recently was her husband, she asks for assistance to take care of her deceased husband.",
    "none",
    [
	
	],
    [
      ("choice_22_1n",[],"Give her monetary assistance and send for a priest.",
       [
 #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 500),
		#(troop_remove_gold, "trp_player", 500),
		  #(call_script, "script_change_player_honor", 5),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -10),
		(try_end),
          (change_screen_return),
        ]
       ),
      ("choice_22_2n",[],"Do Nothing.",
       [
    #(call_script, "script_change_player_honor", -8),
	(change_screen_return),
        ]
       ),
      ]
  ),

      (
    "event_23_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Your wife and queen approaches you with a request, 'My lord, would it not show your great mercy and honour by providing for those who have suffered while serving under you? We have dozens of maimed, lame and aged soldiers begging for coin in the streets, and many families who have lost fathers and husbands in your battles. We need to reward and protect your loyal supporters or else men might be hesitant in the future to be in your army.",
    "none",
    [
	
	],
    [
      ("choice_23_1n",[],"Bah! Let the orphans and my warriors who were unskilled enough to defend themselves properly rot.",
       [
		#(call_script, "script_change_troop_renown", "trp_player", -15),
    #(call_script, "script_change_player_honor", -15),
	    (change_screen_return),
        ]
       ),
      ("choice_23_2n",[],"Send those outcasts my regards, but I regret there is nothing I can do for them.",
       [
		#(call_script, "script_change_troop_renown", "trp_player", -15),
	   (change_screen_return),
        ]
       ),
      ("choice_23_3n",[],"I agree, we should support our veterans and their families, just this once as I am feeling generous.",
       [
 #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 500),
		#(troop_remove_gold, "trp_player", 500),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -10),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_23_4n",[],"This is a tragedy! Immediately open my coffers and make it kingdom policy that all families shall receive support from their King.",
       [
 #(store_troop_gold, ":gold", "trp_player"),
	   (try_begin),
		#(ge, ":gold", 2000),
		#(troop_remove_gold, "trp_player", 2000),
		#(call_script, "script_change_troop_renown", "trp_player", 15),
    #(call_script, "script_change_player_honor", 15),
		(else_try),
		(display_message, "@You don't have enough gold. How embarassing!"),
		#(call_script, "script_change_troop_renown", "trp_player", -30),
		(try_end),
	   (change_screen_return),
        ]
       ),
      ]
  ),

      (
    "event_24_juicio",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "A seemingly straightforward case is brought before you: Yesterday, the accused man broke into the victim's house and removed large amounts of wealth. Many people saw him and the missing items were discovered in his house. But the victim was a influential supporter of the previous lord, had actually served as a councilor and was known to be of doubtful loyalties, while the accused was one of your most vocal supporters and had donated much money to your cause.",
    "none",
    [
	
	],
    [
      ("choice_24_1n",[],"Ignoring the evidence, you settle in your man's favour, actually saying that he was acting on your orders.",
       [
    #(call_script, "script_change_player_honor", -6),
            #(call_script, "script_change_player_party_morale", 5),
  #reduce relacion con cada centro chief
      #(try_for_range, ":party_3", centers_begin, centers_end),
  #(call_script, "script_change_player_relation_with_center", ":party_3", -1),
      (try_end),
	    (change_screen_return),
        ]
       ),
      ("choice_24_2n",[],"The evidence is clear, the jury agrees, and the accused is found guilty and has his hands cut off for theft!",
       [
            #(call_script, "script_change_player_party_morale", -15),
  #reduce relacion con cada centro chief
      #(try_for_range, ":party_3", centers_begin, centers_end),
  #(call_script, "script_change_player_relation_with_center", ":party_3", 1),
      #(try_end),
	   (change_screen_return),
        ]
       ),
      ("choice_24_3n",[],"You claim both parties are in the wrong, exiling them and confiscating all material pertaining to the case.",
       [
        #(troop_add_gold, "trp_player", 1000),
            #(call_script, "script_change_player_party_morale", -10),
  #reduce relacion con cada centro chief
      #(try_for_range, ":party_3", centers_begin, centers_end),
  #(call_script, "script_change_player_relation_with_center", ":party_3", -1),
      #(try_end),
	   (change_screen_return),
        ]
       ),
      ]
  ),
	
	
	
	
	#Notes & Hotkeys
	#
	 #   ("notes_and_hotkeys_full",menu_text_color(0xFF000000)|mnf_disable_all_keys,

	 #old ("notes_and_hotkeys_full",0,"^^            
	 ("notes_and_hotkeys_full",menu_text_color(0xFF000000)|mnf_disable_all_keys,"^^*Notes*^Some skills were moved to the Trait menu in Camp, there are additional skills, such as Policy, Battle & Adventure skills, all upgradeable within the Camp & Report menus.^^If you wish to find a location, simply click the target name at the menu. ^^Notes menu is removed due to hardcoded limitations, its being used for additional features. ^^If you require a tip for the Main Quest, you can find it in Camp, I implore you to explore everything in the Camp & Reports menu at your own pace.^^*Overworld Hotkeys*^1. Useful information: ESC^2. Fast forward time = Spacebar + CTRL^^*Diplomacy*^If you wish to attempt to persuade your faction to attack a specific castle, right click it then left click on (Set Map Marker), afterwards go to Reports --> Attend Faction Meeting, then suggest (Attack the Castle). Note that map marker can be used for more than attacking, its also used for quests, trading, and multiple other features.^^You can suggest as well as vote on proposals within Reports --> Attend faction meeting.^^*Recruitment*^There are 2 methods for recruitment within a fief, you may start either start the process and administrate it yourself or leave it to be handled by one of your troops, the latter of which is less efficient recruitment wise, however delegating the supervision of the process to one of your troops frees you to do whatever you wish.^^You may also hire volunteers immediatly, they cost denars however they are viable for hunting down small parties. Such as bandits & sea raiders for instance. Huge levy armies are inefficient in fighting small bands, as the bands are much smaller and thus more nimble, if you try to use a large army against a small band, only a portion of your army will be able to participate in the battle.^^*Battles*^You can control troops by clicking on the minimap after opening the Command Menu.   ^^1. Activate Command Menu = V key. ^^2. Delegate or Charge = T key^^3. Click on enemy army flag within Command Menu = Track and attack enemy^^4. Right click on allied army flag = Back them up^^5. Left click on map = Move^^6. Right click on map = Attack & move^^7. Comma = Encourage allies^^Retreat: Tab^^*Army mechanics*^Armies are infulenced by troops within parties. The higher the tier a troop is the less of them there will be. Upgrading your troops in your party screen will also upgrade more of your army itself to reflect the changes. Thus, your army is a unified count of your lesser party, whereby they reflect your party in a larger scale. (E.G: Having your entire party as Cavalry: 100 Cavalry troops for example + 8000 army in your party will make your entire army 100% Cavalry.)^^ Armies greatly benefit from a good commander whom upgrades them as well as equips them with better equipment through fiefs. An unupgraded/uneqipped army will have a tough time against an army that has Improved armor, weaponry, and so on. Especially in Field Battles.",
    "none",
    [
	],
    [
	
	
      ("choice_back_to_camp",[],"Got it, I'll come back to Camp (bottom left) and click on Notes & Hotkeys if I need to read this again.",
       [
(jump_to_menu, "mnu_wm_pst_map_return"),
	(eq, "$randomize_skills_fired", 0), #
	(assign, "$randomize_skills_fired", 1),
	
	#Add gear
		#Is player starting as a lord?
		(try_begin),
		(eq, "$r_player_class", 3),
		(eq, "$player_noble", 1),
		#Raising skills
		(troop_raise_attribute, "trp_player",0,13), #Add 13 extra points, so 7 total points excluding other benefits.#
	    (store_random_in_range, ":4_to_6", 4, 7),
        (troop_raise_skill, "trp_player",skl_riding,":4_to_6"), #3 Def
		(troop_raise_skill, "trp_player", skl_shield,":4_to_6"),
        (troop_raise_skill, "trp_player", skl_power_draw,":4_to_6"),
		#Raising skills end
		(call_script, "script_equip_royals", "trp_player"),

		
		
		(try_end),
		#Find faction player is part of
		#Equip gear depending on faction (if any)
		#Maybe equip monarch's armor if taking over
		#Take items from a random pool of lord(s) armor.
	#End add gear
	
	
			#Enhance skills begin
			(store_random_in_range, ":randomize_tactics", 1, 7),
			(store_random_in_range, ":randomize_leadership", 1, 7),
			(store_random_in_range, ":randomize_strategy", 1, 7),
			(store_random_in_range, ":randomize_naval", 1, 7),
			(troop_set_slot, "trp_player", 28, ":randomize_tactics"), #Tactics
			(troop_set_slot, "trp_player", 29, ":randomize_leadership"), #Leadership
			(troop_set_slot, "trp_player", 30, ":randomize_strategy"), #Strategy
			(troop_set_slot, "trp_player", 31, ":randomize_naval"), #Naval
			(display_message, "@Your tactics, leadership, strategy, naval & policy traits have been randomized to create a fresh experience.", 0x0000ff00),
			
			#V2
			(store_random_in_range, ":randomize_1", 1, 7),
			(store_random_in_range, ":randomize_2", 1, 7),
			(store_random_in_range, ":randomize_3", 1, 7),
			(store_random_in_range, ":randomize_4", 1, 7),
			(store_random_in_range, ":randomize_5", 1, 7),
			(store_random_in_range, ":randomize_6", 1, 7),
			(store_random_in_range, ":randomize_7", 1, 7),
					(troop_set_slot, "trp_player", 35, ":randomize_1"),
					(troop_set_slot, "trp_player", 36, ":randomize_2"),
					(troop_set_slot, "trp_player", 37, ":randomize_3"),
					(troop_set_slot, "trp_player", 38, ":randomize_4"),
					(troop_set_slot, "trp_player", 39, ":randomize_5"),
					(troop_set_slot, "trp_player", 40, ":randomize_6"),
					(troop_set_slot, "trp_player", 41, ":randomize_7"),
			#Adventure traits end
			
			
			(store_random_in_range, ":cf", 0, 2),
			(store_random_in_range, ":bs", 0, 2),
			(store_random_in_range, ":lure", 0, 2),
			(store_random_in_range, ":ambush", 0, 2),
			(store_random_in_range, ":submerge", 0, 2),
			(store_random_in_range, ":firework", 0, 2),
			(store_random_in_range, ":fallrock", 0, 2),
			(store_random_in_range, ":opengate", 0, 2),
			(store_random_in_range, ":infiltration", 0, 2),
			(store_random_in_range, ":sideatt", 0, 2),
			(store_random_in_range, ":backatt", 0, 2),
			(store_random_in_range, ":encamp", 0, 2),
			(store_random_in_range, ":lionheart", 0, 2),
			(store_random_in_range, ":pincer", 0, 2),
			(store_random_in_range, ":mangudai", 0, 2),
			(store_random_in_range, ":briver", 0, 2),
			(store_random_in_range, ":8door", 0, 2),
			
			#Policy
			(store_random_in_range, ":tax", 0, 6),
			(store_random_in_range, ":supply", 0, 6),
			(store_random_in_range, ":trade", 0, 6),
			(store_random_in_range, ":frugal", 0, 6),
			(store_random_in_range, ":ships_management", 0, 6),
			(store_random_in_range, ":lascivious", 0, 6),
			(store_random_in_range, ":tracker", 0, 6),
			(assign, "$policy_tax_collect", ":tax"),
			(assign, "$policy_supply_manage", ":supply"),
			(assign, "$policy_trade_plan", ":trade"),
			(assign, "$policy_frugal", ":frugal"),
			(assign, "$policy_ship_manage", ":ships_management"),
			(assign, "$policy_lascivious", ":lascivious"),
			(assign, "$policy_tracker", ":tracker"),
			#Policy
			


			(try_begin),
			(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_confuse", ":cf"),
			(eq, ":cf", 1),
			(display_message, "@Your character knows how to confuse.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_blocking_supply", ":bs"),
						(eq, ":bs", 1),
			(display_message, "@Your character knows how to block supplies efficiently.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_lure", ":lure"),
			(eq, ":lure", 1),
			(display_message, "@Your character knows how to lure.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_ambush", ":ambush"),
						(eq, ":ambush", 1),
			(display_message, "@Your character knows how to ambush.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_submerge", ":submerge"),
									(eq, ":submerge", 1),
			(display_message, "@Your character knows how to drown armies.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_firework", ":firework"),
									(eq, ":firework", 1),
			(display_message, "@Your character knows how to set fire to forests.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_fallrock", ":fallrock"),
									(eq, ":fallrock", 1),
			(display_message, "@Your character knows how to use boulders to his advantage.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_opengate", ":opengate"),
									(eq, ":opengate", 1),
			(display_message, "@Your character has contact with spies to open gates without being caught.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_infiltration", ":infiltration"),
									(eq, ":infiltration", 1),
			(display_message, "@Your character knows how to infiltrate.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_sideatt", ":sideatt"),
												(eq, ":sideatt", 1),
			(display_message, "@Your character knows how to delegate units to attack from the side.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_backatt", ":backatt"),
															(eq, ":backatt", 1),
			(display_message, "@Your character knows how to delegate units to attack from the back.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_encamp", ":encamp"),
				(eq, ":encamp", 1),
			(display_message, "@Your character knows how to build a small fortification.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_lionheart", ":lionheart"),
							(eq, ":lionheart", 1),
			(display_message, "@Your character is able to withstand damage at the cost of his own troops health and morale. (Lionheart)", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_pincer", ":pincer"),
							(eq, ":pincer", 1),
			(display_message, "@Your character knows how to use the Pincer field strategy.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_mangudai", ":mangudai"),
										(eq, ":mangudai", 1),
			(display_message, "@Your character knows how to use the mangudai field strategy.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_briver", ":briver"),
										(eq, ":briver", 1),
			(display_message, "@Your character knows how to use the river field strategy.", 0x00EEE8AA),
			(try_end),
						(try_begin),
						(store_random_in_range, ":randomize_chance_strategies", 1, 10),
			(eq, ":randomize_chance_strategies", 1),
			(assign, "$bt_st_8door", ":8door"),
										(eq, ":8door", 1),
			(display_message, "@Your character knows how to build a fortress.", 0x00EEE8AA),
			(try_end),
			#Enhance skills end

	
	#(display_message, "@Notes: ^Notes menu is removed due to hardcode limitations, its being used for additional features. ^If you need a tip for the Main Quest, you can find it in Camp, I implore you to explore everything in the Camp & Reports menu at your own pace.^If you wish to attempt to persuade your faction to attack a specific castle, right click it then left click on (Set Map Marker), afterwards go to Reports --> Attend Faction Meeting, then suggest (Attack the Castle), note that map marker can be used for more than attacking, its also used for quests, trading, and multiple other features. ^There are 2 methods for recruiting in a fief, you may either start the recruitment for war preparation's and administrate the process, or leave it to be handled by one of your troops, the latter of which is less efficient but allows you to run around and adventure while your troops recruit for your army.^You may also hire volunteers immediatly, they cost money but they are great for hunting down small parties, such as bandits, sea raiders, huge levy armies are inefficient in fighting small bands, as the bands are much smaller and faster, if you try to use a large army against a band, only a couple of them will be able to participate in the battle.^If you wish to find a location, simply click the target name at the menu.^You can control troops by clicking on the minimap after opening the Command Menu.^Some skills were moved to the Trait menu in Camp, there are additional skills, such as Policy, Battle & Adventure skills, all upgradeable within the Camp & Report menus.", 0x00EEE8AA),
	#(display_message, "@Overworld Hotkeys: ^1. Useful information: ESC^2. Fast forward time = Spacebar + CTRL", 0x00931124),
	#(display_message, "@Battle Hotkeys: ^^1. Activate Command Menu = V key. ^^2. Delegate or Charge = T key^^3. Click on enemy army flag within Command Menu = Track and attack enemy^4. Right click on allied army flag = Back them up^^5. Left click on map = Move^^6. Right click on map = Attack & move^7. Skip battle: Tab", 0x00abc904),
        ]
       ),
      ]
  ),
	
	
	    #####Wounds OSP Begin
	  ( "death_game_over",menu_text_color(0xFFFF2222),#test
      #( "death_game_over",mnf_scale_picture|menu_text_color(0xFFFF2222),#test
          "You have been mortally wounded, your death certain. It is already too late as this dawns upon you - the world seems to grow dim, the sounds seem distant and fading. Only you know your last thought - your greatest joy, or perhaps your deepest regret.", ### sorry, translate "you are dead !"
          "none",
         [                         
          (set_background_mesh, "mesh_pic_mort"),
          (music_set_situation, 0),     
          (play_sound, "snd_death"),
          (assign, "$game_death", 0),       
         ],
         [
           ("end",[],"This is it.",             
            [
         (change_screen_quit),             
            ]),
     ]
   ), 
   #####Wounds OSP End
	
	
	#####Hunger OSP Begin & Hardcore mode, Wounded OSP Begin
  ("hungry_report",0,
   "{s1}^^^{s4}^^{s6}^^{s8}",
   "none",
   [   
   (eq, "$hardcore_mode", 1), #Added
	#(str_clear, s1),
    (str_clear, s4),
    (str_clear, s6),   
    (str_clear, s8),
##hunger mod reports
#    (try_begin),
#        (eq, "$malus_de_faim", 0),
#        (lt, "$malus_de_faim", 1),   
#        (str_store_string, s3, "@I'm satiated. (No Debuffs)"),
#      (else_try),   
#       # (eq, "$malus_de_faim", 1),
#       #(lt, "$malus_de_faim", 0),   
#        (str_store_string, s3, "@I'm starving! *Penalty: -9 STR/AGI -6*"),#
#    (try_end),
#    (str_store_string, s1, "@Hunger Status:^{s3}"),
#wounds/death mod report azqs
    (try_begin),
      (eq, "$blesse_a_jambe", 0),
      (lt, "$blesse_a_jambe", 1),   
        (str_store_string, s9, "@My legs are OK."),
      (else_try),   
        (str_store_string, s9, "@My legs are injured! *Penalty: -1 SPD/AGI -1*"),   
    (try_end),
    (str_store_string, s8, "@Legs: {s9}"),
#
 
    (try_begin),
      (eq, "$blesse_au_bras", 0),
        (lt, "$blesse_au_bras", 1),   
        (str_store_string, s7, "@My arms are OK."),
      (else_try),
        (str_store_string, s7, "@My arms are injured! *Penalty: -3 STR/AGI -4*"),   
    (try_end),
    (str_store_string, s6, "@Arms: {s7}"),   

#
    (try_begin),
      (eq, "$blesse_a_tete", 0),
      (lt, "$blesse_a_tete", 1),   
    (str_store_string, s5, "@My head is OK."),
      (else_try),
        (str_store_string, s5, "@I have a concussion! *Penalty: -1/ INT -4/ CHA -5/ EQUIT/ -1*"),   
    (try_end),
    (str_store_string, s4, "@Head: {s5}"), 
   
    ],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),
		
		
		#####Hunger OSP Begin & Hardcore mode, Wounded OSP Begin
]