from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *

####################################################################################################################
#  Each scene record contains the following fields:
#  1) Scene id {string}: used for referencing scenes in other files. The prefix scn_ is automatically added before each scene-id.
#  2) Scene flags {int}. See header_scenes.py for a list of available flags
#  3) Mesh name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  4) Body name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  5) Min-pos {(float,float)}: minimum (x,y) coordinate. Player can't move beyond this limit.
#  6) Max-pos {(float,float)}: maximum (x,y) coordinate. Player can't move beyond this limit.
#  7) Water-level {float}. 
#  8) Terrain code {string}: You can obtain the terrain code by copying it from the terrain generator screen
#  9) List of other scenes accessible from this scene {list of strings}.
#     (deprecated. This will probably be removed in future versions of the module system)
#     (In the new system passages are used to travel between scenes and
#     the passage's variation-no is used to select the game menu item that the passage leads to.)
# 10) List of chest-troops used in this scene {list of strings}. You can access chests by placing them in edit mode.
#     The chest's variation-no is used with this list for selecting which troop's inventory it will access.
#  town_1   Sargoth     #plain
#  town_2   Tihr        #steppe
#  town_3   Veluca      #steppe
#  town_4   Suno        #plain
#  town_5   Jelkala     #plain
#  town_6   Praven      #plain
#  town_7   Uxkhal      #plain
#  town_8   Reyvadin    #plain
#  town_9   Khudan      #snow
#  town_10  Tulga       #steppe
#  town_11  Curaw       #snow
#  town_12  Wercheg     #plain
#  town_13  Rivacheg    #plain
#  town_14  Halmar      #steppe
#  town_15  Yalen
#  town_16  Dhirim
#  town_17  Ichamur
#  town_18  Narra
#  town_19  Shariz
#  town_20  Durquba
#  town_21  Ahmerrad
#  town_22  Bariyye
####################################################################################################################

