from header_common import *
from header_skills import *

####################################################################################################################
#  Each skill contains the following fields:
#  1) Skill id (string): used for referencing skills in other files. The prefix skl_ is automatically added before each skill-id .
#  2) Skill name (string).
#  3) Skill flags (int). See header_skills.py for a list of available flags
#  4) Maximum level of the skill (int).
#  5) Skill description (string): used in character window for explaining the skills.
# 
####################################################################################################################

#Hardcoded skills are {names (indexes, beginning with 0)}:
# Trade (1)
# Leadership (2)
# Prisoner Management (3)
# First Aid (9)
# Surgery (10)
# Wound Treatment (11)
# Inventory Management (12)
# Spotting (13)
# Pathfinding (14)
# Tactics (15)
# Tracking (16)
# Trainer (17)
# Engineer (18)
# Horse Archery (24)
# Riding (25)
# Athletics (26)
# Shield (27)
# Weapon Master (28)
# Power Draw (34)
# Power Throw (35)
# Power Strike (36)
# Ironflesh (37)
#
# The effects of these skills can only be removed if the skill is disabled with sf_inactive flag.
# If you want to add a new skill, use the reserved skills or use non-hardcoded skills.

skills = [
	("trade", "     ", sf_base_att_int, 0, "_____"),

	("leadership", "     ", sf_base_att_cha, 0, "_____"),

	("prisoner_management", "     ", sf_base_att_cha, 0, "_____"),

	("reserved_1", "Reserved Skill 1", sf_base_att_cha|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_2", "Reserved Skill 2", sf_base_att_cha|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_3", "Reserved Skill 3", sf_base_att_cha|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_4", "Reserved Skill 4", sf_base_att_cha|sf_inactive, 10, "This_is_a_reserved_skill."),

	("persuasion", "     ", sf_base_att_cha, 0, "_____"),

	("engineer", "     ", sf_base_att_int, 0, "_____"),

	("first_aid", "     ", sf_base_att_int|sf_inactive, 0, "_____"),

	("surgery", "     ", sf_base_att_int, 0, "_____"),

	("wound_treatment", "Wound Treatment", sf_base_att_int|sf_effects_party, 10, "Party_healing_speed_is_increased_by_20%%_per_level_of_this_skill._MAX:10_(Party_skill)"),

	("inventory_management", "     ", sf_base_att_int|sf_inactive, 10, "_____"),

	("spotting", "     ", sf_base_att_int, 0, "_____"),

	("pathfinding", "     ", sf_base_att_int, 0, "_____"),

	("tactics", "     ", sf_base_att_int, 0, "_____"),

	("tracking", "     ", sf_base_att_int|sf_inactive, 0, "_____"),

	("trainer", "     ", sf_base_att_int, 0, "_____"),

	("reserved_5", "Reserved Skill 5", sf_base_att_int|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_6", "Reserved Skill 6", sf_base_att_int|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_7", "Reserved Skill 7", sf_base_att_int|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_8", "Reserved Skill 8", sf_base_att_int|sf_inactive, 10, "This_is_a_reserved_skill."),

	("looting", "     ", sf_base_att_agi, 0, "_____"),

	("horse_archery", "Archery", sf_base_att_agi, 10, "Reduces_damage_and_accuracy_penalties_for_archery_and_throwing_from_horseback._(or_ship)__MAX:10_(Personal_skill)"),

	("riding", "Riding", sf_base_att_agi, 10, "Enables_you_to_ride_horses_of_higher_difficulty_levels_and_increases_your_riding_speed_and_manuever._MAX:10_(Personal_skill)"),

	("athletics", "Athletics", sf_base_att_agi, 10, "Improves_your_running_speed._If_you_use_heavy_armor,_you_will_be_slower._MAX:10_(Personal_skill)"),

	("shield", "Shield", sf_base_att_agi, 10, "Reduces_damage_to_shields_(by_8%%_per_skill_level)_and_improves_shield_speed_and_coverage._MAX:10_(Personal_skill)"),

	("weapon_master", "Weapon Master", sf_base_att_agi, 10, "Makes_it_easier_to_learn_weapon_proficiencies_and_increases_the_proficiency_limits._Limits_go_as:_60,_100,_140,_180,_220,_260,_300,_340,_380,_420.__MAX:10_(Personal_skill)"),

	("exploration", "     ", sf_base_att_int, 0, "_____"),

	("navigation", "     ", sf_base_att_int, 0, "_____"),

	("fascination", "     ", sf_base_att_cha, 0, "_____"),

	("reserved_12", "Reserved Skill 12", sf_base_att_agi|sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_13", "Reserved Skill 13", sf_base_att_agi|sf_inactive, 10, "This_is_a_reserved_skill."),

	("power_draw", "Power Draw", sf_base_att_str, 7, "Each_point_to_this_skill_increases_bow_shot_damage_by_14%%__MAX:7_(Personal_skill)"),

	("power_throw", "Power Throw", sf_base_att_str, 10, "Each_point_to_this_skill_increases_throwing_damage_by_10%%._MAX:10_(Personal_skill)"),

	("power_strike", "Power Strike", sf_base_att_str, 7, "Each_point_to_this_skill_increases_melee_damage_by_8%%._MAX:7_(Personal_skill)"),

	("ironflesh", "Ironflesh", sf_base_att_str, 10, "Each_point_to_this_skill_increases_hit_points_by_+2._MAX:10_(Personal_skill)"),

	("reserved_14", "Reserved Skill 14", sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_15", "Reserved Skill 15", sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_16", "Reserved Skill 16", sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_17", "Reserved Skill 17", sf_inactive, 10, "This_is_a_reserved_skill."),

	("reserved_18", "Reserved Skill 18", sf_inactive, 10, "This_is_a_reserved_skill."),

]