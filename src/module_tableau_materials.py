from header_common import *
from ID_animations import *
from header_mission_templates import *
from header_tableau_materials import *
from header_items import *
from module_constants import *

####################################################################################################################
#  Each tableau material contains the following fields:
#  1) Tableau id (string): used for referencing tableaux in other files. The prefix tab_ is automatically added before each tableau-id.
#  2) Tableau flags (int). See header_tableau_materials.py for a list of available flags
#  3) Tableau sample material name (string).
#  4) Tableau width (int).
#  5) Tableau height (int).
#  6) Tableau mesh min x (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  7) Tableau mesh min y (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  8) Tableau mesh max x (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  9) Tableau mesh max y (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  10) Operations block (list): A list of operations. See header_operations.py for reference.
#     The operations block is executed when the tableau is activated.
# 
####################################################################################################################

#banner height = 200, width = 85 with wood, 75 without wood

tableaus = [
	("game_character_sheet", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 266, 532,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 4287137928),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(set_fixed_point_multiplier, 100),
		(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
		(init_position, 1),
		(position_set_z, 1, 100),
		(position_set_x, 1, -20),
		(position_set_y, 1, -20),
		(cur_tableau_add_tableau_mesh, "tableau_troop_character_color", ":script_param_1", 1, 0, 0),
		(position_set_z, 1, 200),
		(cur_tableau_add_tableau_mesh, "tableau_troop_character_alpha_mask", ":script_param_1", 1, 0, 0),
		(position_set_z, 1, 300)
	]),

	("game_inventory_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 180, 270,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 4287137928),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(set_fixed_point_multiplier, 100),
		(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
		(init_position, 1),
		(position_set_z, 1, 100),
		(position_set_x, 1, -20),
		(position_set_y, 1, -20),
		(cur_tableau_add_tableau_mesh, "tableau_troop_inventory_color", ":script_param_1", 1, 0, 0),
		(position_set_z, 1, 200),
		(cur_tableau_add_tableau_mesh, "tableau_troop_inventory_alpha_mask", ":script_param_1", 1, 0, 0),
		(position_set_z, 1, 300)
	]),

	("game_profile_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 320, 480,
	[
		(store_script_param, ":script_param_1", 1),
		(assign, ":var_2", ":script_param_1"),
		(val_mod, ":var_2", 2),
		(try_begin),
			(eq, ":var_2", 0),
			(assign, ":value", "trp_multiplayer_profile_troop_male"),
		(else_try),
			(assign, ":value", "trp_multiplayer_profile_troop_female"),
		(try_end),
		(troop_set_face_key_from_current_profile, ":value"),
		(cur_tableau_set_background_color, 4287137928),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(set_fixed_point_multiplier, 100),
		(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
		(init_position, 1),
		(position_set_z, 1, 100),
		(position_set_x, 1, -20),
		(position_set_y, 1, -20),
		(cur_tableau_add_tableau_mesh, "tableau_troop_profile_color", ":value", 1, 0, 0),
		(position_set_z, 1, 200),
		(cur_tableau_add_tableau_mesh, "tableau_troop_profile_alpha_mask", ":value", 1, 0, 0)
	]),

	("game_party_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 300, 300,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 4287137928),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(set_fixed_point_multiplier, 100),
		(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
		(init_position, 1),
		(position_set_z, 1, 100),
		(position_set_x, 1, -20),
		(position_set_y, 1, -20),
		(cur_tableau_add_tableau_mesh, "tableau_troop_party_color", ":script_param_1", 1, 0, 0),
		(position_set_z, 1, 200),
		(cur_tableau_add_tableau_mesh, "tableau_troop_party_alpha_mask", ":script_param_1", 1, 0, 0),
		(position_set_z, 1, 300)
	]),

	("game_troop_label_banner", 0, "tableau_with_transparency", 256, 256, -128, 0, 128, 256,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 4287137928),
		(set_fixed_point_multiplier, 100),
		(cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),
		(init_position, 1),
		(position_set_y, 1, 120),
		(cur_tableau_add_mesh, ":script_param_1", 1, 120, 0)
	]),

	("round_shield_1", 0, "sample_shield_round_1", 512, 256, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -50),
		(position_set_y, 1, 125),
		(cur_tableau_add_mesh, ":script_param_1", 1, 120, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_1", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000)
	]),

	("round_shield_2", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -50),
		(position_set_y, 1, 120),
		(cur_tableau_add_mesh, ":script_param_1", 1, 116, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_2", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000)
	]),

	("round_shield_3", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -50),
		(position_set_y, 1, 120),
		(cur_tableau_add_mesh, ":script_param_1", 1, 116, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_3", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000)
	]),

	("round_shield_4", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -50),
		(position_set_y, 1, 125),
		(cur_tableau_add_mesh, ":script_param_1", 1, 123, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_4", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000)
	]),

	("round_shield_5", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -50),
		(position_set_y, 1, 125),
		(cur_tableau_add_mesh, ":script_param_1", 1, 122, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_5", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000)
	]),

	("small_round_shield_1", 0, "sample_shield_small_round_1", 512, 256, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -50),
		(position_set_y, 1, 130),
		(cur_tableau_add_mesh, ":script_param_1", 1, 127, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_small_round_1", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000)
	]),

	("small_round_shield_2", 0, "sample_shield_small_round_2", 512, 256, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -50),
		(position_set_y, 1, 130),
		(cur_tableau_add_mesh, ":script_param_1", 1, 127, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_small_round_2", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000)
	]),

	("small_round_shield_3", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -50),
		(position_set_y, 1, 130),
		(cur_tableau_add_mesh, ":script_param_1", 1, 127, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_small_round_3", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000)
	]),

	("kite_shield_1", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -60),
		(position_set_y, 1, 140),
		(cur_tableau_add_mesh, ":script_param_1", 1, 116, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_kite_1", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("kite_shield_2", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -57),
		(position_set_y, 1, 140),
		(cur_tableau_add_mesh, ":script_param_1", 1, 116, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_kite_2", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("kite_shield_3", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -57),
		(position_set_y, 1, 140),
		(cur_tableau_add_mesh, ":script_param_1", 1, 116, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_kite_3", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("kite_shield_4", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -50),
		(position_set_y, 1, 160),
		(cur_tableau_add_mesh, ":script_param_1", 1, 120, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_kite_4", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("heater_shield_1", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -60),
		(position_set_y, 1, 151),
		(cur_tableau_add_mesh, ":script_param_1", 1, 116, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_heater_1", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("heater_shield_2", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -50),
		(position_set_y, 1, 150),
		(cur_tableau_add_mesh, ":script_param_1", 1, 116, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_heater_2", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("pavise_shield_1", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -54),
		(position_set_y, 1, 120),
		(cur_tableau_add_mesh, ":script_param_1", 1, 118, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_pavise_1", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("pavise_shield_2", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -54),
		(position_set_y, 1, 120),
		(cur_tableau_add_mesh, ":script_param_1", 1, 116, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_pavise_2", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("heraldic_armor_a", 0, "sample_heraldic_armor_a", 512, 512, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(store_sub, ":value", ":script_param_1", "mesh_arms_a01"),
		(val_add, ":value", 1),
		(troop_get_slot, ":banner_background_color_array_value", "trp_banner_background_color_array", ":value"),
		(try_begin),
			(eq, ":banner_background_color_array_value", 0),
			(assign, ":banner_background_color_array_value", 4285690482),
		(try_end),
		(cur_tableau_set_background_color, ":banner_background_color_array_value"),
		(init_position, 1),
		(cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", 1, 200, 100, ":banner_background_color_array_value"),
		(init_position, 1),
		(position_set_z, 1, 50),
		(position_set_x, 1, -25),
		(position_set_y, 1, 130),
		(cur_tableau_add_mesh, ":script_param_1", 1, 103, 0),
		(init_position, 1),
		(position_set_z, 1, 100),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_heraldic_armor_a", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("heraldic_armor_b", 0, "sample_heraldic_armor_b", 512, 512, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(store_sub, ":value", ":script_param_1", "mesh_arms_a01"),
		(val_add, ":value", 1),
		(troop_get_slot, ":banner_background_color_array_value", "trp_banner_background_color_array", ":value"),
		(try_begin),
			(eq, ":banner_background_color_array_value", 0),
			(assign, ":banner_background_color_array_value", 4285690482),
		(try_end),
		(cur_tableau_set_background_color, ":banner_background_color_array_value"),
		(init_position, 1),
		(cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", 1, 200, 100, ":banner_background_color_array_value"),
		(init_position, 1),
		(position_set_z, 1, 10),
		(position_set_x, 1, -5),
		(position_set_y, 1, 130),
		(cur_tableau_add_mesh, ":script_param_1", 1, 113, 0),
		(init_position, 1),
		(position_set_z, 1, 100),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_heraldic_armor_b", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("heraldic_armor_c", 0, "sample_heraldic_armor_c", 512, 512, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(store_sub, ":value", ":script_param_1", "mesh_arms_a01"),
		(val_add, ":value", 1),
		(troop_get_slot, ":banner_background_color_array_value", "trp_banner_background_color_array", ":value"),
		(try_begin),
			(eq, ":banner_background_color_array_value", 0),
			(assign, ":banner_background_color_array_value", 4285690482),
		(try_end),
		(cur_tableau_set_background_color, ":banner_background_color_array_value"),
		(init_position, 1),
		(cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", 1, 200, 100, ":banner_background_color_array_value"),
		(init_position, 1),
		(position_set_z, 1, 10),
		(position_set_x, 1, 0),
		(position_set_y, 1, 130),
		(cur_tableau_add_mesh, ":script_param_1", 1, 115, 0),
		(init_position, 1),
		(position_set_z, 1, 100),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_heraldic_armor_c", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("heraldic_armor_d", 0, "sample_heraldic_armor_d", 512, 512, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(store_sub, ":value", ":script_param_1", "mesh_arms_a01"),
		(val_add, ":value", 1),
		(troop_get_slot, ":banner_background_color_array_value", "trp_banner_background_color_array", ":value"),
		(try_begin),
			(eq, ":banner_background_color_array_value", 0),
			(assign, ":banner_background_color_array_value", 4285690482),
		(try_end),
		(cur_tableau_set_background_color, ":banner_background_color_array_value"),
		(init_position, 1),
		(cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", 1, 200, 100, ":banner_background_color_array_value"),
		(init_position, 1),
		(position_set_z, 1, 10),
		(position_set_x, 1, 0),
		(position_set_y, 1, 130),
		(cur_tableau_add_mesh, ":script_param_1", 1, 113, 0),
		(init_position, 1),
		(position_set_z, 1, 100),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_heraldic_armor_d", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("troop_note_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 8947848),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(cur_tableau_render_as_alpha_mask),
		(call_script, "script_add_troop_to_cur_tableau", ":script_param_1")
	]),

	("troop_note_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 4291214228),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(call_script, "script_add_troop_to_cur_tableau", ":script_param_1")
	]),

	("troop_character_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 8947848),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(cur_tableau_render_as_alpha_mask),
		(call_script, "script_add_troop_to_cur_tableau_for_character", ":script_param_1")
	]),

	("troop_character_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 4292923313),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(call_script, "script_add_troop_to_cur_tableau_for_character", ":script_param_1")
	]),

	("troop_inventory_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 8947848),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(cur_tableau_render_as_alpha_mask),
		(call_script, "script_add_troop_to_cur_tableau_for_inventory", ":script_param_1")
	]),

	("troop_inventory_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 4285159482),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(call_script, "script_add_troop_to_cur_tableau_for_inventory", ":script_param_1")
	]),

	("troop_profile_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 8947848),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(cur_tableau_render_as_alpha_mask),
		(call_script, "script_add_troop_to_cur_tableau_for_profile", ":script_param_1")
	]),

	("troop_profile_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 4294567848),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(call_script, "script_add_troop_to_cur_tableau_for_profile", ":script_param_1")
	]),

	("troop_party_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 8947848),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(cur_tableau_render_as_alpha_mask),
		(call_script, "script_add_troop_to_cur_tableau_for_party", ":script_param_1")
	]),

	("troop_party_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 4290681970),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(call_script, "script_add_troop_to_cur_tableau_for_party", ":script_param_1")
	]),

	("troop_note_mesh", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 350, 350,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 4287137928),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(set_fixed_point_multiplier, 100),
		(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
		(init_position, 1),
		(position_set_z, 1, 100),
		(position_set_x, 1, -20),
		(position_set_y, 1, -20),
		(cur_tableau_add_tableau_mesh, "tableau_troop_note_color", ":script_param_1", 1, 0, 0),
		(position_set_z, 1, 200),
		(cur_tableau_add_tableau_mesh, "tableau_troop_note_alpha_mask", ":script_param_1", 1, 0, 0),
		(position_set_z, 1, 300),
		(cur_tableau_add_mesh, "mesh_portrait_blend_out", 1, 0, 0)
	]),

	("center_note_mesh", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(cur_tableau_set_background_color, 8947848),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(init_position, 8),
		(position_set_x, 8, -210),
		(position_set_y, 8, 200),
		(position_set_z, 8, 300),
		(cur_tableau_add_point_light, 8, 550, 500, 450),
		(cur_tableau_set_camera_parameters, 1, 10, 10, 10, 10000),
		(init_position, 1),
		(position_set_z, 1, 0),
		(position_set_z, 1, -500),
		(init_position, 1),
		(position_set_y, 1, -100),
		(position_set_x, 1, -100),
		(position_set_z, 1, 100),
		(position_rotate_z, 1, 200),
		(party_get_icon, ":icon_script_param_1", ":script_param_1"),
		(try_begin),
			(ge, ":icon_script_param_1", 0),
			(cur_tableau_add_map_icon, ":icon_script_param_1", 1, 0),
		(try_end),
		(init_position, 5),
		(position_set_x, 5, -90),
		(position_set_z, 5, 500),
		(position_set_y, 5, 480),
		(position_rotate_x, 5, -90),
		(position_rotate_z, 5, 180),
		(position_rotate_x, 5, -35),
		(cur_tableau_set_camera_position, 5)
	]),

	("faction_note_mesh_for_menu", 0, "pic_arms_swadian", 1024, 512, 0, 0, 450, 225,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 4294967295),
		(set_fixed_point_multiplier, 100),
		(try_begin),
			(is_between, ":script_param_1", "fac_kingdom_1", "fac_kingdoms_end"),
			(store_add, ":value", "mesh_pic_arms_swadian", ":script_param_1"),
			(val_sub, ":value", "fac_kingdom_1"),
			(init_position, 1),
			(position_set_y, 1, -5),
			(position_set_x, 1, -45),
			(cur_tableau_add_mesh, ":value", 1, 0, 0),
			(cur_tableau_set_camera_parameters, 0, 160, 80, 0, 100000),
		(try_end)
	]),

	("faction_note_mesh", 0, "pic_arms_swadian", 1024, 512, 0, 0, 500, 250,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 4294967295),
		(set_fixed_point_multiplier, 100),
		(try_begin),
			(is_between, ":script_param_1", "fac_kingdom_1", "fac_kingdoms_end"),
			(store_add, ":value", "mesh_pic_arms_swadian", ":script_param_1"),
			(val_sub, ":value", "fac_kingdom_1"),
			(init_position, 1),
			(position_set_y, 1, -5),
			(cur_tableau_add_mesh, ":value", 1, 0, 0),
			(cur_tableau_set_camera_parameters, 0, 100, 50, 0, 100000),
		(try_end)
	]),

	("faction_note_mesh_banner", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(try_begin),
			(faction_get_slot, ":script_param_1_1", ":script_param_1", 1),
			(ge, ":script_param_1_1", 0),
			(neq, ":script_param_1_1", 1),
			(troop_get_slot, ":script_param_1_1_1", ":script_param_1_1", 1),
			(store_add, ":value", "spr_banner_k21", 1),
			(is_between, ":script_param_1_1_1", "spr_banner_a", ":value"),
			(val_sub, ":script_param_1_1_1", "spr_banner_a"),
			(store_add, ":value_2", ":script_param_1_1_1", "mesh_banner_a01"),
			(init_position, 1),
			(position_set_y, 1, 100),
			(cur_tableau_add_mesh, ":value_2", 1, 0, 0),
			(cur_tableau_set_camera_parameters, 0, 210, 210, 0, 100000),
		(try_end)
	]),

	("2_factions_mesh", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200,
	[
		(store_script_param, ":script_param_1", 1),
		(store_mod, ":value", ":script_param_1", 128),
		(val_div, ":script_param_1", 128),
		(val_add, ":script_param_1", "fac_kingdom_1"),
		(val_add, ":value", "fac_kingdom_1"),
		(set_fixed_point_multiplier, 100),
		(try_begin),
			(faction_get_slot, ":script_param_1_1", ":script_param_1", 1),
			(ge, ":script_param_1_1", 0),
			(neq, ":script_param_1_1", 1),
			(troop_get_slot, ":script_param_1_1_1", ":script_param_1_1", 1),
			(store_add, ":value_2", "spr_banner_k21", 1),
			(is_between, ":script_param_1_1_1", "spr_banner_a", ":value_2"),
			(val_sub, ":script_param_1_1_1", "spr_banner_a"),
			(store_add, ":value_3", ":script_param_1_1_1", "mesh_banner_a01"),
			(init_position, 1),
			(position_set_x, 1, -50),
			(position_set_y, 1, 100),
			(cur_tableau_add_mesh, ":value_3", 1, 0, 0),
		(try_end),
		(try_begin),
			(faction_get_slot, ":script_param_1_1", ":value", 1),
			(ge, ":script_param_1_1", 0),
			(neq, ":script_param_1_1", 1),
			(troop_get_slot, ":script_param_1_1_1", ":script_param_1_1", 1),
			(store_add, ":value_2", "spr_banner_k21", 1),
			(is_between, ":script_param_1_1_1", "spr_banner_a", ":value_2"),
			(val_sub, ":script_param_1_1_1", "spr_banner_a"),
			(store_add, ":value_3", ":script_param_1_1_1", "mesh_banner_a01"),
			(init_position, 1),
			(position_set_x, 1, 50),
			(position_set_y, 1, 100),
			(cur_tableau_add_mesh, ":value_3", 1, 0, 0),
		(try_end),
		(cur_tableau_set_camera_parameters, 0, 210, 210, 0, 100000)
	]),

	("color_picker", 0, "missiles", 32, 32, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(cur_tableau_add_mesh, "mesh_color_picker", 1, 0, 0),
		(position_move_z, 1, 1),
		(position_move_x, 1, -2),
		(position_move_y, 1, -2),
		(cur_tableau_add_mesh_with_vertex_color, "mesh_white_plane", 1, 200, 0, ":script_param_1"),
		(cur_tableau_set_camera_parameters, 0, 20, 20, 0, 100000)
	]),

	("custom_banner_square_no_mesh", 0, "missiles", 512, 512, 0, 0, 300, 300,
	[]),

	("custom_banner_default", 0, "missiles", 512, 256, 0, 0, 0, 0,
	[]),

	("custom_banner_tall", 0, "missiles", 512, 256, 0, 0, 0, 0,
	[]),

	("custom_banner_square", 0, "missiles", 256, 256, 0, 0, 0, 0,
	[]),

	("custom_banner_short", 0, "missiles", 256, 512, 0, 0, 0, 0,
	[]),

	("background_selection", 0, "missiles", 512, 512, 0, 0, 100, 100,
	[]),

	("positioning_selection", 0, "missiles", 512, 512, 0, 0, 100, 100,
	[]),

	("retired_troop_alpha_mask", 0, "mat_troop_portrait_mask", 2048, 2048, 0, 0, 600, 600,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 8947848),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(cur_tableau_render_as_alpha_mask),
		(call_script, "script_add_troop_to_cur_tableau_for_retirement", ":script_param_1")
	]),

	("retired_troop_color", 0, "mat_troop_portrait_color", 2048, 2048, 0, 0, 600, 600,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 4293383065),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(call_script, "script_add_troop_to_cur_tableau_for_retirement", ":script_param_1")
	]),

	("retirement_troop", 0, "tableau_with_transparency", 2048, 2048, 0, 0, 600, 600,
	[
		(store_script_param, ":script_param_1", 1),
		(cur_tableau_set_background_color, 4287137928),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(set_fixed_point_multiplier, 100),
		(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
		(init_position, 1),
		(position_set_z, 1, 100),
		(position_set_x, 1, -20),
		(position_set_y, 1, -20),
		(cur_tableau_add_tableau_mesh, "tableau_retired_troop_color", ":script_param_1", 1, 0, 0),
		(position_set_z, 1, 200),
		(cur_tableau_add_tableau_mesh, "tableau_retired_troop_alpha_mask", ":script_param_1", 1, 0, 0)
	]),

	("flag_itm", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(init_position, 1),
		(position_set_x, 1, -54),
		(position_set_y, 1, 120),
		(cur_tableau_add_mesh, ":script_param_1", 1, 116, 0),
		(init_position, 1),
		(position_set_z, 1, 10),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_flag", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("fuck_troop", 0, "tableau_with_transparency", 8192, 8192, 0, 0, 600, 600,
	[
		(cur_tableau_set_background_color, 16777215),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(set_fixed_point_multiplier, 100),
		(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
		(cur_tableau_set_background_color, 16777215),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(call_script, "script_add_troop_to_cur_tableau_for_fuck")
	]),

	("early_transitional_heraldic", 0, "sample_early_transitional_heraldic_banner", 1024, 1024, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(store_sub, ":value", ":script_param_1", "mesh_arms_a01"),
		(val_add, ":value", 1),
		(troop_get_slot, ":banner_background_color_array_value", "trp_banner_background_color_array", ":value"),
		(try_begin),
			(eq, ":banner_background_color_array_value", 0),
			(assign, ":banner_background_color_array_value", 4285690482),
		(try_end),
		(cur_tableau_set_background_color, ":banner_background_color_array_value"),
		(init_position, 1),
		(cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", 1, 200, 100, ":banner_background_color_array_value"),
		(init_position, 1),
		(position_set_x, 1, 17),
		(position_set_y, 1, 150),
		(cur_tableau_add_mesh, ":script_param_1", 1, 90, 0),
		(init_position, 1),
		(position_set_z, 1, 30),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_early_transitional_heraldic_banner", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("samurai_heraldic_flag", 0, "sample_samurai_nobori_heraldic", 1024, 1024, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(store_sub, ":value", ":script_param_1", "mesh_arms_a01"),
		(troop_get_slot, ":banner_background_color_array_value", "trp_banner_background_color_array", ":value"),
		(cur_tableau_set_background_color, ":banner_background_color_array_value"),
		(init_position, 1),
		(cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", 1, 200, 100, ":banner_background_color_array_value"),
		(init_position, 1),
		(position_set_x, 1, -85),
		(position_set_y, 1, -22),
		(cur_tableau_add_mesh, ":script_param_1", 1, 43, 0),
		(init_position, 1),
		(position_set_z, 1, 100),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_samurai_heraldic_flag", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("banner_spear", 0, "sample_samurai_weapons", 1024, 1024, 0, 0, 0, 0,
	[
		(store_script_param, ":script_param_1", 1),
		(set_fixed_point_multiplier, 100),
		(store_sub, ":value", ":script_param_1", "mesh_arms_a01"),
		(troop_get_slot, ":banner_background_color_array_value", "trp_banner_background_color_array", ":value"),
		(cur_tableau_set_background_color, ":banner_background_color_array_value"),
		(init_position, 1),
		(cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", 1, 200, 100, ":banner_background_color_array_value"),
		(init_position, 1),
		(position_set_x, 1, -33),
		(position_set_y, 1, -20),
		(cur_tableau_add_mesh, ":script_param_1", 1, 43, 0),
		(init_position, 1),
		(position_set_z, 1, 100),
		(cur_tableau_add_mesh, "mesh_tableau_mesh_banner_spear", 1, 0, 0),
		(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)
	]),

	("blank_stack", 0, "tableau_with_transparency", 8192, 8192, 0, 0, 600, 600,
	[
		(cur_tableau_set_background_color, 16777215),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(set_fixed_point_multiplier, 100),
		(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
		(cur_tableau_set_background_color, 16777215),
		(cur_tableau_set_ambient_light, 10, 11, 15),
		(call_script, "script_add_troop_to_cur_tableau_for_fuck")
	]),

]