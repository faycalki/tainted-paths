# -*- coding: cp1252 -*-
from header_common import *
from header_scene_props import *
from header_operations import *
from header_triggers import *
from header_sounds import *
from module_constants import *
import string

####################################################################################################################
#  Each scene prop record contains the following fields:
#  1) Scene prop id: used for referencing scene props in other files. The prefix spr_ is automatically added before each scene prop id.
#  2) Scene prop flags. See header_scene_props.py for a list of available flags
#  3) Mesh name: Name of the mesh.
#  4) Physics object name:
#  5) Triggers: Simple triggers that are associated with the scene prop
####################################################################################################################

scene_props = [
	("invalid_object", 0, "question_mark", "0", []),

	("inventory", sokf_type_container|sokf_place_at_origin, "package", "bobaggage", []),

	("empty", 0, "0", "0", []),

	("chest_a", sokf_type_container, "chest_gothic", "bochest_gothic", []),

	("container_small_chest", sokf_type_container, "package", "bobaggage", []),

	("container_chest_b", sokf_type_container, "chest_b", "bo_chest_b", []),

	("container_chest_c", sokf_type_container, "chest_c", "bo_chest_c", []),

	("player_chest", sokf_type_container, "player_chest", "bo_player_chest", []),

	("locked_player_chest", 0, "player_chest", "bo_player_chest", []),

	("light_sun", sokf_invisible, "light_sphere", "0", 
	[(ti_on_scene_prop_init,
		[
			(neg|is_currently_night),
			(store_trigger_param_1, ":trigger_param_1"),
			(set_fixed_point_multiplier, 100),
			(prop_instance_get_scale, 5, ":trigger_param_1"),
			(position_get_scale_x, ":position_scale_x_5", 5),
			(store_time_of_day, reg12),
			(try_begin),
				(is_between, reg12, 5, 20),
				(store_mul, ":value", 1000, ":position_scale_x_5"),
				(store_mul, ":value_2", 965, ":position_scale_x_5"),
				(store_mul, ":value_3", 900, ":position_scale_x_5"),
			(else_try),
				(store_mul, ":value", 450, ":position_scale_x_5"),
				(store_mul, ":value_2", 575, ":position_scale_x_5"),
				(store_mul, ":value_3", 750, ":position_scale_x_5"),
			(try_end),
			(val_div, ":value", 100),
			(val_div, ":value_2", 100),
			(val_div, ":value_3", 100),
			(set_current_color, ":value", ":value_2", ":value_3"),
			(set_position_delta, 0, 0, 0),
			(add_point_light_to_entity, 0, 0)
		])
	]),

	("light", sokf_invisible, "light_sphere", "0", 
	[(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(set_fixed_point_multiplier, 100),
			(prop_instance_get_scale, 5, ":trigger_param_1"),
			(position_get_scale_x, ":position_scale_x_5", 5),
			(store_mul, ":value", 600, ":position_scale_x_5"),
			(store_mul, ":value_2", 435, ":position_scale_x_5"),
			(store_mul, ":value_3", 135, ":position_scale_x_5"),
			(val_div, ":value", 100),
			(val_div, ":value_2", 100),
			(val_div, ":value_3", 100),
			(set_current_color, ":value", ":value_2", ":value_3"),
			(set_position_delta, 0, 0, 0),
			(add_point_light_to_entity, 10, 30)
		])
	]),

	("light_red", sokf_invisible, "light_sphere", "0", 
	[(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(set_fixed_point_multiplier, 100),
			(prop_instance_get_scale, 5, ":trigger_param_1"),
			(position_get_scale_x, ":position_scale_x_5", 5),
			(store_mul, ":value", 340, ":position_scale_x_5"),
			(store_mul, ":value_2", 200, ":position_scale_x_5"),
			(store_mul, ":value_3", 60, ":position_scale_x_5"),
			(val_div, ":value", 100),
			(val_div, ":value_2", 100),
			(val_div, ":value_3", 100),
			(set_current_color, ":value", ":value_2", ":value_3"),
			(set_position_delta, 0, 0, 0),
			(add_point_light_to_entity, 20, 30)
		])
	]),

	("light_night", sokf_invisible, "light_sphere", "0", 
	[(ti_on_scene_prop_init,
		[
			(is_currently_night, 0),
			(store_trigger_param_1, ":trigger_param_1"),
			(set_fixed_point_multiplier, 100),
			(prop_instance_get_scale, 5, ":trigger_param_1"),
			(position_get_scale_x, ":position_scale_x_5", 5),
			(store_mul, ":value", 480, ":position_scale_x_5"),
			(store_mul, ":value_2", 435, ":position_scale_x_5"),
			(store_mul, ":value_3", 300, ":position_scale_x_5"),
			(val_div, ":value", 100),
			(val_div, ":value_2", 100),
			(val_div, ":value_3", 100),
			(set_current_color, ":value", ":value_2", ":value_3"),
			(set_position_delta, 0, 0, 0),
			(add_point_light_to_entity, 10, 30)
		])
	]),

	("torch", 0, "torch_a", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, -35, 48),
			(particle_system_add_new, "psys_torch_fire"),
			(particle_system_add_new, "psys_torch_smoke"),
			(particle_system_add_new, "psys_torch_fire_sparks"),
			(play_sound, "snd_torch_loop", 0),
			(set_position_delta, 0, -35, 56),
			(particle_system_add_new, "psys_fire_glow_1"),
			(get_trigger_object_position, 2),
			(set_position_delta, 0, 0, 0),
			(position_move_y, 2, -35),
			(position_move_z, 2, 55),
			(particle_system_burst, "psys_fire_glow_fixed", 2, 1)
		])
	]),

	("torch_night", 0, "torch_a", "0", 
	[(ti_on_scene_prop_init,
		[
			(is_currently_night, 0),
			(set_position_delta, 0, -35, 48),
			(particle_system_add_new, "psys_torch_fire"),
			(particle_system_add_new, "psys_torch_smoke"),
			(particle_system_add_new, "psys_torch_fire_sparks"),
			(set_position_delta, 0, -35, 56),
			(particle_system_add_new, "psys_fire_glow_1"),
			(particle_system_emit, "psys_fire_glow_1", 9000000),
			(play_sound, "snd_torch_loop", 0)
		])
	]),

	("barrier_20m", sokf_type_barrier|sokf_invisible, "barrier_20m", "bo_barrier_20m", []),

	("barrier_16m", sokf_type_barrier|sokf_invisible, "barrier_16m", "bo_barrier_16m", []),

	("barrier_8m", sokf_type_barrier|sokf_invisible, "barrier_8m", "bo_barrier_8m", []),

	("barrier_4m", sokf_type_barrier|sokf_invisible, "barrier_4m", "bo_barrier_4m", []),

	("barrier_2m", sokf_type_barrier|sokf_invisible, "barrier_2m", "bo_barrier_2m", []),

	("exit_4m", sokf_type_barrier_leave|sokf_invisible, "barrier_4m", "bo_barrier_4m", []),

	("exit_8m", sokf_type_barrier_leave|sokf_invisible, "barrier_8m", "bo_barrier_8m", []),

	("exit_16m", sokf_type_barrier_leave|sokf_invisible, "barrier_16m", "bo_barrier_16m", []),

	("ai_limiter_2m", sokf_type_ai_limiter|sokf_invisible, "barrier_2m", "bo_barrier_2m", []),

	("ai_limiter_4m", sokf_type_ai_limiter|sokf_invisible, "barrier_4m", "bo_barrier_4m", []),

	("ai_limiter_8m", sokf_type_ai_limiter|sokf_invisible, "barrier_8m", "bo_barrier_8m", []),

	("ai_limiter_16m", sokf_type_ai_limiter|sokf_invisible, "barrier_16m", "bo_barrier_16m", []),

	("Shield", sokf_dynamic, "0", "boshield", []),

	("catapult_destructible", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "Catapult", "bo_Catapult", 
	[(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 1600)
		]),

		(ti_on_scene_prop_destroy,
		[]),

		(ti_on_scene_prop_hit,
		[])
	]),

	("destroy_a", 0, "destroy_a", "0", []),

	("destroy_b", 0, "destroy_b", "0", []),

	("ship", 0, "ship", "bo_ship", []),

	("ship_b", 0, "ship_b", "bo_ship_b", []),

	("ship_c", 0, "ship_c", "bo_ship_c", []),

	("ship_d", 0, "ship_d", "bo_ship_d", []),

	("skeleton_head", 0, "skeleton_head", "0", []),

	("skeleton_bone", 0, "skeleton_bone", "0", []),

	("skeleton_a", 0, "skeleton_a", "bo_skeleton_a", []),

	("banner_pole", sokf_moveable, "banner_pole", "bo_banner_pole", []),

	("custom_banner_01", 0, "custom_banner_01", "0", []),

	("custom_banner_02", 0, "custom_banner_02", "0", []),

	("banner_a", 0, "banner_a01", "0", []),

	("banner_b", 0, "banner_a02", "0", []),

	("banner_c", 0, "banner_a03", "0", []),

	("banner_d", 0, "banner_a04", "0", []),

	("banner_e", 0, "banner_a05", "0", []),

	("banner_f", 0, "banner_a06", "0", []),

	("banner_g", 0, "banner_a07", "0", []),

	("banner_h", 0, "banner_a08", "0", []),

	("banner_i", 0, "banner_a09", "0", []),

	("banner_j", 0, "banner_a10", "0", []),

	("banner_k", 0, "banner_a11", "0", []),

	("banner_l", 0, "banner_a12", "0", []),

	("banner_m", 0, "banner_a13", "0", []),

	("banner_n", 0, "banner_a14", "0", []),

	("banner_o", 0, "banner_a15", "0", []),

	("banner_p", 0, "banner_a16", "0", []),

	("banner_q", 0, "banner_a17", "0", []),

	("banner_r", 0, "banner_a18", "0", []),

	("banner_s", 0, "banner_a19", "0", []),

	("banner_t", 0, "banner_a20", "0", []),

	("banner_u", 0, "banner_a21", "0", []),

	("banner_ba", 0, "banner_b01", "0", []),

	("banner_bb", 0, "banner_b02", "0", []),

	("banner_bc", 0, "banner_b03", "0", []),

	("banner_bd", 0, "banner_b04", "0", []),

	("banner_be", 0, "banner_b05", "0", []),

	("banner_bf", 0, "banner_b06", "0", []),

	("banner_bg", 0, "banner_b07", "0", []),

	("banner_bh", 0, "banner_b08", "0", []),

	("banner_bi", 0, "banner_b09", "0", []),

	("banner_bj", 0, "banner_b10", "0", []),

	("banner_bk", 0, "banner_b11", "0", []),

	("banner_bl", 0, "banner_b12", "0", []),

	("banner_bm", 0, "banner_b13", "0", []),

	("banner_bn", 0, "banner_b14", "0", []),

	("banner_bo", 0, "banner_b15", "0", []),

	("banner_bp", 0, "banner_b16", "0", []),

	("banner_bq", 0, "banner_b17", "0", []),

	("banner_br", 0, "banner_b18", "0", []),

	("banner_bs", 0, "banner_b19", "0", []),

	("banner_bt", 0, "banner_b20", "0", []),

	("banner_bu", 0, "banner_b21", "0", []),

	("banner_ca", 0, "banner_c01", "0", []),

	("banner_cb", 0, "banner_c02", "0", []),

	("banner_cc", 0, "banner_c03", "0", []),

	("banner_cd", 0, "banner_c04", "0", []),

	("banner_ce", 0, "banner_c05", "0", []),

	("banner_cf", 0, "banner_c06", "0", []),

	("banner_cg", 0, "banner_c07", "0", []),

	("banner_ch", 0, "banner_c08", "0", []),

	("banner_ci", 0, "banner_c09", "0", []),

	("banner_cj", 0, "banner_c10", "0", []),

	("banner_ck", 0, "banner_c11", "0", []),

	("banner_cl", 0, "banner_c12", "0", []),

	("banner_cm", 0, "banner_c13", "0", []),

	("banner_cn", 0, "banner_c14", "0", []),

	("banner_co", 0, "banner_c15", "0", []),

	("banner_cp", 0, "banner_c16", "0", []),

	("banner_cq", 0, "banner_c17", "0", []),

	("banner_cr", 0, "banner_c18", "0", []),

	("banner_cs", 0, "banner_c19", "0", []),

	("banner_ct", 0, "banner_c20", "0", []),

	("banner_cu", 0, "banner_c21", "0", []),

	("banner_da", 0, "banner_d01", "0", []),

	("banner_db", 0, "banner_d02", "0", []),

	("banner_dc", 0, "banner_d03", "0", []),

	("banner_dd", 0, "banner_d04", "0", []),

	("banner_de", 0, "banner_d05", "0", []),

	("banner_df", 0, "banner_d06", "0", []),

	("banner_dg", 0, "banner_d07", "0", []),

	("banner_dh", 0, "banner_d08", "0", []),

	("banner_di", 0, "banner_d09", "0", []),

	("banner_dj", 0, "banner_d10", "0", []),

	("banner_dk", 0, "banner_d11", "0", []),

	("banner_dl", 0, "banner_d12", "0", []),

	("banner_dm", 0, "banner_d13", "0", []),

	("banner_dn", 0, "banner_d14", "0", []),

	("banner_do", 0, "banner_d15", "0", []),

	("banner_dp", 0, "banner_d16", "0", []),

	("banner_dq", 0, "banner_d17", "0", []),

	("banner_dr", 0, "banner_d18", "0", []),

	("banner_ds", 0, "banner_d19", "0", []),

	("banner_dt", 0, "banner_d20", "0", []),

	("banner_du", 0, "banner_d21", "0", []),

	("banner_ea", 0, "banner_e01", "0", []),

	("banner_eb", 0, "banner_e02", "0", []),

	("banner_ec", 0, "banner_e03", "0", []),

	("banner_ed", 0, "banner_e04", "0", []),

	("banner_ee", 0, "banner_e05", "0", []),

	("banner_ef", 0, "banner_e06", "0", []),

	("banner_eg", 0, "banner_e07", "0", []),

	("banner_eh", 0, "banner_e08", "0", []),

	("banner_ei", 0, "banner_e09", "0", []),

	("banner_ej", 0, "banner_e10", "0", []),

	("banner_ek", 0, "banner_e11", "0", []),

	("banner_el", 0, "banner_e12", "0", []),

	("banner_em", 0, "banner_e13", "0", []),

	("banner_en", 0, "banner_e14", "0", []),

	("banner_eo", 0, "banner_e15", "0", []),

	("banner_ep", 0, "banner_e16", "0", []),

	("banner_eq", 0, "banner_e17", "0", []),

	("banner_er", 0, "banner_e18", "0", []),

	("banner_es", 0, "banner_e19", "0", []),

	("banner_et", 0, "banner_e20", "0", []),

	("banner_eu", 0, "banner_e21", "0", []),

	("banner_f01", 0, "banner_f01", "0", []),

	("banner_f02", 0, "banner_f02", "0", []),

	("banner_f03", 0, "banner_f03", "0", []),

	("banner_f04", 0, "banner_f04", "0", []),

	("banner_f05", 0, "banner_f05", "0", []),

	("banner_f06", 0, "banner_f06", "0", []),

	("banner_f07", 0, "banner_f07", "0", []),

	("banner_f08", 0, "banner_f08", "0", []),

	("banner_f09", 0, "banner_f09", "0", []),

	("banner_f10", 0, "banner_f10", "0", []),

	("banner_f11", 0, "banner_f11", "0", []),

	("banner_f12", 0, "banner_f12", "0", []),

	("banner_f13", 0, "banner_f13", "0", []),

	("banner_f14", 0, "banner_f14", "0", []),

	("banner_f15", 0, "banner_f15", "0", []),

	("banner_f16", 0, "banner_f16", "0", []),

	("banner_f17", 0, "banner_f17", "0", []),

	("banner_f18", 0, "banner_f18", "0", []),

	("banner_f19", 0, "banner_f19", "0", []),

	("banner_f20", 0, "banner_f20", "0", []),

	("banner_h01", 0, "banner_h01", "0", []),

	("banner_h02", 0, "banner_h02", "0", []),

	("banner_h03", 0, "banner_h03", "0", []),

	("banner_h04", 0, "banner_h04", "0", []),

	("banner_h05", 0, "banner_h05", "0", []),

	("banner_h06", 0, "banner_h06", "0", []),

	("banner_h07", 0, "banner_h07", "0", []),

	("banner_h08", 0, "banner_h08", "0", []),

	("banner_h09", 0, "banner_h09", "0", []),

	("banner_h10", 0, "banner_h10", "0", []),

	("banner_h11", 0, "banner_h11", "0", []),

	("banner_h12", 0, "banner_h12", "0", []),

	("banner_h13", 0, "banner_h13", "0", []),

	("banner_h14", 0, "banner_h14", "0", []),

	("banner_h15", 0, "banner_h15", "0", []),

	("banner_h16", 0, "banner_h16", "0", []),

	("banner_h17", 0, "banner_h17", "0", []),

	("banner_h18", 0, "banner_h18", "0", []),

	("banner_h19", 0, "banner_h19", "0", []),

	("banner_h20", 0, "banner_h20", "0", []),

	("banner_h21", 0, "banner_h21", "0", []),

	("banner_i01", 0, "banner_i01", "0", []),

	("banner_i02", 0, "banner_i02", "0", []),

	("banner_i03", 0, "banner_i03", "0", []),

	("banner_i04", 0, "banner_i04", "0", []),

	("banner_i05", 0, "banner_i05", "0", []),

	("banner_i06", 0, "banner_i06", "0", []),

	("banner_i07", 0, "banner_i07", "0", []),

	("banner_i08", 0, "banner_i08", "0", []),

	("banner_i09", 0, "banner_i09", "0", []),

	("banner_i10", 0, "banner_i10", "0", []),

	("banner_i11", 0, "banner_i11", "0", []),

	("banner_i12", 0, "banner_i12", "0", []),

	("banner_i13", 0, "banner_i13", "0", []),

	("banner_i14", 0, "banner_i14", "0", []),

	("banner_i15", 0, "banner_i15", "0", []),

	("banner_i16", 0, "banner_i16", "0", []),

	("banner_i17", 0, "banner_i17", "0", []),

	("banner_i18", 0, "banner_i18", "0", []),

	("banner_i19", 0, "banner_i19", "0", []),

	("banner_i20", 0, "banner_i20", "0", []),

	("banner_i21", 0, "banner_i21", "0", []),

	("banner_k01", 0, "banner_k01", "0", []),

	("banner_k02", 0, "banner_k02", "0", []),

	("banner_k03", 0, "banner_k03", "0", []),

	("banner_k04", 0, "banner_k04", "0", []),

	("banner_k05", 0, "banner_k05", "0", []),

	("banner_k06", 0, "banner_k06", "0", []),

	("banner_k07", 0, "banner_k07", "0", []),

	("banner_k08", 0, "banner_k08", "0", []),

	("banner_k09", 0, "banner_k09", "0", []),

	("banner_k10", 0, "banner_k10", "0", []),

	("banner_k11", 0, "banner_k11", "0", []),

	("banner_k12", 0, "banner_k12", "0", []),

	("banner_k13", 0, "banner_k13", "0", []),

	("banner_k14", 0, "banner_k14", "0", []),

	("banner_k15", 0, "banner_k15", "0", []),

	("banner_k16", 0, "banner_k16", "0", []),

	("banner_k17", 0, "banner_k17", "0", []),

	("banner_k18", 0, "banner_k18", "0", []),

	("banner_k19", 0, "banner_k19", "0", []),

	("banner_k20", 0, "banner_k20", "0", []),

	("banner_g01", 0, "banner_g01", "0", []),

	("banner_g02", 0, "banner_g02", "0", []),

	("banner_g03", 0, "banner_g03", "0", []),

	("banner_g04", 0, "banner_g04", "0", []),

	("banner_g05", 0, "banner_g05", "0", []),

	("banner_g06", 0, "banner_g06", "0", []),

	("banner_g07", 0, "banner_g07", "0", []),

	("banner_g08", 0, "banner_g08", "0", []),

	("banner_g09", 0, "banner_g09", "0", []),

	("banner_g10", 0, "banner_g10", "0", []),

	("banner_kingdom_a", 0, "banner_kingdom_a", "0", []),

	("banner_kingdom_b", 0, "banner_kingdom_b", "0", []),

	("banner_kingdom_c", 0, "banner_kingdom_c", "0", []),

	("banner_kingdom_d", 0, "banner_kingdom_d", "0", []),

	("banner_kingdom_e", 0, "banner_kingdom_e", "0", []),

	("banner_kingdom_f", 0, "banner_kingdom_f", "0", []),

	("banner_kingdom_g", 0, "banner_kingdom_g", "0", []),

	("banner_kingdom_h", 0, "banner_kingdom_h", "0", []),

	("banner_kingdom_i", 0, "banner_kingdom_i", "0", []),

	("banner_kingdom_j", 0, "banner_kingdom_j", "0", []),

	("banner_kingdom_k", 0, "banner_kingdom_k", "0", []),

	("banner_kingdom_l", 0, "banner_kingdom_l", "0", []),

	("banner_kingdom_ll", 0, "banner_kingdom_ll", "0", []),

	("banner_kingdom_m", 0, "banner_kingdom_m", "0", []),

	("banner_kingdom_n", 0, "banner_kingdom_n", "0", []),

	("banner_kingdom_o", 0, "banner_kingdom_o", "0", []),

	("banner_kingdom_p", 0, "banner_kingdom_p", "0", []),

	("banner_kingdom_q", 0, "banner_kingdom_q", "0", []),

	("banner_kingdom_r", 0, "banner_kingdom_r", "0", []),

	("banner_kingdom_s", 0, "banner_kingdom_s", "0", []),

	("banner_kingdom_t", 0, "banner_kingdom_t", "0", []),

	("banner_kingdom_u", 0, "banner_kingdom_u", "0", []),

	("banner_kingdom_v", 0, "banner_kingdom_v", "0", []),

	("banner_kingdom_w", 0, "banner_kingdom_w", "0", []),

	("banner_kingdom_x", 0, "banner_kingdom_x", "0", []),

	("banner_kingdom_y", 0, "banner_kingdom_y", "0", []),

	("banner_kingdom_z", 0, "banner_kingdom_z", "0", []),

	("banner_kingdom_2a", 0, "banner_kingdom_2a", "0", []),

	("banner_kingdom_2b", 0, "banner_kingdom_2b", "0", []),

	("banner_kingdom_2c", 0, "banner_kingdom_2c", "0", []),

	("banner_kingdom_2d", 0, "banner_kingdom_2d", "0", []),

	("banner_k21", 0, "banner_k21", "0", []),

	("door_destructible", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable|spr_use_time(2), "tutorial_door_a", "bo_tutorial_door_a", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
			(get_max_players, ":max_players"),
			(try_for_range, ":localvariable", 1, ":max_players"),
				(player_is_active, ":localvariable"),
				(multiplayer_send_2_int_to_player, ":localvariable", 76, ":trigger_param_2", ":trigger_param_1"),
			(try_end)
		]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 2000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(play_sound, "snd_dummy_hit"),
			(particle_system_burst, "psys_dummy_smoke", 1, 3),
			(particle_system_burst, "psys_dummy_straw", 1, 10)
		])
	]),

	("tutorial_door_a", sokf_moveable, "tutorial_door_a", "bo_tutorial_door_a", []),

	("tutorial_door_b", sokf_moveable, "tutorial_door_b", "bo_tutorial_door_b", []),

	("tutorial_flag_yellow", sokf_moveable|sokf_face_player, "tutorial_flag_yellow", "0", []),

	("tutorial_flag_red", sokf_moveable|sokf_face_player, "tutorial_flag_red", "0", []),

	("tutorial_flag_blue", sokf_moveable|sokf_face_player, "tutorial_flag_blue", "0", []),

	("interior_prison_a", 0, "interior_prison_a", "bo_interior_prison_a", []),

	("interior_prison_b", 0, "interior_prison_b", "bo_interior_prison_b", []),

	("interior_prison_cell_a", 0, "interior_prison_cell_a", "bo_interior_prison_cell_a", []),

	("interior_prison_d", 0, "interior_prison_d", "bo_interior_prison_d", []),

	("arena_archery_target_a", 0, "arena_archery_target_a", "bo_arena_archery_target_a", []),

	("archery_butt_a", 0, "archery_butt", "bo_archery_butt", 
	[(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_get_position, 2, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(agent_get_position, 3, ":player_agent_no"),
			(get_distance_between_positions, ":distance_between_positions_3_2", 3, 2),
			(position_transform_position_to_local, 4, 2, 1),
			(position_set_y, 4, 0),
			(position_set_x, 2, 0),
			(position_set_y, 2, 0),
			(position_set_z, 2, 0),
			(get_distance_between_positions, ":distance_between_positions_4_2", 4, 2),
			(assign, ":value", 43),
			(val_sub, ":value", ":distance_between_positions_4_2"),
			(val_mul, ":value", 1299),
			(val_div, ":value", 4300),
			(try_begin),
				(lt, ":value", 0),
				(assign, ":value", 0),
			(try_end),
			(val_div, ":distance_between_positions_3_2", 91),
			(assign, reg60, ":value"),
			(assign, reg61, ":distance_between_positions_3_2"),
			(display_message, "str_archery_target_hit")
		])
	]),

	("archery_target_with_hit_a", 0, "arena_archery_target_a", "bo_arena_archery_target_a", 
	[(ti_on_scene_prop_hit,
		[])
	]),

	("dummy_a", sokf_destructible|sokf_moveable, "arena_archery_target_b", "bo_arena_archery_target_b", 
	[(ti_on_scene_prop_destroy,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_get_starting_position, 1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(agent_get_position, 2, ":player_agent_no"),
			(assign, ":var_3", 80),
			(try_begin),
				(position_is_behind_position, 2, 1),
				(val_mul, ":var_3", -1),
			(try_end),
			(position_rotate_x, 1, ":var_3"),
			(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(play_sound, "snd_dummy_destroyed")
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(assign, reg60, ":trigger_param_2"),
			(val_div, ":trigger_param_2", 8),
			(prop_instance_get_position, 2, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(agent_get_position, 3, ":player_agent_no"),
			(try_begin),
				(position_is_behind_position, 3, 2),
				(val_mul, ":trigger_param_2", -1),
			(try_end),
			(position_rotate_x, 2, ":trigger_param_2"),
			(display_message, "str_delivered_damage"),
			(prop_instance_animate_to_position, ":trigger_param_1", 2, 30),
			(play_sound, "snd_dummy_hit"),
			(particle_system_burst, "psys_dummy_smoke", 1, 3),
			(particle_system_burst, "psys_dummy_straw", 1, 10)
		])
	]),

	("band_a", 0, "band_a", "0", []),

	("arena_sign", 0, "arena_arms", "0", []),

	("castle_f_door_a", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "castle_f_door_a", "bo_castle_f_door_a", 
	[(ti_on_scene_prop_use,
		[]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 1000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("castle_f_doors_top_a", 0, "castle_f_doors_top_a", "bo_castle_f_doors_top_a", []),

	("castle_f_sally_door_a", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "castle_f_sally_door_a", "bo_castle_f_sally_door_a", 
	[(ti_on_scene_prop_use,
		[]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 1000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("battlement_a", 0, "battlement_a", "bo_battlement_a", []),

	("battlement_a_destroyed", 0, "battlement_a_destroyed", "bo_battlement_a_destroyed", []),

	("windmill_fan_turning", sokf_moveable, "windmill_fan_turning", "bo_windmill_fan_turning", []),

	("windmill_fan", 0, "windmill_fan", "bo_windmill_fan", []),

	("earth_wall_a", 0, "earth_wall_a", "bo_earth_wall_a", []),

	("earth_wall_a2", 0, "earth_wall_a2", "bo_earth_wall_a2", []),

	("earth_wall_b", 0, "earth_wall_b", "bo_earth_wall_b", []),

	("earth_wall_b2", 0, "earth_wall_b2", "bo_earth_wall_b2", []),

	("snowy_castle_battlement_a", 0, "snowy_castle_battlement_a", "bo_snowy_castle_battlement_a", []),

	("snowy_castle_battlement_a_destroyed", 0, "snowy_castle_battlement_a_destroyed", "bo_snowy_castle_battlement_a_destroyed", []),

	("castle_e_battlement_a", 0, "castle_e_battlement_a", "bo_castle_e_battlement_a", []),

	("castle_e_battlement_a_destroyed", 0, "castle_e_battlement_a_destroyed", "bo_castle_e_battlement_a_destroyed", []),

	("castle_e_sally_door_a", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "castle_e_sally_door_a", "bo_castle_e_sally_door_a", 
	[(ti_on_scene_prop_use,
		[]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 3000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("arena_block_a", 0, "arena_block_a", "bo_arena_block_ab", []),

	("arena_block_b", 0, "arena_block_b", "bo_arena_block_ab", []),

	("arena_block_d", 0, "arena_block_d", "bo_arena_block_def", []),

	("arena_block_e", 0, "arena_block_e", "bo_arena_block_def", []),

	("arena_block_f", 0, "arena_block_f", "bo_arena_block_def", []),

	("arena_block_g", 0, "arena_block_g", "bo_arena_block_ghi", []),

	("arena_block_h", 0, "arena_block_h", "bo_arena_block_ghi", []),

	("arena_block_i", 0, "arena_block_i", "bo_arena_block_ghi", []),

	("arena_palisade_a", 0, "arena_palisade_a", "bo_arena_palisade_a", []),

	("arena_wall_a", 0, "arena_wall_a", "bo_arena_wall_ab", []),

	("arena_wall_b", 0, "arena_wall_b", "bo_arena_wall_ab", []),

	("arena_barrier_b", 0, "arena_barrier_b", "bo_arena_barrier_bc", []),

	("arena_barrier_c", 0, "arena_barrier_c", "bo_arena_barrier_bc", []),

	("arena_tower_a", 0, "arena_tower_a", "bo_arena_tower_abc", []),

	("arena_tower_b", 0, "arena_tower_b", "bo_arena_tower_abc", []),

	("arena_tower_c", 0, "arena_tower_c", "bo_arena_tower_abc", []),

	("castle_battlement_a", 0, "castle_battlement_a", "bo_castle_battlement_a", []),

	("castle_battlement_b", 0, "castle_battlement_b", "bo_castle_battlement_b", []),

	("castle_battlement_a_destroyed", 0, "castle_battlement_a_destroyed", "bo_castle_battlement_a_destroyed", []),

	("castle_battlement_b_destroyed", 0, "castle_battlement_b_destroyed", "bo_castle_battlement_b_destroyed", []),

	("belfry_b", sokf_moveable, "belfry_b", "bo_belfry_b", []),

	("belfry_b_platform_a", sokf_moveable, "belfry_b_platform_a", "bo_belfry_b_platform_a", []),

	("belfry_old", 0, "belfry_a", "bo_belfry_a", []),

	("belfry_platform_a", sokf_moveable, "belfry_platform_a", "bo_belfry_platform_a", []),

	("belfry_platform_b", sokf_moveable, "belfry_platform_b", "bo_belfry_platform_b", []),

	("belfry_wheel_old", 0, "belfry_wheel", "0", []),

	("mangonel", 0, "mangonel", "bo_mangonel", []),

	("trebuchet_old", 0, "trebuchet_old", "bo_trebuchet_old", []),

	("trebuchet_new", 0, "trebuchet_new", "bo_trebuchet_old", []),

	("trebuchet_destructible", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "trebuchet_new", "bo_trebuchet_old", 
	[(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 2400)
		]),

		(ti_on_scene_prop_destroy,
		[]),

		(ti_on_scene_prop_hit,
		[])
	]),

	("stone_ball", 0, "stone_ball", "0", []),

	("ramp_12m", 0, "ramp_12m", "bo_ramp_12m", []),

	("ramp_14m", 0, "ramp_14m", "bo_ramp_14m", []),

	("siege_ladder_move_6m", sokf_type_ladder|sokf_moveable|spr_use_time(2), "siege_ladder_move_6m", "bo_siege_ladder_move_6m", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
			(get_max_players, ":max_players"),
			(try_for_range, ":localvariable", 1, ":max_players"),
				(player_is_active, ":localvariable"),
				(multiplayer_send_2_int_to_player, ":localvariable", 76, ":trigger_param_2", ":trigger_param_1"),
			(try_end)
		]),

		(ti_on_scene_prop_is_animating,
		[]),

		(ti_on_scene_prop_animation_finished,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_enable_physics, ":trigger_param_1", 1)
		])
	]),

	("siege_ladder_move_8m", sokf_type_ladder|sokf_moveable|spr_use_time(2), "siege_ladder_move_8m", "bo_siege_ladder_move_8m", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
			(get_max_players, ":max_players"),
			(try_for_range, ":localvariable", 1, ":max_players"),
				(player_is_active, ":localvariable"),
				(multiplayer_send_2_int_to_player, ":localvariable", 76, ":trigger_param_2", ":trigger_param_1"),
			(try_end)
		]),

		(ti_on_scene_prop_is_animating,
		[]),

		(ti_on_scene_prop_animation_finished,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_enable_physics, ":trigger_param_1", 1)
		])
	]),

	("siege_ladder_move_10m", sokf_type_ladder|sokf_moveable|spr_use_time(3), "siege_ladder_move_10m", "bo_siege_ladder_move_10m", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
			(get_max_players, ":max_players"),
			(try_for_range, ":localvariable", 1, ":max_players"),
				(player_is_active, ":localvariable"),
				(multiplayer_send_2_int_to_player, ":localvariable", 76, ":trigger_param_2", ":trigger_param_1"),
			(try_end)
		]),

		(ti_on_scene_prop_is_animating,
		[]),

		(ti_on_scene_prop_animation_finished,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_enable_physics, ":trigger_param_1", 1)
		])
	]),

	("siege_ladder_move_12m", sokf_type_ladder|sokf_moveable|spr_use_time(3), "siege_ladder_move_12m", "bo_siege_ladder_move_12m", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
			(get_max_players, ":max_players"),
			(try_for_range, ":localvariable", 1, ":max_players"),
				(player_is_active, ":localvariable"),
				(multiplayer_send_2_int_to_player, ":localvariable", 76, ":trigger_param_2", ":trigger_param_1"),
			(try_end)
		]),

		(ti_on_scene_prop_is_animating,
		[]),

		(ti_on_scene_prop_animation_finished,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_enable_physics, ":trigger_param_1", 1)
		])
	]),

	("siege_ladder_move_14m", sokf_type_ladder|sokf_moveable|spr_use_time(4), "siege_ladder_move_14m", "bo_siege_ladder_move_14m", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
			(get_max_players, ":max_players"),
			(try_for_range, ":localvariable", 1, ":max_players"),
				(player_is_active, ":localvariable"),
				(multiplayer_send_2_int_to_player, ":localvariable", 76, ":trigger_param_2", ":trigger_param_1"),
			(try_end)
		]),

		(ti_on_scene_prop_is_animating,
		[]),

		(ti_on_scene_prop_animation_finished,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_enable_physics, ":trigger_param_1", 1)
		])
	]),

	("bed_d", 0, "bed_d", "bo_bed_d", []),

	("bed_e", 0, "bed_e", "bo_bed_e", []),

	("towngate_door_left", sokf_moveable, "door_g_left", "bo_door_left", []),

	("towngate_door_right", sokf_moveable, "door_g_right", "bo_door_right", []),

	("door_screen", sokf_moveable, "door_screen", "0", []),

	("door_a", sokf_moveable, "door_a", "bo_door_a", []),

	("door_c", sokf_moveable, "door_c", "bo_door_a", []),

	("door_d", sokf_moveable, "door_d", "bo_door_a", []),

	("tavern_door_a", sokf_moveable, "tavern_door_a", "bo_tavern_door_a", []),

	("tavern_door_b", sokf_moveable, "tavern_door_b", "bo_tavern_door_a", []),

	("door_e_left", sokf_moveable, "door_e_left", "bo_door_left", []),

	("door_e_right", sokf_moveable, "door_e_right", "bo_door_right", []),

	("door_f_left", sokf_moveable, "door_f_left", "bo_door_left", []),

	("door_f_right", sokf_moveable, "door_f_right", "bo_door_right", []),

	("door_h_left", sokf_moveable, "door_g_left", "bo_door_left", []),

	("door_h_right", sokf_moveable, "door_g_right", "bo_door_right", []),

	("draw_bridge_a", 0, "draw_bridge_a", "bo_draw_bridge_a", []),

	("chain_1m", 0, "chain_1m", "0", []),

	("chain_2m", 0, "chain_2m", "0", []),

	("chain_5m", 0, "chain_5m", "0", []),

	("chain_10m", 0, "chain_10m", "0", []),

	("church_a", 0, "church_a", "bo_church_a", []),

	("church_tower_a", 0, "church_tower_a", "bo_church_tower_a", []),

	("stone_step_a", 0, "floor_stone_a", "bo_floor_stone_a", []),

	("stone_step_b", 0, "stone_step_b", "0", []),

	("stone_step_c", 0, "stone_step_c", "0", []),

	("stone_heap", 0, "stone_heap", "bo_stone_heap", []),

	("panel_door_a", 0, "house_door_a", "bo_house_door_a", []),

	("panel_door_b", 0, "house_door_b", "bo_house_door_a", []),

	("smoke_stain", 0, "soot_a", "0", []),

	("tripod_cauldron_a", 0, "tripod_cauldron_a", "bo_tripod_cauldron_a", []),

	("tripod_cauldron_b", 0, "tripod_cauldron_b", "bo_tripod_cauldron_b", []),

	("cauldron_a", 0, "cauldron_a", "bo_cauldron_a", []),

	("fry_pan_a", 0, "fry_pan_a", "0", []),

	("open_stable_a", 0, "open_stable_a", "bo_open_stable_a", []),

	("open_stable_b", 0, "open_stable_b", "bo_open_stable_b", []),

	("lettuce", 0, "lettuce", "0", []),

	("hanger", 0, "hanger", "0", []),

	("knife_eating", 0, "knife_eating", "0", []),

	("colander", 0, "colander", "0", []),

	("ladle", 0, "ladle", "0", []),

	("spoon", 0, "spoon", "0", []),

	("skewer", 0, "skewer", "0", []),

	("grape_a", 0, "grape_a", "0", []),

	("grape_b", 0, "grape_b", "0", []),

	("apple_a", 0, "apple_a", "0", []),

	("apple_b", 0, "apple_b", "0", []),

	("maize_a", 0, "maize_a", "0", []),

	("maize_b", 0, "maize_b", "0", []),

	("cabbage", 0, "cabbage", "0", []),

	("flax_bundle", 0, "raw_flax", "0", []),

	("olive_plane", 0, "olive_plane", "0", []),

	("grapes_plane", 0, "grapes_plane", "0", []),

	("date_fruit_plane", 0, "date_fruit_plane", "0", []),

	("bowl", 0, "bowl_big", "0", []),

	("bowl_small", 0, "bowl_small", "0", []),

	("dye_blue", 0, "raw_dye_blue", "0", []),

	("dye_red", 0, "raw_dye_red", "0", []),

	("dye_yellow", 0, "raw_dye_yellow", "0", []),

	("basket", 0, "basket_small", "0", []),

	("basket_big", 0, "basket_large", "0", []),

	("basket_big_green", 0, "basket_big", "0", []),

	("leatherwork_frame", 0, "leatherwork_frame", "0", []),

	("cabbage_b", 0, "cabbage_b", "0", []),

	("bean", 0, "bean", "0", []),

	("basket_a", 0, "basket_a", "bo_basket_a", []),

	("feeding_trough_a", 0, "feeding_trough_a", "bo_feeding_trough_a", []),

	("marrow_a", 0, "marrow_a", "0", []),

	("marrow_b", 0, "marrow_b", "0", []),

	("squash_plant", 0, "marrow_c", "0", []),

	("winch", sokf_moveable, "winch", "bo_winch", []),

	("winch_b", sokf_moveable|spr_use_time(5), "winch_b", "bo_winch", 
	[(ti_on_scene_prop_use,
		[])
	]),

	("drawbridge", 0, "drawbridge", "bo_drawbridge", []),

	("gatehouse_door_left", sokf_moveable, "gatehouse_door_left", "bo_gatehouse_door_left", []),

	("gatehouse_door_right", sokf_moveable, "gatehouse_door_right", "bo_gatehouse_door_right", []),

	("candle_a", 0, "candle_a", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, 0, 27),
			(particle_system_add_new, "psys_candle_light")
		])
	]),

	("candle_c", 0, "candle_c", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, 0, 10),
			(particle_system_add_new, "psys_candle_light_small")
		])
	]),

	("hook_a", 0, "hook_a", "0", []),

	("window_night", 0, "window_night", "0", []),

	("fried_pig", 0, "pork", "0", []),

	("village_oven", 0, "village_oven", "bo_village_oven", []),

	("dungeon_water_drops", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_dungeon_water_drops")
		])
	]),

	("shadow_circle_1", 0, "shadow_circle_1", "0", []),

	("shadow_circle_2", 0, "shadow_circle_2", "0", []),

	("shadow_square_1", 0, "shadow_square_1", "0", []),

	("shadow_square_2", 0, "shadow_square_2", "0", []),

	("wheelbarrow", 0, "wheelbarrow", "bo_wheelbarrow", []),

	("gourd", sokf_destructible|sokf_moveable|sokf_enforce_shadows|spr_hit_points(1), "gourd", "bo_gourd", 
	[(ti_on_scene_prop_destroy,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_get_position, 1, ":trigger_param_1"),
			(copy_position, 2, 1),
			(position_set_z, 2, -100000),
			(particle_system_burst, "psys_gourd_smoke", 1, 2),
			(particle_system_burst, "psys_gourd_piece_1", 1, 1),
			(particle_system_burst, "psys_gourd_piece_2", 1, 5),
			(prop_instance_animate_to_position, ":trigger_param_1", 2, 1),
			(play_sound, "snd_gourd_destroyed")
		])
	]),

	("gourd_spike", sokf_moveable, "gourd_spike", "bo_gourd_spike", []),

	("desert_plant_a", 0, "desert_plant_a", "0", []),

	("tree_a01", 0, "tree_a01", "bo_tree_a01", []),

	("stairs_a", sokf_type_ladder, "stairs_a", "bo_stairs_a", []),

	("headquarters_flag_red", sokf_moveable|sokf_face_player, "tutorial_flag_red", "0", []),

	("headquarters_flag_blue", sokf_moveable|sokf_face_player, "tutorial_flag_blue", "0", []),

	("headquarters_flag_gray", sokf_moveable|sokf_face_player, "tutorial_flag_yellow", "0", []),

	("headquarters_flag_red_code_only", sokf_moveable|sokf_face_player, "mp_flag_red", "0", []),

	("headquarters_flag_blue_code_only", sokf_moveable|sokf_face_player, "mp_flag_blue", "0", []),

	("headquarters_flag_gray_code_only", sokf_moveable|sokf_face_player, "mp_flag_white", "0", []),

	("headquarters_pole_code_only", sokf_moveable, "mp_flag_pole", "0", []),

	("headquarters_flag_swadian", sokf_moveable|sokf_face_player, "flag_swadian", "0", []),

	("headquarters_flag_vaegir", sokf_moveable|sokf_face_player, "flag_vaegir", "0", []),

	("headquarters_flag_khergit", sokf_moveable|sokf_face_player, "flag_khergit", "0", []),

	("headquarters_flag_nord", sokf_moveable|sokf_face_player, "flag_nord", "0", []),

	("headquarters_flag_rhodok", sokf_moveable|sokf_face_player, "flag_rhodok", "0", []),

	("headquarters_flag_sarranid", sokf_moveable|sokf_face_player, "flag_sarranid", "0", []),

	("glow_a", 0, "glow_a", "0", []),

	("glow_b", 0, "glow_b", "0", []),

	("dummy_a_undestructable", sokf_destructible, "arena_archery_target_b", "bo_arena_archery_target_b", 
	[(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 10000000)
		]),

		(ti_on_scene_prop_hit,
		[])
	]),

	("cave_entrance_1", 0, "cave_entrance_1", "bo_cave_entrance_1", []),

	("pointer_arrow", 0, "pointer_arrow", "0", []),

	("desert_field", 0, "desert_field", "bo_desert_field", []),

	("harbour_a", 0, "harbour_a", "bo_harbour_a", []),

	("sea_foam_a", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_sea_foam_a")
		])
	]),

	("viking_keep_destroy", 0, "viking_keep_destroy", "bo_viking_keep_destroy", []),

	("viking_keep_destroy_door", 0, "viking_keep_destroy_door", "bo_viking_keep_destroy_door", []),

	("earth_tower_small_b", 0, "earth_tower_small_b", "bo_earth_tower_small_b", []),

	("earth_gate_house_b", 0, "earth_gate_house_b", "bo_earth_gate_house_b", []),

	("earth_tower_a", 0, "earth_tower_a", "bo_earth_tower_a", []),

	("earth_stairs_c", 0, "earth_stairs_c", "bo_earth_stairs_c", []),

	("earth_sally_gate_left", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "earth_sally_gate_left", "bo_earth_sally_gate_left", 
	[(ti_on_scene_prop_use,
		[]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 2000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("earth_sally_gate_right", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "earth_sally_gate_right", "bo_earth_sally_gate_right", 
	[(ti_on_scene_prop_use,
		[]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 2000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("barrier_box", sokf_type_barrier3d|sokf_invisible, "barrier_box", "bo_barrier_box", []),

	("barrier_capsule", sokf_type_barrier3d|sokf_invisible, "barrier_capsule", "bo_barrier_capsule", []),

	("barrier_cone", sokf_type_barrier3d|sokf_invisible, "barrier_cone", "bo_barrier_cone", []),

	("barrier_sphere", sokf_type_barrier3d|sokf_invisible, "barrier_sphere", "bo_barrier_sphere", []),

	("viking_keep_destroy_sally_door_right", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "viking_keep_destroy_sally_door_right", "bo_viking_keep_destroy_sally_door_right", 
	[(ti_on_scene_prop_use,
		[]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 1000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("viking_keep_destroy_sally_door_left", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "viking_keep_destroy_sally_door_left", "bo_viking_keep_destroy_sally_door_left", 
	[(ti_on_scene_prop_use,
		[]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 1000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("castle_f_door_b", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "castle_e_sally_door_a", "bo_castle_e_sally_door_a", 
	[(ti_on_scene_prop_use,
		[]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 1000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("ctf_flag_kingdom_1", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_1", "0", []),

	("ctf_flag_kingdom_2", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_2", "0", []),

	("ctf_flag_kingdom_3", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_3", "0", []),

	("ctf_flag_kingdom_4", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_4", "0", []),

	("ctf_flag_kingdom_5", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_5", "0", []),

	("ctf_flag_kingdom_6", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_6", "0", []),

	("ctf_flag_kingdom_7", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_7", "0", []),

	("headquarters_flag_rebel", sokf_moveable|sokf_face_player, "flag_rebel", "0", []),

	("wood_heap", 0, "wood_heap_a", "bo_wood_heap_a", []),

	("net_b", 0, "net_b", "0", []),

	("cheese_a", 0, "cheese_a", "0", []),

	("cheese_b", 0, "cheese_b", "0", []),

	("cheese_slice_a", 0, "cheese_slice_a", "0", []),

	("fish_a", 0, "fish_a", "0", []),

	("fish_roasted_a", 0, "fish_roasted_a", "0", []),

	("chicken_roasted", 0, "chicken", "0", []),

	("food_steam", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, 0, 0),
			(particle_system_add_new, "psys_food_steam")
		])
	]),

	("city_smoke", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(store_time_of_day, reg12),
			(neg|is_between, reg12, 5, 20),
			(set_position_delta, 0, 0, 0),
			(particle_system_add_new, "psys_night_smoke_1")
		])
	]),

	("city_fire_fly_night", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(store_time_of_day, reg12),
			(neg|is_between, reg12, 5, 20),
			(set_position_delta, 0, 0, 0),
			(particle_system_add_new, "psys_fire_fly_1")
		])
	]),

	("city_fly_day", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_bug_fly_1")
		])
	]),

	("flue_smoke_tall", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_flue_smoke_tall")
		])
	]),

	("flue_smoke_short", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_flue_smoke_short")
		])
	]),

	("moon_beam", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_moon_beam_1"),
			(particle_system_add_new, "psys_moon_beam_paricle_1")
		])
	]),

	("fire_small", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_fireplace_fire_small")
		])
	]),

	("fire_big", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_fireplace_fire_big")
		])
	]),

	("battle_field_smoke", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_war_smoke_tall")
		])
	]),

	("Village_fire_big", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_village_fire_big"),
			(set_position_delta, 0, 0, 100),
			(particle_system_add_new, "psys_village_fire_smoke_big")
		])
	]),

	("aqueduct", 0, "0", "0", []),

	("portcullis", 0, "portcullis_a", "bo_portcullis_a", []),

	("arena_2", 0, "0", "0", []),

	("arena_barrier_a", 0, "arena_barrier_a", "bo_arena_barrier_a", []),

	("arena_block_c", 0, "arena_block_c", "bo_arena_block_c", []),

	("tavern_table_a", 0, "tavern_table_a", "0", []),

	("table_trunk_a", 0, "table_trunk_a", "bo_table_trunk_a", []),

	("chair", 0, "tavern_chair_b", "0", []),

	("door_b", sokf_moveable, "door_b", "bo_door_a", []),

	("table_round_b", 0, "table_round_b", "bo_table_round_b", []),

	("bed_b", 0, "bed_b", "bo_bed_b", []),

	("bed_c", 0, "bed_c", "bo_bed_c", []),

	("carpet_with_pillows_a", 0, "carpet_with_pillows_a", "bo_carpet_with_pillows", []),

	("carpet_with_pillows_b", 0, "carpet_with_pillows_b", "bo_carpet_with_pillows", []),

	("table_round_a", 0, "table_round_a", "bo_table_round_a", []),

	("fireplace_b", 0, "fireplace_b", "bo_fireplace_b", []),

	("fireplace_c", 0, "fireplace_c", "bo_fireplace_c", []),

	("sofa_a", 0, "sofa_a", "bo_sofa", []),

	("sofa_b", 0, "sofa_b", "bo_sofa", []),

	("ewer_a", 0, "ewer_a", "bo_ewer_a", []),

	("cupboard_a", 0, "cupboard_a", "bo_cupboard_a", []),

	("plate_a", 0, "plate_a", "0", []),

	("plate_b", 0, "plate_b", "0", []),

	("plate_c", 0, "plate_c", "0", []),

	("bread_a", 0, "bread_a", "0", []),

	("bread_b", 0, "bread_b", "0", []),

	("bread_slice_a", 0, "bread_slice_a", "0", []),

	("rock_dynamic_physics", sokf_moveable|sokf_dynamic_physics, "rock_a", "borock_a", []),

	("rock_hold", 0, "rock_a", "0", []),

	("5_fire_ball_physics", sokf_moveable|sokf_dynamic_physics, "5_fire_ball", "bo_5_fire_ball", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_fireplace_fire_big"),
			(set_position_delta, 0, 0, 100),
			(particle_system_add_new, "psys_village_fire_smoke_big")
		])
	]),

	("5_fire_ball_hold", 0, "5_fire_ball", "bo_5_fire_ball", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_fireplace_fire_big"),
			(set_position_delta, 0, 0, 100),
			(particle_system_add_new, "psys_village_fire_smoke_big")
		])
	]),

	("5_big_smoke", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, 0, 0),
			(particle_system_add_new, "psys_village_fire_smoke_big")
		])
	]),

	("cow_a", 0, "0", "0", []),

	("cow_b", 0, "0", "0", []),

	("cow_c", 0, "0", "0", []),

	("cow_d", 0, "0", "0", []),

	("donkey", 0, "0", "0", []),

	("goat", 0, "0", "0", []),

	("goat_c", 0, "0", "0", []),

	("wild_donkey", 0, "0", "0", []),

	("camel_2", 0, "camel_2", "0", []),

	("bed_a", 0, "bed_a", "bo_bed_a", []),

	("barrel", 0, "barrel", "bobarrel", []),

	("lamp_b", 0, "lamp_b", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 65, 0, -7),
			(particle_system_add_new, "psys_lamp_fire"),
			(set_position_delta, 70, 0, -5),
			(particle_system_add_new, "psys_fire_glow_1"),
			(particle_system_emit, "psys_fire_glow_1", 9000000),
			(play_sound, "snd_fire_loop", 0)
		])
	]),

	("net_a", 0, "net_a", "bo_net_a", []),

	("cooking_fire", 0, "fire_floor", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, 0, 12),
			(particle_system_add_new, "psys_cooking_fire_1"),
			(particle_system_add_new, "psys_fire_sparks_1"),
			(particle_system_add_new, "psys_cooking_smoke"),
			(set_position_delta, 0, 0, 50),
			(particle_system_add_new, "psys_fire_glow_1"),
			(particle_system_emit, "psys_fire_glow_1", 9000000)
		])
	]),

	("box_a", 0, "box_a", "bo_box_a", []),

	("box_a_dynamic", sokf_moveable|sokf_dynamic_physics, "box_a", "bo_box_a", []),

	("bed_f", 0, "bed_f", "bo_bed_f", []),

	("carpet_d", 0, "carpet_d", "0", []),

	("carpet_e", 0, "carpet_e", "0", []),

	("carpet_f", 0, "carpet_f", "0", []),

	("stone_heap_b", 0, "stone_heap_b", "0", []),

	("wood_heap_b", 0, "wood_heap_b", "bo_wood_heap_b", []),

	("straw_b", 0, "straw_b", "0", []),

	("straw_c", 0, "straw_c", "0", []),

	("brazier_with_fire", 0, "brazier", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, 0, 85),
			(particle_system_add_new, "psys_brazier_fire_1"),
			(particle_system_add_new, "psys_fire_sparks_1"),
			(set_position_delta, 0, 0, 100),
			(particle_system_add_new, "psys_fire_glow_1"),
			(particle_system_emit, "psys_fire_glow_1", 9000000)
		])
	]),

	("village_stand", 0, "village_stand", "0", []),

	("jug", 0, "jug", "0", []),

	("cup", 0, "cup", "0", []),

	("shelves", 0, "shelves", "boshelves", []),

	("candle_b", 0, "candle_b", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, 0, 25),
			(particle_system_add_new, "psys_candle_light")
		])
	]),

	("gothic_chair", 0, "gothic_chair", "bogothic_chair", []),

	("bucket_a", 0, "bucket_a", "0", []),

	("bridge_b", 0, "bridge_b", "bo_bridge_b", []),

	("bridge_modular_a", 0, "bridge_modular_a", "bo_bridge_modular_a", []),

	("bridge_modular_b", 0, "bridge_modular_b", "bo_bridge_modular_b", []),

	("water_river", 0, "water_plane", "0", []),

	("siege_ladder_6m", sokf_type_ladder, "siege_ladder_move_6m", "bo_siege_ladder_move_6m", []),

	("siege_ladder_8m", sokf_type_ladder, "siege_ladder_move_8m", "bo_siege_ladder_move_8m", []),

	("siege_ladder_10m", sokf_type_ladder, "siege_ladder_move_10m", "bo_siege_ladder_move_10m", []),

	("siege_ladder_12m", sokf_type_ladder, "siege_ladder_12m", "bo_siege_ladder_12m", []),

	("siege_ladder_14m", sokf_type_ladder, "siege_ladder_14m", "bo_siege_ladder_14m", []),

	("arena_spectator_a", 0, "arena_spectator_a", "0", []),

	("arena_spectator_b", 0, "arena_spectator_b", "0", []),

	("arena_spectator_c", 0, "arena_spectator_c", "0", []),

	("arena_spectator_sitting_a", 0, "arena_spectator_sitting_a", "0", []),

	("arena_spectator_sitting_b", 0, "arena_spectator_sitting_b", "0", []),

	("arena_spectator_sitting_c", 0, "arena_spectator_sitting_c", "0", []),

	("belfry_wheel", sokf_moveable, "belfry_wheel", "0", []),

	("tent", 0, "arabian_tent_2", "0", []),

	("410_tent", 0, "new_tent", "bo_new_tent", []),

	("5_river_flood", 0, "water_plane", "0", []),

	("5_stand_cloth", 0, "stand_cloth", "0", []),

	("5_stand_thatched", 0, "stand_thatched", "0", []),

	("5_grave_a", 0, "grave_a", "0", []),

	("5_arabian_parterre_a", 0, "arabian_parterre_a", "0", []),

	("5_counter_tavern", 0, "counter_tavern.3", "bocounter_tavern", []),

	("5_grate", 0, "grate", "bograte", []),

	("5_winery_wine_cart_empty", 0, "winery_wine_cart_empty", "0", []),

	("5_mill_flour_sack_desk_a", 0, "mill_flour_sack_desk_a", "0", []),

	("5_smithy_forge_bellows", 0, "smithy_forge_bellows", "0", []),

	("5_smithy_grindstone_wheel", 0, "smithy_grindstone_wheel", "0", []),

	("5_smithy_anvil", 0, "smithy_anvil", "0", []),

	("5_water_well_a", 0, "water_well_a", "0", []),

	("5_fence", 0, "fence", "0", []),

	("5_bridge_wooden", 0, "bridge_wooden", "bo_bridge_wooden", []),

	("5_bridge_wooden_snowy", 0, "bridge_wooden_snowy", "bo_bridge_wooden", []),

	("5_angry_wheat", 0, "5_angry_wheat", "0", []),

	("ply_strat_barrier", sokf_invisible, "ply_strat_barrier", "bo_ply_strat_barrier", []),

	("castle_h_battlement_a", 0, "7771_wall", "bo_77712_wall_destroy", []),

	("6663_castle_wall_on_off", 0, "7771_wall", "bo_77712_wall_destroy", []),

	("6663_castle_wall_destory", 0, "7771_wall", "bo_77712_wall_destroy", []),

	("castle_h_stairs_new_1", 0, "7771_castle_h_stairs_new_1", "bo_castle_e_stairs_a", []),

	("castle_h_battlement_barrier", 0, "castle_h_battlement_barrier", "bo_castle_h_battlement_barrier", []),

	("castle_h_corner_a", 0, "castle_h_corner_a", "bo_castle_h_corner_a", []),

	("7771_guard_tower", 0, "7771_guard_tower", "bo_earth_tower_a", []),

	("7771_castle_gatehouse_1", 0, "7771_castle_gatehouse_1", "bo_castle_f_gatehouse_a", []),

	("7771_inner_gate", 0, "7771_inner_gate", "bo_7771_inner_gate", []),

	("7771_wall_belfry", 0, "7771_wall_belfry", "bo_7771_wall_belfry", []),

	("77712_wall", 0, "77712_wall", "bo_77712_wall_destroy", []),

	("77712_wall_on_off", 0, "77712_wall", "bo_77712_wall_destroy", []),

	("77712_wall_destory", 0, "77712_wall_destroy", "bo_77712_wall_destroy", []),

	("77712_stair", 0, "77712_stair", "bo_castle_e_stairs_a", []),

	("77712_river_block", 0, "77712_river_block", "bo_castle_h_battlement_barrier", []),

	("77712_corner_a", 0, "77712_corner_a", "bo_77712_corner_a", []),

	("77712_guard_tower", 0, "77712_guard_tower", "bo_earth_tower_a", []),

	("77712_gatehouse", 0, "77712_gate_house", "bo_77712_gate_house", []),

	("77712_inner_gate", 0, "77712_inner_gate", "bo_77712_inner_gate", []),

	("77712_wall_belfry", 0, "77712_wall_belfry", "bo_7771_wall_belfry", []),

	("77713_wall", 0, "77713_wall", "bo_77712_wall_destroy", []),

	("77713_wall_on_off", 0, "77713_wall", "bo_77712_wall_destroy", []),

	("77713_wall_destory", 0, "77713_wall_destroy", "bo_77712_wall_destroy", []),

	("77713_stair", 0, "77713_stair", "bo_castle_e_stairs_a", []),

	("77713_river_block", 0, "77713_river_block", "bo_castle_h_battlement_barrier", []),

	("77713_corner_a", 0, "77713_corner_a", "bo_77713_corner_a", []),

	("77713_guard_tower", 0, "77713_guard_tower", "bo_earth_tower_a", []),

	("77713_gatehouse", 0, "77713_gatehouse", "bo_castle_f_gatehouse_a", []),

	("77713_inner_gate", 0, "77713_inner_gate", "bo_77712_inner_gate", []),

	("77713_wall_belfry", 0, "77713_wall_belfry", "bo_7771_wall_belfry", []),

	("7772_wall", 0, "7772_wall", "bo_77712_wall_destroy", []),

	("7772_wall_on_off", 0, "7772_wall", "bo_77712_wall_destroy", []),

	("7772_wall_destory", 0, "7772_wall", "bo_77712_wall_destroy", []),

	("7772_stair", 0, "7772_stair", "bo_castle_e_stairs_a", []),

	("7772_river_block", 0, "7772_river_block", "bo_castle_h_battlement_barrier", []),

	("7772_corner_a", 0, "7772_corner_a", "bo_castle_h_corner_a", []),

	("7772_guard_tower", 0, "7772_guard_tower", "bo_earth_tower_a", []),

	("7772_gatehouse", 0, "7772_gatehouse", "bo_castle_f_gatehouse_a", []),

	("7772_inner_gate", 0, "7772_inner_gate", "bo_7771_inner_gate", []),

	("7772_wall_belfry", 0, "7772_wall_belfry", "bo_7771_wall_belfry", []),

	("77722_wall", 0, "77722_wall", "bo_77712_wall_destroy", []),

	("77722_wall_on_off", 0, "77722_wall", "bo_77712_wall_destroy", []),

	("77722_wall_destory", 0, "77722_wall", "bo_77712_wall_destroy", []),

	("77722_stair", 0, "77722_stair", "bo_castle_e_stairs_a", []),

	("77722_river_block", 0, "77722_river_block", "bo_castle_h_battlement_barrier", []),

	("77722_corner_a", 0, "77722_corner_a", "bo_77722_corner_a", []),

	("77722_guard_tower", 0, "77722_guard_tower", "bo_earth_tower_a", []),

	("77722_gatehouse", 0, "77722_gatehouse", "bo_77722_gatehouse", []),

	("77722_inner_gate", 0, "77722_inner_gate", "bo_77722_inner_gate", []),

	("77722_wall_belfry", 0, "77722_wall_belfry", "bo_7771_wall_belfry", []),

	("7773_wall", 0, "7773_wall", "bo_77712_wall_destroy", []),

	("7773_wall_on_off", 0, "7773_wall", "bo_77712_wall_destroy", []),

	("7773_wall_destory", 0, "7773_wall", "bo_77712_wall_destroy", []),

	("7773_stair", 0, "7773_stair", "bo_castle_e_stairs_a", []),

	("7773_river_block", 0, "7773_river_block", "bo_castle_h_battlement_barrier", []),

	("7773_corner_a", 0, "7773_corner_a", "bo_7773_corner_a", []),

	("7773_guard_tower", 0, "7773_guard_tower", "bo_earth_tower_a", []),

	("7773_gatehouse", 0, "7773_gatehouse", "bo_7773_gatehouse", []),

	("7773_inner_gate", 0, "7773_inner_gate", "bo_7773_inner_gate", []),

	("7773_wall_belfry", 0, "7773_wall_belfry", "bo_7771_wall_belfry", []),

	("7774_wall", 0, "7774_wall", "bo_77712_wall_destroy", []),

	("7774_wall_on_off", 0, "7774_wall", "bo_77712_wall_destroy", []),

	("7774_wall_destory", 0, "7774_wall_destroy", "bo_77712_wall_destroy", []),

	("7774_stair", 0, "7774_stair", "bo_castle_e_stairs_a", []),

	("7774_river_block", 0, "7774_river_block", "bo_castle_h_battlement_barrier", []),

	("7774_corner_a", 0, "7774_corner_a", "bo_77712_corner_a", []),

	("7774_guard_tower", 0, "7774_guard_tower", "bo_earth_tower_a", []),

	("7774_gatehouse", 0, "7774_gate_house", "bo_77712_gate_house", []),

	("7774_inner_gate", 0, "7774_inner_gate", "bo_77712_inner_gate", []),

	("7774_wall_belfry", 0, "7774_wall_belfry", "bo_7771_wall_belfry", []),

	("77742_wall", 0, "77742_wall", "bo_77712_wall_destroy", []),

	("77742_wall_on_off", 0, "77742_wall", "bo_77712_wall_destroy", []),

	("77742_wall_destory", 0, "77742_wall_destroy", "bo_77712_wall_destroy", []),

	("77742_stair", 0, "7774_stair", "bo_castle_e_stairs_a", []),

	("77742_river_block", 0, "7774_river_block", "bo_castle_h_battlement_barrier", []),

	("77742_corner_a", 0, "77742_corner_a", "bo_77713_corner_a", []),

	("77742_guard_tower", 0, "7774_guard_tower", "bo_earth_tower_a", []),

	("77742_gatehouse", 0, "77742_gatehouse", "bo_castle_f_gatehouse_a", []),

	("77742_inner_gate", 0, "7774_inner_gate", "bo_77712_inner_gate", []),

	("77742_wall_belfry", 0, "7774_wall_belfry", "bo_7771_wall_belfry", []),

	("7775_wall", 0, "7775_wall", "bo_77712_wall_destroy", []),

	("7775_wall_on_off", 0, "7775_wall", "bo_77712_wall_destroy", []),

	("7775_wall_destory", 0, "7775_wall_destroy", "bo_77712_wall_destroy", []),

	("7775_stair", 0, "7775_stair", "bo_castle_e_stairs_a", []),

	("7775_river_block", 0, "7775_river_block", "bo_castle_h_battlement_barrier", []),

	("7775_corner_a", 0, "7775_corner_a", "bo_77713_corner_a", []),

	("7775_guard_tower", 0, "7775_guard_tower", "bo_earth_tower_a", []),

	("7775_gatehouse", 0, "7775_gatehouse", "bo_castle_f_gatehouse_a", []),

	("7775_inner_gate", 0, "7775_inner_gate", "bo_77712_inner_gate", []),

	("7775_wall_belfry", 0, "7775_wall_belfry", "bo_7771_wall_belfry", []),

	("77752_wall", 0, "77752_wall", "bo_77712_wall_destroy", []),

	("77752_wall_on_off", 0, "77752_wall", "bo_77712_wall_destroy", []),

	("77752_wall_destory", 0, "77752_wall_destroy", "bo_77712_wall_destroy", []),

	("77752_stair", 0, "77752_stair", "bo_castle_e_stairs_a", []),

	("77752_river_block", 0, "77752_river_block", "bo_castle_h_battlement_barrier", []),

	("77752_corner_a", 0, "77752_corner_a", "bo_77713_corner_a", []),

	("77752_guard_tower", 0, "77752_guard_tower", "bo_earth_tower_a", []),

	("77752_gatehouse", 0, "77752_gatehouse", "bo_castle_f_gatehouse_a", []),

	("77752_inner_gate", 0, "77752_inner_gate", "bo_77712_inner_gate", []),

	("77752_wall_belfry", 0, "77752_wall_belfry", "bo_7771_wall_belfry", []),

	("7776_wall", 0, "7776_wall", "bo_77712_wall_destroy", []),

	("7776_wall_on_off", 0, "7776_wall", "bo_77712_wall_destroy", []),

	("7776_wall_destory", 0, "7776_wall", "bo_77712_wall_destroy", []),

	("7776_stair", 0, "7776_stair", "bo_castle_e_stairs_a", []),

	("7776_river_block", 0, "7776_river_block", "bo_castle_h_battlement_barrier", []),

	("7776_corner_a", 0, "7776_corner_a", "bo_7776_corner_a", []),

	("7776_guard_tower", 0, "7776_guard_tower", "bo_7776_guard_tower", []),

	("7776_gatehouse", 0, "7776_gate_house", "bo_7776_gate_house", []),

	("7776_inner_gate", 0, "7776_inner_gate", "bo_7776_inner_gate", []),

	("7776_wall_belfry", 0, "7776_wall_belfry", "bo_7771_wall_belfry", []),

	("77762_wall", 0, "77762_wall", "bo_77712_wall_destroy", []),

	("77762_wall_on_off", 0, "77762_wall", "bo_77712_wall_destroy", []),

	("77762_wall_destory", 0, "77762_wall", "bo_77712_wall_destroy", []),

	("77762_stair", 0, "77762_stair", "bo_castle_e_stairs_a", []),

	("77762_river_block", 0, "77762_river_block", "bo_castle_h_battlement_barrier", []),

	("77762_corner_a", 0, "77762_corner_a", "bo_7776_corner_a", []),

	("77762_guard_tower", 0, "77762_guard_tower", "bo_7776_guard_tower", []),

	("77762_gatehouse", 0, "77762_gate_house", "bo_7776_gate_house", []),

	("77762_inner_gate", 0, "77762_inner_gate", "bo_7776_inner_gate", []),

	("77762_wall_belfry", 0, "77762_wall_belfry", "bo_7771_wall_belfry", []),

	("77763_wall", 0, "77763_wall", "bo_77712_wall_destroy", []),

	("77763_wall_on_off", 0, "77763_wall", "bo_77712_wall_destroy", []),

	("77763_wall_destory", 0, "77763_wall", "bo_77712_wall_destroy", []),

	("77763_stair", 0, "77763_stair", "bo_castle_e_stairs_a", []),

	("77763_river_block", 0, "77763_river_block", "bo_castle_h_battlement_barrier", []),

	("77763_corner_a", 0, "77763_corner_a", "bo_7776_corner_a", []),

	("77763_guard_tower", 0, "77763_guard_tower", "bo_7776_guard_tower", []),

	("77763_gatehouse", 0, "77763_gate_house", "bo_7776_gate_house", []),

	("77763_inner_gate", 0, "77763_inner_gate", "bo_7776_inner_gate", []),

	("77763_wall_belfry", 0, "77763_wall_belfry", "bo_7771_wall_belfry", []),

	("7777_wall", 0, "7777_wall", "bo_77712_wall_destroy", []),

	("7777_wall_on_off", 0, "7777_wall", "bo_77712_wall_destroy", []),

	("7777_wall_destory", 0, "7777_wall", "bo_77712_wall_destroy", []),

	("7777_stair", 0, "7777_stair", "bo_castle_e_stairs_a", []),

	("7777_river_block", 0, "7777_river_block", "bo_castle_h_battlement_barrier", []),

	("7777_corner_a", 0, "7777_corner_a", "bo_7776_corner_a", []),

	("7777_guard_tower", 0, "7777_guard_tower", "bo_7776_guard_tower", []),

	("7777_gatehouse", 0, "7777_gate_house", "bo_7776_gate_house", []),

	("7777_inner_gate", 0, "7777_inner_gate", "bo_7776_inner_gate", []),

	("7777_wall_belfry", 0, "7777_wall_belfry", "bo_7771_wall_belfry", []),

	("0_1_h_1", 0, "0_1_h_1", "bo_0_1_h_1", []),

	("0_2_h_1", 0, "0_2_h_1", "bo_0_2_h_1", []),

	("0_3_h_1", 0, "0_3_h_1", "bo_0_3_h_1", []),

	("0_4_h_1", 0, "0_4_h_1", "bo_0_4_h_1", []),

	("0_5_h_1", 0, "0_5_h_1", "bo_0_5_h_1", []),

	("0_6_h_1", 0, "0_6_h_1", "bo_0_6_h_1", []),

	("0_7_h_1", 0, "0_7_h_1", "bo_0_7_h_1", []),

	("0_8_h_1", 0, "0_8_h_1", "bo_0_8_h_1", []),

	("0_2_hex_1", 0, "0_2_h_1", "bo_0_2_h_1", []),

	("0_4_hex_1", 0, "0_4_h_1", "bo_0_4_h_1", []),

	("0_6_hex_1", 0, "0_6_h_1", "bo_0_6_h_1", []),

	("0_1_h_2", 0, "0_1_h_2", "bo_0_1_h_2", []),

	("0_2_h_2", 0, "0_2_h_2", "bo_0_2_h_2", []),

	("0_3_h_2", 0, "0_3_h_2", "bo_0_3_h_2", []),

	("0_4_h_2", 0, "0_4_h_2", "bo_0_4_h_2", []),

	("0_5_h_2", 0, "0_5_h_2", "bo_0_5_h_2", []),

	("0_6_h_2", 0, "0_6_h_2", "bo_0_6_h_2", []),

	("0_7_h_2", 0, "0_7_h_2", "bo_0_7_h_2", []),

	("0_8_h_2", 0, "0_8_h_2", "bo_0_8_h_2", []),

	("0_2_hex_2", 0, "0_2_h_2", "bo_0_2_h_2", []),

	("0_4_hex_2", 0, "0_4_h_2", "bo_0_4_h_2", []),

	("0_6_hex_2", 0, "0_6_h_2", "bo_0_6_h_2", []),

	("0_1_h_22", 0, "0_1_h_22", "bo_0_1_h_2", []),

	("0_2_h_22", 0, "0_2_h_22", "bo_0_2_h_2", []),

	("0_3_h_22", 0, "0_3_h_22", "bo_0_3_h_2", []),

	("0_4_h_22", 0, "0_4_h_22", "bo_0_4_h_2", []),

	("0_5_h_22", 0, "0_5_h_22", "bo_0_5_h_2", []),

	("0_6_h_22", 0, "0_6_h_22", "bo_0_6_h_2", []),

	("0_7_h_22", 0, "0_7_h_22", "bo_0_7_h_2", []),

	("0_8_h_22", 0, "0_8_h_22", "bo_0_8_h_2", []),

	("0_2_hex_22", 0, "0_2_h_22", "bo_0_2_h_2", []),

	("0_4_hex_22", 0, "0_4_h_22", "bo_0_4_h_2", []),

	("0_6_hex_22", 0, "0_6_h_22", "bo_0_6_h_2", []),

	("0_1_h_3", 0, "0_1_h_3", "bo_0_1_h_3", []),

	("0_2_h_3", 0, "0_2_h_3", "bo_0_2_h_3", []),

	("0_3_h_3", 0, "0_3_h_3", "bo_0_3_h_3", []),

	("0_4_h_3", 0, "0_4_h_3", "bo_0_4_h_3", []),

	("0_5_h_3", 0, "0_5_h_3", "bo_0_5_h_3", []),

	("0_6_h_3", 0, "0_6_h_3", "bo_0_6_h_3", []),

	("0_7_h_3", 0, "0_7_h_3", "bo_0_7_h_3", []),

	("0_8_h_3", 0, "0_8_h_3", "bo_0_8_h_3", []),

	("0_2_hex_3", 0, "0_2_h_3", "bo_0_2_h_3", []),

	("0_4_hex_3", 0, "0_4_h_3", "bo_0_4_h_3", []),

	("0_6_hex_3", 0, "0_6_h_3", "bo_0_6_h_3", []),

	("0_1_h_4", 0, "0_1_h_4", "bo_0_1_h_4", []),

	("0_2_h_4", 0, "0_2_h_4", "bo_0_2_h_4", []),

	("0_3_h_4", 0, "0_3_h_4", "bo_0_3_h_4", []),

	("0_4_h_4", 0, "0_4_h_4", "bo_0_4_h_4", []),

	("0_5_h_4", 0, "0_5_h_4", "bo_0_5_h_4", []),

	("0_6_h_4", 0, "0_6_h_4", "bo_0_6_h_4", []),

	("0_7_h_4", 0, "0_7_h_4", "bo_0_7_h_4", []),

	("0_8_h_4", 0, "0_8_h_4", "bo_0_8_h_4", []),

	("0_2_hex_4", 0, "0_2_h_4", "bo_0_2_h_4", []),

	("0_4_hex_4", 0, "0_4_h_4", "bo_0_4_h_4", []),

	("0_6_hex_4", 0, "0_6_h_4", "bo_0_6_h_4", []),

	("0_1_h_5", 0, "0_1_h_5", "bo_0_1_h_5", []),

	("0_2_h_5", 0, "0_2_h_5", "bo_0_2_h_5", []),

	("0_3_h_5", 0, "0_3_h_5", "bo_0_3_h_5", []),

	("0_4_h_5", 0, "0_4_h_5", "bo_0_4_h_5", []),

	("0_5_h_5", 0, "0_5_h_5", "bo_0_5_h_5", []),

	("0_6_h_5", 0, "0_6_h_5", "bo_0_6_h_5", []),

	("0_7_h_5", 0, "0_7_h_5", "bo_0_7_h_5", []),

	("0_8_h_5", 0, "0_8_h_5", "bo_0_8_h_5", []),

	("0_2_hex_5", 0, "0_2_h_5", "bo_0_2_h_5", []),

	("0_4_hex_5", 0, "0_4_h_5", "bo_0_4_h_5", []),

	("0_6_hex_5", 0, "0_6_h_5", "bo_0_6_h_5", []),

	("0_1_h_6", 0, "0_1_h_6", "bo_0_1_h_6", []),

	("0_2_h_6", 0, "0_2_h_6", "bo_0_2_h_6", []),

	("0_3_h_6", 0, "0_3_h_6", "bo_0_3_h_6", []),

	("0_4_h_6", 0, "0_4_h_6", "bo_0_4_h_6", []),

	("0_5_h_6", 0, "0_5_h_6", "bo_0_5_h_6", []),

	("0_6_h_6", 0, "0_6_h_6", "bo_0_6_h_6", []),

	("0_7_h_6", 0, "0_7_h_6", "bo_0_7_h_6", []),

	("0_8_h_6", 0, "0_8_h_6", "bo_0_8_h_6", []),

	("0_2_hex_6", 0, "0_2_h_6", "bo_0_2_h_6", []),

	("0_4_hex_6", 0, "0_4_h_6", "bo_0_4_h_6", []),

	("0_6_hex_6", 0, "0_6_h_6", "bo_0_6_h_6", []),

	("0_1_h_7", 0, "0_1_h_6", "bo_0_1_h_6", []),

	("0_2_h_7", 0, "0_2_h_6", "bo_0_2_h_6", []),

	("0_3_h_7", 0, "0_3_h_6", "bo_0_3_h_6", []),

	("0_4_h_7", 0, "0_4_h_6", "bo_0_4_h_6", []),

	("0_5_h_7", 0, "0_5_h_6", "bo_0_5_h_6", []),

	("0_6_h_7", 0, "0_6_h_6", "bo_0_6_h_6", []),

	("0_7_h_7", 0, "0_7_h_6", "bo_0_7_h_6", []),

	("0_8_h_7", 0, "0_8_h_6", "bo_0_8_h_6", []),

	("0_2_hex_7", 0, "0_2_h_6", "bo_0_2_h_6", []),

	("0_4_hex_7", 0, "0_4_h_6", "bo_0_4_h_6", []),

	("0_6_hex_7", 0, "0_6_h_6", "bo_0_6_h_6", []),

	("0_farm_1", 0, "0_farm_1", "bo_0_farm_1", []),

	("0_farm_2", 0, "0_farm_2", "bo_0_farm_2", []),

	("0_farm_22", 0, "0_farm_22", "bo_0_farm_2", []),

	("0_farm_3", 0, "0_farm_3", "bo_0_farm_3", []),

	("0_farm_4", 0, "0_farm_4", "bo_0_farm_4", []),

	("0_farm_5", 0, "0_farm_5", "bo_0_farm_5", []),

	("0_farm_6", 0, "0_farm_1", "bo_0_farm_1", []),

	("0_farm_7", 0, "0_farm_1", "bo_0_farm_1", []),

	("0_k_1", 0, "0_k_1", "bo_0_k_1", []),

	("0_k_12", 0, "0_k_12", "bo_0_k_12", []),

	("0_k_13", 0, "0_k_13", "bo_0_k_13", []),

	("0_k_2", 0, "0_k_2", "bo_0_k_2", []),

	("0_k_22", 0, "0_k_22", "bo_0_k_2", []),

	("0_k_3", 0, "0_k_3", "bo_0_k_3", []),

	("0_k_4", 0, "0_k_4", "bo_0_k_4", []),

	("0_k_42", 0, "0_k_42", "bo_0_k_42", []),

	("0_k_5", 0, "0_k_5", "bo_0_k_5", []),

	("0_k_6", 0, "0_k_6", "bo_0_k_6", []),

	("0_k_62", 0, "0_k_6", "bo_0_k_6", []),

	("0_k_63", 0, "0_k_6", "bo_0_k_6", []),

	("0_k_7", 0, "0_k_6", "bo_0_k_6", []),

	("0_e_1_1", 0, "0_e_1_1", "bo_0_e_1_1", []),

	("0_e_1_2", 0, "0_e_1_2", "bo_0_e_1_2", []),

	("0_e_1_21", 0, "0_e_1_21", "bo_0_e_1_21", []),

	("0_e_1_3", 0, "0_e_1_3", "bo_0_e_1_3", []),

	("0_e_2_1", 0, "0_e_2_1", "bo_0_e_2_1", []),

	("0_e_2_2", 0, "0_e_2_2", "bo_0_e_2_2", []),

	("0_e_2_3", 0, "0_e_2_3", "bo_0_e_2_3", []),

	("0_e_3_1", 0, "0_e_3_1", "bo_0_e_3_1", []),

	("0_e_4_1", 0, "0_e_4_1", "0", []),

	("0_e_4_2", 0, "0_e_4_2", "0", []),

	("0_e_4_3", 0, "0_e_4_3", "0", []),

	("0_e_5_1", 0, "0_e_5_1", "bo_0_e_5_1", []),

	("0_e_5_2", 0, "0_e_5_2", "bo_0_e_5_2", []),

	("0_e_5_3", 0, "0", "0", []),

	("0_e_5_4", 0, "0_e_5_4", "bo_0_e_5_4", []),

	("0_e_5_5", 0, "0_e_5_5", "bo_0_e_5_5", []),

	("0_5_h_5ex", 0, "0_5_h_5", "bo_0_5_h_5", []),

	("0_6_h_5ex", 0, "0_6_h_5", "bo_0_6_h_5", []),

	("0_e_6_1", 0, "0", "0", []),

	("0_e_6_2", 0, "0", "0", []),

	("0_e_6_3", 0, "0", "0", []),

	("0_e_6_4", 0, "0", "0", []),

	("0_e_6_5", 0, "0", "0", []),

	("0_e_6_6", 0, "0", "0", []),

	("0_e_6_7", 0, "0", "0", []),

	("0_5_h_6ex", 0, "0_5_h_6", "bo_0_5_h_6", []),

	("0_6_h_6ex", 0, "0_6_h_6", "bo_0_6_h_6", []),

	("7778_keep_1", 0, "0", "0", []),

	("7778_keep_2", 0, "0", "0", []),

	("7778_h_1", 0, "0", "0", []),

	("7778_h_2", 0, "0", "0", []),

	("7778_h_3", 0, "0", "0", []),

	("7778_h_4", 0, "0", "0", []),

	("7778_h_5", 0, "0", "0", []),

	("7778_h_6", 0, "0", "0", []),

	("7778_h_7", 0, "0", "0", []),

	("7778_etc_1", 0, "0", "0", []),

	("7778_etc_2", 0, "0", "0", []),

	("7778_etc_3", 0, "0", "0", []),

	("7778_etc_4", 0, "0", "0", []),

	("7778_etc_5", 0, "0", "0", []),

	("7778_wall", 0, "0", "0", []),

	("7778_wall_tower", 0, "0", "0", []),

	("7778_wall_gate", 0, "0", "0", []),

	("7779_urt_1", 0, "7779_urt_1", "bo_7779_urt_1", []),

	("7779_urt_2", 0, "7779_urt_2", "bo_7779_urt_2", []),

	("7779_urt_3", 0, "7779_urt_3", "bo_7779_urt_3", []),

	("7779_inner_urt", 0, "7779_inner_urt", "bo_7779_inner_urt", []),

	("7780_teepee_1", 0, "7780_teepee_1", "bo_7780_teepee_1", []),

	("7780_teepee_2", 0, "7780_teepee_2", "bo_7780_teepee_1", []),

	("belfry_a", sokf_moveable, "belfry_a", "bo_belfry_a", []),

	("belfry_platform_old", 0, "belfry_platform_b", "bo_belfry_platform_b", []),

	("ram_body", sokf_moveable, "666_ram_body", "bo_ram_body", []),

	("ram_shaft", sokf_moveable, "666_ram_shaft", "0", []),

	("ram_wheel", sokf_moveable, "666_ram_wheel", "0", []),

	("towngate_rectangle_door_left", sokf_moveable, "666_towngate_rectangle_door_left", "bo_towngate_rectangle_door_left", []),

	("towngate_rectangle_door_right", sokf_moveable, "666_towngate_rectangle_door_right", "bo_towngate_rectangle_door_right", []),

	("666_door_left", sokf_moveable, "666_towngate_rectangle_door_left", "bo_666_towngate_rectangle_door_left", []),

	("666_door_right", sokf_moveable, "666_towngate_rectangle_door_right", "bo_666_towngate_rectangle_door_right", []),

	("666Catapult", 0, "666Catapult", "bo_666Catapult", []),

	("666_portculis_new", 0, "666_portculis_new", "bo_portculis_new", []),

	("666_portculis_second", 0, "666_portculis_new", "bo_portculis_new", []),

	("666_ballista_javelin", sokf_moveable, "666_ballista_javelin", "0", []),

	("666_destroy_heap_no_bo", 0, "destroy_heap", "0", []),

	("666_wood_heap_b_for_destroy_wall", 0, "wood_heap_b", "bo_wood_heap_b", []),

	("666_box_a_for_ram", 0, "box_a", "0", []),

	("666_ballista_stand", sokf_moveable, "666ballista_sp_stand", "0", []),

	("666_siege_large_shield_plyr", 0, "3siege_large_shield_a", "bo_2siege_large_shield_a", []),

	("666siege_large_shield_a", 0, "2siege_large_shield_a", "bo_2siege_large_shield_a", []),

	("666siege_camp_spikes", 0, "spike_group_a", "0", []),

	("666Catapult_stone_1", sokf_moveable|sokf_dynamic_physics, "666Catapult_stone", "bo_666Catapult_stone", []),

	("666Catapult_stone_2", sokf_moveable|sokf_dynamic_physics, "666Catapult_stone", "bo_666Catapult_stone", []),

	("666Catapult_stone_3", sokf_moveable|sokf_dynamic_physics, "666Catapult_stone", "bo_666Catapult_stone", []),

	("666Catapult_stone_4", sokf_moveable|sokf_dynamic_physics, "666Catapult_stone", "bo_666Catapult_stone", []),

	("666Catapult_stone_ready_1", sokf_moveable, "666Catapult_stone", "bo_666Catapult_stone", []),

	("666Catapult_stone_ready_2", sokf_moveable, "666Catapult_stone", "bo_666Catapult_stone", []),

	("666Catapult_stone_ready_3", sokf_moveable, "666Catapult_stone", "bo_666Catapult_stone", []),

	("666Catapult_stone_ready_4", sokf_moveable, "666Catapult_stone", "bo_666Catapult_stone", []),

	("666Catapult_pul_1", sokf_moveable, "666Catapult_pul", "bo_666Catapult_pul", []),

	("666Catapult_pul_2", sokf_moveable, "666Catapult_pul", "bo_666Catapult_pul", []),

	("666Catapult_pul_3", sokf_moveable, "666Catapult_pul", "bo_666Catapult_pul", []),

	("666Catapult_pul_4", sokf_moveable, "666Catapult_pul", "bo_666Catapult_pul", []),

	("666_portculis_part_1", sokf_moveable|sokf_dynamic_physics, "666_portculis_part_1", "bo_666_portculis_part_1", []),

	("666_portculis_part_2", sokf_moveable|sokf_dynamic_physics, "666_portculis_part_2", "bo_666_portculis_part_2", []),

	("666_ballista_1", sokf_moveable, "666ballista_shooter", "0", []),

	("666_ballista_2", sokf_moveable, "666ballista_shooter", "0", []),

	("666_ballista_javelin_ready_1", sokf_moveable, "666_ballista_javelin", "0", []),

	("666_ballista_javelin_ready_2", sokf_moveable, "666_ballista_javelin", "0", []),

	("6662_fire_big", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_fireplace_fire_big")
		])
	]),

	("6662_Village_fire_big", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_village_fire_big"),
			(set_position_delta, 0, 0, 100),
			(particle_system_add_new, "psys_village_fire_smoke_big")
		])
	]),

	("666_ballista_stand_for_belf", sokf_moveable, "666ballista_sp_stand", "0", []),

	("6662_belfry", 0, "belfry_b", "bo_belfry_b", []),

	("6662_belfry_platform", 0, "belfry_platform_b", "bo_belfry_platform_b", []),

	("6662_siege_ladder_14m", sokf_type_ladder, "siege_ladder_14m", "bo_siege_ladder_14m", []),

	("6662_ballista_1", sokf_moveable, "666ballista_shooter", "0", []),

	("6662_ballista_2", sokf_moveable, "666ballista_shooter", "0", []),

	("6662_ballista_javelin_ready_1", sokf_moveable, "666_ballista_javelin", "0", []),

	("6662_ballista_javelin_ready_2", sokf_moveable, "666_ballista_javelin", "0", []),

	("666_stone_heap_no_bo", 0, "stone_heap_b", "0", []),

	("6663_siege_ladder_for_ruin", sokf_type_ladder, "siege_ladder_move_8m", "bo_siege_ladder_move_8m", []),

	("6663_destroy_heap_no_bo", 0, "destroy_heap", "0", []),

	("8_hall_arab_1", 0, "8_hall_arab_1", "bo_8_hall_arab_1", []),

	("8_hall_arab_2", 0, "8_hall_arab_2", "bo_8_hall_arab_2", []),

	("8_hall_asia", 0, "8_hall_euro_2", "bo_8_hall_euro_2", []),

	("8_hall_euro_1", 0, "8_hall_euro_1", "bo_8_hall_euro_1", []),

	("8_hall_euro_2", 0, "8_hall_euro_2", "bo_8_hall_euro_2", []),

	("8_hall_euro_3", 0, "8_hall_euro_3", "bo_8_hall_euro_3", []),

	("8_hall_greek", 0, "8_hall_roma_1", "bo_8_hall_roma_1", []),

	("8_hall_roma_1", 0, "8_hall_roma_1", "bo_8_hall_roma_1", []),

	("8_hall_viking_1", 0, "8_hall_viking_1", "bo_8_hall_viking_1", []),

	("8_hall_wood_1", 0, "8_hall_wood_1", "bo_8_hall_wood_1", []),

	("8_prison_arab_1", 0, "8_prison_arab_1", "bo_8_prison_arab_1", []),

	("8_prison_asia", 0, "8_prison_asia", "bo_8_prison_asia", []),

	("8_prison_euro", 0, "8_prison_euro", "bo_8_prison_euro", []),

	("8_prison_wood_1", 0, "8_prison_wood_1", "bo_8_prison_wood_1", []),

	("8_tavern_arab_1", 0, "8_tavern_arab_1", "bo_8_tavern_arab_1", []),

	("8_tavern_asia", 0, "8_tavern_roma_1", "bo_8_tavern_roma_1", []),

	("8_tavern_euro_1", 0, "8_tavern_euro_1", "bo_8_tavern_euro_1", []),

	("8_tavern_roma_1", 0, "8_tavern_roma_1", "bo_8_tavern_roma_1", []),

	("9_arabian_ground_a", 0, "arabian_ground_a", "bo_arabian_ground_a", []),

	("666thorn_combined", 0, "thorn_combined", "0", []),

	("ttt_hill_round_plain_01", 0, "ttt_hill_round_plain", "bo_ttt_hill_round_plain", []),

	("ttt_hill_round_plain_02", 0, "ttt_hill_round_plain", "bo_ttt_hill_round_plain", []),

	("ttt_hill_round_plain_03", 0, "ttt_hill_round_plain", "bo_ttt_hill_round_plain", []),

	("ttt_hill_round_plain_04", 0, "ttt_hill_round_plain", "bo_ttt_hill_round_plain", []),

	("ttt_hill_round_plain_05", 0, "ttt_hill_round_plain", "bo_ttt_hill_round_plain", []),

	("ttt_hill_round_spike_01", 0, "ttt_hill_round_spike", "0", []),

	("ttt_hill_round_spike_02", 0, "ttt_hill_round_spike", "0", []),

	("ttt_hill_round_spike_03", 0, "ttt_hill_round_spike", "0", []),

	("ttt_hill_round_spike_04", 0, "ttt_hill_round_spike", "0", []),

	("ttt_hill_round_spike_05", 0, "ttt_hill_round_spike", "0", []),

	("ttt_hill_lean_plain_01", 0, "ttt_hill_lean_plain", "bo_ttt_hill_lean_plain", []),

	("ttt_hill_lean_plain_02", 0, "ttt_hill_lean_plain", "bo_ttt_hill_lean_plain", []),

	("ttt_hill_lean_plain_03", 0, "ttt_hill_lean_plain", "bo_ttt_hill_lean_plain", []),

	("ttt_hill_lean_plain_04", 0, "ttt_hill_lean_plain", "bo_ttt_hill_lean_plain", []),

	("ttt_hill_lean_plain_05", 0, "ttt_hill_lean_plain", "bo_ttt_hill_lean_plain", []),

	("ttt_hill_lean_spike_01", 0, "ttt_hill_lean_spike", "0", []),

	("ttt_hill_lean_spike_02", 0, "ttt_hill_lean_spike", "0", []),

	("ttt_hill_lean_spike_03", 0, "ttt_hill_lean_spike", "0", []),

	("ttt_hill_lean_spike_04", 0, "ttt_hill_lean_spike", "0", []),

	("ttt_hill_lean_spike_05", 0, "ttt_hill_lean_spike", "0", []),

	("ttt_tree_plain_01", 0, "ttt_tree_plain", "bo_ttt_tree_plain", []),

	("ttt_tree_plain_02", 0, "ttt_tree_plain", "bo_ttt_tree_plain", []),

	("ttt_tree_plain_03", 0, "ttt_tree_plain", "bo_ttt_tree_plain", []),

	("ttt_tree_plain_04", 0, "ttt_tree_plain", "bo_ttt_tree_plain", []),

	("ttt_tree_plain_05", 0, "ttt_tree_plain", "bo_ttt_tree_plain", []),

	("ttt_tree_plain_06", 0, "ttt_tree_plain", "bo_ttt_tree_plain", []),

	("ttt_tree_plain_07", 0, "ttt_tree_plain", "bo_ttt_tree_plain", []),

	("ttt_tree_plain_08", 0, "ttt_tree_plain", "bo_ttt_tree_plain", []),

	("ttt_tree_plain_09", 0, "ttt_tree_plain", "bo_ttt_tree_plain", []),

	("ttt_tree_plain_10", 0, "ttt_tree_plain", "bo_ttt_tree_plain", []),

	("ttt_bridge_wooden_01", 0, "ttt_bridge_wooden", "bo_ttt_bridge_wooden", []),

	("ttt_bridge_wooden_02", 0, "ttt_bridge_wooden", "bo_ttt_bridge_wooden", []),

	("ttt_bridge_wooden_03", 0, "ttt_bridge_wooden", "bo_ttt_bridge_wooden", []),

	("ttt_phragmites", 0, "ttt_phragmites", "0", []),

	("666_torture_barrier", 0, "arena_barrier_c", "0", []),

	("666_torture_the_rack", 0, "0", "0", []),

	("666_torture_hanging_cage", 0, "0", "0", []),

	("666_torture_torture_stool", 0, "pussy_torture", "bo_pussy_torture", []),

	("666_torture_iron_maiden_open", 0, "0", "0", []),

	("666_torture_door", 0, "iron_doorr", "bo_iron_doorr", []),

	("5_freamed_1", 0, "framed_1", "0", []),

	("7771_full_keep", 0, "7771_full_keep", "bo_full_keep_b", []),

	("77712_full_keep", 0, "77712_full_keep", "bo_full_keep_b", []),

	("77713_full_keep", 0, "77713_full_keep", "bo_full_keep_b", []),

	("7772_full_keep", 0, "7772_full_keep", "bo_full_keep_b", []),

	("77722_full_keep", 0, "77722_full_keep", "bo_full_keep_b", []),

	("7774_full_keep", 0, "7774_full_keep", "bo_full_keep_b", []),

	("666_cannon_1", sokf_moveable, "666_saker_cannon", "0", []),

	("666_cannon_2", sokf_moveable, "666_saker_cannon", "0", []),

	("666_cannonball_ready_1", sokf_moveable, "666_cannonball", "0", []),

	("666_cannonball_ready_2", sokf_moveable, "666_cannonball", "0", []),

	("666_cannonball_shoot", sokf_moveable, "666_cannonball", "0", []),

	("666_cannonball_1", sokf_moveable|sokf_dynamic_physics, "666_cannonball", "bo_666_cannonball", []),

	("666_cannonball_2", sokf_moveable|sokf_dynamic_physics, "666_cannonball", "bo_666_cannonball", []),

	("666_cannonball_3", sokf_moveable|sokf_dynamic_physics, "666_cannonball", "bo_666_cannonball", []),

	("666_cannonball_4", sokf_moveable|sokf_dynamic_physics, "666_cannonball", "bo_666_cannonball", []),

	("666_cannonb_ready_1", sokf_moveable, "666_cannonball", "bo_666_cannonball", []),

	("666_cannonb_ready_2", sokf_moveable, "666_cannonball", "bo_666_cannonball", []),

	("666_cannonb_ready_3", sokf_moveable, "666_cannonball", "bo_666_cannonball", []),

	("666_cannonb_ready_4", sokf_moveable, "666_cannonball", "bo_666_cannonball", []),

	("666_cannon_body", 0, "666_saker_cannon", "0", []),

	("666_cannon_12", sokf_moveable, "666_saker_cannon", "0", []),

	("666_cannon_22", sokf_moveable, "666_saker_cannon", "0", []),

	("666_cannonball_ready_12", sokf_moveable, "666_cannonball", "0", []),

	("666_cannonball_ready_22", sokf_moveable, "666_cannonball", "0", []),

	("666_fake_stone_for_cannon_1", sokf_moveable, "666_cannonball", "bo_666_cannonball", []),

	("666_fake_stone_for_cannon_2", sokf_moveable, "666_cannonball", "bo_666_cannonball", []),

	("666_fake_stone_for_cannon_3", sokf_moveable, "666_cannonball", "bo_666_cannonball", []),

	("666_fake_stone_for_cannon_4", sokf_moveable, "666_cannonball", "bo_666_cannonball", []),

	("666_tribal_cage_1", 0, "tribal_cage_1", "bo_tribal_cage_1", []),
 ("head_dynamic_male", sokf_moveable|sokf_dynamic_physics, "cut_off_head_male_dynamic", "bo_cut_off_head_dynamic", [ #here
    (ti_on_scene_prop_init,[
      (store_trigger_param_1, ":var0"),
      (scene_prop_set_prune_time, ":var0", 60),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 1000),
      (position_set_y, pos0, 80),
      (position_set_z, pos0, 0),
      (prop_instance_dynamics_set_properties, ":var0", 0),
      (store_random_in_range, ":var1", -2000, 2000),
      (position_set_x, pos0, ":var1"),
      (store_random_in_range, ":var1", -2000, 2000),
      (position_set_y, pos0, ":var1"),
      (store_random_in_range, ":var1", -2000, 2000),
      (position_set_z, pos0, ":var1"),
      (prop_instance_dynamics_set_omega, ":var0", 0),
      (store_random_in_range, ":var1", -2000, 2000),
      (position_set_x, pos0, ":var1"),
      (store_random_in_range, ":var1", -2000, 2000),
      (position_set_y, pos0, ":var1"),
      (store_random_in_range, ":var1", 30, 1000),
      (position_set_z, pos0, ":var1"),
      (prop_instance_dynamics_apply_impulse, ":var0", 0),
    ]),
  ]),

  ("head_dynamic_female", sokf_moveable|sokf_dynamic_physics, "cut_off_head_female_dynamic", "bo_cut_off_head_dynamic", [
    (ti_on_scene_prop_init,[
      (store_trigger_param_1, ":var0"),
      (scene_prop_set_prune_time, ":var0", 60),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 1000),
      (position_set_y, pos0, 80),
      (position_set_z, pos0, 0),
      (prop_instance_dynamics_set_properties, ":var0", 0),
      (store_random_in_range, ":var1", -2000, 2000),
      (position_set_x, pos0, ":var1"),
      (store_random_in_range, ":var1", -2000, 2000),
      (position_set_y, pos0, ":var1"),
      (store_random_in_range, ":var1", -2000, 2000),
      (position_set_z, pos0, ":var1"),
      (prop_instance_dynamics_set_omega, ":var0", 0),
      (store_random_in_range, ":var1", -2000, 2000),
      (position_set_x, pos0, ":var1"),
      (store_random_in_range, ":var1", -2000, 2000),
      (position_set_y, pos0, ":var1"),
      (store_random_in_range, ":var1", 30, 800),
      (position_set_z, pos0, ":var1"),
      (prop_instance_dynamics_apply_impulse, ":var0", 0),
    ]),
  ]),

]