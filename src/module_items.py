# -*- coding: UTF-8 -*-

from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
items = [
  ["no_item","INVALID_ITEM", [("invalid_item", 0)], itp_type_book|itp_food|itp_no_pick_up_from_ground, 0,3, weight(1.5)|abundance(100), imodbits_none, []],
  ["tutorial_spear","spear", [("spear", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield, itc_spear,0, weight(4.5)|abundance(100)|spd_rtng(80)|weapon_length(158)|thrust_damage(19, pierce), imodbits_polearm, []],
  ["tutorial_club","Club", [("club", 0)], itp_type_one_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_primary, itc_scimitar,0, weight(2.5)|abundance(100)|hit_points(11264)|spd_rtng(95)|weapon_length(95)|thrust_damage(0, pierce)|swing_damage(11, blunt), imodbits_none, []],
  ["tutorial_battle_axe","Battle_Axe", [("battle_ax", 0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_carry_axe_back|itc_nodachi,0, weight(5)|abundance(100)|hit_points(27648)|spd_rtng(88)|weapon_length(108)|thrust_damage(0, pierce)|swing_damage(27, cut), imodbits_axe, []],
  ["tutorial_arrows","Arrows", [("arrow", 0),("flying_arrow", ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back,0, weight(3)|abundance(160)|weapon_length(95)|max_ammo(20)|thrust_damage(0, pierce), imodbits_missile, []],
  ["tutorial_bolts","Bolts", [("bolt", 0),("flying_bolt", ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical,0, weight(2.25)|abundance(90)|weapon_length(55)|max_ammo(18)|thrust_damage(0, pierce), imodbits_missile, []],
  ["tutorial_short_bow","Short_Bow", [("short_bow", 0),("short_bow_carry", ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,0, weight(1)|abundance(100)|accuracy(95)|spd_rtng(98)|shoot_speed(49)|thrust_damage(12, pierce), imodbit_cracked|imodbit_bent|imodbit_strong, []],
  ["tutorial_crossbow","Crossbow", [("crossbow", 0)], itp_type_crossbow|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back,0, weight(3)|abundance(100)|spd_rtng(42)|shoot_speed(68)|max_ammo(1)|thrust_damage(32, pierce), imodbits_crossbow, []],
  ["tutorial_throwing_daggers","Throwing_Daggers", [("throwing_dagger", 0)], itp_type_thrown|itp_primary, itcf_throw_stone,0, weight(3.5)|abundance(100)|spd_rtng(102)|shoot_speed(25)|max_ammo(14)|thrust_damage(16, cut), imodbits_missile, []],
  ["tutorial_saddle_horse","Saddle_Horse", [("saddle_horse", 0)], itp_type_horse, 0,0, weight(0)|abundance(90)|body_armor(3)|hit_points(150)|horse_maneuver(38)|horse_speed(40)|thrust_damage(8, blunt), imodbits_horse_basic, []],
  ["tutorial_shield","Round_Shield", [("leathershield_small_b", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,118, weight(2.5)|abundance(100)|body_armor(1)|hit_points(480)|spd_rtng(82)|shield_width(150), imodbits_shield, 	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		],
  ["tutorial_staff_no_attack","Staff", [("wooden_staff", 0)], itp_type_polearm|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itcf_carry_sword_back|itc_parry_polearm,9, weight(3.5)|abundance(100)|spd_rtng(120)|weapon_length(115)|thrust_damage(0, blunt)|swing_damage(0, blunt), imodbits_none, []],
  ["tutorial_staff","Staff", [("wooden_staff", 0)], itp_type_polearm|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itcf_carry_sword_back|itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,9, weight(3.5)|abundance(100)|hit_points(16384)|spd_rtng(120)|weapon_length(115)|thrust_damage(16, blunt)|swing_damage(16, blunt), imodbits_none, []],
  ["tutorial_sword","Sword", [("long_sword", 0),("scab_longsw_a", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,0, weight(1.5)|abundance(100)|hit_points(18432)|spd_rtng(100)|weapon_length(102)|thrust_damage(15, pierce)|swing_damage(18, cut), imodbits_sword, []],
  ["tutorial_axe","Axe", [("iron_ax", 0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_carry_axe_back|itc_nodachi,0, weight(4)|abundance(100)|hit_points(19456)|spd_rtng(91)|weapon_length(108)|thrust_damage(0, pierce)|swing_damage(19, cut), imodbits_axe, []],
  ["tutorial_dagger","Dagger", [("khyber_knife", 0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword,3, weight(1.5)|abundance(100)|hit_points(16384)|spd_rtng(103)|weapon_length(40)|thrust_damage(10, blunt)|swing_damage(16, blunt), imodbits_none, []],
  ["horse_meat","Horse_Meat", [("raw_meat", 0)], itp_type_goods|itp_food|itp_consumable, 0,12, weight(40)|abundance(100)|food_quality(30)|max_ammo(40), imodbits_none, []],
  ["practice_sword","Practice_Sword", [("roman_cav_sword_2", 0),("roman_cav_sword_2_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,900, weight(1.25)|abundance(100)|difficulty(1)|hit_points(35840)|spd_rtng(82)|weapon_length(95)|thrust_damage(10, pierce)|swing_damage(35, cut), imodbits_none, []],
  ["heavy_practice_sword","War_Axe", [("one_handed_war_axe_a", 0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar,457, weight(3)|abundance(100)|difficulty(1)|hit_points(31744)|spd_rtng(77)|weapon_length(68)|thrust_damage(0, pierce)|swing_damage(31, pierce), imodbits_axe, []],
  ["practice_dagger","Practice_Dagger", [("khyber_knife", 0)], itp_type_one_handed_wpn| itp_no_parry|itp_wooden_attack|itp_primary|itp_secondary, itcf_carry_dagger_front_left|itc_dagger,60, weight(0.5)|abundance(100)|hit_points(11264)|spd_rtng(97)|weapon_length(40)|thrust_damage(11, pierce)|swing_damage(11, cut), imodbits_none, []],
  ["practice_axe","Practice_Axe", [("one_handed_war_axe_a", 0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar,457, weight(2)|abundance(100)|difficulty(1)|hit_points(31744)|spd_rtng(77)|weapon_length(68)|thrust_damage(0, pierce)|swing_damage(31, pierce), imodbits_axe, []],
  ["arena_axe","Axe", [("one_handed_war_axe_a", 0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar,300, weight(1.5)|abundance(100)|hit_points(26624)|spd_rtng(77)|weapon_length(68)|thrust_damage(0, pierce)|swing_damage(26, pierce), imodbits_axe, []],
  ["arena_sword","Sword", [("roman_cav_sword_2", 0),("roman_cav_sword_2_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,900, weight(1.25)|abundance(100)|hit_points(35840)|spd_rtng(82)|weapon_length(95)|thrust_damage(10, pierce)|swing_damage(35, cut), imodbits_sword|imodbit_masterwork, []],
  ["arena_sword_two_handed","War_Axe", [("long_axe_a", 0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_carry_axe_back|itc_nodachi,220, weight(3)|abundance(100)|difficulty(1)|hit_points(43008)|spd_rtng(71)|weapon_length(100)|thrust_damage(0, pierce)|swing_damage(42, pierce), imodbits_axe, []],
  ["arena_lance","Arena_spear", [("javelin", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,420, weight(4)|abundance(80)|difficulty(1)|hit_points(16384)|spd_rtng(91)|weapon_length(114)|thrust_damage(27, pierce)|swing_damage(16, blunt), imodbits_polearm, []],
  ["arena_lance","Arena_spear", [("javelin", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,420, weight(4)|abundance(80)|difficulty(1)|hit_points(16384)|spd_rtng(91)|weapon_length(114)|thrust_damage(27, pierce)|swing_damage(16, blunt), imodbits_polearm, []],
  ["arena_lance","Arena_spear", [("javelin", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,420, weight(4)|abundance(80)|difficulty(1)|hit_points(16384)|spd_rtng(91)|weapon_length(114)|thrust_damage(27, pierce)|swing_damage(16, blunt), imodbits_polearm, []],
  ["practice_shield","Practice_Shield", [("leathershield_small_b", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,400, weight(4.5)|abundance(100)|body_armor(6)|hit_points(400)|spd_rtng(55)|shield_width(70), imodbits_shield, 	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		],
  ["practice_bow","Hunting_Bow", [("hunting_bow", 0),("hunting_bow_carry", ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,267, weight(1)|abundance(100)|accuracy(95)|spd_rtng(70)|shoot_speed(45)|thrust_damage(14, pierce), imodbit_cracked|imodbit_bent|imodbit_strong, []],
  ["practice_crossbow","Javelins", [("javelin", 0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,100, weight(2)|abundance(100)|spd_rtng(60)|shoot_speed(28)|weapon_length(65)|max_ammo(6)|thrust_damage(21, pierce), imodbits_missile|imodbit_balanced|imodbit_heavy, []],
  ["practice_javelin","Practice_Javelins", [("javelin", 0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,100, weight(2)|abundance(100)|spd_rtng(60)|shoot_speed(28)|weapon_length(65)|max_ammo(6)|thrust_damage(21, pierce), imodbits_missile|imodbit_balanced|imodbit_heavy, []],
  ["practice_javelin_melee","practice_javelin_melee", [("javelin", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_secondary, itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,100, weight(2)|abundance(100)|hit_points(4096)|spd_rtng(70)|weapon_length(65)|thrust_damage(19, pierce)|swing_damage(4, cut), imodbits_polearm, []],
  ["practice_throwing_daggers","Throwing_Daggers", [("throwing_dagger", 0)], itp_type_thrown|itp_primary, itcf_throw_stone,0, weight(3.5)|abundance(100)|spd_rtng(102)|shoot_speed(25)|max_ammo(10)|thrust_damage(6, blunt), imodbits_missile|imodbit_balanced|imodbit_heavy, []],
  ["practice_throwing_daggers_100_amount","Throwing_Daggers", [("throwing_dagger", 0)], itp_type_thrown|itp_primary, itcf_throw_stone,0, weight(3.5)|abundance(100)|spd_rtng(102)|shoot_speed(25)|max_ammo(100)|thrust_damage(6, blunt), imodbits_missile|imodbit_balanced|imodbit_heavy, []],
  ["practice_horse","Practice_Horse", [("saddle_horse", 0)], itp_type_horse, 0,37, weight(0)|abundance(100)|body_armor(10)|hit_points(150)|horse_maneuver(37)|horse_speed(35)|thrust_damage(8, blunt), imodbits_none, []],
  ["practice_arrows","Practice_Arrows", [("arena_arrow", 0),("flying_arrow", ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_default_ammo, itcf_carry_quiver_back,100, weight(3)|abundance(110)|weapon_length(95)|max_ammo(60)|thrust_damage(1, pierce), imodbits_missile, []],
  ["practice_bolts","Practice_Dagger", [("khyber_knife", 0)], itp_type_one_handed_wpn| itp_no_parry|itp_wooden_attack|itp_primary|itp_secondary, itcf_carry_dagger_front_left|itc_dagger,60, weight(0.5)|abundance(100)|hit_points(11264)|spd_rtng(97)|weapon_length(40)|thrust_damage(11, pierce)|swing_damage(11, cut), imodbits_none, []],
  ["practice_arrows_10_amount","Practice_Arrows", [("arrow", 0),("flying_arrow", ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back,0, weight(1.5)|abundance(100)|weapon_length(95)|max_ammo(10), imodbits_missile, []],
  ["practice_arrows_100_amount","Practice_Arrows", [("arrow", 0),("flying_arrow", ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back,0, weight(1.5)|abundance(100)|weapon_length(95)|max_ammo(100), imodbits_missile, []],
  ["practice_bolts_9_amount","Practice_Bolts", [("bolt", 0),("flying_bolt", ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical,0, weight(2.25)|abundance(100)|weapon_length(55)|max_ammo(9), imodbits_missile, []],
  ["practice_boots","Practice_Boots", [("hide_boots_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,11, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, []],
  ["red_tourney_armor","Red_Tourney_Armor", [("arena_tunicR_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0,152, weight(15)|abundance(100)|body_armor(20)|leg_armor(6), imodbits_none, []],
  ["blue_tourney_armor","Blue_Tourney_Armor", [("arena_tunicB_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0,152, weight(15)|abundance(100)|body_armor(20)|leg_armor(6), imodbits_none, []],
  ["green_tourney_armor","Green_Tourney_Armor", [("arena_tunicG_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0,152, weight(15)|abundance(100)|body_armor(20)|leg_armor(6), imodbits_none, []],
  ["gold_tourney_armor","White_Tourney_Armor", [("arena_tunicW_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0,152, weight(15)|abundance(100)|body_armor(20)|leg_armor(6), imodbits_none, []],
  ["red_tourney_helmet","Red Tourney Helmet", [("steppe_helmetR", 0)], itp_type_head_armor|itp_civilian|itp_fit_to_head|itp_covers_beard, 0,50, weight(1.75)|abundance(40)|head_armor(35)|difficulty(6), imodbits_armor|imodbit_cracked, []],
  ["blue_tourney_helmet","Blue Tourney Helmet", [("steppe_helmetB", 0)], itp_type_head_armor|itp_civilian|itp_fit_to_head|itp_covers_beard, 0,50, weight(1.75)|abundance(40)|head_armor(35)|difficulty(6), imodbits_armor|imodbit_cracked, []],
  ["green_tourney_helmet","Green Tourney Helmet", [("steppe_helmetG", 0)], itp_type_head_armor|itp_civilian|itp_fit_to_head|itp_covers_beard, 0,50, weight(1.75)|abundance(40)|head_armor(35)|difficulty(6), imodbits_armor|imodbit_cracked, []],
  ["gold_tourney_helmet","Gold Tourney Helmet", [("steppe_helmetY", 0)], itp_type_head_armor|itp_civilian|itp_fit_to_head|itp_covers_beard, 0,50, weight(1.75)|abundance(40)|head_armor(35)|difficulty(6), imodbits_armor|imodbit_cracked, []],
  ["arena_shield_red","Shield", [("leathershield_medium", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,100, weight(4.5)|abundance(100)|body_armor(20)|hit_points(300)|spd_rtng(65)|shield_width(70), imodbits_shield,
#####Begin add effect to shields	
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		],
		#####End add effect to shields
  ["arena_shield_blue","Shield", [("woodenshield_small_d", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,100, weight(4.5)|abundance(100)|body_armor(20)|hit_points(300)|spd_rtng(65)|shield_width(70), imodbits_shield, 
#####Begin add effect to shields	
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		],
		#####End add effect to shields
  ["arena_shield_green","Shield", [("leathershield_medium_b", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,100, weight(4.5)|abundance(100)|body_armor(20)|hit_points(300)|spd_rtng(65)|shield_width(70), imodbits_shield, 
#####Begin add effect to shields	
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		],
		#####End add effect to shields
  ["arena_shield_yellow","Shield", [("leathershield_medium_y", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,100, weight(4.5)|abundance(100)|body_armor(20)|hit_points(300)|spd_rtng(65)|shield_width(70), imodbits_shield, 
#####Begin add effect to shields	
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		],
		#####End add effect to shields
  ["arena_armor_white","Armor", [("arena_tunicW_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0,600, weight(4)|abundance(90)|body_armor(30), imodbits_armor, []],
  ["arena_armor_red","Armor", [("arena_tunicR_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0,600, weight(4)|abundance(90)|body_armor(30), imodbits_armor, []],
  ["arena_armor_blue","Armor", [("arena_tunicB_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0,600, weight(4)|abundance(90)|body_armor(30), imodbits_armor, []],
  ["arena_armor_green","Armor", [("arena_tunicG_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0,600, weight(4)|abundance(90)|body_armor(30), imodbits_armor, []],
  ["arena_armor_yellow","Armor", [("shirt_ylw", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0,600, weight(4)|abundance(90)|body_armor(30), imodbits_armor, []],
  ["arena_tunic_white","Tunic_White_", [("arena_tunicW_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,140, weight(0.5)|abundance(50)|body_armor(5)|leg_armor(2), imodbits_cloth, []],
  ["arena_tunic_red","Tunic_Red", [("arena_tunicR_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,140, weight(0.5)|abundance(50)|body_armor(5)|leg_armor(2), imodbits_cloth, []],
  ["arena_tunic_blue","Tunic_Blue", [("arena_tunicB_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,140, weight(0.5)|abundance(50)|body_armor(5)|leg_armor(2), imodbits_cloth, []],
  ["arena_tunic_green","Tunic_Green", [("arena_tunicG_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,140, weight(0.5)|abundance(50)|body_armor(5)|leg_armor(2), imodbits_cloth, []],
  ["arena_tunic_yellow","Tunic_Yellow", [("shirt_ylw", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,140, weight(0.5)|abundance(50)|body_armor(5)|leg_armor(2), imodbits_cloth, []],
  ["qqnew_horse_nor","Warhorse", [("new_horse_nor", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_10]],
  ["qqnew_horse_swe","Warhorse", [("new_horse_swe", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_12]],
  ["qqnew_horse_sco","Warhorse", [("new_horse_sco", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_18]],
  ["qqnew_horse_11","Warhorse", [("new_horse_11", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, []],
  ["qqteu_heraldic_horse_3","Warhorse", [("heraldic_horse_3", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, []],
  ["qqnew_horse_8","Warhorse", [("new_horse_8", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqcharger_plate_brownsp_uniq1","Rocinante", [("charger_plate_brown", 0)], itp_type_horse, 0,7300, weight(0)|abundance(20)|body_armor(40)|difficulty(6)|hit_points(80)|horse_maneuver(5)|horse_speed(54)|weapon_length(102)|thrust_damage(50, blunt), imodbits_horse_basic, []],
  ["afri_warhorse_chain_brass","Warhorse", [("warhorse_chain_brass", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["cc_warhorse_lamellar_b","Warhorse", [("warhorse_lamellar_b", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["qqnew_horse_den","Warhorse", [("new_horse_den", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["yf_ydzx","Elephant", [("yf_ydzx", 0)], itp_type_horse|itp_covers_legs|itp_doesnt_cover_hair|itp_can_knock_down, 0,3200, weight(0)|abundance(100)|body_armor(35)|difficulty(10)|hit_points(200)|horse_maneuver(25)|horse_speed(25)|weapon_length(170)|thrust_damage(100, blunt), imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["horse_redhorse","Horse", [("rus_horse", 0)], itp_type_horse, 0,5, weight(5)|abundance(100)|body_armor(33)|difficulty(8)|hit_points(80)|horse_maneuver(44)|horse_speed(50)|weapon_length(102)|thrust_damage(33, blunt), imodbits_none, []],
  ["tour_horse_1","Horse", [("roman_horse_1", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["tour_horse_2","Horse", [("roman_horse_1", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["tour_horse_3","Horse", [("roman_horse_1", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["tour_horse_4","Horse", [("roman_horse_1", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["roman_horse_1_3","Horse", [("roman_horse_1", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["roman_horse_1_4","Horse", [("roman_horse_1", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["book_tactics","History_of_the_Peloponnesian_War", [("book_a", 0)], itp_type_book, 0,4000, weight(2)|abundance(100), imodbits_none, []],
  ["book_persuasion","Rhetorica_ad_Herennium", [("book_b", 0)], itp_type_book, 0,5000, weight(2)|abundance(100), imodbits_none, []],
  ["book_leadership","The_Life_of_alexander_the_great", [("book_d", 0)], itp_type_book, 0,4200, weight(2)|abundance(100), imodbits_none, []],
  ["book_intelligence","Paedeia", [("book_e", 0)], itp_type_book, 0,2900, weight(2)|abundance(100), imodbits_none, []],
  ["book_trade","Oeconomica_of_Aristoteles", [("book_f", 0)], itp_type_book, 0,3100, weight(2)|abundance(100), imodbits_none, []],
  ["book_weapon_mastery","Polity_of_the_Lacedaemonians_of_Xenofonte", [("book_d", 0)], itp_type_book, 0,4200, weight(2)|abundance(100), imodbits_none, []],
  ["book_engineering","De_architectura_of_Vitrivius", [("book_open", 0)], itp_type_book, 0,4000, weight(2)|abundance(100), imodbits_none, []],
  ["book_wound_treatment_reference","De_Materia_Medica_of_Dioscorides", [("book_c", 0)], itp_type_book, 0,3500, weight(2)|abundance(100), imodbits_none, []],
  ["book_training_reference","Epitoma_Rei_Militaris", [("book_open", 0)], itp_type_book, 0,3500, weight(2)|abundance(100), imodbits_none, []],
  ["book_surgery_reference","Synopsis_of_Aelius_Galenus", [("book_c", 0)], itp_type_book, 0,3500, weight(2)|abundance(100), imodbits_none, []],
  ["book_non","nnn", [("book_e", 0)], itp_type_book, 0,100, weight(2)|abundance(100), imodbits_none, []],
  ["horse","Horse", [("roman_horse_1", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["fine_wood","Fine_wood", [("chest_simple", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["iron","Iron", [("iron", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["elephant","Elephant", [("yf_ydzx", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["whale","Whales", [("raw_meat", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["fish","Fish", [("fish_a", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["maize","Maize", [("maize_b", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["copper","Copper", [("raw_silk_single", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["marble","Marbles", [("ore_iron", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["pearl","Pearls", [("chest_b", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["gem","Gems", [("chest_c", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["ceramic","Ceramics", [("oil", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["gold","Gold", [("ore_gold", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["silver","silver", [("ore_silver", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["ivory","Ivory", [("chest_simple", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["coffee","Coffee", [("coff", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["cacao","Cacao", [("olive_inventory", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["silk","Silk", [("velvet", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["nutmeg","Nutmeg", [("kherb", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["allspice","All spices", [("allspice", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["cinnamon","Cinnamon", [("spice_sack", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["clove","Clove", [("wheat_sack", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["pepper","Pepper", [("saffron", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["tabaco","Tabaco", [("bean", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["tea","Tea", [("raw_flax", 0)], itp_type_goods|itp_merchandise, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["goods_low","goods_low", [("spice_sack", 0)], itp_type_goods, 0,1000, weight(40)|abundance(100), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite, []],
  ["temp_mark_2","temp_mark_2", [("arrow", 0)], itp_type_goods, 0,96, weight(40)|abundance(70), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["roman_horse_2","Horse", [("roman_horse_2", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|difficulty(1)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["roman_horse_1","Horse", [("roman_horse_1", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["normal_horse11","Horse", [("normal_horse11", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|difficulty(1)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["roman_horse_1_2","Horse", [("roman_horse_1", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|difficulty(1)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["normal_horse11","Horse", [("normal_horse11", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|difficulty(1)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["normal_horse12","Horse", [("normal_horse12", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|difficulty(1)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["normal_horse13","Horse", [("normal_horse13", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|difficulty(1)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["normal_horse14","Horse", [("normal_horse14", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|difficulty(1)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["rus_horse","Horse", [("rus_horse", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|difficulty(1)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["rus_horse_2","Horse", [("rus_horse", 0)], itp_type_horse|itp_merchandise, 0,1000, weight(0)|abundance(30)|body_armor(20)|difficulty(1)|hit_points(80)|horse_maneuver(42)|horse_speed(44)|weapon_length(100)|thrust_damage(10, blunt), imodbits_horse_basic, []],
  ["qqnew_horse_hun","Warhorse", [("new_horse_hun", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_24]],
  ["qqnew_horse_pol","Warhorse", [("new_horse_pol", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_15]],
  ["ffnew_horse_4","Warhorse", [("new_horse_4", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_28]],
  ["ffnew_horse_1","Warhorse", [("new_horse_1", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_17]],
  ["ffnew_horse_10","Warhorse", [("new_horse_10", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_19]],
  ["wwcamel_big","Camel", [("camel_2", 0),("camel_2", imodbit_heavy|imodbit_spirited)], itp_type_horse, 0,1600, weight(0)|abundance(60)|body_armor(25)|difficulty(2)|hit_points(80)|horse_maneuver(44)|horse_speed(42)|weapon_length(110)|thrust_damage(15, blunt), imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["lamellar_armor_horse_2","Warhorse", [("lamellar_armor_horse_2", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(10)|body_armor(42)|difficulty(6)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(100)|thrust_damage(50, blunt), imodbits_horse_basic, [], [fac_kingdom_7,fac_kingdom_14,fac_kingdom_16,fac_kingdom_21,fac_kingdom_22,fac_kingdom_26,fac_kingdom_29,fac_kingdom_30,fac_kingdom_52]],
  ["qqnew_horse_ger","Warhorse", [("new_horse_ger", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_11]],
  ["qqnew_horse_tem","Warhorse", [("new_horse_tem", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_6]],
  ["qqnew_horse_fra","Warhorse", [("new_horse_fra", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_8]],
  ["qqnew_horse_eng","Warhorse", [("new_horse_eng", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_18]],
  ["qqnew_horse_cas","Warhorse", [("new_horse_cas", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_23]],
  ["qqnew_horse_por","Warhorse", [("new_horse_por", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_25]],
  ["ccwarhorse_lamellar_c","Warhorse", [("warhorse_lamellar_c", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_1,fac_kingdom_21,fac_kingdom_22,fac_kingdom_30]],
  ["qqcharger_plate_white","Warhorse", [("charger_plate_white", 0)], itp_type_horse|itp_merchandise, 0,5300, weight(0)|abundance(20)|body_armor(40)|difficulty(6)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(50, blunt), imodbits_horse_basic, [], [fac_kingdom_23,fac_kingdom_25]],
  ["qqcharger_plate_brown","Warhorse", [("charger_plate_brown", 0)], itp_type_horse|itp_merchandise, 0,5300, weight(0)|abundance(20)|body_armor(40)|difficulty(6)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(50, blunt), imodbits_horse_basic, [], [fac_kingdom_23,fac_kingdom_25]],
  ["qqcharger_new_steel","Warhorse", [("charger_new_steel", 0)], itp_type_horse|itp_merchandise, 0,5300, weight(0)|abundance(20)|body_armor(40)|difficulty(6)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(50, blunt), imodbits_horse_basic, [], [fac_kingdom_23,fac_kingdom_25]],
  ["qqnew_horse_2","Warhorse", [("new_horse_2", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqnew_horse_9","Warhorse", [("new_horse_9", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqnew_horse_5","Warhorse", [("new_horse_5", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqnew_horse_7","Warhorse", [("new_horse_7", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqnew_horse_hos","Warhorse", [("new_horse_hos", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqnew_horse_nov","Warhorse", [("new_horse_nov", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_47]],
  ["qqnew_horse_gal","Warhorse", [("new_horse_gal", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_48]],
  ["qqwplatedcharger2","Warhorse_silver", [("WPlatedCharger2", 0)], itp_type_horse, 0,10300, weight(0)|abundance(20)|body_armor(40)|difficulty(6)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(50, blunt), imodbits_horse_basic, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["ccwarhorse_mongol3","Warhorse", [("warhorse_lamellar_a", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_7,fac_kingdom_14,fac_kingdom_16,fac_kingdom_21,fac_kingdom_22,fac_kingdom_26,fac_kingdom_29,fac_kingdom_30,fac_kingdom_52]],
  ["ccwarhorse_mongol4","Warhorse", [("warhorse_lamellar_b", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_7,fac_kingdom_14,fac_kingdom_16,fac_kingdom_21,fac_kingdom_22,fac_kingdom_26,fac_kingdom_29,fac_kingdom_30,fac_kingdom_52]],
  ["ccwarhorse_mongol1","Warhorse", [("warhorse_sarranid", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_7,fac_kingdom_14,fac_kingdom_16,fac_kingdom_21,fac_kingdom_22,fac_kingdom_26,fac_kingdom_29,fac_kingdom_30,fac_kingdom_52]],
  ["qqnew_horse_6","Warhorse", [("new_horse_6", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, []],
  ["cc_warhorse_steppe","Warhorse", [("warhorse_steppe", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_7,fac_kingdom_14,fac_kingdom_16,fac_kingdom_21,fac_kingdom_22,fac_kingdom_26,fac_kingdom_29,fac_kingdom_30,fac_kingdom_52]],
  ["qqnew_horse_3","Warhorse", [("new_horse_3", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, []],
  ["wplatedcharger9","Charger", [("WPlatedCharger9", 0)], itp_type_horse, 0,10300, weight(0)|abundance(10)|body_armor(42)|difficulty(6)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(100)|thrust_damage(50, blunt), imodbits_horse_basic|imodbit_champion, []],
  ["charger_new_black","Warhorse", [("charger_new_black", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["charger_new_brown","Warhorse", [("charger_new_brown", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_7,fac_kingdom_14,fac_kingdom_16,fac_kingdom_21,fac_kingdom_22,fac_kingdom_26,fac_kingdom_29,fac_kingdom_30,fac_kingdom_52]],
  ["charger_plate","Warhorse", [("charger_plate", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(10)|body_armor(42)|difficulty(6)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(100)|thrust_damage(50, blunt), imodbits_horse_basic, [], [fac_kingdom_7,fac_kingdom_14,fac_kingdom_16,fac_kingdom_21,fac_kingdom_22,fac_kingdom_26,fac_kingdom_29,fac_kingdom_30,fac_kingdom_52]],
  ["arrows","Arrows", [("arrow", 0),("flying_arrow", ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_back,200, weight(3)|abundance(110)|weapon_length(95)|max_ammo(20)|thrust_damage(30, pierce), imodbits_missile, []],
  ["khergit_arrows","Explosive arrow", [("arrow_b", 0),("guangjian_fly_SEO", ixmesh_flying_ammo),("quiver_c", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back_right,410, weight(3.5)|abundance(100)|weapon_length(95)|max_ammo(10)|thrust_damage(35, pierce), imodbits_missile, [
    (ti_on_missile_hit, [
      (store_trigger_param_1, ":var0"),
      (call_script, "script_molda_bomb_arrow", ":var0"),
    ]),
   ]],
  ["barbed_arrows","Fire_Arrow", [("arrow_b", 0),("guangjian_fly_SEO", ixmesh_flying_ammo),("quiver_c", ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_back,200, weight(3)|abundance(110)|weapon_length(95)|max_ammo(20)|thrust_damage(32, pierce), imodbits_missile, [
    (ti_on_missile_hit, [
      (store_trigger_param_1, ":var0"),
      (call_script, "script_fire_at_pos1", 500, 15, ":var0"),
    ]),
   ]],
  ["bolts","Bolts", [("bolt", 0),("flying_bolt", ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, itcf_carry_quiver_right_vertical,164, weight(1)|abundance(50)|weapon_length(63)|max_ammo(20)|thrust_damage(32, pierce), imodbits_missile, []],
  ["pilgrim_disguise","Pilgrim_Disguise", [("pilgrim_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,25, weight(2)|abundance(100)|body_armor(55)|leg_armor(15), imodbits_cloth, []],
  ["pilgrim_hood","Pilgrim_Hood", [("pil_hood", 0)], itp_type_head_armor|itp_civilian, 0,35, weight(1.25)|abundance(100)|head_armor(45), imodbits_cloth, []],
  ["sandal_girl","Sandal_for_girl", [("sandal_girl", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,280, weight(1)|abundance(100)|leg_armor(15), imodbits_cloth, []],
  ["leather_boots_a55","Leather_boots", [("leather_boots_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,480, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, []],
  ["wrapping_boots","Wrapping_Boots", [("wrapping_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,100, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, []],
  ["ankle_boots","Ankle_Boots", [("ankle_boots_c", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,250, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, []],
  ["wrapping_boots2","Leather_shoes", [("wrapping_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,120, weight(1)|abundance(90)|leg_armor(10), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18,fac_kingdom_23,fac_kingdom_24,fac_kingdom_25]],
  ["hide_boots_a_1","Hide_boots", [("hide_boots_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,280, weight(1)|abundance(100)|leg_armor(25), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18,fac_kingdom_23,fac_kingdom_24,fac_kingdom_25]],
  ["inca_boot","Inca_boot", [("inca_boot", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,280, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, [], [fac_kingdom_45]],
  ["iber_mosk_postoli_a","Shoes", [("mosk_postoli_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,200, weight(0.5)|abundance(100)|leg_armor(20), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["iber_mosk_postoli_a2","Shoes", [("mosk_postoli_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,200, weight(0.5)|abundance(100)|leg_armor(20), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["iber_sockshoes12","Shoes", [("sockshoes1", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,200, weight(0.5)|abundance(100)|leg_armor(20), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["iber_sockshoes1","Shoes", [("sockshoes1", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,200, weight(0.5)|abundance(100)|leg_armor(20), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["cc_mgj_boots_yunxue","Boots", [("mgj_boots_yunxue", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,320, weight(2)|abundance(30)|leg_armor(25), imodbits_armor, [], [fac_kingdom_1,fac_kingdom_7,fac_kingdom_16,fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29,fac_kingdom_30]],
  ["amer_boot","Boots", [("inca_boot", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,280, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, [], [fac_kingdom_50]],
  ["cc_mgj_boots","Boots", [("mgj_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,320, weight(2)|abundance(30)|leg_armor(25), imodbits_armor, [], [fac_kingdom_1,fac_kingdom_7,fac_kingdom_16,fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29,fac_kingdom_30]],
  ["qqnew_horse_ire","Warhorse", [("new_horse_ire", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_53]],
  ["qqnew_horse_kiv","Warhorse", [("new_horse_kiv", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_7]],
  ["qqnew_horse_jer","Warhorse", [("new_horse_jer", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_6]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["zzmail_boots_a","Chainmail boots", [("mail_boots_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,700, weight(3.5)|abundance(100)|leg_armor(35), imodbits_armor|imodbit_cracked, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["zzsteel_boots_cav","Steel boots", [("shynbaulds", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,1500, weight(3.5)|abundance(100)|leg_armor(40)|difficulty(30), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["zzshynbaulds","Shynbaulds", [("shynbaulds", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,1700, weight(3.5)|abundance(100)|leg_armor(40)|difficulty(30), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["zzsteel_boots_inf","Steel_boots", [("steel_boots_inf", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,1070, weight(3.5)|abundance(100)|leg_armor(40)|difficulty(18), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["iber_splinted_greaves_nospurs","Splinted_greaves", [("splinted_greaves_nospurs", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,800, weight(3.5)|abundance(100)|leg_armor(35), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["wwsarranid_camel_boots","Sarranid_camel_boots", [("sarranid_camel_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,470, weight(3.5)|abundance(100)|leg_armor(25), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["legacy_foot_uniq1","Legacy_foot", [("nord_splinted_greaves", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,3070, weight(3.5)|abundance(100)|leg_armor(45)|difficulty(30), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["qqnew_horse_sic","Warhorse", [("new_horse_sic", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["iber_iron_greaves","Iron_greaves", [("shynbaulds", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,1100, weight(3.5)|abundance(100)|leg_armor(40), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["qqnew_horse_leo","Warhorse", [("new_horse_leo", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["cc_rus_cav_boots","Boots", [("rus_cav_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,300, weight(3.5)|abundance(100)|leg_armor(25), imodbits_armor|imodbit_cracked, []],
  ["qqnew_horse_ara","Warhorse", [("new_horse_ara", 0)], itp_type_horse|itp_merchandise, 0,1600, weight(0)|abundance(20)|body_armor(33)|difficulty(3)|hit_points(80)|horse_maneuver(38)|horse_speed(44)|weapon_length(102)|thrust_damage(33, blunt), imodbits_horse_basic, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["shadow_greaves","Shadow greaves", [("shadow_greaves", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,270, weight(3.5)|abundance(100)|leg_armor(27), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_20]],
  ["qqrus_shoes","Russian shoes", [("rus_shoes", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,270, weight(3.5)|abundance(100)|leg_armor(25), imodbits_armor|imodbit_cracked, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["wwsarranid_boots","Sarranian boots", [("sarranid_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,270, weight(3.5)|abundance(100)|leg_armor(25), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["rus_splint_greaves","Splinted greaves", [("rus_splint_greaves", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,480, weight(2)|abundance(30)|leg_armor(30), imodbits_armor, []],
  ["zzhanboot_nomad_b","Nomad_boots", [("hanboot_nomad_b", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,220, weight(2)|abundance(30)|leg_armor(20), imodbits_armor, [], [fac_kingdom_1,fac_kingdom_7,fac_kingdom_16,fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29,fac_kingdom_30]],
  ["zzhankhergit_leather_boots","Black_leather_boots", [("hankhergit_leather_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,320, weight(2)|abundance(30)|leg_armor(25), imodbits_armor, [], [fac_kingdom_1,fac_kingdom_7,fac_kingdom_16,fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29,fac_kingdom_30]],
  ["zzeast_boots","Eastern boots", [("east_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,220, weight(2)|abundance(30)|leg_armor(20), imodbits_armor, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["jjsuneate_low","Suneate", [("suneate_low", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,300, weight(2)|abundance(30)|leg_armor(25), imodbits_armor, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["jjsuneate_red","Suneate", [("suneate_red", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,300, weight(2)|abundance(30)|leg_armor(25), imodbits_armor, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["lgreaves1","Leather_greaves", [("lgreaves1", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,300, weight(1)|abundance(10)|leg_armor(25), imodbits_cloth, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["bronze_greaves","Bronze_greaves", [("bronze_greaves", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,300, weight(1)|abundance(10)|leg_armor(25), imodbits_cloth, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["zzroman_greaves_caligea","Sandals", [("roman_greaves_caligea", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,100, weight(1)|abundance(10)|leg_armor(15), imodbits_cloth, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["zzroman_greaves_gutter","Gutter greaves", [("roman_greaves_gutter", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,300, weight(1)|abundance(10)|leg_armor(25), imodbits_cloth, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["zzroman_greaves_gutter_single","Greaves_gutter_single", [("roman_greaves_gutter_single", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,300, weight(1)|abundance(10)|leg_armor(20), imodbits_cloth, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["gallic_foot","Gaelic_boots", [("gallic_boots", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,120, weight(1)|abundance(100)|leg_armor(15), imodbits_cloth, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["per_strapsandals","Boots", [("strapsandals", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,250, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, [], [fac_kingdom_9]],
  ["pir_infantry_boots_a","Infantry boots", [("infantry_boots_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,311, weight(3.5)|abundance(10)|leg_armor(20), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["iri_highlander_boots_blue","Scottish boots", [("highlander_boots_blue", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,111, weight(3.5)|abundance(10)|leg_armor(25), imodbits_armor, [], [fac_kingdom_18]],
  ["per_brgreaves2","Boots", [("brgreaves2", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,250, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, [], [fac_kingdom_9]],
  ["per_brgreaves1","Boots", [("brgreaves1", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,250, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, [], [fac_kingdom_9]],
  ["zzshynbaulds_bk","Shynbaulds", [("shynbaulds_bk", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,1700, weight(3.5)|abundance(100)|leg_armor(40)|difficulty(30), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["jjjsuneate","Suneate", [("suneate", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,920, weight(2)|abundance(30)|leg_armor(30), imodbits_armor, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["ro_sandal","Sandals", [("sandal_ro", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,100, weight(1)|abundance(10)|leg_armor(15), imodbits_cloth, [], [fac_kingdom_27,fac_kingdom_33]],
  ["wwsarranid_shoes","Sarranian shoes", [("sarranid_shoes", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,270, weight(3.5)|abundance(100)|leg_armor(20), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["sayazn_female_peasant_cap","Sandals", [("sayazn_female_peasant_cap", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,100, weight(1)|abundance(10)|leg_armor(15), imodbits_cloth, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["sayazn_female_peasant_cap_2","Sandals", [("sayazn_female_peasant_cap_2", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,100, weight(1)|abundance(10)|leg_armor(15), imodbits_cloth, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["zzroman_greaves_greek","Greaves_greek", [("roman_greaves_greek", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,410, weight(2)|abundance(30)|leg_armor(25), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["sayazn_sandals_white","Sandals", [("sayazn_sandals_white", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,100, weight(1)|abundance(10)|leg_armor(15), imodbits_cloth, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwsarranid_mail_chausses","Sarranian mail chaussess", [("sarranid_mail_chausses", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,470, weight(3.5)|abundance(100)|leg_armor(35), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["mgj_boots_yunxue_uniq1","Warlord_armor", [("mgj_boots_yunxue", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1000, weight(3.5)|abundance(100)|leg_armor(35), imodbits_armor, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["zzsplinted_greaves_a","Splinted_greaves", [("splinted_greaves_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise, 0,370, weight(1.5)|abundance(100)|leg_armor(30), imodbits_armor|imodbit_cracked, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["yellowinfboots","Infantry_boots", [("yellowinfboots", 0)], itp_type_foot_armor|itp_attach_armature|itp_merchandise|itp_civilian, 0,311, weight(3.5)|abundance(10)|leg_armor(20), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["robe","Robe", [("sar_robered", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, 0,163, weight(1)|abundance(100)|body_armor(15)|leg_armor(4), imodbits_cloth, []],
  ["blue_gambeson","Monk_robes", [("priest_1", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,170, weight(4)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["tabard_hospitaller","Hospitallers tabard", [("tabard_hospitaller", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,975, weight(5)|abundance(10)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["coat_of_plates_b","White worn robe", [("coat_of_plates_b", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair, 0,163, weight(1)|abundance(100)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["red_dress2","Wool_dress", [("red_dress", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,100, weight(1)|abundance(10)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["cc_mgj_yel","Yellow_armor", [("mgj", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,800, weight(10)|abundance(30)|body_armor(55)|leg_armor(20), imodbits_armor, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["roman_shirt_female","Shirt", [("roman_shirt_female", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,250, weight(1)|abundance(10)|body_armor(15)|leg_armor(4), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["cc_swj","swj", [("swj", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,800, weight(10)|abundance(30)|body_armor(55)|leg_armor(20), imodbits_armor, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["shirt","Shirt", [("robe", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(0.5)|abundance(100)|body_armor(15)|leg_armor(4), imodbits_cloth, []],
  ["peasant_man_a","Shirt", [("peasant_man_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(0.5)|abundance(100)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["green_dress2","Formal dress", [("green_dress", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,500, weight(1)|abundance(10)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["loincloth_girl","Clothes", [("ro_light_body_under", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,20, weight(0.5)|abundance(10)|body_armor(15)|leg_armor(4), imodbits_armor, []],
  ["iri_highlander_armour_blue","Scottish armour", [("highlander_armour_blue", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(7)|abundance(10)|body_armor(44)|leg_armor(15), imodbits_armor, [], [fac_kingdom_18]],
  ["shirtb","Green_tunic", [("shirt_a_bry", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,210, weight(0.5)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["peasant_man_a","Tunic", [("peasant_man_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,210, weight(0.5)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["peasant_archer","Tunic", [("peasant_archer", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,210, weight(0.5)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["red_gambeson_a","Tunic", [("red_gambeson_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,210, weight(0.5)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jug_armor_adilshahi_chihali","Chihali", [("armor_adilshahi_chihali", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(10)|abundance(30)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_27,fac_kingdom_33]],
  ["linen_tunic","Linen tunic", [("shirt_a_bry", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,200, weight(0.5)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["short_tunic","Tunic", [("peasant_archer", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,200, weight(0.5)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["short_tunic","Tunic", [("peasant_man_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,200, weight(0.5)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["blue_tunic","Blue_Tunic", [("arena_tunicB_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,200, weight(0.5)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["blue_tunic","Blue_Tunic", [("arena_tunicB_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,200, weight(0.5)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["jjnew_kimono_1","Kimono", [("new_kimono_1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,240, weight(2)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["iber_gaelic_03","Clothes", [("gaelic_03", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(5)|abundance(30)|body_armor(40)|leg_armor(15), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["jjnew_kimono_2","Kimono", [("new_kimono_2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,240, weight(2)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["wwsayazn_waistcoat_man","Shirt", [("sayazn_waistcoat_man", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,310, weight(0.5)|abundance(100)|body_armor(40)|leg_armor(15), imodbits_cloth, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwsayazn_waistcoat_man_2","Shirt", [("sayazn_waistcoat_man_2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,310, weight(0.5)|abundance(100)|body_armor(40)|leg_armor(15), imodbits_cloth, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwwei_xiadi_archers_vest03","Eastern leather", [("wei_xiadi_archers_vest03", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(2)|abundance(10)|body_armor(38)|leg_armor(15), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwsar_robered","Sarranian clothes", [("sar_robered", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(0.5)|abundance(100)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwsar_robe","Sarranian robe", [("sar_robe", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(0.5)|abundance(100)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwwei_xiadi_swa_tabard","Arabian tabard", [("wei_xiadi_swa_tabard", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(30)|body_armor(59)|leg_armor(20), imodbits_cloth|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwwei_xiadi_sarranid_mamluk_robes","Arabian armor", [("wei_xiadi_sarranid_mamluk_robes", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,344, weight(2)|abundance(10)|body_armor(40)|leg_armor(15), imodbits_armor, [], [fac_kingdom_8,fac_kingdom_10,fac_kingdom_18,fac_kingdom_19,fac_kingdom_20,fac_kingdom_21,fac_kingdom_22,fac_kingdom_40]],
  ["coarse_tunic1","Merchants tunic", [("coarse_tunic_wt", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,500, weight(0.5)|abundance(100)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["jjman_cloth_2","Clothes", [("man_cloth_2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,140, weight(2)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["mmkhergit_lady_dress","Ladies dress", [("khergit_lady_dress", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(20)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["mmkhergit_lady_dress_b","Ladies dress", [("khergit_lady_dress_b", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(20)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["mmleather_jacket_new","Leather jacket", [("leather_jacket_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(20)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["mmnomad_armor_new","Nomad armor", [("nomad_armor_new", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,510, weight(1)|abundance(20)|body_armor(40)|leg_armor(10), imodbits_cloth, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["coarse_tunic","Poor Merchant's tunic", [("coarse_tunic_wt", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,100, weight(0.5)|abundance(100)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["leather_apron","Leather apron", [("leather_apron", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,161, weight(3)|abundance(100)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["iber_richleather_02","Clothes", [("richleather_02", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(5)|abundance(30)|body_armor(40)|leg_armor(15), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["iber_generictunic_10","Musketeers clothes", [("generictunic_10", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(5)|abundance(30)|body_armor(40)|leg_armor(15), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["wwsayazn_shirt_man_2","Shirt", [("sayazn_shirt_man_2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,310, weight(0.5)|abundance(100)|body_armor(40)|leg_armor(15), imodbits_cloth, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwsayazn_shirt_man","Shirt", [("sayazn_shirt_man", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,310, weight(0.5)|abundance(100)|body_armor(40)|leg_armor(15), imodbits_cloth, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["iber_generictunic_14","Musketeers tunic", [("generictunic_14", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(5)|abundance(30)|body_armor(40)|leg_armor(15), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jug_jungle_armor_ro_grey","Jungle armor", [("jungle_armor_ro_grey", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(5)|abundance(30)|body_armor(35)|leg_armor(5), imodbits_armor, [], [fac_kingdom_17,fac_kingdom_32,fac_kingdom_33]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["rrbronze_armor","Bronze armor", [("a_tribune", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,999, weight(20)|abundance(10)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["han_lamellar_a","Lamellar armor", [("han_lamellar_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,580, weight(6)|abundance(60)|body_armor(35)|leg_armor(10), imodbits_cloth, [], [fac_kingdom_1]],
  ["jjjyoroi","Yoroi", [("yoroi", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(20)|abundance(10)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["jjyoroi_red","Yoroi", [("yoroi_red", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(20)|abundance(10)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["jug_armor_adilshahi_chihalii","Chihali", [("armor_adilshahi_chihalii", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(10)|abundance(30)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_27,fac_kingdom_33]],
  ["jug_jungle_armor_ro","Jungle armor", [("jungle_armor_ro", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(3)|abundance(30)|body_armor(35)|leg_armor(5), imodbits_armor, [], [fac_kingdom_27,fac_kingdom_33]],
  ["iri_a_h3_1","Scottish armor", [("a_h3_1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,533, weight(10)|abundance(10)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_18]],
  ["amer_outfit1","Outfit", [("amer_outfit1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,111, weight(1)|abundance(10)|body_armor(15)|leg_armor(5), imodbits_armor, [], [fac_kingdom_50]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["cc_juanjia2","Moonguan armor", [("juanjia", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,800, weight(10)|abundance(30)|body_armor(55)|leg_armor(20), imodbits_armor, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["cc_mgj_late_y","Red armor", [("mgj_late_y", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,800, weight(10)|abundance(30)|body_armor(55)|leg_armor(20), imodbits_armor, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jjwei_xiadi_kher_lamellar_vest02","Haramaki", [("wei_xiadi_kher_lamellar_vest02", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,580, weight(6)|abundance(60)|body_armor(35)|leg_armor(15), imodbits_cloth, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["man_cloth_1","Cloth", [("man_cloth_1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,120, weight(3)|abundance(60)|body_armor(35)|leg_armor(15), imodbits_cloth, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["jjwei_xiadi_nord_lamellar_purple","Doumaru", [("wei_xiadi_nord_lamellar_purple", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,580, weight(6)|abundance(60)|body_armor(45)|leg_armor(15), imodbits_cloth, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jug_jungle_armor_r2","Jungle armor", [("jungle_armor_ro", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(5)|abundance(30)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_5,fac_kingdom_27,fac_kingdom_33]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["rrroman_light_armor","Light armor", [("roman_light_armor", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,111, weight(1)|abundance(50)|body_armor(35)|leg_armor(5), imodbits_cloth, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["rrragged_outfit_a","Ragged outfit", [("ragged_outfit_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,111, weight(1)|abundance(50)|body_armor(35)|leg_armor(5), imodbits_cloth, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["rrroman_shirt2","Shirt", [("roman_shirt", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,111, weight(1)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jjshadow_outfit_c","Outfit", [("shadow_outfit_c", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,580, weight(6)|abundance(60)|body_armor(50)|leg_armor(15), imodbits_cloth, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["rrroman_shirt","Shirt", [("roman_shirt", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,111, weight(1)|abundance(50)|body_armor(15)|leg_armor(5), imodbits_cloth, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["iber_baretunic_09","Cloth", [("baretunic_09", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,233, weight(2)|abundance(30)|body_armor(40)|leg_armor(15), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jjdomaru_b","Domaru", [("domaru_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(15)|abundance(10)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["iber_baretunic_01","Clothes", [("baretunic_01", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,233, weight(2)|abundance(30)|body_armor(40)|leg_armor(15), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["man_cloth_3","Clothes", [("man_cloth_3", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(20)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_1,fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29,fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43]],
  ["jjdomaru_r","Domaru", [("domaru_r", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(15)|abundance(10)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["lcuirass1","Cuirass", [("lcuirass1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,500, weight(5)|abundance(10)|body_armor(45)|leg_armor(15), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["leather_jacket","Grey_godelic_Jacket", [("thick_coat_a", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,300, weight(4)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["blue_dress_new","Blue dress", [("blue_dress_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,150, weight(1)|abundance(100)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["red_dress","Red dress", [("red_dress", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,150, weight(1)|abundance(100)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["woolen_dress","Woolen dress", [("woolen_dress", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,130, weight(1)|abundance(100)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["peasant_dress_b_new","Dress", [("peasant_dress_b_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,130, weight(1)|abundance(100)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["amer_body","Outfit", [("amer_body", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(4)|abundance(10)|body_armor(45)|leg_armor(15), imodbits_armor, [], [fac_kingdom_50]],
  ["amer_body2","Outfit", [("amer_body", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(4)|abundance(10)|body_armor(45)|leg_armor(15), imodbits_armor, [], [fac_kingdom_50]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["han_g_armor2_2bu","Point_Armor", [("Han_g_armor2_2bu", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(10)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_1]],
  ["jjdomaru_a","Domaru", [("domaru_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(15)|abundance(10)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["per_corselet2","Corselet", [("corselet2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,300, weight(10)|abundance(10)|body_armor(53)|leg_armor(20), imodbits_none, [], [fac_kingdom_9]],
  ["han_g_armor2_2br","Point_Armor", [("Han_g_armor2_2br", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(10)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_1]],
  ["han_g_armor2_2yb","Point_Armor", [("Han_g_armor2_2yb", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(10)|body_armor(49)|leg_armor(20), imodbits_armor, [], [fac_kingdom_1]],
  ["han_g_armor2_2n","Point_Armor", [("Han_g_armor2_2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(10)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_1]],
  ["inca_outfit","Inca_outfit", [("inca_outfit", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(4)|abundance(10)|body_armor(45)|leg_armor(15), imodbits_armor, [], [fac_kingdom_45]],
  ["inca_outfit2","Inca_outfit", [("inca_outfit2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(4)|abundance(10)|body_armor(45)|leg_armor(15), imodbits_armor, [], [fac_kingdom_45]],
  ["inca_outfit3","Inca_outfit", [("inca_outfit3", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(4)|abundance(10)|body_armor(45)|leg_armor(15), imodbits_armor, [], [fac_kingdom_45]],
  ["inca_outfit4","Inca_outfit", [("inca_outfit4", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(4)|abundance(10)|body_armor(45)|leg_armor(15), imodbits_armor, [], [fac_kingdom_45]],
  ["han_g_armor2_yel","Scale_armor", [("Han_g_armor2_yel", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(100)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_1]],
  ["han_g_armor_red","Scale_armor", [("Han_g_armor2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(100)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_1]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["cc_armor_lam","Leather armor", [("armor_lam", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(4)|abundance(10)|body_armor(55)|leg_armor(20), imodbits_armor, [], [fac_kingdom_7,fac_kingdom_14,fac_kingdom_16,fac_kingdom_21,fac_kingdom_22,fac_kingdom_26,fac_kingdom_29,fac_kingdom_30,fac_kingdom_52]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["rr_romanbreastplate_red","Bronze armor", [("romanbreastplate_red", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(4)|abundance(10)|body_armor(55)|leg_armor(20), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["per_corselet5","Corselet", [("corselet5", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,500, weight(10)|abundance(10)|body_armor(53)|leg_armor(20), imodbits_none, [], [fac_kingdom_9]],
  ["jjheraldic_domaru_nobori","Domaru", [("domaru_nobori", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,800, weight(20)|abundance(10)|body_armor(59)|leg_armor(20), imodbits_armor, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_samurai_heraldic_flag", ":var0", ":var1"),
    ]),
   ], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["rr_romanbreastplate_whi","Bronze breastplate", [("romanbreastplate_whi", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,533, weight(4)|abundance(10)|body_armor(55)|leg_armor(20), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rr_roman_cent_hamata","Roman armor", [("roman_cent_hamata", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1022, weight(8)|abundance(10)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["cc_tunic_fur","Fur Tunic", [("tunic_fur", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,122, weight(4)|abundance(10)|body_armor(40)|leg_armor(10), imodbits_armor, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["gallic_body","Gaelic Woad", [("gallic_woad", 0)], itp_type_body_armor, 0,112, weight(2)|abundance(15)|body_armor(35)|leg_armor(5), imodbits_cloth, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["heraldic_armor_new_c","Heraldic armor", [("heraldic_armor_new_c", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,444, weight(5)|abundance(10)|body_armor(45)|leg_armor(15), imodbits_armor, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_c", ":var0", ":var1"),
    ]),
   ]],
  ["cc_nomad_vest_new","Nomads vest", [("nomad_vest_new", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,222, weight(4)|abundance(10)|body_armor(40)|leg_armor(10), imodbits_armor, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["cc_nmd_warrior_a","Warriors outfit", [("nmd_warrior_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,222, weight(4)|abundance(10)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["corselet5","Corselet", [("corselet5", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,555, weight(10)|abundance(30)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["leather_imperial_armor_mesh","Leather armor", [("leather_imperial_armor_mesh", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,555, weight(10)|abundance(30)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["iber_dress","Dress", [("dress", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,244, weight(1)|abundance(10)|body_armor(15)|leg_armor(4), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["iber_cbride_dress","Dress", [("bride_dress", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,244, weight(1)|abundance(10)|body_armor(15)|leg_armor(4), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["mm_lamellar_vest_a","Lamellar vest", [("lamellar_vest_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,400, weight(8)|abundance(30)|body_armor(55)|leg_armor(20), imodbits_armor, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["mm_lamellar_vest_b","Lamellar vest", [("lamellar_vest_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,400, weight(8)|abundance(30)|body_armor(55)|leg_armor(20), imodbits_armor, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["lamellar_leather","Lamellar armor", [("lamellar_leather", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,400, weight(8)|abundance(30)|body_armor(40)|leg_armor(15), imodbits_armor, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["pir_richleather_04","Uniform", [("richleather_04", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,111, weight(0.5)|abundance(100)|body_armor(40)|leg_armor(10), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_25]],
  ["cc_swj2","Warchiefs armor", [("swj", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,800, weight(10)|abundance(30)|body_armor(55)|leg_armor(20), imodbits_armor, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["mgj_late","Armor", [("mgj_late", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,800, weight(10)|abundance(30)|body_armor(55)|leg_armor(20)|difficulty(11), imodbits_armor, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["east_woman_cloth_3","Dress", [("east_woman_cloth_3", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,244, weight(1)|abundance(10)|body_armor(15)|leg_armor(4), imodbits_armor, [], [fac_kingdom_1,fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29,fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43]],
  ["rough_leather_fur","Rough leather", [("rough_leather_fur", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,400, weight(8)|abundance(30)|body_armor(40)|leg_armor(15), imodbits_armor, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["east_woman_cloth_2","Dress", [("east_woman_cloth_2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,244, weight(1)|abundance(10)|body_armor(15)|leg_armor(4), imodbits_armor, [], [fac_kingdom_1,fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29,fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["court_dress","Dress", [("court_dress", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,348, weight(1)|abundance(100)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["rrroman_hamata","Hamata", [("roman_hamata", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(5)|abundance(30)|body_armor(40)|leg_armor(15), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrroman_squamata","Squamata", [("roman_squamata", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(5)|abundance(30)|body_armor(35)|leg_armor(15), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["qqarmor_3","Leather shirt", [("armor_3", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(8)|abundance(30)|body_armor(40)|leg_armor(15), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqrich_mail","Rich mail", [("rich_mail", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(7)|abundance(30)|body_armor(40)|leg_armor(15), imodbits_armor, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqhaubergeon_d","Haubergeon", [("haubergeon_d", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(8)|abundance(30)|body_armor(40)|leg_armor(15), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["man_cloth_4","Clothes", [("man_cloth_4", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,100, weight(0.5)|abundance(50)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["lady_dress_r","Dress", [("lady_dress_r", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,500, weight(3)|abundance(10)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["wwwei_xiadi_archers_vest02","Archers vest", [("wei_xiadi_archers_vest02", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(6)|abundance(30)|body_armor(38)|leg_armor(15), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwjacobhinds_long_waistcoat","Long waistcoat", [("jacobhinds_long_waistcoat", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(6)|abundance(30)|body_armor(45)|leg_armor(15), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwsar_pants","Pants", [("sar_pants", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(2)|abundance(30)|body_armor(15)|leg_armor(4), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwjacobhinds_long_waistcoat_1","Long waistcoat", [("jacobhinds_long_waistcoat_1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(6)|abundance(30)|body_armor(45)|leg_armor(15), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwjacobhinds_long_waistcoat_2","Long waistcoat", [("jacobhinds_long_waistcoat_2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(6)|abundance(30)|body_armor(45)|leg_armor(15), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["pir_buffcoat_04","Uniform", [("buffcoat_04", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,222, weight(1.5)|abundance(100)|body_armor(40)|leg_armor(10), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_25]],
  ["per_leather_imperial_armor_mesh","Leather armor", [("leather_imperial_armor_mesh", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,522, weight(10)|abundance(10)|body_armor(53)|leg_armor(20), imodbits_none, [], [fac_kingdom_9]],
  ["heraldic_armor_new_b","Heraldic armor", [("heraldic_armor_new_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,444, weight(5)|abundance(10)|body_armor(45)|leg_armor(15), imodbits_armor, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_b", ":var0", ":var1"),
    ]),
   ]],
  ["red_dress3","Dress", [("red_dress", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,222, weight(1)|abundance(10)|body_armor(45)|leg_armor(15), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["lady_dress_b","Dress", [("lady_dress_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,500, weight(1)|abundance(10)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["lady_dress_g","Dress", [("lady_dress_g", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,500, weight(1)|abundance(10)|body_armor(15)|leg_armor(4), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["heraldic_armor_new_a","Heraldic armor", [("heraldic_armor_new_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(5)|abundance(10)|body_armor(63)|leg_armor(28), imodbits_armor, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":var0", ":var1"),
    ]),
   ]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["rritalianxiphos","Hoplite sword", [("Italianxiphos", 0),("Italianxiphos_sc", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_cleaver,580, weight(0.75)|abundance(100)|difficulty(2)|hit_points(20480)|spd_rtng(88)|weapon_length(60)|thrust_damage(38, pierce)|swing_damage(35, cut), imodbits_sword, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["green_dress","Dress", [("green_dress", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,222, weight(1)|abundance(10)|body_armor(45)|leg_armor(15), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["arab_sarranid_lady_dress_b","Dress", [("sarranid_lady_dress_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,24, weight(1)|abundance(10)|body_armor(15)|leg_armor(4), imodbits_armor, [], [fac_kingdom_8,fac_kingdom_10,fac_kingdom_18,fac_kingdom_19,fac_kingdom_20,fac_kingdom_21,fac_kingdom_22,fac_kingdom_40]],
  ["arab_sarranid_lady_dress","Dress", [("sarranid_lady_dress", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,242, weight(1)|abundance(10)|body_armor(15)|leg_armor(4), imodbits_armor, [], [fac_kingdom_8,fac_kingdom_10,fac_kingdom_18,fac_kingdom_19,fac_kingdom_20,fac_kingdom_21,fac_kingdom_22,fac_kingdom_40]],
  ["wwwei_xiadi_swa_tabard2","Mamluks mail", [("wei_xiadi_swa_tabard", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,444, weight(5)|abundance(10)|body_armor(40)|leg_armor(15), imodbits_armor, [], [fac_kingdom_8,fac_kingdom_10,fac_kingdom_18,fac_kingdom_19,fac_kingdom_20,fac_kingdom_21,fac_kingdom_22,fac_kingdom_40]],
  ["heraldic_armor_new_d","Heraldic armor", [("heraldic_armor_new_d", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(5)|abundance(10)|body_armor(63)|leg_armor(28), imodbits_armor, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_d", ":var0", ":var1"),
    ]),
   ]],
  ["cc_bubinjia","Bubinjia", [("bubinjia", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(10)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["cc_khergit_leather_e","Leather armor", [("khergit_leather_e", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(55)|leg_armor(20), imodbits_armor, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["cc_armor_1","Armor", [("armor_1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["early_transitional_heraldic","Early transitional armor", [("early_transitional_heraldic", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,9900, weight(22)|abundance(100)|body_armor(70)|leg_armor(40)|difficulty(30), imodbits_armor, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_early_transitional_heraldic", ":var0", ":var1"),
    ]),
   ]],
  ["cc_khergit_scale_c","Armor", [("khergit_scale_c", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jjjyoroihev_uniq1","Evil_spirits_armor", [("yoroi", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(22)|abundance(10)|body_armor(70)|leg_armor(40)|difficulty(30), imodbits_armor, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["jjjyoroihev2","yoroi", [("yoroi", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(22)|abundance(10)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["cc_rough_macle_fured","Rough macle armor", [("rough_macle_fured", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["cc_juanjia","Juanjia", [("juanjia", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["cc_armor_2","Nomads armor", [("armor_2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["qq_rus_scale","Scale armor", [("rus_scale", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_47,fac_kingdom_56,fac_kingdom_64]],
  ["qq_kuyak_a","Kuyak", [("kuyak_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_47,fac_kingdom_56,fac_kingdom_64]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["cc_mgj_early","Armor", [("mgj_early", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["rrcorselet1","Corselet", [("corselet1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["qqarmor_24","Broigne", [("armor_24", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_47,fac_kingdom_56,fac_kingdom_64]],
  ["qqbroigne5","Broigne", [("broigne5", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_47,fac_kingdom_56,fac_kingdom_64]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["wwwei_xiadi_sar_leather_chain","Eastern armor", [("wei_xiadi_sar_leather_chain", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwwei_xiadi_sar_decorated_surcoat02","Eastern armor", [("wei_xiadi_sar_decorated_surcoat02", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwwei_xiadi_mail_shirt02","Mail shirt", [("wei_xiadi_mail_shirt02", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(25), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["qqbroigne_shirt_metal_plate","Broigne shirt with metal plates", [("broigne_shirt_metal_plate", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,555, weight(9)|abundance(30)|body_armor(59)|leg_armor(19), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqad_viking_byrnie_03","Byrnie", [("ad_viking_byrnie_03", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,555, weight(9)|abundance(10)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqad_viking_byrnie_06","Byrnie", [("ad_viking_byrnie_06", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,555, weight(9)|abundance(10)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["rough_spiked_plainring","Rough_spiked_plainring", [("rough_spiked_plainring", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,500, weight(10)|abundance(10)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["armor_45","Armor", [("armor_45", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,500, weight(10)|abundance(10)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["gallic_woad","Gaelic woad", [("gallic_woad", 0)], itp_type_body_armor, 0,1000, weight(2)|abundance(100)|body_armor(63)|leg_armor(28)|difficulty(65), imodbits_cloth, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrspartanbronzehero_uniq1","Spartan armor", [("a_tribune", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,29999, weight(19)|abundance(100)|body_armor(67)|leg_armor(37), imodbits_none, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["chain_tab_2","Chainmail", [("chain_tab_2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,500, weight(10)|abundance(10)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["qqmilanese_armour","Milanese armor", [("milanese_armour", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,11000, weight(30)|abundance(10)|body_armor(65)|leg_armor(35)|difficulty(30), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qqcorrazina_green","Heavy armor", [("corrazina_green", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(20)|abundance(10)|body_armor(64)|leg_armor(29), imodbits_armor, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18,fac_kingdom_23,fac_kingdom_24,fac_kingdom_25]],
  ["qqcorrazina_red","Heavy_armor", [("corrazina_red", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(20)|abundance(10)|body_armor(64)|leg_armor(29), imodbits_armor, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18,fac_kingdom_23,fac_kingdom_24,fac_kingdom_25]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qqsurcoat_over_mail_hospitaller","Surcoat", [("surcoat_over_mail_hospitaller", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_6]],
  ["qqteu_armor_30","Surcoat", [("armor_30", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qqad_viking_byrnie_06","Byrnie", [("ad_viking_byrnie_06", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,555, weight(9)|abundance(10)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqad_viking_byrnie_03","Byrnie", [("ad_viking_byrnie_03", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,555, weight(9)|abundance(10)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqad_viking_byrnie_01","Byrnie", [("ad_viking_byrnie_01", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,555, weight(9)|abundance(10)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["afri_native_body","body", [("afri_native_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,100, weight(1)|abundance(100)|body_armor(35)|leg_armor(15), imodbits_none, [], [fac_kingdom_34,fac_kingdom_46]],
  ["cuirassier2","cuirassier", [("cuirassier2", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(70)|leg_armor(40)|difficulty(30), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["wwsarranian_mail_shirt","mail_shirt", [("sarranian_mail_shirt", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(10)|abundance(10)|body_armor(63)|leg_armor(25), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["cuirassier1","cuirassier", [("cuirassier1", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(70)|leg_armor(40)|difficulty(30), imodbits_armor, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["east_woman_cloth_1","Woman_dress", [("east_woman_cloth_1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,244, weight(1)|abundance(10)|body_armor(55)|leg_armor(15), imodbits_armor, [], [fac_kingdom_1,fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29,fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43]],
  ["early_transitional_white_uniq1","Plate_armor", [("early_transitional_white", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,9900, weight(22)|abundance(100)|body_armor(70)|leg_armor(40)|difficulty(30), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["yoroi_uniq1","Samurai_black_plate", [("yoroi", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,9900, weight(22)|abundance(100)|body_armor(70)|leg_armor(40), imodbits_armor, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["wwsarranid_elite_cavalary","elite_cavalary", [("sarranid_elite_cavalary", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(25), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwlamellar_armor_c","Lamellar armor", [("lamellar_armor_c", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(25), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["wwtunic_armor_a","tunic_armor_a", [("tunic_armor_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(25), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwwei_xiadi_sarranid_mamluk_armor","mamluk_armor", [("wei_xiadi_sarranid_mamluk_armor", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(25), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["mmlamellar_armor_a","Lamellar armor", [("lamellar_armor_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(25), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["romanbreastplate_red2","cuirass_spartan", [("romanbreastplate_red", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(25), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["mmwei_xiadi_lamellar_armor02","Mongol_armor", [("wei_xiadi_lamellar_armor02", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(30)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_21,fac_kingdom_22,fac_kingdom_30]],
  ["byz_scale_shirt","scale_shirt", [("scale_shirt", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,800, weight(16)|abundance(30)|body_armor(63)|leg_armor(25), imodbits_armor, [], [fac_kingdom_7,fac_kingdom_16,fac_kingdom_26]],
  ["byz_broigne_shirt","Broigne_mail", [("broigne_shirt", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,800, weight(16)|abundance(30)|body_armor(63)|leg_armor(25), imodbits_armor, [], [fac_kingdom_7,fac_kingdom_16,fac_kingdom_26]],
  ["byz_mail_coat_f","mail_shirt", [("mail_coat_f", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,800, weight(16)|abundance(30)|body_armor(63)|leg_armor(25), imodbits_armor, [], [fac_kingdom_7,fac_kingdom_16,fac_kingdom_26]],
  ["byz_mail_coat_a","mail_shirt", [("mail_coat_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,800, weight(16)|abundance(30)|body_armor(63)|leg_armor(25), imodbits_armor, [], [fac_kingdom_7,fac_kingdom_16,fac_kingdom_26]],
  ["byz_ragged_scale_b","scale_heavy", [("ragged_scale_b", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,800, weight(10)|abundance(30)|body_armor(63)|leg_armor(25), imodbits_armor, [], [fac_kingdom_7,fac_kingdom_16,fac_kingdom_26]],
  ["qqrus_lamellar_b","Russian lamellar armor", [("rus_lamellar_b", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(16)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqkuyak_b","Kuyak armor", [("kuyak_b", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["lamellar_armor_e","Lamellar armor", [("lamellar_armor_e", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,800, weight(8)|abundance(30)|body_armor(45)|leg_armor(15), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["cru_mail_surcoat_a_kt","Surcoat", [("mail_surcoat_a_kt", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_6]],
  ["iber_genericpikeman_02","Pikiner", [("genericpikeman_02", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["iber_genericpikeman_08","Pikeman_armor", [("genericpikeman_08", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["iber_early_transitional_blue","early_transitional_blue", [("early_transitional_blue", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(70)|leg_armor(40)|difficulty(30), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["iber_churburg_13_mail","churburg_mail", [("churburg_13_mail", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["qqearly_transitional_orange_uniq","early_transitional_orange", [("early_transitional_orange", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,31000, weight(30)|abundance(5)|body_armor(70)|leg_armor(40)|difficulty(30), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["iber_churburg_13_brass","Churburg_brass", [("churburg_13_brass", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["iber_bnw_armour_stripes","Armour_stripes", [("bnw_armour_stripes", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(30)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["legacy_uniq1","Legacy_armor", [("nord_coat_of_plates", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1000, weight(19)|abundance(100)|body_armor(63)|leg_armor(28), imodbits_armor, [], [fac_kingdom_23,fac_kingdom_25]],
  ["mmwei_xiadi_samurai_armor02","Mongol_armor", [("wei_xiadi_samurai_armor02", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(30)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_21,fac_kingdom_22,fac_kingdom_30]],
  ["pijia_uniq1","Warlord_armor", [("pijia", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,29999, weight(19)|abundance(100)|body_armor(65)|leg_armor(35), imodbit_thick|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["amer_outfit2","amer_outfit", [("amer_outfit2", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,333, weight(1)|abundance(10)|body_armor(45)|leg_armor(15), imodbits_armor, [], [fac_kingdom_50]],
  ["rrroman_armor","roman_armor", [("roman_armor", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(30)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrroman_armor_red","roman_armor_red", [("roman_armor_red", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(30)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrroman_armor_cent","roman_armor_cent", [("roman_armor_cent", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(30)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrroman_armor_white","roman_armor_white", [("roman_armor_white", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(30)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["wwsar_scale_a","arab_scale_mail", [("sar_scale_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(30)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwwei_xiadi_swa_tabard","Arabic armor", [("wei_xiadi_swa_tabard", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(30)|body_armor(59)|leg_armor(20), imodbits_cloth|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwarabian_armor_a","arabian_armor_a", [("arabian_armor_a", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(30)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwwei_xiadi_sar_leather_armor","leather_armor", [("wei_xiadi_sar_leather_armor", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(10)|body_armor(59)|leg_armor(20), imodbits_none, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["mmwei_xiadi_lamellar_armor03","Mongol_armor", [("wei_xiadi_lamellar_armor03", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(30)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_21,fac_kingdom_22,fac_kingdom_30]],
  ["mmmongol_armor_gray","Mongol_armor", [("mongol_armor_gray", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(30)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_21,fac_kingdom_22,fac_kingdom_30]],
  ["han_g_armor","Scale_armor", [("Han_g_armor2_br", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(100)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_1]],
  ["han_g_armor_dark","Scale_armor", [("Han_g_armor_dark", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,700, weight(10)|abundance(100)|body_armor(59)|leg_armor(20), imodbits_armor, [], [fac_kingdom_1]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["han_g_head","Helmet", [("Han_g_head2_br", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,500, weight(2)|abundance(100)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_1]],
  ["han_g_head_dark","Helmet", [("Han_g_head_dark", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,500, weight(2)|abundance(100)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_1]],
  ["han_g_head_red","Helmet", [("Han_g_head2", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,500, weight(2)|abundance(100)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_1]],
  ["han_g_head_yellow","Helmet", [("Han_g_head2_yel", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,500, weight(2)|abundance(100)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_1]],
  ["555_helmet_infil_river","hide_helmet", [("hide_helmet", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,11, weight(0.5)|abundance(100)|head_armor(5), imodbits_none, []],
  ["555_helmet_ambush_forest","hide_helmet", [("hide_helmet", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,11, weight(0.5)|abundance(100)|head_armor(5), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["hair_band_east","Hair_band", [("hair_band_east", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,10, weight(1)|abundance(10)|head_armor(10), imodbits_cloth, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["youhou_assassin_hood","Hood", [("youhou_assassin_hood", 0)], itp_type_head_armor|itp_civilian, 0,280, weight(1)|abundance(10)|head_armor(35), imodbits_cloth, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["youhou_assassin_hood_red","Hood", [("youhou_assassin_hood_red", 0)], itp_type_head_armor|itp_civilian, 0,280, weight(1)|abundance(10)|head_armor(35), imodbits_cloth, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["woolen_cap_newblu","Blue_cap", [("woolen_cap_newblu", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,100, weight(1)|abundance(15)|head_armor(10), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["woolen_cap_newred","Narrow_cap", [("woolen_cap_newred", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,100, weight(1)|abundance(15)|head_armor(10), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["woolen_cap_newgrn","Green_cap", [("woolen_cap_newgrn", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,100, weight(1)|abundance(15)|head_armor(10), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["woolen_cap_newblk","Black_cap", [("woolen_cap_newblk", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,100, weight(1)|abundance(15)|head_armor(10), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["woolen_cap_newwht","White_cap", [("woolen_cap_newwht", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,100, weight(1)|abundance(15)|head_armor(10), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["woolen_cap","Woolen_Cap", [("woolen_cap_new_bry", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,100, weight(1)|abundance(15)|head_armor(10), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["hood_newblu","Hood", [("hood_newblu", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,110, weight(1)|abundance(15)|head_armor(10), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["hood_newred","Hood", [("hood_newred", 0)], itp_type_head_armor|itp_civilian, 0,110, weight(1)|abundance(15)|head_armor(10), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["hood_newblk","Hood", [("hood_newblk", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,110, weight(1)|abundance(15)|head_armor(10), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["hood_newwht","Hood", [("hood_newwht", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,110, weight(1)|abundance(15)|head_armor(10), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["black_hood","Black_Hood", [("hood_black_bry", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,110, weight(1)|abundance(15)|head_armor(10), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["head_wrappings","Head_Wrapping", [("head_wrapping_bry", 0)], itp_type_head_armor|itp_fit_to_head, 0,30, weight(0.25)|abundance(100)|head_armor(6), imodbit_tattered|imodbit_ragged|imodbit_sturdy|imodbit_thick, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["mmnomad_cap_a_new","nomad_cap", [("nomad_cap_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,110, weight(1)|abundance(15)|head_armor(45), imodbits_cloth, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["mmnomad_cap_b_new","Nomad_cap", [("nomad_cap_b_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,110, weight(1)|abundance(15)|head_armor(45), imodbits_cloth, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["mmleather_steppe_cap_a_new","leather_steppe_cap", [("leather_steppe_cap_a_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,110, weight(1)|abundance(15)|head_armor(10), imodbits_cloth, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["common_hood","Hood", [("hood_new_bry", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,40, weight(1)|abundance(15)|head_armor(8), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["per_helm","Persian_helmet", [("per_helm", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian|itp_fit_to_head, 0,280, weight(1.75)|abundance(40)|head_armor(45), imodbits_armor|imodbit_cracked, [], [fac_kingdom_9]],
  ["qqinv_rus_helm","Helmet", [("inv_rus_helm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,580, weight(1.75)|abundance(40)|head_armor(65), imodbits_armor|imodbit_cracked, [], [fac_kingdom_47,fac_kingdom_56,fac_kingdom_64]],
  ["arabia_noble_veil_girl","Noble_veil", [("arabia_noble_veil", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,780, weight(0.25)|abundance(10)|head_armor(10), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["qqinv_novogrod_helm","Helmet", [("inv_novogrod_helm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,580, weight(1.75)|abundance(40)|head_armor(65), imodbits_armor|imodbit_cracked, [], [fac_kingdom_47,fac_kingdom_56,fac_kingdom_64]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qqinv_tagancha_helm_a","Helmet", [("inv_tagancha_helm_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,580, weight(1.75)|abundance(40)|head_armor(65), imodbits_armor|imodbit_cracked, [], [fac_kingdom_47,fac_kingdom_56,fac_kingdom_64]],
  ["mmlamellar_helmet_a","Mongol_helmet", [("lamellar_helmet_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,580, weight(1.75)|abundance(40)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_21,fac_kingdom_22,fac_kingdom_30]],
  ["mmmon_helmet_07_lam1","Mongol_helmet", [("mon_helmet_07_lam1", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,580, weight(1.75)|abundance(40)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_21,fac_kingdom_22,fac_kingdom_30]],
  ["mmvaeg_helmet4","Mongol_helmet", [("vaeg_helmet4", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,580, weight(1.75)|abundance(40)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_21,fac_kingdom_22,fac_kingdom_30]],
  ["jjkabuto_sep_red","Kabuto", [("kabuto_sep_red", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,450, weight(3)|abundance(10)|head_armor(65), imodbits_armor|imodbit_cracked, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["wwarab_turban_c","Turban", [("arab_turban_white", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_fit_to_head, 0,6, weight(1)|abundance(100)|head_armor(15), imodbits_cloth, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jjjkabuto2222","Kabuto", [("kabuto2222_inv", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,450, weight(3)|abundance(10)|head_armor(65), imodbits_armor|imodbit_cracked, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["cc_swj_douao","Douao", [("swj_douao", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,340, weight(2.5)|abundance(80)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["cc_mgj_late_douao","Late douao", [("mgj_late_douao", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,340, weight(2.5)|abundance(80)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["jjkabuto2222_sep","Kabuto", [("kabuto2222_sep", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,450, weight(3)|abundance(10)|head_armor(65), imodbits_armor|imodbit_cracked, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["hanhelm","Soldier_helmet", [("hanhelm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,200, weight(2)|abundance(50)|head_armor(45), imodbits_armor|imodbit_cracked, [], [fac_kingdom_1]],
  ["cc_mgj_douao","Douao", [("mgj_douao", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,340, weight(2.5)|abundance(80)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["byz_old_spangenhelmaven","Helmet", [("old_spangenhelmaven", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,300, weight(3)|abundance(90)|head_armor(55), imodbits_cloth, [], [fac_kingdom_7,fac_kingdom_16,fac_kingdom_26]],
  ["byz_spangenhelm_helm","Spangen helmet", [("spangenhelm_helm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,300, weight(3)|abundance(90)|head_armor(55), imodbits_cloth, [], [fac_kingdom_7,fac_kingdom_16,fac_kingdom_26]],
  ["byz_rathos_spangenhelm_a","Spangen helmet", [("Rathos_Spangenhelm_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,300, weight(3)|abundance(90)|head_armor(55), imodbits_cloth, [], [fac_kingdom_7,fac_kingdom_16,fac_kingdom_26]],
  ["wwrabati","Rabati", [("rabati", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,200, weight(2)|abundance(20)|head_armor(30), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["rus_helmet_1","Helmet", [("helmet_1", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,300, weight(3)|abundance(90)|head_armor(55), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["rus_helmet_2","Helmet", [("helmet_2", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,300, weight(3)|abundance(90)|head_armor(55), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["afri_rabati_new","rabati", [("rabati_new", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,110, weight(1)|abundance(90)|head_armor(30), imodbits_cloth, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["meruruhair","Meruruhair", [("meruruhair", 0)], itp_type_head_armor|itp_civilian, 0,110, weight(1)|abundance(100)|head_armor(30), imodbits_cloth, []],
  ["pir_tricorne_goldlace_cockade_white","Tricorne", [("tricorne_goldlace_cockade_white", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(90)|head_armor(30), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_25]],
  ["pir_tricorne_whitelace_nocockade","Tricorne", [("tricorne_whitelace_nocockade", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(90)|head_armor(30), imodbits_cloth, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["pir_pirates_tricorne","Tricorne", [("pirates_tricorne", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(90)|head_armor(30), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_25]],
  ["jjnon_la","Jingasa", [("non_la", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,200, weight(1)|abundance(80)|head_armor(40), imodbits_cloth, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["officerhatblack","Hat", [("officerhatblack", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(90)|head_armor(30), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_25]],
  ["officerhatbrown","Hat", [("officerhatbrown", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(90)|head_armor(30), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_25]],
  ["non_la2","Straw_hat", [("non_la2", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,90, weight(1)|abundance(80)|head_armor(18), imodbits_cloth, []],
  ["crown_m","Crown", [("osp_crown", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian|itp_fit_to_head, 0,5000, weight(2)|abundance(100)|head_armor(65), imodbits_cloth, []],
  ["brownhat2","Hat", [("brownhat2", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(90)|head_armor(30), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_25]],
  ["wwsaracen_helmet_d","Saracen_helmet", [("saracen_helmet_d", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,380, weight(1.75)|abundance(40)|head_armor(65), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["ccpimao","Pimao", [("pimao", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,360, weight(1.75)|abundance(20)|head_armor(40), imodbits_armor|imodbit_cracked, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["bluehat1","Hat", [("bluehat1", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(90)|head_armor(30), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_25]],
  ["qqcoif_crown_b","Coif_crown", [("coif_crown_b", 0)], itp_type_head_armor|itp_fit_to_head, 0,780, weight(2)|abundance(10)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["wwblack_sar_helmet1","Arabic_helmet", [("black_sar_helmet1", 0)], itp_type_head_armor|itp_fit_to_head, 0,780, weight(3)|abundance(10)|head_armor(65), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwtuareg_helmet","Arabic_helmet", [("tuareg_helmet", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_covers_beard, 0,780, weight(3)|abundance(10)|head_armor(65), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["qqfacecovermail_plume","Plume", [("facecovermail_plume", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,580, weight(3)|abundance(10)|head_armor(65), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqosp_greathelm_b2","Full helmet", [("osp_greathelm_b", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_covers_head, 0,580, weight(4)|abundance(10)|head_armor(70), imodbits_armor|imodbit_cracked, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqhelmet_21","Full helmet", [("helmet_21", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_covers_head, 0,580, weight(4)|abundance(10)|head_armor(70), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqlobster1","Lobster helmet", [("lobster1", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,1500, weight(3.75)|abundance(10)|head_armor(75)|difficulty(30), imodbits_armor|imodbit_cracked, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqarmet_04","Armet", [("armet_04", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,1500, weight(3.75)|abundance(10)|head_armor(75)|difficulty(30), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["qqarmet_02","Armet", [("armet_02", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_covers_head, 0,1500, weight(4)|abundance(10)|head_armor(75)|difficulty(30), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["qqvisored_salet_coif","Salet_coif", [("visored_salet_coif", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,1500, weight(3)|abundance(20)|head_armor(75)|difficulty(30), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["qqhelmet_20","Fullhelm", [("helmet_20", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_covers_head, 0,580, weight(4)|abundance(10)|head_armor(70), imodbits_armor|imodbit_cracked, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qqlobster2","Lobster helmet", [("lobster2", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,1500, weight(3.75)|abundance(10)|head_armor(75)|difficulty(30), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["lagacy_helm_uniq1","Legacy_helm", [("inv_nord_ornate_visored_helmet", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,1580, weight(2)|abundance(100)|head_armor(75), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["cc_tangtiedou","Tangtiedou", [("tangtiedou", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,340, weight(2.5)|abundance(80)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["cc_bubinjia_douao","Helmet", [("bubinjia_douao", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,340, weight(2.5)|abundance(80)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["qq_inv_gnezdovo_helm_a","Gnezdovo_helmet", [("inv_gnezdovo_helm_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,540, weight(2.5)|abundance(80)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_7,fac_kingdom_16,fac_kingdom_26]],
  ["qq_inv_tagancha_helm_b","Tagancha_helmet", [("inv_tagancha_helm_b", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,540, weight(2.5)|abundance(80)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_7,fac_kingdom_16,fac_kingdom_26]],
  ["qq_helm9","Helmet", [("helm9", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,540, weight(2.5)|abundance(80)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_7,fac_kingdom_16,fac_kingdom_26]],
  ["rrroman_helm_lego","Roman_helmet", [("roman_helm_lego", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,420, weight(2)|abundance(40)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrroman_helm_preator","Roman_helmet", [("roman_helm_preator", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,760, weight(2)|abundance(60)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrroman_helm_cent","Centurions_helmet", [("roman_helm_cent", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,760, weight(2)|abundance(60)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["blackhat2","Hat", [("blackhat2", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(90)|head_armor(30), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_25]],
  ["brownhat1","Hat", [("brownhat1", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(90)|head_armor(30), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_25]],
  ["officerhatblue","Hat", [("officerhatblue", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(90)|head_armor(30), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_25]],
  ["rr_corintiah_helmet","Corintiah_helmet", [("corintiah_helmet", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,320, weight(2.75)|abundance(40)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["mm_lamellar_helmet_kk","Lamellar_helmet", [("lamellar_helmet_KK", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,220, weight(1.5)|abundance(40)|head_armor(50), imodbits_armor|imodbit_cracked, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["rus_helmet_12","Helmet", [("helmet_12", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,300, weight(3)|abundance(90)|head_armor(55), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["rragenhelm","Helmet", [("agenhelm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,520, weight(2.75)|abundance(40)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["tuareg_open_white","White_hood", [("tuareg_open_white", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,90, weight(1)|abundance(80)|head_armor(18), imodbits_cloth, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["wwsar_helmet1","Arabic_helmet", [("sar_helmet1", 0)], itp_type_head_armor|itp_fit_to_head, 0,780, weight(3)|abundance(10)|head_armor(65), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["qqnasal_helmet_b","Pointed_helmet", [("nasal_helmet_b", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,320, weight(2.5)|abundance(40)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqhelmet_w_eyeguard_new","Viking_helmet", [("helmet_w_eyeguard_new", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,300, weight(2)|abundance(90)|head_armor(55), imodbits_cloth, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqreinf_helmet_new","Helmet", [("reinf_helmet_new", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,360, weight(2)|abundance(80)|head_armor(55), imodbits_cloth, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qqosp_kettle_hat_a","Kettle_hat", [("osp_kettle_hat_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,380, weight(2.5)|abundance(40)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqmaciejowski_helmet_new","Full helmet", [("maciejowski_helmet_new", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_covers_head, 0,780, weight(4)|abundance(60)|head_armor(70), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqhelmet_202","Full helmet", [("helmet_20", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_covers_head, 0,780, weight(4)|abundance(10)|head_armor(70), imodbits_armor|imodbit_cracked, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqgreat_helmet_new","Full helmet", [("great_helmet_new", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_covers_head, 0,780, weight(4)|abundance(10)|head_armor(70), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqosp_greathelm_b","Great helmet", [("osp_greathelm_b", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_covers_head, 0,780, weight(3.5)|abundance(10)|head_armor(70), imodbits_armor|imodbit_cracked, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqosp_greathelm_a","Heaume", [("osp_greathelm_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_covers_head, 0,780, weight(4)|abundance(20)|head_armor(70), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqmail_coif_new","Coif", [("mail_coif_new", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,250, weight(2)|abundance(10)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqflattop_helmet_new","Helmet", [("flattop_helmet_new", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,250, weight(2)|abundance(10)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqosp_kettle_hat_b","Kettle_hat", [("osp_kettle_hat_b", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,260, weight(2)|abundance(20)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qqprato_chapel_de_fer","Kettle_hat", [("prato_chapel-de-fer", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,250, weight(2)|abundance(10)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqmaciejowski_kettle","Kettle_hat", [("maciejowski_kettle", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,280, weight(2.5)|abundance(10)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qqmaciejowskihelm","Full helmet", [("maciejowskihelm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_covers_head, 0,780, weight(4)|abundance(30)|head_armor(70), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["iber_combed_morion","Morion", [("combed_morion", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,350, weight(2)|abundance(10)|head_armor(60), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["iber_combed_morion_blued","Morion", [("combed_morion_blued", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,350, weight(2)|abundance(10)|head_armor(60), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["iber_chapel_de_fer","Chapel", [("chapel-de-fer", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,350, weight(2)|abundance(10)|head_armor(60), imodbits_armor|imodbit_cracked, [], [fac_kingdom_23,fac_kingdom_25]],
  ["wwmoorish_helmet_b","Helmet", [("moorish_helmet_b", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,300, weight(2)|abundance(20)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwmoorish_helmet_c","Helmet", [("moorish_helmet_c", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,300, weight(2)|abundance(20)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwmoorish_helmet_a","Helmet", [("moorish_helmet_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,300, weight(2)|abundance(20)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["wwmoorish_helmet_d","Helmet", [("moorish_helmet_d", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,300, weight(2)|abundance(20)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["cc_mgj_early_douao","Douao", [("mgj_early_douao", 0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0,310, weight(2)|abundance(90)|head_armor(30), imodbits_cloth, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["rr_lplume_helm1","Helmet", [("lplume_helm1", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,720, weight(2.75)|abundance(40)|head_armor(45), imodbits_armor|imodbit_cracked, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rr_boeotiangreek","Helmet", [("boeotiangreek", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,720, weight(2.75)|abundance(40)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rr_samniteattic","Helmet", [("Samniteattic", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,720, weight(2.75)|abundance(40)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["mmkhergit_lady_hat","Lady's hat", [("khergit_lady_hat", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(90)|head_armor(10), imodbits_cloth, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["cc_swj_doua2","Helmet", [("swj_doua2", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,360, weight(2.5)|abundance(80)|head_armor(50)|difficulty(3), imodbits_armor|imodbit_cracked, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["cc_suannidou","Suannidou", [("suannidou", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,155, weight(1.5)|abundance(80)|head_armor(35)|difficulty(3), imodbits_armor|imodbit_cracked, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qqinv_litchina_helm","Litchina", [("inv_litchina_helm", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,780, weight(3)|abundance(10)|head_armor(70), imodbits_armor|imodbit_cracked, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["han_g_head2_2br","Scale_helmet", [("Han_g_head2_2br", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,580, weight(2)|abundance(60)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_1]],
  ["han_g_head2_2yb","Scale_helmet", [("Han_g_head2_2yb", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,580, weight(2)|abundance(60)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_1]],
  ["han_g_head2_2","Scale_helmet", [("Han_g_head2_2", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,580, weight(2)|abundance(60)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_1]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jjshadow_mask","Shadow_mask", [("shadow_mask", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,400, weight(2)|abundance(20)|head_armor(25), imodbits_armor|imodbit_cracked, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["mmkhergit_lady_hat_b","Ladie's_hat", [("khergit_lady_hat_b", 0)], itp_type_head_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,110, weight(1)|abundance(90)|head_armor(10), imodbits_cloth, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["han_g_head2_2bu","Scale_helmet", [("Han_g_head2_2bu", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,580, weight(2)|abundance(60)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_1]],
  ["skin_helmet","Skin helmet", [("skin_helmet", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,400, weight(2)|abundance(20)|head_armor(45), imodbits_armor|imodbit_cracked, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["conical_helmet_steppe","Conical helmet", [("conical_helmet_steppe", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,400, weight(2)|abundance(20)|head_armor(55), imodbits_armor|imodbit_cracked, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["wwarab_helmet","Helmet", [("rabati_new", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,200, weight(2)|abundance(20)|head_armor(45), imodbits_armor|imodbit_cracked, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["rrroman_helm_copper","Helmet", [("roman_helm_copper", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,180, weight(2)|abundance(60)|head_armor(45), imodbits_armor|imodbit_cracked, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["headless_neck","Headless_neck", [("headless_neck", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,180, weight(2)|abundance(100)|head_armor(25), imodbits_armor|imodbit_cracked, []],
  ["wooden_stick","Wooden_stick", [("wooden_stick", 0)], itp_type_one_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_secondary, itc_scimitar,2, weight(2)|abundance(100)|hit_points(16384)|spd_rtng(82)|weapon_length(80)|thrust_damage(0, pierce)|swing_damage(16, blunt), imodbits_none, []],
  ["club","Club", [("club", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_secondary|itp_can_knock_down, itc_scimitar,20, weight(1.5)|abundance(100)|difficulty(4)|hit_points(17408)|spd_rtng(80)|weapon_length(65)|thrust_damage(15, pierce)|swing_damage(22, blunt), imodbits_none, []],
  ["maul_b","Maul", [("maul_b", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_secondary|itp_can_knock_down, itc_scimitar,20, weight(1.5)|abundance(100)|difficulty(4)|hit_points(17408)|spd_rtng(75)|weapon_length(67)|thrust_damage(0, pierce)|swing_damage(36, blunt), imodbits_none, []],
  ["maul_c","Maul", [("maul_c", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_secondary|itp_can_knock_down, itc_scimitar,20, weight(1.5)|abundance(100)|difficulty(4)|hit_points(17408)|spd_rtng(75)|weapon_length(67)|thrust_damage(0, pierce)|swing_damage(36, blunt), imodbits_none, []],
  ["maul_d","Maul", [("maul_d", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_secondary|itp_can_knock_down, itc_scimitar,20, weight(1.5)|abundance(100)|difficulty(4)|hit_points(17408)|spd_rtng(72)|weapon_length(65)|thrust_damage(0, pierce)|swing_damage(39, blunt), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["spiked_club","Spiked_Club", [("spiked_club", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_can_knock_down, itcf_carry_mace_left_hip|itc_scimitar,130, weight(3)|abundance(100)|hit_points(22528)|spd_rtng(77)|weapon_length(85)|thrust_damage(15, pierce)|swing_damage(22, pierce), imodbits_none, []],
  ["sickle","Sickle", [("sickle", 0)], itp_type_one_handed_wpn| itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itc_cleaver,100, weight(1.5)|abundance(100)|hit_points(15360)|spd_rtng(86)|weapon_length(40)|thrust_damage(15, pierce)|swing_damage(15, cut), imodbits_none, []],
  ["knife","Knife", [("peasant_knife", 0)], itp_type_one_handed_wpn| itp_no_parry|itp_merchandise|itp_primary|itp_secondary, itcf_carry_dagger_front_left|itc_dagger,105, weight(0.5)|abundance(100)|hit_points(16384)|spd_rtng(97)|weapon_length(30)|thrust_damage(16, pierce)|swing_damage(16, cut), imodbits_sword, []],
  ["butchering_knife","Butchering_knife", [("khyber_knife", 0)], itp_type_one_handed_wpn| itp_no_parry|itp_primary|itp_secondary, itcf_carry_dagger_front_right|itc_dagger,85, weight(0.75)|abundance(100)|hit_points(19456)|spd_rtng(82)|weapon_length(40)|thrust_damage(9, pierce)|swing_damage(19, cut), imodbits_sword, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["khergit_pike_cc","Pudao", [("khergit_pike_cc", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_can_knock_down, itcf_carry_sword_back|itc_nodachi|itcf_thrust_twohanded,600, weight(2.25)|abundance(100)|difficulty(15)|hit_points(62464)|spd_rtng(87)|weapon_length(121)|thrust_damage(31, pierce)|swing_damage(52, cut), imodbits_polearm, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["inca_h_spear","Spear", [("h_spear", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,370, weight(3)|abundance(100)|difficulty(8)|hit_points(15360)|spd_rtng(84)|weapon_length(133)|thrust_damage(31, pierce)|swing_damage(28, cut), imodbits_polearm, [], [fac_kingdom_21,fac_kingdom_22,fac_kingdom_32,fac_kingdom_33,fac_kingdom_46]],
  ["cc_long_axe_a","Long axe", [("long_axe_a", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_can_knock_down, itcf_carry_spear|itc_nodachi|itcf_thrust_twohanded,400, weight(2.25)|abundance(100)|difficulty(15)|hit_points(62464)|spd_rtng(84)|weapon_length(107)|thrust_damage(31, pierce)|swing_damage(52, cut), imodbits_polearm, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["cc_crecent_long","Crecent", [("khergit_pike_l", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_horseback_overswing_right_onehanded|itcf_horseback_overswing_left_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance|itcf_horseback_slash_polearm,680, weight(3)|abundance(100)|difficulty(18)|hit_points(40960)|spd_rtng(74)|weapon_length(185)|thrust_damage(44, pierce)|swing_damage(38, cut), imodbits_polearm, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["rr_spear1","Spear", [("spear1", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,440, weight(1.25)|abundance(90)|difficulty(4)|hit_points(15360)|spd_rtng(79)|weapon_length(161)|thrust_damage(35, pierce)|swing_damage(28, cut), imodbits_polearm, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["qqfalchion","Falchion", [("falchion_new", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar,200, weight(1.25)|abundance(100)|difficulty(8)|hit_points(41984)|spd_rtng(86)|weapon_length(71)|thrust_damage(22, pierce)|swing_damage(36, cut), imodbits_sword, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["cc_osp_guofengwuqi01a","Jian", [("osp_guofengwuqi01a", 0),("osp_guofengwuqi01b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,580, weight(1)|abundance(100)|difficulty(6)|hit_points(30720)|spd_rtng(86)|weapon_length(114)|thrust_damage(34, pierce)|swing_damage(38, cut), imodbits_sword, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["cc_mongol_heavy_sword","Mongolians_heavy_sword", [("mongol_heavy_sword", 0),("khergit_sword_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar|itcf_show_holster_when_drawn,532, weight(1.5)|abundance(100)|hit_points(43008)|spd_rtng(84)|weapon_length(117)|thrust_damage(22, pierce)|swing_damage(47, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_21,fac_kingdom_22,fac_kingdom_30]],
  ["cc_yitiansword_twohand","Jian", [("yitiansword_01", 0),("yitiansword_01_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_left_hip|itc_longsword|itcf_thrust_twohanded|itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_show_holster_when_drawn|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded,710, weight(1.25)|abundance(100)|difficulty(11)|hit_points(36864)|spd_rtng(88)|weapon_length(122)|thrust_damage(33, pierce)|swing_damage(49, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["cc_khergit_pike_l","Daolong", [("khergit_pike_l", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_unbalanced, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance|itcf_horseback_slash_polearm,600, weight(2.25)|abundance(100)|difficulty(15)|hit_points(62464)|spd_rtng(76)|weapon_length(175)|thrust_damage(31, pierce)|swing_damage(52, cut), imodbits_polearm, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["cc_khergit_pike_b","Crecent", [("khergit_pike_b", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_can_knock_down, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance|itcf_horseback_slash_polearm,600, weight(2.25)|abundance(100)|difficulty(15)|hit_points(62464)|spd_rtng(82)|weapon_length(130)|thrust_damage(31, pierce)|swing_damage(52, cut), imodbits_polearm, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["jjmonohoshi","Monohoshi", [("monohoshi", 0),("monohoshi_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_unique|itp_two_handed|itp_primary, itcf_carry_sword_back|itc_nodachi|itcf_thrust_twohanded|itcf_show_holster_when_drawn,22040, weight(1.25)|abundance(100)|difficulty(18)|hit_points(36864)|spd_rtng(79)|weapon_length(172)|thrust_damage(38, pierce)|swing_damage(56, cut), imodbit_masterwork, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["english_longsword","Longsword", [("english_longsword", 0),("english_longsword_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,667, weight(1.5)|abundance(50)|difficulty(8)|hit_points(36864)|spd_rtng(84)|weapon_length(100)|thrust_damage(22, pierce)|swing_damage(40, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
    ["longsword_b","Longsword", [("longsword_b", 0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,636, weight(1.75)|abundance(50)|difficulty(11)|hit_points(44032)|spd_rtng(85)|weapon_length(103)|thrust_damage(35, pierce)|swing_damage(52, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  #["longsword_b","longsword_b", [("longsword_b", 0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_can_knock_down, itcf_carry_sword_left_hip|itc_nodachi|itcf_thrust_twohanded|itcf_show_holster_when_drawn,636, weight(1.75)|abundance(50)|difficulty(11)|hit_points(44032)|spd_rtng(85)|weapon_length(103)|thrust_damage(35, pierce)|swing_damage(52, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["irish_sword","Sword", [("irish_sword", 0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,667, weight(1.5)|abundance(50)|difficulty(8)|hit_points(36864)|spd_rtng(82)|weapon_length(105)|thrust_damage(22, pierce)|swing_damage(40, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["italian_sword","Sword", [("italian_sword", 0),("italian_sword_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,676, weight(1.75)|abundance(50)|difficulty(11)|hit_points(45056)|spd_rtng(85)|weapon_length(97)|thrust_damage(25, pierce)|swing_damage(52, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["crusader_sword","Crusaders sword", [("crusader_sword", 0),("crusader_sword_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,667, weight(1.5)|abundance(50)|difficulty(8)|hit_points(36864)|spd_rtng(84)|weapon_length(97)|thrust_damage(22, pierce)|swing_damage(40, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["milanese_sword","Sword", [("milanese_sword", 0),("milanese_sword_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,660, weight(1.25)|abundance(50)|difficulty(8)|hit_points(25600)|spd_rtng(84)|weapon_length(76)|thrust_damage(34, pierce)|swing_damage(37, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["ch_khergit_pike_l_uniq1","Crecent", [("khergit_pike_l", 0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance,600, weight(2.25)|abundance(100)|difficulty(15)|hit_points(32464)|spd_rtng(93)|weapon_length(185)|thrust_damage(46, pierce)|swing_damage(66, cut), imodbit_masterwork, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["morglay_uniq1","Morgelai", [("morglay", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_sword_back|itc_nodachi,2040, weight(100)|abundance(100)|difficulty(65)|hit_points(36864)|spd_rtng(74)|weapon_length(168)|thrust_damage(0, pierce)|swing_damage(50, blunt), imodbit_masterwork, []],
  ["godenak","Godenak", [("mackie_godenak", 0),("mackie_godenak", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar,400, weight(0.75)|abundance(100)|difficulty(2)|hit_points(20480)|spd_rtng(82)|weapon_length(109)|swing_damage(41, cut), imodbits_sword, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jjkatana","Katana", [("katana", 0),("katana_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_left_hip|itc_longsword|itcf_thrust_twohanded|itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_show_holster_when_drawn|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded,700, weight(1.25)|abundance(100)|difficulty(11)|hit_points(36864)|spd_rtng(87)|weapon_length(95)|thrust_damage(27, pierce)|swing_damage(58, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["jjkatana_a","Katana", [("katana_a", 0),("katana_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,700, weight(1.25)|abundance(100)|difficulty(11)|hit_points(38912)|spd_rtng(88)|weapon_length(89)|thrust_damage(31, pierce)|swing_damage(47, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_33]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jjno_dachi","Nodachi", [("no_dachi", 0),("no_dachi_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_left_hip|itc_nodachi|itcf_thrust_twohanded|itcf_show_holster_when_drawn,840, weight(1.25)|abundance(100)|difficulty(18)|hit_points(36864)|spd_rtng(83)|weapon_length(130)|thrust_damage(27, pierce)|swing_damage(52, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qqgerman_bastard_sword","Bastard_sword", [("german_bastard_sword", 0),("german_bastard_sword_scabbard", ixmesh_carry),("german_bastard_sword", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,709, weight(1.75)|abundance(30)|difficulty(9)|hit_points(43008)|spd_rtng(84)|weapon_length(105)|thrust_damage(32, pierce)|swing_damage(44, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqandalusian_sword","Andalusian_sword", [("andalusian_sword", 0),("andalusian_sword_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,410, weight(1.5)|abundance(100)|hit_points(30720)|spd_rtng(86)|weapon_length(95)|thrust_damage(30, pierce)|swing_damage(38, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["qqarabian_sword_c","Arabian_sword", [("arabian_sword_c", 0),("scab_arabian_sword_c", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,444, weight(1.75)|abundance(100)|hit_points(39936)|spd_rtng(85)|weapon_length(105)|thrust_damage(30, pierce)|swing_damage(40, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["qqglaive1","Glaive", [("glaive1", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,572, weight(2.75)|abundance(100)|difficulty(15)|hit_points(53248)|spd_rtng(77)|weapon_length(147)|thrust_damage(32, pierce)|swing_damage(53, cut), imodbits_polearm, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["han_katana_new_small","Hwando", [("katana_new_small", 0),("Katana_New_small_scabb", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,440, weight(1.25)|abundance(100)|difficulty(8)|hit_points(34816)|spd_rtng(90)|weapon_length(72)|thrust_damage(38, pierce)|swing_damage(43, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_1]],
  ["qqscimitar","Scimitar", [("scimitar_a", 0),("scab_scimeter_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar|itcf_show_holster_when_drawn,755, weight(1.5)|abundance(100)|hit_points(41984)|spd_rtng(87)|weapon_length(97)|thrust_damage(22, pierce)|swing_damage(43, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["qqscimitar_b","Elite_scimitar", [("scimitar_b", 0),("scab_scimeter_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar|itcf_show_holster_when_drawn,823, weight(1.75)|abundance(100)|hit_points(43008)|spd_rtng(87)|weapon_length(100)|thrust_damage(22, pierce)|swing_damage(46, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["rrgladius_pompeii","Gladius", [("gladius_pompeii", 0),("roman_gladius_2_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_longsword,380, weight(0.75)|abundance(100)|difficulty(2)|hit_points(20480)|spd_rtng(88)|weapon_length(66)|thrust_damage(45, pierce)|swing_damage(42, cut), imodbits_sword, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrgladius_mainz","Gladius", [("gladius_mainz", 0),("roman_gladius_1_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_longsword,380, weight(0.75)|abundance(100)|difficulty(2)|hit_points(22528)|spd_rtng(88)|weapon_length(67)|thrust_damage(45, pierce)|swing_damage(42, cut), imodbits_sword, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["qqtwo_handed_cleaver","War_Cleaver", [("military_cleaver_a", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_back|itc_nodachi,674, weight(2)|abundance(100)|difficulty(15)|hit_points(41024)|spd_rtng(82)|weapon_length(120)|swing_damage(59, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqsword_khergit_3","Sabre", [("khergit_sword_a", 0),("khergit_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar|itcf_show_holster_when_drawn,349, weight(1.5)|abundance(100)|hit_points(41984)|spd_rtng(85)|weapon_length(87)|thrust_damage(22, pierce)|swing_damage(44, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_21,fac_kingdom_22,fac_kingdom_30]],
  ["qqsword_khergit_4","Heavy_Sabre", [("khergit_sword_d", 0),("khergit_sword_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar|itcf_show_holster_when_drawn,432, weight(1.5)|abundance(100)|hit_points(43008)|spd_rtng(84)|weapon_length(88)|thrust_damage(22, pierce)|swing_damage(47, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_21,fac_kingdom_22,fac_kingdom_30]],
  ["khergit_pike_dd","Meijiandao", [("khergit_pike_dd", 0),("khergit_pike_dd", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar,480, weight(1)|abundance(100)|difficulty(8)|hit_points(30720)|spd_rtng(86)|weapon_length(88)|thrust_damage(22, pierce)|swing_damage(44, cut), imodbits_sword, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["cc_china_sword_long","Jian", [("china_sword_long", 0),("china_sword_long_scabb", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,580, weight(1)|abundance(100)|difficulty(6)|hit_points(30720)|spd_rtng(86)|weapon_length(105)|thrust_damage(34, pierce)|swing_damage(38, cut), imodbits_sword, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["inca_h_axe_long","Stone_axe", [("h_axe_long", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance|itcf_horseback_slash_polearm,300, weight(2.25)|abundance(100)|difficulty(15)|hit_points(62464)|spd_rtng(88)|weapon_length(95)|thrust_damage(31, pierce)|swing_damage(52, cut), imodbits_polearm, [], [fac_kingdom_45]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["muramasa_uniq1","Muramasa", [("mackie_nodachi", 0),("no_dachi_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_left_hip|itc_nodachi|itcf_thrust_twohanded|itcf_show_holster_when_drawn,2040, weight(1.25)|abundance(100)|difficulty(18)|hit_points(36864)|spd_rtng(90)|weapon_length(130)|thrust_damage(43, pierce)|swing_damage(65, cut), imodbit_masterwork, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["nuryo_uniq1","Nuryo", [("Katana_BIG_New_tex", 0),("Katana_BIG_New_scabb", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_left_hip|itc_longsword|itcf_thrust_twohanded|itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_show_holster_when_drawn|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded,700, weight(1.25)|abundance(100)|difficulty(11)|hit_points(36864)|spd_rtng(90)|weapon_length(130)|thrust_damage(27, pierce)|swing_damage(67, cut), imodbits_sword|imodbit_masterwork, []],
  ["hh_jikdo","Jikdo", [("katana_long", 0),("katana_long_scabb", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_left_hip|itc_longsword|itcf_thrust_twohanded|itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_show_holster_when_drawn|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded,500, weight(1.25)|abundance(100)|difficulty(11)|hit_points(36864)|spd_rtng(87)|weapon_length(91)|thrust_damage(27, pierce)|swing_damage(49, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_1]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["hwanse_uniq1","Hwanse", [("huanshou_b", 0),("huanshou_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword,480, weight(1)|abundance(100)|difficulty(8)|hit_points(30720)|spd_rtng(93)|weapon_length(123)|thrust_damage(35, pierce)|swing_damage(42, cut), imodbits_sword, []],
  ["jihad_uniq1","Jihad", [("pa_sword_02", 0),("pa_sword_02_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itcf_carry_sword_left_hip|itc_scimitar|itcf_show_holster_when_drawn,5123, weight(1.75)|abundance(100)|hit_points(7472)|spd_rtng(89)|weapon_length(108)|thrust_damage(22, pierce)|swing_damage(54, cut), imodbit_masterwork, []],
  ["rrakinakes_uniq1","Ea", [("dirk", 0),("dirk_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_crush_through, itcf_carry_sword_left_hip|itc_longsword,222, weight(0.75)|abundance(100)|hit_points(30480)|spd_rtng(95)|weapon_length(45)|thrust_damage(70, pierce)|swing_damage(40, cut), imodbit_masterwork, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["vorpal_s_uniq1","Vorpal_sword", [("vorpal_s", 0),("vorpal_s", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_sword_back|itc_nodachi,22040, weight(1.25)|abundance(100)|difficulty(18)|hit_points(36864)|spd_rtng(92)|weapon_length(131)|swing_damage(70, cut), imodbit_masterwork, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qqwinged_mace_3","Winged_mace", [("winged_mace_3", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,464, weight(1.75)|abundance(30)|difficulty(8)|hit_points(27648)|spd_rtng(84)|weapon_length(75)|thrust_damage(22, cut)|swing_damage(35, blunt), imodbits_axe|imodbit_balanced, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["gae_bolga_melee_uniq1","Gae_Bolga", [("new_xueqiang", 0)], itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,2222, weight(3)|abundance(100)|difficulty(65)|hit_points(37168)|spd_rtng(92)|weapon_length(150)|thrust_damage(45, pierce)|swing_damage(45, pierce), imodbit_balanced, []],
  ["alexander_spear_uniq1","Alexander_spear", [("arabian_spear_a_3m", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_can_knock_down, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,1495, weight(3.25)|abundance(100)|difficulty(65)|hit_points(16384)|spd_rtng(90)|weapon_length(197)|thrust_damage(55, pierce)|swing_damage(65, cut), imodbits_polearm, []],
  ["cc_huanshoudao","Huanshoudao", [("huanshoudao", 0),("scab_huanshou", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,480, weight(1)|abundance(100)|difficulty(6)|hit_points(30720)|spd_rtng(86)|weapon_length(118)|thrust_damage(34, pierce)|swing_damage(38, cut), imodbits_sword, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["han_kanabo_b","Pyeongon", [("han_blunt", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_can_knock_down, itcf_carry_mace_left_hip|itc_scimitar,488, weight(3)|abundance(100)|hit_points(22528)|spd_rtng(75)|weapon_length(110)|swing_damage(26, pierce), imodbits_none, [], [fac_kingdom_1]],
  ["khergit_pike_b_uniq","Green_dragon_crecent", [("khergit_pike_b", 0)], itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itcf_horseback_slash_polearm,3000, weight(5.5)|abundance(100)|difficulty(30)|hit_points(43008)|spd_rtng(92)|weapon_length(131)|thrust_damage(44, pierce)|swing_damage(67, cut), imodbit_masterwork, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jjwakizashi","Wakizashi", [("wakizashi", 0),("wakizashi_scabbard", ixmesh_carry)], itp_type_one_handed_wpn| itp_no_parry|itp_merchandise|itp_primary|itp_secondary, itcf_carry_dagger_front_right|itc_dagger|itcf_show_holster_when_drawn,280, weight(0.5)|abundance(100)|hit_points(17408)|spd_rtng(93)|weapon_length(72)|thrust_damage(28, pierce)|swing_damage(33, cut), imodbits_sword, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["qqbattle_axe_c","Battle_Axe", [("one_handed_battle_axe_c", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_axe_back|itc_nodachi,570, weight(3)|abundance(100)|difficulty(11)|hit_points(47104)|spd_rtng(73)|weapon_length(85)|thrust_damage(0, pierce)|swing_damage(50, pierce), imodbits_axe, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["bianfu","Bianfu", [("china_blunt", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,319, weight(1.5)|abundance(2)|difficulty(8)|hit_points(30720)|spd_rtng(85)|weapon_length(80)|thrust_damage(21, pierce)|swing_damage(31, blunt), imodbits_axe|imodbit_balanced, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["great_scimitar","Great_scimitar", [("great_scimitar", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_back|itc_nodachi,674, weight(2)|abundance(100)|difficulty(15)|hit_points(41024)|spd_rtng(84)|weapon_length(114)|swing_damage(59, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["hongzi_uniq1","Hongzi", [("Katana_New", 0),("Katana_New_scabb", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_left_hip|itc_longsword|itcf_thrust_twohanded|itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_show_holster_when_drawn|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded,5005, weight(1.25)|abundance(100)|difficulty(11)|hit_points(36864)|spd_rtng(88)|weapon_length(100)|thrust_damage(27, pierce)|swing_damage(62, cut), imodbits_sword|imodbit_masterwork, []],
  ["kanesada_uniq1","Kanesada", [("xiaoyewan_s", 0),("xiaoyewan_s_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_left_hip|itc_nodachi|itcf_thrust_twohanded|itcf_show_holster_when_drawn,5005, weight(1.25)|abundance(100)|difficulty(11)|hit_points(36864)|spd_rtng(87)|weapon_length(105)|thrust_damage(27, pierce)|swing_damage(66, cut), imodbits_sword|imodbit_masterwork, []],
  ["tonbogiri_uniq1","Tonbogiri", [("tonbogiri", 0)], itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_can_knock_down, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,5555, weight(1.25)|abundance(100)|difficulty(4)|hit_points(15360)|spd_rtng(84)|weapon_length(189)|thrust_damage(45, pierce)|swing_damage(45, cut), imodbits_polearm, []],
  ["ch_jumonji_yari_l","Ji", [("jumonji_yari_l", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,480, weight(3)|abundance(100)|difficulty(18)|hit_points(40960)|spd_rtng(73)|weapon_length(178)|thrust_damage(42, pierce)|swing_damage(44, cut), imodbits_polearm, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["snake_spear","Snake_spear", [("gallic_spear_4", 0)], itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance|itcf_horseback_slash_polearm,3000, weight(5.5)|abundance(100)|difficulty(15)|hit_points(43008)|spd_rtng(87)|weapon_length(187)|thrust_damage(55, pierce)|swing_damage(55, cut), imodbit_masterwork, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["haiiro_uniq1","Haiiro", [("katana_new_2", 0),("katana_new_2_scabb", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_left_hip|itc_longsword|itcf_thrust_twohanded|itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_show_holster_when_drawn|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded,5005, weight(1.25)|abundance(100)|difficulty(11)|hit_points(36864)|spd_rtng(90)|weapon_length(100)|thrust_damage(27, pierce)|swing_damage(62, cut), imodbits_sword|imodbit_masterwork, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jug_criss_1","Criss", [("criss_1", 0),("criss_1", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,867, weight(1.5)|abundance(50)|difficulty(8)|hit_points(36864)|spd_rtng(88)|weapon_length(70)|thrust_damage(40, pierce)|swing_damage(40, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_27,fac_kingdom_33]],
  ["azt_mackie_basehuitl","Maquahuitl", [("mackie_basehuitl", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_spear|itc_nodachi,319, weight(1.5)|abundance(2)|difficulty(8)|hit_points(30720)|spd_rtng(85)|weapon_length(94)|thrust_damage(22, pierce)|swing_damage(48, blunt), imodbits_axe|imodbit_balanced, [], [fac_kingdom_46]],
  ["yitianjian_uniq1","Yitianjian", [("yuchang_jian_2", 0),("yuchang_jianku_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_dagger,580, weight(1)|abundance(100)|difficulty(6)|hit_points(30720)|spd_rtng(89)|weapon_length(95)|thrust_damage(45, pierce)|swing_damage(45, pierce), imodbits_sword, []],
  ["qqmorningstar_3","Morningstar", [("morningstar_3", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced, itcf_carry_axe_left_hip|itc_nodachi|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded,443, weight(2)|abundance(100)|difficulty(8)|hit_points(31744)|spd_rtng(82)|weapon_length(75)|thrust_damage(22, pierce)|swing_damage(30, pierce), imodbits_axe, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqluc_warhammer_s_v1","Warhammer", [("luc_warhammer_s_v1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,319, weight(1.5)|abundance(2)|difficulty(8)|hit_points(30720)|spd_rtng(85)|weapon_length(69)|thrust_damage(22, pierce)|swing_damage(35, blunt), imodbits_axe|imodbit_balanced, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqmorningstar_2","Morningstar", [("morningstar_2", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_unbalanced, itcf_carry_axe_left_hip|itc_nodachi|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded,443, weight(2)|abundance(100)|difficulty(8)|hit_points(31744)|spd_rtng(82)|weapon_length(75)|thrust_damage(22, pierce)|swing_damage(30, pierce), imodbits_axe, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["shaver_uniq1","Shaver", [("mackie_celtic_axe", 0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_bonus_against_shield, itcf_carry_axe_back|itc_scimitar,2000, weight(4)|abundance(100)|difficulty(18)|hit_points(51200)|spd_rtng(82)|weapon_length(100)|thrust_damage(0, pierce)|swing_damage(41, pierce), imodbits_axe, []],
  ["excalibur_stone_uniq1","Excalibur", [("mackie_bastard", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_sword_back|itc_nodachi,50000, weight(20)|abundance(100)|hit_points(31744)|spd_rtng(81)|weapon_length(107)|swing_damage(30, blunt), imodbits_none, [
    (ti_on_weapon_attack, [
      (store_trigger_param_1, ":var0"),
      (call_script, "script_molda_excalibur_seal", ":var0"),
    ]),
   ]],
  ["executioner_uniq1","Executioner", [("mackie_bearded_axe", 0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_parry_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance|itcf_horseback_slash_polearm,5555, weight(2.25)|abundance(100)|difficulty(15)|hit_points(62464)|spd_rtng(83)|weapon_length(135)|thrust_damage(31, pierce)|swing_damage(72, cut), imodbits_polearm, []],
  ["wolven_gladius_uniq1","Wolven_Gladius", [("WolvenGladius", 0),("WolvenGladius", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword,9999, weight(0.75)|abundance(100)|difficulty(2)|hit_points(20480)|spd_rtng(96)|weapon_length(70)|thrust_damage(55, pierce)|swing_damage(55, cut), imodbits_sword, []],
  ["archangel_uniq1","Archangel", [("pa_sword_04", 0),("pa_sword_04_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_back|itc_nodachi|itcf_thrust_twohanded,9999, weight(0.75)|abundance(100)|difficulty(2)|hit_points(20480)|spd_rtng(89)|weapon_length(145)|thrust_damage(38, pierce)|swing_damage(69, cut), imodbits_sword, []],
  ["hhlong_axe_a","Axe_long", [("long_axe_a", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_axe_back|itc_nodachi,570, weight(3)|abundance(100)|difficulty(18)|hit_points(47104)|spd_rtng(69)|weapon_length(110)|thrust_damage(0, pierce)|swing_damage(50, pierce), imodbits_axe, []],
  ["cursed_falcata_uniq1","Cursed_falcata", [("mackie_falcata01", 0),("mackie_falcata01", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword,9999, weight(0.75)|abundance(100)|difficulty(2)|hit_points(20480)|spd_rtng(93)|weapon_length(88)|thrust_damage(35, pierce)|swing_damage(57, cut), imodbits_sword, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["bardiche","Bardiche", [("bardiche", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_can_knock_down, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance|itcf_horseback_slash_polearm,600, weight(2.25)|abundance(100)|difficulty(15)|hit_points(62464)|spd_rtng(83)|weapon_length(130)|thrust_damage(31, pierce)|swing_damage(52, cut), imodbits_polearm, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["war_pick","War_pickaxe", [("xeno_war_pick01", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar,461, weight(2)|abundance(100)|difficulty(9)|hit_points(32768)|spd_rtng(80)|weapon_length(76)|thrust_damage(22, pierce)|swing_damage(32, pierce), imodbits_axe, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["double_axe","Double_axe", [("mackie_double_axe", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar,461, weight(2)|abundance(100)|difficulty(9)|hit_points(32768)|spd_rtng(78)|weapon_length(74)|thrust_damage(22, pierce)|swing_damage(34, pierce), imodbits_axe, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["kriegsmesser","Kriegsmesser", [("mackie_kriegsmesser", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_sword_back|itc_greatsword|itcf_horseback_thrust_onehanded,2200, weight(3)|abundance(10)|difficulty(15)|hit_points(31744)|spd_rtng(81)|weapon_length(140)|thrust_damage(31, pierce)|swing_damage(58, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_11]],
  ["mangler_uniq1","Mangler", [("mackie_mangler", 0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_unbalanced|itp_can_knock_down, itcf_carry_spear|itc_cut_two_handed|itc_parry_polearm|itcf_thrust_twohanded|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,440, weight(1.25)|abundance(100)|difficulty(4)|hit_points(15360)|spd_rtng(79)|weapon_length(196)|thrust_damage(40, pierce)|swing_damage(46, cut), imodbits_polearm, []],
  ["qqmorning_star_long","Morningstar", [("mackie_morning_star_long", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_can_knock_down, itc_nodachi|itcf_thrust_twohanded,643, weight(2)|abundance(100)|difficulty(8)|hit_points(31744)|spd_rtng(82)|weapon_length(135)|thrust_damage(27, pierce)|swing_damage(36, pierce), imodbits_axe, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["swordcane_blade_uniq1","Nekhbet", [("mackie_swordcane_blade", 0),("mackie_swordcane_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,580, weight(1)|abundance(100)|hit_points(30720)|spd_rtng(95)|weapon_length(80)|thrust_damage(44, pierce)|swing_damage(44, cut), imodbits_sword, []],
  ["pendulum_uniq1","Pendulum", [("mackie_pendulum", 0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itcf_horseback_slash_polearm,600, weight(2.25)|abundance(100)|difficulty(15)|hit_points(62464)|spd_rtng(83)|weapon_length(180)|thrust_damage(65, cut)|swing_damage(52, cut), imodbits_polearm, []],
  ["excalibur_uniq1","Excalibur", [("mackie_bastard_ori", 0),("scab_mackie_bastard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,50000, weight(2)|abundance(100)|hit_points(30720)|spd_rtng(89)|weapon_length(80)|thrust_damage(45, pierce)|swing_damage(45, pierce), imodbits_none, []],
  ["yuchang_jian_2_uniq1","Qinghongjian", [("yuchang_jian_2", 0),("yuchang_jianku_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword,580, weight(1)|abundance(100)|difficulty(6)|hit_points(30720)|spd_rtng(90)|weapon_length(95)|thrust_damage(37, pierce)|swing_damage(37, pierce), imodbits_sword, []],
  ["shiva_blade_uniq1","Shiva_blade", [("war_concept_may09_04_01_2", 0),("war_concept_may09_04_01_scabbard_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_crush_through, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,100000, weight(1.5)|abundance(100)|hit_points(43008)|spd_rtng(92)|weapon_length(118)|thrust_damage(38, pierce)|swing_damage(32, pierce), imodbits_none, []],
  ["sun_blade_uniq1","Sun_blade", [("war_concept_may09_03_03", 0),("war_concept_may09_03_03_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_secondary|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_sword_back|itc_nodachi|itcf_thrust_twohanded,22580, weight(1)|abundance(100)|hit_points(30720)|spd_rtng(87)|weapon_length(133)|thrust_damage(41, pierce)|swing_damage(69, cut), imodbits_sword, []],
  ["hashashin_blade","Sister_killer", [("war_concept_may09_04_01_2", 0),("war_concept_may09_04_01_scabbard_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,100000, weight(1.5)|abundance(100)|hit_points(43008)|spd_rtng(83)|weapon_length(118)|thrust_damage(32, pierce)|swing_damage(35, cut), imodbits_none, []],
  ["first_axe_uniq1","Crusader's axe", [("first_axe", 0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_bonus_against_shield, itcf_carry_axe_back|itc_scimitar,2000, weight(4)|abundance(100)|difficulty(18)|hit_points(51200)|spd_rtng(93)|weapon_length(91)|thrust_damage(0, pierce)|swing_damage(45, pierce), imodbits_axe, []],
  ["northwind_uniq1","Northwind", [("pa_sword_05", 0),("pa_sword_05_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_back|itc_nodachi|itcf_thrust_twohanded,9999, weight(0.75)|abundance(100)|difficulty(2)|hit_points(20480)|spd_rtng(87)|weapon_length(156)|thrust_damage(38, pierce)|swing_damage(69, cut), imodbits_sword, []],
  ["crystal_sword_uniq1","Crystal_sword", [("gallic_sword_1", 0),("gallic_sword_scabbard_1", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword,9999, weight(0.75)|abundance(100)|difficulty(2)|hit_points(20480)|spd_rtng(88)|weapon_length(108)|thrust_damage(38, pierce)|swing_damage(55, cut), imodbits_sword, []],
  ["holyknight_sword_uniq1","Holy knights_sword", [("pa_sword_03", 0),("pa_sword_03_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_back|itc_nodachi|itcf_thrust_twohanded,9999, weight(0.75)|abundance(100)|difficulty(2)|hit_points(20480)|spd_rtng(89)|weapon_length(143)|thrust_damage(60, pierce)|swing_damage(55, cut), imodbits_sword, []],
  ["staff","Staff", [("wooden_staff", 0)], itp_type_polearm|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itcf_carry_sword_back|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,70, weight(1.5)|abundance(100)|hit_points(18432)|spd_rtng(90)|weapon_length(140)|thrust_damage(16, blunt)|swing_damage(18, blunt), imodbits_polearm, []],
  ["quarter_staff","Short_Staff", [("quarter_staff", 0)], itp_type_polearm|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itcf_carry_sword_back|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,90, weight(2)|abundance(100)|hit_points(18432)|spd_rtng(90)|weapon_length(130)|thrust_damage(17, blunt)|swing_damage(25, blunt), imodbits_polearm, []],
  ["iron_staff","Iron staff", [("iron_staff", 0)], itp_type_polearm|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itcf_carry_sword_back|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,190, weight(2)|abundance(100)|hit_points(19456)|spd_rtng(87)|weapon_length(125)|thrust_damage(10, blunt)|swing_damage(19, blunt), imodbits_polearm, []],
  ["pitch_fork","Pitch_Fork", [("pitch_fork", 0)], itp_type_polearm|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itcf_carry_sword_back|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance_horseback,60, weight(3.5)|abundance(100)|hit_points(17408)|spd_rtng(70)|weapon_length(154)|thrust_damage(14, pierce)|swing_damage(17, blunt), imodbit_bent, []],
  ["battle_fork","Battle_fork", [("battle_fork", 0)], itp_type_polearm|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itcf_carry_sword_back|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,70, weight(3.5)|abundance(100)|hit_points(18432)|spd_rtng(70)|weapon_length(143)|thrust_damage(15, pierce)|swing_damage(18, blunt), imodbit_bent, []],
  ["qqgallic_spear_3","Spear", [("gallic_spear_3", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,320, weight(4)|abundance(80)|difficulty(4)|hit_points(16384)|spd_rtng(79)|weapon_length(150)|thrust_damage(31, pierce)|swing_damage(27, cut), imodbits_polearm, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["qqspear_i_2_3m","Spear", [("spear_i_2-3m", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_spear|itc_parry_polearm|itcf_thrust_polearm|itcf_overswing_polearm|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,440, weight(1.25)|abundance(90)|difficulty(4)|hit_points(15360)|spd_rtng(78)|weapon_length(157)|thrust_damage(32, pierce)|swing_damage(27, cut), imodbits_polearm, []],
  ["bamboo_lance","Bamboo_spear", [("bamboo_lance", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_spear|itc_parry_polearm|itcf_thrust_polearm|itcf_overswing_polearm|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,160, weight(1.5)|abundance(90)|difficulty(4)|hit_points(15360)|spd_rtng(81)|weapon_length(160)|thrust_damage(25, pierce)|swing_damage(17, blunt), imodbits_polearm, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["rrmacedoniansarissa","Sarissa", [("macedoniansarissa", 0)], itp_type_polearm| itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_cant_use_on_horseback|itp_unbalanced, itcf_carry_spear|itc_parry_polearm|itcf_thrust_polearm|itcf_overswing_polearm|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,480, weight(4.5)|abundance(60)|difficulty(17)|hit_points(5360)|spd_rtng(67)|weapon_length(400)|thrust_damage(37, pierce)|swing_damage(31, cut), imodbits_polearm, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrpike_22","Spear", [("pike_2", 0)], itp_type_polearm| itp_no_parry|itp_merchandise|itp_wooden_parry|itp_primary|itp_unbalanced, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,495, weight(3.25)|abundance(40)|difficulty(27)|hit_points(16384)|spd_rtng(70)|weapon_length(290)|thrust_damage(35, pierce)|swing_damage(31, cut), imodbits_polearm, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["qqhasta","Hasta", [("hasta", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itc_parry_polearm|itcf_thrust_polearm|itcf_overswing_polearm|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,310, weight(3)|abundance(100)|difficulty(8)|hit_points(14336)|spd_rtng(74)|weapon_length(182)|thrust_damage(30, pierce)|swing_damage(26, cut), imodbits_polearm, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["ch_crecent_long2","Crecent", [("khergit_pike_l", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_horseback_overswing_right_onehanded|itcf_horseback_overswing_left_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance|itcf_horseback_slash_polearm,380, weight(3)|abundance(100)|difficulty(18)|hit_points(40960)|spd_rtng(73)|weapon_length(183)|thrust_damage(35, pierce)|swing_damage(44, cut), imodbits_polearm, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["arabian_spear_a_3m_cc","Spear", [("arabian_spear_a_3m", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itc_parry_polearm|itcf_thrust_polearm|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,270, weight(3)|abundance(100)|difficulty(8)|hit_points(15360)|spd_rtng(72)|weapon_length(200)|thrust_damage(31, pierce)|swing_damage(28, cut), imodbits_polearm, [], [fac_kingdom_46,fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29,fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qqheavy_lance","Charge_lance", [("heavy_lance", 0)], itp_type_polearm| itp_no_parry|itp_merchandise|itp_primary|itp_offset_lance|itp_covers_head|itp_unbalanced, itc_pike|itcf_horseback_thrust_onehanded,1120, weight(5)|abundance(20)|difficulty(30)|hit_points(35000)|spd_rtng(67)|weapon_length(250)|thrust_damage(45, pierce), imodbit_cracked|imodbit_bent, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqlance_4","Charge_lance", [("lance_4", 0)], itp_type_polearm| itp_no_parry|itp_merchandise|itp_primary|itp_offset_lance|itp_covers_head|itp_unbalanced, itc_pike|itcf_horseback_thrust_onehanded,1320, weight(5)|abundance(20)|difficulty(30)|hit_points(35900)|spd_rtng(67)|weapon_length(255)|thrust_damage(43, pierce), imodbit_cracked|imodbit_bent, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqlance_3","Charge_lance", [("lance_3", 0)], itp_type_polearm| itp_no_parry|itp_primary|itp_offset_lance|itp_covers_head|itp_unbalanced, itcf_carry_spear|itc_pike|itcf_horseback_thrust_onehanded,1900, weight(2)|abundance(100)|difficulty(50)|hit_points(35000)|spd_rtng(59)|weapon_length(325)|thrust_damage(45, pierce), imodbits_polearm, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["wwspear_f_2_9m","Lance", [("spear_f_2-9m", 0)], itp_type_polearm| itp_no_parry|itp_merchandise|itp_primary|itp_offset_lance|itp_covers_head|itp_unbalanced, itc_pike|itcf_horseback_thrust_onehanded,680, weight(2.75)|abundance(100)|difficulty(12)|hit_points(30240)|spd_rtng(75)|weapon_length(180)|thrust_damage(42, pierce), imodbits_polearm, []],
  ["snake_spear_uniq1","Snake_spear", [("gallic_spear_4", 0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance|itp_can_knock_down, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,5555, weight(2.5)|abundance(100)|difficulty(8)|hit_points(15360)|spd_rtng(84)|weapon_length(185)|thrust_damage(40, pierce)|swing_damage(40, cut), imodbits_polearm, []],
  ["qqspear_e_3_25m","Two_handed_spear", [("spear_e_3-25m", 0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,300, weight(4)|abundance(100)|difficulty(30)|hit_points(25000)|spd_rtng(65)|weapon_length(230)|thrust_damage(35, pierce)|swing_damage(35, cut), imodbits_polearm, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqspear_e_2_5m","Blade_spear", [("spear_e_2-5m", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,380, weight(3)|abundance(100)|difficulty(15)|hit_points(40960)|spd_rtng(85)|weapon_length(150)|thrust_damage(33, pierce)|swing_damage(35, cut), imodbits_polearm, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqspear_g_short","Short_spear", [("spear_g_short", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_sword_left_hip|itc_parry_onehanded|itcf_thrust_onehanded|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded,360, weight(0.5)|abundance(100)|hit_points(12288)|spd_rtng(90)|weapon_length(92)|thrust_damage(33, pierce)|swing_damage(22, cut), imodbits_polearm, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["highlad_broadsword","Broadsword", [("highlad_broadsword", 0),("highlad_broadsword_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,700, weight(1.75)|abundance(5)|difficulty(5)|hit_points(32768)|spd_rtng(85)|weapon_length(105)|thrust_damage(35, pierce)|swing_damage(44, cut), imodbits_sword, [], [fac_kingdom_23,fac_kingdom_25]],
  ["espada_eslavona_b","Espada eslavona", [("espada_eslavona_b", 0),("espada_eslavona_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_penalty_with_shield, itcf_carry_sword_left_hip|itc_parry_onehanded|itcf_thrust_onehanded|itcf_horseback_thrust_onehanded|itcf_show_holster_when_drawn,750, weight(0.75)|abundance(5)|spd_rtng(88)|weapon_length(100)|thrust_damage(44, pierce)|swing_damage(0, pierce), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_23,fac_kingdom_25]],
  ["cchafted_blade_b","Hafted_Blade", [("khergit_pike_b", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_can_knock_down, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance|itcf_horseback_slash_polearm,600, weight(2.25)|abundance(100)|difficulty(15)|hit_points(62464)|spd_rtng(83)|weapon_length(130)|thrust_damage(31, pierce)|swing_damage(52, cut), imodbits_polearm, [], [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["cchafted_blade_a","Hafted_Blade", [("khergit_pike_a", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_can_knock_down, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance|itcf_horseback_slash_polearm,600, weight(2.75)|abundance(100)|difficulty(15)|hit_points(8192)|spd_rtng(81)|weapon_length(153)|thrust_damage(31, pierce)|swing_damage(52, cut), imodbits_polearm, [], [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["wwele_spear","Elephant_spear", [("pike_2", 0)], itp_type_polearm| itp_no_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_unbalanced, itcf_carry_spear|itcf_thrust_polearm|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_thrust_onehanded_lance|itcf_horseback_slash_polearm,668, weight(2.75)|abundance(100)|difficulty(35)|hit_points(8192)|spd_rtng(55)|weapon_length(300)|thrust_damage(27, pierce)|swing_damage(65, cut), imodbits_polearm, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["amer_h_spear2","Spear", [("h_spear", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,270, weight(3)|abundance(100)|difficulty(8)|hit_points(15360)|spd_rtng(84)|weapon_length(133)|thrust_damage(31, pierce)|swing_damage(29, cut), imodbits_polearm, [], [fac_kingdom_50]],
  ["banner_spear_2","Banner_spear", [("banner_spear_2", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,360, weight(2.5)|abundance(100)|hit_points(17408)|spd_rtng(75)|weapon_length(205)|thrust_damage(39, pierce)|swing_damage(30, cut), imodbit_balanced, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_banner_spear", ":var0", ":var1"),
    ]),
   ]],
  ["spear_of_xiangshan_uniq1","Spear_of_Xiangshan", [("gallic_spear_2_uniq", 0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,5555, weight(2.5)|abundance(100)|difficulty(8)|hit_points(15360)|spd_rtng(84)|weapon_length(190)|thrust_damage(40, pierce)|swing_damage(40, cut), imodbit_balanced, []],
  ["mackie_nagamaki","Nagamaki", [("mackie_nagamaki", 0),("mackie_nagamaki", ixmesh_carry)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_penalty_with_shield|itp_offset_lance, itcf_carry_sword_back|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance|itcf_show_holster_when_drawn,535, weight(3)|abundance(100)|difficulty(15)|hit_points(43008)|spd_rtng(82)|weapon_length(122)|thrust_damage(31, pierce)|swing_damage(52, cut), imodbits_polearm, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["impaler_uniq1","Impaler", [("lance_6", 0)], itp_type_polearm| itp_no_parry|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_covers_head|itp_unbalanced|itp_can_knock_down, itc_pike|itcf_horseback_thrust_onehanded,5555, weight(5)|abundance(100)|difficulty(30)|hit_points(35900)|spd_rtng(77)|weapon_length(255)|thrust_damage(55, pierce), imodbit_cracked|imodbit_bent, []],
  ["azt_mackie_basehuitl_onehand","Maquahuitl", [("mackie_basehuitl_onehand", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary, itcf_carry_mace_left_hip|itc_scimitar,319, weight(1.5)|abundance(2)|difficulty(8)|hit_points(30720)|spd_rtng(85)|weapon_length(73)|thrust_damage(22, pierce)|swing_damage(35, blunt), imodbits_axe|imodbit_balanced, [], [fac_kingdom_46]],
  ["uhtc","Ultra_high_temperature_cutter", [("uhtc", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itcf_carry_sword_back|itc_greatsword|itcf_horseback_thrust_onehanded,1, weight(2.25)|abundance(100)|difficulty(15)|hit_points(62464)|spd_rtng(87)|weapon_length(147)|thrust_damage(45, pierce)|swing_damage(45, pierce), imodbits_none, []],
  ["wave_uniq1","Wave", [("pa_sword_07", 0),("pa_sword_07_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_scimitar|itcf_show_holster_when_drawn,9999, weight(1.5)|abundance(10)|hit_points(43008)|spd_rtng(89)|weapon_length(106)|thrust_damage(32, pierce)|swing_damage(52, cut), imodbit_masterwork, [], [fac_kingdom_21,fac_kingdom_22,fac_kingdom_30]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["hhsain_high_uniq1","Sain", [("two_handed_katana", 0),("two_handed_katana_scabb", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,9999, weight(1.25)|abundance(10)|difficulty(18)|hit_points(36864)|spd_rtng(87)|weapon_length(130)|thrust_damage(42, pierce)|swing_damage(66, cut), imodbit_masterwork, [], [fac_kingdom_1]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["personalbanner","Banner", [("tableau_flag_itm", 0)], itp_type_two_handed_wpn| itp_no_parry|itp_two_handed|itp_primary, itcf_carry_spear|itcf_overswing_twohanded|itcf_horseback_overswing_right_onehanded|itcf_horseback_overswing_left_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded,180, weight(2)|abundance(100)|hit_points(18432)|spd_rtng(55)|weapon_length(300)|thrust_damage(0, pierce)|swing_damage(27, cut), imodbits_none, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_flag_itm", ":var0", ":var1"),
    ]),
   ]],
  ["rrroman_shield_velite","Velite_shield", [("roman_shield_velite", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(10)|difficulty(1)|hit_points(370)|spd_rtng(55)|shield_width(70), imodbits_shield, [#####Begin add effect to shields	
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		[fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrafricanskirm2","Leather shield", [("africanskirm2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,340, weight(4)|abundance(100)|body_armor(7)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(60), imodbits_shield, 
  
#####Begin add effect to shields	
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		[fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["afri_nguni_shield","Leather shield", [("nguni_shield", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,340, weight(4)|abundance(100)|body_armor(7)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(60), imodbits_shield, 
  
#####Begin add effect to shields	
	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields 
[fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["lyre","Lyre", [("lyre", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_next_item_as_melee, itcf_carry_bow_back,218, weight(2.5)|abundance(100)|body_armor(1)|hit_points(100)|spd_rtng(82)|shield_width(90), imodbits_none, []],
  ["lute","Lute", [("lute", 0)], itp_type_shield|itp_wooden_parry|itp_next_item_as_melee, itcf_carry_bow_back,218, weight(2.5)|abundance(100)|body_armor(1)|hit_points(100)|spd_rtng(82)|shield_width(90), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["tab_shield_pavise_d","Pavise shield", [("tableau_shield_pavise_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield,400, weight(5)|abundance(100)|body_armor(14)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(100)|shield_width(43), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		
		#####End add effect to shields
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["tab_shield_pavise_c","Pavise shield", [("tableau_shield_pavise_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield,400, weight(4.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(100)|shield_width(43), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		#####End add effect to shields
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["tab_shield_pavise_b","Pavise shield", [("tableau_shield_pavise_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield,400, weight(4)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(100)|shield_width(43), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":var0", ":var1"),
 #####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["tab_shield_pavise_a","Pavise shield", [("tableau_shield_pavise_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield,400, weight(3.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(100)|shield_width(43), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["tab_shield_heater_cav_b","Heater shield", [("tableau_shield_heater_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,300, weight(2.5)|abundance(100)|body_armor(23)|difficulty(2)|hit_points(550)|spd_rtng(65)|shield_height(50)|shield_width(30), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["tab_shield_heater_cav_a","Heater shield", [("tableau_shield_heater_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,300, weight(2)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(65)|shield_height(50)|shield_width(30), imodbits_shield, [
  #Possible shield mesh bug above nativeshield_heater_cav was shield_heater_cav
  
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["tab_shield_heater_d","Heater shield", [("tableau_shield_heater_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,300, weight(3.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(70)|shield_width(36), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["tab_shield_round_a","Round shield", [("tableau_shield_round_3", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(3)|abundance(100)|body_armor(8)|difficulty(1)|hit_points(370)|spd_rtng(55)|shield_width(65), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":var0", ":var1"),
 #####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["tab_shield_round_b","Round shield", [("tableau_shield_round_3", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(3)|abundance(100)|body_armor(8)|difficulty(1)|hit_points(370)|spd_rtng(55)|shield_width(65), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["tab_shield_round_c","Round shield", [("tableau_shield_round_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(8)|difficulty(1)|hit_points(370)|spd_rtng(55)|shield_width(65), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_round_shield_2", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["tab_shield_round_d","Round shield", [("tableau_shield_round_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4)|abundance(100)|body_armor(8)|difficulty(1)|hit_points(370)|spd_rtng(55)|shield_width(65), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["tab_shield_round_e","Round shield", [("tableau_shield_round_4", 0)], itp_type_shield|itp_merchandise, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(8)|difficulty(1)|hit_points(370)|spd_rtng(55)|shield_width(65), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["tab_shield_small_round_a","Small round shield", [("tableau_shield_small_round_3", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(2)|abundance(100)|body_armor(10)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(40), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["tab_shield_small_round_b","Small round shield", [("tableau_shield_small_round_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(2.5)|abundance(100)|body_armor(10)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(40), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["tab_shield_small_round_c","Small round shield", [("tableau_shield_small_round_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(2.5)|abundance(100)|body_armor(10)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(60), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["han_shield_2","Shield", [("shield_round_222", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_width(70), imodbits_shield, 
  [
  (ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		[fac_kingdom_1]],
		
		
		
		
		
  ["han_shield_5","Shield", [("shield_round_111", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_1]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["rrsnakehoplon","Shield", [("snakehoplon", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_width(70), imodbits_shield, 	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["ccdal_hindum","Shield", [("dal_hindum", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(100)|shield_width(50), imodbits_shield, [	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["ccluc_cavalry_shield_z","Shield", [("luc_cavalry_shield_z", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(110)|shield_width(50), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43,fac_kingdom_62]],
  ["ccdal_hindul","Shield", [("dal_hindul", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(100)|shield_width(50), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29]],
  ["rrspartan_shield","Shield", [("spartan_shield", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrspartanhoplon","Shield", [("spartanhoplon", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		
		
		
		
		
		 [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["ccdal_wicker","Nomad shield", [("dal_wicker", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,340, weight(4)|abundance(100)|body_armor(7)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(60), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_21,fac_kingdom_22,fac_kingdom_30]],
  ["ccdal_hinduk","Nomad shield", [("dal_hinduk", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,340, weight(4)|abundance(100)|body_armor(7)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(60), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_21,fac_kingdom_22,fac_kingdom_30]],
  ["jjwooden_bari","Shield", [("wooden_bari", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(100)|shield_width(50), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["ddbrass_shield","Eastern_shield", [("brass_shield", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,340, weight(4)|abundance(100)|body_armor(7)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(60), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["ddbrass_shield1","Eastern_shield", [("brass_shield1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,340, weight(4)|abundance(100)|body_armor(7)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(60), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["ddbrass_shield2","Eastern_shield", [("brass_shield2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,340, weight(4)|abundance(100)|body_armor(7)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(60), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["ddbrass_shield3","Eastern_shield", [("brass_shield3", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,340, weight(4)|abundance(100)|body_armor(7)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(60), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["ddbrass_shield7","Eastern_shield", [("brass_shield7", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,340, weight(4)|abundance(100)|body_armor(7)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(60), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["azt_africanskirm1","Shield", [("africanskirm1", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,340, weight(4)|abundance(100)|body_armor(7)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(60), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_46]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jug_shield_pavisei","Pavise shield", [("shield_pavisei", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,400, weight(4.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(100)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_27,fac_kingdom_33]],
  ["easternskirmshield1","Wooden shield", [("easternskirmshield1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,400, weight(4.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(100)|shield_width(70), imodbits_shield, 	[(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		],
		
		
		
		
		
  ["ad_viking_shield_round_02","Round shield", [("ad_viking_shield_round_02", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		
		
		
		
		
		
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["ad_viking_shield_round_03","Round shield", [("ad_viking_shield_round_03", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["ad_viking_shield_round_04","Round shield", [("ad_viking_shield_round_04", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["ad_viking_shield_round_10","Round shield", [("ad_viking_shield_round_10", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["ad_viking_shield_round_08","Round shield", [("ad_viking_shield_round_08", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["ad_viking_shield_round_15","Round shield", [("ad_viking_shield_round_15", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["iber_steel_buckler2","Buckler", [("steel_buckler2", 0)], itp_type_shield|itp_wooden_parry, 0,340, weight(4)|abundance(100)|body_armor(7)|difficulty(1)|hit_points(550)|spd_rtng(60)|shield_width(60), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_23,fac_kingdom_25]],
  ["ad_viking_shield_round_07","Round shield", [("ad_viking_shield_round_07", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["per_dal_hinduh","Shield", [("dal_hinduh", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,400, weight(4.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(100)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_9]],
  ["per_dal_hindua","Shield", [("dal_hindua", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,200, weight(4.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(100)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_9]],
  ["inca_dal_hinduj","Shield", [("dal_hinduj", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,240, weight(4)|abundance(100)|body_armor(7)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(60), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_45]],
  ["rr_mecedon_shield_3","Shield", [("mecedon_shield_3", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(9)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["rrroman_shield_cav_2","Shield", [("roman_shield_cav_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(87)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrroman_shield_early","Shield", [("roman_shield_early", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,300, weight(4.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(100)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrroman_shield_oval","Oval shield", [("roman_shield_oval", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,400, weight(4.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(70)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrroman_shield_round","Round shield", [("roman_shield_round", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,400, weight(4.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrroman_shield_square","Square shield", [("roman_shield_square", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,400, weight(4.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(100)|shield_width(70), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["jug_dal_turkiv","Shield", [("dal_turkiv", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,340, weight(4)|abundance(100)|body_armor(7)|difficulty(1)|hit_points(370)|spd_rtng(60)|shield_width(60), imodbits_shield, [(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
		
		(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),

		
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		
		
		
		
		 [fac_kingdom_27,fac_kingdom_33]],
  ["tab_shield_kite_a","Kite shield", [("tableau_shield_kite_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,400, weight(2)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(70)|shield_width(36), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_kite_shield_1", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["tab_shield_kite_b","Kite shield", [("tableau_shield_kite_3", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,400, weight(2.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(70)|shield_width(36), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_kite_shield_3", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["tab_shield_kite_c","Kite shield", [("tableau_shield_kite_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,400, weight(3)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(70)|shield_width(36), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["tab_shield_kite_d","Kite shield", [("tableau_shield_kite_2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,400, weight(3.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(70)|shield_width(36), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["tab_shield_kite_cav_a","Kite shield", [("tableau_shield_kite_4", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,400, weight(2)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(70)|shield_height(50)|shield_width(30), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["tab_shield_kite_cav_b","Kite shield", [("tableau_shield_kite_4", 0)], itp_type_shield|itp_merchandise, itcf_carry_kite_shield,400, weight(2.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(70)|shield_height(50)|shield_width(30), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["tab_shield_heater_a","Heater shield", [("tableau_shield_heater_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,300, weight(2)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(70)|shield_width(36), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["tab_shield_heater_b","Heater shield", [("tableau_shield_heater_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,300, weight(2.5)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(70)|shield_width(36), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["tab_shield_heater_c","Heater shield", [("tableau_shield_heater_1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,700, weight(3)|abundance(100)|body_armor(10)|difficulty(2)|hit_points(550)|spd_rtng(55)|shield_height(70)|shield_width(36), imodbits_shield, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":var0", ":var1"),
#####Begin add effect to shields for tableau
#old: 		])],
#old:	],	
		]),
	(ti_on_shield_hit,
		[
		(store_trigger_param_1, ":trigger_param_1"),
		#(agent_get_scale, pos1, ":trigger_param_1", 13),
        (agent_get_position, pos1, ":trigger_param_1"), #Get Agent Position
		#Extend to include horsemen
		(agent_get_horse, ":rider", ":trigger_param_1"), #Get agent who is riding a horse.
		#Not needed
		#(agent_get_scale, pos1, ":trigger_param_1", 13), #Bugged, thus horses will have issues.
	    #(position_transform_position_to_parent, pos3, pos2, pos1),
		
		(try_begin),
		(eq, ":rider", -1), #If agent is NOT on a horse
       (position_move_z, pos1, 120), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS NOT ON A HORSE!"),
	   
	   (else_try), #If agent is a rider
	   (position_move_z, pos1, 188), #Up/Down
       (position_move_x, 3, 10), #Left/Right
       (position_move_y, pos1, 30), #Forward/Back 10 def
	   #(display_message, "@DEBUG: AGENT IS ON A HORSE!"),
		(try_end),
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_lanse_blood"), #We use this instead if we want dummy_straw_big to have a chance.
		#Not needed
		#(store_random_in_range, ":psys_to_use", "psys_lanse", "psys_dummy_straw_big"), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		#(store_random_in_range, ":random_effect_in_range", 1, 2), #Randomize smoke size between  3 to 6, for props this is set to 3.
		#(particle_system_burst, "psys_dummy_smoke", pos1, ":random_effect_in_range"), #We want smoke randomized sizes.
		#Good
		#(particle_system_burst, "psys_dummy_smoke", pos1, 1), #We want smoke randomized sizes.
		#(particle_system_burst, "psys_dummy_straw", pos1, 3), #We don't want randomized partifle effects for shields.
		#Good
		#(particle_system_burst, ":psys_to_use", pos1, 2), #We want particle effects randomized for the actual shield.
				(store_random_in_range, ":smoke_chance", 0, 8), #We probably don't want to include dummy_straw_big, so we ignore it in this one
		(try_begin),
		(eq, ":smoke_chance", 1), #If agent is NOT on a horse
		(particle_system_burst, "psys_dummy_smoke", pos1, 1), #Smoke size
		(try_end),
		(particle_system_burst, "psys_dummy_straw", pos1, 3), #Particle effect size for wood
		###Other options###
		#(particle_system_burst, "psys_dummy_straw", pos1, ":random_effect_in_range"), #We want particle effects randomized for the actual shield.
		#(particle_system_burst, "psys_lanse", pos1, 10),
        #(particle_system_burst, "psys_lanse_straw", pos1, 30)
		###Other Options###
		])],
		

		#####End add effect to shields
		 [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["end_of_africa","End_of_Africa", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["buddha_statues_made_of_stone_underground","Buddha_statues_made_of_stone_underground", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["triangular_building","Triangular_building", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["temple_of_many_columns","Temple_of_many_columns", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["tower_tilted","Tower_tilted", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["murder_stadium","Murder_stadium", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["cathedral_of_the_western_end","Cathedral_of_the_western_end", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["temple_of_the_sun_god","Temple_of_the_sun_god", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["herd_of_stone","Herd_of_stone", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["temple_of_thebes","Temple_of_Thebes", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_boundaries_of_china","The_boundaries_of_China", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["minotaur","Minotaur", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["city_covered_in_volcanic_ash","City_covered_in_volcanic_ash", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["floating_island","Floating_Island", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["rules_of_stone","Rules_of_stone", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_silk_sky","The_Silk_sky", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_monk","The_Monk", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["sad_story_of_the_hunchback","Sad_story_of_the_hunchback", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["palace_of_the_last","Palace_of_the_last", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["golden_capital","Golden_Capital", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_chimera","The_Chimera", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["huge_cliff","Huge_cliff", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["building_of_people_to_make_a_calendar","Building_of_people_to_make_a_calendar", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["i_dont_like_pepsi","I_dont_like_Pepsi", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["long_live_the_golden","Long_live_the_Golden", [("book_open", 0)], itp_type_book, 0,5000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_pikachu","The_Pikachu", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["temple_of_bleeding","Temple_of_bleeding", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_tunnel_man","The_Tunnel_Man", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_blue_gate","The_Blue_Gate", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["encore_encore_what","Encore_encore_what", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["castle_of_princess","Castle_of_Princess", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["stone_buddha","Stone_Buddha", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["king_of_immortality","King_of_immortality", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_big_head","The_Big_Head", [("book_open", 0)], itp_type_book|itp_merchandise, 0,6000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_forgotten_king","The_Forgotten_King", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["huge_building_made_of_mud","Huge_building_made_of_mud", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["temple_of_desert","Temple_of_desert", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["pinwheel_tower","Pinwheel_tower", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["record_of_ptolemy","Record_of_Ptolemy", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["great_africa","great_Africa", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["rainbow_falls","Rainbow_Falls", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["dragon_island","Dragon_island", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["forgotten_palace","Forgotten_Palace", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["greece_square","Greece_Square", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["legend_of_the_lake_monster","Legend_of_the_lake_monster", [("book_open", 0)], itp_type_book, 0,5000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["stairway_to_heaven","Stairway_to_Heaven", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["giant_buddha","Giant_Buddha", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["temple_of_gold","Temple_of_gold", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["castle_of_high_base","Castle_of_high_base", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["bowl_isle","Bowl_isle", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["tomb_of_the_north","Tomb_of_the_North", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_north_end_of_greece","The_north_end_of_Greece", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["temple_of_useless","Temple_of_useless", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["yellow_tower","Yellow_Tower", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_buddha_of_carved_into_cliff","The_Buddha_of_carved_into_cliff", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_natural_wonder","The_Natural_wonder", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["ultra_large_buddha","Ultra_large_buddha", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["white_cliffs_of_buddha","White_Cliffs_of_Buddha", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["black_and_white_bear","Black_and_white_bear", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["dongle_dongle_building","Dongle_dongle_building", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["created_many_of_fucking_dolmen_fucking_ancestor","created_many_of_fucking_dolmen_fucking_ancestor", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["simple_temple","Simple_temple", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["useless_building","Useless_building", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["nomad_valley","Nomad_Valley", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["nomad_lake","Nomad_Lake", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["ryukyu","Ryukyu", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["sacred_mountain","Sacred_Mountain", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["tripitaka_koreana","Tripitaka_Koreana", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["india_fort","India_Fort", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["mossy_temple","Mossy_temple", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["ancient_city_on_the_rock","Ancient_City_on_the_Rock", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["buddhist_town","Buddhist_Town", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["invisible_cave","Invisible_cave", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["group_of_monuments","Group_of_Monuments", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["marvelous_temple","Marvelous_temple", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["black_pagoda","Black_Pagoda", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["reef","reef", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["subterranean_river","Subterranean_River", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["java_temple","Java_Temple", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["buddha_in_the_wood","Buddha_in_the_wood", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["opak_river_temple","Opak_River_Temple", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["da_nang_sanctuary","Da_Nang_Sanctuary", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["great_reef","great_reef", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["bungle_bungle_range","Bungle_Bungle_Range", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["shark_bay","Shark_Bay", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_stone_color_changes","The_Stone_color_changes", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["blue_mountain","Blue_Mountain", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["hammad_recode","Hammad_recode", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["oasis_town","Oasis_Town", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["city_of_nile","City_of_Nile", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_destruction_of_rome","The_destruction_of_Rome", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["traces_of_roman","Traces_of_Roman", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["rome_in_africa","Rome_in_Africa", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["forgotten_roman_city","Forgotten_Roman_city", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["another_triangle","Another_triangle", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["glory_of_rome","Glory_of_Rome", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["africa_fort","Africa_Fort", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["cave_paintings","Cave_paintings", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["leopard_in_the_mountains","Leopard_in_the_mountains", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["desert_city","Desert_city", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["askia_muhammad","Askia_muhammad", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["religious_and_spiritual_significance","Religious_and_spiritual_significance", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_largest_impact_crater_on_earth","the_largest_impact_crater_on_Earth", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["lakes_of_desert","Lakes_of_Desert", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["city_of_perished","City_of_Perished", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["ancient_city","Ancient_City", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["sand_fort","Sand_Fort", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["citadel_on_the_silk_road","Citadel_on_the_Silk_Road", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["persian_inscription","Persian_Inscription", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["neolithic_age","Neolithic_age", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["rock_art","Rock_Art", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["sharp_tower","Sharp_Tower", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["stone_ancient_city","Stone_ancient_city", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["dragon_tree","Dragon_tree", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["city_of_sacrifice","City_of_sacrifice", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["city_of_black_stone","City_of_black_stone", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["cut_surface_of_the_sky","Cut_surface_of_the_sky", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["ever_green_hills","Ever_green_hills", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["forgotten_civilization","Forgotten_Civilization", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_3000_year_old_temple","The_3000_year_old_Temple", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["pictures_of_primitive_humanity","Pictures_of_primitive_humanity", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["stone_of_sacrifice","Stone_of_Sacrifice", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["ice_palace","Ice_Palace", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_ground_pattern_of_the_unknown","The_ground_pattern_of_the_unknown", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["obsidian_city","Obsidian_City", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["traces_of_an_unknown_civilization","Traces_of_an_unknown_civilization", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["hypogea","Hypogea", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["traces_of_humanity","Traces_of_Humanity", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["fort_isle","Fort_isle", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_oldest_civilization_in_the_new_land","The_oldest_civilization_in_the_new_land", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["razor_mountains","Razor_Mountains", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["secluded_island","Secluded_island", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_glacier","The_Glacier", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["ash_covered_town","Ash_covered_town", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["viking_church","Viking_Church", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["star_fort","Star_Fort", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["rune_stone","Rune_Stone", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["hamlet_castle","Hamlet_castle", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["silkroad","Silkroad", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["petroglyph_in_the_semirechye","Petroglyph_in_the_Semirechye", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["parthian_fortresses","Parthian_Fortresses", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_blue_roof","The_Blue_Roof", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_thousand_spear","The_Thousand_spear", [("book_open", 0)], itp_type_book|itp_merchandise, 0,2000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["golden_mountains","Golden_Mountains", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["iron_meteorite","Iron_meteorite", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1000, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["sand_curtain","Sand_Curtain", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["crusades","Crusades", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_fall_of_joseon","The_Fall_of_Joseon", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["alexander_biography","alexander_Biography", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["zhou_yu_biography","Zhou_Yu_Biography", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_fall_of_yuan_shao","The_Fall_of_Yuan_Shao", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["tokugawa_ieyasu_biography","Tokugawa_Ieyasu_Biography", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["yi_sun_sin_biography","Yi_Sun_sin_Biography", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["three_hundred","Three_hundred", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["hannibal_barca_biography","hannibal_Barca_Biography", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["xiang_yu_biography","xiang_Yu_Biography", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["marcus_licinius_crassus_biography","Marcus_Licinius_Crassus_Biography", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["themistocles_biography","Themistocles_Biography", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["darius_biography","Darius_Biography", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["gaius_julius_caesar_biography","Gaius_Julius_Caesar_Biography", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["marcus_vipsanius_agrippa_biography","Marcus_Vipsanius_Agrippa_Biography", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_hadrianopolis","The_Hadrianopolis", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["salsu","Salsu", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["islamic_war","Islamic_War", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["mongol_invader","Mongol_Invader", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["seljuk_empire","Seljuk_Empire", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_fall_of_liu_bei","The_Fall_of_Liu_Bei", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_huns","The_Huns", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_first_war","The_First_War", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["the_west_march","The_West_march", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["bai_qi_biography","Bai_Qi_Biography", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["important_letter","Important_letter", [("linen", 0)], itp_type_book, 0,1, weight(0.5)|abundance(100), imodbits_none, []],
  ["liquor_qst","Liquor", [("ale_barrel", 0)], itp_type_goods, 0,1, weight(500)|abundance(100), imodbits_none, []],
  ["oil_bottle","Greek_fire_bomb", [("gourd_stand", 0)], itp_type_thrown|itp_unique|itp_primary|itp_secondary|itp_covers_legs|itp_doesnt_cover_hair|itp_no_pick_up_from_ground, itcf_throw_stone,1, weight(1)|abundance(100)|spd_rtng(60)|shoot_speed(10)|weapon_length(14)|max_ammo(3)|thrust_damage(40, pierce), imodbits_none, [
    (ti_on_init_item, [
      (set_position_delta, 0, 28, 0),
      (particle_system_add_new, "psys_fire_glow_1"),
      (set_current_color, 150, 130, 70),
    ]),
   (ti_on_missile_hit, [
      (try_begin),
        (store_trigger_param_1, ":var0"),
        (copy_position, 63, 1),
        (particle_system_burst, "psys_musket_smoke", pos1, 15),
        (particle_system_burst, "psys_map_village_fire", pos1, 30),
        (play_sound_at_position, "snd_burn222", pos1),
        (store_random_in_range, ":var1", 10, 35),
        (assign, reg0, ":var1"),
        (try_for_agents, ":var2"),
          (agent_get_position, pos62, ":var2"),
          (get_distance_between_positions, ":var3", pos63, pos62),
          (try_begin),
            (lt, ":var3", 100),
            (agent_is_active, ":var2"),
            (agent_is_alive, ":var2"),
            (store_agent_hit_points, ":var4", ":var2", 1),
            (val_sub, ":var4", ":var1"),
            (try_begin),
              (lt, ":var4", 1),
              (agent_deliver_damage_to_agent, ":var0", ":var2"),
            (else_try),
              (agent_set_hit_points, ":var2", ":var4", 1),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
    ]),
   ]],
  ["test_att","itm_test_att", [("throwing_stone", 0)], itp_type_thrown|itp_primary|itp_can_knock_down, itcf_throw_stone,0, weight(1.75)|abundance(100)|hit_points(5555)|spd_rtng(100)|max_ammo(5)|thrust_damage(45, pierce)|swing_damage(45, pierce), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["175_26_leather_gloves","Leather_gloves", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,0, weight(0.25)|abundance(100)|head_armor(150)|body_armor(116)|leg_armor(150)|difficulty(175), imodbits_none, []],
  ["175_22_mail_mittens","Mail_mittens", [("mail_mittens_L", 0)], itp_type_hand_armor, 0,0, weight(1.5)|abundance(100)|head_armor(150)|body_armor(112)|leg_armor(150)|difficulty(175), imodbits_none, []],
  ["175_22_scale_gauntlets","Scale_gauntlets", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,0, weight(0.75)|abundance(100)|head_armor(150)|body_armor(112)|leg_armor(150)|difficulty(175), imodbits_none, []],
  ["175_30_lamellar_gauntlets","Lamellar_gauntlets", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,0, weight(0.75)|abundance(100)|head_armor(150)|body_armor(120)|leg_armor(150)|difficulty(175), imodbits_none, []],
  ["175_30_leather_glove_female","Female_leather_gloves", [("female_gloveL", 0)], itp_type_hand_armor, 0,0, weight(0.5)|abundance(100)|head_armor(150)|body_armor(120)|leg_armor(150)|difficulty(175), imodbits_none, []],
  ["175_26_kote_arms","Mail gloves", [("kote_arms_L", 0),("kote_arms_L", imodbit_reinforced)], itp_type_hand_armor, 0,0, weight(1)|abundance(100)|head_armor(150)|body_armor(116)|leg_armor(150)|difficulty(175), imodbits_none, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["125_26_leather_gloves","Leather gloves", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,0, weight(0.25)|abundance(100)|head_armor(130)|body_armor(86)|leg_armor(100)|difficulty(125), imodbits_none, []],
  ["125_22_mail_mittens","Mail_mittens", [("mail_mittens_L", 0)], itp_type_hand_armor, 0,0, weight(1.5)|abundance(100)|head_armor(130)|body_armor(82)|leg_armor(100)|difficulty(125), imodbits_none, []],
  ["125_22_scale_gauntlets","Scale_gauntlets", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,0, weight(0.75)|abundance(100)|head_armor(130)|body_armor(82)|leg_armor(100)|difficulty(125), imodbits_none, []],
  ["125_30_lamellar_gauntlets","Lamellar_gauntlets", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,0, weight(0.75)|abundance(100)|head_armor(130)|body_armor(90)|leg_armor(100)|difficulty(125), imodbits_none, []],
  ["125_30_leather_glove_female","Female_leather_gloves", [("female_gloveL", 0)], itp_type_hand_armor, 0,0, weight(0.5)|abundance(100)|head_armor(130)|body_armor(90)|leg_armor(100)|difficulty(125), imodbits_none, []],
  ["125_26_kote_arms","Mail_gloves", [("kote_arms_L", 0),("kote_arms_L", imodbit_reinforced)], itp_type_hand_armor, 0,0, weight(1)|abundance(100)|head_armor(130)|body_armor(86)|leg_armor(100)|difficulty(125), imodbits_none, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["1444_mail_mittens","Mail_mittens", [("mail_mittens_L", 0)], itp_type_hand_armor, 0,888, weight(1.5)|abundance(10)|head_armor(20)|body_armor(20)|leg_armor(20), imodbits_none, []],
  ["3444_leather_gloves","Leather_gloves", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,390, weight(0.25)|abundance(120)|head_armor(10)|body_armor(10)|leg_armor(10), imodbits_none, []],
  ["2444_iber_mail_gauntlets_l","Mail_gauntlets", [("mail_gauntlets_L", 0)], itp_type_hand_armor, 0,888, weight(1.5)|abundance(10)|head_armor(15)|body_armor(15)|leg_armor(15), imodbits_none, [], [fac_kingdom_23,fac_kingdom_25]],
  ["1444_iber_mail_gauntlets_l","Mail_gauntlets", [("mail_gauntlets_L", 0)], itp_type_hand_armor, 0,888, weight(1.5)|abundance(10)|head_armor(20)|body_armor(20)|leg_armor(20), imodbits_none, [], [fac_kingdom_23,fac_kingdom_25]],
  ["1444_lamellar_gauntlets","Lamellar_gauntlets", [("scale_gauntlets_a_L", 0)], itp_type_hand_armor, 0,888, weight(0.75)|abundance(100)|head_armor(20)|body_armor(20)|leg_armor(20), imodbits_none, []],
  ["2444_mail_mittens","Mail_mittens", [("mail_mittens_L", 0)], itp_type_hand_armor, 0,888, weight(1.5)|abundance(10)|head_armor(15)|body_armor(15)|leg_armor(15), imodbits_none, []],
  ["1444_steel_gauntlets_L","Steel_gauntlets", [("steel_gauntlets_L", 0)], itp_type_hand_armor, 0,2222, weight(1.5)|abundance(10)|head_armor(25)|body_armor(25)|leg_armor(25), imodbits_none, [], [fac_kingdom_23,fac_kingdom_25]],
  ["2444_lamellar_gauntlets","Lamellar_gauntlets", [("scale_gauntlets_a_L", 0)], itp_type_hand_armor, 0,777, weight(0.75)|abundance(100)|head_armor(15)|body_armor(15)|leg_armor(15), imodbits_none, []],
  ["333_26leather_gloves","Leather_gloves", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,0, weight(0.25)|abundance(100)|head_armor(60)|body_armor(36)|leg_armor(50)|difficulty(65), imodbits_none, []],
  ["333_22_mail_mittens","Mail_mittens", [("mail_mittens_L", 0)], itp_type_hand_armor, 0,0, weight(1.5)|abundance(100)|head_armor(60)|body_armor(32)|leg_armor(50)|difficulty(65), imodbits_none, []],
  ["333_22_steel_gauntlets_L","Steel_gauntlets", [("steel_gauntlets_L", 0)], itp_type_hand_armor, 0,0, weight(1.5)|abundance(100)|head_armor(60)|body_armor(32)|leg_armor(50)|difficulty(65), imodbits_none, []],
  ["333_22_scale_gauntlets","Scale_gauntlets", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,0, weight(0.75)|abundance(100)|head_armor(60)|body_armor(32)|leg_armor(50)|difficulty(65), imodbits_none, []],
  ["333_30_lamellar_gauntlets","Lamellar_gauntlets", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,0, weight(0.75)|abundance(100)|head_armor(60)|body_armor(40)|leg_armor(50)|difficulty(65), imodbits_none, []],
  ["333_30_leather_glove_female","Female leather gloves", [("female_gloveL", 0)], itp_type_hand_armor, 0,0, weight(0.5)|abundance(100)|head_armor(60)|body_armor(40)|leg_armor(50)|difficulty(65), imodbits_none, []],
  ["333_26_samurai_kote","Samurai gloves", [("kote_L", 0),("kote_L", imodbit_reinforced)], itp_type_hand_armor, 0,0, weight(1)|abundance(100)|head_armor(60)|body_armor(36)|leg_armor(50)|difficulty(65), imodbits_none, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["333_26_kote_arms","Mail gloves", [("kote_arms_L", 0),("kote_arms_L", imodbit_reinforced)], itp_type_hand_armor, 0,0, weight(1)|abundance(100)|head_armor(60)|body_armor(36)|leg_armor(50)|difficulty(65), imodbits_none, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["2444_leather_gloves","Leather gloves", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,555, weight(0.25)|abundance(120)|head_armor(15)|body_armor(15)|leg_armor(15), imodbits_none, []],
  ["1444_leather_gloves","Leather gloves", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,888, weight(0.25)|abundance(10)|head_armor(20)|body_armor(20)|leg_armor(20), imodbits_none, []],
  ["1444_kote_arms","Mail gloves", [("kote_L", 0),("kote_L", imodbit_reinforced)], itp_type_hand_armor, 0,888, weight(1)|abundance(100)|head_armor(20)|body_armor(20)|leg_armor(20), imodbits_none, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["2444_kote_arms","Mail gloves", [("kote_arms_L", 0),("kote_arms_L", imodbit_reinforced)], itp_type_hand_armor, 0,777, weight(1)|abundance(100)|head_armor(15)|body_armor(15)|leg_armor(15), imodbits_none, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["222leather_gloves","Leather gloves", [("leather_gloves_L", 0)], itp_type_hand_armor|itp_merchandise, 0,888, weight(0.25)|abundance(50)|head_armor(25)|body_armor(25)|leg_armor(25), imodbits_none, []],
  ["222mail_mittens","Mail mittens", [("mail_mittens_L", 0)], itp_type_hand_armor|itp_merchandise, 0,888, weight(1.5)|abundance(50)|head_armor(25)|body_armor(25)|leg_armor(25), imodbits_none, []],
  ["222steel_gauntlets_L","Steel gauntlets", [("steel_gauntlets_L", 0)], itp_type_hand_armor|itp_merchandise, 0,888, weight(1.5)|abundance(50)|head_armor(25)|body_armor(25)|leg_armor(25), imodbits_none, [], [fac_kingdom_23,fac_kingdom_25]],
  ["222scale_gauntlets","Scale gauntlets", [("scale_gauntlets_b_l", 0)], itp_type_hand_armor|itp_merchandise, 0,888, weight(0.75)|abundance(50)|head_armor(25)|body_armor(25)|leg_armor(25), imodbits_none, []],
  ["222lamellar_gauntlets","Lamellar_gauntlets", [("scale_gauntlets_a_L", 0)], itp_type_hand_armor|itp_merchandise, 0,888, weight(0.75)|abundance(50)|head_armor(25)|body_armor(25)|leg_armor(25), imodbits_none, []],
  ["222leather_glove_female","Female leather gloves", [("female_gloveL", 0)], itp_type_hand_armor|itp_merchandise, 0,888, weight(0.5)|abundance(50)|head_armor(25)|body_armor(25)|leg_armor(25), imodbits_none, []],
  ["222blade_kote_arms","Gloves", [("kote_L", 0),("kote_L", imodbit_reinforced)], itp_type_hand_armor|itp_merchandise, 0,888, weight(1)|abundance(50)|head_armor(25)|body_armor(25)|leg_armor(25), imodbits_none, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["222kote_arms","Gloves", [("kote_arms_L", 0),("kote_arms_L", imodbit_reinforced)], itp_type_hand_armor|itp_merchandise, 0,888, weight(1)|abundance(50)|head_armor(25)|body_armor(25)|leg_armor(25), imodbits_none, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["555_adventege_20","Leather gloves", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,1, weight(0.25)|abundance(100)|head_armor(25)|body_armor(25)|leg_armor(25), imodbits_none, []],
  ["555_adventege_30","Leather_gloves", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,1, weight(0.25)|abundance(100)|head_armor(30)|body_armor(30)|leg_armor(30), imodbits_none, []],
  ["555_adventege_40","Leather_gloves", [("leather_gloves_L", 0)], itp_type_hand_armor, 0,1, weight(0.25)|abundance(100)|head_armor(40)|body_armor(40)|leg_armor(40), imodbits_none, []],
  ["amer_h_spear","Spear", [("h_spear", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,270, weight(3)|abundance(100)|difficulty(8)|hit_points(15360)|spd_rtng(84)|weapon_length(133)|thrust_damage(31, pierce)|swing_damage(29, cut), imodbits_polearm, [], [fac_kingdom_50]],
  ["rrpike_1_iber","Pike", [("pike_1", 0)], itp_type_polearm| itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itcf_thrust_polearm|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,580, weight(2.5)|abundance(60)|difficulty(27)|hit_points(5360)|spd_rtng(55)|weapon_length(400)|thrust_damage(35, pierce), imodbits_polearm, [], [fac_kingdom_23,fac_kingdom_25]],
  ["rrpike_2_iber","Pike", [("pike_2", 0)], itp_type_polearm| itp_no_parry|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itcf_thrust_polearm|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,580, weight(2.5)|abundance(60)|difficulty(27)|hit_points(5360)|spd_rtng(66)|weapon_length(289)|thrust_damage(37, pierce), imodbits_polearm, [], [fac_kingdom_23,fac_kingdom_25]],
  ["kahratwohand_scimitar","Twohanded_scimitar", [("scimitar_a2", 0),("scab_scimeter_a2", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_left_hip|itc_nodachi|itcf_horseback_overswing_right_onehanded|itcf_horseback_overswing_left_onehanded|itcf_show_holster_when_drawn,723, weight(1.75)|abundance(20)|hit_points(43008)|spd_rtng(87)|weapon_length(123)|thrust_damage(0, pierce)|swing_damage(57, cut), imodbits_none, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["qqtwohand_scimitar","Twohanded_scimitar", [("scimitar_a2", 0),("scab_scimeter_a2", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_left_hip|itc_nodachi|itcf_horseback_overswing_right_onehanded|itcf_horseback_overswing_left_onehanded|itcf_show_holster_when_drawn,723, weight(1.75)|abundance(20)|hit_points(43008)|spd_rtng(85)|weapon_length(123)|thrust_damage(0, pierce)|swing_damage(55, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["per_spear_g_1_9m","Spear", [("spear_g_1-9m", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,340, weight(1.25)|abundance(90)|difficulty(4)|hit_points(15360)|spd_rtng(79)|weapon_length(162)|thrust_damage(35, pierce)|swing_damage(33, cut), imodbits_polearm, [], [fac_kingdom_9]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qq2h_claymore","Claymore", [("2h_claymore", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_sword_back|itc_greatsword,700, weight(3)|abundance(10)|difficulty(15)|hit_points(31744)|spd_rtng(85)|weapon_length(115)|thrust_damage(31, pierce)|swing_damage(58, cut), imodbits_sword|imodbit_masterwork, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["qqgerman_poleaxe","Halberd", [("german_poleaxe", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_offset_lance|itp_unbalanced, itc_parry_polearm|itcf_thrust_twohanded|itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,678, weight(5.75)|abundance(100)|difficulty(18)|hit_points(49152)|spd_rtng(77)|weapon_length(151)|thrust_damage(37, pierce)|swing_damage(47, cut), imodbits_polearm|imodbit_fine, [], [fac_kingdom_23,fac_kingdom_25]],
  ["qqelegant_poleaxe","Poleaxe", [("elegant_poleaxe", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_offset_lance, itc_greatsword|itcf_horseback_thrust_onehanded,499, weight(7)|abundance(100)|difficulty(15)|hit_points(32768)|spd_rtng(78)|weapon_length(140)|thrust_damage(31, pierce)|swing_damage(46, cut), imodbits_polearm|imodbit_fine, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["qqflamberge11","Flamberge", [("flamberge", 0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_can_knock_down, itcf_carry_sword_back|itc_greatsword|itcf_show_holster_when_drawn,810, weight(3.25)|abundance(100)|difficulty(15)|hit_points(46080)|spd_rtng(83)|weapon_length(150)|thrust_damage(31, pierce)|swing_damage(58, cut), imodbits_sword|imodbit_fine|imodbit_masterwork, [], [fac_kingdom_8]],
  ["qqone_handed_war_axe_b","One_handed_war_axe", [("one_handed_war_axe_b", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar,495, weight(2.5)|abundance(100)|difficulty(8)|hit_points(34816)|spd_rtng(75)|weapon_length(68)|thrust_damage(22, pierce)|swing_damage(34, pierce), imodbits_axe, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qqone_handed_battle_axe_a","Military_axe", [("one_handed_battle_axe_a", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar,290, weight(1.5)|abundance(100)|difficulty(8)|hit_points(33792)|spd_rtng(78)|weapon_length(70)|thrust_damage(22, pierce)|swing_damage(33, pierce), imodbits_axe, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["qqone_handed_war_axe_a","One_handed_war_axe", [("one_handed_war_axe_a", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar,469, weight(2)|abundance(100)|difficulty(9)|hit_points(30720)|spd_rtng(80)|weapon_length(68)|thrust_damage(22, pierce)|swing_damage(30, pierce), imodbits_axe, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["jjnaginata","Naginata", [("naginata", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,580, weight(3)|abundance(100)|difficulty(15)|hit_points(40960)|spd_rtng(68)|weapon_length(197)|thrust_damage(27, pierce)|swing_damage(52, cut), imodbits_polearm, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["jjnaginata_light","Naginata", [("naginata_light", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,580, weight(3)|abundance(100)|difficulty(15)|hit_points(40960)|spd_rtng(67)|weapon_length(210)|thrust_damage(27, pierce)|swing_damage(52, cut), imodbits_polearm, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jjjumonji_yari","Yari", [("jumonji_yari", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,295, weight(3.25)|abundance(40)|difficulty(8)|hit_points(16384)|spd_rtng(73)|weapon_length(160)|thrust_damage(35, pierce)|swing_damage(42, cut), imodbits_polearm, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["jjyari_spear_crimson","Yari", [("yari_spear_crimson", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itcf_carry_spear|itc_parry_polearm|itcf_thrust_polearm|itcf_overswing_polearm|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,295, weight(3.25)|abundance(40)|difficulty(8)|hit_points(16384)|spd_rtng(69)|weapon_length(205)|thrust_damage(35, pierce)|swing_damage(29, cut), imodbits_polearm, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["jjheraldic_banner_yari","Yari", [("banner_yari", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itc_parry_polearm|itcf_thrust_polearm|itcf_overswing_polearm|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,295, weight(3.25)|abundance(40)|difficulty(8)|hit_points(16384)|spd_rtng(66)|weapon_length(245)|thrust_damage(35, pierce)|swing_damage(29, cut), imodbits_polearm, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_banner_spear", ":var0", ":var1"),
    ]),
   ], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["qqspear_h_2_15m","Spear", [("spear_h_2-15m", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,340, weight(1.25)|abundance(90)|difficulty(4)|hit_points(15360)|spd_rtng(78)|weapon_length(133)|thrust_damage(32, pierce)|swing_damage(29, cut), imodbits_polearm, []],
  ["banner_lance_1","Lance", [("banner_lance_1", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itc_parry_polearm|itcf_thrust_polearm|itcf_overswing_polearm|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,295, weight(3.25)|abundance(40)|difficulty(8)|hit_points(16384)|spd_rtng(69)|weapon_length(257)|thrust_damage(35, pierce)|swing_damage(29, cut), imodbits_polearm, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_banner_spear", ":var0", ":var1"),
    ]),
   ], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["banner_lance_2","Lance", [("banner_lance_2", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itc_parry_polearm|itcf_thrust_polearm|itcf_overswing_polearm|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,295, weight(3.25)|abundance(40)|difficulty(8)|hit_points(16384)|spd_rtng(60)|weapon_length(262)|thrust_damage(35, pierce)|swing_damage(29, cut), imodbits_polearm, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_banner_spear", ":var0", ":var1"),
    ]),
   ], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["banner_lance_3","Lance", [("banner_lance_3", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance|itp_unbalanced, itcf_carry_spear|itc_parry_polearm|itcf_thrust_polearm|itcf_overswing_polearm|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,295, weight(3.25)|abundance(40)|difficulty(8)|hit_points(16384)|spd_rtng(65)|weapon_length(288)|thrust_damage(35, pierce)|swing_damage(29, cut), imodbits_polearm, [
    (ti_on_init_item, [
      (store_trigger_param_1, ":var0"),
      (store_trigger_param_2, ":var1"),
      (call_script, "script_shield_item_set_banner", "tableau_banner_spear", ":var0", ":var1"),
    ]),
   ], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["han_sp_arrows","Arrows", [("arrow_b", 0),("flying_arrow", ixmesh_flying_ammo),("quiver_c", ixmesh_carry)], itp_type_arrows|itp_default_ammo, itcf_carry_quiver_back,200, weight(3)|abundance(100)|weapon_length(95)|max_ammo(20)|thrust_damage(33, pierce), imodbits_missile, [], [fac_kingdom_1]],
  ["chongtong_arrows","Chongtong_arrows", [("arrow_b", 0),("guangjian_fly_SEO", ixmesh_flying_ammo),("quiver_c", ixmesh_carry)], itp_type_bullets|itp_default_ammo|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, itcf_carry_quiver_right_vertical,410, weight(3.5)|abundance(90)|weapon_length(95)|max_ammo(15)|thrust_damage(33, pierce), imodbits_missile, [
    (ti_on_missile_hit, [
      (store_trigger_param_1, ":var0"),
      (call_script, "script_fire_at_pos1", 500, 15, ":var0"),
    ]),
   ], [fac_kingdom_1]],
  ["cartridge_a","Bullet", [("cartridge_a", 0)], itp_type_bullets|itp_default_ammo|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair, 0,410, weight(2.25)|abundance(90)|weapon_length(3)|max_ammo(15)|thrust_damage(50, pierce), imodbit_large_bag, []],
  ["sling_rocks","Rocks", [("throwing_stone", 0),("throwing_stone", ixmesh_flying_ammo),("bolt_bag_c", ixmesh_carry)], itp_type_bullets, 0,5, weight(0.5)|abundance(90)|weapon_length(3)|max_ammo(15)|thrust_damage(20, blunt), imodbits_missile, []],
  ["darts","Darts", [("dart_b", 0),("dart_b_bag", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_primary, itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn,85, weight(2)|abundance(100)|difficulty(1)|spd_rtng(90)|shoot_speed(30)|weapon_length(32)|max_ammo(15)|thrust_damage(28, pierce), imodbits_missile|imodbit_balanced|imodbit_heavy, []],
  ["javelin","Javelin", [("javelin", 0)], itp_type_thrown|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee, itcf_throw_javelin,200, weight(2)|abundance(100)|spd_rtng(75)|shoot_speed(28)|weapon_length(65)|max_ammo(6)|thrust_damage(40, pierce), imodbits_missile|imodbit_balanced|imodbit_heavy, []],
  ["javelin_melee","Javelin", [("javelin", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_secondary, itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,200, weight(2)|abundance(100)|hit_points(9216)|spd_rtng(82)|weapon_length(65)|thrust_damage(31, pierce)|swing_damage(18, cut), imodbits_polearm, []],
  ["throwing_knives","Throwing_Knives", [("throwing_knife", 0)], itp_type_thrown|itp_merchandise|itp_primary, itcf_throw_knife,76, weight(2.5)|abundance(100)|spd_rtng(121)|shoot_speed(25)|max_ammo(14)|thrust_damage(30, cut), imodbits_missile|imodbit_balanced|imodbit_heavy, []],
  ["throwing_daggers","Throwing_Daggers", [("throwing_dagger", 0)], itp_type_thrown|itp_merchandise|itp_primary, itcf_throw_knife,193, weight(2.5)|abundance(100)|spd_rtng(110)|shoot_speed(24)|max_ammo(13)|thrust_damage(35, cut), imodbits_missile|imodbit_balanced|imodbit_heavy, []],
  ["torch","Torch", [("torch_h", 0)], itp_type_thrown|itp_primary|itp_remove_item_on_use, itcf_throw_axe,41, weight(5)|abundance(100)|spd_rtng(80)|shoot_speed(20)|weapon_length(53)|max_ammo(3)|thrust_damage(35, cut), imodbits_missile|imodbit_balanced|imodbit_heavy, [
    (ti_on_init_item, [
      (set_position_delta, 0, 60, 0),
      (particle_system_add_new, "psys_fire_glow_1"),
      (set_current_color, 150, 130, 70),
    ]),
   (ti_on_missile_hit, [
      (store_trigger_param_1, ":var0"),
      (call_script, "script_fire_at_pos1", 500, 15, ":var0"),
    ]),
   ]],
  ["amer_h_axe","Tomahawk", [("h_axe", 0)], itp_type_thrown|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee, itcf_throw_axe,360, weight(2)|abundance(100)|difficulty(1)|spd_rtng(69)|shoot_speed(18)|weapon_length(60)|max_ammo(4)|thrust_damage(55, cut), imodbits_missile|imodbit_balanced, [], [fac_kingdom_50]],
  ["qqthrowing_axes","Throwing axe", [("throwing_axe_b", 0)], itp_type_thrown|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee, itcf_throw_axe,360, weight(2)|abundance(100)|difficulty(1)|spd_rtng(69)|shoot_speed(18)|weapon_length(53)|max_ammo(4)|thrust_damage(55, cut), imodbits_missile|imodbit_balanced, []],
  ["qqthrowing_axes_melee","Throwing axe", [("throwing_axe_b", 0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar,380, weight(2)|abundance(100)|difficulty(2)|hit_points(35840)|spd_rtng(75)|weapon_length(53)|thrust_damage(22, pierce)|swing_damage(39, cut), imodbits_missile|imodbit_balanced, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["light_throwing_axes","Francisca", [("francisca", 0)], itp_type_thrown|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee, itcf_throw_axe,380, weight(3)|abundance(100)|difficulty(1)|spd_rtng(65)|shoot_speed(17)|weapon_length(53)|max_ammo(4)|thrust_damage(58, cut), imodbits_missile|imodbit_balanced, []],
  ["light_throwing_axes_melee","Francisca", [("francisca", 0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar,380, weight(3)|abundance(100)|difficulty(4)|hit_points(35840)|spd_rtng(75)|weapon_length(53)|thrust_damage(22, pierce)|swing_damage(39, cut), imodbits_missile|imodbit_balanced, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["stones","Stones", [("throwing_stone", 0)], itp_type_thrown|itp_merchandise|itp_primary|itp_secondary, itcf_throw_stone,1, weight(1)|abundance(100)|spd_rtng(95)|shoot_speed(20)|weapon_length(8)|max_ammo(15)|thrust_damage(23, blunt), imodbit_large_bag, []],
  ["rrroman_pilum_3","Pilum", [("roman_pilum_3", 0)], itp_type_thrown|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee, itcf_throw_javelin,325, weight(2)|abundance(100)|difficulty(1)|spd_rtng(70)|shoot_speed(28)|weapon_length(115)|max_ammo(6)|thrust_damage(42, pierce), imodbits_missile|imodbit_balanced|imodbit_heavy, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["rrroman_pilum_3_melee","Pilum", [("roman_pilum_3", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_secondary, itc_poleaxe|itcf_horseback_thrust_onehanded|itcf_thrust_onehanded_lance,325, weight(2)|abundance(100)|difficulty(2)|hit_points(10240)|spd_rtng(85)|weapon_length(115)|thrust_damage(31, pierce)|swing_damage(17, cut), imodbits_missile|imodbit_balanced|imodbit_heavy, [], [fac_kingdom_2,fac_kingdom_3,fac_kingdom_5,fac_kingdom_26]],
  ["jjshuriken2","Shuriken", [("shuriken2", 0)], itp_type_thrown|itp_merchandise|itp_primary|itp_secondary, itcf_throw_stone,300, weight(1)|abundance(100)|spd_rtng(95)|shoot_speed(30)|weapon_length(8)|max_ammo(15)|thrust_damage(36, pierce), imodbit_large_bag, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["jjshinobi_bite","Shinobi_bite", [("shinobi_bite_throw", 0)], itp_type_thrown|itp_merchandise|itp_primary|itp_secondary, itcf_throw_stone,300, weight(1)|abundance(100)|spd_rtng(95)|shoot_speed(30)|weapon_length(8)|max_ammo(15)|thrust_damage(36, pierce), imodbit_large_bag, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["pking_pistol","Pirate_king_pistol", [("flintlock_pistol_1", 0)], itp_type_pistol|itp_primary, itcf_shoot_pistol|itcf_reload_pistol,20500, weight(2)|abundance(10)|accuracy(83)|spd_rtng(60)|shoot_speed(220)|max_ammo(1)|thrust_damage(100, pierce), imodbits_none, [
    (ti_on_weapon_attack, [
      (position_move_x, 1, 20),
      (position_move_y, pos1, 60),
      (play_sound, "snd_pistol_shot"),
      (particle_system_burst, "psys_pistol_svet", pos1, 15),
      #(particle_system_burst, "psys_ship_shrapnel", pos1, 30), #Musket issues #Musket issues
	  #Musket issues
	   (particle_system_burst, "psys_pistol_smoke", pos1, 10),  #Add smoke
      (particle_system_burst, "psys_pistol_ogon", pos1, 30), #Add Ogon
    ]),
   ]],
  ["atomic_god","Atomic_god", [("book_open", 0)], itp_type_thrown|itp_primary|itp_secondary, itcf_throw_javelin,1, weight(169.6)|abundance(100)|spd_rtng(95)|shoot_speed(20)|weapon_length(300)|max_ammo(1)|thrust_damage(244, blunt)|swing_damage(0, blunt), imodbits_none, [
    (ti_on_missile_hit, [
      (call_script, "script_molda_atomic_god"),
    ]),
   ]],
  ["whip","Whip", [("whip", 0)], itp_type_one_handed_wpn| itp_no_parry|itp_merchandise|itp_primary, itc_scimitar,20, weight(0.2)|abundance(100)|hit_points(17408)|spd_rtng(91)|weapon_length(92)|swing_damage(20, blunt), imodbits_none, [
    (ti_on_weapon_attack, [
      (play_sound, "snd_gbt_whip_for_agent"),
    ]),
   ]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["arquebus_uniq1","Improved_arquebus", [("arquebus", 0)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_shoot_musket|itcf_reload_musket,8500, weight(2)|abundance(5)|accuracy(93)|spd_rtng(45)|shoot_speed(220)|max_ammo(1)|thrust_damage(100, pierce), imodbits_none, [
    (ti_on_weapon_attack, [
      (position_move_y, pos1, 150),
      (position_move_z, pos1, 6),
      (play_sound_at_position, "snd_pistol_shot", pos1),
      (particle_system_burst, "psys_musket_svet", pos1, 15),
      #(particle_system_burst, "psys_ship_shrapnel", pos1, 30), #Musket issues #Musket issues
      	  #Musket issues
	   (particle_system_burst, "psys_musket_smoke", pos1, 10),  #Add smoke
      (particle_system_burst, "psys_musket_ogon", pos1, 30), #Add Ogon
    ]),
   ], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["hunting_bow","Hunting_bow", [("hunting_bow", 0),("hunting_bow_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,267, weight(1)|abundance(100)|accuracy(85)|spd_rtng(65)|shoot_speed(47)|thrust_damage(25, pierce), imodbit_cracked|imodbit_bent|imodbit_strong, []],
  ["short_bow","Short_bow", [("short_bow", 0),("short_bow_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,368, weight(1)|abundance(100)|accuracy(88)|difficulty(1)|spd_rtng(62)|shoot_speed(48)|thrust_damage(27, pierce), imodbit_cracked|imodbit_bent|imodbit_strong, []],
  ["nomad_bow","Composite_bow", [("nomad_bow", 0),("nomad_bow_case", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,690, weight(1.25)|abundance(100)|accuracy(91)|difficulty(1)|spd_rtng(60)|shoot_speed(49)|thrust_damage(29, pierce), imodbit_cracked|imodbit_bent|imodbit_strong, [], [fac_kingdom_4,fac_kingdom_9,fac_kingdom_13,fac_kingdom_14,fac_kingdom_34,fac_kingdom_40,fac_kingdom_56,fac_kingdom_57]],
  ["long_bow","Long_bow", [("long_bow", 0),("long_bow_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back,630, weight(1.75)|abundance(100)|accuracy(91)|difficulty(1)|spd_rtng(57)|shoot_speed(50)|thrust_damage(32, pierce), imodbit_cracked|imodbit_bent|imodbit_strong, [], [fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_15,fac_kingdom_16,fac_kingdom_18]],
  ["hangong_bow","Composite_reflex_bow", [("nomad_bow", 0),("nomad_bow_case", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,700, weight(1)|abundance(100)|accuracy(91)|difficulty(1)|spd_rtng(59)|shoot_speed(50)|thrust_damage(30, pierce), imodbits_bow, [], [fac_kingdom_1,fac_kingdom_17,fac_kingdom_19,fac_kingdom_21,fac_kingdom_22,fac_kingdom_28,fac_kingdom_29,fac_kingdom_30,fac_kingdom_38,fac_kingdom_42,fac_kingdom_43]],
  ["han_chongton","Chongtong", [("han_CHONGTONG", 0)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket,1300, weight(25)|abundance(40)|accuracy(90)|spd_rtng(25)|shoot_speed(160)|max_ammo(1)|thrust_damage(80, pierce), imodbit_masterwork, [
    (ti_on_weapon_attack, [
      (position_move_y, pos1, 150),
      (position_move_z, pos1, 6),
      (play_sound_at_position, "snd_pistol_shot", pos1),
      (particle_system_burst, "psys_musket_svet", pos1, 15),
      #(particle_system_burst, "psys_ship_shrapnel", pos1, 30), #Musket issues #Musket issues
      	  #Musket issues
	   (particle_system_burst, "psys_musket_smoke", pos1, 10),  #Add smoke
      (particle_system_burst, "psys_musket_ogon", pos1, 30), #Add Ogon
    ]),
   ], [fac_kingdom_41]],
  ["jjbogmir_yumi","Yumi", [("bogmir_yumi_final", 0),("bogmir_yumi_final_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,368, weight(1)|abundance(100)|accuracy(88)|difficulty(1)|spd_rtng(57)|shoot_speed(49)|thrust_damage(28, pierce), imodbit_cracked|imodbit_bent|imodbit_strong, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["qqhunting_crossbow","Crossbow", [("crossbow_a", 0)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_shoot_crossbow|itcf_carry_crossbow_back,550, weight(2.25)|abundance(100)|accuracy(98)|spd_rtng(55)|shoot_speed(70)|max_ammo(1)|thrust_damage(50, pierce), imodbits_crossbow, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["eye_of_eagle_uniq1","Eagle eye", [("Archer_Bow", 0),("Archer_Bow4_carry", ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itcf_shoot_bow|itcf_carry_bow_back,9999, weight(1.75)|abundance(100)|accuracy(99)|difficulty(7)|spd_rtng(80)|shoot_speed(64)|thrust_damage(32, pierce), imodbits_none, []],
  ["bow_of_taejo_uniq1","Taejo bow", [("nomad_bow", 0),("nomad_bow_case", ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_shoot_bow|itcf_carry_bow_back,7005, weight(1)|abundance(100)|accuracy(99)|difficulty(7)|spd_rtng(80)|shoot_speed(64)|thrust_damage(32, pierce), imodbits_none, []],
  ["flintlock_pistol","Sling", [("Sling", 0)], itp_type_pistol|itp_primary|itp_cant_use_on_horseback, itcf_throw_stone,30, weight(0.5)|abundance(100)|accuracy(90)|spd_rtng(80)|shoot_speed(50)|max_ammo(1)|thrust_damage(45, blunt), imodbits_none, [
    (ti_on_weapon_attack, [
      (play_sound, "snd_throw_stone"),
    ]),
   ]],
  ["jjarquebus","Arquebus", [("arquebus", 0)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_shoot_musket|itcf_reload_musket,800, weight(2)|abundance(10)|accuracy(93)|spd_rtng(35)|shoot_speed(220)|max_ammo(1)|thrust_damage(60, pierce), imodbits_none, [
    (ti_on_weapon_attack, [
      (position_move_y, pos1, 150),
      (position_move_z, pos1, 6),
      (play_sound_at_position, "snd_pistol_shot", pos1),
      (particle_system_burst, "psys_musket_svet", pos1, 15),
      #(particle_system_burst, "psys_ship_shrapnel", pos1, 30), #Musket issues #Musket issues #Musket issues
      	  #Musket issues
	   (particle_system_burst, "psys_musket_smoke", pos1, 10),  #Add smoke
      (particle_system_burst, "psys_musket_ogon", pos1, 30), #Add Ogon
    ]),
   ], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["heavy_crossbow","Bola", [("Sling", 0)], itp_type_pistol|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_throw_stone,510, weight(1)|abundance(100)|accuracy(90)|spd_rtng(90)|shoot_speed(75)|max_ammo(1)|thrust_damage(60, blunt), imodbits_none, [
    (ti_on_weapon_attack, [
      (play_sound, "snd_throw_stone"),
    ]),
   ], [fac_kingdom_61]],
  ["cheeeeeeese_uniq1","Kaaaaaase", [("heavy_crossbow", 0)], itp_type_crossbow|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back,5505, weight(2.25)|abundance(100)|accuracy(98)|spd_rtng(70)|shoot_speed(80)|max_ammo(1)|thrust_damage(85, pierce), imodbits_crossbow, []],
  ["han_chongtong_hi","Chongtong", [("han_CHONGTONG", 0)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_cant_reload_while_moving, itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket,8300, weight(25)|abundance(40)|accuracy(90)|spd_rtng(30)|shoot_speed(160)|max_ammo(1)|thrust_damage(120, pierce), imodbit_masterwork, [
    (ti_on_weapon_attack, [
      (position_move_y, pos1, 150),
      (position_move_z, pos1, 6),
      (play_sound_at_position, "snd_pistol_shot", pos1),
      (particle_system_burst, "psys_musket_svet", pos1, 15),
      #(particle_system_burst, "psys_ship_shrapnel", pos1, 30), #Musket issues #Musket issues
      	  #Musket issues
	   (particle_system_burst, "psys_musket_smoke", pos1, 10),  #Add smoke
      (particle_system_burst, "psys_musket_ogon", pos1, 30), #Add Ogon
    ]),
   ], [fac_kingdom_41]],
  ["qqhunting_crossbow","Crossbow", [("crossbow_b", 0)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_shoot_crossbow|itcf_carry_crossbow_back,550, weight(2.25)|abundance(100)|accuracy(98)|spd_rtng(55)|shoot_speed(70)|max_ammo(1)|thrust_damage(50, pierce), imodbits_crossbow, [], [fac_kingdom_23,fac_kingdom_24,fac_kingdom_25,fac_kingdom_53,fac_kingdom_54,fac_kingdom_55,fac_kingdom_58,fac_kingdom_59,fac_kingdom_60,fac_kingdom_61]],
  ["iber_matchlock_2","Matchlock", [("matchlock_2", 0)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_shoot_musket|itcf_reload_musket,800, weight(2)|abundance(10)|accuracy(93)|spd_rtng(35)|shoot_speed(220)|max_ammo(1)|thrust_damage(60, pierce), imodbits_none, [
    (ti_on_weapon_attack, [
      (position_move_y, pos1, 150),
      (position_move_z, pos1, 6),
      (play_sound_at_position, "snd_pistol_shot", pos1),
      (particle_system_burst, "psys_musket_svet", pos1, 15),
      #(particle_system_burst, "psys_ship_shrapnel", pos1, 30), #Musket issues #Musket issues
      	  #Musket issues
	   (particle_system_burst, "psys_musket_smoke", pos1, 10),  #Add smoke
      (particle_system_burst, "psys_musket_ogon", pos1, 30), #Add Ogon
    ]),
   ], [fac_kingdom_23,fac_kingdom_25]],
  ["iber_matchlock_1","Matchlock", [("matchlock_1", 0)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_shoot_musket|itcf_reload_musket,800, weight(2)|abundance(10)|accuracy(93)|spd_rtng(35)|shoot_speed(220)|max_ammo(1)|thrust_damage(60, pierce), imodbits_none, [
    (ti_on_weapon_attack, [
      (position_move_y, pos1, 150),
      (position_move_z, pos1, 6),
      (play_sound_at_position, "snd_pistol_shot", pos1),
      (particle_system_burst, "psys_musket_svet", pos1, 15),
      #(particle_system_burst, "psys_ship_shrapnel", pos1, 30), #Musket issues #Musket issues
            	  #Musket issues
	   (particle_system_burst, "psys_musket_smoke", pos1, 10),  #Add smoke
      (particle_system_burst, "psys_musket_ogon", pos1, 30), #Add Ogon
    ]),
   ], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["iber_flintlock_pistol_1","Pistol", [("flintlock_pistol_1", 0)], itp_type_pistol|itp_merchandise|itp_primary, itcf_shoot_pistol|itcf_reload_pistol,1000, weight(2)|abundance(10)|accuracy(73)|spd_rtng(45)|shoot_speed(220)|max_ammo(1)|thrust_damage(50, pierce), imodbits_none, [
    (ti_on_weapon_attack, [
      (position_move_x, 1, 20),
      (position_move_y, pos1, 60),
      (play_sound, "snd_pistol_shot"),
      (particle_system_burst, "psys_pistol_svet", pos1, 15),
      #(particle_system_burst, "psys_ship_shrapnel", pos1, 30), #Musket issues #Musket issues
            	  #Musket issues
	   (particle_system_burst, "psys_pistol_smoke", pos1, 10),  #Add smoke
      (particle_system_burst, "psys_pistol_ogon", pos1, 30), #Add Ogon
    ]),
   ], [fac_kingdom_23,fac_kingdom_25]],
  ["cunt_hitter_uniq1","Cunt_hitter", [("long_bow", 0),("long_bow_carry", ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_shoot_bow|itcf_carry_bow_back,6300, weight(1.75)|abundance(100)|accuracy(98)|difficulty(1)|spd_rtng(80)|shoot_speed(60)|thrust_damage(32, pierce), imodbit_cracked|imodbit_bent|imodbit_strong, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["jjbogmir_yumi_uniq1","Yoichi_yumi", [("bogmir_yumi_final", 0),("bogmir_yumi_final_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,368, weight(1)|abundance(100)|accuracy(95)|difficulty(1)|spd_rtng(60)|shoot_speed(49)|thrust_damage(40, pierce), imodbit_cracked|imodbit_bent|imodbit_strong, [], [fac_kingdom_20,fac_kingdom_63,fac_kingdom_64,fac_kingdom_65,fac_kingdom_66,fac_kingdom_67]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["supply_food","Food supplies", [("wheat_sack", 0)], itp_type_goods, 0,1, weight(500)|abundance(100), imodbits_none, []],
  ["coin_box","Coin box", [("chest_simple", 0)], itp_type_goods|itp_always_loot, 0,30000, weight(0.1)|abundance(100), imodbits_none, []],
  ["ship_invisiblehead","ship_invis", [("osp_greathelm_a", ixmesh_inventory),("invalid_item", 0)], itp_type_head_armor|itp_civilian|itp_covers_head, 0,1, weight(1)|abundance(100)|head_armor(111)|body_armor(111)|leg_armor(111), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_deadly|imodbit_masterwork, []],
  ["ship_invisiblehand","ship_invis", [("leather_gloves_L", ixmesh_inventory),("invalid_item", 0)], itp_type_hand_armor|itp_civilian, 0,1, weight(0.5)|abundance(100)|head_armor(111)|body_armor(111)|leg_armor(111), imodbits_none, []],
  ["ship_invisiblefoot","ship_invis", [("hanboot_nomad_b", ixmesh_inventory),("1_inv_foot", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|head_armor(111)|body_armor(111)|leg_armor(111), imodbits_armor, []],
  ["ship_invisiblebody","ship_invis", [("wei_xiadi_sar_leather_chain", ixmesh_inventory),("1_inv_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(15)|abundance(100)|head_armor(111)|body_armor(111)|leg_armor(111), imodbits_armor|imodbit_cracked, []],
  ["invisiblehead","Head", [("osp_greathelm_a", ixmesh_inventory),("invalid_item", 0)], itp_type_head_armor|itp_civilian|itp_covers_head, 0,1, weight(1)|abundance(100)|head_armor(55), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_deadly|imodbit_masterwork, []],
  ["invisiblehand","222invhand", [("leather_gloves_L", ixmesh_inventory),("invalid_item", 0)], itp_type_hand_armor|itp_civilian, 0,1, weight(0.5)|abundance(100)|head_armor(25)|body_armor(25)|leg_armor(25), imodbits_none, []],
  ["invisiblefoot","Foot", [("hanboot_nomad_b", ixmesh_inventory),("1_inv_foot", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["invisiblebody","Body", [("wei_xiadi_sar_leather_chain", ixmesh_inventory),("1_inv_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(15)|abundance(100)|body_armor(55)|leg_armor(25), imodbits_armor|imodbit_cracked, []],
  ["invisible_nocoverhead","Nocover_head", [("osp_greathelm_a", ixmesh_inventory),("invalid_item", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|head_armor(55), imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_deadly|imodbit_masterwork, []],
  ["mi_sb_boat","Boat", [("mi_sb_dragonship", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(500)|horse_maneuver(15)|horse_speed(25)|weapon_length(100), imodbits_none, []],
  ["mi_sb_caravel","Caravel", [("mi_sb_caravel", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(700)|horse_maneuver(20)|horse_speed(40)|weapon_length(100), imodbits_none, []],
  ["mi_sb_carrack","Carrack", [("mi_sb_carrack", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(800)|horse_maneuver(15)|horse_speed(35)|weapon_length(100), imodbits_none, []],
  ["mi_sb_xebec","Xebec", [("mi_sb_xebec", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(800)|horse_maneuver(20)|horse_speed(35)|weapon_length(100), imodbits_none, []],
  ["mi_sb_galley","Galley", [("mi_sb_galley", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(750)|horse_maneuver(25)|horse_speed(35)|weapon_length(100), imodbits_none, []],
  ["mi_sb_galleon","Galleon", [("mi_sb_galleon", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(1100)|horse_maneuver(15)|horse_speed(25)|weapon_length(100), imodbits_none, []],
  ["mi_sb_turship","Geobukseon", [("mi_sb_turship", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(1800)|horse_maneuver(20)|horse_speed(30)|weapon_length(100), imodbits_none, []],
  ["mi_sb_junkship","Junk", [("mi_sb_junkship", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(800)|horse_maneuver(15)|horse_speed(35)|weapon_length(100), imodbits_none, []],
  ["mi_sb_panship","Flat_ship", [("mi_sb_panship", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(700)|horse_maneuver(20)|horse_speed(35)|weapon_length(100), imodbits_none, []],
  ["mi_sb_frigate","Frigate", [("mi_sb_frigate", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(1600)|horse_maneuver(15)|horse_speed(25)|weapon_length(100), imodbits_none, []],
  ["mi_sb_dragonship","Dragon_ship", [("mi_sb_dragonship", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(700)|horse_maneuver(25)|horse_speed(35)|weapon_length(100), imodbits_none, []],
  ["mi_sb_galleas","Galleass", [("mi_sb_galleas", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(1100)|horse_maneuver(20)|horse_speed(30)|weapon_length(100), imodbits_none, []],
  ["mi_sb_black_ship","Black_ship", [("mi_sb_black_ship", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(1500)|horse_maneuver(20)|horse_speed(40)|weapon_length(100), imodbits_none, []],
  ["mi_sb_ghost","Ghost_ship", [("mi_sb_black_ship", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(1600)|horse_maneuver(20)|horse_speed(35)|weapon_length(100), imodbits_none, []],
  ["mi_sb_antecship","Atakebune", [("mi_sb_antecship", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(950)|horse_maneuver(15)|horse_speed(25)|weapon_length(100), imodbits_none, []],
  ["mi_sb_nugakship","Pavilion_ship", [("mi_sb_nugakship", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(800)|horse_maneuver(20)|horse_speed(25)|weapon_length(100), imodbits_none, []],
  ["mi_sb_panokship","Panokseon", [("mi_sb_panokship", 0)], itp_type_horse, 0,1, weight(0.1)|abundance(100)|body_armor(250)|hit_points(900)|horse_maneuver(20)|horse_speed(25)|weapon_length(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["blueprint_of_black_ship","Black ship blueprint", [("book_a", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["blueprint_of_ghost_ship","Ghost ship blueprint", [("book_b", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["blueprint_of_geobukseon","Geobukseon ship blueprint", [("book_c", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["blueprint_of_frigate","Frigate blueprint", [("book_d", 0)], itp_type_book|itp_always_loot, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["body_hd_wet_trans_under","body_hd_wet_trans_under", [("body_hd_wet_trans_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["ship_range_ball_1","ship_range_ball", [("invalid_item", 0),("sb_range_cannon", ixmesh_flying_ammo),("arrow", ixmesh_carry)], itp_type_thrown, itcf_throw_javelin,1, weight(3)|abundance(100)|hit_points(10000)|spd_rtng(100)|shoot_speed(35)|weapon_length(95)|max_ammo(10)|thrust_damage(25, cut), imodbits_none, [
    (ti_on_weapon_attack, [
      (play_sound_at_position, "snd_cannon_shot", pos1),
      (position_move_z, pos1, -60),
      (position_move_y, pos1, -130),
      (position_move_x, 1, -120),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
      (particle_system_burst, "psys_ship_shrapnel", pos1, 2), #Musket issues #Musket issues
      (particle_system_burst, "psys_lanse_straw", pos1, 2), #Musket issues 
      (position_move_z, pos1, 30),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
      (particle_system_burst, "psys_ship_shrapnel", pos1, 2), #Musket issues #Musket issues
      (particle_system_burst, "psys_lanse_straw", pos1, 2), #Musket issues
      (position_move_z, pos1, 30),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
      (particle_system_burst, "psys_ship_shrapnel", pos1, 2), #Musket issues #Musket issues
      (particle_system_burst, "psys_lanse_straw", pos1, 2), #Musket issues
      (position_move_z, pos1, 30),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
      (particle_system_burst, "psys_ship_shrapnel", pos1, 2), #Musket issues #Musket issues
      (particle_system_burst, "psys_lanse_straw", pos1, 2), #Musket issues
      (position_move_z, pos1, 30),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
      (particle_system_burst, "psys_ship_shrapnel", pos1, 2), #Musket issues #Musket issues
      (particle_system_burst, "psys_lanse_straw", pos1, 2), #Musket issues
    ]),
   (ti_on_missile_hit, [
      (store_trigger_param_1, ":var0"),
      (call_script, "script_molda_ship_range_attack", ":var0"),
    ]),
   ]],
  ["ship_range_arrow_1","ship_range_arrow", [("invalid_item", 0),("sb_range_arrow", ixmesh_flying_ammo),("arrow", ixmesh_carry)], itp_type_thrown, itcf_throw_javelin,1, weight(3)|abundance(100)|hit_points(10000)|spd_rtng(100)|shoot_speed(25)|weapon_length(95)|max_ammo(10)|thrust_damage(25, cut), imodbits_none, [
    (ti_on_weapon_attack, [
      (play_sound_at_position, "snd_sea_bow_shoot", pos1),
    ]),
   (ti_on_missile_hit, [
      (store_trigger_param_1, ":var0"),
      (call_script, "script_molda_ship_range_attack", ":var0"),
    ]),
   ]],
  ["ship_melee_gun_1","ship_melee_fight", [("invalid_item", 0),("arrow", 0)], itp_type_one_handed_wpn| itp_no_parry|itp_two_handed|itp_primary|itp_no_pick_up_from_ground, itcf_thrust_onehanded|itcf_horseback_thrust_onehanded,1, weight(1)|abundance(100)|hit_points(34463)|spd_rtng(50)|weapon_length(140)|thrust_damage(35, cut)|swing_damage(35, cut), imodbits_none, [
    (ti_on_weapon_attack, [
      (position_move_z, pos1, -50),
      (position_move_y, pos1, 80),
      (position_move_x, 1, -60),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
      (particle_system_burst, "psys_ship_shrapnel", pos1, 2), #Musket issues #Musket issues
      (particle_system_burst, "psys_lanse_straw", pos1, 2), #Musket issues
      (position_move_x, 1, 30),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
      (particle_system_burst, "psys_ship_shrapnel", pos1, 2), #Musket issues #Musket issues
      (particle_system_burst, "psys_lanse_straw", pos1, 2), #Musket issues
      (position_move_x, 1, 30),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
      (particle_system_burst, "psys_ship_shrapnel", pos1, 2), #Musket issues #Musket issues
      (particle_system_burst, "psys_lanse_straw", pos1, 2), #Musket issues
      (position_move_x, 1, 30),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
      (particle_system_burst, "psys_ship_shrapnel", pos1, 2), #Musket issues #Musket issues
      (particle_system_burst, "psys_lanse_straw", pos1, 2), #Musket issues
      (position_move_x, 1, 30),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
      (particle_system_burst, "psys_ship_shrapnel", pos1, 2), #Musket issues #Musket issues
      (particle_system_burst, "psys_lanse_straw", pos1, 2), #Musket issues
      (call_script, "script_molda_ship_melee_gun_fire"),
    ]),
   (ti_on_weapon_attack, [
      (store_trigger_param_1, ":var0"),
      (call_script, "script_molda_ship_melee_attack", ":var0"),
    ]),
   ]],
  ["ship_melee_1","ship_melee_fight", [("invalid_item", 0),("arrow", 0)], itp_type_one_handed_wpn| itp_no_parry|itp_two_handed|itp_primary|itp_no_pick_up_from_ground, itcf_thrust_onehanded|itcf_horseback_thrust_onehanded,1, weight(1)|abundance(100)|hit_points(34463)|spd_rtng(50)|weapon_length(140)|thrust_damage(35, cut)|swing_damage(35, cut), imodbits_none, [
    (ti_on_weapon_attack, [
      (position_move_z, pos1, -50),
      (position_move_y, pos1, 80),
      (position_move_x, 1, -60),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
      (position_move_x, 1, 30),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
      (position_move_x, 1, 30),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
      (position_move_x, 1, 30),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
      (position_move_x, 1, 30),
      (particle_system_burst, "psys_pistol_svet", pos1, 10),
    ]),
   (ti_on_weapon_attack, [
      (store_trigger_param_1, ":var0"),
      (call_script, "script_molda_ship_melee_attack", ":var0"),
    ]),
   ]],
  ["face_cover_turbun","Turban", [("rabati_new", 0)], itp_type_head_armor|itp_civilian|itp_covers_beard, 0,1, weight(1)|abundance(100)|head_armor(30), imodbits_cloth, []],
  ["smallboob_herb","Smallboob_herb", [("lettuce", 0)], itp_type_animal|itp_merchandise, 0,410, weight(3)|abundance(100), imodbits_none, []],
  ["bigboob_herb","Bigboob_herb", [("olive_inventory", 0)], itp_type_animal|itp_merchandise, 0,410, weight(3)|abundance(100), imodbits_none, []],
  ["pawnpenis_herb","Pawnpenis_herb", [("bean", 0)], itp_type_animal|itp_merchandise, 0,210, weight(3)|abundance(100), imodbits_none, []],
  ["kingpenis_herb","Kingpenis_herb", [("kherb", 0)], itp_type_animal|itp_merchandise, 0,210, weight(3)|abundance(100), imodbits_none, []],
  ["assassinate_mission_arrow","Poison_bolts", [("bolt", 0),("flying_bolt", ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_default_ammo, itcf_carry_quiver_right_vertical,164, weight(1)|abundance(100)|weapon_length(63)|max_ammo(2)|thrust_damage(35, pierce), imodbits_missile, [
    (ti_on_missile_hit, [
      (call_script, "script_poison_arrow_trig"),
    ]),
   ]],
  ["gem_box","Gem_box", [("chest_simple", 0)], itp_type_goods|itp_always_loot, 0,60000, weight(0.1)|abundance(100), imodbits_none, []],
  ["woman_no_head","woman_no_head", [("invalid_item", 0)], itp_type_head_armor|itp_covers_head|itp_covers_beard, 0,1, weight(1)|abundance(100)|head_armor(70), imodbits_none, []],
  ["cattt","Cat", [("cattt", 0)], itp_type_goods, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["juice","Juice", [("honey_pot", 0)], itp_type_goods, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["compass_inv","Sextant", [("compass_inv", 0)], itp_type_goods, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["checkbook","Checkbook", [("book_e", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["desert_fortress","Desert_fortress", [("book_open", 0)], itp_type_book|itp_merchandise, 0,1500, weight(4)|abundance(100), imodbits_shield, [], [fac_kingdom_27]],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["11111","1111", [("book_open", 0)], itp_type_book, 0,1, weight(1)|abundance(100), imodbits_none, []],
  ["rom_handl","rom_handL", [("rom_handL", 0)], itp_type_hand_armor|itp_civilian, 0,1, weight(1)|abundance(100)|head_armor(5)|body_armor(5)|leg_armor(5), imodbits_none, []],
  ["man_hard_new_ro","man_hard_new_ro", [("man_hard_new_ro", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["man_hard_new_ro_2","man_hard_new_ro_2", [("man_hard_new_ro_2", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["man_hard_new_ro_3","man_hard_new_ro_3", [("man_hard_new_ro_3", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["man_hard_new_ro_4","man_hard_new_ro_4", [("man_hard_new_ro_4", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["man_hard_new_ro_5","man_hard_new_ro_5", [("man_hard_new_ro_5", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["pussy_ass_a","pussy_ass_a", [("pussy_ass_a", 0)], itp_type_head_armor|itp_civilian|itp_covers_head|itp_covers_beard, 0,11, weight(0.5)|abundance(100)|head_armor(25), imodbits_none, []],
  ["pussy_ass_b","pussy_ass_b", [("pussy_ass_b", 0)], itp_type_head_armor|itp_civilian|itp_covers_head|itp_covers_beard, 0,11, weight(0.5)|abundance(100)|head_armor(25), imodbits_none, []],
  ["pussy_ass_c","pussy_ass_c", [("pussy_ass_c", 0)], itp_type_head_armor|itp_civilian|itp_covers_head|itp_covers_beard, 0,11, weight(0.5)|abundance(100)|head_armor(25), imodbits_none, []],
  ["pussy_ass_d","pussy_ass_d", [("pussy_ass_d", 0)], itp_type_head_armor|itp_civilian|itp_covers_head|itp_covers_beard, 0,11, weight(0.5)|abundance(100)|head_armor(25), imodbits_none, []],
  ["pussy_ass_gape_b","pussy_ass_gape_b", [("pussy_ass_gape_b", 0)], itp_type_head_armor|itp_civilian|itp_covers_head|itp_covers_beard, 0,11, weight(0.5)|abundance(100)|head_armor(25), imodbits_none, []],
  ["pussy_ass_gape_c","pussy_ass_gape_c", [("pussy_ass_gape_c", 0)], itp_type_head_armor|itp_civilian|itp_covers_head|itp_covers_beard, 0,11, weight(0.5)|abundance(100)|head_armor(25), imodbits_none, []],
  ["pussy_ass_gape_d","pussy_ass_gape_d", [("pussy_ass_gape_d", 0)], itp_type_head_armor|itp_civilian|itp_covers_head|itp_covers_beard, 0,11, weight(0.5)|abundance(100)|head_armor(25), imodbits_none, []],
  ["bukkake_face","bukkake_face", [("Semen2", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|head_armor(25), imodbits_none, []],
  ["bukkake_face2","bukkake_face2", [("Semen4", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|head_armor(25), imodbits_none, []],
  ["bukkake_mouth","bukkake_mouth", [("Semen5_mouth", 0)], itp_type_head_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|head_armor(25), imodbits_none, []],
  ["man_hard_neww","man_hard_neww", [("man_hard_neww", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["man_hard_new_bk","man_hard_new_bk", [("man_hard_new_bk", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["bm_handl","bm_handL", [("bm_handL", 0)], itp_type_hand_armor|itp_civilian, 0,1, weight(1)|abundance(100)|head_armor(5)|body_armor(5)|leg_armor(5), imodbits_none, []],
  ["am_handl","am_handL", [("am_handL", 0)], itp_type_hand_armor|itp_civilian, 0,1, weight(1)|abundance(100)|head_armor(5)|body_armor(5)|leg_armor(5), imodbits_none, []],
  ["man_hard_neww_2","man_hard_neww_2", [("man_hard_neww_2", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["man_hard_neww_3","man_hard_neww_3", [("man_hard_neww_3", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["man_hard_neww_4","man_hard_neww_4", [("man_hard_neww_4", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["man_hard_neww_5","man_hard_neww_5", [("man_hard_neww_5", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["man_hard_new_bk_2","man_hard_new_bk_2", [("man_hard_new_bk_2", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["man_hard_new_bk_3","man_hard_new_bk_3", [("man_hard_new_bk_3", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["man_hard_new_bk_4","man_hard_new_bk_4", [("man_hard_new_bk_4", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["man_hard_new_bk_5","man_hard_new_bk_5", [("man_hard_new_bk_5", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["whi_handl","whi_handL", [("whi_handL", 0)], itp_type_hand_armor|itp_civilian, 0,1, weight(0.5)|abundance(100)|head_armor(15)|body_armor(15)|leg_armor(15), imodbits_none, []],
  ["lig_handl","lig_handL", [("lig_handL", 0)], itp_type_hand_armor|itp_civilian, 0,1, weight(0.5)|abundance(100)|head_armor(15)|body_armor(15)|leg_armor(15), imodbits_none, []],
  ["red_handl","red_handL", [("red_handL", 0)], itp_type_hand_armor|itp_civilian, 0,1, weight(0.5)|abundance(100)|head_armor(15)|body_armor(15)|leg_armor(15), imodbits_none, []],
  ["norm_handl","norm_handL", [("norm_handL", 0)], itp_type_hand_armor|itp_civilian, 0,1, weight(0.5)|abundance(100)|head_armor(15)|body_armor(15)|leg_armor(15), imodbits_none, []],
  ["ro_handl","ro_handL", [("ro_handL", 0)], itp_type_hand_armor|itp_civilian, 0,1, weight(0.5)|abundance(100)|head_armor(15)|body_armor(15)|leg_armor(15), imodbits_none, []],
  ["bk_handl","bk_handL", [("bk_handL", 0)], itp_type_hand_armor|itp_civilian, 0,1, weight(0.5)|abundance(100)|head_armor(15)|body_armor(15)|leg_armor(15), imodbits_none, []],
  ["noboob_body","noboob_body", [("noboob_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["tiny_body","tiny_body", [("tiny_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["flat_body","flat_body", [("flat_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["light_body","light_body", [("light_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["light_body_sunburn","light_body_sunburn", [("light_body_sunburn", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["housemaid_body","housemaid_body", [("housemaid_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["body_brown","body_brown", [("body_brown", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["binyu_body","binyu_body", [("binyu_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["balance_body","balance_body", [("balance_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["normal_body","normal_body", [("normal_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["unor_body","unor_body", [("unor_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["unor_body_sunburn","unor_body_sunburn", [("unor_body_sunburn", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["body_hd_wet","body_hd_wet", [("body_hd_wet", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["boobs_body","boobs_body", [("boobs_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["boobs_body_sunburn","boobs_body_sunburn", [("boobs_body_sunburn", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["ultraboobs_body","ultraboobs_body", [("ultraboobs_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["bk_light_body","bk_light_body", [("bk_light_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["bk_normal_body","bk_normal_body", [("bk_normal_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["bk_boobs_body","bk_boobs_body", [("bk_boobs_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["ro_light_body","ro_light_body", [("ro_light_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["ro_normal_body","ro_normal_body", [("ro_normal_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["ro_boobs_body","ro_boobs_body", [("ro_boobs_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["noboob_body_under","noboob_body_under", [("noboob_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["tiny_body_under","tiny_body_under", [("tiny_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["flat_body_under","flat_body_under", [("flat_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["light_body_under","light_body_under", [("light_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["light_body_sunburn_under","light_body_sunburn_under", [("light_body_sunburn_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["housemaid_body_under","housemaid_body_under", [("housemaid_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["body_brown_under","body_brown_under", [("body_brown_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["binyu_body_under","binyu_body_under", [("binyu_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["balance_body_under","balance_body_under", [("balance_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["normal_body_under","normal_body_under", [("normal_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["unor_body_under","unor_body_under", [("unor_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["unor_body_sunburn_under","unor_body_sunburn_under", [("unor_body_sunburn_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["body_hd_wet_under","body_hd_wet_under", [("body_hd_wet_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["boobs_body_under","boobs_body_under", [("boobs_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["boobs_body_sunburn_under","boobs_body_sunburn_under", [("boobs_body_sunburn_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["ultraboobs_body_under","ultraboobs_body_under", [("ultraboobs_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["bk_light_body_under","bk_light_body_under", [("bk_light_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["bk_normal_body_under","bk_normal_body_under", [("bk_normal_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["bk_boobs_body_under","bk_boobs_body_under", [("bk_boobs_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["ro_light_body_under","ro_light_body_under", [("ro_light_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["ro_normal_body_under","ro_normal_body_under", [("ro_normal_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["ro_boobs_body_under","ro_boobs_body_under", [("ro_boobs_body_under", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["squirt_noboob_body","squirt_noboob_body", [("hanboot_nomad_b", ixmesh_inventory),("squirt_noboob_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["squirt_tiny_body","squirt_tiny_body", [("hanboot_nomad_b", ixmesh_inventory),("squirt_tiny_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["squirt_flat_body","squirt_flat_body", [("hanboot_nomad_b", ixmesh_inventory),("squirt_flat_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["squirt_light_body","squirt_light_body", [("hanboot_nomad_b", ixmesh_inventory),("squirt_light_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["squirt_housemaid_body","squirt_housemaid_body", [("hanboot_nomad_b", ixmesh_inventory),("squirt_housemaid_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["squirt_body_brown","squirt_body_brown", [("hanboot_nomad_b", ixmesh_inventory),("squirt_body_brown", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["squirt_binyu_body","squirt_binyu_body", [("hanboot_nomad_b", ixmesh_inventory),("squirt_binyu_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["squirt_balance_body","squirt_balance_body", [("hanboot_nomad_b", ixmesh_inventory),("squirt_balance_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["squirt_normal_body","squirt_normal_body", [("hanboot_nomad_b", ixmesh_inventory),("squirt_normal_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["squirt_unor_body","squirt_unor_body", [("hanboot_nomad_b", ixmesh_inventory),("squirt_unor_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["squirt_body_hd_wet","squirt_body_hd_wet", [("hanboot_nomad_b", ixmesh_inventory),("squirt_body_hd_wet", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["squirt_boobs_body","squirt_boobs_body", [("hanboot_nomad_b", ixmesh_inventory),("squirt_boobs_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["squirt_ultraboobs_body","squirt_ultraboobs_body", [("hanboot_nomad_b", ixmesh_inventory),("squirt_ultraboobs_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["pussycum_noboob_body","pussycum_noboob_body", [("hanboot_nomad_b", ixmesh_inventory),("pussycum_noboob_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["pussycum_tiny_body","pussycum_tiny_body", [("hanboot_nomad_b", ixmesh_inventory),("pussycum_tiny_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["pussycum_flat_body","pussycum_flat_body", [("hanboot_nomad_b", ixmesh_inventory),("pussycum_flat_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["pussycum_light_body","pussycum_light_body", [("hanboot_nomad_b", ixmesh_inventory),("pussycum_light_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["pussycum_housemaid_body","pussycum_housemaid_body", [("hanboot_nomad_b", ixmesh_inventory),("pussycum_housemaid_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["pussycum_body_brown","pussycum_body_brown", [("hanboot_nomad_b", ixmesh_inventory),("pussycum_body_brown", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["pussycum_binyu_body","pussycum_binyu_body", [("hanboot_nomad_b", ixmesh_inventory),("pussycum_binyu_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["pussycum_balance_body","pussycum_balance_body", [("hanboot_nomad_b", ixmesh_inventory),("pussycum_balance_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["pussycum_normal_body","pussycum_normal_body", [("hanboot_nomad_b", ixmesh_inventory),("pussycum_normal_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["pussycum_unor_body","pussycum_unor_body", [("hanboot_nomad_b", ixmesh_inventory),("pussycum_unor_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["pussycum_body_hd_wet","pussycum_body_hd_wet", [("hanboot_nomad_b", ixmesh_inventory),("pussycum_body_hd_wet", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["pussycum_boobs_body","pussycum_boobs_body", [("hanboot_nomad_b", ixmesh_inventory),("pussycum_boobs_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["pussycum_ultraboobs_body","pussycum_ultraboobs_body", [("hanboot_nomad_b", ixmesh_inventory),("pussycum_ultraboobs_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["bellycum_noboob_body","bellycum_noboob_body", [("hanboot_nomad_b", ixmesh_inventory),("bellycum_noboob_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["bellycum_tiny_body","bellycum_tiny_body", [("hanboot_nomad_b", ixmesh_inventory),("bellycum_tiny_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["bellycum_flat_body","bellycum_flat_body", [("hanboot_nomad_b", ixmesh_inventory),("bellycum_flat_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["bellycum_light_body","bellycum_light_body", [("hanboot_nomad_b", ixmesh_inventory),("bellycum_light_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["bellycum_housemaid_body","bellycum_housemaid_body", [("hanboot_nomad_b", ixmesh_inventory),("bellycum_housemaid_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["bellycum_body_brown","bellycum_body_brown", [("hanboot_nomad_b", ixmesh_inventory),("bellycum_body_brown", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["bellycum_binyu_body","bellycum_binyu_body", [("hanboot_nomad_b", ixmesh_inventory),("bellycum_binyu_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["bellycum_balance_body","bellycum_balance_body", [("hanboot_nomad_b", ixmesh_inventory),("bellycum_balance_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["bellycum_normal_body","bellycum_normal_body", [("hanboot_nomad_b", ixmesh_inventory),("bellycum_normal_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["bellycum_unor_body","bellycum_unor_body", [("hanboot_nomad_b", ixmesh_inventory),("bellycum_unor_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["bellycum_body_hd_wet","bellycum_body_hd_wet", [("hanboot_nomad_b", ixmesh_inventory),("bellycum_body_hd_wet", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["bellycum_boobs_body","bellycum_boobs_body", [("hanboot_nomad_b", ixmesh_inventory),("bellycum_boobs_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["bellycum_ultraboobs_body","bellycum_ultraboobs_body", [("hanboot_nomad_b", ixmesh_inventory),("bellycum_ultraboobs_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["boobcum_noboob_body","boobcum_noboob_body", [("hanboot_nomad_b", ixmesh_inventory),("boobcum_noboob_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["boobcum_tiny_body","boobcum_tiny_body", [("hanboot_nomad_b", ixmesh_inventory),("boobcum_tiny_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["boobcum_flat_body","boobcum_flat_body", [("hanboot_nomad_b", ixmesh_inventory),("boobcum_flat_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["boobcum_light_body","boobcum_light_body", [("hanboot_nomad_b", ixmesh_inventory),("boobcum_light_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["boobcum_housemaid_body","boobcum_housemaid_body", [("hanboot_nomad_b", ixmesh_inventory),("boobcum_housemaid_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["boobcum_body_brown","boobcum_body_brown", [("hanboot_nomad_b", ixmesh_inventory),("boobcum_body_brown", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["boobcum_binyu_body","boobcum_binyu_body", [("hanboot_nomad_b", ixmesh_inventory),("boobcum_binyu_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["boobcum_balance_body","boobcum_balance_body", [("hanboot_nomad_b", ixmesh_inventory),("boobcum_balance_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["boobcum_normal_body","boobcum_normal_body", [("hanboot_nomad_b", ixmesh_inventory),("boobcum_normal_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["boobcum_unor_body","boobcum_unor_body", [("hanboot_nomad_b", ixmesh_inventory),("boobcum_unor_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["boobcum_body_hd_wet","boobcum_body_hd_wet", [("hanboot_nomad_b", ixmesh_inventory),("boobcum_body_hd_wet", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["boobcum_boobs_body","boobcum_boobs_body", [("hanboot_nomad_b", ixmesh_inventory),("boobcum_boobs_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["boobcum_ultraboobs_body","boobcum_ultraboobs_body", [("hanboot_nomad_b", ixmesh_inventory),("boobcum_ultraboobs_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["virginblood_noboob_body","virginblood_noboob_body", [("hanboot_nomad_b", ixmesh_inventory),("virginblood_noboob_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["virginblood_tiny_body","virginblood_tiny_body", [("hanboot_nomad_b", ixmesh_inventory),("virginblood_tiny_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["virginblood_flat_body","virginblood_flat_body", [("hanboot_nomad_b", ixmesh_inventory),("virginblood_flat_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["virginblood_light_body","virginblood_light_body", [("hanboot_nomad_b", ixmesh_inventory),("virginblood_light_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["virginblood_housemaid_body","virginblood_housemaid_body", [("hanboot_nomad_b", ixmesh_inventory),("virginblood_housemaid_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["virginblood_body_brown","virginblood_body_brown", [("hanboot_nomad_b", ixmesh_inventory),("virginblood_body_brown", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["virginblood_binyu_body","virginblood_binyu_body", [("hanboot_nomad_b", ixmesh_inventory),("virginblood_binyu_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["virginblood_balance_body","virginblood_balance_body", [("hanboot_nomad_b", ixmesh_inventory),("virginblood_balance_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["virginblood_normal_body","virginblood_normal_body", [("hanboot_nomad_b", ixmesh_inventory),("virginblood_normal_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["virginblood_unor_body","virginblood_unor_body", [("hanboot_nomad_b", ixmesh_inventory),("virginblood_unor_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["virginblood_body_hd_wet","virginblood_body_hd_wet", [("hanboot_nomad_b", ixmesh_inventory),("virginblood_body_hd_wet", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["virginblood_boobs_body","virginblood_boobs_body", [("hanboot_nomad_b", ixmesh_inventory),("virginblood_boobs_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["virginblood_ultraboobs_body","virginblood_ultraboobs_body", [("hanboot_nomad_b", ixmesh_inventory),("virginblood_ultraboobs_body", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,1, weight(3)|abundance(100)|leg_armor(36), imodbits_armor, []],
  ["light_body_rope","light_body_rope", [("light_body_rope", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["normal_body_rope","normal_body_rope", [("normal_body_rope", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["boobs_body_rope","boobs_body_rope", [("boobs_body_rope", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,1, weight(1)|abundance(100)|body_armor(55)|leg_armor(20), imodbits_none, []],
  ["fake_head_euro_1","head", [("fake_head_euro_1", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,1, weight(5)|abundance(100)|head_armor(45), imodbits_none, []],
  ["fake_head_euro_2","head", [("fake_head_euro_2", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,1, weight(5)|abundance(100)|head_armor(45), imodbits_none, []],
  ["fake_head_rome","head", [("fake_head_rome", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,1, weight(5)|abundance(100)|head_armor(45), imodbits_none, []],
  ["fake_head_asia_1","head", [("fake_head_asia_1", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,1, weight(5)|abundance(100)|head_armor(45), imodbits_none, []],
  ["fake_head_asia_2","head", [("fake_head_asia_2", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,1, weight(5)|abundance(100)|head_armor(45), imodbits_none, []],
  ["fake_head_brown_1","head", [("fake_head_brown_1", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,1, weight(5)|abundance(100)|head_armor(45), imodbits_none, []],
  ["fake_head_brown_2","head", [("fake_head_brown_2", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,1, weight(5)|abundance(100)|head_armor(45), imodbits_none, []],
  ["fake_head_arab_1","head", [("fake_head_arab_1", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,1, weight(5)|abundance(100)|head_armor(45), imodbits_none, []],
  ["fake_head_arab_2","head", [("fake_head_arab_2", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,1, weight(5)|abundance(100)|head_armor(45), imodbits_none, []],
  ["fake_head_afri_1","head", [("fake_head_afri_1", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,1, weight(5)|abundance(100)|head_armor(45), imodbits_none, []],
  ["fake_head_afri_2","head", [("fake_head_afri_2", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,1, weight(5)|abundance(100)|head_armor(45), imodbits_none, []],
  ["fake_head_etc_1","head", [("fake_head_etc_1", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,1, weight(5)|abundance(100)|head_armor(45), imodbits_none, []],
  ["test_item_1","test_item_1", [("invalid_item", 0)], itp_type_head_armor|itp_civilian|itp_fit_to_head|itp_covers_beard, 0,50, weight(1.75)|abundance(40)|head_armor(35)|difficulty(6), imodbits_armor|imodbit_cracked, []],
  ["test_item_2","test_item_2", [("invalid_item", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,11, weight(0.5)|abundance(100), imodbits_cloth, []],
  ["test_item_3","test_item_3", [("invalid_item", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,11, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, []],
  ["test_item_4","test_item_4", [("invalid_item", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,11, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, []],
  ["test_item_5","test_item_5", [("invalid_item", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,11, weight(0.5)|abundance(100), imodbits_cloth, []],
  ["test_item_6","test_item_6", [("invalid_item", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,11, weight(0.5)|abundance(100), imodbits_cloth, []],
  ["test_item_7","test_item_7", [("invalid_item", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,11, weight(0.5)|abundance(100), imodbits_cloth, []],
  ["test_item_8","test_item_8", [("invalid_item", 0)], itp_type_hand_armor, 0,888, weight(0.25)|abundance(50)|head_armor(35)|body_armor(45)|leg_armor(35), imodbits_none, []],
  ["test_item_9","test_item_9", [("invalid_item", 0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head, 0,580, weight(4)|abundance(10)|head_armor(70), imodbits_armor|imodbit_cracked, []],
  
  
    #DMK
  #Dismemberment DMK
    ["invisiblegloves","Invisiblegloves", [("invisiblegloves", 0)], itp_type_hand_armor, 0,550, weight(0)|abundance(5), imodbits_armor, []],
  #["looter_bully_handless_body","Ragged_Stolen_Brigandine", [("looter_bully_handless_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,27, weight(2)|abundance(5)|body_armor(27)|leg_armor(10), imodbits_none, []],
  #["looter_thug_armless_body","Ragged_Cloak", [("looter_thug_armless_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,27, weight(2)|abundance(5)|body_armor(27)|leg_armor(10), imodbits_none, []],
  #["thin_looter_armless_body","Leather_Outfit", [("thin_looter_armless_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,27, weight(2)|abundance(5)|body_armor(17)|leg_armor(6), imodbits_none, []],
  #["fat_peasant_handless_body","Large_Peasant_Apron", [("fat_peasant_handless_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,27, weight(2)|abundance(5)|body_armor(18)|leg_armor(8), imodbits_none, []],
  #["severedhand","Severed_Hand", [("severedhand", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,42, weight(2)|abundance(50)|body_armor(20)|hit_points(2)|spd_rtng(100)|shield_width(3), imodbits_none, []],
  #["fatseveredarm","Severed_Arm", [("fatseveredarm", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,42, weight(2)|abundance(50)|body_armor(25)|hit_points(10)|spd_rtng(100)|shield_width(8), imodbits_none, []],
  #["severedarm","Severed_Arm", [("severedarm", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,42, weight(2)|abundance(50)|body_armor(15)|hit_points(3)|spd_rtng(100)|shield_width(8), imodbits_none, []],

  
  ["invisible_head","Headless", [("invalid_item", 0)], itp_type_head_armor|itp_covers_head, 0,0, weight(4)|abundance(100), imodbits_armor|imodbit_cracked, []],
  ["cut_off_head_male","Bloody_Male_Head", [("cut_off_head_male", 0)], itp_type_head_armor|itp_covers_head, 0,0, weight(4)|abundance(100), imodbits_armor|imodbit_cracked, []],
  ["cut_off_head_female","Bloody_Female_Head", [("cut_off_head_female", 0)], itp_type_head_armor|itp_covers_head, 0,0, weight(4)|abundance(100), imodbits_armor|imodbit_cracked, []],
#  ["default_male_no_right_arm","Your_right_arm_is_missing!", [("man_body_right_arm_gone", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,0, weight(0)|abundance(5), imodbits_none, []],
#  ["default_male_no_left_arm","Your_left_arm_is_missing!", [("man_body_left_arm_gone", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,0, weight(0)|abundance(5), imodbits_none, []],
#  ["default_male_no_arms","Your_arms_are_missing!", [("man_body_both_arms_gone", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,0, weight(0)|abundance(5), imodbits_none, []],
#  ["supercrossbow","Semi-Automatic_Crossbow", [("crossbow_b", 0)], itp_type_crossbow|itp_two_handed|itp_primary|itp_extra_penetration, itcf_shoot_crossbow|itcf_carry_crossbow_back,10, weight(3)|abundance(10)|accuracy(240)|spd_rtng(68)|shoot_speed(110)|max_ammo(30)|thrust_damage(70, pierce), imodbits_crossbow, []],
#  ["super_bolts","Super_Bolts", [("bolt", 0),("bolt", ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_covers_legs|itp_doesnt_cover_hair, itcf_carry_quiver_right_vertical,10, weight(2)|abundance(5)|weapon_length(63)|max_ammo(200)|thrust_damage(60, pierce), imodbits_missile, []],
#  ["supersledge","Power-Sledge", [("maul_b", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itcf_carry_spear|itc_nodachi,1000, weight(10)|abundance(100)|hit_points(22528)|spd_rtng(100)|weapon_length(90)|thrust_damage(0, pierce)|swing_damage(150, blunt), imodbits_axe, []],
  #Dismemberment DMK
  
  ["test_item_10","test_item_10", [("invalid_item", 0)], itp_type_hand_armor, 0,888, weight(0.25)|abundance(50)|head_armor(35)|body_armor(45)|leg_armor(35), imodbits_none, []],
  
#  #DMK
#  #Dismemberment DMK
#    ["invisiblegloves","Invisiblegloves", [("invisiblegloves", 0)], itp_type_hand_armor, 0,550, weight(0)|abundance(5), imodbits_armor, []],
#  #["looter_bully_handless_body","Ragged_Stolen_Brigandine", [("looter_bully_handless_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,27, weight(2)|abundance(5)|body_armor(27)|leg_armor(10), imodbits_none, []],
#  #["looter_thug_armless_body","Ragged_Cloak", [("looter_thug_armless_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,27, weight(2)|abundance(5)|body_armor(27)|leg_armor(10), imodbits_none, []],
#  #["thin_looter_armless_body","Leather_Outfit", [("thin_looter_armless_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,27, weight(2)|abundance(5)|body_armor(17)|leg_armor(6), imodbits_none, []],
#  #["fat_peasant_handless_body","Large_Peasant_Apron", [("fat_peasant_handless_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,27, weight(2)|abundance(5)|body_armor(18)|leg_armor(8), imodbits_none, []],
#  #["severedhand","Severed_Hand", [("severedhand", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,42, weight(2)|abundance(50)|body_armor(20)|hit_points(2)|spd_rtng(100)|shield_width(3), imodbits_none, []],
#  #["fatseveredarm","Severed_Arm", [("fatseveredarm", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,42, weight(2)|abundance(50)|body_armor(25)|hit_points(10)|spd_rtng(100)|shield_width(8), imodbits_none, []],
#  #["severedarm","Severed_Arm", [("severedarm", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,42, weight(2)|abundance(50)|body_armor(15)|hit_points(3)|spd_rtng(100)|shield_width(8), imodbits_none, []],
#
#  
#  ["invisible_head","Headless", [("invalid_item", 0)], itp_type_head_armor|itp_covers_head, 0,0, weight(4)|abundance(100), imodbits_armor|imodbit_cracked, []],
#  ["cut_off_head_male","Bloody_Male_Head", [("cut_off_head_male", 0)], itp_type_head_armor|itp_covers_head, 0,0, weight(4)|abundance(100), imodbits_armor|imodbit_cracked, []],
#  ["cut_off_head_female","Bloody_Female_Head", [("cut_off_head_female", 0)], itp_type_head_armor|itp_covers_head, 0,0, weight(4)|abundance(100), imodbits_armor|imodbit_cracked, []],
##  ["default_male_no_right_arm","Your_right_arm_is_missing!", [("man_body_right_arm_gone", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,0, weight(0)|abundance(5), imodbits_none, []],
##  ["default_male_no_left_arm","Your_left_arm_is_missing!", [("man_body_left_arm_gone", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,0, weight(0)|abundance(5), imodbits_none, []],
##  ["default_male_no_arms","Your_arms_are_missing!", [("man_body_both_arms_gone", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,0, weight(0)|abundance(5), imodbits_none, []],
##  ["supercrossbow","Semi-Automatic_Crossbow", [("crossbow_b", 0)], itp_type_crossbow|itp_two_handed|itp_primary|itp_extra_penetration, itcf_shoot_crossbow|itcf_carry_crossbow_back,10, weight(3)|abundance(10)|accuracy(240)|spd_rtng(68)|shoot_speed(110)|max_ammo(30)|thrust_damage(70, pierce), imodbits_crossbow, []],
##  ["super_bolts","Super_Bolts", [("bolt", 0),("bolt", ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_covers_legs|itp_doesnt_cover_hair, itcf_carry_quiver_right_vertical,10, weight(2)|abundance(5)|weapon_length(63)|max_ammo(200)|thrust_damage(60, pierce), imodbits_missile, []],
##  ["supersledge","Power-Sledge", [("maul_b", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itcf_carry_spear|itc_nodachi,1000, weight(10)|abundance(100)|hit_points(22528)|spd_rtng(100)|weapon_length(90)|thrust_damage(0, pierce)|swing_damage(150, blunt), imodbits_axe, []],
#  #Dismemberment DMK
]