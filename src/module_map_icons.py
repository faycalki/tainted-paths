from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from ID_sounds import *

####################################################################################################################
#  Each map icon record contains the following fields:
#  1) Map icon id: used for referencing map icons in other files.
#     The prefix icon_ is automatically added before each map icon id.
#  2) Map icon flags. See header_map icons.py for a list of available flags
#  3) Mesh name.
#  4) Scale. 
#  5) Sound.
#  6) Offset x position for the flag icon.
#  7) Offset y position for the flag icon.
#  8) Offset z position for the flag icon.
####################################################################################################################

banner_scale = 0.3
avatar_scale = 0.15

map_icons = [
	("player", 0, "dd_euro", 0.18, snd_footstep_grass, 0.2, 0.4, 1.1),

	("player_horseman", 0, "dd_knight_euro", 0.18, snd_gallop, 0.2, 0.4, 1.1),

	("gray_knight", 0, "dd_knight_cru", 0.18, snd_gallop, 0.2, 0.4, 1.1),

	("vaegir_knight", 0, "dd_mongol", 0.18, snd_gallop, 0.2, 0.4, 1.1),

	("flagbearer_a", 0, "dd_nomad", 0.18, snd_gallop, 0.2, 0.4, 1.1),

	("flagbearer_b", 0, "dd_arab", 0.18, snd_gallop, 0.2, 0.4, 1.1),

	("peasant", 0, "icon_mule", 0.18, snd_footstep_grass, 0.2, 0.4, 1.1),

	("khergit", 0, "dd_swordman", 0.18, snd_gallop, 0.2, 0.4, 1.1),

	("khergit_horseman_b", 0, "dd_ancient", 0.18, snd_gallop, 0.2, 0.4, 1.1),

	("axeman", 0, "dd_bandit", 0.18, snd_footstep_grass, 0.2, 0.4, 1.1),

	("woman", 0, "dd_viking", 0.18, snd_footstep_grass, 0.2, 0.4, 1.1),

	("woman_b", 0, "dd_china", 0.18, snd_footstep_grass, 0.2, 0.4, 1.1),

	("camp", mcn_no_shadow, "camp_tent", 0.1, snd_click, 0.0, 0.0, 0.0),

	("ship", mcn_no_shadow, "boat_sail_on2", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("caravel", mcn_no_shadow, "caravel", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("carrack", mcn_no_shadow, "carrack", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("xebec", mcn_no_shadow, "xebec", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("galley", mcn_no_shadow, "galley", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("galleon", mcn_no_shadow, "galleon", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("turship", mcn_no_shadow, "turship", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("junkship", mcn_no_shadow, "junkship", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("panship", mcn_no_shadow, "panship", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("dragonship", mcn_no_shadow, "dragonship", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("galleas", mcn_no_shadow, "galleas", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("black_ship", mcn_no_shadow, "black_ship", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("line_ship", mcn_no_shadow, "galleon", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("ghost_ship", mcn_no_shadow, "black_ship", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("antecship", mcn_no_shadow, "antecship", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("nugakship", mcn_no_shadow, "nugakship", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("panokship", mcn_no_shadow, "panokship", 0.18, snd_footstep_water, 0.0, 0.0, 0.0),

	("point_mark", mcn_no_shadow, "battle_track_ruin", 1.5, snd_click, 0.0, 0.0, 0.0),

	("cave_exn", mcn_no_shadow, "map_bandit_lair", 1.5, snd_click, 0.0, 0.0, 0.0),

	("house_exn", mcn_no_shadow, "house_exn", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_euro_1", mcn_no_shadow, "wm_town_euro_1", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_rome_1", mcn_no_shadow, "wm_town_rome_1", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_arab_1", mcn_no_shadow, "wm_town_arab_1", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_asia_1", mcn_no_shadow, "wm_town_asia_1", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_barb_1", mcn_no_shadow, "wm_town_barb_1", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_jjap_1", mcn_no_shadow, "wm_town_jjap_1", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_euro_2", mcn_no_shadow, "wm_town_euro_2", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_rome_2", mcn_no_shadow, "wm_town_rome_2", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_arab_2", mcn_no_shadow, "wm_town_arab_2", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_asia_2", mcn_no_shadow, "wm_town_asia_2", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_barb_2", mcn_no_shadow, "wm_town_barb_2", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_jjap_2", mcn_no_shadow, "wm_town_jjap_2", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_euro_3", mcn_no_shadow, "wm_town_euro_3", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_rome_3", mcn_no_shadow, "wm_town_rome_3", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_arab_3", mcn_no_shadow, "wm_town_arab_3", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_asia_3", mcn_no_shadow, "wm_town_asia_3", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_barb_3", mcn_no_shadow, "wm_town_barb_3", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_jjap_3", mcn_no_shadow, "wm_town_asia_3", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_uurt", mcn_no_shadow, "wm_town_uurt", 1.5, snd_click, 0.0, 0.0, 0.0),

	("wm_town_teepee", mcn_no_shadow, "wm_town_teepee", 1.5, snd_click, 0.0, 0.0, 0.0),

	("bridge_stone", mcn_no_shadow, "map_river_bridge_a", 1.6, snd_click, 0.0, 0.0, 0.0),

	("bridge_wood", mcn_no_shadow, "map_river_bridge_b", 1.6, snd_click, 0.0, 0.0, 0.0),

	("harbor", mcn_no_shadow, "dukou", 0.5, snd_click, 0.0, 0.0, 0.0),

	("wm_plantation", mcn_no_shadow, "wm_plantation", 1.0, snd_click, 0.0, 0.0, 0.0),

	("cantsee", mcn_no_shadow, "invalid_item", 0.25, snd_click, 0.0, 0.0, 0.0),

	("attack_target", mcn_no_shadow, "attack_target", 1.5, snd_click, 0.0, 0.0, 0.0),

	("defence_target", mcn_no_shadow, "defence_target", 1.5, snd_click, 0.0, 0.0, 0.0),

	("tournament_flag", mcn_no_shadow, "tournament_flag", 1.5, snd_click, 0.0, 0.0, 0.0),

	("disaster_volcano", mcn_no_shadow, "disaster_volcano", 1.5, snd_click, 0.0, 0.0, 0.0),

	("disaster_earthquake", mcn_no_shadow, "disaster_earthquake", 1.5, snd_click, 0.0, 0.0, 0.0),

	("disaster_storm", mcn_no_shadow, "disaster_storm", 1.5, snd_click, 0.0, 0.0, 0.0),

	("disaster_typhoon", mcn_no_shadow, "disaster_typhoon", 1.5, snd_click, 0.0, 0.0, 0.0),

	("disaster_fire", mcn_no_shadow, "disaster_fire", 1.5, snd_click, 0.0, 0.0, 0.0),

	("disaster_sand", mcn_no_shadow, "disaster_sand", 1.5, snd_click, 0.0, 0.0, 0.0),

	("disaster_tides", mcn_no_shadow, "disaster_tides", 1.5, snd_click, 0.0, 0.0, 0.0),

	("disaster_ice", mcn_no_shadow, "disaster_ice", 1.5, snd_click, 0.0, 0.0, 0.0),

	("disaster_flood", mcn_no_shadow, "disaster_flood", 1.5, snd_click, 0.0, 0.0, 0.0),

	("disaster_blackdeath", mcn_no_shadow, "disaster_blackdeath", 1.5, snd_click, 0.0, 0.0, 0.0),

	("disaster_malaria", mcn_no_shadow, "disaster_malaria", 1.5, snd_click, 0.0, 0.0, 0.0),

	("disaster_riot", mcn_no_shadow, "disaster_riot", 1.5, snd_click, 0.0, 0.0, 0.0),

	("text_sea_01", mcn_no_shadow, "text_sea_01", 7.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_02", mcn_no_shadow, "text_sea_02", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_03", mcn_no_shadow, "text_sea_03", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_04", mcn_no_shadow, "text_sea_04", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_05", mcn_no_shadow, "text_sea_05", 3.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_06", mcn_no_shadow, "text_sea_06", 6.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_07", mcn_no_shadow, "text_sea_07", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_08", mcn_no_shadow, "text_sea_08", 3.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_09", mcn_no_shadow, "text_sea_09", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_10", mcn_no_shadow, "text_sea_10", 7.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_11", mcn_no_shadow, "text_sea_11", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_12", mcn_no_shadow, "text_sea_12", 6.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_13", mcn_no_shadow, "text_sea_13", 7.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_14", mcn_no_shadow, "text_sea_14", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_15", mcn_no_shadow, "text_sea_15", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_16", mcn_no_shadow, "text_sea_16", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_17", mcn_no_shadow, "text_sea_17", 7.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_18", mcn_no_shadow, "text_sea_18", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_19", mcn_no_shadow, "text_sea_19", 3.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_20", mcn_no_shadow, "text_sea_20", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_21", mcn_no_shadow, "text_sea_21", 7.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_22", mcn_no_shadow, "text_sea_22", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_23", mcn_no_shadow, "text_sea_23", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_24", mcn_no_shadow, "text_sea_24", 3.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_25", mcn_no_shadow, "text_sea_25", 3.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_26", mcn_no_shadow, "text_sea_26", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_27", mcn_no_shadow, "text_sea_27", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_28", mcn_no_shadow, "text_sea_28", 7.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_29", mcn_no_shadow, "text_sea_29", 3.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_30", mcn_no_shadow, "text_sea_30", 7.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_31", mcn_no_shadow, "text_sea_31", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_32", mcn_no_shadow, "text_sea_32", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_33", mcn_no_shadow, "text_sea_33", 7.0, snd_click, 0.0, 0.0, 0.0),

	("text_sea_34", mcn_no_shadow, "text_sea_34", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_01", mcn_no_shadow, "text_geo_01", 6.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_02", mcn_no_shadow, "text_geo_02", 5.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_03", mcn_no_shadow, "text_geo_03", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_04", mcn_no_shadow, "text_geo_04", 12.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_05", mcn_no_shadow, "text_geo_05", 3.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_06", mcn_no_shadow, "text_geo_06", 7.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_07", mcn_no_shadow, "text_geo_07", 9.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_08", mcn_no_shadow, "text_geo_08", 5.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_09", mcn_no_shadow, "text_geo_09", 9.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_10", mcn_no_shadow, "text_geo_10", 6.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_11", mcn_no_shadow, "text_geo_11", 9.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_12", mcn_no_shadow, "text_geo_12", 5.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_13", mcn_no_shadow, "text_geo_13", 5.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_14", mcn_no_shadow, "text_geo_14", 7.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_15", mcn_no_shadow, "text_geo_15", 4.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_16", mcn_no_shadow, "text_geo_16", 5.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_17", mcn_no_shadow, "text_geo_17", 9.0, snd_click, 0.0, 0.0, 0.0),

	("text_geo_18", mcn_no_shadow, "text_geo_18", 5.0, snd_click, 0.0, 0.0, 0.0),

	("battle_site", mcn_no_shadow, "dedal_battlefield_d", 1.5, snd_click, 0.0, 0.0, 0.0),

	("windmill", mcn_no_shadow, "dedal_map_windmill", 1.5, snd_click, 0.0, 0.0, 0.0),

	("watchtower", mcn_no_shadow, "dedal_map_watchtower", 1.5, snd_click, 0.0, 0.0, 0.0),

	("banner_01", 0, "map_flag_01", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_02", 0, "map_flag_02", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_03", 0, "map_flag_03", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_04", 0, "map_flag_04", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_05", 0, "map_flag_05", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_06", 0, "map_flag_06", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_07", 0, "map_flag_07", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_08", 0, "map_flag_08", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_09", 0, "map_flag_09", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_10", 0, "map_flag_10", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_11", 0, "map_flag_11", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_12", 0, "map_flag_12", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_13", 0, "map_flag_13", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_14", 0, "map_flag_14", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_15", 0, "map_flag_f21", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_16", 0, "map_flag_16", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_17", 0, "map_flag_17", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_18", 0, "map_flag_18", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_19", 0, "map_flag_19", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_20", 0, "map_flag_20", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_21", 0, "map_flag_21", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_22", 0, "map_flag_22", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_23", 0, "map_flag_23", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_24", 0, "map_flag_24", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_25", 0, "map_flag_25", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_26", 0, "map_flag_26", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_27", 0, "map_flag_27", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_28", 0, "map_flag_28", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_29", 0, "map_flag_29", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_30", 0, "map_flag_30", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_31", 0, "map_flag_31", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_32", 0, "map_flag_32", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_33", 0, "map_flag_33", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_34", 0, "map_flag_34", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_35", 0, "map_flag_35", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_36", 0, "map_flag_36", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_37", 0, "map_flag_37", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_38", 0, "map_flag_38", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_39", 0, "map_flag_39", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_40", 0, "map_flag_40", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_41", 0, "map_flag_41", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_42", 0, "map_flag_42", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_43", 0, "map_flag_43", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_44", 0, "map_flag_44", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_45", 0, "map_flag_45", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_46", 0, "map_flag_46", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_47", 0, "map_flag_47", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_48", 0, "map_flag_48", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_49", 0, "map_flag_49", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_50", 0, "map_flag_50", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_51", 0, "map_flag_51", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_52", 0, "map_flag_52", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_53", 0, "map_flag_53", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_54", 0, "map_flag_54", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_55", 0, "map_flag_55", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_56", 0, "map_flag_56", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_57", 0, "map_flag_57", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_58", 0, "map_flag_58", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_59", 0, "map_flag_59", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_60", 0, "map_flag_60", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_61", 0, "map_flag_61", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_62", 0, "map_flag_62", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_63", 0, "map_flag_63", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_64", 0, "map_flag_d01", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_65", 0, "map_flag_d02", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_66", 0, "map_flag_d03", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_67", 0, "map_flag_d04", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_68", 0, "map_flag_d05", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_69", 0, "map_flag_d06", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_70", 0, "map_flag_d07", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_71", 0, "map_flag_d08", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_72", 0, "map_flag_d09", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_73", 0, "map_flag_d10", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_74", 0, "map_flag_d11", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_75", 0, "map_flag_d12", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_76", 0, "map_flag_d13", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_77", 0, "map_flag_d14", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_78", 0, "map_flag_d15", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_79", 0, "map_flag_d16", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_80", 0, "map_flag_d17", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_81", 0, "map_flag_d18", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_82", 0, "map_flag_d19", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_83", 0, "map_flag_d20", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_84", 0, "map_flag_d21", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_85", 0, "map_flag_e01", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_86", 0, "map_flag_e02", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_87", 0, "map_flag_e03", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_88", 0, "map_flag_e04", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_89", 0, "map_flag_e05", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_90", 0, "map_flag_e06", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_91", 0, "map_flag_e07", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_92", 0, "map_flag_e08", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_93", 0, "map_flag_e09", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_94", 0, "map_flag_e10", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_95", 0, "map_flag_e11", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_96", 0, "map_flag_e12", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_97", 0, "map_flag_e13", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_98", 0, "map_flag_e14", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_99", 0, "map_flag_e15", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_100", 0, "map_flag_e16", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_101", 0, "map_flag_e17", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_102", 0, "map_flag_e18", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_103", 0, "map_flag_e19", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_104", 0, "map_flag_e20", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_105", 0, "map_flag_e21", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_106", 0, "map_flag_f01", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_107", 0, "map_flag_f02", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_108", 0, "map_flag_f03", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_109", 0, "map_flag_f04", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_110", 0, "map_flag_f05", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_111", 0, "map_flag_f06", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_112", 0, "map_flag_f07", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_113", 0, "map_flag_f08", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_114", 0, "map_flag_f09", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_115", 0, "map_flag_f10", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_116", 0, "map_flag_f11", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_117", 0, "map_flag_f12", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_118", 0, "map_flag_f13", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_119", 0, "map_flag_f14", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_120", 0, "map_flag_f15", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_121", 0, "map_flag_f16", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_122", 0, "map_flag_f17", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_123", 0, "map_flag_f18", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_124", 0, "map_flag_f19", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_125", 0, "map_flag_f20", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_126", 0, "map_flag_h01", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_127", 0, "map_flag_h02", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_128", 0, "map_flag_h03", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_129", 0, "map_flag_h04", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_130", 0, "map_flag_h05", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_131", 0, "map_flag_h06", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_132", 0, "map_flag_h07", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_133", 0, "map_flag_h08", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_134", 0, "map_flag_h09", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_135", 0, "map_flag_h10", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_136", 0, "map_flag_h11", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_137", 0, "map_flag_h12", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_138", 0, "map_flag_h13", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_139", 0, "map_flag_h14", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_140", 0, "map_flag_h15", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_141", 0, "map_flag_h16", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_142", 0, "map_flag_h17", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_143", 0, "map_flag_h18", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_144", 0, "map_flag_h19", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_145", 0, "map_flag_h20", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_146", 0, "map_flag_h21", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_147", 0, "map_flag_i01", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_148", 0, "map_flag_i02", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_149", 0, "map_flag_i03", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_150", 0, "map_flag_i04", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_151", 0, "map_flag_i05", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_152", 0, "map_flag_i06", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_153", 0, "map_flag_i07", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_154", 0, "map_flag_i08", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_155", 0, "map_flag_i09", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_156", 0, "map_flag_i10", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_157", 0, "map_flag_i11", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_158", 0, "map_flag_i12", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_159", 0, "map_flag_i13", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_160", 0, "map_flag_i14", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_161", 0, "map_flag_i15", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_162", 0, "map_flag_i16", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_163", 0, "map_flag_i17", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_164", 0, "map_flag_i18", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_165", 0, "map_flag_i19", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_166", 0, "map_flag_i20", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_167", 0, "map_flag_i21", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_168", 0, "map_flag_k01", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_169", 0, "map_flag_k02", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_170", 0, "map_flag_k03", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_171", 0, "map_flag_k04", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_172", 0, "map_flag_k05", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_173", 0, "map_flag_k06", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_174", 0, "map_flag_k07", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_175", 0, "map_flag_k08", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_176", 0, "map_flag_k09", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_177", 0, "map_flag_k10", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_178", 0, "map_flag_k11", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_179", 0, "map_flag_k12", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_180", 0, "map_flag_k13", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_181", 0, "map_flag_k14", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_182", 0, "map_flag_k15", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_183", 0, "map_flag_k16", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_184", 0, "map_flag_k17", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_185", 0, "map_flag_k18", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_186", 0, "map_flag_k19", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_187", 0, "map_flag_k20", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_188", 0, "map_flag_f21", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_189", 0, "map_flag_f02", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_190", 0, "map_flag_f03", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_191", 0, "map_flag_f04", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_192", 0, "map_flag_f05", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_193", 0, "map_flag_f06", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_194", 0, "map_flag_f07", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_195", 0, "map_flag_f08", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_196", 0, "map_flag_f09", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_197", 0, "map_flag_f10", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_a", 0, "map_flag_kingdom_a", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_b", 0, "map_flag_kingdom_b", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_c", 0, "map_flag_kingdom_c", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_d", 0, "map_flag_kingdom_d", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_e", 0, "map_flag_kingdom_e", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_f", 0, "map_flag_kingdom_f", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_g", 0, "map_flag_kingdom_g", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_h", 0, "map_flag_kingdom_h", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_i", 0, "map_flag_kingdom_i", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_j", 0, "map_flag_kingdom_j", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_k", 0, "map_flag_kingdom_k", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_l", 0, "map_flag_kingdom_l", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_ll", 0, "map_flag_kingdom_ll", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_m", 0, "map_flag_kingdom_m", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_n", 0, "map_flag_kingdom_n", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_o", 0, "map_flag_kingdom_o", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_p", 0, "map_flag_kingdom_p", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_q", 0, "map_flag_kingdom_q", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_r", 0, "map_flag_kingdom_r", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_s", 0, "map_flag_kingdom_s", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_t", 0, "map_flag_kingdom_t", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_u", 0, "map_flag_kingdom_u", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_v", 0, "map_flag_kingdom_v", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_w", 0, "map_flag_kingdom_w", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_x", 0, "map_flag_kingdom_x", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_y", 0, "map_flag_kingdom_y", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_z", 0, "map_flag_kingdom_z", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_2a", 0, "map_flag_kingdom_2a", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_2b", 0, "map_flag_kingdom_2b", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_2c", 0, "map_flag_kingdom_2c", 0.18, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_2d", 0, "map_flag_kingdom_2d", 0.18, snd_click, 0.0, 0.0, 0.0),

	("banner_198", 0, "map_flag_15", 0.18, snd_click, 0.0, 0.0, 0.0),

	("bandit_lair", mcn_no_shadow, "map_bandit_lair", 1.0, snd_click, 0.0, 0.0, 0.0),

]