scenes = [
	("random_scene", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x300028000003e8fa0000034e00004b34000059be", [], []),

	("conversation_scene", 0, "encounter_spot", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("water", 0, "none", "none", (-1000.00, -1000.00), (1000.00, 1000.00), -0.5, "0", [], []),

	("random_scene_steppe", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000032c6f93930004f12700006ece0000216500000d15", [], [], "outer_terrain_steppe"),

	("random_scene_plain", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000032c6f93930004f12700006ece0000216500000d15", [], [], "outer_terrain_plain"),

	("random_scene_snow", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000034c6f93930004f1270000030c0000216500000d15", [], [], "outer_terrain_snow"),

	("random_scene_desert", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000035c6466130004f127000065cf00002165000022e8", [], [], "outer_terrain_desert"),

	("random_scene_steppe_forest", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000003bc72ec470004f1270000634a00002165000022e8", [], [], "outer_terrain_plain"),

	("random_scene_plain_forest", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000003bc72ec470004f1270000634a00002165000022e8", [], [], "outer_terrain_plain"),

	("random_scene_snow_forest", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000003cc72ec470004f127000031d800002165000022e8", [], [], "outer_terrain_snow"),

	("random_scene_desert_forest", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000035c72ec470004f1270000268400002165000022e8", [], [], "outer_terrain_desert"),

	("camp_scene", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x0000000333c9d2c6800cd73100001bc6000069b500005d69", [], [], "outer_terrain_plain"),

	("camp_scene_horse_track", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x0000000334e9cb52000cd73100001bc6000069b500005d69", [], [], "outer_terrain_plain"),

	("random_scene_plain_forest2", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x00000002bc684be300065e1700003ed2000025e300002221", [], [], "outer_terrain_plain"),

	("four_ways_inn", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x0000000030015f2b000350d4000011a4000017ee000054af", [], [], "outer_terrain_town_thir_1"),

	("test_scene", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x0230817a00028ca300007f4a0000479400161992", [], [], "outer_terrain_plain"),

	("quick_battle_1", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x30401ee300059966000001bf0000299a0000638f", [], [], "outer_terrain_plain"),

	("salt_mine", sf_generate, "none", "none", (-200.00, -200.00), (200.00, 200.00), -100.0, "0x2a07b23200025896000023ee00007f9c000022a8", [], [], "outer_terrain_steppe"),

	("novice_ground", sf_indoors, "training_house_a", "bo_training_house_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("zendar_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0xa0001d9300031ccb0000156f000048ba0000361c", [], [], "outer_terrain_plain"),

	("dhorak_keep", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x33a7946000028ca300007f4a0000479400161992", ["exit"], []),

	("reserved4", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "28791", [], []),

	("reserved5", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "117828", [], []),

	("reserved6", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "6849", [], []),

	("reserved7", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "6849", [], []),

	("reserved8", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "13278", [], []),

	("reserved9", sf_indoors, "thirsty_lion", "bo_thirsty_lion", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("reserved10", 0, "none", "none", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("reserved11", 0, "none", "none", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("reserved12", sf_indoors, "thirsty_lion", "bo_thirsty_lion", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("training_ground", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x30000500400360d80000189f00002a8380006d91", [], ["tutorial_chest_1", "tutorial_chest_2"], "outer_terrain_plain"),

	("tutorial_1", sf_indoors, "tutorial_1_scene", "bo_tutorial_1_scene", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("tutorial_2", sf_indoors, "tutorial_2_scene", "bo_tutorial_2_scene", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("tutorial_3", sf_indoors, "tutorial_3_scene", "bo_tutorial_3_scene", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("tutorial_4", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x30000500400360d80000189f00002a8380006d91", [], [], "outer_terrain_plain"),

	("tutorial_5", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x3a06dca80005715c0000537400001377000011fe", [], [], "outer_terrain_plain"),

	("training_ground_horse_track_1", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x00000000337553240004d53700000c0500002a0f80006267", [], [], "outer_terrain_plain"),

	("training_ground_horse_track_2", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x00000000301553240004d5370000466000002a0f800073f1", [], [], "outer_terrain_plain"),

	("training_ground_horse_track_3", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x00000000400c12b2000515470000216b0000485e00006928", [], [], "outer_terrain_snow"),

	("training_ground_horse_track_4", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x00000000200b60320004a5290000180d0000452f00000e90", [], [], "outer_terrain_plain"),

	("training_ground_horse_track_5", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x000000003008208e0006419000000f730000440f00003c86", [], [], "outer_terrain_plain"),

	("training_ground_ranged_melee_1", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x00000001350455c20005194a000041cb00005ae800000ff5", [], [], "outer_terrain_plain"),

	("training_ground_ranged_melee_2", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x0000000532c8dccb0005194a000041cb00005ae800001bdd", [], [], "outer_terrain_plain"),

	("training_ground_ranged_melee_3", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x000000054327dcba0005194a00001b1d00005ae800004d63", [], [], "outer_terrain_snow"),

	("training_ground_ranged_melee_4", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x000000012247dcba0005194a000041ef00005ae8000050af", [], [], "outer_terrain_plain"),

	("training_ground_ranged_melee_5", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x00000001324a9cba0005194a000041ef00005ae800003c55", [], [], "outer_terrain_plain"),

	("zendar_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x300bc5430001e0780000448a0000049f00007932", ["the_happy_boar", "random_scene", "zendar_merchant"], [], "outer_terrain_plain"),

	("the_happy_boar", sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["zendar_center"], ["zendar_chest"]),

	("zendar_merchant", sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("field_1", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000033a059a5a0009525600002005000060e300001175", [], [], "outer_terrain_plain"),

	("field_2", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000033a079a3f000a3a8000006dfd000030a100006522", [], [], "outer_terrain_plain"),

	("field_3", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x30054da28004050000005a76800022aa00002e3b", [], [], "outer_terrain_plain"),

	("field_4", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x30054da28004050000005a76800022aa00002e3b", [], [], "outer_terrain_plain"),

	("field_5", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x30054da28004050000005a76800022aa00002e3b", [], [], "outer_terrain_plain"),

	("test2", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b0078cb20003fd0000005e480000288c0000286f", [], [], "outer_terrain_steppe"),

	("test3", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b00511d98004b12e0000039f00004e6300005c7d", [], [], "outer_terrain_plain"),

	("multi_scene_1", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000023007a3b20005795e0000706d0000381800000bbc", [], [], "sea_outer_terrain_1"),

	("random_multi_plain_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x000000033c6005004006c62500003efe00004b34000059be", [], [], "outer_terrain_plain"),

	("random_multi_plain_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x000000033c6005004006c62500003efe00004b34000059be", [], [], "outer_terrain_plain"),

	("random_multi_steppe_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -0.5, "0x000000033c6005004006c62500003efe00004b34000059be", [], [], "outer_terrain_plain"),

	("random_multi_steppe_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -0.5, "0x00000000408305e30006c625000033bd000065b400002904", [], [], "outer_terrain_snow"),

	("multiplayer_maps_end", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300389800003a4ea000058340000637a0000399b", [], [], "outer_terrain_plain"),

	("wedding", sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("quick_battle_scene_1", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x000000023002dee300045d1d000001bf0000299a0000638f", [], [], "outer_terrain_plain"),

	("quick_battle_scene_2", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x0000000250001d630005114300006228000053bf00004eb9", [], [], "outer_terrain_desert_b"),

	("quick_battle_scene_3", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x000000023002b76300046d2400000190000076300000692a", [], [], "outer_terrain_plain"),

	("quick_battle_scene_4", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x000000025a00f23700057d5f00006d6a000050ba000036df", [], [], "outer_terrain_desert_b"),

	("quick_battle_scene_5", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007985300055550000064d500005c060000759e", [], [], "outer_terrain_plain"),

	("quick_battle_maps_end", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300389800003a4ea000058340000637a0000399b", [], [], "outer_terrain_plain"),

	("tutorial_training_ground", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x000000003000050000046d1b0000189f00002a8380006d91", [], [], "outer_terrain_plain"),

	("meeting_scene_steppe", 0, "none", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("meeting_scene_plain", 0, "ch_meet_plain_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("meeting_scene_snow", 0, "ch_meet_snow_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("meeting_scene_desert", 0, "ch_meet_desert_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("meeting_scene_steppe_forest", 0, "ch_meet_steppe_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("meeting_scene_plain_forest", 0, "ch_meet_plain_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("meeting_scene_snow_forest", 0, "ch_meet_snow_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("meeting_scene_desert_forest", 0, "ch_meet_desert_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("molda_jungle_1", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x3a078bb2000589630000667200002fb90000179c", [], [], "outer_terrain_plain"),

	("duel_sea", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x0000000030000000c00d2348000000008000000000000000", [], [], "sea_outer_terrain_2"),

	("duel_plain", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x000000073000050040043d0a000000000000000000000000", [], [], "outer_terrain_plain"),

	("duel_snow", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x000000044464c8d1400d23480000530700007b430000254d", [], [], "outer_terrain_snow"),

	("duel_desert", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x000000045464c8d1400d23480000530700007b430000254d", [], [], "outer_terrain_desert"),

	("conv_camp", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000004350515194002308c000008c70000136600003b1c", [], [], "outer_terrain_plain"),

	("conv_camp_desert", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000004550515194002308c000008c70000136600003b1c", [], [], "outer_terrain_desert"),

	("conv_camp_snow", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000004450515190002308c00002c040000136600003b1c", [], [], "outer_terrain_snow"),

	("conv_camp_sea", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x0000000730000500000691a200005299000033cc00006e1f", [], [], "sea_outer_terrain_2"),

	("ex_bedroom", sf_indoors, "ex_bedroom", "bo_ex_bedroom", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("fuck_place", sf_indoors, "arabian_ground_a", "bo_arabian_ground_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("molda_siege_mission_plain", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000720e0120040054952000050db00006001000076c0", [], [], "outer_terrain_steppe"),

	("molda_siege_mission_plain_desert", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000720e0120040054952000050db00006001000076c0", [], [], "outer_terrain_desert"),

	("molda_siege_mission_plain_snow", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000720e0120040054952000050db00006001000076c0", [], [], "outer_terrain_snow"),

	("molda_siege_mission_urt", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000323201216c0054952000002df0000038700007600", [], [], "outer_terrain_steppe"),

	("molda_siege_mission_teepee", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000323201216c0054952000002df0000038700007600", [], [], "outer_terrain_steppe"),

	("molda_siege_mission_jap_1", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000720e01200c0054952000050db00006001000076c0", [], [], "outer_terrain_steppe"),

	("8_tavern_arab_1", sf_indoors, "8_tavern_arab_1", "bo_8_tavern_arab_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_tavern_asia", sf_indoors, "8_tavern_roma_1", "bo_8_tavern_roma_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_tavern_euro_1", sf_indoors, "8_tavern_euro_1", "bo_8_tavern_euro_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_tavern_roma_1", sf_indoors, "8_tavern_roma_1", "bo_8_tavern_roma_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_tavern_wood", sf_indoors, "8_tavern_wood", "bo_8_tavern_wood", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_tavern_urt_1", sf_indoors, "8_0_ground", "bo_8_0_ground", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_tavern_teepee_1", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000723201216c0054952000002df0000038700007600", ["exit"], [], "outer_terrain_steppe"),

	("8_vill_plain", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000723201216c0054952000002df0000038700007600", [], [], "outer_terrain_plain"),

	("8_vill_desert", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000723201216c0054952000002df0000038700007600", [], [], "outer_terrain_desert"),

	("8_vill_snow", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000723201216c0054952000002df0000038700007600", [], [], "outer_terrain_snow"),

	("8_vill_urt", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000323201216c0054952000002df0000038700007600", [], [], "outer_terrain_steppe"),

	("8_vill_teepee", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000323201216c0054952000002df0000038700007600", [], [], "outer_terrain_steppe"),

	("8_vill_jap", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000720e01200c0054952000050db00006001000076c0", [], [], "outer_terrain_steppe"),

	("molda_scn_end", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000723201216c0054952000002df0000038700007600", [], []),

	("8_hall_arab_1", sf_indoors, "8_hall_arab_1", "bo_8_hall_arab_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_hall_arab_2", sf_indoors, "8_hall_arab_2", "bo_8_hall_arab_2", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_hall_asia", sf_indoors, "8_hall_euro_2", "bo_8_hall_euro_2", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_hall_euro_1", sf_indoors, "8_hall_euro_1", "bo_8_hall_euro_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_hall_euro_2", sf_indoors, "8_hall_euro_2", "bo_8_hall_euro_2", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_hall_euro_3", sf_indoors, "8_hall_euro_3", "bo_8_hall_euro_3", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_hall_greek", sf_indoors, "8_hall_roma_1", "bo_8_hall_roma_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_hall_roma_1", sf_indoors, "8_hall_roma_1", "bo_8_hall_roma_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_hall_viking_1", sf_indoors, "8_hall_viking_1", "bo_8_hall_viking_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_hall_wood_1", sf_indoors, "8_hall_wood_1", "bo_8_hall_wood_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_hall_urt_1", sf_indoors, "8_0_ground", "bo_8_0_ground", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("8_hall_teepee_1", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000723201216c0054952000002df0000038700007600", ["exit"], [], "outer_terrain_steppe"),

	("8_prison_arab_1", sf_indoors, "8_prison_arab_1", "bo_8_prison_arab_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("8_prison_asia", sf_indoors, "8_prison_asia", "bo_8_prison_asia", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("8_prison_euro", sf_indoors, "8_prison_euro", "bo_8_prison_euro", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("8_prison_wood_1", sf_indoors, "8_prison_wood_1", "bo_8_prison_wood_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("8_prison_urt_1", sf_indoors, "8_0_ground", "bo_8_0_ground", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("8_prison_teepee_1", sf_indoors, "8_0_ground", "bo_8_0_ground", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("8_prison_arab_1_for_castle", sf_indoors, "8_prison_arab_1", "bo_8_prison_arab_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("8_prison_asia_for_castle", sf_indoors, "8_prison_asia", "bo_8_prison_asia", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("8_prison_euro_for_castle", sf_indoors, "8_prison_euro", "bo_8_prison_euro", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("8_prison_wood_1_for_castle", sf_indoors, "8_prison_wood_1", "bo_8_prison_wood_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("8_prison_urt_1_for_castle", sf_indoors, "8_0_ground", "bo_8_0_ground", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("8_prison_teepee_1_for_castle", sf_indoors, "8_0_ground", "bo_8_0_ground", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("8_arena_plain", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0xa0001d9300031ccb0000156f000048ba0000361c", [], [], "outer_terrain_steppe"),

	("8_arena_desert", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000050001d9300031ccb0000156f000048ba0000361c", [], [], "outer_terrain_desert"),

	("8_arena_snow", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000040001d9340031ccb0000156f000048ba0000361c", [], [], "outer_terrain_snow"),

	("8_arena_roma", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0xa0001d9300031ccb0000156f000048ba0000361c", [], [], "outer_terrain_steppe"),

	("8_arena_no_fence", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0xa0001d9300031ccb0000156f000048ba0000361c", [], [], "outer_terrain_steppe"),

	("9_battle_random_plain", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000334875393c004f127000078b7000039e100000d15", [], [], "outer_terrain_plain"),

	("9_battle_random_snow", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000344875393c004f127000078b7000039e100000d15", [], [], "outer_terrain_snow"),

	("9_battle_random_desert", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000354875393c004f127000078b7000039e100000d15", [], [], "outer_terrain_desert"),

	("9_battle_random_mount_plain", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000003bc74ea534004f127000015f40000216500000d15", [], [], "outer_terrain_plain"),

	("9_battle_random_mount_snow", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000003cc74ea534004f127000015f40000216500000d15", [], [], "outer_terrain_snow"),

	("9_battle_random_mount_desert", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000035c74ea534004f127000015f40000216500000d15", [], [], "outer_terrain_desert"),

	("molda_sea_battle_1", sf_generate, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x00000007300005000005e97600004912800053ec0000202b", [], [], "sea_outer_terrain_2"),

	("ex_meetroom", sf_indoors, "ex_bedroom", "bo_ex_bedroom", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("ruin_dun_askia", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000007500005000005354d000060ae00006cbf0000509e", [], [], "outer_terrain_desert"),

	("ruin_dun_impaler", sf_indoors, "8_hall_euro_3", "bo_8_hall_euro_3", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("ruin_dun_shaver", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000007300005004005354d000060ae00006cbf0000509e", [], [], "outer_terrain_plain"),

	("ruin_dun_shiva_blade", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000007300005004005354d000060ae00006cbf0000509e", [], [], "outer_terrain_plain"),

	("ruin_dun_sun_blade", sf_indoors, "8_prison_arab_1", "bo_8_prison_arab_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("kidnapper_fight", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000007300005004005354d000060ae00006cbf0000509e", [], [], "outer_terrain_plain"),

	("rebel_wooden_fort", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000007300005004005354d000060ae00006cbf0000509e", [], [], "outer_terrain_plain"),

	("ruin_dun_evil_spirits_armor", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000720e01200c0054952000050db00006001000076c0", [], [], "outer_terrain_steppe"),

	("ruin_dun_dracul_armor", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000007300005004005354d000060ae00006cbf0000509e", [], [], "outer_terrain_plain"),

	("bandit_leader_hideout", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000007300005004005354d000060ae00006cbf0000509e", [], [], "outer_terrain_plain"),

	("fortress_ruins", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000007300005004005354d000060ae00006cbf0000509e", [], [], "outer_terrain_plain"),

	("farm_defence", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000007300005004005354d000060ae00006cbf0000509e", [], [], "outer_terrain_plain"),

	("protect_family_house", sf_indoors, "8_hall_wood_1", "bo_8_hall_wood_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("insult_woman", sf_indoors, "8_tavern_roma_1", "bo_8_tavern_roma_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("camp_assassination", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000004350515194002308c000008c70000136600003b1c", [], [], "outer_terrain_plain"),

	("family_exterminate_house", sf_indoors, "8_hall_wood_1", "bo_8_hall_wood_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("assassinate_mission", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000007300005004005354d000060ae00006cbf0000509e", [], [], "outer_terrain_plain"),

	("protect_caravan", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000003a0792320005cd6c000000cb0000598f000062ff", [], [], "outer_terrain_steppe"),

	("formation_battle_p", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000013323c7944006298a00000b1200000fc800002954", [], [], "outer_terrain_steppe"),

	("formation_battle_d", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000015323c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_desert"),

	("formation_battle_s", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000014323c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_snow"),

	("formation_lion_p", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000013323c7944006298a00000b1200000fc800002954", [], [], "outer_terrain_steppe"),

	("formation_lion_d", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000015323c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_desert"),

	("formation_lion_s", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000014323c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_snow"),

	("formation_pincer_p", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000013323c7944006298a00000b1200000fc800002954", [], [], "outer_terrain_steppe"),

	("formation_pincer_d", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000015323c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_desert"),

	("formation_pincer_s", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000014323c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_snow"),

	("formation_mangudai_p", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000013323c7944006298a00000b1200000fc800002954", [], [], "outer_terrain_steppe"),

	("formation_mangudai_d", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000015323c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_desert"),

	("formation_mangudai_s", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000014323c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_snow"),

	("formation_encamp_p", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000013003c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_steppe"),

	("formation_encamp_d", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000015003c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_desert"),

	("formation_encamp_s", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000014003c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_snow"),

	("formation_8door_p", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000013003c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_steppe"),

	("formation_8door_d", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000015003c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_desert"),

	("formation_8door_s", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000014003c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_snow"),

	("formation_backatt_p", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000013323c7944006298a00000b1200000fc800002954", [], [], "outer_terrain_steppe"),

	("formation_backatt_d", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000015323c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_desert"),

	("formation_backatt_s", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000014323c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_snow"),

	("formation_sideatt_p", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000013323c7944006298a00000b1200000fc800002954", [], [], "outer_terrain_steppe"),

	("formation_sideatt_d", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000015323c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_desert"),

	("formation_sideatt_s", sf_generate|sf_randomize, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000014323c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_snow"),

	("formation_briver_p", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000013323c7944006298a00000b1200000fc800002954", [], [], "outer_terrain_steppe"),

	("formation_briver_d", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000015323c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_desert"),

	("formation_briver_s", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000014323c7940006298a00000b1200000fc800002954", [], [], "outer_terrain_snow"),

	("battle_tile_forest", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000230034b0b0004c5f4000078a600000d89000042c3", [], [], "outer_terrain_steppe"),

	("battle_tile_cliff", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000002342c36ba0004f1f200006acc00004cd1000054b4", [], [], "outer_terrain_steppe"),

	("battle_tile_cliff_d", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000002542c36ba0004f1f200006acc00004cd1000054b4", [], [], "outer_terrain_desert"),

	("battle_tile_cliff_s", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000002442c36ba0004f1f200006acc00004cd1000054b4", [], [], "outer_terrain_snow"),

	("battle_tile_submerge", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000335c8372a800509450000654500000f0100007521", [], [], "outer_terrain_steppe"),

	("battle_tile_submerge_s", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000345c8372a800509450000654500000f0100007521", [], [], "outer_terrain_snow"),

	("battle_tile_firework", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000233258c940004e9ed000065700000712000006e94", [], [], "outer_terrain_steppe"),

	("battle_tile_lure", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000000392c24b20004892800002fcc0000407000004e16", [], [], "outer_terrain_steppe"),

	("battle_tile_lure_d", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000000592c24b20004892800002fcc0000407000004e16", [], [], "outer_terrain_desert"),

	("battle_tile_lure_s", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000000492c24b20004892800002fcc0000407000004e16", [], [], "outer_terrain_snow"),

	("battle_tile_ambush", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000033c68a6480004c5b800004e7800004974000046d3", [], [], "outer_terrain_steppe"),

	("battle_tile_ambush_s", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000034c68a6480004c5b800004e7800004974000046d3", [], [], "outer_terrain_snow"),

	("battle_tile_bridge", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000032c795950004f19000007a720000120600000d59", [], [], "outer_terrain_steppe"),

	("battle_tile_bridge_d", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000052c795950004f19000007a720000120600000d59", [], [], "outer_terrain_desert"),

	("battle_tile_bridge_s", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000042c795950004f19000007a720000120600000d59", [], [], "outer_terrain_snow"),

	("battle_tile_farm", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000073000050000043d45000036990000293c00001ca8", [], [], "outer_terrain_steppe"),

	("battle_tile_valley", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000023c71722f00066597000017b60000454d00002ea9", [], [], "outer_terrain_steppe"),

	("battle_tile_valley_d", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000025c71722f00066597000017b60000454d00002ea9", [], [], "outer_terrain_desert"),

	("battle_tile_valley_s", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000024c71722f00066597000017b60000454d00002ea9", [], [], "outer_terrain_snow"),

	("battle_tile_snakepass_new", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000003a07b2320004390d000069a1000052cc000071d1", [], [], "outer_terrain_steppe"),

	("battle_tile_snakepass_new_d", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000005a07b2320004390d000069a1000052cc000071d1", [], [], "outer_terrain_desert"),

	("battle_tile_snakepass_new_s", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000004a07b2320004390d000069a1000052cc000071d1", [], [], "outer_terrain_snow"),

	("battle_tile_village", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000723201216c0054952000002df0000038700007600", [], [], "outer_terrain_steppe"),

	("battle_tile_village_desert", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000723201216c0054952000002df0000038700007600", [], [], "outer_terrain_desert"),

	("battle_tile_village_snow", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000723201216c0054952000002df0000038700007600", [], [], "outer_terrain_snow"),

	("battle_tile_village_jap", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000720e01200c0054952000050db00006001000076c0", [], [], "outer_terrain_steppe"),

	("battle_tile_village_urt", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000323201216c0054952000002df0000038700007600", [], [], "outer_terrain_steppe"),

	("battle_tile_village_teepee", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000323201216c0054952000002df0000038700007600", [], [], "outer_terrain_steppe"),

	("battle_tile_siege_valley", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000063000050000080601000039db00007af20000350a", [], [], "outer_terrain_steppe"),

	("battle_tile_siege_valley_d", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000065000050000080601000039db00007af20000350a", [], [], "outer_terrain_desert"),

	("battle_tile_siege_valley_s", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000064000050000080601000039db00007af20000350a", [], [], "outer_terrain_snow"),

	("battle_tile_siege_harbor", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000006300005000005053e000039db00007af20000350a", [], [], "outer_terrain_beach"),

	("battle_tile_siege_highland", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000006300005000005053e000039db00007af20000350a", [], [], "outer_terrain_steppe"),

	("battle_tile_siege_highland_d", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000006500005004005053e000039db00007af20000350a", [], [], "outer_terrain_desert"),

	("battle_tile_siege_highland_s", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000006400005004005053e000039db00007af20000350a", [], [], "outer_terrain_snow"),

	("molda_siege_fortruin", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000006300005000005053e000039db00007af20000350a", [], [], "outer_terrain_beach"),

	("hideout_bed", sf_indoors, "ex_bedroom", "bo_ex_bedroom", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("hideout_comp", sf_indoors, "8_tavern_euro_1", "bo_8_tavern_euro_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("hideout_slave", sf_indoors, "8_prison_euro", "bo_8_prison_euro", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("hideout_torture", sf_indoors, "8_prison_asia", "bo_8_prison_asia", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("brothel", sf_indoors, "8_tavern_euro_1", "bo_8_tavern_euro_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("pit_arena", sf_indoors, "8_hall_viking_1", "bo_8_hall_viking_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("public_bath", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x000000003a07b232000258960000013c00001fe100006dff", [], [], "outer_terrain_steppe"),

	("scene_for_capture", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x0000000730000500000258960000158600000bf1000053cc", [], [], "outer_terrain_steppe"),

	("all_scene_end", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000723201216c0054952000002df0000038700007600", [], []),

]