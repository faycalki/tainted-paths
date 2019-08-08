from header_sounds import *

sounds = [
 ("click", sf_2d|sf_vol_1,["bogus.ogg"]),

 ("tutorial_1", sf_2d|sf_vol_7,["tutorial_1.ogg"]),

 ("tutorial_2", sf_2d|sf_vol_7,["tutorial_2.ogg"]),

 ("gong", sf_2d|sf_priority_9|sf_vol_9, ["cymbal_01.wav"]),

 ("quest_taken", sf_2d|sf_priority_9|sf_vol_10, ["get_quest_01.wav"]),

 ("quest_completed", sf_2d|sf_priority_9|sf_vol_7, ["quest_completed.ogg"]),

 ("quest_succeeded", sf_2d|sf_priority_9|sf_vol_7, ["quest_succeeded.ogg"]),

 ("quest_concluded", sf_2d|sf_priority_9|sf_vol_7, ["quest_concluded.ogg"]),

 ("quest_failed", sf_2d|sf_priority_9|sf_vol_7, ["quest_failed.ogg"]),

 ("quest_cancelled", sf_2d|sf_priority_9|sf_vol_7, ["quest_cancelled.ogg"]),

# ("rain",sf_2d|sf_priority_10|sf_vol_13|sf_looping, ["rain_1.ogg"]), #Old
 ("rain",sf_2d|sf_priority_10|sf_vol_13|sf_looping, ["rain_1.ogg", "rain_medium_01R.wav", "rain_medium_01L.wav", "rain_light_01R.wav", "rain_heavy_01R.wav", "rain_heavy_01L.wav", "rain_hail_02R.wav", "rain_hail_02L.wav","rain_hail_01R.wav","rain_hail_01L.wav"]),

 ("money_received",sf_2d|sf_priority_10|sf_vol_6, ["coins_dropped_1.ogg"]),

 ("money_paid",sf_2d|sf_priority_10|sf_vol_10, ["coins_dropped_2.ogg"]),

 ("sword_clash_1", sf_priority_5|sf_vol_9,["sword_clank_metal_09.ogg","sword_clank_metal_09b.ogg","sword_clank_metal_10.ogg","sword_clank_metal_10b.ogg","sword_clank_metal_12.ogg","sword_clank_metal_12b.ogg","sword_clank_metal_13.ogg","sword_clank_metal_13b.ogg"]),

 ("sword_clash_2", sf_priority_5|sf_vol_9,["sword_clank_metal_09.ogg"]),

 ("sword_clash_3", sf_priority_5|sf_vol_9,["sword_clank_metal_12.ogg"]),

 ("sword_swing", sf_vol_4|sf_priority_2,["weapon_swing_01.wav","weapon_swing_02.wav","weapon_swing_03.wav","weapon_swing_04.wav","weapon_swing_05.wav","weapon_swing_06.wav","weapon_swing_07.wav","weapon_swing_08.wav","weapon_swing_09.wav","weapon_swing_10.wav","swoosh_01.wav","swoosh_02.wav","swoosh_03.wav","swoosh_04.wav","swoosh_05.wav","swoosh_06.wav","swoosh_07.wav","swoosh_08.wav","swoosh_09.wav","swoosh_10.wav"]),

 ("footstep_grass", sf_vol_13|sf_priority_1,["footstep_grass_light_01.wav","footstep_grass_light_02.wav","footstep_grass_light_03.wav","footstep_grass_light_04.wav","footstep_grass_light_05.wav","footstep_grass_light_06.wav","footstep_grass_light_07.wav","footstep_grass_light_08.wav","footstep_grass_light_09.wav","footstep_grass_light_10.wav","footstep_grass_light_11.wav","footstep_grass_light_12.wav","footstep_grass_light_13.wav","footstep_grass_light_14.wav","footstep_grass_light_15.wav"]),

 ("footstep_wood", sf_vol_15|sf_priority_1,["footstep_wood_light_01.wav","footstep_wood_light_02.wav","footstep_wood_light_03.wav","footstep_wood_light_04.wav","footstep_wood_light_05.wav","footstep_wood_light_06.wav","footstep_wood_light_07.wav","footstep_wood_light_08.wav","footstep_wood_light_09.wav","footstep_wood_light_10.wav"]),

# ("footstep_wood", sf_vol_3|sf_priority_1,["footstep_stone_1.wav","footstep_stone_3.wav","footstep_stone_4.wav"]),
 ("footstep_water", sf_vol_13|sf_priority_3,["footstep_water_01.wav","footstep_water_02.wav","footstep_water_03.wav","footstep_water_04.wav","footstep_water_05.wav","footstep_water_06.wav","footstep_water_07.wav","footstep_water_08.wav","footstep_water_09.wav","footstep_water_10.wav","Water_SSplash_01.wav","Water_SSplash_08.wav","Water_SSplash_09.wav","Water_SSplash_10.wav","Water_SSplash_12.wav"]),

 ("footstep_horse",sf_priority_3|sf_vol_15, ["footstep_horse_5.ogg","footstep_horse_2.ogg","footstep_horse_3.ogg","footstep_horse_4.ogg"]),

# ("footstep_horse",0, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
 ("footstep_horse_1b",sf_priority_3|sf_vol_15, ["s_footstep_horse_4b.ogg","s_footstep_horse_4f.ogg","s_footstep_horse_5b.ogg","s_footstep_horse_5f.ogg"]),

 ("footstep_horse_1f",sf_priority_3|sf_vol_15, ["s_footstep_horse_2b.ogg","s_footstep_horse_2f.ogg","s_footstep_horse_3b.ogg","s_footstep_horse_3f.ogg"]),

# ("footstep_horse_1f",sf_priority_3|sf_vol_15, ["footstep_horse_5.wav","footstep_horse_2.wav","footstep_horse_3.wav","footstep_horse_4.wav"]),
 ("footstep_horse_2b",sf_priority_3|sf_vol_15, ["s_footstep_horse_2b.ogg"]),

 ("footstep_horse_2f",sf_priority_3|sf_vol_15, ["s_footstep_horse_2f.ogg"]),

 ("footstep_horse_3b",sf_priority_3|sf_vol_15, ["s_footstep_horse_3b.ogg"]),

 ("footstep_horse_3f",sf_priority_3|sf_vol_15, ["s_footstep_horse_3f.ogg"]),

 ("footstep_horse_4b",sf_priority_3|sf_vol_15, ["s_footstep_horse_4b.ogg"]),

 ("footstep_horse_4f",sf_priority_3|sf_vol_15, ["s_footstep_horse_4f.ogg"]),

 ("footstep_horse_5b",sf_priority_3|sf_vol_15, ["s_footstep_horse_5b.ogg"]),

 ("footstep_horse_5f",sf_priority_3|sf_vol_15, ["s_footstep_horse_5f.ogg"]),

 ("jump_begin", sf_vol_7|sf_priority_9,["jump_light_b_01.wav","jump_light_b_02.wav","jump_light_b_03.wav"]),

 ("jump_end", sf_vol_5|sf_priority_9,["jump_light_e_01.wav","jump_light_e_02.wav"]),

 ("jump_begin_water", sf_vol_9|sf_priority_9,["water_jump_01.wav","water_jump_02.wav","water_jump_03.wav"]),

 ("jump_end_water", sf_vol_8|sf_priority_9,["water_splash_01.wav","water_splash_02.wav","water_splash_03.wav","water_splash_04.wav","water_splash_05.wav"]),

 ("horse_jump_begin", sf_vol_10|sf_priority_9,["horse_jump_b_01.wav","horse_jump_b_02.wav"]),

 ("horse_jump_end", sf_vol_10|sf_priority_9,["horse_jump_e_01.wav","horse_jump_e_02.wav"]),

 ("horse_jump_begin_water", sf_vol_10|sf_priority_9,["water_jump_large_01.wav","water_jump_large_02.wav","water_jump_large_03.wav"]),

 ("horse_jump_end_water", sf_vol_10|sf_priority_9,["water_splash_large_01.wav","water_splash_large_02.wav","water_splash_large_03.wav","water_splash_large_04.wav","water_splash_large_05.wav"]),







 ("release_bow",sf_vol_5, ["bow_shoot_01.wav","bow_shoot_02.wav","bow_shoot_03.wav","bow_shoot_04.wav","bow_shoot_05.wav","bow_shoot_06.wav","bow_shoot_07.wav","bow_shoot_08.wav","bow_shoot_09.wav","bow_shoot_10.wav"]),
 ("release_crossbow",sf_vol_7, ["crossbow_shoot_01.wav","crossbow_shoot_02.wav","crossbow_shoot_03.wav","crossbow_shoot_04.wav","crossbow_shoot_05.wav","crossbow_shoot_06.wav", "Crossbow_Fire_07.wav", "Crossbow_Fire_08.wav", "Crossbow_Fire_10.wav", "Crossbow_Fire_11.wav", "Crossbow_Fire_12.wav", "Crossbow_Fire_13.wav", "Crossbow_Fire_14.wav",  "Crossbow_Fire_15.wav"]),
 ("throw_javelin",sf_vol_5, ["throw_javelin_01.wav","throw_javelin_02.wav","throw_javelin_03.wav"]),
 ("throw_axe",sf_vol_7, ["throw_axe_1.ogg"]),

 ("throw_knife",sf_vol_5, ["throw_knife_01.wav","throw_knife_02.wav","throw_knife_03.wav","throw_knife_04.wav"]),

 ("throw_stone",sf_vol_5, ["throw_stone_01.wav","throw_stone_02.wav","throw_stone_03.wav"]),



 ("reload_crossbow",sf_vol_3, ["pull_crossbow_string_01.wav","pull_crossbow_string_02.wav","pull_crossbow_string_03.wav","pull_crossbow_string_04.wav","pull_crossbow_string_05.wav"]),
 ("reload_crossbow_continue",sf_vol_6, ["put_back_dagger.ogg"]),

 ("pull_bow",sf_vol_10, ["pull_bow_string_01.wav","pull_bow_string_02.wav","pull_bow_string_03.wav","pull_bow_string_04.wav","pull_bow_string_05.wav"]),

 ("pull_arrow",sf_vol_5, ["draw_arrow_01.wav","draw_arrow_02.wav","draw_arrow_03.wav"]),


















































































































 ("arrow_pass_by",sf_priority_7|sf_vol_4, ["arrow_pass_01.wav","arrow_pass_02.wav","arrow_pass_03.wav","arrow_pass_04.wav","arrow_pass_05.wav","arrow_pass_06.wav","arrow_pass_07.wav","arrow_pass_08.wav","arrow_pass_09.wav","arrow_pass_10.wav","arrow_fly_01.wav","arrow_fly_02.wav","arrow_fly_03.wav","arrow_fly_04.wav","arrow_fly_05.wav","arrow_fly_06.wav","arrow_fly_08.wav","arrow_fly_10.wav","arrow_fly_11.wav","arrow_fly_12.wav","arrow_fly_13.wav","arrow_fly_14.wav","arrow_fly_15.wav","arrow_fly_16.wav","arrow_fly_17.wav","arrow_fly_18.wav","arrow_fly_19.wav","arrow_fly_20.wav"]),
 ("bolt_pass_by",sf_priority_7|sf_vol_4, ["bolt_pass_01.wav","bolt_pass_02.wav","bolt_pass_03.wav","bolt_pass_04.wav","bolt_pass_05.wav","bolt_pass_06.wav","bolt_pass_07.wav","bolt_pass_08.wav", "crossbow_fly_09.wav", "crossbow_fly_10.wav", "crossbow_fly_11.wav", "crossbow_fly_12.wav", "crossbow_fly_13.wav", "crossbow_fly_14.wav", "crossbow_fly_15.wav"]),
 ("javelin_pass_by",sf_priority_7, ["javelin_pass_by_1.ogg","javelin_pass_by_2.ogg"]),
 ("stone_pass_by",sf_vol_9|sf_priority_7, ["stone_pass_01.wav","stone_pass_02.wav","stone_pass_03.wav"]),
 ("axe_pass_by",sf_priority_7, ["axe_pass_by_1.ogg"]),
 ("knife_pass_by",sf_priority_7, ["knife_pass_01.wav","knife_pass_02.wav","knife_pass_03.wav","knife_pass_04.wav"]),
	("bullet_pass_by", sf_priority_9, ["bullet_pass_01.ogg", "bullet_pass_02.ogg", "bullet_pass_03.ogg", "bullet_pass_04.ogg", "bullet_pass_05.ogg", "bullet_pass_06.ogg", "bullet_pass_07.ogg", "bullet_pass_08.ogg", "bullet_pass_09.ogg", "bullet_pass_10.ogg", "bullet_pass_11.ogg", "bullet_pass_12.ogg"]),


 ("incoming_arrow_hit_ground",sf_priority_7|sf_vol_14, ["arrow_ground_01.wav","arrow_ground_02.wav","arrow_ground_03.wav","arrow_ground_04.wav","arrow_ground_05.wav","arrow_ground_06.wav","arrow_ground_07.wav","arrow_ground_08.wav"]),
 ("incoming_bolt_hit_ground",sf_priority_7|sf_vol_14, ["bolt_ground_01.wav","bolt_ground_02.wav","bolt_ground_03.wav","bolt_ground_04.wav","bolt_ground_05.wav","bolt_ground_06.wav","bolt_ground_07.wav","bolt_ground_08.wav"]),
 ("incoming_javelin_hit_ground",sf_priority_7|sf_vol_14, ["javelin_ground_01.wav","javelin_ground_02.wav","javelin_ground_03.wav"]),
 ("incoming_stone_hit_ground",sf_priority_7|sf_vol_14, ["stone_ground_01.wav","stone_ground_02.wav","stone_ground_03.wav"]),
 ("incoming_axe_hit_ground",sf_priority_7|sf_vol_14, ["axe_ground_01.wav","axe_ground_02.wav","axe_ground_03.wav"]),
 ("incoming_knife_hit_ground",sf_priority_7|sf_vol_14, ["knife_ground_01.wav","knife_ground_02.wav","knife_ground_03.wav"]),
	("incoming_bullet_hit_ground", sf_priority_9|sf_vol_7, ["bullet_ric_01.ogg", "bullet_ric_02.ogg", "bullet_ric_03.ogg", "bullet_ric_04.ogg", "bullet_ric_05.ogg", "bullet_ric_06.ogg", "bullet_ric_07.ogg", "bullet_ric_08.ogg"]),

 ("outgoing_arrow_hit_ground",sf_priority_7|sf_vol_14, ["arrow_ground_01.wav","arrow_ground_02.wav","arrow_ground_03.wav","arrow_ground_04.wav","arrow_ground_05.wav","arrow_ground_06.wav","arrow_ground_07.wav","arrow_ground_08.wav"]),
 ("outgoing_bolt_hit_ground",sf_priority_7|sf_vol_14,  ["bolt_ground_01.wav","bolt_ground_02.wav","bolt_ground_03.wav","bolt_ground_04.wav","bolt_ground_05.wav","bolt_ground_06.wav","bolt_ground_07.wav","bolt_ground_08.wav"]),
 ("outgoing_javelin_hit_ground",sf_priority_7|sf_vol_15, ["javelin_ground_01.wav","javelin_ground_02.wav","javelin_ground_03.wav"]),
 ("outgoing_stone_hit_ground",sf_priority_7|sf_vol_14, ["stone_ground_01.wav","stone_ground_02.wav","stone_ground_03.wav"]),
 ("outgoing_axe_hit_ground",sf_priority_7|sf_vol_14, ["axe_ground_01.wav","axe_ground_02.wav","axe_ground_03.wav"]),
 ("outgoing_knife_hit_ground",sf_priority_7|sf_vol_14, ["knife_ground_01.wav","knife_ground_02.wav","knife_ground_03.wav"]),
	("outgoing_bullet_hit_ground", sf_priority_9|sf_vol_7, ["bullet_ric_01.ogg", "bullet_ric_02.ogg", "bullet_ric_03.ogg", "bullet_ric_04.ogg", "bullet_ric_05.ogg", "bullet_ric_06.ogg", "bullet_ric_07.ogg", "bullet_ric_08.ogg"]),





 ("draw_sword",sf_priority_2, ["draw_sword_02.wav","draw_sword_03.wav"]),
 ("put_back_sword",sf_priority_1, ["put_away_sword_01.wav"]),
 ("draw_greatsword",sf_priority_2, ["draw_greatsword_01.wav","draw_greatsword_03.wav"]),
 ("put_back_greatsword",sf_priority_1, ["put_away_greatsword_01.wav"]),
 ("draw_axe",sf_priority_2, ["draw_axe_01.wav","draw_axe_02.wav"]),
 ("put_back_axe",sf_priority_1, ["put_away_axe_01.wav"]),
 ("draw_greataxe",sf_priority_2, ["draw_greataxe_01.wav","draw_greataxe_02.wav"]),
 ("put_back_greataxe",sf_priority_1, ["put_away_greataxe_01.wav"]),
 ("draw_spear",sf_priority_2, ["draw_spear_01.wav","draw_spear_02.wav"]),
 ("put_back_spear",sf_priority_1, ["put_away_spear_01.wav"]),
 ("draw_crossbow",sf_priority_2|sf_vol_6, ["draw_crossbow_01.wav","draw_crossbow_02.wav"]),
 ("put_back_crossbow",sf_priority_1, ["put_away_crossbow_01.wav"]),
 ("draw_revolver",sf_priority_2, ["draw_from_holster.ogg"]),
 ("put_back_revolver",sf_priority_1, ["put_back_to_holster.ogg"]),
 ("draw_dagger",sf_priority_2, ["draw_dagger_01.wav","draw_dagger_02.wav"]),
 ("put_back_dagger",sf_priority_1, ["put_away_dagger_01.wav"]),
 ("draw_bow",sf_priority_2, ["draw_bow_01.wav","draw_bow_02.wav"]),
 ("put_back_bow",sf_priority_1, ["put_away_bow_01.wav"]),
 ("draw_shield",sf_priority_2|sf_vol_7, ["draw_shield_01.wav","draw_shield_02.wav"]),
 ("put_back_shield",sf_priority_1|sf_vol_7, ["put_away_shield_01.wav"]),
 ("draw_other",sf_priority_2, ["draw_other.ogg"]),
 ("put_back_other",sf_priority_1, ["draw_other2.ogg"]),


 ("body_fall_small",sf_priority_5|sf_vol_10, ["body_fall_small_01.wav","body_fall_small_02.wav","body_fall_small_03.wav","body_fall_small_04.wav","body_fall_small_05.wav","body_fall_small_06.wav","body_fall_small_07.wav","body_fall_small_08.wav", "Fall_Infantry_Grass_07.wav", "Fall_Infantry_Snow_01.wav", "Fall_Infantry_Snow_02.wav", "Fall_Infantry_Snow_03.wav"]),
 ("body_fall_big",sf_priority_6|sf_vol_10, ["body_fall_large_01.wav","body_fall_large_02.wav","body_fall_large_03.wav","body_fall_large_04.wav","body_fall_large_05.wav","body_fall_large_06.wav","body_fall_large_07.wav","body_fall_large_08.wav", "Fall_Infantry_Grass_03.wav", "Fall_Infantry_Grass_04.wav", "Fall_Infantry_Grass_05.wav", "Fall_Infantry_Grass_06.wav"]),
# ("body_fall_very_big",sf_priority_9|sf_vol_10, ["body_fall_very_big_1.wav"]),
 ("horse_body_fall_begin",sf_priority_6|sf_vol_10, ["horse_fall_b_01.wav","horse_fall_b_02.wav","horse_fall_b_03.wav"]),
 ("horse_body_fall_end",sf_priority_6|sf_vol_10, ["horse_fall_e_01.wav","horse_fall_e_02.wav","horse_fall_e_03.wav", "Fall_horse_grass_01.wav","Fall_horse_grass_02.wav","Fall_horse_grass_05.wav"]),
 
## ("clang_metal",sf_priority_9, ["clang_metal_1.ogg","clang_metal_2.ogg","s_swordClash1.wav","s_swordClash2.wav","s_swordClash3.wav"]),
 ("hit_wood_wood",sf_priority_7|sf_vol_10, ["wpn_impact_blunt2hand_wood_01.ogg", "wpn_impact_blunt2hand_wood_02.ogg", "wpn_impact_blunt2hand_wood_03.ogg", "wpn_impact_blunt_wood_01.ogg", "wpn_impact_blunt_wood_02.ogg", "wpn_impact_blunt_wood_03.ogg","wood_on_wood_01.wav","wood_on_wood_02.wav","wood_on_wood_03.wav","wood_on_wood_04.wav","wood_on_wood_05.wav","wood_on_wood_06.wav","wood_on_wood_07.wav","wood_on_wood_08.wav"]),#dummy
 ("hit_metal_metal",sf_priority_7|sf_vol_9, ["swordclash_01.ogg", "swordclash_02.ogg", "swordclash_03.ogg", "swordclash_04.ogg", "swordclash_05.ogg", "swordclash_06.ogg", "swordclash_07.ogg", "swordclash_08.ogg", "wpn_bash_blade_01.ogg", "wpn_bash_blade_02.ogg","Sword_clash_01.wav","Sword_clash_02.wav","Sword_clash_03.wav","Sword_clash_04.wav","Sword_clash_05.wav","Sword_clash_06.wav","Sword_clash_07.wav","Sword_clash_08.wav","Sword_clash_09.wav","Sword_clash_10.wav","Sword_clash_11.wav","Sword_clash_12.wav","Sword_clash_13.wav","Sword_clash_14.wav","Sword_clash_15.wav"]),
 ("hit_wood_metal",sf_priority_7|sf_vol_10, ["fx_melee_sword_wood_02.ogg", "fx_melee_sword_wood_01.ogg","metal_on_wood_01.wav","metal_on_wood_02.wav","metal_on_wood_03.wav","metal_on_wood_04.wav","metal_on_wood_05.wav","metal_on_wood_06.wav","metal_on_wood_07.wav","metal_on_wood_08.wav","metal_on_wood_09.wav","metal_on_wood_10.wav"]),
# ("clang_metal", sf_priority_9,["sword_clank_metal_09.wav","sword_clank_metal_10.wav","sword_clank_metal_12.wav","sword_clank_metal_13.wav"]),
## ("shield_hit_cut",sf_priority_5, ["shield_hit_cut_3.wav","shield_hit_cut_4.wav","shield_hit_cut_5.wav"]),
# ("clang_metal", sf_priority_9,["sword_clank_metal_09.ogg","sword_clank_metal_10.ogg","sword_clank_metal_12.ogg","sword_clank_metal_13.ogg"]),
## ("shield_hit_cut",sf_priority_5, ["shield_hit_cut_3.ogg","shield_hit_cut_4.ogg","shield_hit_cut_5.ogg"]),
 ("shield_hit_wood_wood",sf_priority_7|sf_vol_10, ["wpn_bash_shield_light_01.ogg", "wpn_bash_shield_light_02.ogg","shield_wood_wood_01.wav","shield_wood_wood_02.wav","shield_wood_wood_03.wav","shield_wood_wood_04.wav","shield_wood_wood_05.wav","shield_wood_wood_06.wav","shield_wood_wood_07.wav","shield_wood_wood_08.wav","shield_wood_wood_09.wav","shield_wood_wood_10.wav","shield_wood_wood_11.wav","shield_wood_wood_12.wav"]),
 ("shield_hit_metal_metal",sf_priority_7|sf_vol_10, ["wpn_bash_shield_heavy_01.ogg", "wpn_bash_shield_heavy_02.ogg", "wpn_bash_shield_heavy_03.ogg", "wpn_impact_blade_metal_01.ogg","wpn_impact_blade_metal_02.ogg","wpn_impact_blade_metal_03.ogg","shield_metal_metal_01.wav","shield_metal_metal_02.wav","shield_metal_metal_03.wav","shield_metal_metal_04.wav","shield_metal_metal_05.wav","shield_metal_metal_06.wav","shield_metal_metal_07.wav","shield_metal_metal_08.wav","shield_metal_metal_09.wav","shield_metal_metal_10.wav","shield_metal_metal_11.wav","shield_metal_metal_12.wav"]),
 ("shield_hit_wood_metal",sf_priority_7|sf_vol_10, ["wpn_bash_bow_01.ogg", "wpn_bash_bow_02.ogg", "wpn_bash_bow_03.ogg", "fx_melee_metalimpactlarge_flesh_01.ogg", "fx_melee_metalimpactlarge_flesh_02.ogg", "shield_metal_wood_01.wav","shield_metal_wood_02.wav","shield_metal_wood_03.wav","shield_metal_wood_04.wav","shield_metal_wood_05.wav","shield_metal_wood_06.wav","shield_metal_wood_07.wav","shield_metal_wood_08.wav","shield_metal_wood_09.wav","shield_metal_wood_10.wav"]), #(shield is wood)
 ("shield_hit_metal_wood",sf_priority_7|sf_vol_10, ["wpn_bash_shield_light_02.ogg","wpn_bash_shield_light_01.ogg","shield_wood_metal_01.wav","shield_wood_metal_02.wav","shield_wood_metal_03.wav","shield_wood_metal_04.wav","shield_wood_metal_05.wav","shield_wood_metal_06.wav","shield_wood_metal_07.wav","shield_wood_metal_08.wav"]),#(shield is metal)
 ("shield_broken",sf_priority_9, ["obj_cwbarricade_destroyed.ogg","shield_break_01.wav","shield_break_02.wav"]), #   #DMK ADDED HERE ("shield_broken", sf_priority_9, ["shield_broken.ogg", "shield_broken1.ogg", "shield_broken2.ogg"]), #heree  ("shield_broken", sf_priority_9, ["shield_broken.ogg", "shield_broken1.ogg", "shield_broken2.ogg"]),
 #("man_hit",sf_priority_7|sf_vol_7, ["man_hit_5.ogg","man_hit_6.ogg","man_hit_7.ogg","man_hit_8.ogg","man_hit_9.ogg","man_hit_10.ogg","man_hit_11.ogg","man_hit_12.ogg","man_hit_13.ogg","man_hit_14.ogg","man_hit_15.ogg","man_hit_17.ogg","man_hit_18.ogg","man_hit_19.ogg","man_hit_22.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg","man_hit_59.ogg"]),
 #Disabled due to no sounds("man_hit",sf_priority_7|sf_vol_10, ["man_grunt_pain_01.wav","man_grunt_pain_02.wav","man_grunt_pain_03.wav","man_grunt_pain_04.wav","man_grunt_pain_05.wav","man_grunt_pain_06.wav","man_grunt_pain_07.wav","man_grunt_pain_08.wav","man_grunt_pain_09.wav","man_grunt_pain_10.wav","man_grunt_pain_11.wav","man_grunt_pain_12.wav","man_grunt_pain_13.wav","man_grunt_pain_14.wav","man_grunt_pain_15.wav","man_grunt_pain_16.wav","man_grunt_pain_17.wav","man_grunt_pain_18.wav","man_grunt_pain_19.wav","man_grunt_pain_20.wav"]),
 ("man_die",sf_priority_10|sf_vol_10,  ["man_die_01.ogg","man_die_02.ogg","man_die_03.ogg","man_die_04.ogg","man_die_05.ogg","man_die_06.ogg","man_die_07.ogg","man_die_08.ogg","man_die_09.ogg","man_die_10.ogg","man_die_11.ogg","man_die_12.ogg","man_die_13.ogg","man_die_14.ogg","man_die_15.ogg","man_die_16.ogg","man_die_17.ogg","man_die_18.ogg","man_die_19.ogg","man_die_20.ogg","man_die_21.ogg","man_die_22.ogg","man_die_23.ogg","man_die_24.ogg","man_die_25.ogg","man_die_26.ogg","man_die_27.ogg","man_die_28.ogg","man_die_29.ogg","man_die_30.ogg","man_die_31.ogg","man_die_32.ogg"]),
 #("woman_hit",sf_priority_7, ["woman_hit_2.ogg","woman_hit_3.ogg","woman_hit_b_2.ogg","woman_hit_b_4.ogg","woman_hit_b_6.ogg","woman_hit_b_7.ogg","woman_hit_b_8.ogg","woman_hit_b_11.ogg","woman_hit_b_14.ogg","woman_hit_b_16.ogg"]),
 #("woman_die",sf_priority_10, ["woman_fall_1.ogg","woman_hit_b_5.ogg", "Death_Hit_01.mp3", "Death_Hit_02.mp3", "Death_Hit_03.mp3", "Death_Hit_04.mp3", "Death_Hit_05.mp3", "Death_Hit_06.mp3", "Death_Hit_07.mp3", "Death_Hit_08.mp3", "Death_Hit_09.mp3", "Death_Hits_01.mp3", "Death_Hits_02.mp3", "Death_Hits_03.mp3", "Death_Hits_04.mp3", "Death_Hits_05.mp3"]),
  ("woman_die",sf_priority_10, ["woman_fall_1.ogg","woman_hit_b_5.ogg"]),
 #("woman_yell",sf_priority_8|sf_vol_10, ["woman_yell_1.ogg","woman_yell_2.ogg"]),
 ("hide",0, ["s_hide.wav"]),
 ("unhide",0, ["s_unhide.wav"]),
 ("neigh",0, ["horse_exterior_whinny_01.ogg","horse_exterior_whinny_02.ogg","horse_exterior_whinny_03.ogg","horse_exterior_whinny_04.ogg","horse_exterior_whinny_05.ogg","horse_whinny.ogg"]),

 ("gallop",sf_vol_3, ["horse_gallop_04.wav","horse_gallop_05.wav","horse_gallop_06.wav"]),

 ("battle",sf_vol_4, ["Group_Fight_Medium.wav", "Group_Fight_Small.wav"]),

# ("bow_shoot_player",sf_priority_10|sf_vol_10, ["bow_shoot_4.ogg"]),
# ("bow_shoot",sf_priority_4, ["bow_shoot_4.ogg"]),
# ("crossbow_shoot",sf_priority_4, ["bow_shoot_2.ogg"]),
 ("arrow_hit_body",sf_priority_4, ["missile_flesh_01.wav","missile_flesh_02.wav","missile_flesh_03.wav","missile_flesh_04.wav","missile_flesh_05.wav","missile_flesh_06.wav","missile_flesh_07.wav","missile_flesh_08.wav","Arrow_Hit_flesh_01.wav","Arrow_Hit_flesh_02.wav","Arrow_Hit_flesh_03.wav","Arrow_Hit_flesh_04.wav","Arrow_Hit_flesh_05.wav","Arrow_Hit_flesh_06.wav","Arrow_Hit_flesh_07.wav","Arrow_Hit_flesh_08.wav","Arrow_Hit_flesh_09.wav","Arrow_Hit_flesh_10.wav","Arrow_Hit_flesh_11.wav","Arrow_Hit_flesh_12.wav","Arrow_Hit_flesh_13.wav","Arrow_Hit_flesh_14.wav","Arrow_Hit_flesh_15.wav","Arrow_Hit_flesh_16.wav","Arrow_Hit_flesh_17.wav"]),

 ("metal_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["metal_low_low_01.wav","metal_low_low_02.wav","metal_low_low_03.wav","metal_low_low_04.wav","metal_low_low_05.wav","metal_low_low_06.wav","metal_low_low_07.wav","metal_low_low_08.wav"]),

 ("metal_hit_low_armor_high_damage",sf_priority_5|sf_vol_10, ["metal_low_high_01.wav","metal_low_high_02.wav","metal_low_high_03.wav","metal_low_high_04.wav","metal_low_high_05.wav","metal_low_high_06.wav","metal_low_high_07.wav","metal_low_high_08.wav","metal_low_high_09.wav","sword_flesh_hit_01.wav","sword_flesh_hit_02.wav","sword_flesh_hit_03.wav","sword_flesh_hit_04.wav","sword_flesh_hit_05.wav","sword_flesh_hit_07.wav","sword_flesh_hit_08.wav","sword_flesh_hit_09.wav","sword_flesh_hit_10.wav","sword_flesh_hit_11.wav","sword_flesh_hit_12.wav","sword_flesh_hit_13.wav","sword_flesh_hit_14.wav","sword_flesh_hit_15.wav","sword_flesh_hit_16.wav","sword_flesh_hit_17.wav","sword_flesh_hit_18.wav"]),

 ("metal_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["metal_high_low_01.wav","metal_high_low_02.wav","metal_high_low_03.wav","metal_high_low_04.wav","metal_high_low_05.wav","metal_high_low_06.wav","metal_high_low_07.wav","metal_high_low_08.wav","metal_high_low_09.wav","metal_high_low_10.wav","metal_high_low_11.wav","metal_high_low_12.wav","metal_high_low_13.wav","metal_high_low_14.wav","metal_high_low_15.wav","metal_high_low_16.wav","metal_high_low_17.wav","metal_high_low_18.wav","metal_high_low_19.wav","metal_high_low_20.wav","metal_high_low_21.wav","metal_high_low_22.wav","metal_high_low_23.wav","metal_high_low_24.wav","metal_high_low_25.wav"]),

 ("metal_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["metal_high_high_01.wav","metal_high_high_02.wav","metal_high_high_03.wav","metal_high_high_04.wav","metal_high_high_05.wav","metal_high_high_06.wav","metal_high_high_07.wav","metal_high_high_08.wav","metal_high_high_09.wav","metal_high_high_10.wav","metal_high_high_11.wav","metal_high_high_12.wav","metal_high_high_13.wav","metal_high_high_14.wav","metal_high_high_15.wav","metal_high_high_16.wav","metal_high_high_17.wav","metal_high_high_18.wav","metal_high_high_19.wav","metal_high_high_20.wav","metal_high_high_21.wav","metal_high_high_22.wav","metal_high_high_23.wav","metal_high_high_24.wav","metal_high_high_25.wav","metal_high_high_26.wav","metal_high_high_27.wav","metal_high_high_28.wav","metal_high_high_29.wav","metal_high_high_30.wav","metal_high_high_31.wav","metal_high_high_32.wav"]),

 ("wooden_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["blunt_low_low_01.wav","blunt_low_low_02.wav","blunt_low_low_03.wav","blunt_low_low_04.wav","blunt_low_low_05.wav","blunt_low_low_06.wav","blunt_low_low_07.wav","blunt_low_low_08.wav","blunt_low_low_09.wav","blunt_low_low_10.wav"]),

 ("wooden_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_low_high_01.wav","blunt_low_high_02.wav","blunt_low_high_03.wav","blunt_low_high_04.wav","blunt_low_high_05.wav","blunt_low_high_06.wav","blunt_low_high_07.wav","blunt_low_high_08.wav","blunt_low_high_09.wav","blunt_low_high_10.wav","blunt_low_high_11.wav","blunt_low_high_12.wav","blunt_low_high_13.wav"]),

 ("wooden_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["blunt_high_low_01.wav","blunt_high_low_02.wav","blunt_high_low_03.wav","blunt_high_low_04.wav","blunt_high_low_05.wav","blunt_high_low_06.wav","blunt_high_low_07.wav","blunt_high_low_08.wav","blunt_high_low_09.wav","blunt_high_low_10.wav"]),

 ("wooden_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_high_high_01.wav","blunt_high_high_02.wav","blunt_high_high_03.wav","blunt_high_high_04.wav","blunt_high_high_05.wav","blunt_high_high_06.wav","blunt_high_high_07.wav","blunt_high_high_08.wav","blunt_high_high_09.wav","blunt_high_high_10.wav","blunt_high_high_11.wav","blunt_high_high_12.wav","blunt_high_high_13.wav","blunt_high_high_14.wav","blunt_high_high_15.wav","blunt_high_high_16.wav","blunt_high_high_17.wav","blunt_high_high_18.wav","blunt_high_high_19.wav","blunt_high_high_20.wav","blunt_high_high_21.wav","blunt_high_high_22.wav"]),

 ("mp_arrow_hit_target",sf_2d|sf_priority_15|sf_vol_9, ["mp_arrow_hit_target.wav"]),

 ("blunt_hit",sf_priority_5|sf_vol_10, ["fx_melee_punchmedium_01.ogg", "fx_melee_punchmedium_02.ogg", "fx_melee_punchmedium_03.ogg", "fx_melee_punchlarge_01.ogg", "fx_melee_punchlarge_02.ogg", "fx_melee_punchlarge_03.ogg","horse_charge_01.wav","horse_charge_02.wav","horse_charge_03.wav","horse_charge_04.wav","horse_charge_05.wav","horse_charge_06.wav","horse_charge_07.wav","horse_charge_08.wav"]),

 ("player_hit_by_arrow",sf_priority_10|sf_vol_10, ["player_hit_by_arrow.ogg"]),

	("pistol_shot", sf_priority_9|sf_vol_15, ["stw2_gun_breechload_rifle_shot_01_adpcm_gme.wav", "stw2_gun_breechload_rifle_shot_02_adpcm_gme.wav", "stw2_gun_breechload_rifle_shot_04_adpcm_gme.wav", "stw2_gun_breechload_rifle_shot_05_adpcm_gme.wav", "stw2_gun_breechload_rifle_shot_06_adpcm_gme.wav", "stw2_gun_breechload_rifle_shot_08_adpcm_gme.wav", "stw2_gun_breechload_rifle_shot_09_adpcm_gme.wav", "stw2_gun_breechload_rifle_shot_12_adpcm_gme.wav","stw2_gun_breechload_rifle_shot_13_adpcm_gme.wav","stw2_gun_breechload_rifle_shot_14_adpcm_gme.wav","stw2_gun_breechload_rifle_shot_15_adpcm_gme.wav","stw2_gun_breechload_rifle_shot_17_adpcm_gme.wav","stw2_gun_rifle_shot_01_adpcm_gme.wav","stw2_gun_rifle_shot_02_adpcm_gme.wav","stw2_gun_rifle_shot_03_adpcm_gme.wav","stw2_gun_rifle_shot_04_adpcm_gme.wav","stw2_gun_rifle_shot_05_adpcm_gme.wav","stw2_gun_rifle_shot_06_adpcm_gme.wav","stw2_gun_rifle_shot_07_adpcm_gme.wav","stw2_gun_rifle_shot_12_adpcm_gme.wav","stw2_gun_rifle_shot_13_adpcm_gme.wav","stw2_gun_rifle_shot_14_adpcm_gme.wav","stw2_gun_rifle_shot_15_adpcm_gme.wav","stw2_gun_rifle_shot_16_adpcm_gme.wav","stw2_gun_rifle_shot_17_adpcm_gme.wav","stw2_gun_rifle_shot_18_adpcm_gme.wav", "stw2_gun_breechload_rifle_shot_11_adpcm_gme.wav"]),





















































































 #("man_grunt",sf_priority_6|sf_vol_4, ["man_ugh_01.wav","man_ugh_02.wav","man_ugh_03.wav","man_ugh_04.wav","man_ugh_05.wav","man_ugh_06.wav","man_ugh_07.wav","man_ugh_08.wav","man_ugh_09.wav","man_ugh_10.wav"]),
 
 #Not supposed to be used at all
 ("man_grunt", sf_priority_3|sf_vol_3, ["man_heavy_grunt_01.ogg", "man_heavy_grunt_02.ogg", "man_heavy_grunt_03.ogg", "man_heavy_grunt_04.ogg", "man_heavy_grunt_05.ogg", "man_heavy_grunt_06.ogg", "man_heavy_grunt_07.ogg", "man_heavy_grunt_08.ogg", "man_heavy_grunt_09.ogg", "man_heavy_grunt_10.ogg", "man_heavy_grunt_11.ogg", "man_heavy_grunt_12.ogg", "man_heavy_grunt_13.ogg", "man_heavy_grunt_14.ogg", "man_heavy_grunt_15.ogg"]),
 #Not supposed to be used at all
 

 ("man_breath_hard",sf_priority_3|sf_vol_8, ["man_ugh_01.wav","man_ugh_02.wav","man_ugh_03.wav","man_ugh_04.wav","man_ugh_05.wav","man_ugh_06.wav","man_ugh_07.wav","man_ugh_08.wav","man_ugh_09.wav","man_ugh_10.wav"]),
 ("man_stun",sf_priority_3|sf_vol_9, ["man_short_grunt_01.wav","man_short_grunt_02.wav"]),
 #OLD("man_grunt_long",sf_priority_6|sf_vol_8, ["man_yell_01.wav","man_yell_02.wav","man_yell_03.wav","man_yell_04.wav","man_yell_05.wav","man_yell_06.wav","man_yell_07.wav","man_yell_08.wav","man_yell_09.wav","man_yell_10.wav","man_yell_11.wav","man_yell_12.wav","man_yell_13.wav","man_yell_14.wav","man_yell_15.wav","man_yell_16.wav","man_yell_17.wav","man_yell_18.wav","man_yell_19.wav","man_yell_20.wav","man_yell_21.wav","man_yell_22.wav","man_yell_23.wav","man_yell_24.wav","man_yell_25.wav","man_yell_26.wav","man_yell_27.wav","man_yell_28.wav","man_yell_29.wav","man_yell_30.wav"]),
 ("man_grunt_long", sf_priority_3|sf_vol_7, ["man_heavy_grunt_01.ogg", "man_heavy_grunt_02.ogg", "man_heavy_grunt_03.ogg", "man_heavy_grunt_04.ogg", "man_heavy_grunt_05.ogg", "man_heavy_grunt_06.ogg", "man_heavy_grunt_07.ogg", "man_heavy_grunt_08.ogg", "man_heavy_grunt_09.ogg", "man_heavy_grunt_10.ogg", "man_heavy_grunt_11.ogg", "man_heavy_grunt_12.ogg", "man_heavy_grunt_13.ogg", "man_heavy_grunt_14.ogg", "man_heavy_grunt_15.ogg"]),
 #("man_yell",sf_priority_5|sf_vol_5, ["man_yell_01.wav","man_yell_02.wav","man_yell_03.wav","man_yell_04.wav","man_yell_05.wav","man_yell_06.wav","man_yell_07.wav","man_yell_08.wav","man_yell_09.wav","man_yell_10.wav","man_yell_11.wav","man_yell_12.wav","man_yell_13.wav","man_yell_14.wav","man_yell_15.wav","man_yell_16.wav","man_yell_17.wav","man_yell_18.wav","man_yell_19.wav","man_yell_20.wav","man_yell_21.wav","man_yell_22.wav","man_yell_23.wav","man_yell_24.wav","man_yell_25.wav","man_yell_26.wav","man_yell_27.wav","man_yell_28.wav","man_yell_29.wav","man_yell_30.wav"]),
## not adequate, removed: "man_yell_b_21.wav","man_yell_b_22.wav","man_yell_b_23.wav"]),
#TODONOW:
 ("man_warcry", sf_priority_3|sf_vol_6, ["man_insult_2.ogg", "man_insult_3.ogg", "man_insult_7.ogg", "man_insult_9.ogg", "man_insult_13.ogg", "man_insult_15.ogg", "man_insult_16.ogg", "man_yell_4.ogg", "man_yell_7.ogg", "man_yell_9.ogg", "man_yell_11.ogg", "man_yell_13.ogg", "man_yell_15.ogg", "man_yell_16.ogg"]),
#OLD ("man_warcry",sf_priority_5, ["man_insult_01.wav","man_insult_02.wav","man_insult_03.wav","man_insult_04.wav","man_insult_05.wav","man_insult_06.wav","man_insult_07.wav","man_insult_08.wav","man_insult_09.wav","man_insult_10.wav","man_insult_11.wav","man_insult_12.wav","man_insult_13.wav","man_insult_14.wav","man_insult_15.wav","man_insult_16.wav","man_insult_17.wav","man_insult_18.wav","man_insult_19.wav","man_insult_20.wav","man_insult_21.wav","man_insult_22.wav","man_insult_23.wav","man_insult_24.wav","man_insult_25.wav","man_insult_26.wav","man_insult_27.wav","man_insult_28.wav"]),


 ("encounter_looters",sf_2d|sf_vol_8, []),
 #
 ("encounter_bandits",sf_2d|sf_vol_8, []),
 ("encounter_farmers",sf_2d|sf_vol_8, []),
 ("encounter_sea_raiders",sf_2d|sf_vol_8, []),
 ("encounter_steppe_bandits",sf_2d|sf_vol_8, []),
 #("encounter_nobleman",sf_2d|sf_vol_8, ["encounter_nobleman_1.wav"]),
 #("encounter_vaegirs_ally",sf_2d|sf_vol_8, ["encounter_vaegirs_ally.wav","encounter_vaegirs_ally_2.wav"]),
 #("encounter_vaegirs_neutral",sf_2d|sf_vol_8, ["encounter_vaegirs_neutral.wav","encounter_vaegirs_neutral_2.wav","encounter_vaegirs_neutral_3.wav","encounter_vaegirs_neutral_4.wav"]),
 #("encounter_vaegirs_enemy",sf_2d|sf_vol_8, ["encounter_vaegirs_neutral.wav","encounter_vaegirs_neutral_2.wav","encounter_vaegirs_neutral_3.wav","encounter_vaegirs_neutral_4.wav"]),
 ("sneak_town_halt",sf_2d, ["sneak_halt_1.wav","sneak_halt_2.wav"]),
 ("horse_walk",sf_priority_3|sf_vol_10, ["horse_walk_01.wav","horse_walk_02.wav","horse_walk_03.wav","horse_walk_04.wav","horse_walk_05.wav","horse_walk_06.wav","horse_walk_07.wav","horse_walk_08.wav"]),
 ("horse_trot",sf_priority_4|sf_vol_10, ["horse_trot_01.wav","horse_trot_02.wav","horse_trot_03.wav","horse_trot_04.wav","horse_trot_05.wav","horse_trot_06.wav","horse_trot_07.wav","horse_trot_08.wav","horse_trot_09.wav","horse_trot_10.wav"]),
 ("horse_canter",sf_priority_4|sf_vol_13, ["horse_canter_01.wav","horse_canter_02.wav","horse_canter_03.wav","horse_canter_04.wav","horse_canter_05.wav","horse_canter_06.wav","horse_canter_07.wav","horse_canter_08.wav"]),
 ("horse_gallop",sf_priority_5|sf_vol_13, ["horse_gallop_01.wav","horse_gallop_02.wav","horse_gallop_03.wav","horse_gallop_04.wav","horse_gallop_05.wav","horse_gallop_06.wav","horse_gallop_07.wav","horse_gallop_08.wav","horse_gallop_09.wav","horse_gallop_10.wav"]),
 ("horse_breath",sf_priority_1|sf_priority_9|sf_vol_10, ["horse_breath_4.wav","horse_breath_5.wav","horse_breath_6.wav","horse_breath_7.wav"]),
 ("horse_snort",sf_priority_1|sf_vol_10, ["horse_snort_1.wav","horse_snort_2.wav","horse_snort_3.wav","horse_snort_4.wav","horse_snort_5.wav"]),
 ("horse_low_whinny",sf_vol_12, ["horse_whinny-1.wav","horse_whinny-2.wav"]),
 ("block_fist",0, ["block_fist_3.wav","block_fist_4.wav"]),
 ("man_hit_blunt_weak",sf_priority_5|sf_vol_10, ["man_grunt_10.wav","man_grunt_11.wav","man_grunt_12.wav","man_grunt_13.wav","man_grunt_14.wav","man_grunt_15.wav","man_grunt_16.wav","man_grunt_17.wav","man_grunt_18.wav","man_grunt_19.wav","man_grunt_20.wav","man_grunt_21.wav","man_grunt_22.wav","man_grunt_23.wav","man_grunt_24.wav","man_grunt_25.wav","man_grunt_26.wav","man_grunt_27.wav","man_grunt_28.wav","man_grunt_29.wav","man_grunt_30.wav","man_grunt_31.wav","man_grunt_32.wav","man_grunt_33.wav","man_grunt_34.wav","man_grunt_35.wav","man_grunt_36.wav","man_grunt_37.wav","man_grunt_38.wav","man_grunt_39.wav","man_grunt_40.wav","man_grunt_41.wav"]),
 ("man_hit_blunt_strong",sf_priority_5|sf_vol_10, ["man_grunt_01.wav","man_grunt_02.wav","man_grunt_03.wav","man_grunt_04.wav","man_grunt_05.wav","man_grunt_17.wav","man_grunt_18.wav","man_grunt_19.wav","man_grunt_20.wav","man_grunt_21.wav","man_grunt_22.wav","man_grunt_23.wav","man_grunt_24.wav","man_grunt_25.wav","man_grunt_26.wav","man_grunt_27.wav","man_grunt_28.wav","man_grunt_29.wav","man_grunt_30.wav","man_grunt_31.wav","man_grunt_32.wav","man_grunt_33.wav","man_grunt_34.wav","man_grunt_35.wav","man_grunt_36.wav","man_grunt_37.wav","man_grunt_38.wav","man_grunt_39.wav","man_grunt_40.wav","man_grunt_41.wav"]),
 ("man_hit_pierce_weak",sf_priority_5|sf_vol_10, ["man_grunt_01.wav","man_grunt_02.wav","man_grunt_03.wav","man_grunt_04.wav","man_grunt_05.wav","man_grunt_06.wav","man_grunt_07.wav","man_grunt_08.wav","man_grunt_09.wav","man_grunt_10.wav","man_grunt_11.wav","man_grunt_12.wav","man_grunt_22.wav","man_grunt_23.wav","man_grunt_24.wav","man_grunt_25.wav","man_grunt_26.wav","man_grunt_27.wav","man_grunt_28.wav","man_grunt_29.wav","man_grunt_30.wav","man_grunt_31.wav","man_grunt_32.wav","man_grunt_33.wav","man_grunt_34.wav","man_grunt_35.wav","man_grunt_36.wav","man_grunt_37.wav","man_grunt_38.wav","man_grunt_39.wav","man_grunt_40.wav","man_grunt_41.wav"]),
 ("man_hit_pierce_strong",sf_priority_5|sf_vol_10, ["man_grunt_01.wav","man_grunt_02.wav","man_grunt_03.wav","man_grunt_04.wav","man_grunt_05.wav","man_grunt_06.wav","man_grunt_07.wav","man_grunt_08.wav","man_grunt_09.wav","man_grunt_10.wav","man_grunt_11.wav","man_grunt_12.wav","man_grunt_13.wav","man_grunt_14.wav","man_grunt_15.wav","man_grunt_16.wav","man_grunt_17.wav","man_grunt_18.wav","man_grunt_19.wav","man_grunt_20.wav","man_grunt_21.wav","man_grunt_22.wav","man_grunt_32.wav","man_grunt_33.wav","man_grunt_34.wav","man_grunt_35.wav","man_grunt_36.wav","man_grunt_37.wav","man_grunt_38.wav","man_grunt_39.wav","man_grunt_40.wav","man_grunt_41.wav"]),
 ("man_hit_cut_weak",sf_priority_5|sf_vol_10, ["man_grunt_01.wav","man_grunt_02.wav","man_grunt_03.wav","man_grunt_04.wav","man_grunt_05.wav","man_grunt_06.wav","man_grunt_07.wav","man_grunt_08.wav","man_grunt_09.wav","man_grunt_10.wav","man_grunt_11.wav","man_grunt_12.wav","man_grunt_13.wav","man_grunt_14.wav","man_grunt_15.wav","man_grunt_16.wav","man_grunt_17.wav","man_grunt_18.wav","man_grunt_19.wav","man_grunt_20.wav","man_grunt_21.wav","man_grunt_22.wav","man_grunt_23.wav","man_grunt_24.wav","man_grunt_25.wav","man_grunt_26.wav","man_grunt_27.wav","man_grunt_28.wav","man_grunt_29.wav","man_grunt_30.wav","man_grunt_31.wav","man_grunt_32.wav"]),
 ("man_hit_cut_strong",sf_priority_5|sf_vol_10, ["man_grunt_01.wav","man_grunt_02.wav","man_grunt_03.wav","man_grunt_04.wav","man_grunt_05.wav","man_grunt_06.wav","man_grunt_07.wav","man_grunt_08.wav","man_grunt_09.wav","man_grunt_10.wav","man_grunt_11.wav","man_grunt_12.wav","man_grunt_13.wav","man_grunt_14.wav","man_grunt_15.wav","man_grunt_16.wav","man_grunt_17.wav","man_grunt_18.wav","man_grunt_19.wav","man_grunt_20.wav","man_grunt_21.wav","man_grunt_22.wav","man_grunt_23.wav","man_grunt_24.wav","man_grunt_25.wav","man_grunt_35.wav","man_grunt_36.wav","man_grunt_37.wav","man_grunt_38.wav","man_grunt_39.wav","man_grunt_40.wav","man_grunt_41.wav"]),
 ("man_victory",sf_priority_5|sf_vol_9, ["man_victory_3.wav","man_victory_4.wav","man_victory_5.wav","man_victory_8.wav","man_victory_15.wav","man_victory_49.wav","man_victory_52.wav","man_victory_54.wav","man_victory_57.wav","man_victory_71.wav","man_victory_01.wav","man_victory_02.wav","man_victory_03.wav"]),
 ("fire_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["fx_fire_medium_01_lp.ogg", "fx_fire_campfire_lp.ogg", "fx_fire_campfire_lp.ogg", "fx_fire_embers_02_lp.ogg", "fx_fire_embers_02a_lp.ogg", "fx_fire_embers_02b_lp.ogg", "fx_fire_embers_02c_lp.ogg", "fx_fire_large_01_lp.ogg", "fx_fire_large_02_lp.ogg", "fx_fire_large_03_lp.ogg","Fire_Torch_Loop3.wav"]),
 ("torch_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.wav"]),
 ("dummy_hit",sf_priority_9, ["dummy_hit_01.wav","dummy_hit_02.wav","dummy_hit_03.wav"]),
 ("dummy_destroyed",sf_priority_9, ["dummy_break_01.wav","dummy_break_02.wav","dummy_break_03.wav","dummy_break_04.wav","dummy_break_05.wav"]),
 ("gourd_destroyed",sf_priority_9, ["dummy_break_01.wav","dummy_break_02.wav","dummy_break_03.wav","dummy_break_04.wav","dummy_break_05.wav"]),#TODO
 ("cow_moo", sf_2d|sf_priority_9|sf_vol_8, ["cow_moo_1.wav"]),
 ("cow_slaughter", sf_2d|sf_priority_9|sf_vol_8, ["cow_slaughter_01.wav","cow_slaughter_02.wav"]),
 ("distant_dog_bark", sf_2d|sf_priority_3|sf_vol_8, ["d_dog1.wav","d_dog2.wav","d_dog3.wav","d_dog7.wav"]),
 ("distant_owl", sf_2d|sf_priority_3|sf_vol_9, ["d_owl2.wav","d_owl3.wav","d_owl4.wav"]),
 ("distant_chicken", sf_2d|sf_priority_3|sf_vol_8, ["d_chicken1.wav","d_chicken2.wav"]),
 ("distant_carpenter", sf_2d|sf_priority_3|sf_vol_3, ["d_carpenter1.wav","d_saw_short3.wav"]),
 ("distant_blacksmith", sf_2d|sf_priority_3|sf_vol_4, ["d_blacksmith2.wav"]),
 ("arena_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["arena_loop11.wav"]),
 ("town_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["town_loop_3.wav"]),
 ("tutorial_fail", sf_2d|sf_vol_7,["cue_failure.wav"]),
 ("your_flag_taken", sf_2d|sf_priority_10|sf_vol_10, []),
 ("enemy_flag_taken", sf_2d|sf_priority_10|sf_vol_10, []),
 ("flag_returned", sf_2d|sf_priority_10|sf_vol_10, []),
 ("team_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, []),
 ("enemy_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, []),

	#("sea_travel", sf_looping|sf_priority_1|sf_vol_4, ["sea_travel.ogg"]),

	("horn", sf_priority_14|sf_vol_15, ["horn1.wav", "horn2.wav", "horn3.wav", "horn4.wav", "horn5.wav", "horn6.wav", "c1.wav", "c2.wav", "ee1.wav", "ee2.wav", "ee3.wav", "ee4.wav", "greek2.wav", "ne1.wav", "ne2.wav", "ne4.wav", "vhorn.wav", "vhorn1.wav", "vhorn2.wav", "vhorn3.wav", "vhorn4.wav", "vhorn5.wav", "ME_warhorn_charge_01.wav","ME_warhorn_charge_02.wav","NE_warhorn_charge.wav","SE_warhorn_charge.wav",]),

	#("wind", sf_looping|sf_priority_10|sf_vol_5, ["wind.wav"]),
	("wind", sf_looping|sf_priority_10|sf_vol_5, ["wind.wav", "Wind_WinterStorm1.wav", "Wind_WinterHills.wav", "Wind_Winter_Medium.wav", "Wind_Winter_Light_02.wav", "Wind_Winter_Light_01.wav", "Wind_Winter_Icy.wav", "Wind_Winter_Howl.wav", "Wind_Winter_Gales_01.wav", "Wind_winter.wav", "Wind_Whistling.wav", "Wind_Sand_03.wav", "Wind_Sand_02.wav", "Wind_Mountain.wav", "Wind_Lush.wav", "Wind_HowlGusty_02.wav", "Wind_Breezes_02.wav", ]),

	#("thunder", sf_priority_1|sf_vol_15, ["thunder01.wav", "thunder02.wav", "thunder03.wav", "thunder04.wav"]),
	("thunder", sf_priority_15|sf_vol_15, ["thunder01.wav", "thunder02.wav", "thunder03.wav", "thunder04.wav", "thunder_medium_03.wav", "thunder_medium_02.wav", "thunder_medium_01.wav", "thunder_far_05.wav", "thunder_far_04.wav", "thunder_far_03.wav", "thunder_far_02.wav", "thunder_far_01.wav", "thunder_close_06.wav", "thunder_close_05.wav", "thunder_close_04.wav", "thunder_close_03.wav", "thunder_close_02.wav", "thunder_close_01.wav"]),
	("cough", sf_priority_5|sf_vol_5, ["man_cough_1.wav", "man_cough_2.wav", "man_cough_3.wav", "cough_01.wav", "cough_02.wav", "cough_03.wav", "cough_04.wav", "cough_05.wav", "cough_06.wav", "cough_07.wav", "cough_08.wav", "cough_09.wav", "cough_10.wav", "belch_01.wav", "belch_02.wav", "belch_03.wav", "belch_04.wav", "belch_05.wav", "belch_06.wav", "sneeze_01.wav", "sneeze_02.wav", "sneeze_03.wav", "sneeze_04.wav", "sneeze_05.wav" "sniff_04.wav", "spit_01.wav", "spit_02.wav", "throat_04.wav", "throat_03.wav", "throat_10.wav"]),

	#("sea_ambiance", sf_2d|sf_looping|sf_priority_8|sf_vol_9, ["sea_loop.wav"]),

	### Dice game ### Dice game ###
 ("dice_roll",sf_priority_10|sf_vol_10, ["dice_roll.wav"]),
### Dice game ### Dice game ### END ###


#####Drinking game OSP Begin
#("drunk_concourt",sf_priority_10|sf_vol_10, ["drunk_fight.wav"]),
 #("drunk_ko",sf_priority_10|sf_vol_10, ["vomi.wav"]),  
#####Drinking game OSP End



  #Summaries begin
  #("summary_generic", sf_2d|sf_priority_1|sf_vol_2, ["summary_generic_01.mp3", "summary_generic_02.mp3", "summary_generic_03.mp3", "summary_generic_04.mp3", "report.mp3", "diplomacy_report.mp3", "mission_issued.mp3"]),
  ("summary_finance", sf_2d|sf_priority_1|sf_vol_5, ["summary_finance_01.mp3", "summary_finance_02.mp3"]),
  ####
  

  #AI Death Sounds Begin
	  ("decapitation", sf_priority_9|sf_vol_11, ["decap1.ogg", "decap2.ogg", "decap3.ogg", "decap4.ogg"]), #here
  ("decapitation_leader", sf_2d|sf_priority_4|sf_vol_7, ["faction_leader_dies.mp3", "faction_leader_killed.mp3"]),
  ("new_faction_leader", sf_2d|sf_priority_5|sf_vol_9, ["new_faction_leader.mp3", "new_faction_heir.mp3", "general_promoted.mp3"]),
  ####
  
  #Battle-related sounds begin
  #("battle_sounds", sf_2d|sf_priority_6|sf_vol_6, ["players_army_destroyed.mp3"]),
  #("won_battle", sf_2d|sf_priority_7|sf_vol_6, ["rebels_victorious.mp3", "infantry_group_celebrate_small_01.wav", "infantry_group_celebrate_large_01.wav"]),
  ####
	

  #Rebel-independece-related sounds begin
  ("rebel_sounds", sf_2d|sf_priority_8|sf_vol_7, ["settlement_unrest.mp3", "settlement_taken.mp3", "settlement_surrenders.mp3", "settlement_revolts.mp3", "settlement_razed.mp3", "settlement_exterminated.mp3", "settlement_destroyed.mp3", "disaster_riot.mp3", "city_gained_through_revolt.mp3", "end_turn_brittania_03.mp3", "end_turn_brittania_04.mp3"]),
  ("new_factions", sf_2d|sf_priority_9|sf_vol_7, ["historic_event.mp3", "mission_denounce.mp3", "mission_denounce_arrived.mp3", "mission_denounce_fail.mp3", "emergent_faction_appears.mp3", "end_turn_brittania_01.mp3", "end_turn_brittania_02.mp3"]),
  ("historical_event", sf_2d|sf_priority_9|sf_vol_7, ["historic_event.mp3"]),
  ####
  
  #Recruitment-related sounds begin
  ("bribe_hire", sf_2d|sf_priority_10|sf_vol_5, ["army_bribed.mp3", "character_bribed.mp3"]),
  ("hire_units", sf_2d|sf_priority_11|sf_vol_5, ["unit_completed.mp3", "recruitment_complete_03.mp3", "recruitment_complete_02.mp3", "recruitment_complete_01.mp3", "merge_armies_02.wav"]),
  ####
  
  ####Diplomatic sounds begin
  ("ceasefire", sf_2d|sf_priority_12|sf_vol_5, ["ceasefire_declared.mp3", "relations_improved.mp3"]),
  ("truce_declare", sf_2d|sf_priority_12|sf_vol_5, ["alliance_declared.mp3", "ally_declared_alliance_with_enemy.mp3", "peace_treaty_signed.mp3", "mission_success.mp3"]),
  ("war_declared", sf_2d|sf_priority_12|sf_vol_5, ["war_declared.mp3", "war_declared_arrived.mp3", "transgression.mp3", "mission_expired.mp3", "relations_worsened.mp3"]),
  ("decline_prisoner", sf_2d|sf_priority_12|sf_vol_5, ["decline_release.mp3"]),
  ("accept_prisoner", sf_2d|sf_priority_12|sf_vol_5, ["event_prisoner_release.mp3", "prisoner_ransom_01.mp3", "prisoner_ransom_02.mp3","prisoner_ransom_03.mp3","prisoner_ransom_04.mp3","prisoner_ransom_05.mp3","prisoner_ransom_06.mp3","prisoner_ransom_07.mp3","prisoner_ransom_08.mp3","prisoner_ransom_10.mp3","prisoner_ransom_11.mp3","prisoner_ransom_12.mp3"]),
  ####
  
  ####Events Begin
  ("crusade_called", sf_2d|sf_priority_13|sf_vol_7, ["crusade_called.mp3", "crusade_called_arrived.mp3"]),
  ("crusade_reached", sf_2d|sf_priority_13|sf_vol_5, ["crusade_factions_joined.mp3"]),
  ("crusade_fail", sf_2d|sf_priority_13|sf_vol_8, ["crusade_cancelled.mp3", "crusade_failed.mp3", "crusade_unit_deserted_no_progress.mp3", "pope_dies.mp3"]),
  ("crusade_success", sf_2d|sf_priority_13|sf_vol_8, ["crusade_succeed.mp3"]),
  ("recruits_left", sf_2d|sf_priority_14|sf_vol_5, ["crusade_units_desert_warning.mp3", "crusade_units_deserted_removed.mp3", "small_army_disbands.mp3"]),
  ("faction_defeated", sf_2d|sf_priority_13|sf_vol_8, ["faction_defeated.mp3", "faction_defeated_by_player.mp3", "rebel_revolt_suppressed.mp3"]),
  ("occupy_center", sf_2d|sf_priority_15|sf_vol_5, ["settlement_occupied.mp3", "building_captured_battle.mp3", "building_captured_by_allies.mp3"]), #Occupied center
  ("players_settlement_besieged", sf_2d|sf_priority_14|sf_vol_5, ["settlement_besieged_arrived.mp3"]),
  ("prepare_equipment_for_siege", sf_2d|sf_priority_14|sf_vol_6, ["protectorate_established.mp3", "upgrade_settlement_01.mp3"]),
  

  

  #New
  ("treaty_degraded", sf_2d|sf_priority_14|sf_vol_6, ["alliance_broken.mp3"]),
  ("construction_approved", sf_2d|sf_priority_14|sf_vol_6, ["construction_approval.mp3", "construction_complete_many.mp3", "upgrade_settlement_01.mp3", "upgrade_guild.mp3"]), #For towns and villages only
    ##("construction_approved", sf_2d|sf_priority_14|sf_vol_6, ["construction_approval.mp3", "construction_complete_many.mp3", "upgrade_settlement_02.mp3", "upgrade_settlement_01.mp3", "upgrade_guild.mp3", "upgrade_settlement_03.mp3", "upgrade_settlement_04.mp3"]), #For towns and villages only
  ("purchase_manor", sf_2d|sf_priority_14|sf_vol_6, ["create_guild.mp3"]),
  ("engage_enemy_field", sf_2d|sf_priority_14|sf_vol_6, ["engage_enemy.mp3", "CMA_defend.mp3", "CMA_attack.mp3", "sbattle.mp3", "start_battle_teutonic.mp3", "engage_enemy_02.mp3", "attack.mp3", "attack_out_of_range_01.mp3", "siege_attack.mp3"]),
  ("manor_upgrade_complete", sf_2d|sf_priority_14|sf_vol_6, ["mission_issued_arrived.mp3"]),
  #("enter_arena", sf_2d|sf_priority_14|sf_vol_6, ["summary_training_01.mp3", "summary_training_02.mp3", "summary_training_03.mp3", "summary_training_04.mp3", "summary_training_05.mp3"]),
  ("ambient_menus", sf_2d|sf_priority_14|sf_vol_6, ["ambient_town_euro_01.wav", "ambient_town_euro_02.wav", "ambient_town_euro_03.wav", "ambient_town_euro_04.wav", "ambient_town_euro_05.wav" "ambient_town_euro_bell_02.wav", "ambient_town_euro_bell_03.wav", "ambient_town_euro_bell_04.wav", "ambient_town_euro_birds_01a.wav", "ambient_town_euro_birds_01b.wav", "ambient_town_euro_birds_01c.wav", "ambient_town_euro_birds_02a.wav", "ambient_town_euro_birds_02b.wav", "ambient_town_euro_birds_02c.wav", "ambient_town_euro_birds_03a.wav", "ambient_town_euro_birds_03b.wav", "ambient_town_euro_birds_03c.wav", "ambient_town_euro_birds_04a.wav", "ambient_town_euro_birds_04b.wav", "ambient_town_euro_birds_04c.wav", "ambient_town_euro_birds_05a.wav", "ambient_town_euro_birds_05b.wav"]),
  ("belfry_sound", sf_looping|sf_priority_10|sf_vol_15, ["Siege_Tower_Move_Grass.wav", "Siege_Tower_Move_Snow.wav", "Siege_Tower_Move_Stone.wav", "Siege_Tower_Move_Wood.wav"]),
  ("belfry_sound_end", sf_priority_10|sf_vol_15, ["siege_t1.mp3", "siege_t2.mp3"]), #Co-Op Only
  ("belfry_sound_end_sp", sf_priority_10|sf_vol_15, ["siege_t1_sp.mp3", "siege_t2_sp.mp3"]), #SP Only
#####Wounded OSP Begin
("death",sf_priority_10|sf_vol_10, ["death_end.ogg"]),
#####Wounded OSP End

#####Extra sounds Begin
 ("oil_noise",sf_priority_1|sf_vol_1, ["boiling_oil.wav"]),
 

#####Extra Sounds End

#Warwolf begin additional sounds for disasters
#  ("Typhoon", sf_2d|sf_priority_9|sf_vol_10, ["Typhoon.ogg"]),
#  ("Forest_fires", sf_2d|sf_priority_9|sf_vol_10, ["Forest_fires.ogg"]),
#  ("Tsunami", sf_2d|sf_priority_9|sf_vol_10, ["Tsunami.ogg"]),
#  ("Drought", sf_2d|sf_priority_9|sf_vol_10, ["Drought.ogg"]),
#  ("The_Black_Death", sf_2d|sf_priority_9|sf_vol_10, ["The_Black_Death.ogg"]),
#  ("Earthquake", sf_2d|sf_priority_9|sf_vol_10, ["Earthquake.ogg"]),
#  ("Flood", sf_2d|sf_priority_9|sf_vol_10, ["Flood.ogg"]),
#  ("eruptions", sf_2d|sf_priority_9|sf_vol_10, ["eruptions.ogg"]),
#  ("bad_drum", sf_2d|sf_priority_10|sf_vol_9, ["quest_cancelled2.ogg"]),
#    #("rats_squeak", sf_2d|sf_priority_9|sf_vol_8, ["rats_squeak.ogg"]),
#	 # ("cat_meow", sf_2d|sf_vol_15, ["cat_meow.ogg"]),
#  ("Typhoon", sf_2d|sf_priority_9|sf_vol_10, ["Typhoon.ogg"]),
#
#  ("Forest_fires", sf_2d|sf_priority_9|sf_vol_10, ["Forest_fires.ogg"]),
#
#  ("Tsunami", sf_2d|sf_priority_9|sf_vol_10, ["Tsunami.ogg"]),
#
#  ("Drought", sf_2d|sf_priority_9|sf_vol_10, ["Drought.ogg"]),
#
#  ("The_Black_Death", sf_2d|sf_priority_9|sf_vol_10, ["The_Black_Death.ogg"]),
#
#  ("Earthquake", sf_2d|sf_priority_9|sf_vol_10, ["Earthquake.ogg"]),
#
#  ("Flood", sf_2d|sf_priority_9|sf_vol_10, ["Flood.ogg"]),
#
#  ("eruptions", sf_2d|sf_priority_9|sf_vol_10, ["eruptions.ogg"]),
#  ("bad_drum", sf_2d|sf_priority_10|sf_vol_9, ["quest_cancelled2.ogg"]),
    #("rats_squeak", sf_2d|sf_priority_9|sf_vol_8, ["rats_squeak.ogg"]),
	 # ("cat_meow", sf_2d|sf_vol_15, ["cat_meow.ogg"]),
#Warwolf end


#####MUSICBOX  BEGIN
#Battle Music Begin


 # ##Tensions
##  ("arab_tension1", sf_2d|sf_priority_15|sf_vol_10, ["(Arabic_Tension_4).mp3","(Arabic_Tension_3).mp3", "(Crusades_Tension)_Parched.mp3", "(Crusades_Loading)_Against_The_Rock.mp3", "(Arabic_Camp_Battle_1)_Honour_Of_Sultan.mp3", "(Crusades_Campaign_Battle)_Sun_Eyes.mp3"]),
##  ("steppe_tension", sf_2d|sf_priority_15|sf_vol_10, ["(Brittania_Tension)_Ghosts_Of_Loch.mp3", "(Britannia_Camp_Battle)_Tally-ho.mp3", "(Euro_Tension_2)_Call_Of_The_Sheep.mp3", "(Euro_Tension_9)_Grave_Blow.mp3", "(Euro_Tension_6)_Chase.mp3"]),
##  ("euro_tension", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Tension_1)_BladeGrass.mp3","(Euro_Tension_3)_Fear_Frozen.mp3","(Euro_Tension_4).mp3","(Euro_Tension_5).mp3","(Euro_Tension_7)_The_Reveal.mp3","(Euro_Tension_8)_Ignosi.mp3","(Teutonic_Tension)_Forest_Haze.mp3", "(Teutonic_Campaign_Loading)_Brothers_Together", "(Euro_Loading_3)_Epic_Unease.mp3", "(Teutonic_Campaign_Battle)_Hungry_Sword.mp3", "(Euro_Camp_Battle_1)_Destiny.mp3" ]),
 # ##Field Battles
##  ("arabb1", sf_2d|sf_priority_15|sf_vol_10, ["(Arabic_Battle_1)_Crack_your_head_with_a_Tabla.mp3"]),
##  ("arabb2", sf_2d|sf_priority_15|sf_vol_10, ["(Arabic_Battle_2)_Wind_Cuts.mp3"]),
##  #("arabb3", sf_2d|sf_priority_15|sf_vol_10, ["(Arabic_Camp_Battle_1)_Honour_Of_Sultan.mp3"]),
##  ("arabb4", sf_2d|sf_priority_15|sf_vol_10, ["(Arabic_Battle_3).mp3"]),
##  ("arabb5", sf_2d|sf_priority_15|sf_vol_10, ["(Arabic_Battle_4).mp3"]),
##  ("arabb6", sf_2d|sf_priority_15|sf_vol_10, ["(Crusades_Battle)_Valley_Of_Death.mp3"]),
##  ("arabb8", sf_2d|sf_priority_15|sf_vol_10, ["(Arabic_Tension_1)_Kebabka.mp3"]),
##  ("arabb9", sf_2d|sf_priority_15|sf_vol_10, ["(Arabic_Tension_5).mp3"]),
##  #("arabb7", sf_2d|sf_priority_15|sf_vol_10, ["(Crusades_Campaign_Battle)_Sun_Eyes.mp3"]),
##  #NOTE Mediterrain battle and mobilize (sieges) are shared songs.
##  ("medib1", sf_2d|sf_priority_15|sf_vol_10, ["(Mediterranean_Battle_1)_Lifted_To_The_Hotplate.mp3"]),
##  #("medib2", sf_2d|sf_priority_15|sf_vol_10, ["(Britannia_Camp_Battle)_Tally-ho.mp3"]),
##  #Mobilize
##  ("medib3", sf_2d|sf_priority_15|sf_vol_10, ["(Mediterranean_Mobilize_1)_Mare_Nostrum.mp3"]), #Sieges too
##  ("medib4", sf_2d|sf_priority_15|sf_vol_10, ["(Mediterranean_Mobilize_2)_Death_Lullaby.mp3"]), #Sieges too
##  ("medib5", sf_2d|sf_priority_15|sf_vol_10, ["(Mediterranean_Mobilize_2)_Song_For_Toomba.mp3"]), #Sieges too
##  ("medib6", sf_2d|sf_priority_15|sf_vol_10, ["(Mediterranean_Tension_1)_By_The_Marmara.mp3"]),
##  ("medib7", sf_2d|sf_priority_15|sf_vol_10, ["(Mediterranean_Tension_2)_Secret_Sandals.mp3"]),
##  ("medib8", sf_2d|sf_priority_15|sf_vol_10, ["(Arabic_Tension_2)_Starsand.mp3"]), #Starsand
##  #Field Continuation
##  ##
##  ("eurob1", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Battle_1)_Duke_of_Death.mp3"]),
##  ("eurob2", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Battle_2)_Nothing_Left.mp3"]),
##  ("eurob3", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Battle_3)_Crusaders.mp3"]),
##  ("eurob4", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Battle_4)_War_of_Kings.mp3"]),
##  ("eurob5", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Battle_5).mp3"]),
##  ("eurob6", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Battle_6).mp3"]),
##  ("eurob7", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Battle_7).mp3"]),
##  ("eurob8", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Battle_8)_Vortex.mp3"]),
##  ("eurob9", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Battle_9)_Dangerous.mp3"]),
##  #("eurob10", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Camp_Battle_1)_Destiny.mp3"]),
##  ("eurob11", sf_2d|sf_priority_15|sf_vol_10, ["(Teutonic_Battle)_Darker_Skies_Ahead.mp3"]),
##  ##Sieges
##   ("arabs1", sf_2d|sf_priority_15|sf_vol_10, ["(Arabic_Mobilize_1)_High_Winds.mp3"]),
##   ("arabs2", sf_2d|sf_priority_15|sf_vol_10, ["(Arabic_Mobilize_2).mp3"]),
##   ("arabs3", sf_2d|sf_priority_15|sf_vol_10, ["(Arabic_Mobilize_3).mp3"]),
##   ("arabs4", sf_2d|sf_priority_15|sf_vol_10, ["(Arabic_Mobilize_4).mp3"]),
##   ("arabs5", sf_2d|sf_priority_15|sf_vol_10, ["(Crusades_Mobilize)_Honour_Moment.mp3"]),
##    #Mediterr & Arabs
##	("medis1", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_5)_Action.mp3"]),
##	("medis2", sf_2d|sf_priority_15|sf_vol_7, ["(Euro_Mobilize_9)_Feral_Chase.mp3"]), #This should be less volume than others.
##   ##Euro
##   ("euros1", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_1)_Sister_Davul.mp3"]),
##   ("euros2", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_2)_Solenka.mp3"]),
##   ("euros3", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_3)_This_is_it.mp3"]),
##   ("euros4", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_4)_New_Arc_Ascending.mp3"]),
##   ("euros5", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_6).mp3"]),
##   ("euros6", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_7).mp3"]),
##   ("euros7", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_8).mp3"]),
##   ("euros8", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_10)_Tectonic.mp3"]),
##   ("euros9", sf_2d|sf_priority_15|sf_vol_8, ["(Teutonic_Mobilize)_Hymn_Of_War.mp3"]),
##   ("euros10", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_11)_We_Got_Trouble.mp3"]),
#####MUSICBOX  END
#Battle Music End

#Misc
("objective_success", sf_2d|sf_priority_10|sf_vol_9, ["brittania_mission_arrived.mp3"]), #Used for feasts and byzantine empire reform roman empire
("notification_hostile", sf_2d|sf_priority_10|sf_vol_9, ["teutonic_mission_arrived.mp3"]),
("notification_center_lost", sf_2d|sf_priority_10|sf_vol_9, ["building_lost_battle.mp3", "player_lose_warning.mp3"]),
("choose_faction_menu", sf_2d|sf_priority_10|sf_vol_7, ["change_faction.mp3"]),
##
#("result_won_battle", sf_2d|sf_priority_10|sf_vol_7, ["rebels_victorious.mp3", "infantry_group_celebrate_small_01.mp3","infantry_group_celebrate_large_01.mp3"]),
#("result_lost_battle", sf_2d|sf_priority_10|sf_vol_7, ["players_army_destroyed.mp3"]),
#####Cultural Speeches begin

#("euros10", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_11)_We_Got_Trouble.mp3"]),
#("euros10", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_11)_We_Got_Trouble.mp3"]),
#("euros10", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_11)_We_Got_Trouble.mp3"]),
#("euros10", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_11)_We_Got_Trouble.mp3"]),
#("euros10", sf_2d|sf_priority_15|sf_vol_10, ["(Euro_Mobilize_11)_We_Got_Trouble.mp3"]),

#########Factional & King
("engfk_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["English_Admiral_Attacked_Enemy_1.mp3","English_Admiral_Attacked_Enemy_2.mp3","English_Admiral_Attacked_Enemy_3.mp3"]),
("engfk_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["English_Admiral_Attacking_1.mp3","English_Admiral_Attacking_2.mp3","English_Admiral_Attacking_3.mp3"]),
("engfk_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Attacking_1.mp3","English_Army_Attacking_2.mp3","English_Army_Attacking_3.mp3","English_General_Fight_On_Battle_Map_Chivalry_2.mp3","English_Army_Fight_On_Battle_Map_6.mp3","English_Army_Fight_On_Battle_Map_1.mp3","English_Army_Fight_On_Battle_Map_2.mp3","English_Army_Fight_On_Battle_Map_3.mp3","English_Army_Fight_On_Battle_Map_4.mp3","English_Army_Fight_On_Battle_Map_5.mp3","English_General_Attacking_1.mp3","English_General_Attacking_2.mp3","English_General_Attacking_3.mp3","English_General_Attacking_Chivalry_1.mp3","English_General_Attacking_Chivalry_3.mp3","English_General_Attacking_Dread_1.mp3","English_General_Attacking_Dread_2.mp3","English_General_Attacking_Dread_3.mp3", "English_General_Attacking_Chivalry_2.mp3"]),
("engfk_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Battle_lost_retreat_1.mp3","English_Army_Battle_lost_retreat_2.mp3","English_Army_Battle_lost_retreat_3.mp3","English_General_Battle_lost_retreat_1.mp3","English_General_Battle_lost_retreat_2.mp3","English_General_Battle_lost_retreat_3.mp3","English_General_Battle_lost_retreat_Chivalry_1.mp3","English_General_Battle_lost_retreat_Chivalry_2.mp3","English_General_Battle_lost_retreat_Chivalry_3.mp3","English_General_Battle_lost_retreat_Dread_1.mp3","English_General_Battle_lost_retreat_Dread_2.mp3","English_General_Battle_lost_retreat_Dread_3.mp3","English_General_Fight_On_Battle_Map_1.mp3","English_General_Fight_On_Battle_Map_2.mp3","English_General_Fight_On_Battle_Map_3.mp3","English_General_Fight_On_Battle_Map_Chivalry_1.mp3","English_General_Fight_On_Battle_Map_Chivalry_3.mp3","English_General_Fight_On_Battle_Map_Dread_1.mp3","English_General_Fight_On_Battle_Map_Dread_2.mp3","English_General_Fight_On_Battle_Map_Dread_3.mp3"]),
("engfk_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Battle_won_1.mp3","English_Army_Battle_won_2.mp3","English_Army_Battle_won_3.mp3","English_General_Battle_won_1.mp3","English_General_Battle_won_2.mp3","English_General_Battle_won_3.mp3","English_General_Battle_won_Chivalry_1.mp3","English_General_Battle_won_Chivalry_2.mp3","English_General_Battle_won_Chivalry_3.mp3","English_General_Battle_won_Dread_1.mp3","English_General_Battle_won_Dread_2.mp3","English_General_Battle_won_Dread_3.mp3"]),
("engfk_army_join", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Joins_Army_1.mp3","English_Army_Joins_Army_2.mp3","English_Army_Joins_Army_3.mp3","English_General_Joins_Army_1.mp3","English_General_Joins_Army_2.mp3","English_General_Joins_Army_3.mp3","English_General_Joins_Army_Chivalry_1.mp3","English_General_Joins_Army_Chivalry_2.mp3","English_General_Joins_Army_Chivalry_3.mp3","English_General_Joins_Army_Dread_1.mp3","English_General_Joins_Army_Dread_2.mp3","English_General_Joins_Army_Dread_3.mp3"]),
("engfk_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["English_General_Leaves_Army_1.mp3","English_General_Leaves_Army_2.mp3","English_General_Leaves_Army_3.mp3","English_General_Leaves_Army_Chivalry_1.mp3","English_General_Leaves_Army_Chivalry_2.mp3","English_General_Leaves_Army_Chivalry_3.mp3","English_General_Leaves_Army_Dread_1.mp3","English_General_Leaves_Army_Dread_2.mp3","English_General_Leaves_Army_Dread_3.mp3",]),
("engfk_capture", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Settlement_Capture_Celebration_1.mp3","English_Army_Settlement_Capture_Celebration_3.mp3","English_Army_Settlement_Capture_Celebration_2.mp3","English_General_Settlement_Capture_Celebration_1.mp3","English_General_Settlement_Capture_Celebration_2.mp3","English_General_Settlement_Capture_Celebration_3.mp3","English_General_Settlement_Capture_Celebration_Chivalry_1.mp3","English_General_Settlement_Capture_Celebration_Chivalry_2.mp3","English_General_Settlement_Capture_Celebration_Chivalry_3.mp3","English_General_Settlement_Capture_Celebration_Dread_1.mp3","English_General_Settlement_Capture_Celebration_Dread_2.mp3","English_General_Settlement_Capture_Celebration_Dread_3.mp3"]),
("engfk_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_siege_Begun_1.mp3","English_Army_siege_Begun_2.mp3","English_General_siege_Begun_1.mp3","English_General_siege_Begun_2.mp3","English_General_siege_Begun_Chivalry_1.mp3","English_General_siege_Begun_Chivalry_2.mp3","English_General_siege_Begun_Dread_1.mp3","English_General_siege_Begun_Dread_2.mp3"]),
("engfk_besieged", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_siege_Besieged_1.mp3","English_Army_siege_Besieged_2.mp3","English_Army_siege_Besieged_3.mp3","English_General_siege_Besieged_1.mp3","English_General_siege_Besieged_2.mp3","English_General_siege_Besieged_3.mp3","English_General_siege_Besieged_Chivalry_1.mp3","English_General_siege_Besieged_Chivalry_2.mp3","English_General_siege_Besieged_Chivalry_3.mp3","English_General_siege_Besieged_Dread_1.mp3","English_General_siege_Besieged_Dread_2.mp3","English_General_siege_Besieged_Dread_3.mp3"]),
("engfk_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_siege_Ongoing_1.mp3","English_Army_siege_Ongoing_2.mp3","English_Army_siege_Ongoing_3.mp3","English_General_siege_Ongoing_1.mp3","English_General_siege_Ongoing_2.mp3","English_General_siege_Ongoing_3.mp3","English_General_siege_Ongoing_Chivalry_1.mp3","English_General_siege_Ongoing_Chivalry_2.mp3","English_General_siege_Ongoing_Chivalry_3.mp3","English_General_siege_Ongoing_Dread_1.mp3","English_General_siege_Ongoing_Dread_2.mp3","English_General_siege_Ongoing_Dread_3.mp3"]),

#French
("frenchfk_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["French_Admiral_Attacked_Enemy_2.mp3","French_Admiral_Attacked_Enemy_3.mp3","French_Admiral_Attacked_Enemy_1.mp3"]),
("frenchfk_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["French_Admiral_Attacking_1.mp3","French_Admiral_Attacking_2.mp3","French_Admiral_Attacking_3.mp3"]),
("frenchfk_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Attacking_2.mp3","French_Army_Fight_On_Battle_Map_1.mp3","French_Army_Fight_On_Battle_Map_3.mp3","French_Army_Fight_On_Battle_Map_5.mp3","French_General_Attacking_2.mp3","French_General_Attacking_3.mp3","French_General_Attacking_Chivalry_1.mp3","French_General_Attacking_Chivalry_2.mp3","French_General_Attacking_Dread_1.mp3","French_General_Attacking_Dread_3.mp3","French_General_Fight_On_Battle_Map_3.mp3","French_General_Fight_On_Battle_Map_Chivalry_1.mp3","French_General_Fight_On_Battle_Map_Dread_1.mp3","French_General_Fight_On_Battle_Map_Dread_2.mp3","French_General_Fight_On_Battle_Map_Dread_3.mp3","French_Army_Attacking_1.mp3","French_Army_Attacking_3.mp3","French_Army_Fight_On_Battle_Map_2.mp3","French_General_Attacking_1.mp3","French_General_Attacking_Dread_2.mp3","French_Army_Fight_On_Battle_Map_4.mp3","French_Army_Fight_On_Battle_Map_6.mp3","French_General_Attacking_Chivalry_3.mp3","French_General_Fight_On_Battle_Map_1.mp3","French_General_Fight_On_Battle_Map_2.mp3","French_General_Fight_On_Battle_Map_Chivalry_2.mp3","French_General_Fight_On_Battle_Map_Chivalry_3.mp3"]),
("frenchfk_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Battle_lost_retreat_1.mp3","French_Army_Battle_lost_retreat_2.mp3","French_General_Battle_lost_retreat_1.mp3","French_General_Battle_lost_retreat_2.mp3","French_General_Battle_lost_retreat_Chivalry_1.mp3","French_General_Battle_lost_retreat_Chivalry_2.mp3","French_General_Battle_lost_retreat_Chivalry_3.mp3","French_General_Battle_lost_retreat_Dread_1.mp3","French_General_Battle_lost_retreat_Dread_2.mp3","French_General_Battle_lost_retreat_Dread_3.mp3","French_Army_Battle_lost_retreat_3.mp3","French_General_Battle_lost_retreat_3.mp3"]),
("frenchfk_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["French_General_Battle_won_3.mp3","French_General_Battle_won_Chivalry_1.mp3","French_General_Battle_won_Chivalry_3.mp3","French_General_Battle_won_Dread_1.mp3","French_General_Battle_won_Dread_2.mp3","French_General_Battle_won_Dread_3.mp3","French_Army_Battle_won_1.mp3","French_General_Battle_won_2.mp3","French_General_Battle_won_1.mp3","French_General_Battle_won_Chivalry_2.mp3"]),
("frenchfk_army_join", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Joins_Army_1.mp3","French_Army_Joins_Army_2.mp3","French_Army_Joins_Army_3.mp3","French_General_Joins_Army_1.mp3","French_General_Joins_Army_3.mp3","French_General_Joins_Army_Chivalry_3.mp3","French_General_Joins_Army_Dread_1.mp3","French_General_Joins_Army_Dread_2.mp3","French_General_Joins_Army_Dread_3.mp3","French_General_Joins_Army_2.mp3","French_General_Joins_Army_Chivalry_1.mp3","French_General_Joins_Army_Chivalry_2.mp3"]),
("frenchfk_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Leaves_Army_1.mp3","French_Army_Leaves_Army_2.mp3","French_General_Leaves_Army_1.mp3","French_General_Leaves_Army_2.mp3","French_General_Leaves_Army_3.mp3","French_General_Leaves_Army_Chivalry_1.mp3","French_General_Leaves_Army_Chivalry_2.mp3","French_General_Leaves_Army_Dread_1.mp3","French_General_Leaves_Army_Dread_2.mp3", "French_General_Leaves_Army_Dread_3.mp3", "French_Army_Leaves_Army_3.mp3", "French_General_Leaves_Army_Chivalry_3.mp3"]),
("frenchfk_capture", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Settlement_Capture_Celebration_3.mp3","French_General_Settlement_Capture_Celebration_3.mp3","French_General_Settlement_Capture_Celebration_Dread_1.mp3","French_General_Settlement_Capture_Celebration_Dread_3.mp3","French_Army_Settlement_Capture_Celebration_2.mp3","French_General_Settlement_Capture_Celebration_2.mp3","French_General_Settlement_Capture_Celebration_Chivalry_2.mp3","French_General_Settlement_Capture_Celebration_Dread_2.mp3","French_Army_Settlement_Capture_Celebration_1.mp3","French_General_Settlement_Capture_Celebration_1.mp3","French_General_Settlement_Capture_Celebration_Chivalry_1.mp3","French_General_Settlement_Capture_Celebration_Chivalry_3.mp3"]),
("frenchfk_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_siege_Begun_2.mp3","French_General_siege_Begun_1.mp3","French_General_siege_Begun_2.mp3","French_General_siege_Begun_Dread_2.mp3","French_Army_siege_Begun_1.mp3","French_General_siege_Begun_Chivalry_1.mp3","French_General_siege_Begun_Dread_1.mp3","French_General_siege_Begun_Chivalry_2.mp3"]),
("frenchfk_besieged", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_siege_Besieged_1.mp3","French_Army_siege_Besieged_2.mp3","French_General_siege_Besieged_1.mp3","French_General_siege_Besieged_2.mp3","French_General_siege_Besieged_Chivalry_1.mp3","French_General_siege_Besieged_Dread_1.mp3","French_General_siege_Besieged_Dread_2.mp3","French_General_siege_Besieged_Dread_3.mp3","French_Army_siege_Besieged_3.mp3","French_General_siege_Besieged_3.mp3","French_General_siege_Besieged_Chivalry_2.mp3","French_General_siege_Besieged_Chivalry_3.mp3"]),
("frenchfk_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_siege_Ongoing_1.mp3","French_Army_siege_Ongoing_3.mp3","French_General_siege_Ongoing_1.mp3","French_General_siege_Ongoing_2.mp3","French_General_siege_Ongoing_Chivalry_3.mp3","French_General_siege_Ongoing_Dread_2.mp3","French_General_siege_Ongoing_Dread_3.mp3","French_Army_siege_Ongoing_2.mp3","French_General_siege_Ongoing_3.mp3","French_General_siege_Ongoing_Chivalry_1.mp3","French_General_siege_Ongoing_Chivalry_2.mp3","French_General_siege_Ongoing_Dread_1.mp3"]),
#French

#########Factional Generic
#Scotland
("scotfg_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Admiral_Attacked_Enemy_1.mp3","Scottish_Admiral_Attacked_Enemy_2.mp3","Scottish_Admiral_Attacked_Enemy_3.mp3"]),
("scotfg_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Admiral_Attacking_1.mp3","Scottish_Admiral_Attacking_2.mp3","Scottish_Admiral_Attacking_3.mp3"]),
("scotfg_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_Attacking_1.mp3","Scottish_Army_Attacking_2.mp3","Scottish_Army_Attacking_3.mp3","Scottish_Army_Fight_On_Battle_Map_1.mp3","Scottish_Army_Fight_On_Battle_Map_6.mp3","Scottish_General_Attacking_1.mp3","Scottish_General_Attacking_2.mp3","Scottish_General_Attacking_3.mp3","Scottish_General_Attacking_Chivalry_1.mp3","Scottish_General_Attacking_Chivalry_3.mp3","Scottish_General_Attacking_Dread_1.mp3","Scottish_General_Attacking_Dread_2.mp3","Scottish_General_Attacking_Dread_3.mp3","Scottish_General_Fight_On_Battle_Map_Dread_1.mp3","Scottish_General_Fight_On_Battle_Map_Dread_2.mp3","Scottish_General_Fight_On_Battle_Map_Dread_3.mp3"      ,"Scottish_Army_Fight_On_Battle_Map_2.mp3","Scottish_Army_Fight_On_Battle_Map_3.mp3","Scottish_Army_Fight_On_Battle_Map_4.mp3","Scottish_Army_Fight_On_Battle_Map_5.mp3","Scottish_General_Attacking_Chivalry_2.mp3"             ,"Scottish_General_Fight_On_Battle_Map_1.mp3","Scottish_General_Fight_On_Battle_Map_2.mp3","Scottish_General_Fight_On_Battle_Map_3.mp3","Scottish_General_Fight_On_Battle_Map_Chivalry_1.mp3","Scottish_General_Fight_On_Battle_Map_Chivalry_2.mp3","Scottish_General_Fight_On_Battle_Map_Chivalry_3.mp3"]),
("scotfg_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_Battle_lost_retreat_1.mp3","Scottish_Army_Battle_lost_retreat_2.mp3","Scottish_Army_Battle_lost_retreat_3.mp3","Scottish_General_Battle_lost_retreat_1.mp3","Scottish_General_Battle_lost_retreat_2.mp3","Scottish_General_Battle_lost_retreat_3.mp3","Scottish_General_Battle_lost_retreat_Chivalry_1.mp3","Scottish_General_Battle_lost_retreat_Chivalry_2.mp3","Scottish_General_Battle_lost_retreat_Chivalry_3.mp3","Scottish_General_Battle_lost_retreat_Dread_1.mp3","Scottish_General_Battle_lost_retreat_Dread_2.mp3","Scottish_General_Battle_lost_retreat_Dread_3.mp3"]),
("scotfg_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_Battle_won_1.mp3","Scottish_Army_Battle_won_3.mp3","Scottish_General_Battle_won_2.mp3","Scottish_General_Battle_won_3.mp3","Scottish_General_Battle_won_Chivalry_3.mp3","Scottish_General_Battle_won_Dread_1.mp3","Scottish_General_Battle_won_Dread_2.mp3","Scottish_General_Battle_won_Dread_3.mp3","Scottish_Army_Battle_won_2.mp3","Scottish_General_Battle_won_1.mp3","Scottish_General_Battle_won_Chivalry_1.mp3","Scottish_General_Battle_won_Chivalry_2.mp3"]),
("scotfg_army_join", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_Joins_Army_1.mp3","Scottish_Army_Joins_Army_2.mp3","Scottish_Army_Joins_Army_3.mp3","Scottish_General_Joins_Army_1.mp3","Scottish_General_Joins_Army_2.mp3","Scottish_General_Joins_Army_3.mp3","Scottish_General_Joins_Army_Chivalry_2.mp3","Scottish_General_Joins_Army_Chivalry_3.mp3","Scottish_General_Joins_Army_Dread_1.mp3","Scottish_General_Joins_Army_Dread_2.mp3","Scottish_General_Joins_Army_Chivalry_1.mp3","Scottish_General_Joins_Army_Dread_3.mp3"]),
("scotfg_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_Leaves_Army_1.mp3","Scottish_Army_Leaves_Army_2.mp3","Scottish_Army_Leaves_Army_3.mp3","Scottish_General_Leaves_Army_1.mp3","Scottish_General_Leaves_Army_2.mp3","Scottish_General_Leaves_Army_3.mp3","Scottish_General_Leaves_Army_Chivalry_1.mp3","Scottish_General_Leaves_Army_Chivalry_2.mp3","Scottish_General_Leaves_Army_Chivalry_3.mp3","Scottish_General_Leaves_Army_Dread_1.mp3","Scottish_General_Leaves_Army_Dread_2.mp3","Scottish_General_Leaves_Army_Dread_3.mp3"]),
("scotfg_capture", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_Settlement_Capture_Celebration_1.mp3","Scottish_Army_Settlement_Capture_Celebration_3.mp3","Scottish_General_Settlement_Capture_Celebration_1.mp3","Scottish_General_Settlement_Capture_Celebration_3.mp3","Scottish_General_Settlement_Capture_Celebration_Chivalry_3.mp3","Scottish_General_Settlement_Capture_Celebration_Dread_1.mp3","Scottish_General_Settlement_Capture_Celebration_Dread_2.mp3","Scottish_General_Settlement_Capture_Celebration_Dread_3.mp3","Scottish_Army_Settlement_Capture_Celebration_2.mp3","Scottish_General_Settlement_Capture_Celebration_2.mp3","Scottish_General_Settlement_Capture_Celebration_Chivalry_1.mp3","Scottish_General_Settlement_Capture_Celebration_Chivalry_2.mp3"]),
("scotfg_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_siege_Begun_1.mp3","Scottish_Army_siege_Begun_2.mp3","Scottish_General_siege_Begun_1.mp3","Scottish_General_siege_Begun_2.mp3","Scottish_General_siege_Begun_Chivalry_1.mp3","Scottish_General_siege_Begun_Chivalry_2.mp3","Scottish_General_siege_Begun_Dread_1.mp3","Scottish_General_siege_Begun_Dread_2.mp3"]),
("scotfg_besieged", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_siege_Besieged_1.mp3","Scottish_Army_siege_Besieged_2.mp3","Scottish_Army_siege_Besieged_3.mp3","Scottish_General_siege_Besieged_1.mp3","Scottish_General_siege_Besieged_2.mp3","Scottish_General_siege_Besieged_3.mp3","Scottish_General_siege_Besieged_Chivalry_1.mp3","Scottish_General_siege_Besieged_Chivalry_2.mp3","Scottish_General_siege_Besieged_Chivalry_3.mp3","Scottish_General_siege_Besieged_Dread_1.mp3","Scottish_General_siege_Besieged_Dread_2.mp3","Scottish_General_siege_Besieged_Dread_3.mp3"]),
("scotfg_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_siege_Ongoing_1.mp3","Scottish_Army_siege_Ongoing_2.mp3","Scottish_Army_siege_Ongoing_3.mp3","Scottish_General_siege_Ongoing_1.mp3","Scottish_General_siege_Ongoing_2.mp3","Scottish_General_siege_Ongoing_3.mp3","Scottish_General_siege_Ongoing_Chivalry_1.mp3","Scottish_General_siege_Ongoing_Chivalry_2.mp3","Scottish_General_siege_Ongoing_Chivalry_3.mp3","Scottish_General_siege_Ongoing_Dread_1.mp3","Scottish_General_siege_Ongoing_Dread_2.mp3","Scottish_General_siege_Ongoing_Dread_3.mp3"]),
#Scotland

("engfg_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["English_Admiral_Attacked_Enemy_1.mp3","English_Admiral_Attacked_Enemy_2.mp3","English_Admiral_Attacked_Enemy_3.mp3"]),
("engfg_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["English_Admiral_Attacking_1.mp3","English_Admiral_Attacking_2.mp3","English_Admiral_Attacking_3.mp3"]),
("engfg_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Attacking_1.mp3","English_Army_Attacking_2.mp3","English_Army_Attacking_3.mp3","English_General_Fight_On_Battle_Map_Chivalry_2.mp3","English_Army_Fight_On_Battle_Map_6.mp3","English_Army_Fight_On_Battle_Map_1.mp3","English_Army_Fight_On_Battle_Map_2.mp3","English_Army_Fight_On_Battle_Map_3.mp3","English_Army_Fight_On_Battle_Map_4.mp3","English_Army_Fight_On_Battle_Map_5.mp3","English_General_Attacking_1.mp3","English_General_Attacking_2.mp3","English_General_Attacking_3.mp3","English_General_Attacking_Chivalry_1.mp3","English_General_Attacking_Chivalry_3.mp3","English_General_Attacking_Dread_1.mp3","English_General_Attacking_Dread_2.mp3","English_General_Attacking_Dread_3.mp3"]),
("engfg_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Battle_lost_retreat_1.mp3","English_Army_Battle_lost_retreat_2.mp3","English_Army_Battle_lost_retreat_3.mp3","English_General_Battle_lost_retreat_1.mp3","English_General_Battle_lost_retreat_2.mp3","English_General_Battle_lost_retreat_3.mp3","English_General_Battle_lost_retreat_Chivalry_1.mp3","English_General_Battle_lost_retreat_Chivalry_2.mp3","English_General_Battle_lost_retreat_Chivalry_3.mp3","English_General_Battle_lost_retreat_Dread_1.mp3","English_General_Battle_lost_retreat_Dread_2.mp3","English_General_Battle_lost_retreat_Dread_3.mp3","English_General_Fight_On_Battle_Map_1.mp3","English_General_Fight_On_Battle_Map_2.mp3","English_General_Fight_On_Battle_Map_3.mp3","English_General_Fight_On_Battle_Map_Chivalry_1.mp3","English_General_Fight_On_Battle_Map_Chivalry_3.mp3","English_General_Fight_On_Battle_Map_Dread_1.mp3","English_General_Fight_On_Battle_Map_Dread_2.mp3","English_General_Fight_On_Battle_Map_Dread_3.mp3"]),
("engfg_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Battle_won_1.mp3","English_Army_Battle_won_2.mp3","English_Army_Battle_won_3.mp3","English_General_Battle_won_1.mp3","English_General_Battle_won_2.mp3","English_General_Battle_won_3.mp3","English_General_Battle_won_Chivalry_1.mp3","English_General_Battle_won_Chivalry_2.mp3","English_General_Battle_won_Chivalry_3.mp3","English_General_Battle_won_Dread_1.mp3","English_General_Battle_won_Dread_2.mp3","English_General_Battle_won_Dread_3.mp3"]),
("engfg_army_join", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Joins_Army_1.mp3","English_Army_Joins_Army_2.mp3","English_Army_Joins_Army_3.mp3","English_General_Joins_Army_1.mp3","English_General_Joins_Army_2.mp3","English_General_Joins_Army_3.mp3","English_General_Joins_Army_Chivalry_1.mp3","English_General_Joins_Army_Chivalry_2.mp3","English_General_Joins_Army_Chivalry_3.mp3","English_General_Joins_Army_Dread_1.mp3","English_General_Joins_Army_Dread_2.mp3","English_General_Joins_Army_Dread_3.mp3"]),
("engfg_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["English_General_Leaves_Army_1.mp3","English_General_Leaves_Army_2.mp3","English_General_Leaves_Army_3.mp3","English_General_Leaves_Army_Chivalry_1.mp3","English_General_Leaves_Army_Chivalry_2.mp3","English_General_Leaves_Army_Chivalry_3.mp3","English_General_Leaves_Army_Dread_1.mp3","English_General_Leaves_Army_Dread_2.mp3","English_General_Leaves_Army_Dread_3.mp3",]),
("engfg_capture", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Settlement_Capture_Celebration_1.mp3","English_Army_Settlement_Capture_Celebration_3.mp3","English_Army_Settlement_Capture_Celebration_2.mp3","English_General_Settlement_Capture_Celebration_1.mp3","English_General_Settlement_Capture_Celebration_2.mp3","English_General_Settlement_Capture_Celebration_3.mp3","English_General_Settlement_Capture_Celebration_Chivalry_1.mp3","English_General_Settlement_Capture_Celebration_Chivalry_2.mp3","English_General_Settlement_Capture_Celebration_Chivalry_3.mp3","English_General_Settlement_Capture_Celebration_Dread_1.mp3","English_General_Settlement_Capture_Celebration_Dread_2.mp3","English_General_Settlement_Capture_Celebration_Dread_3.mp3"]),
("engfg_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_siege_Begun_1.mp3","English_Army_siege_Begun_2.mp3","English_General_siege_Begun_1.mp3","English_General_siege_Begun_2.mp3","English_General_siege_Begun_Chivalry_1.mp3","English_General_siege_Begun_Chivalry_2.mp3","English_General_siege_Begun_Dread_1.mp3","English_General_siege_Begun_Dread_2.mp3"]),
("engfg_besieged", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_siege_Besieged_1.mp3","English_Army_siege_Besieged_2.mp3","English_Army_siege_Besieged_3.mp3","English_General_siege_Besieged_1.mp3","English_General_siege_Besieged_2.mp3","English_General_siege_Besieged_3.mp3","English_General_siege_Besieged_Chivalry_1.mp3","English_General_siege_Besieged_Chivalry_2.mp3","English_General_siege_Besieged_Chivalry_3.mp3","English_General_siege_Besieged_Dread_1.mp3","English_General_siege_Besieged_Dread_2.mp3","English_General_siege_Besieged_Dread_3.mp3"]),
("engfg_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_siege_Ongoing_1.mp3","English_Army_siege_Ongoing_2.mp3","English_Army_siege_Ongoing_3.mp3","English_General_siege_Ongoing_1.mp3","English_General_siege_Ongoing_2.mp3","English_General_siege_Ongoing_3.mp3","English_General_siege_Ongoing_Chivalry_1.mp3","English_General_siege_Ongoing_Chivalry_2.mp3","English_General_siege_Ongoing_Chivalry_3.mp3","English_General_siege_Ongoing_Dread_1.mp3","English_General_siege_Ongoing_Dread_2.mp3","English_General_siege_Ongoing_Dread_3.mp3"]),

#French
("frenchfg_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["French_Admiral_Attacked_Enemy_2.mp3","French_Admiral_Attacked_Enemy_3.mp3"]),
("frenchfg_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["French_Admiral_Attacking_1.mp3","French_Admiral_Attacking_2.mp3"]),
("frenchfg_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["French_General_Attacking_1.mp3","French_Army_Attacking_2.mp3","French_Army_Fight_On_Battle_Map_1.mp3","French_Army_Fight_On_Battle_Map_3.mp3","French_Army_Fight_On_Battle_Map_5.mp3","French_General_Attacking_2.mp3","French_General_Attacking_3.mp3","French_General_Attacking_Chivalry_1.mp3","French_General_Attacking_Chivalry_2.mp3","French_General_Attacking_Dread_1.mp3","French_General_Attacking_Dread_3.mp3","French_General_Fight_On_Battle_Map_3.mp3","French_General_Fight_On_Battle_Map_Chivalry_1.mp3","French_General_Fight_On_Battle_Map_Dread_1.mp3","French_General_Fight_On_Battle_Map_Dread_2.mp3","French_General_Fight_On_Battle_Map_Dread_3.mp3","French_General_Fight_On_Battle_Map_1.mp3", "French_Army_Fight_On_Battle_Map_4.mp3","French_Army_Fight_On_Battle_Map_6.mp3", "French_General_Attacking_Chivalry_3.mp3", "French_General_Fight_On_Battle_Map_2.mp3","French_General_Fight_On_Battle_Map_Chivalry_2.mp3", "French_General_Fight_On_Battle_Map_Chivalry_3.mp3"]),
("frenchfg_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Battle_lost_retreat_1.mp3","French_Army_Battle_lost_retreat_2.mp3","French_General_Battle_lost_retreat_1.mp3","French_General_Battle_lost_retreat_2.mp3","French_General_Battle_lost_retreat_Chivalry_1.mp3","French_General_Battle_lost_retreat_Chivalry_2.mp3","French_General_Battle_lost_retreat_Chivalry_3.mp3","French_General_Battle_lost_retreat_Dread_1.mp3","French_General_Battle_lost_retreat_Dread_2.mp3","French_General_Battle_lost_retreat_Dread_3.mp3"]),
("frenchfg_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["French_General_Battle_won_3.mp3","French_General_Battle_won_Chivalry_1.mp3","French_General_Battle_won_Chivalry_3.mp3","French_General_Battle_won_Dread_1.mp3","French_General_Battle_won_Dread_2.mp3","French_General_Battle_won_Dread_3.mp3","French_General_Battle_won_1.mp3","French_General_Battle_won_Chivalry_2.mp3"]),
("frenchfg_army_join", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Joins_Army_1.mp3","French_Army_Joins_Army_2.mp3","French_Army_Joins_Army_3.mp3","French_General_Joins_Army_1.mp3","French_General_Joins_Army_3.mp3","French_General_Joins_Army_Chivalry_3.mp3","French_General_Joins_Army_Dread_1.mp3","French_General_Joins_Army_Dread_2.mp3","French_General_Joins_Army_Dread_3.mp3"]),
("frenchfg_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Leaves_Army_1.mp3","French_Army_Leaves_Army_2.mp3","French_General_Leaves_Army_1.mp3","French_General_Leaves_Army_2.mp3","French_General_Leaves_Army_3.mp3","French_General_Leaves_Army_Chivalry_1.mp3","French_General_Leaves_Army_Chivalry_2.mp3","French_General_Leaves_Army_Dread_1.mp3","French_General_Leaves_Army_Dread_2.mp3", "French_General_Leaves_Army_Dread_3.mp3"]),
("frenchfg_capture", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Settlement_Capture_Celebration_3.mp3","French_General_Settlement_Capture_Celebration_3.mp3","French_General_Settlement_Capture_Celebration_Dread_1.mp3","French_General_Settlement_Capture_Celebration_Dread_3.mp3","French_Army_Settlement_Capture_Celebration_1.mp3","French_General_Settlement_Capture_Celebration_1.mp3","French_General_Settlement_Capture_Celebration_Chivalry_1.mp3","French_General_Settlement_Capture_Celebration_Chivalry_3.mp3"]),
("frenchfg_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_siege_Begun_2.mp3","French_General_siege_Begun_1.mp3","French_General_siege_Begun_2.mp3","French_General_siege_Begun_Dread_2.mp3","French_General_siege_Begun_Chivalry_2.mp3"]),
("frenchfg_besieged", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_siege_Besieged_1.mp3","French_Army_siege_Besieged_2.mp3","French_General_siege_Besieged_1.mp3","French_General_siege_Besieged_2.mp3","French_General_siege_Besieged_Chivalry_1.mp3","French_General_siege_Besieged_Dread_1.mp3","French_General_siege_Besieged_Dread_2.mp3","French_General_siege_Besieged_Dread_3.mp3","French_General_siege_Besieged_Chivalry_3.mp3"]),
("frenchfg_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_siege_Ongoing_1.mp3","French_Army_siege_Ongoing_3.mp3","French_General_siege_Ongoing_1.mp3","French_General_siege_Ongoing_2.mp3","French_General_siege_Ongoing_Chivalry_3.mp3","French_General_siege_Ongoing_Dread_2.mp3","French_General_siege_Ongoing_Dread_3.mp3"]),
#French

#("fac_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["nss1.mp3","nss2.mp3","nss3.mp3"]),
#("fac_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["nss1.mp3","nss2.mp3","nss3.mp3"]),
#("fac_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["nss1.mp3","nss2.mp3","nss3.mp3","nss4.mp3","nss5.mp3","nss6.mp3","nss7.mp3","nss8.mp3","nss9.mp3","nss10.mp3","nss11.mp3","nss12.mp3","nss13.mp3","nss14.mp3","nss15.mp3","nss16.mp3"]),
#("fac_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["nss1.mp3","nss2.mp3","nss3.mp3","nss4.mp3","nss5.mp3","nss6.mp3","nss7.mp3","nss8.mp3","nss9.mp3","nss10.mp3","nss11.mp3","nss12.mp3","nss13.mp3","nss14.mp3","nss15.mp3","nss16.mp3","nss17.mp3","nss18.mp3","nss19.mp3","nss20.mp3"]),
#("fac_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["nss1.mp3","nss2.mp3","nss3.mp3","nss4.mp3","nss5.mp3","nss6.mp3","nss7.mp3","nss8.mp3","nss9.mp3","nss10.mp3","nss11.mp3","nss12.mp3"]),
#("fac_army_join", sf_2d|sf_priority_10|sf_vol_7, ["nss1.mp3","nss2.mp3","nss3.mp3","nss4.mp3","nss5.mp3","nss6.mp3","nss7.mp3","nss8.mp3","nss9.mp3","nss10.mp3","nss11.mp3","nss12.mp3"]),
#("fac_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["nss1.mp3","nss2.mp3","nss3.mp3","nss4.mp3","nss5.mp3","nss6.mp3","nss7.mp3","nss8.mp3","nss9.mp3"]),
#("fac_capture", sf_2d|sf_priority_10|sf_vol_7, ["nss1.mp3","nss2.mp3","nss3.mp3","nss4.mp3","nss5.mp3","nss6.mp3","nss7.mp3","nss8.mp3","nss9.mp3","nss10.mp3","nss11.mp3"]),
#("fac_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["nss1.mp3","nss2.mp3","nss3.mp3","nss4.mp3","nss5.mp3","nss6.mp3","nss7.mp3","nss8.mp3"]),
#("fac_besieged", sf_2d|sf_priority_10|sf_vol_7, ["nss1.mp3","nss2.mp3","nss3.mp3","nss4.mp3","nss5.mp3","nss6.mp3","nss7.mp3","nss8.mp3","nss9.mp3","nss10.mp3","nss11.mp3","nss12.mp3"]),
#("fac_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["nss1.mp3","nss2.mp3","nss3.mp3","nss4.mp3","nss5.mp3","nss6.mp3","nss7.mp3","nss8.mp3","nss9.mp3","nss10.mp3","nss11.mp3","nss12.mp3"]),





#########Generic King
#Islamics
("arabick_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Admiral_Attacked_Enemy_1.mp3","Arabic_Admiral_Attacked_Enemy_3.mp3","Arabic_Admiral_Attacked_Enemy_2.mp3"]),
("arabick_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Admiral_Attacking_1.mp3","Arabic_Admiral_Attacking_2.mp3","Arabic_Admiral_Attacking_3.mp3"]),
("arabick_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_Attacking_1.mp3","Arabic_Army_Attacking_2.mp3","Arabic_Army_Attacking_3.mp3","Arabic_Army_Fight_On_Battle_Map_1.mp3","Arabic_Army_Fight_On_Battle_Map_2.mp3","Arabic_Army_Fight_On_Battle_Map_3.mp3","Arabic_Army_Fight_On_Battle_Map_4.mp3","Arabic_Army_Fight_On_Battle_Map_5.mp3","Arabic_Army_Fight_On_Battle_Map_6.mp3","Arabic_General_Attacking_2.mp3","Arabic_General_Attacking_3.mp3","Arabic_General_Attacking_Chivalry_1.mp3","Arabic_General_Attacking_Chivalry_3.mp3","Arabic_General_Attacking_Dread_1.mp3","Arabic_General_Attacking_Dread_2.mp3","Arabic_General_Fight_On_Battle_Map_1.mp3","Arabic_General_Fight_On_Battle_Map_2.mp3","Arabic_General_Fight_On_Battle_Map_3.mp3","Arabic_General_Fight_On_Battle_Map_Chivalry_1.mp3","Arabic_General_Fight_On_Battle_Map_Chivalry_2.mp3","Arabic_General_Fight_On_Battle_Map_Chivalry_3.mp3","Arabic_General_Fight_On_Battle_Map_3.mp3","Arabic_General_Fight_On_Battle_Map_Dread_1.mp3","Arabic_General_Fight_On_Battle_Map_Dread_2.mp3","Arabic_General_Fight_On_Battle_Map_Dread_3.mp3","Arabic_General_Attacking_1.mp3","Arabic_General_Attacking_Chivalry_2.mp3","Arabic_General_Attacking_Dread_3.mp3"]),
("arabick_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_Battle_lost_retreat_1.mp3","Arabic_Army_Battle_lost_retreat_2.mp3","Arabic_Army_Battle_lost_retreat_3.mp3","Arabic_General_Battle_lost_retreat_1.mp3","Arabic_General_Battle_lost_retreat_2.mp3","Arabic_General_Battle_lost_retreat_3.mp3","Arabic_General_Battle_lost_retreat_Chivalry_1.mp3","Arabic_General_Battle_lost_retreat_Chivalry_2.mp3","Arabic_General_Battle_lost_retreat_Chivalry_3.mp3","Arabic_General_Battle_lost_retreat_Dread_1.mp3","Arabic_General_Battle_lost_retreat_Dread_2.mp3","Arabic_General_Battle_lost_retreat_Dread_3.mp3"]),
("arabick_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_Battle_won_1.mp3","Arabic_Army_Battle_won_2.mp3","Arabic_General_Battle_won_1.mp3","Arabic_General_Battle_won_2.mp3","Arabic_General_Battle_won_3.mp3","Arabic_General_Battle_won_Chivalry_1.mp3","Arabic_General_Battle_won_Chivalry_2.mp3","Arabic_General_Battle_won_Chivalry_3.mp3","Arabic_General_Battle_won_Dread_2.mp3","Arabic_Army_Battle_won_3.mp3","Arabic_General_Battle_won_Dread_1.mp3","Arabic_General_Battle_won_Dread_3.mp3"]),
("arabick_army_join", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_Joins_Army_1.mp3","Arabic_Army_Joins_Army_2.mp3","Arabic_General_Joins_Army_1.mp3","Arabic_General_Joins_Army_2.mp3","Arabic_General_Joins_Army_Chivalry_2.mp3","Arabic_General_Joins_Army_Chivalry_3.mp3","Arabic_General_Joins_Army_Dread_2.mp3","Arabic_Army_Joins_Army_3.mp3" ,"Arabic_General_Joins_Army_3.mp3","Arabic_General_Joins_Army_Chivalry_1.mp3","Arabic_General_Joins_Army_Dread_1.mp3","Arabic_General_Joins_Army_Dread_3.mp3"]),
("arabick_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_Leaves_Army_1.mp3","Arabic_Army_Leaves_Army_2.mp3","Arabic_General_Leaves_Army_1.mp3","Arabic_General_Leaves_Army_2.mp3","Arabic_General_Leaves_Army_Dread_1.mp3","Arabic_General_Leaves_Army_Dread_3.mp3","Arabic_Army_Leaves_Army_3.mp3","Arabic_General_Leaves_Army_3.mp3","Arabic_General_Leaves_Army_Chivalry_1.mp3" ,"Arabic_General_Leaves_Army_Chivalry_2.mp3","Arabic_General_Leaves_Army_Chivalry_3.mp3","Arabic_General_Leaves_Army_Dread_2.mp3"]),
("arabick_capture", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_Settlement_Capture_Celebration_2.mp3","Arabic_Army_Settlement_Capture_Celebration_3.mp3","Arabic_General_Settlement_Capture_Celebration_2.mp3","Arabic_General_Settlement_Capture_Celebration_3.mp3","Arabic_General_Settlement_Capture_Celebration_Chivalry_1.mp3","Arabic_General_Settlement_Capture_Celebration_Chivalry_2.mp3","Arabic_General_Settlement_Capture_Celebration_Chivalry_3.mp3","Arabic_General_Settlement_Capture_Celebration_Dread_3.mp3","Arabic_Army_Settlement_Capture_Celebration_1.mp3","Arabic_General_Settlement_Capture_Celebration_1.mp3","Arabic_General_Settlement_Capture_Celebration_Dread_1.mp3","Arabic_General_Settlement_Capture_Celebration_Dread_2.mp3"]),
("arabick_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_siege_Begun_2.mp3","Arabic_General_siege_Begun_2.mp3","Arabic_General_siege_Begun_Chivalry_1.mp3","Arabic_General_siege_Begun_Chivalry_2.mp3","Arabic_Army_siege_Begun_1.mp3","Arabic_General_siege_Begun_1.mp3","Arabic_General_siege_Begun_Dread_1.mp3","Arabic_General_siege_Begun_Dread_2.mp3"]),
("arabick_besieged", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_siege_Ongoing_1.mp3","Arabic_General_siege_Besieged_Chivalry_1.mp3","Arabic_General_siege_Besieged_Chivalry_2.mp3","Arabic_General_siege_Besieged_Dread_1.mp3","Arabic_General_siege_Besieged_Dread_2.mp3","Arabic_Army_siege_Besieged_1.mp3","Arabic_Army_siege_Besieged_2.mp3","Arabic_Army_siege_Besieged_3.mp3","Arabic_General_siege_Besieged_1.mp3","Arabic_General_siege_Besieged_2.mp3","Arabic_General_siege_Besieged_3.mp3","Arabic_General_siege_Besieged_Chivalry_3.mp3","Arabic_General_siege_Besieged_Dread_3.mp3"]),
("arabick_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_General_siege_Ongoing_1.mp3","Arabic_Army_siege_Ongoing_2.mp3","Arabic_Army_siege_Ongoing_3.mp3","Arabic_General_siege_Ongoing_2.mp3","Arabic_General_siege_Ongoing_3.mp3","Arabic_General_siege_Ongoing_Chivalry_1.mp3","Arabic_General_siege_Ongoing_Chivalry_2.mp3","Arabic_General_siege_Ongoing_Chivalry_3.mp3","Arabic_General_siege_Ongoing_Dread_1.mp3","Arabic_General_siege_Ongoing_Dread_2.mp3","Arabic_General_siege_Ongoing_Dread_3.mp3"]),
#Islamics

#French
("frenchk_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["French_Admiral_Attacked_Enemy_2.mp3","French_Admiral_Attacked_Enemy_3.mp3","French_Admiral_Attacked_Enemy_1.mp3"]),
("frenchk_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["French_Admiral_Attacking_1.mp3","French_Admiral_Attacking_2.mp3","French_Admiral_Attacking_3.mp3"]),
("frenchk_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Attacking_2.mp3","French_Army_Fight_On_Battle_Map_3.mp3","French_Army_Fight_On_Battle_Map_5.mp3","French_General_Attacking_2.mp3","French_General_Attacking_3.mp3","French_General_Attacking_Chivalry_1.mp3","French_General_Attacking_Chivalry_2.mp3","French_General_Attacking_Dread_1.mp3","French_General_Attacking_Dread_3.mp3","French_General_Fight_On_Battle_Map_3.mp3","French_General_Fight_On_Battle_Map_Chivalry_1.mp3","French_General_Fight_On_Battle_Map_Dread_1.mp3","French_General_Fight_On_Battle_Map_Dread_2.mp3","French_General_Fight_On_Battle_Map_Dread_3.mp3","French_Army_Attacking_1.mp3","French_Army_Attacking_3.mp3"]),
("frenchk_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Battle_lost_retreat_1.mp3","French_Army_Battle_lost_retreat_2.mp3","French_General_Battle_lost_retreat_1.mp3","French_General_Battle_lost_retreat_2.mp3","French_General_Battle_lost_retreat_Chivalry_1.mp3","French_General_Battle_lost_retreat_Chivalry_2.mp3","French_General_Battle_lost_retreat_Chivalry_3.mp3","French_General_Battle_lost_retreat_Dread_1.mp3","French_General_Battle_lost_retreat_Dread_2.mp3","French_General_Battle_lost_retreat_Dread_3.mp3","French_Army_Battle_lost_retreat_3.mp3","French_General_Battle_lost_retreat_3.mp3"]),
("frenchk_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["French_General_Battle_won_3.mp3","French_General_Battle_won_Chivalry_1.mp3","French_General_Battle_won_Chivalry_3.mp3","French_General_Battle_won_Dread_1.mp3","French_General_Battle_won_Dread_2.mp3","French_General_Battle_won_Dread_3.mp3","French_Army_Battle_won_1.mp3","French_General_Battle_won_2.mp3"]),
("frenchk_army_join", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Joins_Army_1.mp3","French_Army_Joins_Army_2.mp3","French_Army_Joins_Army_3.mp3","French_General_Joins_Army_1.mp3","French_General_Joins_Army_3.mp3","French_General_Joins_Army_Chivalry_3.mp3","French_General_Joins_Army_Dread_1.mp3","French_General_Joins_Army_Dread_2.mp3","French_General_Joins_Army_Dread_3.mp3","French_General_Joins_Army_2.mp3","French_General_Joins_Army_Chivalry_1.mp3"]),
("frenchk_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Leaves_Army_1.mp3","French_Army_Leaves_Army_2.mp3","French_General_Leaves_Army_1.mp3","French_General_Leaves_Army_2.mp3","French_General_Leaves_Army_3.mp3","French_General_Leaves_Army_Chivalry_1.mp3","French_General_Leaves_Army_Chivalry_2.mp3","French_General_Leaves_Army_Dread_1.mp3","French_General_Leaves_Army_Dread_2.mp3", "French_General_Leaves_Army_Dread_3.mp3", "French_Army_Leaves_Army_3.mp3", "French_General_Leaves_Army_Chivalry_3.mp3"]),
("frenchk_capture", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Settlement_Capture_Celebration_3.mp3","French_General_Settlement_Capture_Celebration_3.mp3","French_General_Settlement_Capture_Celebration_Dread_1.mp3","French_General_Settlement_Capture_Celebration_Dread_3.mp3","French_Army_Settlement_Capture_Celebration_2.mp3","French_General_Settlement_Capture_Celebration_2.mp3","French_General_Settlement_Capture_Celebration_Chivalry_2.mp3","French_General_Settlement_Capture_Celebration_Dread_2.mp3"]),
("frenchk_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_siege_Begun_2.mp3","French_General_siege_Begun_1.mp3","French_General_siege_Begun_2.mp3","French_General_siege_Begun_Dread_2.mp3","French_Army_siege_Begun_1.mp3","French_General_siege_Begun_Chivalry_1.mp3","French_General_siege_Begun_Dread_1.mp3"]),
("frenchk_besieged", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_siege_Besieged_1.mp3","French_Army_siege_Besieged_2.mp3","French_General_siege_Besieged_1.mp3","French_General_siege_Besieged_2.mp3","French_General_siege_Besieged_Chivalry_1.mp3","French_General_siege_Besieged_Dread_1.mp3","French_General_siege_Besieged_Dread_2.mp3","French_General_siege_Besieged_Dread_3.mp3","French_Army_siege_Besieged_3.mp3","French_General_siege_Besieged_3.mp3","French_General_siege_Besieged_Chivalry_2.mp3"]),
("frenchk_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_siege_Ongoing_1.mp3","French_Army_siege_Ongoing_3.mp3","French_General_siege_Ongoing_1.mp3","French_General_siege_Ongoing_2.mp3","French_General_siege_Ongoing_Chivalry_3.mp3","French_General_siege_Ongoing_Dread_2.mp3","French_General_siege_Ongoing_Dread_3.mp3","French_Army_siege_Ongoing_2.mp3","French_General_siege_Ongoing_3.mp3","French_General_siege_Ongoing_Chivalry_1.mp3","French_General_siege_Ongoing_Chivalry_2.mp3","French_General_siege_Ongoing_Dread_1.mp3"]),
#French



#New factional
##German
#("germanfk_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["German_Admiral_Attacked_Enemy_2.mp3","German_Admiral_Attacked_Enemy_1.mp3","German_Admiral_Attacked_Enemy_3.mp3"]),
#("germanfk_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["German_Admiral_Attacking_2.mp3","German_Admiral_Attacking_1.mp3","German_Admiral_Attacking_3.mp3"]),
#("germanfk_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Attacking_2.mp3","German_Army_Fight_On_Battle_Map_1.mp3","German_Army_Fight_On_Battle_Map_2.mp3","German_Army_Fight_On_Battle_Map_3.mp3","German_Army_Fight_On_Battle_Map_4.mp3","German_Army_Fight_On_Battle_Map_5.mp3","German_General_Attacking_2.mp3","German_General_Attacking_Chivalry_2.mp3","German_General_Attacking_Dread_1.mp3","German_General_Fight_On_Battle_Map_1.mp3","German_General_Fight_On_Battle_Map_2.mp3","German_General_Fight_On_Battle_Map_3.mp3","German_General_Fight_On_Battle_Map_Chivalry_1.mp3","German_General_Fight_On_Battle_Map_Chivalry_2.mp3","German_General_Fight_On_Battle_Map_Chivalry_3.mp3","German_General_Fight_On_Battle_Map_Dread_1.mp3","German_General_Fight_On_Battle_Map_Dread_2.mp3","German_General_Fight_On_Battle_Map_Dread_3.mp3","German_Army_Attacking_1.mp3","German_Army_Attacking_3.mp3","German_Army_Fight_On_Battle_Map_6.mp3","German_General_Attacking_1.mp3","German_General_Attacking_3.mp3","German_General_Attacking_Chivalry_1.mp3","German_General_Attacking_Chivalry_3.mp3","German_General_Attacking_Dread_2.mp3","German_General_Attacking_Dread_3.mp3"]),
#("germanfk_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Battle_lost_retreat_1.mp3","German_Army_Battle_lost_retreat_2.mp3","German_Army_Battle_lost_retreat_3.mp3","German_General_Battle_lost_retreat_1.mp3","German_General_Battle_lost_retreat_2.mp3","German_General_Battle_lost_retreat_3.mp3","German_General_Battle_lost_retreat_Chivalry_1.mp3","German_General_Battle_lost_retreat_Chivalry_2.mp3","German_General_Battle_lost_retreat_Chivalry_3.mp3","German_General_Battle_lost_retreat_Dread_1.mp3","German_General_Battle_lost_retreat_Dread_2.mp3","German_General_Battle_lost_retreat_Dread_3.mp3"]),
#("germanfk_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Battle_won_2.mp3","German_Army_Battle_won_3.mp3","German_General_Battle_won_2.mp3","German_General_Battle_won_3.mp3","German_General_Battle_won_Chivalry_2.mp3","German_General_Battle_won_Chivalry_3.mp3","German_General_Battle_won_Dread_1.mp3","German_General_Battle_won_Dread_3.mp3","German_Army_Battle_won_1.mp3","German_General_Battle_won_1.mp3","German_General_Battle_won_Chivalry_1.mp3","German_General_Battle_won_Dread_2.mp3"]),
#("germanfk_army_join", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Joins_Army_2.mp3","German_General_Joins_Army_2.mp3","German_General_Joins_Army_Dread_2.mp3","German_Army_Joins_Army_1.mp3","German_Army_Joins_Army_3.mp3","German_General_Joins_Army_1.mp3","German_General_Joins_Army_3.mp3","German_General_Joins_Army_Chivalry_1.mp3","German_General_Joins_Army_Chivalry_2.mp3","German_General_Joins_Army_Chivalry_3.mp3","German_General_Joins_Army_Dread_1.mp3","German_General_Joins_Army_Dread_3.mp3"]),
#("germanfk_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Leaves_Army_3.mp3","German_General_Leaves_Army_3.mp3","German_General_Leaves_Army_Chivalry_1.mp3","German_General_Leaves_Army_Dread_2.mp3","German_General_Leaves_Army_Dread_3.mp3","German_Army_Leaves_Army_1.mp3","German_Army_Leaves_Army_2.mp3","German_General_Leaves_Army_1.mp3","German_General_Leaves_Army_2.mp3","German_General_Leaves_Army_Chivalry_2.mp3","German_General_Leaves_Army_Chivalry_3.mp3","German_General_Leaves_Army_Dread_1.mp3"]),
#("germanfk_capture", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Settlement_Capture_Celebration_1.mp3","German_Army_Settlement_Capture_Celebration_3.mp3","German_General_Settlement_Capture_Celebration_Chivalry_1.mp3","German_General_Settlement_Capture_Celebration_Chivalry_3.mp3","German_General_Settlement_Capture_Celebration_Dread_1.mp3","German_General_Settlement_Capture_Celebration_Dread_2.mp3","German_Army_Settlement_Capture_Celebration_2.mp3","German_General_Settlement_Capture_Celebration_1.mp3","German_General_Settlement_Capture_Celebration_2.mp3","German_General_Settlement_Capture_Celebration_3.mp3","German_General_Settlement_Capture_Celebration_Chivalry_2.mp3","German_General_Settlement_Capture_Celebration_Dread_3.mp3"]),
#("germanfk_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["German_General_siege_Begun_Dread_1.mp3", "German_General_siege_Begun_Dread_2.mp3","German_Army_siege_Begun_1.mp3","German_Army_siege_Begun_2.mp3","German_General_siege_Begun_1.mp3","German_General_siege_Begun_2.mp3","German_General_siege_Begun_Chivalry_1.mp3","German_General_siege_Begun_Chivalry_2.mp3"]),
#("germanfk_besieged", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_siege_Besieged_3.mp3","German_General_siege_Besieged_3.mp3","German_General_siege_Besieged_Chivalry_1.mp3","German_General_siege_Besieged_Chivalry_2.mp3","German_General_siege_Besieged_Dread_1.mp3","German_General_siege_Besieged_Dread_3.mp3","German_Army_siege_Besieged_1.mp3","German_Army_siege_Besieged_2.mp3","German_General_siege_Besieged_1.mp3","German_General_siege_Besieged_2.mp3","German_General_siege_Besieged_Chivalry_3.mp3","German_General_siege_Besieged_Dread_2.mp3"]),
#("germanfk_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["German_General_siege_Ongoing_Dread_2.mp3","German_General_siege_Ongoing_Dread_3.mp3","German_Army_siege_Ongoing_1.mp3","German_Army_siege_Ongoing_2.mp3","German_Army_siege_Ongoing_3.mp3","German_General_siege_Ongoing_1.mp3","German_General_siege_Ongoing_2.mp3","German_General_siege_Ongoing_3.mp3","German_General_siege_Ongoing_Chivalry_1.mp3","German_General_siege_Ongoing_Chivalry_2.mp3","German_General_siege_Ongoing_Chivalry_3.mp3","German_General_siege_Ongoing_Dread_1.mp3"]),
##German
#
##German
#("germanfg_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["German_Admiral_Attacked_Enemy_2.mp3"]),
#("germanfg_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["German_Admiral_Attacking_2.mp3"]),
#("germanfg_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Attacking_2.mp3","German_Army_Fight_On_Battle_Map_1.mp3","German_Army_Fight_On_Battle_Map_2.mp3","German_Army_Fight_On_Battle_Map_3.mp3","German_Army_Fight_On_Battle_Map_4.mp3","German_Army_Fight_On_Battle_Map_5.mp3","German_General_Attacking_2.mp3","German_General_Attacking_Chivalry_2.mp3","German_General_Attacking_Dread_1.mp3","German_General_Fight_On_Battle_Map_1.mp3","German_General_Fight_On_Battle_Map_2.mp3","German_General_Fight_On_Battle_Map_3.mp3","German_General_Fight_On_Battle_Map_Chivalry_1.mp3","German_General_Fight_On_Battle_Map_Chivalry_2.mp3","German_General_Fight_On_Battle_Map_Chivalry_3.mp3","German_General_Fight_On_Battle_Map_Dread_1.mp3","German_General_Fight_On_Battle_Map_Dread_2.mp3","German_General_Fight_On_Battle_Map_Dread_3.mp3"]),
#("germanfg_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Battle_lost_retreat_1.mp3","German_Army_Battle_lost_retreat_2.mp3","German_Army_Battle_lost_retreat_3.mp3","German_General_Battle_lost_retreat_1.mp3","German_General_Battle_lost_retreat_2.mp3","German_General_Battle_lost_retreat_3.mp3","German_General_Battle_lost_retreat_Chivalry_1.mp3","German_General_Battle_lost_retreat_Chivalry_2.mp3","German_General_Battle_lost_retreat_Chivalry_3.mp3","German_General_Battle_lost_retreat_Dread_1.mp3","German_General_Battle_lost_retreat_Dread_2.mp3","German_General_Battle_lost_retreat_Dread_3.mp3"]),
#("germanfg_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Battle_won_2.mp3","German_Army_Battle_won_3.mp3","German_General_Battle_won_2.mp3","German_General_Battle_won_3.mp3","German_General_Battle_won_Chivalry_2.mp3","German_General_Battle_won_Chivalry_3.mp3","German_General_Battle_won_Dread_1.mp3","German_General_Battle_won_Dread_3.mp3"]),
#("germanfg_army_join", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Joins_Army_2.mp3","German_General_Joins_Army_2.mp3","German_General_Joins_Army_Dread_2.mp3"]),
#("germanfg_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Leaves_Army_3.mp3","German_General_Leaves_Army_3.mp3","German_General_Leaves_Army_Chivalry_1.mp3","German_General_Leaves_Army_Dread_2.mp3","German_General_Leaves_Army_Dread_3.mp3"]),
#("germanfg_capture", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Settlement_Capture_Celebration_1.mp3","German_Army_Settlement_Capture_Celebration_3.mp3","German_General_Settlement_Capture_Celebration_Chivalry_1.mp3","German_General_Settlement_Capture_Celebration_Chivalry_3.mp3","German_General_Settlement_Capture_Celebration_Dread_1.mp3","German_General_Settlement_Capture_Celebration_Dread_2.mp3"]),
#("germanfg_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["German_General_siege_Begun_Dread_1.mp3","German_General_siege_Begun_Dread_2.mp3"]),
#("germanfg_besieged", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_siege_Besieged_3.mp3","German_General_siege_Besieged_3.mp3","German_General_siege_Besieged_Chivalry_1.mp3","German_General_siege_Besieged_Chivalry_2.mp3","German_General_siege_Besieged_Dread_1.mp3","German_General_siege_Besieged_Dread_3.mp3"]),
#("germanfg_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["German_General_siege_Ongoing_Dread_2.mp3","German_General_siege_Ongoing_Dread_3.mp3"]),
##German
#END FACTIONAL




#German
("germank_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["German_Admiral_Attacked_Enemy_2.mp3","German_Admiral_Attacked_Enemy_1.mp3","German_Admiral_Attacked_Enemy_3.mp3"]),
("germank_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["German_Admiral_Attacking_2.mp3","German_Admiral_Attacking_1.mp3","German_Admiral_Attacking_3.mp3"]),
("germank_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Attacking_2.mp3","German_Army_Fight_On_Battle_Map_1.mp3","German_Army_Fight_On_Battle_Map_2.mp3","German_Army_Fight_On_Battle_Map_3.mp3","German_Army_Fight_On_Battle_Map_4.mp3","German_Army_Fight_On_Battle_Map_5.mp3","German_General_Attacking_2.mp3","German_General_Attacking_Chivalry_2.mp3","German_General_Attacking_Dread_1.mp3","German_General_Fight_On_Battle_Map_1.mp3","German_General_Fight_On_Battle_Map_2.mp3","German_General_Fight_On_Battle_Map_3.mp3","German_General_Fight_On_Battle_Map_Chivalry_1.mp3","German_General_Fight_On_Battle_Map_Chivalry_2.mp3","German_General_Fight_On_Battle_Map_Chivalry_3.mp3","German_General_Fight_On_Battle_Map_Dread_1.mp3","German_General_Fight_On_Battle_Map_Dread_2.mp3","German_General_Fight_On_Battle_Map_Dread_3.mp3","German_Army_Attacking_1.mp3","German_Army_Attacking_3.mp3","German_Army_Fight_On_Battle_Map_6.mp3","German_General_Attacking_1.mp3","German_General_Attacking_3.mp3","German_General_Attacking_Chivalry_1.mp3","German_General_Attacking_Chivalry_3.mp3","German_General_Attacking_Dread_2.mp3","German_General_Attacking_Dread_3.mp3"]),
("germank_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Battle_lost_retreat_1.mp3","German_Army_Battle_lost_retreat_2.mp3","German_Army_Battle_lost_retreat_3.mp3","German_General_Battle_lost_retreat_1.mp3","German_General_Battle_lost_retreat_2.mp3","German_General_Battle_lost_retreat_3.mp3","German_General_Battle_lost_retreat_Chivalry_1.mp3","German_General_Battle_lost_retreat_Chivalry_2.mp3","German_General_Battle_lost_retreat_Chivalry_3.mp3","German_General_Battle_lost_retreat_Dread_1.mp3","German_General_Battle_lost_retreat_Dread_2.mp3","German_General_Battle_lost_retreat_Dread_3.mp3"]),
("germank_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Battle_won_2.mp3","German_Army_Battle_won_3.mp3","German_General_Battle_won_2.mp3","German_General_Battle_won_3.mp3","German_General_Battle_won_Chivalry_2.mp3","German_General_Battle_won_Chivalry_3.mp3","German_General_Battle_won_Dread_1.mp3","German_General_Battle_won_Dread_3.mp3","German_Army_Battle_won_1.mp3","German_General_Battle_won_1.mp3","German_General_Battle_won_Chivalry_1.mp3","German_General_Battle_won_Dread_2.mp3"]),
("germank_army_join", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Joins_Army_2.mp3","German_General_Joins_Army_2.mp3","German_General_Joins_Army_Dread_2.mp3","German_Army_Joins_Army_1.mp3","German_Army_Joins_Army_3.mp3","German_General_Joins_Army_1.mp3","German_General_Joins_Army_3.mp3","German_General_Joins_Army_Chivalry_1.mp3","German_General_Joins_Army_Chivalry_2.mp3","German_General_Joins_Army_Chivalry_3.mp3","German_General_Joins_Army_Dread_1.mp3","German_General_Joins_Army_Dread_3.mp3"]),
("germank_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Leaves_Army_3.mp3","German_General_Leaves_Army_3.mp3","German_General_Leaves_Army_Chivalry_1.mp3","German_General_Leaves_Army_Dread_2.mp3","German_General_Leaves_Army_Dread_3.mp3","German_Army_Leaves_Army_1.mp3","German_Army_Leaves_Army_2.mp3","German_General_Leaves_Army_1.mp3","German_General_Leaves_Army_2.mp3","German_General_Leaves_Army_Chivalry_2.mp3","German_General_Leaves_Army_Chivalry_3.mp3","German_General_Leaves_Army_Dread_1.mp3"]),
("germank_capture", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Settlement_Capture_Celebration_1.mp3","German_Army_Settlement_Capture_Celebration_3.mp3","German_General_Settlement_Capture_Celebration_Chivalry_1.mp3","German_General_Settlement_Capture_Celebration_Chivalry_3.mp3","German_General_Settlement_Capture_Celebration_Dread_1.mp3","German_General_Settlement_Capture_Celebration_Dread_2.mp3","German_Army_Settlement_Capture_Celebration_2.mp3","German_General_Settlement_Capture_Celebration_1.mp3","German_General_Settlement_Capture_Celebration_2.mp3","German_General_Settlement_Capture_Celebration_3.mp3","German_General_Settlement_Capture_Celebration_Chivalry_2.mp3","German_General_Settlement_Capture_Celebration_Dread_3.mp3"]),
("germank_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["German_General_siege_Begun_Dread_1.mp3", "German_General_siege_Begun_Dread_2.mp3","German_Army_siege_Begun_1.mp3","German_Army_siege_Begun_2.mp3","German_General_siege_Begun_1.mp3","German_General_siege_Begun_2.mp3","German_General_siege_Begun_Chivalry_1.mp3","German_General_siege_Begun_Chivalry_2.mp3"]),
("germank_besieged", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_siege_Besieged_3.mp3","German_General_siege_Besieged_3.mp3","German_General_siege_Besieged_Chivalry_1.mp3","German_General_siege_Besieged_Chivalry_2.mp3","German_General_siege_Besieged_Dread_1.mp3","German_General_siege_Besieged_Dread_3.mp3","German_Army_siege_Besieged_1.mp3","German_Army_siege_Besieged_2.mp3","German_General_siege_Besieged_1.mp3","German_General_siege_Besieged_2.mp3","German_General_siege_Besieged_Chivalry_3.mp3","German_General_siege_Besieged_Dread_2.mp3"]),
("germank_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["German_General_siege_Ongoing_Dread_2.mp3","German_General_siege_Ongoing_Dread_3.mp3","German_Army_siege_Ongoing_1.mp3","German_Army_siege_Ongoing_2.mp3","German_Army_siege_Ongoing_3.mp3","German_General_siege_Ongoing_1.mp3","German_General_siege_Ongoing_2.mp3","German_General_siege_Ongoing_3.mp3","German_General_siege_Ongoing_Chivalry_1.mp3","German_General_siege_Ongoing_Chivalry_2.mp3","German_General_siege_Ongoing_Chivalry_3.mp3","German_General_siege_Ongoing_Dread_1.mp3"]),
#German


#English
("engk_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["English_Admiral_Attacked_Enemy_1.mp3","English_Admiral_Attacked_Enemy_2.mp3","English_Admiral_Attacked_Enemy_3.mp3"]),
("engk_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["English_Admiral_Attacking_1.mp3","English_Admiral_Attacking_2.mp3","English_Admiral_Attacking_3.mp3"]),
("engk_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Attacking_1.mp3","English_Army_Attacking_2.mp3","English_Army_Attacking_3.mp3","English_Army_Fight_On_Battle_Map_1.mp3","English_Army_Fight_On_Battle_Map_2.mp3","English_Army_Fight_On_Battle_Map_3.mp3","English_Army_Fight_On_Battle_Map_4.mp3","English_Army_Fight_On_Battle_Map_5.mp3","English_General_Attacking_1.mp3","English_General_Attacking_2.mp3","English_General_Attacking_3.mp3","English_General_Attacking_Chivalry_1.mp3","English_General_Attacking_Chivalry_3.mp3","English_General_Attacking_Dread_1.mp3","English_General_Attacking_Dread_2.mp3","English_General_Attacking_Dread_3.mp3", "English_General_Attacking_Chivalry_2.mp3"]),
("engk_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Battle_lost_retreat_1.mp3","English_Army_Battle_lost_retreat_2.mp3","English_Army_Battle_lost_retreat_3.mp3","English_General_Battle_lost_retreat_1.mp3","English_General_Battle_lost_retreat_2.mp3","English_General_Battle_lost_retreat_3.mp3","English_General_Battle_lost_retreat_Chivalry_1.mp3","English_General_Battle_lost_retreat_Chivalry_2.mp3","English_General_Battle_lost_retreat_Chivalry_3.mp3","English_General_Battle_lost_retreat_Dread_1.mp3","English_General_Battle_lost_retreat_Dread_2.mp3","English_General_Battle_lost_retreat_Dread_3.mp3","English_General_Fight_On_Battle_Map_1.mp3","English_General_Fight_On_Battle_Map_2.mp3","English_General_Fight_On_Battle_Map_3.mp3","English_General_Fight_On_Battle_Map_Chivalry_1.mp3","English_General_Fight_On_Battle_Map_Chivalry_3.mp3","English_General_Fight_On_Battle_Map_Dread_1.mp3","English_General_Fight_On_Battle_Map_Dread_2.mp3","English_General_Fight_On_Battle_Map_Dread_3.mp3"]),
("engk_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Battle_won_1.mp3","English_Army_Battle_won_2.mp3","English_Army_Battle_won_3.mp3","English_General_Battle_won_1.mp3","English_General_Battle_won_2.mp3","English_General_Battle_won_3.mp3","English_General_Battle_won_Chivalry_1.mp3","English_General_Battle_won_Chivalry_2.mp3","English_General_Battle_won_Chivalry_3.mp3","English_General_Battle_won_Dread_1.mp3","English_General_Battle_won_Dread_2.mp3","English_General_Battle_won_Dread_3.mp3"]),
("engk_army_join", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Joins_Army_1.mp3","English_Army_Joins_Army_2.mp3","English_Army_Joins_Army_3.mp3","English_General_Joins_Army_1.mp3","English_General_Joins_Army_2.mp3","English_General_Joins_Army_3.mp3","English_General_Joins_Army_Chivalry_1.mp3","English_General_Joins_Army_Chivalry_2.mp3","English_General_Joins_Army_Chivalry_3.mp3","English_General_Joins_Army_Dread_1.mp3","English_General_Joins_Army_Dread_2.mp3","English_General_Joins_Army_Dread_3.mp3"]),
("engk_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["English_General_Leaves_Army_1.mp3","English_General_Leaves_Army_2.mp3","English_General_Leaves_Army_3.mp3","English_General_Leaves_Army_Chivalry_1.mp3","English_General_Leaves_Army_Chivalry_2.mp3","English_General_Leaves_Army_Chivalry_3.mp3","English_General_Leaves_Army_Dread_1.mp3","English_General_Leaves_Army_Dread_2.mp3","English_General_Leaves_Army_Dread_3.mp3",]),
("engk_capture", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Settlement_Capture_Celebration_1.mp3","English_Army_Settlement_Capture_Celebration_3.mp3","English_General_Settlement_Capture_Celebration_1.mp3","English_General_Settlement_Capture_Celebration_2.mp3","English_General_Settlement_Capture_Celebration_3.mp3","English_General_Settlement_Capture_Celebration_Chivalry_1.mp3","English_General_Settlement_Capture_Celebration_Chivalry_2.mp3","English_General_Settlement_Capture_Celebration_Chivalry_3.mp3","English_General_Settlement_Capture_Celebration_Dread_1.mp3","English_General_Settlement_Capture_Celebration_Dread_2.mp3","English_General_Settlement_Capture_Celebration_Dread_3.mp3"]),
("engk_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_siege_Begun_1.mp3","English_Army_siege_Begun_2.mp3","English_General_siege_Begun_1.mp3","English_General_siege_Begun_2.mp3","English_General_siege_Begun_Chivalry_1.mp3","English_General_siege_Begun_Chivalry_2.mp3","English_General_siege_Begun_Dread_1.mp3","English_General_siege_Begun_Dread_2.mp3"]),
("engk_besieged", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_siege_Besieged_1.mp3","English_Army_siege_Besieged_2.mp3","English_Army_siege_Besieged_3.mp3","English_General_siege_Besieged_1.mp3","English_General_siege_Besieged_2.mp3","English_General_siege_Besieged_3.mp3","English_General_siege_Besieged_Chivalry_1.mp3","English_General_siege_Besieged_Chivalry_2.mp3","English_General_siege_Besieged_Chivalry_3.mp3","English_General_siege_Besieged_Dread_1.mp3","English_General_siege_Besieged_Dread_2.mp3","English_General_siege_Besieged_Dread_3.mp3"]),
("engk_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_siege_Ongoing_1.mp3","English_Army_siege_Ongoing_2.mp3","English_Army_siege_Ongoing_3.mp3","English_General_siege_Ongoing_1.mp3","English_General_siege_Ongoing_2.mp3","English_General_siege_Ongoing_3.mp3","English_General_siege_Ongoing_Chivalry_1.mp3","English_General_siege_Ongoing_Chivalry_2.mp3","English_General_siege_Ongoing_Chivalry_3.mp3","English_General_siege_Ongoing_Dread_1.mp3","English_General_siege_Ongoing_Dread_2.mp3","English_General_siege_Ongoing_Dread_3.mp3"]),
#English


#Eastern Euro
("easternk_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["East_European_Admiral_Attacked_Enemy_1.mp3", "East_European_Admiral_Attacked_Enemy_2.mp3", "East_European_Admiral_Attacked_Enemy_3.mp3"]),
("easternk_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["East_European_Admiral_Attacking_1.mp3", "East_European_Admiral_Attacking_2.mp3", "East_European_Admiral_Attacking_3.mp3"]),
("easternk_army_attacking", sf_2d|sf_priority_10|sf_vol_7, ["East_European_General_Attacking_2.mp3","East_European_Army_Attacking_1.mp3", "East_European_Army_Attacking_2.mp3", "East_European_Army_Attacking_3.mp3", "East_European_Army_Fight_On_Battle_Map_1.mp3", "East_European_Army_Fight_On_Battle_Map_2.mp3", "East_European_Army_Fight_On_Battle_Map_3.mp3", "East_European_Army_Fight_On_Battle_Map_4.mp3", "East_European_Army_Fight_On_Battle_Map_5.mp3", "East_European_Army_Fight_On_Battle_Map_6.mp3",  "East_European_General_Attacking_1.mp3", "East_European_General_Attacking_3.mp3", "East_European_General_Attacking_Chivalry_1.mp3", "East_European_General_Attacking_Chivalry_2.mp3", "East_European_General_Attacking_Chivalry_3.mp3", "East_European_General_Attacking_Dread_1.mp3", "East_European_General_Attacking_Dread_2.mp3", "East_European_General_Attacking_Dread_3.mp3",  "East_European_General_Fight_On_Battle_Map_1.mp3", "East_European_General_Fight_On_Battle_Map_2.mp3",  "East_European_General_Fight_On_Battle_Map_3.mp3", "East_European_General_Fight_On_Battle_Map_Chivalry_1.mp3", "East_European_General_Fight_On_Battle_Map_Chivalry_2.mp3", "East_European_General_Fight_On_Battle_Map_Chivalry_3.mp3", "East_European_General_Fight_On_Battle_Map_Dread_1.mp3", "East_European_General_Fight_On_Battle_Map_Dread_2.mp3", "East_European_General_Fight_On_Battle_Map_Dread_3.mp3"]),
("easternk_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["East_European_General_Battle_lost_retreat_2.mp3","East_European_Army_Battle_lost_retreat_2.mp3", "East_European_Army_Battle_lost_retreat_1.mp3",  "East_European_Army_Battle_lost_retreat_3.mp3",  "East_European_General_Battle_lost_retreat_1.mp3",  "East_European_General_Battle_lost_retreat_3.mp3", "East_European_General_Battle_lost_retreat_Chivalry_1.mp3", "East_European_General_Battle_lost_retreat_Chivalry_2.mp3", "East_European_General_Battle_lost_retreat_Chivalry_3.mp3", "East_European_General_Battle_lost_retreat_Dread_1.mp3", "East_European_General_Battle_lost_retreat_Dread_2.mp3", "East_European_General_Battle_lost_retreat_Dread_3.mp3"]),
("easternk_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["East_European_Army_Battle_won_1.mp3", "East_European_Army_Battle_won_2.mp3", "East_European_Army_Battle_won_3.mp3", "East_European_General_Battle_won_1.mp3", "East_European_General_Battle_won_2.mp3", "East_European_General_Battle_won_3.mp3", "East_European_General_Battle_won_Chivalry_1.mp3", "East_European_General_Battle_won_Chivalry_2.mp3", "East_European_General_Battle_won_Chivalry_3.mp3", "East_European_General_Battle_won_Dread_1.mp3", "East_European_General_Battle_won_Dread_2.mp3", "East_European_General_Battle_won_Dread_3.mp3"]),
("easternk_army_join", sf_2d|sf_priority_10|sf_vol_7, ["East_European_General_Joins_Army_Chivalry_1.mp3", "East_European_General_Joins_Army_Chivalry_2.mp3", "East_European_General_Joins_Army_Chivalry_3.mp3","East_European_Army_Joins_Army_1.mp3", "East_European_Army_Joins_Army_2.mp3", "East_European_Army_Joins_Army_3.mp3", "East_European_General_Joins_Army_1.mp3", "East_European_General_Joins_Army_2.mp3", "East_European_General_Joins_Army_3.mp3", "East_European_General_Joins_Army_Dread_1.mp3", "East_European_General_Joins_Army_Dread_2.mp3"]),
("easternk_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["East_European_General_Leaves_Army_Chivalry_2.mp3","East_European_General_Leaves_Army_Chivalry_1.mp3","East_European_Army_Leaves_Army_2.mp3","East_European_Army_Leaves_Army_1.mp3",  "East_European_Army_Leaves_Army_3.mp3", "East_European_General_Leaves_Army_1.mp3", "East_European_General_Leaves_Army_2.mp3", "East_European_General_Leaves_Army_3.mp3", "East_European_General_Leaves_Army_Dread_1.mp3", "East_European_General_Leaves_Army_Dread_3.mp3"]),
("easternk_capture", sf_2d|sf_priority_10|sf_vol_7, ["East_European_General_Settlement_Capture_Celebration_3.mp3","East_European_Army_Settlement_Capture_Celebration_1.mp3", "East_European_Army_Settlement_Capture_Celebration_2.mp3", "East_European_Army_Settlement_Capture_Celebration_3.mp3", "East_European_General_Settlement_Capture_Celebration_1.mp3", "East_European_General_Settlement_Capture_Celebration_2.mp3", "East_European_General_Settlement_Capture_Celebration_Chivalry_1.mp3", "East_European_General_Settlement_Capture_Celebration_Chivalry_2.mp3", "East_European_General_Settlement_Capture_Celebration_Chivalry_3.mp3", "East_European_General_Settlement_Capture_Celebration_Dread_1.mp3", "East_European_General_Settlement_Capture_Celebration_Dread_2.mp3",]),
("easternk_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["East_European_General_siege_Begun_Chivalry_1.mp3","East_European_General_siege_Begun_Chivalry_2.mp3","East_European_Army_siege_Begun_2.mp3","East_European_Army_siege_Begun_1.mp3", "East_European_General_siege_Begun_1.mp3", "East_European_General_siege_Begun_2.mp3", "East_European_General_siege_Begun_Dread_1.mp3", "East_European_General_siege_Begun_Dread_2.mp3" ]),
("easternk_besieged", sf_2d|sf_priority_10|sf_vol_7, ["East_European_General_siege_Besieged_1.mp3", "East_European_General_siege_Besieged_Chivalry_1.mp3","East_European_Army_siege_Besieged_1.mp3", "East_European_Army_siege_Besieged_2.mp3", "East_European_Army_siege_Besieged_3.mp3", "East_European_General_siege_Besieged_2.mp3", "East_European_General_siege_Besieged_3.mp3", "East_European_General_siege_Besieged_Chivalry_2.mp3", "East_European_General_siege_Besieged_Chivalry_3.mp3", "East_European_General_siege_Besieged_Dread_1.mp3", "East_European_General_siege_Besieged_Dread_2.mp3", "East_European_General_siege_Besieged_Dread_3.mp3"]),
("easternk_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["East_European_General_siege_Ongoing_Dread_3.mp3", "East_European_General_siege_Ongoing_Dread_1.mp3", "East_European_General_siege_Ongoing_Chivalry_2.mp3",  "East_European_General_siege_Ongoing_Chivalry_1.mp3", "East_European_General_siege_Ongoing_2.mp3","East_European_Army_siege_Ongoing_1.mp3", "East_European_Army_siege_Ongoing_2.mp3", "East_European_Army_siege_Ongoing_3.mp3",  "East_European_General_siege_Ongoing_1.mp3", "East_European_General_siege_Ongoing_3.mp3", "East_European_General_siege_Ongoing_1.mp3", "East_European_General_siege_Ongoing_3.mp3",  "East_European_General_siege_Ongoing_Chivalry_3.mp3", "East_European_General_siege_Ongoing_Dread_2.mp3"]),
#Eastern Euro






#########Generic No King

#Scotland
("scotg_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Admiral_Attacked_Enemy_1.mp3","Scottish_Admiral_Attacked_Enemy_2.mp3","Scottish_Admiral_Attacked_Enemy_3.mp3"]),
("scotg_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Admiral_Attacking_1.mp3","Scottish_Admiral_Attacking_2.mp3","Scottish_Admiral_Attacking_3.mp3"]),
("scotg_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_Attacking_1.mp3","Scottish_Army_Attacking_2.mp3","Scottish_Army_Attacking_3.mp3","Scottish_Army_Fight_On_Battle_Map_1.mp3","Scottish_Army_Fight_On_Battle_Map_6.mp3","Scottish_General_Attacking_1.mp3","Scottish_General_Attacking_2.mp3","Scottish_General_Attacking_3.mp3","Scottish_General_Attacking_Chivalry_1.mp3","Scottish_General_Attacking_Chivalry_3.mp3","Scottish_General_Attacking_Dread_1.mp3","Scottish_General_Attacking_Dread_2.mp3","Scottish_General_Attacking_Dread_3.mp3","Scottish_General_Fight_On_Battle_Map_Dread_1.mp3","Scottish_General_Fight_On_Battle_Map_Dread_2.mp3","Scottish_General_Fight_On_Battle_Map_Dread_3.mp3"]),
("scotg_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_Battle_lost_retreat_1.mp3","Scottish_Army_Battle_lost_retreat_2.mp3","Scottish_Army_Battle_lost_retreat_3.mp3","Scottish_General_Battle_lost_retreat_1.mp3","Scottish_General_Battle_lost_retreat_2.mp3","Scottish_General_Battle_lost_retreat_3.mp3","Scottish_General_Battle_lost_retreat_Chivalry_1.mp3","Scottish_General_Battle_lost_retreat_Chivalry_2.mp3","Scottish_General_Battle_lost_retreat_Chivalry_3.mp3","Scottish_General_Battle_lost_retreat_Dread_1.mp3","Scottish_General_Battle_lost_retreat_Dread_2.mp3","Scottish_General_Battle_lost_retreat_Dread_3.mp3"]),
("scotg_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_Battle_won_1.mp3","Scottish_Army_Battle_won_3.mp3","Scottish_General_Battle_won_2.mp3","Scottish_General_Battle_won_3.mp3","Scottish_General_Battle_won_Dread_1.mp3","Scottish_General_Battle_won_Dread_2.mp3","Scottish_General_Battle_won_Dread_3.mp3"]),
("scotg_army_join", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_Joins_Army_1.mp3","Scottish_Army_Joins_Army_2.mp3","Scottish_Army_Joins_Army_3.mp3","Scottish_General_Joins_Army_1.mp3","Scottish_General_Joins_Army_2.mp3","Scottish_General_Joins_Army_3.mp3","Scottish_General_Joins_Army_Chivalry_2.mp3","Scottish_General_Joins_Army_Chivalry_3.mp3","Scottish_General_Joins_Army_Dread_1.mp3","Scottish_General_Joins_Army_Dread_2.mp3"]),
("scotg_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_Leaves_Army_1.mp3","Scottish_Army_Leaves_Army_2.mp3","Scottish_Army_Leaves_Army_3.mp3","Scottish_General_Leaves_Army_1.mp3","Scottish_General_Leaves_Army_2.mp3","Scottish_General_Leaves_Army_3.mp3","Scottish_General_Leaves_Army_Chivalry_1.mp3","Scottish_General_Leaves_Army_Chivalry_2.mp3","Scottish_General_Leaves_Army_Chivalry_3.mp3","Scottish_General_Leaves_Army_Dread_1.mp3","Scottish_General_Leaves_Army_Dread_2.mp3","Scottish_General_Leaves_Army_Dread_3.mp3"]),
("scotg_capture", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_Settlement_Capture_Celebration_1.mp3","Scottish_Army_Settlement_Capture_Celebration_3.mp3","Scottish_General_Settlement_Capture_Celebration_1.mp3","Scottish_General_Settlement_Capture_Celebration_3.mp3","Scottish_General_Settlement_Capture_Celebration_Chivalry_3.mp3","Scottish_General_Settlement_Capture_Celebration_Dread_1.mp3","Scottish_General_Settlement_Capture_Celebration_Dread_2.mp3","Scottish_General_Settlement_Capture_Celebration_Dread_3.mp3"]),
("scotg_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_siege_Begun_1.mp3","Scottish_Army_siege_Begun_2.mp3","Scottish_General_siege_Begun_1.mp3","Scottish_General_siege_Begun_2.mp3","Scottish_General_siege_Begun_Chivalry_1.mp3","Scottish_General_siege_Begun_Chivalry_2.mp3","Scottish_General_siege_Begun_Dread_1.mp3","Scottish_General_siege_Begun_Dread_2.mp3"]),
("scotg_besieged", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_siege_Besieged_1.mp3","Scottish_Army_siege_Besieged_2.mp3","Scottish_Army_siege_Besieged_3.mp3","Scottish_General_siege_Besieged_1.mp3","Scottish_General_siege_Besieged_2.mp3","Scottish_General_siege_Besieged_3.mp3","Scottish_General_siege_Besieged_Chivalry_1.mp3","Scottish_General_siege_Besieged_Chivalry_2.mp3","Scottish_General_siege_Besieged_Chivalry_3.mp3","Scottish_General_siege_Besieged_Dread_1.mp3","Scottish_General_siege_Besieged_Dread_2.mp3","Scottish_General_siege_Besieged_Dread_3.mp3"]),
("scotg_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["Scottish_Army_siege_Ongoing_1.mp3","Scottish_Army_siege_Ongoing_2.mp3","Scottish_Army_siege_Ongoing_3.mp3","Scottish_General_siege_Ongoing_1.mp3","Scottish_General_siege_Ongoing_2.mp3","Scottish_General_siege_Ongoing_3.mp3","Scottish_General_siege_Ongoing_Chivalry_1.mp3","Scottish_General_siege_Ongoing_Chivalry_2.mp3","Scottish_General_siege_Ongoing_Chivalry_3.mp3","Scottish_General_siege_Ongoing_Dread_1.mp3","Scottish_General_siege_Ongoing_Dread_2.mp3","Scottish_General_siege_Ongoing_Dread_3.mp3"]),
#Scotland

#Mediterranean
("medig_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["Mediterranean_Admiral_Attacked_Enemy_1.mp3","Mediterranean_Admiral_Attacked_Enemy_2.mp3","Mediterranean_Admiral_Attacked_Enemy_3.mp3"]),
("medig_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["Mediterranean_Admiral_Attacking_1.mp3","Mediterranean_Admiral_Attacking_2.mp3","Mediterranean_Admiral_Attacking_3.mp3"]),
("medig_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["Mediterranean_Army_Attacking_1.mp3","Mediterranean_Army_Attacking_2.mp3","Mediterranean_Army_Attacking_3.mp3","Mediterranean_Army_Fight_On_Battle_Map_1.mp3","Mediterranean_Army_Fight_On_Battle_Map_2.mp3","Mediterranean_Army_Fight_On_Battle_Map_3.mp3","Mediterranean_Army_Fight_On_Battle_Map_4.mp3","Mediterranean_Army_Fight_On_Battle_Map_5.mp3","Mediterranean_Army_Fight_On_Battle_Map_6.mp3","Mediterranean_General_Attacking_1.mp3","Mediterranean_General_Attacking_2.mp3","Mediterranean_General_Attacking_3.mp3","Mediterranean_General_Attacking_Chivalry_1.mp3","Mediterranean_General_Attacking_Chivalry_2.mp3","Mediterranean_General_Attacking_Chivalry_3.mp3","Mediterranean_General_Attacking_Dread_1.mp3","Mediterranean_General_Attacking_Dread_2.mp3","Mediterranean_General_Attacking_Dread_3.mp3"     ,"Mediterranean_General_Fight_On_Battle_Map_1.mp3","Mediterranean_General_Fight_On_Battle_Map_2.mp3","Mediterranean_General_Fight_On_Battle_Map_3.mp3","Mediterranean_General_Fight_On_Battle_Map_Chivalry_1.mp3","Mediterranean_General_Fight_On_Battle_Map_Chivalry_2.mp3","Mediterranean_General_Fight_On_Battle_Map_Chivalry_3.mp3","Mediterranean_General_Fight_On_Battle_Map_Dread_1.mp3","Mediterranean_General_Fight_On_Battle_Map_Dread_2.mp3","Mediterranean_General_Fight_On_Battle_Map_Dread_3.mp3"]),
("medig_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["Mediterranean_Army_Battle_lost_retreat_1.mp3","Mediterranean_Army_Battle_lost_retreat_2.mp3","Mediterranean_Army_Battle_lost_retreat_3.mp3","Mediterranean_General_Battle_lost_retreat_1.mp3","Mediterranean_General_Battle_lost_retreat_2.mp3","Mediterranean_General_Battle_lost_retreat_3.mp3","Mediterranean_General_Battle_lost_retreat_Chivalry_1.mp3","Mediterranean_General_Battle_lost_retreat_Chivalry_2.mp3","Mediterranean_General_Battle_lost_retreat_Chivalry_3.mp3","Mediterranean_General_Battle_lost_retreat_Dread_1.mp3","Mediterranean_General_Battle_lost_retreat_Dread_2.mp3","Mediterranean_General_Battle_lost_retreat_Dread_3.mp3"]),
("medig_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["Mediterranean_Army_Battle_won_1.mp3","Mediterranean_Army_Battle_won_2.mp3","Mediterranean_Army_Battle_won_3.mp3","Mediterranean_General_Battle_won_1.mp3","Mediterranean_General_Battle_won_2.mp3","Mediterranean_General_Battle_won_3.mp3","Mediterranean_General_Battle_won_Chivalry_1.mp3","Mediterranean_General_Battle_won_Chivalry_2.mp3","Mediterranean_General_Battle_won_Chivalry_3.mp3","Mediterranean_General_Battle_won_Dread_1.mp3","Mediterranean_General_Battle_won_Dread_2.mp3","Mediterranean_General_Battle_won_Dread_3.mp3"]),
("medig_army_join", sf_2d|sf_priority_10|sf_vol_7, ["Mediterranean_Army_Joins_Army_1.mp3","Mediterranean_Army_Joins_Army_2.mp3","Mediterranean_Army_Joins_Army_3.mp3","Mediterranean_General_Joins_Army_1.mp3","Mediterranean_General_Joins_Army_2.mp3","Mediterranean_General_Joins_Army_3.mp3","Mediterranean_General_Joins_Army_Chivalry_1.mp3","Mediterranean_General_Joins_Army_Chivalry_2.mp3","Mediterranean_General_Joins_Army_Chivalry_3.mp3","Mediterranean_General_Joins_Army_Dread_1.mp3","Mediterranean_General_Joins_Army_Dread_2.mp3","Mediterranean_General_Joins_Army_Dread_3.mp3"]),
("medig_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["Mediterranean_Army_Leaves_Army_1.mp3","Mediterranean_Army_Leaves_Army_2.mp3","Mediterranean_Army_Leaves_Army_3.mp3","Mediterranean_General_Leaves_Army_1.mp3","Mediterranean_General_Leaves_Army_2.mp3","Mediterranean_General_Leaves_Army_3.mp3","Mediterranean_General_Leaves_Army_Chivalry_1.mp3","Mediterranean_General_Leaves_Army_Chivalry_2.mp3","Mediterranean_General_Leaves_Army_Chivalry_3.mp3"         ,"Mediterranean_General_Leaves_Army_Dread_1.mp3","Mediterranean_General_Leaves_Army_Dread_2.mp3","Mediterranean_General_Leaves_Army_Dread_3.mp3"]),
("medig_capture", sf_2d|sf_priority_10|sf_vol_7, ["Mediterranean_Army_Settlement_Capture_Celebration_1.mp3","Mediterranean_Army_Settlement_Capture_Celebration_2.mp3","Mediterranean_Army_Settlement_Capture_Celebration_3.mp3","Mediterranean_General_Settlement_Capture_Celebration_1.mp3","Mediterranean_General_Settlement_Capture_Celebration_2.mp3","Mediterranean_General_Settlement_Capture_Celebration_3.mp3","Mediterranean_General_Settlement_Capture_Celebration_Chivalry_1.mp3","Mediterranean_General_Settlement_Capture_Celebration_Chivalry_2.mp3","Mediterranean_General_Settlement_Capture_Celebration_Chivalry_3.mp3","Mediterranean_General_Settlement_Capture_Celebration_Dread_1.mp3","Mediterranean_General_Settlement_Capture_Celebration_Dread_2.mp3","Mediterranean_General_Settlement_Capture_Celebration_Dread_3.mp3"]),
("medig_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["Mediterranean_Army_siege_Begun_1.mp3","Mediterranean_Army_siege_Begun_2.mp3","Mediterranean_General_siege_Begun_1.mp3","Mediterranean_General_siege_Begun_2.mp3","Mediterranean_General_siege_Begun_Chivalry_1.mp3","Mediterranean_General_siege_Begun_Chivalry_2.mp3","Mediterranean_General_siege_Begun_Dread_1.mp3","Mediterranean_General_siege_Begun_Dread_2.mp3"]),
("medig_besieged", sf_2d|sf_priority_10|sf_vol_7, ["Mediterranean_Army_siege_Besieged_1.mp3","Mediterranean_Army_siege_Besieged_2.mp3","Mediterranean_Army_siege_Besieged_3.mp3","Mediterranean_General_siege_Besieged_1.mp3","Mediterranean_General_siege_Besieged_2.mp3","Mediterranean_General_siege_Besieged_3.mp3","Mediterranean_General_siege_Besieged_Chivalry_1.mp3","Mediterranean_General_siege_Besieged_Chivalry_2.mp3","Mediterranean_General_siege_Besieged_Chivalry_3.mp3","Mediterranean_General_siege_Besieged_Dread_1.mp3","Mediterranean_General_siege_Besieged_Dread_2.mp3","Mediterranean_General_siege_Besieged_Dread_3.mp3"]),
("medig_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["Mediterranean_Army_siege_Ongoing_1.mp3","Mediterranean_Army_siege_Ongoing_2.mp3","Mediterranean_Army_siege_Ongoing_3.mp3","Mediterranean_General_siege_Ongoing_1.mp3","Mediterranean_General_siege_Ongoing_2.mp3","Mediterranean_General_siege_Ongoing_3.mp3","Mediterranean_General_siege_Ongoing_Chivalry_1.mp3","Mediterranean_General_siege_Ongoing_Chivalry_2.mp3","Mediterranean_General_siege_Ongoing_Chivalry_3.mp3","Mediterranean_General_siege_Ongoing_Dread_1.mp3","Mediterranean_General_siege_Ongoing_Dread_2.mp3","Mediterranean_General_siege_Ongoing_Dread_3.mp3"]),
#Mediterranen

#Islamics
("arabicg_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Admiral_Attacked_Enemy_1.mp3","Arabic_Admiral_Attacked_Enemy_3.mp3"]),
("arabicg_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Admiral_Attacking_1.mp3","Arabic_Admiral_Attacking_2.mp3"]),
("arabicg_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_Attacking_1.mp3","Arabic_Army_Attacking_2.mp3","Arabic_Army_Attacking_3.mp3","Arabic_Army_Fight_On_Battle_Map_1.mp3","Arabic_Army_Fight_On_Battle_Map_2.mp3","Arabic_Army_Fight_On_Battle_Map_3.mp3","Arabic_Army_Fight_On_Battle_Map_4.mp3","Arabic_Army_Fight_On_Battle_Map_5.mp3","Arabic_Army_Fight_On_Battle_Map_6.mp3","Arabic_General_Attacking_2.mp3","Arabic_General_Attacking_3.mp3","Arabic_General_Attacking_Chivalry_1.mp3","Arabic_General_Attacking_Chivalry_3.mp3","Arabic_General_Attacking_Dread_1.mp3","Arabic_General_Attacking_Dread_2.mp3","Arabic_General_Fight_On_Battle_Map_1.mp3","Arabic_General_Fight_On_Battle_Map_2.mp3","Arabic_General_Fight_On_Battle_Map_3.mp3","Arabic_General_Fight_On_Battle_Map_Chivalry_1.mp3","Arabic_General_Fight_On_Battle_Map_Chivalry_2.mp3","Arabic_General_Fight_On_Battle_Map_Chivalry_3.mp3","Arabic_General_Fight_On_Battle_Map_3.mp3","Arabic_General_Fight_On_Battle_Map_Dread_1.mp3","Arabic_General_Fight_On_Battle_Map_Dread_2.mp3","Arabic_General_Fight_On_Battle_Map_Dread_3.mp3"]),
("arabicg_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_Battle_lost_retreat_1.mp3","Arabic_Army_Battle_lost_retreat_2.mp3","Arabic_Army_Battle_lost_retreat_3.mp3","Arabic_General_Battle_lost_retreat_1.mp3","Arabic_General_Battle_lost_retreat_2.mp3","Arabic_General_Battle_lost_retreat_3.mp3","Arabic_General_Battle_lost_retreat_Chivalry_1.mp3","Arabic_General_Battle_lost_retreat_Chivalry_2.mp3","Arabic_General_Battle_lost_retreat_Chivalry_3.mp3","Arabic_General_Battle_lost_retreat_Dread_1.mp3","Arabic_General_Battle_lost_retreat_Dread_2.mp3","Arabic_General_Battle_lost_retreat_Dread_3.mp3"]),
("arabicg_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_Battle_won_1.mp3","Arabic_Army_Battle_won_2.mp3","Arabic_General_Battle_won_1.mp3","Arabic_General_Battle_won_2.mp3","Arabic_General_Battle_won_3.mp3","Arabic_General_Battle_won_Chivalry_1.mp3","Arabic_General_Battle_won_Chivalry_2.mp3","Arabic_General_Battle_won_Chivalry_3.mp3","Arabic_General_Battle_won_Dread_2.mp3"]),
("arabicg_army_join", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_Joins_Army_1.mp3","Arabic_Army_Joins_Army_2.mp3","Arabic_General_Joins_Army_1.mp3","Arabic_General_Joins_Army_2.mp3","Arabic_General_Joins_Army_Chivalry_2.mp3","Arabic_General_Joins_Army_Chivalry_3.mp3","Arabic_General_Joins_Army_Dread_2.mp3"]),
("arabicg_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_Leaves_Army_1.mp3","Arabic_Army_Leaves_Army_2.mp3","Arabic_General_Leaves_Army_1.mp3","Arabic_General_Leaves_Army_2.mp3","Arabic_General_Leaves_Army_Dread_1.mp3","Arabic_General_Leaves_Army_Dread_3.mp3"]),
("arabicg_capture", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_Settlement_Capture_Celebration_2.mp3","Arabic_Army_Settlement_Capture_Celebration_3.mp3","Arabic_General_Settlement_Capture_Celebration_2.mp3","Arabic_General_Settlement_Capture_Celebration_3.mp3","Arabic_General_Settlement_Capture_Celebration_Chivalry_1.mp3","Arabic_General_Settlement_Capture_Celebration_Chivalry_2.mp3","Arabic_General_Settlement_Capture_Celebration_Chivalry_3.mp3","Arabic_General_Settlement_Capture_Celebration_Dread_3.mp3"]),
("arabicg_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_siege_Begun_2.mp3","Arabic_General_siege_Begun_2.mp3","Arabic_General_siege_Begun_Chivalry_1.mp3","Arabic_General_siege_Begun_Chivalry_2.mp3"]),
("arabicg_besieged", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_Army_siege_Ongoing_1.mp3","Arabic_General_siege_Besieged_Chivalry_1.mp3","Arabic_General_siege_Besieged_Chivalry_2.mp3","Arabic_General_siege_Besieged_Dread_1.mp3","Arabic_General_siege_Besieged_Dread_2.mp3"]),
("arabicg_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["Arabic_General_siege_Ongoing_1.mp3"]),
#Islamics

#German
("germang_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["German_Admiral_Attacked_Enemy_2.mp3"]),
("germang_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["German_Admiral_Attacking_2.mp3"]),
("germang_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Attacking_2.mp3","German_Army_Fight_On_Battle_Map_1.mp3","German_Army_Fight_On_Battle_Map_2.mp3","German_Army_Fight_On_Battle_Map_3.mp3","German_Army_Fight_On_Battle_Map_4.mp3","German_Army_Fight_On_Battle_Map_5.mp3","German_General_Attacking_2.mp3","German_General_Attacking_Chivalry_2.mp3","German_General_Attacking_Dread_1.mp3","German_General_Fight_On_Battle_Map_1.mp3","German_General_Fight_On_Battle_Map_2.mp3","German_General_Fight_On_Battle_Map_3.mp3","German_General_Fight_On_Battle_Map_Chivalry_1.mp3","German_General_Fight_On_Battle_Map_Chivalry_2.mp3","German_General_Fight_On_Battle_Map_Chivalry_3.mp3","German_General_Fight_On_Battle_Map_Dread_1.mp3","German_General_Fight_On_Battle_Map_Dread_2.mp3","German_General_Fight_On_Battle_Map_Dread_3.mp3"]),
("germang_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Battle_lost_retreat_1.mp3","German_Army_Battle_lost_retreat_2.mp3","German_Army_Battle_lost_retreat_3.mp3","German_General_Battle_lost_retreat_1.mp3","German_General_Battle_lost_retreat_2.mp3","German_General_Battle_lost_retreat_3.mp3","German_General_Battle_lost_retreat_Chivalry_1.mp3","German_General_Battle_lost_retreat_Chivalry_2.mp3","German_General_Battle_lost_retreat_Chivalry_3.mp3","German_General_Battle_lost_retreat_Dread_1.mp3","German_General_Battle_lost_retreat_Dread_2.mp3","German_General_Battle_lost_retreat_Dread_3.mp3"]),
("germang_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Battle_won_2.mp3","German_Army_Battle_won_3.mp3","German_General_Battle_won_2.mp3","German_General_Battle_won_3.mp3","German_General_Battle_won_Chivalry_2.mp3","German_General_Battle_won_Chivalry_3.mp3","German_General_Battle_won_Dread_1.mp3","German_General_Battle_won_Dread_3.mp3"]),
("germang_army_join", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Joins_Army_2.mp3","German_General_Joins_Army_2.mp3","German_General_Joins_Army_Dread_2.mp3"]),
("germang_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Leaves_Army_3.mp3","German_General_Leaves_Army_3.mp3","German_General_Leaves_Army_Chivalry_1.mp3","German_General_Leaves_Army_Dread_2.mp3","German_General_Leaves_Army_Dread_3.mp3"]),
("germang_capture", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_Settlement_Capture_Celebration_1.mp3","German_Army_Settlement_Capture_Celebration_3.mp3","German_General_Settlement_Capture_Celebration_Chivalry_1.mp3","German_General_Settlement_Capture_Celebration_Chivalry_3.mp3","German_General_Settlement_Capture_Celebration_Dread_1.mp3","German_General_Settlement_Capture_Celebration_Dread_2.mp3"]),
("germang_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["German_General_siege_Begun_Dread_1.mp3","German_General_siege_Begun_Dread_2.mp3"]),
("germang_besieged", sf_2d|sf_priority_10|sf_vol_7, ["German_Army_siege_Besieged_3.mp3","German_General_siege_Besieged_3.mp3","German_General_siege_Besieged_Chivalry_1.mp3","German_General_siege_Besieged_Chivalry_2.mp3","German_General_siege_Besieged_Dread_1.mp3","German_General_siege_Besieged_Dread_3.mp3"]),
("germang_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["German_General_siege_Ongoing_Dread_2.mp3","German_General_siege_Ongoing_Dread_3.mp3"]),
#German

#English
("engg_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["English_Admiral_Attacked_Enemy_1.mp3","English_Admiral_Attacked_Enemy_2.mp3","English_Admiral_Attacked_Enemy_3.mp3"]),
("engg_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["English_Admiral_Attacking_1.mp3","English_Admiral_Attacking_2.mp3","English_Admiral_Attacking_3.mp3"]),
("engg_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Attacking_1.mp3","English_Army_Attacking_2.mp3","English_Army_Attacking_3.mp3","English_Army_Fight_On_Battle_Map_1.mp3","English_Army_Fight_On_Battle_Map_2.mp3","English_Army_Fight_On_Battle_Map_3.mp3","English_Army_Fight_On_Battle_Map_4.mp3","English_Army_Fight_On_Battle_Map_5.mp3","English_General_Attacking_1.mp3","English_General_Attacking_2.mp3","English_General_Attacking_3.mp3","English_General_Attacking_Chivalry_1.mp3","English_General_Attacking_Chivalry_3.mp3","English_General_Attacking_Dread_1.mp3","English_General_Attacking_Dread_2.mp3","English_General_Attacking_Dread_3.mp3"]),
("engg_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Battle_lost_retreat_1.mp3","English_Army_Battle_lost_retreat_2.mp3","English_Army_Battle_lost_retreat_3.mp3","English_General_Battle_lost_retreat_1.mp3","English_General_Battle_lost_retreat_2.mp3","English_General_Battle_lost_retreat_3.mp3","English_General_Battle_lost_retreat_Chivalry_1.mp3","English_General_Battle_lost_retreat_Chivalry_2.mp3","English_General_Battle_lost_retreat_Chivalry_3.mp3","English_General_Battle_lost_retreat_Dread_1.mp3","English_General_Battle_lost_retreat_Dread_2.mp3","English_General_Battle_lost_retreat_Dread_3.mp3","English_General_Fight_On_Battle_Map_1.mp3","English_General_Fight_On_Battle_Map_2.mp3","English_General_Fight_On_Battle_Map_3.mp3","English_General_Fight_On_Battle_Map_Chivalry_1.mp3","English_General_Fight_On_Battle_Map_Chivalry_3.mp3","English_General_Fight_On_Battle_Map_Dread_1.mp3","English_General_Fight_On_Battle_Map_Dread_2.mp3","English_General_Fight_On_Battle_Map_Dread_3.mp3"]),
("engg_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Battle_won_1.mp3","English_Army_Battle_won_2.mp3","English_Army_Battle_won_3.mp3","English_General_Battle_won_1.mp3","English_General_Battle_won_2.mp3","English_General_Battle_won_3.mp3","English_General_Battle_won_Chivalry_1.mp3","English_General_Battle_won_Chivalry_2.mp3","English_General_Battle_won_Chivalry_3.mp3","English_General_Battle_won_Dread_1.mp3","English_General_Battle_won_Dread_2.mp3","English_General_Battle_won_Dread_3.mp3"]),
("engg_army_join", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Joins_Army_1.mp3","English_Army_Joins_Army_2.mp3","English_Army_Joins_Army_3.mp3","English_General_Joins_Army_1.mp3","English_General_Joins_Army_2.mp3","English_General_Joins_Army_3.mp3","English_General_Joins_Army_Chivalry_1.mp3","English_General_Joins_Army_Chivalry_2.mp3","English_General_Joins_Army_Chivalry_3.mp3","English_General_Joins_Army_Dread_1.mp3","English_General_Joins_Army_Dread_2.mp3","English_General_Joins_Army_Dread_3.mp3"]),
("engg_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["English_General_Leaves_Army_1.mp3","English_General_Leaves_Army_2.mp3","English_General_Leaves_Army_3.mp3","English_General_Leaves_Army_Chivalry_1.mp3","English_General_Leaves_Army_Chivalry_2.mp3","English_General_Leaves_Army_Chivalry_3.mp3","English_General_Leaves_Army_Dread_1.mp3","English_General_Leaves_Army_Dread_2.mp3","English_General_Leaves_Army_Dread_3.mp3",]),
("engg_capture", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_Settlement_Capture_Celebration_1.mp3","English_Army_Settlement_Capture_Celebration_3.mp3","English_General_Settlement_Capture_Celebration_1.mp3","English_General_Settlement_Capture_Celebration_2.mp3","English_General_Settlement_Capture_Celebration_3.mp3","English_General_Settlement_Capture_Celebration_Chivalry_1.mp3","English_General_Settlement_Capture_Celebration_Chivalry_2.mp3","English_General_Settlement_Capture_Celebration_Chivalry_3.mp3","English_General_Settlement_Capture_Celebration_Dread_1.mp3","English_General_Settlement_Capture_Celebration_Dread_2.mp3","English_General_Settlement_Capture_Celebration_Dread_3.mp3"]),
("engg_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_siege_Begun_1.mp3","English_Army_siege_Begun_2.mp3","English_General_siege_Begun_1.mp3","English_General_siege_Begun_2.mp3","English_General_siege_Begun_Chivalry_1.mp3","English_General_siege_Begun_Chivalry_2.mp3","English_General_siege_Begun_Dread_1.mp3","English_General_siege_Begun_Dread_2.mp3"]),
("engg_besieged", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_siege_Besieged_1.mp3","English_Army_siege_Besieged_2.mp3","English_Army_siege_Besieged_3.mp3","English_General_siege_Besieged_1.mp3","English_General_siege_Besieged_2.mp3","English_General_siege_Besieged_3.mp3","English_General_siege_Besieged_Chivalry_1.mp3","English_General_siege_Besieged_Chivalry_2.mp3","English_General_siege_Besieged_Chivalry_3.mp3","English_General_siege_Besieged_Dread_1.mp3","English_General_siege_Besieged_Dread_2.mp3","English_General_siege_Besieged_Dread_3.mp3"]),
("engg_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["English_Army_siege_Ongoing_1.mp3","English_Army_siege_Ongoing_2.mp3","English_Army_siege_Ongoing_3.mp3","English_General_siege_Ongoing_1.mp3","English_General_siege_Ongoing_2.mp3","English_General_siege_Ongoing_3.mp3","English_General_siege_Ongoing_Chivalry_1.mp3","English_General_siege_Ongoing_Chivalry_2.mp3","English_General_siege_Ongoing_Chivalry_3.mp3","English_General_siege_Ongoing_Dread_1.mp3","English_General_siege_Ongoing_Dread_2.mp3","English_General_siege_Ongoing_Dread_3.mp3"]),
#English

#Easteuro
("eastern_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["East_European_Admiral_Attacked_Enemy_1.mp3", "East_European_Admiral_Attacked_Enemy_2.mp3", "East_European_Admiral_Attacked_Enemy_3.mp3"]),
("eastern_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["East_European_Admiral_Attacking_1.mp3", "East_European_Admiral_Attacking_2.mp3", "East_European_Admiral_Attacking_3.mp3"]),
("eastern_army_attacking", sf_2d|sf_priority_10|sf_vol_7, ["East_European_Army_Attacking_1.mp3", "East_European_Army_Attacking_2.mp3", "East_European_Army_Attacking_3.mp3", "East_European_Army_Fight_On_Battle_Map_1.mp3", "East_European_Army_Fight_On_Battle_Map_2.mp3", "East_European_Army_Fight_On_Battle_Map_3.mp3", "East_European_Army_Fight_On_Battle_Map_4.mp3", "East_European_Army_Fight_On_Battle_Map_5.mp3", "East_European_Army_Fight_On_Battle_Map_6.mp3",  "East_European_General_Attacking_1.mp3", "East_European_General_Attacking_3.mp3", "East_European_General_Attacking_Chivalry_1.mp3", "East_European_General_Attacking_Chivalry_2.mp3", "East_European_General_Attacking_Chivalry_3.mp3", "East_European_General_Attacking_Dread_1.mp3", "East_European_General_Attacking_Dread_2.mp3", "East_European_General_Attacking_Dread_3.mp3",  "East_European_General_Fight_On_Battle_Map_1.mp3", "East_European_General_Fight_On_Battle_Map_2.mp3",  "East_European_General_Fight_On_Battle_Map_3.mp3", "East_European_General_Fight_On_Battle_Map_Chivalry_1.mp3", "East_European_General_Fight_On_Battle_Map_Chivalry_2.mp3", "East_European_General_Fight_On_Battle_Map_Chivalry_3.mp3", "East_European_General_Fight_On_Battle_Map_Dread_1.mp3", "East_European_General_Fight_On_Battle_Map_Dread_2.mp3", "East_European_General_Fight_On_Battle_Map_Dread_3.mp3"]),
("eastern_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["East_European_Army_Battle_lost_retreat_1.mp3",  "East_European_Army_Battle_lost_retreat_3.mp3",  "East_European_General_Battle_lost_retreat_1.mp3",  "East_European_General_Battle_lost_retreat_3.mp3", "East_European_General_Battle_lost_retreat_Chivalry_1.mp3", "East_European_General_Battle_lost_retreat_Chivalry_2.mp3", "East_European_General_Battle_lost_retreat_Chivalry_3.mp3", "East_European_General_Battle_lost_retreat_Dread_1.mp3", "East_European_General_Battle_lost_retreat_Dread_2.mp3", "East_European_General_Battle_lost_retreat_Dread_3.mp3"]),
("eastern_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["East_European_Army_Battle_won_1.mp3", "East_European_Army_Battle_won_2.mp3", "East_European_Army_Battle_won_3.mp3", "East_European_General_Battle_won_1.mp3", "East_European_General_Battle_won_2.mp3", "East_European_General_Battle_won_3.mp3", "East_European_General_Battle_won_Chivalry_1.mp3", "East_European_General_Battle_won_Chivalry_2.mp3", "East_European_General_Battle_won_Chivalry_3.mp3", "East_European_General_Battle_won_Dread_1.mp3",  "East_European_General_Battle_won_Dread_3.mp3"]),
("eastern_army_join", sf_2d|sf_priority_10|sf_vol_7, ["East_European_Army_Joins_Army_1.mp3", "East_European_Army_Joins_Army_2.mp3", "East_European_Army_Joins_Army_3.mp3", "East_European_General_Joins_Army_1.mp3", "East_European_General_Joins_Army_2.mp3", "East_European_General_Joins_Army_3.mp3", "East_European_General_Joins_Army_Dread_1.mp3", "East_European_General_Joins_Army_Dread_2.mp3"]),
("eastern_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["East_European_Army_Leaves_Army_1.mp3",  "East_European_Army_Leaves_Army_3.mp3", "East_European_General_Leaves_Army_1.mp3", "East_European_General_Leaves_Army_2.mp3", "East_European_General_Leaves_Army_3.mp3", "East_European_General_Leaves_Army_Dread_1.mp3", "East_European_General_Leaves_Army_Dread_3.mp3"]),
("eastern_capture", sf_2d|sf_priority_10|sf_vol_7, ["East_European_Army_Settlement_Capture_Celebration_1.mp3", "East_European_Army_Settlement_Capture_Celebration_2.mp3", "East_European_Army_Settlement_Capture_Celebration_3.mp3", "East_European_General_Settlement_Capture_Celebration_1.mp3", "East_European_General_Settlement_Capture_Celebration_2.mp3", "East_European_General_Settlement_Capture_Celebration_Chivalry_1.mp3", "East_European_General_Settlement_Capture_Celebration_Chivalry_2.mp3", "East_European_General_Settlement_Capture_Celebration_Chivalry_3.mp3", "East_European_General_Settlement_Capture_Celebration_Dread_1.mp3", "East_European_General_Settlement_Capture_Celebration_Dread_2.mp3",]),
("eastern_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["East_European_Army_siege_Begun_1.mp3", "East_European_General_siege_Begun_1.mp3", "East_European_General_siege_Begun_2.mp3", "East_European_General_siege_Begun_Dread_1.mp3", "East_European_General_siege_Begun_Dread_2.mp3" ]),
("eastern_besieged", sf_2d|sf_priority_10|sf_vol_7, [ "East_European_Army_siege_Besieged_2.mp3", "East_European_Army_siege_Besieged_3.mp3", "East_European_General_siege_Besieged_2.mp3", "East_European_General_siege_Besieged_3.mp3", "East_European_General_siege_Besieged_Chivalry_2.mp3", "East_European_General_siege_Besieged_Chivalry_3.mp3", "East_European_General_siege_Besieged_Dread_1.mp3", "East_European_General_siege_Besieged_Dread_2.mp3", "East_European_General_siege_Besieged_Dread_3.mp3"]),
("eastern_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, [ "East_European_Army_siege_Ongoing_2.mp3", "East_European_Army_siege_Ongoing_3.mp3",  "East_European_General_siege_Ongoing_1.mp3", "East_European_General_siege_Ongoing_3.mp3", "East_European_General_siege_Ongoing_1.mp3", "East_European_General_siege_Ongoing_3.mp3",  "East_European_General_siege_Ongoing_Chivalry_3.mp3", "East_European_General_siege_Ongoing_Dread_2.mp3"]),
#Easteuro

#French
("frenchg_admiral_attacked", sf_2d|sf_priority_10|sf_vol_7, ["French_Admiral_Attacked_Enemy_2.mp3","French_Admiral_Attacked_Enemy_3.mp3"]),
("frenchg_admiral_attacking", sf_2d|sf_priority_10|sf_vol_7, ["French_Admiral_Attacking_1.mp3","French_Admiral_Attacking_2.mp3"]),
("frenchg_army_attack", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Attacking_2.mp3","French_Army_Fight_On_Battle_Map_3.mp3","French_Army_Fight_On_Battle_Map_5.mp3","French_General_Attacking_2.mp3","French_General_Attacking_3.mp3","French_General_Attacking_Chivalry_1.mp3","French_General_Attacking_Chivalry_2.mp3","French_General_Attacking_Dread_1.mp3","French_General_Attacking_Dread_3.mp3","French_General_Fight_On_Battle_Map_3.mp3","French_General_Fight_On_Battle_Map_Chivalry_1.mp3","French_General_Fight_On_Battle_Map_Dread_1.mp3","French_General_Fight_On_Battle_Map_Dread_2.mp3","French_General_Fight_On_Battle_Map_Dread_3.mp3"]),
("frenchg_army_retreat", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Battle_lost_retreat_1.mp3","French_Army_Battle_lost_retreat_2.mp3","French_General_Battle_lost_retreat_1.mp3","French_General_Battle_lost_retreat_2.mp3","French_General_Battle_lost_retreat_Chivalry_1.mp3","French_General_Battle_lost_retreat_Chivalry_2.mp3","French_General_Battle_lost_retreat_Chivalry_3.mp3","French_General_Battle_lost_retreat_Dread_1.mp3","French_General_Battle_lost_retreat_Dread_2.mp3","French_General_Battle_lost_retreat_Dread_3.mp3"]),
("frenchg_army_bwon", sf_2d|sf_priority_10|sf_vol_7, ["French_General_Battle_won_3.mp3","French_General_Battle_won_Chivalry_1.mp3","French_General_Battle_won_Chivalry_3.mp3","French_General_Battle_won_Dread_1.mp3","French_General_Battle_won_Dread_2.mp3","French_General_Battle_won_Dread_3.mp3"]),
("frenchg_army_join", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Joins_Army_1.mp3","French_Army_Joins_Army_2.mp3","French_Army_Joins_Army_3.mp3","French_General_Joins_Army_1.mp3","French_General_Joins_Army_3.mp3","French_General_Joins_Army_Chivalry_3.mp3","French_General_Joins_Army_Dread_1.mp3","French_General_Joins_Army_Dread_2.mp3","French_General_Joins_Army_Dread_3.mp3"]),
("frenchg_army_leave", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Leaves_Army_1.mp3","French_Army_Leaves_Army_2.mp3","French_General_Leaves_Army_1.mp3","French_General_Leaves_Army_2.mp3","French_General_Leaves_Army_3.mp3","French_General_Leaves_Army_Chivalry_1.mp3","French_General_Leaves_Army_Chivalry_2.mp3","French_General_Leaves_Army_Dread_1.mp3","French_General_Leaves_Army_Dread_2.mp3", "French_General_Leaves_Army_Dread_3.mp3"]),
("frenchg_capture", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_Settlement_Capture_Celebration_3.mp3","French_General_Settlement_Capture_Celebration_3.mp3","French_General_Settlement_Capture_Celebration_Dread_1.mp3","French_General_Settlement_Capture_Celebration_Dread_3.mp3"]),
("frenchg_begin_siege", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_siege_Begun_2.mp3","French_General_siege_Begun_1.mp3","French_General_siege_Begun_2.mp3","French_General_siege_Begun_Dread_2.mp3"]),
("frenchg_besieged", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_siege_Besieged_1.mp3","French_Army_siege_Besieged_2.mp3","French_General_siege_Besieged_1.mp3","French_General_siege_Besieged_2.mp3","French_General_siege_Besieged_Chivalry_1.mp3","French_General_siege_Besieged_Dread_1.mp3","French_General_siege_Besieged_Dread_2.mp3","French_General_siege_Besieged_Dread_3.mp3"]),
("frenchg_siege_ongoing", sf_2d|sf_priority_10|sf_vol_7, ["French_Army_siege_Ongoing_1.mp3","French_Army_siege_Ongoing_3.mp3","French_General_siege_Ongoing_1.mp3","French_General_siege_Ongoing_2.mp3","French_General_siege_Ongoing_Chivalry_3.mp3","French_General_siege_Ongoing_Dread_2.mp3","French_General_siege_Ongoing_Dread_3.mp3"]),
#French

#Reinforcements
("fac_reinforce_eastern_enemy", sf_2d|sf_priority_10|sf_vol_8, ["East_European_Enemy_Reinforcements_Arrive_1.mp3","East_European_Enemy_Reinforcements_Arrive_2.mp3"]),
("fac_reinforce_mongol_enemy", sf_2d|sf_priority_10|sf_vol_8, ["Mongolian_Enemy_Reinforcements_Arrive_1.mp3","Mongolian_Enemy_Reinforcements_Arrive_2.mp3"]),
("fac_reinforce_scotland_enemy", sf_2d|sf_priority_10|sf_vol_8, ["Scottish_Enemy_Reinforcements_Arrive_1.mp3","Scottish_Enemy_Reinforcements_Arrive_2.mp3"]),
("fac_reinforce_medi_enemy", sf_2d|sf_priority_10|sf_vol_8, ["Mediterranean_Enemy_Reinforcements_Arrive_1.mp3","Mediterranean_Enemy_Reinforcements_Arrive_2.mp3"]),
("fac_reinforce_islam_enemy", sf_2d|sf_priority_10|sf_vol_8, ["Arabic_Enemy_Reinforcements_Arrive_1.mp3","Arabic_Enemy_Reinforcements_Arrive_2.mp3"]),
("fac_reinforce_german_enemy", sf_2d|sf_priority_10|sf_vol_8, ["German_Enemy_Reinforcements_Arrive_1.mp3","German_Enemy_Reinforcements_Arrive_2.mp3"]),
("fac_reinforce_eng_enemy", sf_2d|sf_priority_10|sf_vol_8, ["English_Enemy_Reinforcements_Arrive_1.mp3","English_Enemy_Reinforcements_Arrive_2.mp3"]),
("fac_reinforce_french_enemy", sf_2d|sf_priority_10|sf_vol_8, ["French_Enemy_Reinforcements_Arrive_1.mp3","French_Enemy_Reinforcements_Arrive_2.mp3"]),

("fac_reinforce_ally", sf_2d|sf_priority_10|sf_vol_8, ["reinforcements_arrived.mp3"]),
#

##Ladders
#("eastern_ladder", sf_2d|sf_priority_10|sf_vol_8, ["East_European_Light_Generic_Ladder_2.mp3","East_European_Light_Generic_Ladder_1.mp3", "East_European_Heavy_Generic_Ladder_2.mp3","East_European_Heavy_Generic_Ladder_1.mp3", "East_European_General_Generic_Ladder_2.mp3","East_European_General_Generic_Ladder_1.mp3"]),
#("mongol_ladder", sf_2d|sf_priority_10|sf_vol_8, ["Mongolian_Light_Generic_Ladder_2.mp3","Mongolian_Light_Generic_Ladder_1.mp3", "Mongolian_Heavy_Generic_Ladder_2.mp3","Mongolian_Heavy_Generic_Ladder_1.mp3", "Mongolian_General_Generic_Ladder_2.mp3","Mongolian_General_Generic_Ladder_1.mp3"]),
#("scotland_ladder", sf_2d|sf_priority_10|sf_vol_8, ["Scottish_Light_Generic_Ladder_2.mp3","Scottish_Light_Generic_Ladder_1.mp3", "Scottish_Heavy_Generic_Ladder_2.mp3","Scottish_Heavy_Generic_Ladder_1.mp3", "Scottish_General_Generic_Ladder_2.mp3","Scottish_General_Generic_Ladder_1.mp3"]),
#("medi_ladder", sf_2d|sf_priority_10|sf_vol_8, ["Mediterranean_Light_Generic_Ladder_2.mp3","Mediterranean_Light_Generic_Ladder_1.mp3", "Mediterranean_Heavy_Generic_Ladder_2.mp3","Mediterranean_Heavy_Generic_Ladder_1.mp3", "Mediterranean_General_Generic_Ladder_2.mp3","Mediterranean_General_Generic_Ladder_1.mp3"]),
#("islam_ladder", sf_2d|sf_priority_10|sf_vol_8, ["Arabic_Light_Generic_Ladder_2.mp3","Arabic_Light_Generic_Ladder_1.mp3", "Arabic_Heavy_Generic_Ladder_2.mp3","Arabic_Heavy_Generic_Ladder_1.mp3", "Arabic_General_Generic_Ladder_2.mp3","Arabic_General_Generic_Ladder_1.mp3"]),
#("german_ladder", sf_2d|sf_priority_10|sf_vol_8, ["German_Light_Generic_Ladder_2.mp3","German_Light_Generic_Ladder_1.mp3", "German_Heavy_Generic_Ladder_2.mp3","German_Heavy_Generic_Ladder_1.mp3", "German_General_Generic_Ladder_2.mp3","German_General_Generic_Ladder_1.mp3"]),
#("eng_ladder", sf_2d|sf_priority_10|sf_vol_8, ["English_Light_Generic_Ladder_2.mp3","English_Light_Generic_Ladder_1.mp3", "English_Heavy_Generic_Ladder_2.mp3","English_Heavy_Generic_Ladder_1.mp3", "English_General_Generic_Ladder_2.mp3","English_General_Generic_Ladder_1.mp3"]),
#("french_ladder", sf_2d|sf_priority_10|sf_vol_8, ["French_Light_Generic_Ladder_2.mp3","French_Light_Generic_Ladder_1.mp3", "French_Heavy_Generic_Ladder_2.mp3","French_Heavy_Generic_Ladder_1.mp3", "French_General_Generic_Ladder_2.mp3","French_General_Generic_Ladder_1.mp3"]),
##Towers
#("eastern_tower", sf_2d|sf_priority_10|sf_vol_8, ["East_European_General_Generic_Tower_1.mp3","East_European_General_Generic_Tower_2.mp3", "East_European_Heavy_Generic_Tower_1.mp3","East_European_Heavy_Generic_Tower_2.mp3", "East_European_Light_Generic_Tower_1.mp3","East_European_Light_Generic_Tower_2.mp3"]),
#("mongol_tower", sf_2d|sf_priority_10|sf_vol_8, ["1.mp3","2.mp3", "3.mp3","4.mp3", "5.mp3","6.mp3"]),
#("scotland_tower", sf_2d|sf_priority_10|sf_vol_8, ["1.mp3","2.mp3", "3.mp3","4.mp3", "5.mp3","6.mp3"]),
#("medi_tower", sf_2d|sf_priority_10|sf_vol_8, ["Mediterranean_General_Generic_Tower_1.mp3","Mediterranean_General_Generic_Tower_2.mp3", "Mediterranean_Heavy_Generic_Tower_1.mp3","Mediterranean_Heavy_Generic_Tower_2.mp3", "Mediterranean_Light_Generic_Tower_1.mp3","Mediterranean_Light_Generic_Tower_2.mp3"]),
#("islam_tower", sf_2d|sf_priority_10|sf_vol_8, ["Arabic_General_Generic_Tower_1.mp3","Arabic_General_Generic_Tower_2.mp3", "Arabic_Heavy_Generic_Tower_1.mp3","Arabic_Heavy_Generic_Tower_2.mp3", "Arabic_Light_Generic_Tower_1.mp3","Arabic_Light_Generic_Tower_2.mp3"]),
#("german_tower", sf_2d|sf_priority_10|sf_vol_8, ["German_General_Generic_Tower_1.mp3","German_General_Generic_Tower_2.mp3", "German_Heavy_Generic_Tower_1.mp3","German_Heavy_Generic_Tower_2.mp3", "German_Light_Generic_Tower_1.mp3","German_Light_Generic_Tower_2.mp3"]),
#("eng_tower", sf_2d|sf_priority_10|sf_vol_8, ["English_General_Generic_Tower_1.mp3","English_General_Generic_Tower_2.mp3", "English_Heavy_Generic_Tower_1.mp3","English_Heavy_Generic_Tower_2.mp3", "English_Light_Generic_Tower_1.mp3","English_Light_Generic_Tower_2.mp3"]),
#("french_tower", sf_2d|sf_priority_10|sf_vol_8, ["French_General_Generic_Tower_1.mp3","French_General_Generic_Tower_2.mp3", "French_Heavy_Generic_Tower_1.mp3","French_Heavy_Generic_Tower_2.mp3", "French_Light_Generic_Tower_1.mp3","French_Light_Generic_Tower_2.mp3"]),
#

###In-battle
("eastern_all", sf_2d|sf_priority_10|sf_vol_8, ["East_European_General_Group_Select_1.wav","East_European_General_Group_Select_2.wav", "East_European_Heavy_Group_Select_1.wav", "East_European_Heavy_Group_Select_2.wav", "East_European_Light_Group_Select_1.wav", "East_European_Light_Group_Select_2.wav"]),
("eastern_inf", sf_2d|sf_priority_10|sf_vol_8, ["East_European_General_Group_Select_Infantry_1.wav","East_European_General_Group_Select_Infantry_2.wav", "East_European_Heavy_Group_Select_Infantry_1.wav","East_European_Heavy_Group_Select_Infantry_2.wav", "East_European_Light_Group_Select_Infantry_1.wav","East_European_Light_Group_Select_Infantry_2.wav"]),
("eastern_archers", sf_2d|sf_priority_10|sf_vol_8, ["East_European_General_Group_Select_Missiles_1.wav","East_European_General_Group_Select_Missiles_2.wav", "East_European_Heavy_Group_Select_Missiles_1.wav","East_European_Heavy_Group_Select_Missiles_2.wav", "East_European_Light_Group_Select_Missiles_1.wav","East_European_Light_Group_Select_Missiles_2.wav"]),
("eastern_cav", sf_2d|sf_priority_10|sf_vol_8, ["East_European_General_Group_Select_Cavalry_1.wav","East_European_General_Group_Select_Cavalry_2.wav", "East_European_Heavy_Group_Select_Cavalry_1.wav","East_European_Heavy_Group_Select_Cavalry_2.wav", "East_European_Light_Group_Select_Cavalry_1.wav","East_European_Light_Group_Select_Cavalry_2.wav"]),

("mongol_all", sf_2d|sf_priority_10|sf_vol_8, ["Mongolian_General_Group_Select_1.wav","Mongolian_General_Group_Select_2.wav", "Mongolian_Heavy_Group_Select_1.wav", "Mongolian_Heavy_Group_Select_2.wav", "Mongolian_Light_Group_Select_1.wav", "Mongolian_Light_Group_Select_2.wav"]),
("mongol_inf", sf_2d|sf_priority_10|sf_vol_8, ["Mongolian_General_Group_Select_Infantry_1.wav","Mongolian_General_Group_Select_Infantry_2.wav", "Mongolian_Heavy_Group_Select_Infantry_1.wav","Mongolian_Heavy_Group_Select_Infantry_2.wav", "Mongolian_Light_Group_Select_Infantry_1.wav","Mongolian_Light_Group_Select_Infantry_2.wav"]),
("mongol_archers", sf_2d|sf_priority_10|sf_vol_8, ["Mongolian_General_Group_Select_Missiles_1.wav","Mongolian_General_Group_Select_Missiles_2.wav", "Mongolian_Heavy_Group_Select_Missiles_1.wav","Mongolian_Heavy_Group_Select_Missiles_2.wav", "Mongolian_Light_Group_Select_Missiles_1.wav","Mongolian_Light_Group_Select_Missiles_2.wav"]),
("mongol_cav", sf_2d|sf_priority_10|sf_vol_8, ["Mongolian_General_Group_Select_Cavalry_1.wav","Mongolian_General_Group_Select_Cavalry_2.wav", "Mongolian_Heavy_Group_Select_Cavalry_1.wav","Mongolian_Heavy_Group_Select_Cavalry_2.wav", "Mongolian_Light_Group_Select_Cavalry_1.wav","Mongolian_Light_Group_Select_Cavalry_2.wav"]),


("scot_all", sf_2d|sf_priority_10|sf_vol_8, ["Scottish_General_Group_Select_1.wav","Scottish_General_Group_Select_2.wav", "Scottish_Heavy_Group_Select_1.wav", "Scottish_Heavy_Group_Select_2.wav", "Scottish_Light_Group_Select_1.wav", "Scottish_Light_Group_Select_2.wav"]),
("scot_inf", sf_2d|sf_priority_10|sf_vol_8, ["Scottish_General_Group_Select_Infantry_1.wav","Scottish_General_Group_Select_Infantry_2.wav", "Scottish_Heavy_Group_Select_Infantry_1.wav","Scottish_Heavy_Group_Select_Infantry_2.wav", "Scottish_Light_Group_Select_Infantry_1.wav","Scottish_Light_Group_Select_Infantry_2.wav"]),
("scot_archers", sf_2d|sf_priority_10|sf_vol_8, ["Scottish_General_Group_Select_Missiles_1.wav","Scottish_General_Group_Select_Missiles_2.wav", "Scottish_Heavy_Group_Select_Missiles_1.wav","Scottish_Heavy_Group_Select_Missiles_2.wav", "Scottish_Light_Group_Select_Missiles_1.wav","Scottish_Light_Group_Select_Missiles_2.wav"]),
("scot_cav", sf_2d|sf_priority_10|sf_vol_8, ["Scottish_General_Group_Select_Cavalry_1.wav","Scottish_General_Group_Select_Cavalry_2.wav", "Scottish_Heavy_Group_Select_Cavalry_1.wav","Scottish_Heavy_Group_Select_Cavalry_2.wav", "Scottish_Light_Group_Select_Cavalry_1.wav","Scottish_Light_Group_Select_Cavalry_2.wav"]),

("medi_all", sf_2d|sf_priority_10|sf_vol_8, ["Mediterranean_General_Group_Select_1.wav","Mediterranean_General_Group_Select_2.wav", "Mediterranean_Heavy_Group_Select_1.wav", "Mediterranean_Heavy_Group_Select_2.wav", "Mediterranean_Light_Group_Select_1.wav", "Mediterranean_Light_Group_Select_2.wav"]),
("medi_inf", sf_2d|sf_priority_10|sf_vol_8, ["Mediterranean_General_Group_Select_Infantry_1.wav","Mediterranean_General_Group_Select_Infantry_2.wav", "Mediterranean_Heavy_Group_Select_Infantry_1.wav","Mediterranean_Heavy_Group_Select_Infantry_2.wav", "Mediterranean_Light_Group_Select_Infantry_1.wav","Mediterranean_Light_Group_Select_Infantry_2.wav"]),
("medi_archers", sf_2d|sf_priority_10|sf_vol_8, ["Mediterranean_General_Group_Select_Missiles_1.wav","Mediterranean_General_Group_Select_Missiles_2.wav", "Mediterranean_Heavy_Group_Select_Missiles_1.wav","Mediterranean_Heavy_Group_Select_Missiles_2.wav", "Mediterranean_Light_Group_Select_Missiles_1.wav","Mediterranean_Light_Group_Select_Missiles_2.wav"]),
("medi_cav", sf_2d|sf_priority_10|sf_vol_8, ["Mediterranean_General_Group_Select_Cavalry_1.wav","Mediterranean_General_Group_Select_Cavalry_2.wav", "Mediterranean_Heavy_Group_Select_Cavalry_1.wav","Mediterranean_Heavy_Group_Select_Cavalry_2.wav", "Mediterranean_Light_Group_Select_Cavalry_1.wav","Mediterranean_Light_Group_Select_Cavalry_2.wav"]),


("islam_all", sf_2d|sf_priority_10|sf_vol_8, ["Arabic_General_Group_Select_1.wav","Arabic_Heavy_Group_Select_1.wav", "Arabic_General_Group_Select_2.wav", "Arabic_Heavy_Group_Select_2.wav", "Arabic_Light_Group_Select_2.wav", "Arabic_Light_Group_Select_1.wav"]),
("islam_inf", sf_2d|sf_priority_10|sf_vol_8, ["Arabic_General_Group_Select_Infantry_1.wav","Arabic_General_Group_Select_Infantry_2.wav", "Arabic_Heavy_Group_Select_Infantry_1.wav","Arabic_Heavy_Group_Select_Infantry_2.wav", "Arabic_Light_Group_Select_Infantry_1.wav","Arabic_Light_Group_Select_Infantry_2.wav"]),
("islam_archers", sf_2d|sf_priority_10|sf_vol_8, ["Arabic_General_Group_Select_Missiles_1.wav","Arabic_General_Group_Select_Missiles_2.wav", "Arabic_Heavy_Group_Select_Missiles_1.wav","Arabic_Heavy_Group_Select_Missiles_2.wav", "Arabic_Light_Group_Select_Missiles_1.wav","Arabic_Light_Group_Select_Missiles_2.wav"]),
("islam_cav", sf_2d|sf_priority_10|sf_vol_8, ["Arabic_General_Group_Select_Cavalry_1.wav","Arabic_General_Group_Select_Cavalry_2.wav", "Arabic_Heavy_Group_Select_Cavalry_1.wav","Arabic_Heavy_Group_Select_Cavalry_2.wav", "Arabic_Light_Group_Select_Cavalry_1.wav","Arabic_Light_Group_Select_Cavalry_2.wav"]),


("ger_all", sf_2d|sf_priority_10|sf_vol_8, ["German_General_Group_Select_1.wav","German_General_Group_Select_2.wav", "German_Heavy_Group_Select_1.wav", "German_Heavy_Group_Select_2.wav", "German_Light_Group_Select_1.wav", "German_Light_Group_Select_2.wav"]),
("ger_inf", sf_2d|sf_priority_10|sf_vol_8, ["German_General_Group_Select_Infantry_1.wav","German_General_Group_Select_Infantry_2.wav", "German_Heavy_Group_Select_Infantry_1.wav","German_Heavy_Group_Select_Infantry_2.wav", "German_Light_Group_Select_Infantry_1.wav","German_Light_Group_Select_Infantry_2.wav"]),
("ger_archers", sf_2d|sf_priority_10|sf_vol_8, ["German_General_Group_Select_Missiles_1.wav","German_General_Group_Select_Missiles_2.wav", "German_Heavy_Group_Select_Missiles_1.wav","German_Heavy_Group_Select_Missiles_2.wav", "German_Light_Group_Select_Missiles_1.wav","German_Light_Group_Select_Missiles_2.wav"]),
("ger_cav", sf_2d|sf_priority_10|sf_vol_8, ["German_General_Group_Select_Cavalry_1.wav","German_General_Group_Select_Cavalry_2.wav", "German_Heavy_Group_Select_Cavalry_1.wav","German_Heavy_Group_Select_Cavalry_2.wav", "German_Light_Group_Select_Cavalry_1.wav","German_Light_Group_Select_Cavalry_2.wav"]),


("eng_all", sf_2d|sf_priority_10|sf_vol_8, ["English_General_Group_Select_1.wav","English_General_Group_Select_2.wav", "English_Heavy_Group_Select_1.wav", "English_Heavy_Group_Select_2.wav", "English_Light_Group_Select_1.wav", "English_Light_Group_Select_2.wav"]),
("eng_inf", sf_2d|sf_priority_10|sf_vol_8, ["English_General_Group_Select_Infantry_1.wav","English_General_Group_Select_Infantry_2.wav", "English_Heavy_Group_Select_Infantry_1.wav","English_Heavy_Group_Select_Infantry_2.wav", "English_Light_Group_Select_Infantry_2.wav","English_Light_Group_Select_Infantry_1.wav"]),
("eng_archers", sf_2d|sf_priority_10|sf_vol_8, ["English_General_Group_Select_Missiles_1.wav","English_General_Group_Select_Missiles_2.wav", "English_Heavy_Group_Select_Missiles_1.wav","English_Heavy_Group_Select_Missiles_2.wav", "English_Light_Group_Select_Missiles_1.wav","English_Light_Group_Select_Missiles_2.wav"]),
("eng_cav", sf_2d|sf_priority_10|sf_vol_8, ["English_General_Group_Select_Cavalry_1.wav","English_General_Group_Select_Cavalry_2.wav", "English_Heavy_Group_Select_Cavalry_1.wav","English_Heavy_Group_Select_Cavalry_2.wav", "English_Light_Group_Select_Cavalry_1.wav","English_Light_Group_Select_Cavalry_2.wav"]),

("fre_all", sf_2d|sf_priority_10|sf_vol_8, ["French_General_Group_Select_1.wav","French_Heavy_Group_Select_1.wav", "French_General_Group_Select_2.wav", "French_Heavy_Group_Select_2.wav", "French_Light_Group_Select_1.wav", "French_Light_Group_Select_2.wav"]),
("fre_inf", sf_2d|sf_priority_10|sf_vol_8, ["French_General_Group_Select_Infantry_1.wav","French_General_Group_Select_Infantry_2.wav", "French_Heavy_Group_Select_Infantry_1.wav","French_Heavy_Group_Select_Infantry_2.wav", "French_Light_Group_Select_Infantry_1.wav","French_Light_Group_Select_Infantry_2.wav"]),
("fre_archers", sf_2d|sf_priority_10|sf_vol_8, ["French_General_Group_Select_Missiles_1.wav","French_General_Group_Select_Missiles_2.wav", "French_Heavy_Group_Select_Missiles_1.wav","French_Heavy_Group_Select_Missiles_2.wav", "French_Light_Group_Select_Missiles_1.wav","French_Light_Group_Select_Missiles_2.wav"]),
("fre_cav", sf_2d|sf_priority_10|sf_vol_8, ["French_General_Group_Select_Cavalry_1.wav","French_General_Group_Select_Cavalry_2.wav", "French_Heavy_Group_Select_Cavalry_1.wav","French_Heavy_Group_Select_Cavalry_2.wav", "French_Light_Group_Select_Cavalry_1.wav","French_Light_Group_Select_Cavalry_2.wav"]),



#Allies defeated
("eastern_ally", sf_2d|sf_priority_10|sf_vol_8, ["East_European_Allied_General_Executed_2.mp3","East_European_Allied_General_Executed_1.mp3", "East_European_Allied_Army_Leader_Killed_2.mp3","East_European_Allied_Army_Leader_Killed_1.mp3"]),
("mongol_ally", sf_2d|sf_priority_10|sf_vol_8, ["Mongolian_Allied_General_Executed_2.mp3","Mongolian_Allied_General_Executed_1.mp3", "Mongolian_Allied_Army_Leader_Killed_2.mp3","Mongolian_Allied_Army_Leader_Killed_1.mp3"]),
("scotland_ally", sf_2d|sf_priority_10|sf_vol_8, ["Scottish_Allied_General_Executed_2.mp3","Scottish_Allied_General_Executed_1.mp3","Scottish_Allied_Army_Leader_Killed_2.mp3", "Scottish_Allied_Army_Leader_Killed_1.mp3"]),
("medi_ally", sf_2d|sf_priority_10|sf_vol_8, ["Mediterranean_Allied_General_Executed_2.mp3","Mediterranean_Allied_General_Executed_1.mp3", "Mediterranean_Allied_Army_Leader_Killed_2.mp3","Mediterranean_Allied_Army_Leader_Killed_1.mp3"]),
("islam_ally", sf_2d|sf_priority_10|sf_vol_8, ["Arabic_Allied_General_Executed_2.mp3","Arabic_Allied_General_Executed_1.mp3", "Arabic_Allied_Army_Leader_Killed_2.mp3","Arabic_Allied_Army_Leader_Killed_1.mp3"]),
("german_ally", sf_2d|sf_priority_10|sf_vol_8, ["German_Allied_General_Executed_2.mp3","German_Allied_General_Executed_1.mp3", "German_Allied_Army_Leader_Killed_2.mp3","German_Allied_Army_Leader_Killed_1.mp3"]),
("eng_ally", sf_2d|sf_priority_10|sf_vol_8, ["English_Allied_General_Executed_2.mp3","English_Allied_General_Executed_1.mp3", "English_Allied_Army_Leader_Killed_2.mp3","English_Allied_Army_Leader_Killed_1.mp3"]),
("french_ally", sf_2d|sf_priority_10|sf_vol_8, ["French_Allied_General_Executed_2.mp3","French_Allied_General_Executed_1.mp3", "French_Allied_Army_Leader_Killed_2.mp3","French_Allied_Army_Leader_Killed_1.mp3"]),

#player faction defeated
("eastern_player", sf_2d|sf_priority_10|sf_vol_8, ["East_European_Player_General_Killed_2.mp3","East_European_Player_General_Killed_1.mp3", "East_European_Player_General_Executed_2.mp3","East_European_Player_General_Executed_1.mp3"]),
("mongol_player", sf_2d|sf_priority_10|sf_vol_8, ["Mongolian_Player_General_Killed_2.mp3","Mongolian_Player_General_Killed_1.mp3", "Mongolian_Player_General_Executed_2.mp3","Mongolian_Player_General_Executed_1.mp3"]),
("scotland_player", sf_2d|sf_priority_10|sf_vol_8, ["Scottish_Player_General_Killed_2.mp3","Scottish_Player_General_Killed_1.mp3","Scottish_Player_General_Executed_2.mp3", "Scottish_Player_General_Executed_1.mp3"]),
("medi_player", sf_2d|sf_priority_10|sf_vol_8, ["Mediterranean_Player_General_Killed_2.mp3","Mediterranean_Player_General_Killed_1.mp3", "Mediterranean_Player_General_Executed_2.mp3","Mediterranean_Player_General_Executed_1.mp3"]),
("islam_player", sf_2d|sf_priority_10|sf_vol_8, ["Arabic_Player_General_Killed_2.mp3","Arabic_Player_General_Killed_1.mp3", "Arabic_Player_General_Executed_2.mp3","Arabic_Player_General_Executed_1.mp3"]),
("german_player", sf_2d|sf_priority_10|sf_vol_8, ["German_Player_General_Killed_2.mp3","German_Player_General_Killed_1.mp3", "German_Player_General_Executed_2.mp3","German_Player_General_Executed_1.mp3"]),
("eng_player", sf_2d|sf_priority_10|sf_vol_8, ["English_Player_General_Killed_2.mp3","English_Player_General_Killed_1.mp3", "English_Player_General_Executed_2.mp3","English_Player_General_Executed_1.mp3"]),
("french_player", sf_2d|sf_priority_10|sf_vol_8, ["French_Player_General_Killed_2.mp3","French_Player_General_Killed_1.mp3", "French_Player_General_Executed_2.mp3","French_Player_General_Executed_1.mp3"]),

##Enemy slain by us aor allies
("eastern_enemy_beaten", sf_2d|sf_priority_10|sf_vol_8, ["East_European_Pagan_Enemy_General_Killed_2.mp3","East_European_Pagan_Enemy_General_Killed_1.mp3", "East_European_Enemy_General_Killed_2.mp3","East_European_Enemy_General_Killed_1.mp3"]),
("mongol_enemy_beaten", sf_2d|sf_priority_10|sf_vol_8, ["Mongolian_Enemy_General_Killed_2.mp3","Mongolian_Enemy_General_Killed_1.mp3", "Mongolian_Christian_Enemy_General_Killed_2.mp3","Mongolian_Christian_Enemy_General_Killed_1.mp3"]),
("scotland_enemy_beaten", sf_2d|sf_priority_10|sf_vol_8, ["Scottish_Pagan_Enemy_General_Killed_2.mp3","Scottish_Pagan_Enemy_General_Killed_1.mp3","Scottish_Enemy_General_Killed_2.mp3", "Scottish_Enemy_General_Killed_1.mp3"]),
("medi_enemy_beaten", sf_2d|sf_priority_10|sf_vol_8, ["Mediterranean_Pagan_Enemy_General_Killed_2.mp3","Mediterranean_Pagan_Enemy_General_Killed_1.mp3", "Mediterranean_Enemy_General_Killed_2.mp3","Mediterranean_Enemy_General_Killed_1.mp3"]),
("islam_enemy_beaten", sf_2d|sf_priority_10|sf_vol_8, ["Arabic_Pagan_Enemy_General_Killed_2.mp3","Arabic_Pagan_Enemy_General_Killed_1.mp3", "Arabic_Enemy_General_Killed_2.mp3","Arabic_Enemy_General_Killed_1.mp3", "Arabic_Christian_Enemy_General_Killed_2.mp3","Arabic_Christian_Enemy_General_Killed_1.mp3"]),
("german_enemy_beaten", sf_2d|sf_priority_10|sf_vol_8, ["German_Pagan_Enemy_General_Killed_2.mp3","German_Pagan_Enemy_General_Killed_1.mp3", "German_Enemy_General_Killed_2.mp3","German_Enemy_General_Killed_1.mp3"]),
("eng_enemy_beaten", sf_2d|sf_priority_10|sf_vol_8, ["English_Pagan_Enemy_General_Killed_2.mp3","English_Pagan_Enemy_General_Killed_1.mp3", "English_Enemy_General_Killed_2.mp3","English_Enemy_General_Killed_1.mp3"]),
("french_enemy_beaten", sf_2d|sf_priority_10|sf_vol_8, ["French_Pagan_Enemy_General_Killed_2.mp3","French_Pagan_Enemy_General_Killed_1.mp3", "French_Enemy_General_Killed_2.mp3","French_Enemy_General_Killed_1.mp3"]),

#Muslims beaten
("eastern_enemy_beaten_muslim", sf_2d|sf_priority_10|sf_vol_8, ["East_European_Muslim_Enemy_General_Killed_1.mp3","East_European_Muslim_Enemy_General_Killed_2.mp3"]),
("mongol_enemy_beaten_muslim", sf_2d|sf_priority_10|sf_vol_8, ["Mongolian_Muslim_Enemy_General_Killed_1.mp3","Mongolian_Muslim_Enemy_General_Killed_2.mp3"]),
("scotland_enemy_beaten_muslim", sf_2d|sf_priority_10|sf_vol_8, ["Scottish_Muslim_Enemy_General_Killed_1.mp3","Scottish_Muslim_Enemy_General_Killed_2.mp3"]),
("medi_enemy_beaten_muslim", sf_2d|sf_priority_10|sf_vol_8, ["Mediterranean_Muslim_Enemy_General_Killed_1.mp3","Mediterranean_Muslim_Enemy_General_Killed_2.mp3"]),
("islam_enemy_beaten_muslim", sf_2d|sf_priority_10|sf_vol_8, ["Arabic_Player_General_Killed_2.mp3","Arabic_Player_General_Killed_1.mp3"]),
("german_enemy_beaten_muslim", sf_2d|sf_priority_10|sf_vol_8, ["German_Muslim_Enemy_General_Killed_1.mp3","German_Muslim_Enemy_General_Killed_2.mp3"]),
("eng_enemy_beaten_muslim", sf_2d|sf_priority_10|sf_vol_8, ["English_Muslim_Enemy_General_Killed_1.mp3","English_Muslim_Enemy_General_Killed_2.mp3"]),
("french_enemy_beaten_muslim", sf_2d|sf_priority_10|sf_vol_8, ["French_Muslim_Enemy_General_Killed_1.mp3","French_Muslim_Enemy_General_Killed_2.mp3"]),



##Our king slain
("eastern_our_leader", sf_2d|sf_priority_10|sf_vol_8, ["East_European_Player_Leader_Killed_2.mp3","East_European_Player_Leader_Killed_1.mp3"]),
("mongol_our_leader", sf_2d|sf_priority_10|sf_vol_8, ["Mongolian_Player_Leader_Killed_2.mp3","Mongolian_Player_Leader_Killed_1.mp3"]),
("scotland_our_leader", sf_2d|sf_priority_10|sf_vol_8, ["Scottish_Player_Leader_Killed_2.mp3","Scottish_Player_Leader_Killed_1.mp3"]),
("medi_our_leader", sf_2d|sf_priority_10|sf_vol_8, ["Mediterranean_Player_Leader_Killed_2.mp3","Mediterranean_Player_Leader_Killed_1.mp3"]),
("islam_our_leader", sf_2d|sf_priority_10|sf_vol_8, ["Arabic_Player_Leader_Killed_1.mp3"]),
("german_our_leader", sf_2d|sf_priority_10|sf_vol_8, ["German_Player_Leader_Killed_2.mp3","German_Player_Leader_Killed_1.mp3"]),
("eng_our_leader", sf_2d|sf_priority_10|sf_vol_8, ["English_Player_Leader_Killed_2.mp3","English_Player_Leader_Killed_1.mp3"]),
("french_our_leader", sf_2d|sf_priority_10|sf_vol_8, ["French_Player_Leader_Killed_2.mp3","French_Player_Leader_Killed_1.mp3"]),

#Enemy king slain by us or allies
("eastern_enemy_leader_killed", sf_2d|sf_priority_10|sf_vol_8, ["East_European_Enemy_King_Killed_2.mp3","East_European_Enemy_King_Killed_1.mp3"]),
("mongol_enemy_leader_killed", sf_2d|sf_priority_10|sf_vol_8, ["Mongolian_Enemy_King_Killed_2.mp3","Mongolian_Enemy_King_Killed_1.mp3"]),
("scotland_enemy_leader_killed", sf_2d|sf_priority_10|sf_vol_8, ["Scottish_Enemy_King_Killed_2.mp3","Scottish_Enemy_King_Killed_1.mp3"]),
("medi_enemy_leader_killed", sf_2d|sf_priority_10|sf_vol_8, ["Mediterranean_Enemy_King_Killed_2.mp3","Mediterranean_Enemy_King_Killed_1.mp3"]),
("islam_enemy_leader_killed", sf_2d|sf_priority_10|sf_vol_8, ["Arabic_Enemy_King_Killed_2.mp3", "Arabic_Enemy_King_Killed_1.mp3"]),
("german_enemy_leader_killed", sf_2d|sf_priority_10|sf_vol_8, ["German_Enemy_King_Killed_2.mp3","German_Enemy_King_Killed_1.mp3"]),
("eng_enemy_leader_killed", sf_2d|sf_priority_10|sf_vol_8, ["English_Enemy_King_Killed_2.mp3","English_Enemy_King_Killed_1.mp3"]),
("french_enemy_leader_killed", sf_2d|sf_priority_10|sf_vol_8, ["French_Enemy_King_Killed_2.mp3","French_Enemy_King_Killed_1.mp3"]),



###("eastern_tower", sf_2d|sf_priority_10|sf_vol_8, ["1.mp3","2.mp3", "3.mp3","4.mp3", "5.mp3","6.mp3"]),
###("mongol_tower", sf_2d|sf_priority_10|sf_vol_8, ["1.mp3","2.mp3", "3.mp3","4.mp3", "5.mp3","6.mp3"]),
###("scotland_tower", sf_2d|sf_priority_10|sf_vol_8, ["1.mp3","2.mp3", "3.mp3","4.mp3", "5.mp3","6.mp3"]),
###("medi_tower", sf_2d|sf_priority_10|sf_vol_8, ["1.mp3","2.mp3", "3.mp3","4.mp3", "5.mp3","6.mp3"]),
###("islam_tower", sf_2d|sf_priority_10|sf_vol_8, ["1.mp3","2.mp3", "3.mp3","4.mp3", "5.mp3","6.mp3"]),
###("german_tower", sf_2d|sf_priority_10|sf_vol_8, ["1.mp3","2.mp3", "3.mp3","4.mp3", "5.mp3","6.mp3"]),
###("eng_tower", sf_2d|sf_priority_10|sf_vol_8, ["1.mp3","2.mp3", "3.mp3","4.mp3", "5.mp3","6.mp3"]),
###("french_tower", sf_2d|sf_priority_10|sf_vol_8, ["1.mp3","2.mp3", "3.mp3","4.mp3", "5.mp3","6.mp3"]),
#####Cultural Speeches end

	
	("command_horn", sf_priority_9|sf_vol_10, ["command_horn.ogg"]),

	("command_horn_2d", sf_2d|sf_priority_9|sf_vol_10, ["command_horn.ogg"]),

	("sex_asian_female", sf_priority_9|sf_vol_6, ["sex_asian_female.ogg"]),

	("sex_female", sf_priority_9|sf_vol_10, ["sex_female.ogg"]),

	("cryyy_female", sf_priority_9|sf_vol_9, ["cry_fem.ogg"]),

	("bottle_crash_g", sf_priority_9|sf_vol_15, ["bottle_crash_g.ogg"]),

	("GroundHit1", sf_priority_9|sf_vol_15, ["GroundHit1.ogg"]),

	("burn222", sf_priority_9|sf_vol_15, ["Fire_Torch_Loop3.ogg"]),

	("Typhoon", sf_2d|sf_priority_9|sf_vol_10, ["Typhoon.ogg"]),

	("Forest_fires", sf_2d|sf_priority_9|sf_vol_10, ["Forest_fires.ogg"]),

	("Tsunami", sf_2d|sf_priority_9|sf_vol_10, ["Tsunami.ogg"]),

	("Drought", sf_2d|sf_priority_9|sf_vol_10, ["Drought.ogg"]),

	("The_Black_Death", sf_2d|sf_priority_9|sf_vol_10, ["The_Black_Death.ogg"]),

	("Earthquake", sf_2d|sf_priority_9|sf_vol_10, ["Earthquake.ogg"]),

	("Flood", sf_2d|sf_priority_9|sf_vol_10, ["Flood.ogg"]),

	("eruptions", sf_2d|sf_priority_9|sf_vol_10, ["eruptions.ogg"]),

	("fallrocks", sf_2d|sf_priority_9|sf_vol_10, ["fallrocks.ogg"]),

	("tactfail", sf_2d|sf_priority_9|sf_vol_15, ["quest_cancelled2.ogg"]),

	("wood_cuttt", sf_2d|sf_priority_9|sf_vol_12, ["wood_cuttt.ogg"]),

	("womanscream02", sf_2d|sf_priority_9|sf_vol_7, ["womanscream02.ogg"]),

	("blowjobbb", sf_2d|sf_priority_9|sf_vol_10, ["blowjobbbb.ogg"]),

	("swalloww", sf_2d|sf_priority_9|sf_vol_7, ["swalloww.ogg"]),

	("mansatis", sf_2d|sf_priority_9|sf_vol_13, ["mansatis.ogg"]),

	("fireworkss", sf_2d|sf_priority_9|sf_vol_14, ["fireworkss.ogg"]),

	("sabotagee", sf_2d|sf_priority_9|sf_vol_14, ["sabotagee.ogg"]),

	("gbt_whip", sf_2d|sf_priority_9|sf_vol_9, ["gbt_whip.ogg"]),

	("gbt_lick", sf_2d|sf_priority_9|sf_vol_15, ["gbt_lick.ogg"]),

	("gbt_touch", sf_2d|sf_priority_9|sf_vol_15, ["gbt_touch.ogg"]),

	("gbt_orga_up", sf_2d|sf_priority_9|sf_vol_14, ["gbt_orga_up.ogg"]),

	("gbt_orga_fail", sf_2d|sf_priority_9|sf_vol_14, ["gbt_orga_fail.ogg"]),

	("gbt_orgasm", sf_2d|sf_priority_9|sf_vol_14, ["gbt_orgasm.ogg"]),

	("cry_fem_2", sf_2d|sf_priority_9|sf_vol_14, ["cry_fem_2.ogg"]),

	("gbt_whip_hit", sf_2d|sf_priority_9|sf_vol_12, ["gbt_whip_hit.ogg"]),

	("release_crossbow_medium", sf_priority_1, ["molda_null_sound.ogg"]),

	("release_crossbow_far", sf_priority_1, ["molda_null_sound.ogg"]),

	("bullet_hit_body", sf_priority_1, ["molda_null_sound.ogg"]),

	("player_hit_by_bullet", sf_priority_1, ["molda_null_sound.ogg"]),

	("catapult_in_battle", sf_priority_10, ["catapultt.ogg"]),

	("siege_weapon_hit", sf_priority_10, ["siege_weapon_hit_1.ogg", "siege_weapon_hit_2.ogg"]),

	("explosion_volca", sf_priority_9, ["explosion_volca.ogg"]),

	("ballista_shoot", sf_priority_10, ["ballista_shoot.ogg"]),

	("experience_gained", sf_2d|sf_priority_9|sf_vol_9, ["quest_succeeded.ogg"]),

	("found_something", sf_2d|sf_priority_9|sf_vol_9, ["quest_completed2.ogg"]),

	("win_1", sf_2d|sf_priority_9|sf_vol_9, ["defeated_by_neutral_3.ogg"]),

	("lose_1", sf_2d|sf_priority_9|sf_vol_9, ["defeated_by_neutral_2.ogg"]),

	("fallrocks_in_battle", sf_priority_9|sf_vol_3, ["fallrocks.ogg"]),

	("siege_weapon_hit_2d", sf_2d|sf_priority_10|sf_vol_9, ["siege_weapon_hit_1.ogg", "siege_weapon_hit_2.ogg"]),

	("skill_cancel", sf_2d|sf_priority_10|sf_vol_9, ["quest_cancelled.ogg"]),

	("skill_choose", sf_2d|sf_priority_10|sf_vol_9, ["quest_completed.ogg"]),

	("holywar", sf_2d|sf_priority_10|sf_vol_9, ["quest_failed.ogg"]),

	("good_news_2", sf_2d|sf_priority_10|sf_vol_9, ["quest_completed2.ogg"]),

	("bad_drum", sf_2d|sf_priority_10|sf_vol_9, ["quest_cancelled2.ogg"]),

	("cannon_hitt", sf_priority_9|sf_vol_15, ["cannon_hitt.ogg", "sabotagee.ogg"]),

	("cannon_shot", sf_priority_9|sf_vol_10, ["CannonShot1.ogg", "CannonShot2.ogg", "CannonShot3.ogg", "CannonShot4.ogg"]),

	("sea_melee", sf_priority_9|sf_vol_10, ["sea_melee_1.ogg", "sea_melee_2.ogg", "fireworkss.ogg"]),

	("sea_melee_hit", sf_priority_9|sf_vol_10, ["sea_melee_hit_1.ogg", "sea_movee.ogg", "seaswoop.ogg", "sabotagee.ogg"]),

	("sea_bow_shoot", sf_priority_9|sf_vol_15, ["ballista_shoot.ogg"]),

	("ship_down_1", sf_priority_9|sf_vol_15, ["ship_down_1.ogg"]),

	("ship_down_2", sf_priority_9|sf_vol_15, ["ship_down_2.ogg"]),

	("rats_squeak", sf_2d|sf_priority_9|sf_vol_8, ["rats_squeak.ogg"]),

	("need_meeting", sf_2d|sf_vol_5, ["molda_null_sound.ogg"]),

	("market_day", sf_2d|sf_vol_4, ["molda_null_sound.ogg"]),

	("cat_meow", sf_2d|sf_vol_15, ["cat_meow.ogg"]),

	("gbt_whip_for_agent", sf_priority_9|sf_vol_8, ["gbt_whip.ogg"]),

	("pst_click", sf_2d|sf_vol_5, ["click_01.ogg"]),

	("man_sad_cry", sf_2d|sf_vol_15, ["man_die_06.ogg"]),

]