from header_meshes import *

####################################################################################################################
#  Each mesh record contains the following fields:
#  1) Mesh id: used for referencing meshes in other files. The prefix mesh_ is automatically added before each mesh id.
#  2) Mesh flags. See header_meshes.py for a list of available flags
#  3) Mesh resource name: Resource name of the mesh
#  4) Mesh translation on x axis: Will be done automatically when the mesh is loaded
#  5) Mesh translation on y axis: Will be done automatically when the mesh is loaded
#  6) Mesh translation on z axis: Will be done automatically when the mesh is loaded
#  7) Mesh rotation angle over x axis: Will be done automatically when the mesh is loaded
#  8) Mesh rotation angle over y axis: Will be done automatically when the mesh is loaded
#  9) Mesh rotation angle over z axis: Will be done automatically when the mesh is loaded
#  10) Mesh x scale: Will be done automatically when the mesh is loaded
#  11) Mesh y scale: Will be done automatically when the mesh is loaded
#  12) Mesh z scale: Will be done automatically when the mesh is loaded
####################################################################################################################

meshes = [
	("pic_bandits", 0, "pic_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_mb_warrior_1", 0, "pic_mb_warrior_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_messenger", 0, "pic_messenger", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_prisoner_man", 0, "pic_prisoner_man", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_prisoner_fem", 0, "pic_prisoner_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_prisoner_wilderness", 0, "pic_prisoner_wilderness", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_siege_sighted", 0, "pic_siege_sighted", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_siege_sighted_fem", 0, "pic_siege_sighted_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_camp", 0, "pic_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_payment", 0, "pic_payment", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_escape_1", 0, "pic_escape_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_escape_1_fem", 0, "pic_escape_1_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_victory", 0, "pic_victory", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_defeat", 0, "pic_defeat", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wounded", 0, "pic_wounded", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wounded_fem", 0, "pic_wounded_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_steppe_bandits", 0, "pic_steppe_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_mountain_bandits", 0, "pic_mountain_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_sea_raiders", 0, "pic_sea_raiders", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_deserters", 0, "pic_deserters", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_forest_bandits", 0, "pic_forest_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_cattle", 0, "pic_cattle", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_looted_village", 0, "pic_looted_village", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_village_p", 0, "pic_village_p", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_village_s", 0, "pic_village_s", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_village_w", 0, "pic_village_w", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_recruits", 0, "pic_recruits", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_swadian", 0, "pic_arms_swadian", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_castle1", 0, "pic_castle1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_castledes", 0, "pic_castledes", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_castlesnow", 0, "pic_castlesnow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_charge", 0, "pic_charge", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_khergit", 0, "pic_khergit", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_nord", 0, "pic_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_rhodock", 0, "pic_rhodock", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_sally_out", 0, "pic_sally_out", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_siege_attack", 0, "pic_siege_attack", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_swad", 0, "pic_swad", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_town1", 0, "pic_town1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_towndes", 0, "pic_towndes", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_townriot", 0, "pic_townriot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_townsnow", 0, "pic_townsnow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_vaegir", 0, "pic_vaegir", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_villageriot", 0, "pic_villageriot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_sarranid_encounter", 0, "pic_sarranid_encounter", 0, 0, 0, 0, 0, 0, 1, 1, 1),

		#####Wounded OSP Begin
	  ("pic_mort", 0, "pic_mort", 0, 0, 0, 0, 0, 0, 1, 1, 1), 
	#####Wounded OSP End
	
	("mp_score_a", 0, "mp_score_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_score_b", 0, "mp_score_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("portrait_blend_out", 0, "portrait_blend_out", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("load_window", 0, "load_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("checkbox_off", render_order_plus_1, "checkbox_off", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("checkbox_on", render_order_plus_1, "checkbox_on", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("white_plane", 0, "white_plane", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("white_dot", 0, "white_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("player_dot", 0, "player_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_infantry", 0, "flag_infantry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_archers", 0, "flag_archers", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_cavalry", 0, "flag_cavalry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("inv_slot", 0, "inv_slot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ingame_menu", 0, "mp_ingame_menu", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_left", 0, "mp_inventory_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_right", 0, "mp_inventory_right", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_choose", 0, "mp_inventory_choose", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_glove", 0, "mp_inventory_slot_glove", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_horse", 0, "mp_inventory_slot_horse", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_armor", 0, "mp_inventory_slot_armor", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_helmet", 0, "mp_inventory_slot_helmet", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_boot", 0, "mp_inventory_slot_boot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_empty", 0, "mp_inventory_slot_empty", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_equip", 0, "mp_inventory_slot_equip", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_left_arrow", 0, "mp_inventory_left_arrow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_right_arrow", 0, "mp_inventory_right_arrow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_main", 0, "mp_ui_host_main", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_1", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_2", 0, "mp_ui_host_maps_a2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_3", 0, "mp_ui_host_maps_c", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_4", 0, "mp_ui_host_maps_ruinedf", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_5", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_6", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_7", 0, "mp_ui_host_maps_fieldby", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_8", 0, "mp_ui_host_maps_castle2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_9", 0, "mp_ui_host_maps_snovyv", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_10", 0, "mp_ui_host_maps_castle3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_11", 0, "mp_ui_host_maps_c1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_12", 0, "mp_ui_host_maps_c2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_13", 0, "mp_ui_host_maps_c3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_randomp", 0, "mp_ui_host_maps_randomp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_randoms", 0, "mp_ui_host_maps_randoms", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_command_panel", 0, "mp_ui_command_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_command_border_l", 0, "mp_ui_command_border_l", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_command_border_r", 0, "mp_ui_command_border_r", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_welcome_panel", 0, "mp_ui_welcome_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_sw", 0, "flag_project_sw", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_vg", 0, "flag_project_vg", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_kh", 0, "flag_project_kh", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_nd", 0, "flag_project_nd", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_rh", 0, "flag_project_rh", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_sr", 0, "flag_project_sr", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_projects_end", 0, "0", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_sw_miss", 0, "flag_project_sw_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_vg_miss", 0, "flag_project_vg_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_kh_miss", 0, "flag_project_kh_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_nd_miss", 0, "flag_project_nd_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_rh_miss", 0, "flag_project_rh_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_sr_miss", 0, "flag_project_sr_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_misses_end", 0, "0", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("color_picker", 0, "color_picker", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("custom_map_banner_01", 0, "custom_map_banner_01", 0, 0, 0, -90, 0, 90, 1, 1, 1),

	("custom_map_banner_02", 0, "custom_map_banner_02", 0, 0, 0, -90, 0, 90, 1, 1, 1),

	("custom_map_banner_03", 0, "custom_map_banner_03", 0, 0, 0, -90, 0, 90, 1, 1, 1),

	("custom_banner_01", 0, "custom_banner_01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("custom_banner_02", 0, "custom_banner_02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("custom_banner_bg", 0, "custom_banner_bg", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg01", 0, "custom_banner_fg01", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg02", 0, "custom_banner_fg02", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg03", 0, "custom_banner_fg03", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg04", 0, "custom_banner_fg04", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg05", 0, "custom_banner_fg05", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg06", 0, "custom_banner_fg06", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg07", 0, "custom_banner_fg07", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg08", 0, "custom_banner_fg08", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg09", 0, "custom_banner_fg09", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg10", 0, "custom_banner_fg10", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg11", 0, "custom_banner_fg11", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg12", 0, "custom_banner_fg12", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg13", 0, "custom_banner_fg13", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg14", 0, "custom_banner_fg14", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg15", 0, "custom_banner_fg15", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg16", 0, "custom_banner_fg16", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg17", 0, "custom_banner_fg17", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg18", 0, "custom_banner_fg18", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg19", 0, "custom_banner_fg19", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg20", 0, "custom_banner_fg20", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg21", 0, "custom_banner_fg21", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg22", 0, "custom_banner_fg22", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg23", 0, "custom_banner_fg23", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_01", 0, "custom_banner_charge_01", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_02", 0, "custom_banner_charge_02", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_03", 0, "custom_banner_charge_03", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_04", 0, "custom_banner_charge_04", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_05", 0, "custom_banner_charge_05", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_06", 0, "custom_banner_charge_06", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_07", 0, "custom_banner_charge_07", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_08", 0, "custom_banner_charge_08", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_09", 0, "custom_banner_charge_09", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_10", 0, "custom_banner_charge_10", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_11", 0, "custom_banner_charge_11", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_12", 0, "custom_banner_charge_12", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_13", 0, "custom_banner_charge_13", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_14", 0, "custom_banner_charge_14", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_15", 0, "custom_banner_charge_15", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_16", 0, "custom_banner_charge_16", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_17", 0, "custom_banner_charge_17", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_18", 0, "custom_banner_charge_18", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_19", 0, "custom_banner_charge_19", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_20", 0, "custom_banner_charge_20", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_21", 0, "custom_banner_charge_21", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_22", 0, "custom_banner_charge_22", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_23", 0, "custom_banner_charge_23", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_24", 0, "custom_banner_charge_24", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_25", 0, "custom_banner_charge_25", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_26", 0, "custom_banner_charge_26", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_27", 0, "custom_banner_charge_27", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_28", 0, "custom_banner_charge_28", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_29", 0, "custom_banner_charge_29", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_30", 0, "custom_banner_charge_30", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_31", 0, "custom_banner_charge_31", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_32", 0, "custom_banner_charge_32", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_33", 0, "custom_banner_charge_33", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_34", 0, "custom_banner_charge_34", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_35", 0, "custom_banner_charge_35", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_36", 0, "custom_banner_charge_36", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_37", 0, "custom_banner_charge_37", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_38", 0, "custom_banner_charge_38", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_39", 0, "custom_banner_charge_39", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_40", 0, "custom_banner_charge_40", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_41", 0, "custom_banner_charge_41", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_42", 0, "custom_banner_charge_42", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_43", 0, "custom_banner_charge_43", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_44", 0, "custom_banner_charge_44", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_45", 0, "custom_banner_charge_45", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_46", 0, "custom_banner_charge_46", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_custom_banner", 0, "tableau_mesh_custom_banner", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_custom_banner_square", 0, "tableau_mesh_custom_banner_square", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_custom_banner_tall", 0, "tableau_mesh_custom_banner_tall", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_custom_banner_short", 0, "tableau_mesh_custom_banner_short", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_1", 0, "tableau_mesh_shield_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_2", 0, "tableau_mesh_shield_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_3", 0, "tableau_mesh_shield_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_4", 0, "tableau_mesh_shield_round_4", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_5", 0, "tableau_mesh_shield_round_5", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_small_round_1", 0, "tableau_mesh_shield_small_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_small_round_2", 0, "tableau_mesh_shield_small_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_small_round_3", 0, "tableau_mesh_shield_small_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_kite_1", 0, "tableau_mesh_shield_kite_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_kite_2", 0, "tableau_mesh_shield_kite_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_kite_3", 0, "tableau_mesh_shield_kite_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_kite_4", 0, "tableau_mesh_shield_kite_4", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_heater_1", 0, "tableau_mesh_shield_heater_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_heater_2", 0, "tableau_mesh_shield_heater_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_pavise_1", 0, "tableau_mesh_shield_pavise_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_pavise_2", 0, "tableau_mesh_shield_pavise_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("heraldic_armor_bg", 0, "heraldic_armor_bg", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_heraldic_armor_a", 0, "tableau_mesh_heraldic_armor_new_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_armor_b", 0, "tableau_mesh_heraldic_armor_new_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_armor_c", 0, "tableau_mesh_heraldic_armor_new_c", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_armor_d", 0, "tableau_mesh_heraldic_armor_new_d", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("outer_terrain_plain_1", 0, "0", -90, 0, 0, 0, 0, 0, 1, 1, 1),

	("banner_a01", 0, "banner_a01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a02", 0, "banner_a02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a03", 0, "banner_a03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a04", 0, "banner_a04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a05", 0, "banner_a05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a06", 0, "banner_a06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a07", 0, "banner_a07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a08", 0, "banner_a08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a09", 0, "banner_a09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a10", 0, "banner_a10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a11", 0, "banner_a11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a12", 0, "banner_a12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a13", 0, "banner_a13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a14", 0, "banner_a14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a15", 0, "banner_a15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a16", 0, "banner_a16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a17", 0, "banner_a17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a18", 0, "banner_a18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a19", 0, "banner_a19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a20", 0, "banner_a20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a21", 0, "banner_a21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b01", 0, "banner_b01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b02", 0, "banner_b02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b03", 0, "banner_b03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b04", 0, "banner_b04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b05", 0, "banner_b05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b06", 0, "banner_b06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b07", 0, "banner_b07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b08", 0, "banner_b08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b09", 0, "banner_b09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b10", 0, "banner_b10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b11", 0, "banner_b11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b12", 0, "banner_b12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b13", 0, "banner_b13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b14", 0, "banner_b14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b15", 0, "banner_b15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b16", 0, "banner_b16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b17", 0, "banner_b17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b18", 0, "banner_b18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b19", 0, "banner_b19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b20", 0, "banner_b20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b21", 0, "banner_b21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c01", 0, "banner_c01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c02", 0, "banner_c02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c03", 0, "banner_c03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c04", 0, "banner_c04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c05", 0, "banner_c05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c06", 0, "banner_c06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c07", 0, "banner_c07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c08", 0, "banner_c08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c09", 0, "banner_c09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c10", 0, "banner_c10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c11", 0, "banner_c11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c12", 0, "banner_c12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c13", 0, "banner_c13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c14", 0, "banner_c14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c15", 0, "banner_c15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c16", 0, "banner_c16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c17", 0, "banner_c17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c18", 0, "banner_c18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c19", 0, "banner_c19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c20", 0, "banner_c20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c21", 0, "banner_c21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d01", 0, "banner_d01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d02", 0, "banner_d02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d03", 0, "banner_d03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d04", 0, "banner_d04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d05", 0, "banner_d05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d06", 0, "banner_d06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d07", 0, "banner_d07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d08", 0, "banner_d08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d09", 0, "banner_d09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d10", 0, "banner_d10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d11", 0, "banner_d11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d12", 0, "banner_d12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d13", 0, "banner_d13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d14", 0, "banner_d14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d15", 0, "banner_d15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d16", 0, "banner_d16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d17", 0, "banner_d17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d18", 0, "banner_d18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d19", 0, "banner_d19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d20", 0, "banner_d20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d21", 0, "banner_d21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e01", 0, "banner_e01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e02", 0, "banner_e02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e03", 0, "banner_e03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e04", 0, "banner_e04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e05", 0, "banner_e05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e06", 0, "banner_e06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e07", 0, "banner_e07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e08", 0, "banner_e08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e09", 0, "banner_e09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e10", 0, "banner_e10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e11", 0, "banner_e11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e12", 0, "banner_e12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e13", 0, "banner_e13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e14", 0, "banner_e14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e15", 0, "banner_e15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e16", 0, "banner_e16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e17", 0, "banner_e17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e18", 0, "banner_e18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e19", 0, "banner_e19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e20", 0, "banner_e20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e21", 0, "banner_e21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f01", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f02", 0, "banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f03", 0, "banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f04", 0, "banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f05", 0, "banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f06", 0, "banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f07", 0, "banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f08", 0, "banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f09", 0, "banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f10", 0, "banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f11", 0, "banner_f11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f12", 0, "banner_f12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f13", 0, "banner_f13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f14", 0, "banner_f14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f15", 0, "banner_f15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f16", 0, "banner_f16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f17", 0, "banner_f17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f18", 0, "banner_f18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f19", 0, "banner_f19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f20", 0, "banner_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h01", 0, "banner_h01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h02", 0, "banner_h02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h03", 0, "banner_h03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h04", 0, "banner_h04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h05", 0, "banner_h05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h06", 0, "banner_h06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h07", 0, "banner_h07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h08", 0, "banner_h08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h09", 0, "banner_h09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h10", 0, "banner_h10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h11", 0, "banner_h11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h12", 0, "banner_h12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h13", 0, "banner_h13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h14", 0, "banner_h14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h15", 0, "banner_h15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h16", 0, "banner_h16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h17", 0, "banner_h17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h18", 0, "banner_h18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h19", 0, "banner_h19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h20", 0, "banner_h20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h21", 0, "banner_h21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i01", 0, "banner_i01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i02", 0, "banner_i02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i03", 0, "banner_i03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i04", 0, "banner_i04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i05", 0, "banner_i05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i06", 0, "banner_i06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i07", 0, "banner_i07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i08", 0, "banner_i08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i09", 0, "banner_i09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i10", 0, "banner_i10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i11", 0, "banner_i11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i12", 0, "banner_i12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i13", 0, "banner_i13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i14", 0, "banner_i14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i15", 0, "banner_i15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i16", 0, "banner_i16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i17", 0, "banner_i17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i18", 0, "banner_i18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i19", 0, "banner_i19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i20", 0, "banner_i20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i21", 0, "banner_i21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k01", 0, "banner_k01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k02", 0, "banner_k02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k03", 0, "banner_k03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k04", 0, "banner_k04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k05", 0, "banner_k05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k06", 0, "banner_k06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k07", 0, "banner_k07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k08", 0, "banner_k08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k09", 0, "banner_k09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k10", 0, "banner_k10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k11", 0, "banner_k11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k12", 0, "banner_k12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k13", 0, "banner_k13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k14", 0, "banner_k14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k15", 0, "banner_k15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k16", 0, "banner_k16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k17", 0, "banner_k17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k18", 0, "banner_k18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k19", 0, "banner_k19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k20", 0, "banner_k20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g01", 0, "banner_k01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g02", 0, "banner_k02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g03", 0, "banner_k03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g04", 0, "banner_k04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g05", 0, "banner_k05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g06", 0, "banner_k06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g07", 0, "banner_k07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g08", 0, "banner_k08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g09", 0, "banner_k09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g10", 0, "banner_k10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_a", 0, "banner_kingdom_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_b", 0, "banner_kingdom_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_c", 0, "banner_kingdom_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_d", 0, "banner_kingdom_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_e", 0, "banner_kingdom_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_f", 0, "banner_kingdom_f", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_g", 0, "banner_kingdom_g", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_h", 0, "banner_kingdom_h", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_i", 0, "banner_kingdom_i", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_j", 0, "banner_kingdom_j", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_k", 0, "banner_kingdom_k", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_l", 0, "banner_kingdom_l", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_ll", 0, "banner_kingdom_ll", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_m", 0, "banner_kingdom_m", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_n", 0, "banner_kingdom_n", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_o", 0, "banner_kingdom_o", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_p", 0, "banner_kingdom_p", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_q", 0, "banner_kingdom_q", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_r", 0, "banner_kingdom_r", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_s", 0, "banner_kingdom_s", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_t", 0, "banner_kingdom_t", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_u", 0, "banner_kingdom_u", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_v", 0, "banner_kingdom_v", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_w", 0, "banner_kingdom_w", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_x", 0, "banner_kingdom_x", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_y", 0, "banner_kingdom_y", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_z", 0, "banner_kingdom_z", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_2a", 0, "banner_kingdom_2a", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_2b", 0, "banner_kingdom_2b", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_2c", 0, "banner_kingdom_2c", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_2d", 0, "banner_kingdom_2d", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k21", 0, "banner_a15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a01", 0, "arms_a01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a02", 0, "arms_a02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a03", 0, "arms_a03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a04", 0, "arms_a04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a05", 0, "banner_a05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a06", 0, "arms_a06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a07", 0, "banner_a07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a08", 0, "arms_a08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a09", 0, "banner_a09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a10", 0, "banner_a10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a11", 0, "banner_a11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a12", 0, "arms_a12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a13", 0, "arms_a13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a14", 0, "banner_a14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a15", 0, "banner_f21", 0, 0, 0, -90, 0, 180, 1, 1, 1),

	("arms_a16", 0, "arms_a16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a17", 0, "arms_a17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a18", 0, "arms_a18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a19", 0, "arms_a19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a20", 0, "arms_a20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a21", 0, "arms_a21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b01", 0, "arms_b01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b02", 0, "arms_b02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b03", 0, "banner_b03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b04", 0, "banner_b04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b05", 0, "arms_b05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b06", 0, "arms_b06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b07", 0, "arms_b07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b08", 0, "arms_b08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b09", 0, "arms_b09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b10", 0, "arms_b10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b11", 0, "banner_b11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b12", 0, "banner_b12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b13", 0, "banner_b13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b14", 0, "arms_b14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b15", 0, "arms_b15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b16", 0, "arms_b16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b17", 0, "banner_b17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b18", 0, "arms_b18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b19", 0, "banner_b19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b20", 0, "arms_b20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b21", 0, "banner_b21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c01", 0, "arms_c01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c02", 0, "banner_c02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c03", 0, "banner_c03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c04", 0, "arms_c04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c05", 0, "banner_c05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c06", 0, "arms_c06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c07", 0, "arms_c07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c08", 0, "banner_c08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c09", 0, "banner_c09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c10", 0, "arms_c10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c11", 0, "banner_c11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c12", 0, "arms_c12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c13", 0, "arms_c13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c14", 0, "arms_c14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c15", 0, "banner_c15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c16", 0, "arms_c16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c17", 0, "banner_c17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c18", 0, "banner_c18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c19", 0, "arms_c19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c20", 0, "banner_c20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c21", 0, "banner_c21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d01", 0, "banner_d01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d02", 0, "arms_d02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d03", 0, "arms_d03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d04", 0, "arms_d04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d05", 0, "banner_d05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d06", 0, "arms_d06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d07", 0, "arms_d07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d08", 0, "arms_d08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d09", 0, "arms_d09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d10", 0, "banner_d10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d11", 0, "arms_d11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d12", 0, "arms_d12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d13", 0, "arms_d13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d14", 0, "arms_d14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d15", 0, "arms_d15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d16", 0, "arms_d16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d17", 0, "arms_d17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d18", 0, "arms_d18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d19", 0, "arms_d19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d20", 0, "arms_d20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d21", 0, "arms_d21", 0, 0, 0, -90, 0, 180, 1, 1, 1),

	("arms_e01", 0, "banner_e01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e02", 0, "arms_e02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e03", 0, "banner_e03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e04", 0, "banner_e04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e05", 0, "banner_e05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e06", 0, "banner_e06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e07", 0, "banner_e07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e08", 0, "banner_e08", 0, 0, 0, -90, 0, 180, 1, 1, 1),

	("arms_e09", 0, "banner_e09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e10", 0, "banner_e10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e11", 0, "banner_e11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e12", 0, "banner_e12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e13", 0, "banner_e13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e14", 0, "banner_e14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e15", 0, "banner_e15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e16", 0, "banner_e16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e17", 0, "banner_e17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e18", 0, "banner_e18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e19", 0, "banner_e19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e20", 0, "banner_e20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e21", 0, "banner_e21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f01", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f02", 0, "banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f03", 0, "banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f04", 0, "banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f05", 0, "banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f06", 0, "banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f07", 0, "banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f08", 0, "banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f09", 0, "banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f10", 0, "banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f11", 0, "banner_f11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f12", 0, "banner_f12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f13", 0, "banner_f13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f14", 0, "banner_f14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f15", 0, "banner_f15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f16", 0, "banner_f16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f17", 0, "banner_f17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f18", 0, "banner_f18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f19", 0, "banner_f19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f20", 0, "banner_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h01", 0, "banner_h01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h02", 0, "banner_h02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h03", 0, "banner_h03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h04", 0, "banner_h04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h05", 0, "banner_h05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h06", 0, "banner_h06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h07", 0, "banner_h07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h08", 0, "banner_h08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h09", 0, "banner_h09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h10", 0, "banner_h10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h11", 0, "banner_h11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h12", 0, "banner_h12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h13", 0, "banner_h13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h14", 0, "banner_h14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h15", 0, "banner_h15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h16", 0, "banner_h16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h17", 0, "banner_h17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h18", 0, "banner_h18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h19", 0, "banner_h19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h20", 0, "banner_h20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h21", 0, "banner_h21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i01", 0, "banner_i01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i02", 0, "banner_i02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i03", 0, "banner_i03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i04", 0, "banner_i04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i05", 0, "banner_i05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i06", 0, "banner_i06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i07", 0, "banner_i07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i08", 0, "banner_i08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i09", 0, "banner_i09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i10", 0, "banner_i10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i11", 0, "banner_i11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i12", 0, "banner_i12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i13", 0, "banner_i13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i14", 0, "banner_i14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i15", 0, "banner_i15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i16", 0, "banner_i16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i17", 0, "banner_i17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i18", 0, "banner_i18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i19", 0, "banner_i19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i20", 0, "banner_i20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i21", 0, "banner_i21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k01", 0, "banner_k01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k02", 0, "banner_k02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k03", 0, "banner_k03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k04", 0, "banner_k04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k05", 0, "banner_k05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k06", 0, "banner_k06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k07", 0, "banner_k07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k08", 0, "banner_k08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k09", 0, "banner_k09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k10", 0, "banner_k10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k11", 0, "banner_k11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k12", 0, "banner_k12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k13", 0, "banner_k13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k14", 0, "banner_k14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k15", 0, "banner_k15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k16", 0, "banner_k16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k17", 0, "banner_k17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k18", 0, "banner_k18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k19", 0, "banner_k19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k20", 0, "banner_k20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g01", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g02", 0, "banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g03", 0, "banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g04", 0, "banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g05", 0, "banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g06", 0, "banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g07", 0, "banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g08", 0, "banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g09", 0, "banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g10", 0, "banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_a", 0, "banner_kingdom_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_b", 0, "banner_kingdom_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_c", 0, "banner_kingdom_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_d", 0, "banner_kingdom_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_e", 0, "banner_kingdom_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_f", 0, "banner_kingdom_f", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_g", 0, "banner_kingdom_g", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_h", 0, "banner_kingdom_h", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_i", 0, "banner_kingdom_i", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_j", 0, "banner_kingdom_j", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_k", 0, "banner_kingdom_k", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_l", 0, "banner_kingdom_l", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_ll", 0, "banner_kingdom_ll", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_m", 0, "banner_kingdom_m", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_n", 0, "banner_kingdom_n", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_o", 0, "banner_kingdom_o", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_p", 0, "banner_kingdom_p", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_q", 0, "banner_kingdom_q", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_r", 0, "banner_kingdom_r", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_s", 0, "banner_kingdom_s", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_t", 0, "banner_kingdom_t", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_u", 0, "banner_kingdom_u", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_v", 0, "banner_kingdom_v", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_w", 0, "banner_kingdom_w", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_x", 0, "banner_kingdom_x", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_y", 0, "banner_kingdom_y", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_z", 0, "banner_kingdom_z", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_2a", 0, "banner_kingdom_2a", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_2b", 0, "banner_kingdom_2b", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_2c", 0, "banner_kingdom_2c", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_2d", 0, "banner_kingdom_2d", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k21", 0, "banner_a15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_a", 0, "banners_default_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_b", 0, "banners_default_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_c", 0, "banners_default_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_d", 0, "banners_default_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_e", 0, "banners_default_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("troop_label_banner", 0, "troop_label_banner", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("ui_kingdom_shield_1", 0, "ui_kingdom_shield_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_2", 0, "ui_kingdom_shield_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_3", 0, "ui_kingdom_shield_3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_4", 0, "ui_kingdom_shield_4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_5", 0, "ui_kingdom_shield_5", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_6", 0, "ui_kingdom_shield_6", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_7", 0, "ui_kingdom_shield_7", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_8", 0, "ui_kingdom_shield_8", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_9", 0, "ui_kingdom_shield_9", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_10", 0, "ui_kingdom_shield_10", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_11", 0, "ui_kingdom_shield_11", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_12", 0, "ui_kingdom_shield_12", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_13", 0, "ui_kingdom_shield_13", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_14", 0, "ui_kingdom_shield_14", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_15", 0, "ui_kingdom_shield_15", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_16", 0, "ui_kingdom_shield_16", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_17", 0, "ui_kingdom_shield_17", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_18", 0, "ui_kingdom_shield_18", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_19", 0, "ui_kingdom_shield_19", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_20", 0, "ui_kingdom_shield_20", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_21", 0, "ui_kingdom_shield_21", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_22", 0, "ui_kingdom_shield_22", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_23", 0, "ui_kingdom_shield_23", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_24", 0, "ui_kingdom_shield_24", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_25", 0, "ui_kingdom_shield_25", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_26", 0, "ui_kingdom_shield_26", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_27", 0, "ui_kingdom_shield_27", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_28", 0, "ui_kingdom_shield_28", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_29", 0, "ui_kingdom_shield_29", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_30", 0, "ui_kingdom_shield_30", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_31", 0, "ui_kingdom_shield_31", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_down", 0, "mouse_arrow_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_right", 0, "mouse_arrow_right", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_left", 0, "mouse_arrow_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_up", 0, "mouse_arrow_up", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_plus", 0, "mouse_arrow_plus", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_left_click", 0, "mouse_left_click", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_right_click", 0, "mouse_right_click", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("status_ammo_ready", 0, "status_ammo_ready", 0, 0, 0, 0, 0, 0, 1, 1, 1),

#  #Start main menu dust effect start animated main menu, if you decide to re-enable animated main menu, make sure to uncomment the crusaders_menu_meshes in module.ini, and re-add the 3 textures main_menu_move, main_menu_dust & main_menu_static, as well as the code for them in module_presentations & the resource file
#  ("main_menu_dust", 0, "main_menu_dust", 0, 0, 0, 0, 0, 0, 1, 1, 1), #Main menu dust effect
#  
#  ("main_menu_move_1", 0, "main_menu_move_1", 0, 0, 0, 0, 0, 0, 1, 1, 1), #Main menu animation
#  
#  ("main_menu_static", 0, "main_menu_static", 0, 0, 0, 0, 0, 0, 1, 1, 1), # Main menu static picture, in this case its the menu text only on the left side
#  #End animated main menu
  
  ("main_menu_background", 0, "main_menu_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1), #Not needed comment me out if using animated menu

  ("loading_background", 0, "load_screen_2", 0, 0, 0, 0, 0, 0, 1, 1, 1), #Only one loading screen used.

	("ui_quick_battle_a", 0, "ui_quick_battle_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("white_bg_plane_a", 0, "white_bg_plane_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_icon_infantry", 0, "cb_ui_icon_infantry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_icon_archer", 0, "cb_ui_icon_archer", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_icon_horseman", 0, "cb_ui_icon_horseman", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_main", 0, "cb_ui_main", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_01", 0, "cb_ui_maps_scene_01", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_02", 0, "cb_ui_maps_scene_02", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_03", 0, "cb_ui_maps_scene_03", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_04", 0, "cb_ui_maps_scene_04", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_05", 0, "cb_ui_maps_scene_05", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_06", 0, "cb_ui_maps_scene_06", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_07", 0, "cb_ui_maps_scene_07", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_08", 0, "cb_ui_maps_scene_08", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_09", 0, "cb_ui_maps_scene_09", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_14", 0, "mp_ui_host_maps_c4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_15", 0, "mp_ui_host_maps_c5", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	#("quit_adv", 0, "quit_adv", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	#("quit_adv_b", 0, "quit_adv_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_7", 0, "ui_kingdom_shield_7", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_rb", 0, "flag_project_rb", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_rb_miss", 0, "flag_project_rb_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_16", 0, "mp_ui_host_maps_d1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_17", 0, "mp_ui_host_maps_d2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_18", 0, "mp_ui_host_maps_d3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_19", 0, "mp_ui_host_maps_e2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_20", 0, "mp_ui_host_maps_e1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_mb_warrior_2", 0, "pic_mb_warrior_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_mb_warrior_3", 0, "pic_mb_warrior_3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_mb_warrior_4", 0, "pic_mb_warrior_4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_mercenary", 0, "pic_mercenary", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("facegen_board", 0, "facegen_board", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("status_background", 0, "status_background", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("status_health_bar", 0, "status_health_bar", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("game_log_window", 0, "game_log_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("restore_game_panel", 0, "restore_game_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("message_window", 0, "message_window", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("party_window_b", 0, "party_window_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("party_member_button", 0, "party_member_button", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("party_member_button_pressed", 0, "party_member_button_pressed", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("longer_button", 0, "longer_button", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("longer_button_down", 0, "longer_button_down", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("button_1", 0, "button1_up", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("button_1_down", 0, "button1_down", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("used_button", 0, "medium_button", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("used_button_down", 0, "medium_button_down", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("longer_button", 0, "longer_button", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("longer_button_down", 0, "longer_button_down", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("options_window", 0, "options_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("message_window", 0, "message_window", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("note_window", 0, "note_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("left_button", 0, "cb_ui_comp_arrow_l_d", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("left_button_down", 0, "cb_ui_comp_arrow_l_p", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("left_button_hl", 0, "cb_ui_comp_arrow_l_hl", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("right_button", 0, "cb_ui_comp_arrow_r_d", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("right_button_down", 0, "cb_ui_comp_arrow_r_p", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("right_button_hl", 0, "cb_ui_comp_arrow_r_hl", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("center_button", 0, "cb_ui_title_panel", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("drop_button", 0, "button_drop", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_down", 0, "button_drop_clicked", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_hl", 0, "button_drop_hl", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_child", 0, "button_drop_child", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_child_down", 0, "button_drop_child_clicked", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_child_hl", 0, "button_drop_child_hl", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("num_1", 0, "num_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_2", 0, "num_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_3", 0, "num_3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_4", 0, "num_4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_5", 0, "num_5", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_6", 0, "num_6", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_7", 0, "num_7", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_8", 0, "num_8", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_9", 0, "num_9", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_10", 0, "num_10", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_11", 0, "num_11", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_12", 0, "num_12", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_13", 0, "num_13", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_14", 0, "num_14", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_15", 0, "num_15", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_16", 0, "num_16", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_17", 0, "num_17", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_18", 0, "num_18", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_19", 0, "num_19", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_20", 0, "num_20", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_21", 0, "num_21", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_22", 0, "num_22", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_23", 0, "num_23", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_24", 0, "num_24", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_25", 0, "num_25", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_26", 0, "num_26", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_27", 0, "num_27", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_28", 0, "num_28", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_29", 0, "num_29", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_30", 0, "num_30", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_31", 0, "num_31", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_32", 0, "num_32", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_33", 0, "num_33", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_34", 0, "num_34", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_35", 0, "num_35", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_36", 0, "num_36", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_37", 0, "num_37", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_38", 0, "num_38", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_39", 0, "num_39", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_40", 0, "num_40", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_41", 0, "num_41", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_42", 0, "num_42", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_43", 0, "num_43", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_44", 0, "num_44", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_45", 0, "num_45", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_46", 0, "num_46", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_47", 0, "num_47", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("num_48", 0, "num_48", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("message_window", 0, "message_window", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("face_gen_window", 0, "face_gen_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("order_frame", 0, "order_frame", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_early_transitional_heraldic_banner", 0, "tableau_mesh_early_transitional_heraldic_banner", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_early_transitional_heraldic", 0, "tableau_mesh_early_transitional_heraldic", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_samurai_heraldic_flag", 0, "tableau_mesh_samurai_nobori_heraldic", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_banner_spear", 0, "tableau_mesh_banner_spear", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("invisi_st_plane_fullsc", 0, "invisi_st_plane_fullsc", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("bt_flag_1", 0, "bt_flag_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("bt_flag_2", 0, "bt_flag_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("bt_flag_3", 0, "bt_flag_3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_crossbow", 0, "pic_bt_crossbow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_shield", 0, "pic_bt_shield", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_horse_archer", 0, "pic_bt_horse_archer", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_twohand", 0, "pic_bt_twohand", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_bow", 0, "pic_bt_bow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_horse", 0, "pic_bt_horse", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_musket", 0, "pic_bt_musket", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_leader", 0, "pic_bt_leader", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("bt_cion_tier1", 0, "bt_cion_tier1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("bt_cion_tier2", 0, "bt_cion_tier2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("bt_cion_tier3", 0, "bt_cion_tier3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("bt_cion_tier4", 0, "bt_cion_tier4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("bt_cion_tier5", 0, "bt_cion_tier5", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("bt_cion_tier6", 0, "bt_cion_tier6", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_charge_auto", 0, "pic_bt_charge_auto", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_hold", 0, "pic_bt_hold", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_followme", 0, "pic_bt_followme", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_unite", 0, "pic_bt_unite", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_divide", 0, "pic_bt_divide", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_advan", 0, "pic_bt_advan", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_fall", 0, "pic_bt_fall", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_holdfire", 0, "pic_bt_holdfire", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_anyw", 0, "pic_bt_anyw", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_clicked", 0, "pic_bt_clicked", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bt_return", 0, "pic_bt_return", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_camp_meet", 0, "pic_camp_meet", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_meetlady", 0, "pic_meetlady", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_meetlady2", 0, "pic_meetlady2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_meetlady3", 0, "pic_meetlady3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_0", 0, "1pic_ruin0", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_1", 0, "1pic_ruin1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_2", 0, "1pic_ruin2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_3", 0, "1pic_ruin3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_4", 0, "1pic_ruin4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_5", 0, "1pic_ruin5", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_6", 0, "1pic_ruin6", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_7", 0, "1pic_ruin7", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_8", 0, "1pic_ruin8", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_9", 0, "1pic_ruin9", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_10", 0, "1pic_ruin10", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_11", 0, "1pic_ruin11", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_12", 0, "1pic_ruin12", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_13", 0, "1pic_ruin13", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_14", 0, "1pic_ruin14", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_15", 0, "1pic_ruin15", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_16", 0, "1pic_ruin16", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_17", 0, "1pic_ruin17", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_18", 0, "1pic_ruin18", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_19", 0, "1pic_ruin19", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_20", 0, "1pic_ruin20", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_21", 0, "1pic_ruin21", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_22", 0, "1pic_ruin22", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_23", 0, "1pic_ruin23", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_24", 0, "1pic_ruin24", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_25", 0, "1pic_ruin25", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_26", 0, "1pic_ruin26", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_27", 0, "1pic_ruin27", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_28", 0, "1pic_ruin28", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_29", 0, "1pic_ruin29", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_30", 0, "1pic_ruin30", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_31", 0, "1pic_ruin31", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_32", 0, "1pic_ruin32", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_33", 0, "1pic_ruin33", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_34", 0, "1pic_ruin34", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_35", 0, "1pic_ruin35", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_36", 0, "1pic_ruin36", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_37", 0, "1pic_ruin37", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_38", 0, "1pic_ruin38", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_39", 0, "1pic_ruin39", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_40", 0, "1pic_ruin40", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_41", 0, "1pic_ruin41", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_42", 0, "1pic_ruin42", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_43", 0, "1pic_ruin43", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_44", 0, "1pic_ruin44", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_45", 0, "1pic_ruin45", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_46", 0, "1pic_ruin46", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_47", 0, "1pic_ruin47", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_48", 0, "1pic_ruin48", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_49", 0, "1pic_ruin49", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_50", 0, "1pic_ruin50", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_51", 0, "1pic_ruin51", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_52", 0, "1pic_ruin52", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_53", 0, "1pic_ruin53", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_54", 0, "1pic_ruin54", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_55", 0, "1pic_ruin55", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_56", 0, "1pic_ruin56", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_57", 0, "1pic_ruin57", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_58", 0, "1pic_ruin58", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_59", 0, "1pic_ruin59", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_60", 0, "1pic_ruin60", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_61", 0, "1pic_ruin61", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_62", 0, "1pic_ruin62", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_63", 0, "1pic_ruin63", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_64", 0, "1pic_ruin64", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_65", 0, "1pic_ruin65", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_66", 0, "1pic_ruin66", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_67", 0, "1pic_ruin67", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_68", 0, "1pic_ruin68", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_69", 0, "1pic_ruin69", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_70", 0, "1pic_ruin70", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_71", 0, "1pic_ruin71", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_72", 0, "1pic_ruin72", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_73", 0, "1pic_ruin73", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_74", 0, "1pic_ruin74", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_75", 0, "1pic_ruin75", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_76", 0, "1pic_ruin76", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_77", 0, "1pic_ruin77", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_78", 0, "1pic_ruin78", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_79", 0, "1pic_ruin79", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_80", 0, "1pic_ruin80", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_81", 0, "1pic_ruin81", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_82", 0, "1pic_ruin82", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_83", 0, "1pic_ruin83", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_84", 0, "1pic_ruin84", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_85", 0, "1pic_ruin85", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_86", 0, "1pic_ruin86", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_87", 0, "1pic_ruin87", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_88", 0, "1pic_ruin88", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_89", 0, "1pic_ruin89", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_90", 0, "1pic_ruin90", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_91", 0, "1pic_ruin91", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_92", 0, "1pic_ruin92", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_93", 0, "1pic_ruin93", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_94", 0, "1pic_ruin94", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_95", 0, "1pic_ruin95", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_96", 0, "1pic_ruin96", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_97", 0, "1pic_ruin97", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_98", 0, "1pic_ruin98", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_99", 0, "1pic_ruin99", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_100", 0, "1pic_ruin100", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_101", 0, "1pic_ruin101", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_102", 0, "1pic_ruin102", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_103", 0, "1pic_ruin103", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_104", 0, "1pic_ruin104", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_105", 0, "1pic_ruin105", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_106", 0, "1pic_ruin106", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_107", 0, "1pic_ruin107", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_108", 0, "1pic_ruin108", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_109", 0, "1pic_ruin109", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_110", 0, "1pic_ruin110", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_111", 0, "1pic_ruin111", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_112", 0, "1pic_ruin112", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_113", 0, "1pic_ruin113", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_114", 0, "1pic_ruin114", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_115", 0, "1pic_ruin115", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_116", 0, "1pic_ruin116", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_117", 0, "1pic_ruin117", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_118", 0, "1pic_ruin118", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_119", 0, "1pic_ruin119", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_120", 0, "1pic_ruin120", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_121", 0, "1pic_ruin121", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_122", 0, "1pic_ruin122", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_123", 0, "1pic_ruin123", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_124", 0, "1pic_ruin124", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_125", 0, "1pic_ruin125", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_126", 0, "1pic_ruin126", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_127", 0, "1pic_ruin127", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_128", 0, "1pic_ruin128", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_129", 0, "1pic_ruin129", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_130", 0, "1pic_ruin130", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_131", 0, "1pic_ruin131", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_132", 0, "1pic_ruin132", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_133", 0, "1pic_ruin133", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_134", 0, "1pic_ruin134", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_135", 0, "1pic_ruin135", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_136", 0, "1pic_ruin136", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_137", 0, "1pic_ruin137", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_138", 0, "1pic_ruin138", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_139", 0, "1pic_ruin139", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_140", 0, "1pic_ruin140", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_141", 0, "1pic_ruin141", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_142", 0, "1pic_ruin142", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_143", 0, "1pic_ruin143", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_144", 0, "1pic_ruin144", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_145", 0, "1pic_ruin145", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_146", 0, "1pic_ruin146", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex1", 0, "1pic_ruinex1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex2", 0, "1pic_ruinex2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex3", 0, "1pic_ruinex3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex4", 0, "1pic_ruinex4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex5", 0, "1pic_ruinex5", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex6", 0, "1pic_ruinex6", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex7", 0, "1pic_ruinex7", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex8", 0, "1pic_ruinex8", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex9", 0, "1pic_ruinex9", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex10", 0, "1pic_ruinex10", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex11", 0, "1pic_ruinex11", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex12", 0, "1pic_ruinex12", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex13", 0, "1pic_ruinex13", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex14", 0, "1pic_ruinex14", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex15", 0, "1pic_ruinex15", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex16", 0, "1pic_ruinex16", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex17", 0, "1pic_ruinex17", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex18", 0, "1pic_ruinex18", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex19", 0, "1pic_ruinex19", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex20", 0, "1pic_ruinex20", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex21", 0, "1pic_ruinex21", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex22", 0, "1pic_ruinex22", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex23", 0, "1pic_ruinex23", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex24", 0, "1pic_ruinex24", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("1pic_ruin_ex25", 0, "1pic_ruinex25", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter1", 0, "pic_encounter1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter2", 0, "pic_encounter2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_encounter3", 0, "pic_encounter3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_xex8", 0, "pic_xex8", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_xex9", 0, "pic_xex9", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_xex10", 0, "pic_xex10", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_xex11", 0, "pic_xex11", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_xex12", 0, "pic_xex12", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_xex13", 0, "pic_xex13", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_xex14", 0, "pic_xex14", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("st_tercio", 0, "st_tercio", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("st_pincer_movement", 0, "st_pincer_movement", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("encounter4vik", 0, "encounter4vik", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("encounter5pirate", 0, "encounter5pirate", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_ship_shipyard", 0, "pic_ship_shipyard", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("st_pic_plain", 0, "st_pic_plain", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("st_pic_desert", 0, "st_pic_desert", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("st_pic_mount", 0, "st_pic_mount", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("st_pic_snow", 0, "st_pic_snow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("st_pic_sea", 0, "st_pic_sea", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("st_lancecharge", 0, "st_lancecharge", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("st_ccccharge", 0, "st_ccccharge", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("st_viking", 0, "st_viking", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("black_st_plane", 0, "black_st_plane", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("invisi_st_plane", 0, "invisi_st_plane", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_invisi_backgrounds", 0, "pic_invisi_backgrounds", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_policy_choose_prt", 0, "pic_policy_choose_prt", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_policy_choose_prt_bk", 0, "pic_policy_choose_prt_bk", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_screenn", 0, "pic_religion_screenn", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_gbt_punch", 0, "pic_gbt_punch", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_gbt_lick", 0, "pic_gbt_lick", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_gbt_finger", 0, "pic_gbt_finger", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_gbt_love", 0, "pic_gbt_love", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_gbt_place", 0, "pic_gbt_place", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_gbt_bed_sheet", 0, "pic_gbt_bed_sheet", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_money_bag", 0, "pic_money_bag", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_sea_backg", 0, "pic_sea_backg", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_flag", 0, "tableau_mesh_flag", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("pic_backg_inv", 0, "pic_backg_inv", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_library", 0, "pic_library", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_fuck_back", 0, "pic_fuck_back", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_ghost_ship_encount", 0, "pic_ghost_ship_encount", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_visit_train", 0, "pic_visit_train", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_weknow", 0, "pic_weknow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bank_back", 0, "pic_bank_back", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_blank", 0, "pic_wm_blank", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_horse", 0, "pic_wm_horse", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_finewood", 0, "pic_wm_finewood", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_iron", 0, "pic_wm_iron", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_elephant", 0, "pic_wm_elephant", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_whale", 0, "pic_wm_whale", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_fish", 0, "pic_wm_fish", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_maize", 0, "pic_wm_maize", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_copper", 0, "pic_wm_copper", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_marble", 0, "pic_wm_marble", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_pearl", 0, "pic_wm_pearl", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_gem", 0, "pic_wm_gem", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_ceramic", 0, "pic_wm_ceramic", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_gold", 0, "pic_wm_gold", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_silver", 0, "pic_wm_silver", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_ivory", 0, "pic_wm_ivory", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_coffee", 0, "pic_wm_coffee", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_cacao", 0, "pic_wm_cacao", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_silk", 0, "pic_wm_silk", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_nutmeg", 0, "pic_wm_nutmeg", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_allspice", 0, "pic_wm_allspice", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_cinnamon", 0, "pic_wm_cinnamon", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_clove", 0, "pic_wm_clove", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_pepper", 0, "pic_wm_pepper", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_tabaco", 0, "pic_wm_tabaco", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wm_tea", 0, "pic_wm_tea", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_marry", 0, "pic_marry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_0", 0, "pic_religion_symbol_0", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_1", 0, "pic_religion_symbol_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_2", 0, "pic_religion_symbol_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_3", 0, "pic_religion_symbol_3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_4", 0, "pic_religion_symbol_4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_5", 0, "pic_religion_symbol_5", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_6", 0, "pic_religion_symbol_6", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_7", 0, "pic_religion_symbol_7", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_8", 0, "pic_religion_symbol_8", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_9", 0, "pic_religion_symbol_9", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_10", 0, "pic_religion_symbol_10", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_11", 0, "pic_religion_symbol_11", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_12", 0, "pic_religion_symbol_12", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_13", 0, "pic_religion_symbol_13", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_14", 0, "pic_religion_symbol_14", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_15", 0, "pic_religion_symbol_15", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_religion_symbol_16", 0, "pic_religion_symbol_16", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_disaster_volcano", 0, "pic_disaster_volcano", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_disaster_earthquake", 0, "pic_disaster_earthquake", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_disaster_storm", 0, "pic_disaster_storm", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_disaster_typhoon", 0, "pic_disaster_typhoon", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_disaster_fire", 0, "pic_disaster_fire", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_disaster_sand", 0, "pic_disaster_sand", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_disaster_tides", 0, "pic_disaster_tides", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_disaster_ice", 0, "pic_disaster_ice", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_disaster_flood", 0, "pic_disaster_flood", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_div_1", 0, "flag_div_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_div_2", 0, "flag_div_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_div_3", 0, "flag_div_3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_div_4", 0, "flag_div_4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_div_5", 0, "flag_div_5", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_div_6", 0, "flag_div_6", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_div_7", 0, "flag_div_7", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_div_8", 0, "flag_div_8", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_div_9", 0, "flag_div_9", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_2", 0, "pic_battle_tile_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_3", 0, "pic_battle_tile_3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_4", 0, "pic_battle_tile_4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_5", 0, "pic_battle_tile_5", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_6", 0, "pic_battle_tile_6", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_7", 0, "pic_battle_tile_7", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_8", 0, "pic_battle_tile_8", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_9", 0, "pic_battle_tile_9", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_10", 0, "pic_battle_tile_10", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_11", 0, "pic_battle_tile_11", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_s1", 0, "pic_battle_tile_s1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_s2", 0, "pic_battle_tile_s2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_s3", 0, "pic_battle_tile_s3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_s4", 0, "pic_battle_tile_s4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_tile_n1", 0, "pic_battle_tile_n1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_gameover", 0, "pic_gameover", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_cla_mercernary", 0, "pic_cla_mercernary", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_cla_merchant", 0, "pic_cla_merchant", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_cla_adventurer", 0, "pic_cla_adventurer", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_cla_lord", 0, "pic_cla_lord", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_cla_bandit", 0, "pic_cla_bandit", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_cla_pirate", 0, "pic_cla_pirate", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_ptown_euro", 0, "pic_ptown_euro", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_ptown_snow", 0, "pic_ptown_snow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_ptown_roman", 0, "pic_ptown_roman", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_ptown_arab", 0, "pic_ptown_arab", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_ptown_wooden", 0, "pic_ptown_wooden", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_ptown_asia", 0, "pic_ptown_asia", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_ptown_asia_2", 0, "pic_ptown_asia_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_ptown_jap", 0, "pic_ptown_jap", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_ptown_uurt", 0, "pic_ptown_uurt", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_ptown_teepee", 0, "pic_ptown_teepee", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_meetlady4", 0, "pic_meetlady4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_formation_backriver", 0, "pic_battle_formation_backriver", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_formation_sideattack", 0, "pic_battle_formation_sideattack", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_formation_backattack", 0, "pic_battle_formation_backattack", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_formation_8door", 0, "pic_battle_formation_8door", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_formation_encampment", 0, "pic_battle_formation_encampment", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_formation_lionheart", 0, "pic_battle_formation_lionheart", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_formation_mangudai", 0, "pic_battle_formation_mangudai", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_formation_pincer", 0, "pic_battle_formation_pincer", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_battle_formation_base", 0, "pic_battle_formation_base", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("OrteliusWorldMap1570", 0, "OrteliusWorldMap1570", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_yoritomo", 0, "pic_portrait_yoritomo", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_munemori", 0, "pic_portrait_munemori", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_xiaozong", 0, "pic_portrait_xiaozong", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_shizong", 0, "pic_portrait_shizong", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_genghiskhan", 0, "pic_portrait_genghiskhan", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_philip_ii", 0, "pic_portrait_philip_ii", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_richard_i", 0, "pic_portrait_richard_i", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_barbarossa", 0, "pic_portrait_barbarossa", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_alfonso_viii", 0, "pic_portrait_alfonso_viii", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_yaqub", 0, "pic_portrait_yaqub", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_baldwin", 0, "pic_portrait_baldwin", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_saladin", 0, "pic_portrait_saladin", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_tekish", 0, "pic_portrait_tekish", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_ghiyath", 0, "pic_portrait_ghiyath", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_akbar", 0, "pic_portrait_akbar", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_ivan", 0, "pic_portrait_ivan", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_frederick_ii", 0, "pic_portrait_frederick_ii", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_maxi", 0, "pic_portrait_maxi", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_john_iii", 0, "pic_portrait_john_iii", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_selimii", 0, "pic_portrait_selimii", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_stephen", 0, "pic_portrait_stephen", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_elizabeth", 0, "pic_portrait_elizabeth", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_philip", 0, "pic_portrait_philip", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_sebastian", 0, "pic_portrait_sebastian", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_william", 0, "pic_portrait_william", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_wanli", 0, "pic_portrait_wanli", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_portrait_oda", 0, "pic_portrait_oda", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_plain", 0, "town_t_plain", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_water", 0, "town_t_water", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_hill", 0, "town_t_hill", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_desert", 0, "town_t_desert", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_snow", 0, "town_t_snow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_mountain", 0, "town_t_mountain", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_mil", 0, "town_t_mil", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_ore", 0, "town_t_ore", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_horse", 0, "town_t_horse", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_holy", 0, "town_t_holy", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_pasture", 0, "town_t_pasture", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_mine", 0, "town_t_mine", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_market", 0, "town_t_market", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_barrack", 0, "town_t_barrack", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_farm", 0, "town_t_farm", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_hall", 0, "town_t_hall", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_prison", 0, "town_t_prison", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_library", 0, "town_t_library", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_temple", 0, "town_t_temple", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_t_smithy", 0, "town_t_smithy", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("white_plane_upper", 0, "white_plane_upper", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("white_plane_center", 0, "white_plane_center", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_e_onehand", 0, "town_e_onehand", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_e_twohand", 0, "town_e_twohand", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_e_polearm", 0, "town_e_polearm", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_e_bow", 0, "town_e_bow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_e_crossbow", 0, "town_e_crossbow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_e_arquebus", 0, "town_e_arquebus", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_e_ammo", 0, "town_e_ammo", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_e_light", 0, "town_e_light", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_e_heavy", 0, "town_e_heavy", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_e_horse", 0, "town_e_horse", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_e_siege", 0, "town_e_siege", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_e_wood", 0, "town_e_wood", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_e_shipammo", 0, "town_e_shipammo", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_d_onehand", 0, "town_d_onehand", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_d_twohand", 0, "town_d_twohand", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_d_polearm", 0, "town_d_polearm", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_d_bow", 0, "town_d_bow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_d_crossbow", 0, "town_d_crossbow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_d_arquebus", 0, "town_d_arquebus", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_d_ammo", 0, "town_d_ammo", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_d_light", 0, "town_d_light", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_d_heavy", 0, "town_d_heavy", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_d_horse", 0, "town_d_horse", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_d_siege", 0, "town_d_siege", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_d_wood", 0, "town_d_wood", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("town_d_shipammo", 0, "town_d_shipammo", 0, 0, 0, 0, 0, 0, 1, 1, 1),

#			### Dice game ### Dice game ###
## 3 cards  
#  ("3card_back", 0, "mmc_3c_back", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("3card_qoh", 0, "mmc_3c_qh", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("3card_kos", 0, "mmc_3c_ks", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("3card_koc", 0, "mmc_3c_kc", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("3card_table", 0, "mmc_3c_table", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
##  ("3card_textbar", 0, "mmc_3c_textbar", 0, 0, 0, 0, 0, 0, 1, 1, 1), 
#  ("3card_window", 0, "mmc_3c_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
## 3 cards end  
## dices game 
#  ("mmc_dice_1", 0, "mmc_dice_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("mmc_dice_2", 0, "mmc_dice_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("mmc_dice_3", 0, "mmc_dice_3", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("mmc_dice_4", 0, "mmc_dice_4", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("mmc_dice_5", 0, "mmc_dice_5", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("mmc_dice_6", 0, "mmc_dice_6", 0, 0, 0, 0, 0, 0, 1, 1, 1),
# dices game end 
### Dice game ### Dice game ### END ### 
##plus  
####Begin Blackjack
#  ("text_bar", 0, "text_bar", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("button_used", 0, "medium_button", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("button_press_any_key", 0, "button_drop_hl", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("21_troop_portrait", 0, "blackjack_troop_portrait", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("21_button", 0, "21button", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("21_button_down", 0, "21button_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_heart_a", 0, "poker_12", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_heart_2", 0, "poker_13", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_heart_3", 0, "poker_14", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_heart_4", 0, "poker_15", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_heart_5", 0, "poker_16", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_heart_6", 0, "poker_17", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_heart_7", 0, "poker_18", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_heart_8", 0, "poker_19", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_heart_9", 0, "poker_21", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_heart_10", 0, "poker_22", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_heart_j", 0, "poker_23", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_heart_q", 0, "poker_24", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_heart_k", 0, "poker_25", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_spade_a", 0, "poker_26", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_spade_2", 0, "poker_27", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_spade_3", 0, "poker_28", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_spade_4", 0, "poker_29", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_spade_5", 0, "poker_31", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_spade_6", 0, "poker_32", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_spade_7", 0, "poker_33", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_spade_8", 0, "poker_34", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_spade_9", 0, "poker_35", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_spade_10", 0, "poker_36", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_spade_j", 0, "poker_37", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_spade_q", 0, "poker_38", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_spade_k", 0, "poker_39", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_diamond_a", 0, "poker_41", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_diamond_2", 0, "poker_42", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_diamond_3", 0, "poker_43", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_diamond_4", 0, "poker_44", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_diamond_5", 0, "poker_45", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_diamond_6", 0, "poker_46", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_diamond_7", 0, "poker_47", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_diamond_8", 0, "poker_48", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_diamond_9", 0, "poker_49", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_diamond_10", 0, "poker_51", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_diamond_j", 0, "poker_52", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_diamond_q", 0, "poker_53", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_diamond_k", 0, "poker_54", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_club_a", 0, "poker_55", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_club_2", 0, "poker_56", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_club_3", 0, "poker_57", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_club_4", 0, "poker_58", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_club_5", 0, "poker_59", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_club_6", 0, "poker_61", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_club_7", 0, "poker_62", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_club_8", 0, "poker_63", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_club_9", 0, "poker_64", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_club_10", 0, "poker_65", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_club_j", 0, "poker_66", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_club_q", 0, "poker_67", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_club_k", 0, "poker_68", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_red_joker", 0, "poker_69", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_black_joker", 0, "poker_11", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("poker_back", 0, "poker_back", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("wood_table", 0, "wood_table", 0, 0, 0, 0, 0, 0, 1, 1, 1),

###End Blackjack

	
	##################################################
##### troop_ratio_bar
##################################################
  ("status_troop_ratio_bar", 0, "slider_hor", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("status_troop_ratio_bar_button", 0, "handle_hor", 0, 0, 0, 0, 0, 0, 1, 1, 1),
##################################################
##### troop_ratio_bar
##################################################
]