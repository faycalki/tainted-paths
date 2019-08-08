# -*- coding: cp1254 -*-
from header_common import *
from header_dialogs import *
from header_operations import *
from header_parties import *
from header_item_modifiers import *
from header_skills import *
from header_triggers import *
from ID_troops import *
from ID_party_templates import *

from module_constants import *


####################################################################################################################
# During a dialog, the dialog lines are scanned from top to bottom.
# If the dialog-line is spoken by the player, all the matching lines are displayed for the player to pick from.
# If the dialog-line is spoken by another, the first (top-most) matching line is selected.
#
#  Each dialog line contains the following fields:
# 1) Dialogue partner: This should match the person player is talking to.
#    Usually this is a troop-id.
#    You can also use a party-template-id by appending '|party_tpl' to this field.
#    Use the constant 'anyone' if you'd like the line to match anybody.
#    Appending '|plyr' to this field means that the actual line is spoken by the player
#    Appending '|other(troop_id)' means that this line is spoken by a third person on the scene.
#       (You must make sure that this third person is present on the scene)
#
# 2) Starting dialog-state:
#    During a dialog there's always an active Dialog-state.
#    A dialog-line's starting dialog state must be the same as the active dialog state, for the line to be a possible candidate.
#    If the dialog is started by meeting a party on the map, initially, the active dialog state is "start"
#    If the dialog is started by speaking to an NPC in a town, initially, the active dialog state is "start"
#    If the dialog is started by helping a party defeat another party, initially, the active dialog state is "party_relieved"
#    If the dialog is started by liberating a prisoner, initially, the active dialog state is "prisoner_liberated"
#    If the dialog is started by defeating a party led by a hero, initially, the active dialog state is "enemy_defeated"
#    If the dialog is started by a trigger, initially, the active dialog state is "event_triggered"
# 3) Conditions block (list): This must be a valid operation block. See header_operations.py for reference.  
# 4) Dialog Text (string):
# 5) Ending dialog-state:
#    If a dialog line is picked, the active dialog-state will become the picked line's ending dialog-state.
# 6) Consequences block (list): This must be a valid operation block. See header_operations.py for reference.
# 7) Voice-over (string): sound filename for the voice over. Leave here empty for no voice over
####################################################################################################################

dialogs = [
	[anyone, "start",
	[
		(store_conversation_troop, "$g_talk_troop"),
		(store_conversation_agent, "$g_talk_agent"),
		(store_faction_of_troop, "$g_talk_troop_faction", "$g_talk_troop"),
		(call_script, "script_troop_get_player_relation", "$g_talk_troop"),
		(assign, "$g_talk_troop_relation", reg0),
		(troop_get_slot, "$g_talk_troop_ego", "$g_talk_troop", slot_troop_player_order_object),
		(store_skill_level, ":skill_level_persuasion_player", "skl_persuasion", "trp_player"),
		(assign, "$g_talk_troop_effective_relation", "$g_talk_troop_relation"),
		(val_add, "$g_talk_troop_effective_relation", ":skill_level_persuasion_player"),
		(try_begin),
			(gt, "$g_talk_troop_effective_relation", 0),
			(store_add, ":value", 10, ":skill_level_persuasion_player"),
			(val_mul, "$g_talk_troop_effective_relation", ":value"),
			(val_div, "$g_talk_troop_effective_relation", 10),
		(else_try),
			(lt, "$g_talk_troop_effective_relation", 0),
			(store_sub, ":value", 20, ":skill_level_persuasion_player"),
			(val_mul, "$g_talk_troop_effective_relation", ":value"),
			(val_div, "$g_talk_troop_effective_relation", 20),
		(try_end),
		(val_clamp, "$g_talk_troop_effective_relation", -100, 101),
		(store_relation, "$g_talk_troop_faction_relation", "$g_talk_troop_faction", "fac_player_supporters_faction"),
		(try_begin),
			(troop_is_hero, "$g_talk_troop"),
			(talk_info_show, 1),
			(call_script, "script_setup_talk_info"),
		(try_end),
		(troop_get_slot, "$met_time", "$g_talk_troop", 15),
		(try_begin),
			(gt, "$met_time", 0),
			(assign, "$g_talk_troop_already_met", 1),
		(else_try),
			(assign, "$g_talk_troop_already_met", 0),
		(try_end),
		(try_begin),
			(call_script, "script_troop_type_sett", "trp_player"),
			(gt, "$troop_gender_type", 10),
			(assign, reg65, 1),
			(assign, "$player_gender", 1),
		(else_try),
			(assign, reg65, 0),
			(assign, "$player_gender", 0),
		(try_end),
		(try_begin),
			(call_script, "script_troop_type_sett", "$g_talk_troop"),
			(gt, "$troop_gender_type", 10),
			(assign, reg65, 1),
			(assign, "$talk_troop_gender", 1),
		(else_try),
			(assign, reg65, 0),
			(assign, "$talk_troop_gender", 0),
		(try_end),
		(assign, "$player_spouse", -1),
		(try_begin),
			(troop_slot_ge, "trp_player", 3, 1),
			(troop_get_slot, ":player_state", "trp_player", slot_troop_state),
			(troop_slot_eq, ":player_state", slot_troop_state, "trp_player"),
			(troop_slot_eq, "trp_player", slot_troop_state, ":player_state"),
			(assign, "$player_spouse", ":player_state"),
		(try_end),
		(try_begin),
			(faction_slot_eq, "$g_talk_troop_faction", 1, "$g_talk_troop"),
			(str_store_string, 64, "str_lord_lady_comment_1"),
			(str_store_string, 65, "str_lord_lady_comment_1"),
			(str_store_string, 66, "str_lord_lady_comment_1"),
			(str_store_string, 67, "str_lord_lady_comment_1"),
		(else_try),
			(str_store_string, 64, "str_lord_lady_comment_2"),
			(str_store_string, 65, "str_lord_lady_comment_2"),
			(str_store_string, 66, "str_lord_lady_comment_2"),
			(str_store_string, 67, "str_lord_lady_comment_2"),
		(try_end),
		(eq, 1, 0)
	],
	"{!}Warning: This line is never displayed. It is just for storing conversation variables.", "close_window",
	[]],

	[anyone, "member_chat",
	[
		(store_conversation_troop, "$g_talk_troop"),
		(try_begin),
			(troop_is_hero, "$g_talk_troop"),
			(talk_info_show, 1),
			(call_script, "script_setup_talk_info"),
		(try_end),
		(troop_get_type, reg65, "$g_talk_troop"),
		(troop_get_type, reg65, "$g_talk_troop"),
		(try_begin),
			(faction_slot_eq, "$g_talk_troop_faction", 1, "$g_talk_troop"),
			(str_store_string, 64, "str_lord_lady_comment_1"),
			(str_store_string, 65, "str_lord_lady_comment_1"),
			(str_store_string, 66, "str_lord_lady_comment_1"),
		(else_try),
			(str_store_string, 64, "str_lord_lady_comment_2"),
			(str_store_string, 65, "str_lord_lady_comment_2"),
			(str_store_string, 66, "str_lord_lady_comment_2"),
		(try_end),
		(eq, 1, 0)
	],
	"{!}Warning: This line is never displayed. It is just for storing conversation variables.", "close_window",
	[]],

	[anyone, "event_triggered",
	[
		(store_conversation_troop, "$g_talk_troop"),
		(try_begin),
			(troop_is_hero, "$g_talk_troop"),
			(talk_info_show, 1),
			(call_script, "script_setup_talk_info"),
		(try_end),
		(troop_get_type, reg65, "$g_talk_troop"),
		(try_begin),
			(faction_slot_eq, "$g_talk_troop_faction", 1, "$g_talk_troop"),
			(str_store_string, 64, "str_lord_lady_comment_1"),
			(str_store_string, 65, "str_lord_lady_comment_1"),
			(str_store_string, 66, "str_lord_lady_comment_1"),
		(else_try),
			(str_store_string, 64, "str_lord_lady_comment_2"),
			(str_store_string, 65, "str_lord_lady_comment_2"),
			(str_store_string, 66, "str_lord_lady_comment_2"),
		(try_end),
		(eq, 1, 0)
	],
	"{!}Warning: This line is never displayed. It is just for storing conversation variables.", "close_window",
	[]],

	[trp_hideout_warder, "start",
	[],
	"Yes master. How can i help??", "hideout_warder_1",
	[]],

	[trp_hideout_torturer, "start",
	[],
	"Yes master?", "hideout_torturer_1",
	[]],

	[trp_brothel_manager, "start",
	[],
	"Welcome, master.", "brothel_manager",
	[]],

	[trp_fightpit_manager, "start",
	[],
	"Hmm...", "nakepit_manager",
	[]],

	[trp_fightpit_manager, "start",
	[],
	"Hmm...", "nakepit_manager",
	[]],

	[trp_hideout_dancer, "start",
	[],
	"Thank you!", "close_window",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 10, 87)
	]],

	[trp_bath_manager, "start",
	[],
	"What can i do for you?", "bath_manager",
	[]],

	[trp_hideout_chef, "start",
	[],
	" What can i do for you?", "hideout_chef_1",
	[]],

	[trp_covered_face_player_woman, "start",
	[],
	"(It's me.)", "close_window",
	[]],

	[trp_covered_face_player, "start",
	[],
	"(Me, myself and i.)", "close_window",
	[]],

	[trp_playerself_temp, "start",
	[
		(store_conversation_troop, "$g_talk_troop")
	],
	"It's my pussy.", "cunt_view_self",
	[
		(str_clear, 43),
		(call_script, "script_molda_s_scene", 51, 0)
	]],

	[anyone, "cunt_view_self",
	[],
	"{s43}", "close_window",
	[
		(call_script, "script_molda_s_scene", 51, 0)
	]],

	[trp_fugitive, "start",
	[],
	"What do you want?", "fugitive_1",
	[]],

	[auto_proceed|trp_relative_of_merchant, "start",
	[],
	"{!}.", "temp_talker",
	[]],

	[trp_vaegir_merchant, "start",
	[
		(eq, "$main_q_step", 94)
	],
	"[He is extremely embarrassed] Why are you here!?", "mq_94_1",
	[]],

	[trp_vaegir_merchant, "start",
	[
		(eq, "$main_q_step", 95)
	],
	"Sorry. I owe you an apology for... Everything.", "mq_95_1",
	[]],

	[anyone, "start",
	[
		(eq, "$main_q_step", 20),
		(eq, "$g_talk_troop", "$first_comp_id")
	],
	"You're too late. {playername}. They have already moved elsewhere.", "mainq_20_1",
	[]],

	[anyone, "start",
	[
		(eq, "$main_q_step", 48),
		(eq, "$g_talk_troop", "$main_q_troop")
	],
	"You have helped us so much... I want to repay you. Let me join your party.", "mainq_48_1",
	[]],

	[anyone, "start",
	[
		(eq, "$g_talk_troop", "$younger_sister_id"),
		(try_begin),
			(eq, "$current_mission_template", "mt_quest_brothel_mission"),
			(eq, "$main_q_step", 16),
			(try_for_agents, ":var_1"),
				(agent_is_human, ":var_1"),
				(agent_is_alive, ":var_1"),
				(agent_set_is_alarmed, ":var_1", 1),
			(try_end),
			(str_store_string, 15, "str_mq_1_16y_pre"),
		(else_try),
			(eq, "$main_q_step", 44),
			(str_store_string, 15, "str_mq_1_44y_pre"),
		(else_try),
			(eq, "$main_q_step", 50),
			(str_store_string, 15, "str_mq_1_50y_pre"),
		(else_try),
			(str_store_string, 15, "str_mq_sis_ord_talk"),
		(try_end)
	],
	"{s15}", "sister_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$current_mission_template", "mt_quest_brothel_mission"),
		(eq, "$main_q_step", 16),
		(neq, "$g_talk_troop", "$younger_sister_id")
	],
	"(Groan)", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 14)
	],
	"I've got you!", "female_ply_raped_1",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 13),
		(eq, "$g_talk_troop", "$temp_num_01")
	],
	"Oh! God. Sorry! Sorry!", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 13),
		(store_random_in_range, ":random_in_range_bath_comment_1_bath_comment_end", "str_bath_comment_1", "str_bath_comment_end"),
		(str_store_string, 8, ":random_in_range_bath_comment_1_bath_comment_end")
	],
	"{s8}", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 12),
		(try_begin),
			(gt, "$troop_gender_type", 10),
			(str_store_string, 11, "str_nakepit_talk_female"),
		(else_try),
			(neq, "$g_talk_troop", "$pit_fighter_1"),
			(neq, "$g_talk_troop", "$pit_fighter_2"),
			(neq, "$g_talk_troop", "$pit_fighter_3"),
			(neq, "$g_talk_troop", "$pit_fighter_4"),
			(store_random_in_range, ":random_in_range_0_4", 0, 4),
			(try_begin),
				(eq, ":random_in_range_0_4", 0),
				(str_store_troop_name, 8, "$pit_fighter_1"),
			(else_try),
				(eq, ":random_in_range_0_4", 1),
				(str_store_troop_name, 8, "$pit_fighter_2"),
			(else_try),
				(eq, ":random_in_range_0_4", 2),
				(str_store_troop_name, 8, "$pit_fighter_3"),
			(else_try),
				(str_store_troop_name, 8, "$pit_fighter_4"),
			(try_end),
			(str_store_string, 11, "str_nakepit_talk_male"),
		(else_try),
			(str_store_string, 11, "str_nakepit_talk_malefighter"),
		(try_end)
	],
	"{s11}", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 21),
		(eq, "$g_talk_troop", "$wm_slave_dancer"),
		(is_between, "$wm_slave_dancer", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(troop_slot_eq, "$wm_slave_dancer", slot_troop_leaded_party, 3),
		(troop_get_slot, "$slave_attitude", "$g_talk_troop", slot_troop_age_appearance),
		(try_begin),
			(eq, "$slave_attitude", 5),
			(str_store_string, 11, "str_slave_state_5"),
			(str_store_string, 12, "str_slave_intro_5"),
		(else_try),
			(eq, "$slave_attitude", 4),
			(str_store_string, 11, "str_slave_state_4"),
			(str_store_string, 12, "str_slave_intro_4"),
		(else_try),
			(eq, "$slave_attitude", 3),
			(str_store_string, 11, "str_slave_state_3"),
			(str_store_string, 12, "str_slave_intro_3"),
		(else_try),
			(eq, "$slave_attitude", 2),
			(str_store_string, 11, "str_slave_state_2"),
			(str_store_string, 12, "str_slave_intro_2"),
		(else_try),
			(eq, "$slave_attitude", 1),
			(str_store_string, 11, "str_slave_state_1"),
			(str_store_string, 12, "str_slave_intro_1"),
		(else_try),
			(eq, "$slave_attitude", 0),
			(str_store_string, 11, "str_slave_state_0"),
			(str_store_string, 12, "str_slave_intro_0"),
		(try_end)
	],
	"({s11}) {s12}", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 9),
		(is_between, "$g_talk_troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(troop_get_slot, "$slave_attitude", "$g_talk_troop", slot_troop_age_appearance),
		(try_begin),
			(eq, "$slave_attitude", 5),
			(str_store_string, 11, "str_slave_state_5"),
			(str_store_string, 12, "str_slave_intro_5"),
		(else_try),
			(eq, "$slave_attitude", 4),
			(str_store_string, 11, "str_slave_state_4"),
			(str_store_string, 12, "str_slave_intro_4"),
		(else_try),
			(eq, "$slave_attitude", 3),
			(str_store_string, 11, "str_slave_state_3"),
			(str_store_string, 12, "str_slave_intro_3"),
		(else_try),
			(eq, "$slave_attitude", 2),
			(str_store_string, 11, "str_slave_state_2"),
			(str_store_string, 12, "str_slave_intro_2"),
		(else_try),
			(eq, "$slave_attitude", 1),
			(str_store_string, 11, "str_slave_state_1"),
			(str_store_string, 12, "str_slave_intro_1"),
		(else_try),
			(eq, "$slave_attitude", 0),
			(str_store_string, 11, "str_slave_state_0"),
			(str_store_string, 12, "str_slave_intro_0"),
		(try_end)
	],
	"({s11}) {s12}", "lady_slave_prison",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 10),
		(is_between, "$g_talk_troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(troop_get_slot, "$slave_attitude", "$g_talk_troop", slot_troop_age_appearance),
		(try_begin),
			(eq, "$slave_attitude", 5),
			(str_store_string, 11, "str_slave_state_5"),
			(str_store_string, 12, "str_slave_intro_5"),
		(else_try),
			(eq, "$slave_attitude", 4),
			(str_store_string, 11, "str_slave_state_4"),
			(str_store_string, 12, "str_slave_intro_4"),
		(else_try),
			(eq, "$slave_attitude", 3),
			(str_store_string, 11, "str_slave_state_3"),
			(str_store_string, 12, "str_slave_intro_3"),
		(else_try),
			(eq, "$slave_attitude", 2),
			(str_store_string, 11, "str_slave_state_2"),
			(str_store_string, 12, "str_slave_intro_2"),
		(else_try),
			(eq, "$slave_attitude", 1),
			(str_store_string, 11, "str_slave_state_1"),
			(str_store_string, 12, "str_slave_intro_1"),
		(else_try),
			(eq, "$slave_attitude", 0),
			(str_store_string, 11, "str_slave_state_0"),
			(str_store_string, 12, "str_slave_intro_0"),
		(try_end)
	],
	"({s11}) {s12}", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 10),
		(neg|is_between, "$g_talk_troop", "trp_tt_lady_01_01", "trp_tt_lady_end")
	],
	"As you command!", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 11),
		(is_between, "$g_talk_troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(troop_get_slot, "$slave_attitude", "$g_talk_troop", slot_troop_age_appearance),
		(try_begin),
			(eq, "$slave_attitude", 5),
			(str_store_string, 11, "str_slave_state_5"),
			(str_store_string, 12, "str_slave_brothel_5"),
		(else_try),
			(eq, "$slave_attitude", 4),
			(str_store_string, 11, "str_slave_state_4"),
			(str_store_string, 12, "str_slave_brothel_4"),
		(else_try),
			(eq, "$slave_attitude", 3),
			(str_store_string, 11, "str_slave_state_3"),
			(str_store_string, 12, "str_slave_brothel_3"),
		(else_try),
			(eq, "$slave_attitude", 2),
			(str_store_string, 11, "str_slave_state_2"),
			(str_store_string, 12, "str_slave_brothel_2"),
		(else_try),
			(eq, "$slave_attitude", 1),
			(str_store_string, 11, "str_slave_state_1"),
			(str_store_string, 12, "str_slave_brothel_1"),
		(else_try),
			(eq, "$slave_attitude", 0),
			(str_store_string, 11, "str_slave_state_0"),
			(str_store_string, 12, "str_slave_brothel_0"),
		(try_end)
	],
	"({s11}) {s12}", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 11),
		(neg|is_between, "$g_talk_troop", "trp_tt_lady_01_01", "trp_tt_lady_end")
	],
	"(Groan)", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$qquest_type", 32),
		(is_between, "$g_talk_troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
		(eq, "$qquest_target_troop", "$g_talk_troop"),
		(eq, "$qquest_progress", 0)
	],
	"By God, You are a brave soul indeed. I won't forget this.", "close_window",
	[
		(assign, "$qquest_progress", 1),
		(display_message, "str_questsucc", 0x00ffff00),
		(play_sound, "snd_quest_succeeded"),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 35),
		(troop_set_slot, "$g_talk_troop", slot_troop_cur_center, 0),
		(troop_set_slot, "$g_talk_troop", slot_troop_present_at_event, 0),
		(str_store_troop_name, 8, "$g_talk_troop"),
		(str_store_party_name, 9, "$g_encountered_party"),
		(display_message, "str_lord_escape_ai"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return")
	]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 17),
		(is_between, "$g_talk_troop", "trp_tt_lord_01_00", "trp_tt_lord_end")
	],
	"You'll not live long enough to enjoy your victory. My kinsmen will soon wipe out the stain of this defeat.", "lord_captured_1",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 8),
		(is_between, "$g_talk_troop", "trp_tt_lord_01_00", "trp_tt_lord_end")
	],
	"Finally! I've caught you!", "lord_ntr_1",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 16),
		(is_between, "$g_talk_troop", "trp_tt_lady_01_01", "trp_tt_lady_end")
	],
	"Please. I plead for your mercy.", "lady_capture_1",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 6),
		(eq, "$g_talk_troop", "$g_sex_trade_comp_id"),
		(try_begin),
			(this_or_next|eq, "$g_talk_troop_ego", 13),
			(eq, "$g_talk_troop_ego", 14),
			(assign, ":value", "str_lady_say_05"),
		(else_try),
			(assign, ":value", "str_lady_say_06"),
		(try_end),
		(str_store_string, 43, ":value")
	],
	"{s43}", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 4),
		(is_between, "$g_talk_troop", "trp_religionists_1", "trp_prostitute_1")
	],
	"Greetings. I am a priest. How can i help?", "religionist_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 19),
		(eq, "$main_q_step", 46),
		(is_between, "$g_talk_troop", "trp_tt_lady_ex_01", "trp_tt_lady_orphan_01")
	],
	"Thank you for rescuing me, but i am worried about my village!", "mq_46_1",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 19),
		(is_between, "$g_talk_troop", "trp_tt_lady_01_01", "trp_tt_lady_end")
	],
	"Thank you for rescuing me. At last, i can go home...", "lady_rescue_1",
	[]],

	[anyone, "start",
	[
		(eq, "$qquest_type", 24),
		(eq, "$wm_talk_state", 4),
		(is_between, "$g_talk_troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(eq, "$g_talk_troop", "$qquest_target_faction")
	],
	"Oh my god.", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 5),
		(is_between, "$g_talk_troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(try_begin),
			(troop_slot_eq, "$g_talk_troop", 41, 3),
			(assign, ":value", "str_revengeful_lord_say_01"),
		(else_try),
			(lt, "$g_talk_troop_relation", -10),
			(assign, ":value", "str_lady_say_01"),
		(else_try),
			(eq, "$player_gender", 0),
			(eq, "$g_talk_troop", "$player_spouse"),
			(assign, ":value", "str_lady_say_02"),
		(else_try),
			(eq, "$g_talk_troop_already_met", 0),
			(assign, ":value", "str_lady_say_03"),
			(troop_get_slot, ":g_talk_troop_15", "$g_talk_troop", 15),
			(val_add, ":g_talk_troop_15", 1),
			(troop_set_slot, "$g_talk_troop", 15, ":g_talk_troop_15"),
		(else_try),
			(assign, ":value", "str_lady_say_04"),
		(try_end),
		(str_store_string, 43, ":value")
	],
	"{s43}", "lady_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 5),
		(is_between, "$g_talk_troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(try_begin),
			(troop_slot_eq, "$g_talk_troop", 41, 3),
			(assign, ":value", "str_revengeful_lord_say_01"),
		(else_try),
			(lt, "$g_talk_troop_relation", -10),
			(assign, ":value", "str_lady_say_01"),
		(else_try),
			(eq, "$player_gender", 0),
			(eq, "$g_talk_troop", "$player_spouse"),
			(assign, ":value", "str_lady_say_02"),
		(else_try),
			(eq, "$g_talk_troop_already_met", 0),
			(assign, ":value", "str_lady_say_03"),
			(troop_get_slot, ":g_talk_troop_15", "$g_talk_troop", 15),
			(val_add, ":g_talk_troop_15", 1),
			(troop_set_slot, "$g_talk_troop", 15, ":g_talk_troop_15"),
		(else_try),
			(assign, ":value", "str_lady_say_04"),
		(try_end),
		(str_store_string, 43, ":value")
	],
	"{s43}", "lady_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 5),
		(eq, "$g_talk_troop", "$player_spouse"),
		(lt, "$g_talk_troop_relation", -10)
	],
	"Don't bothering me!", "lady_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 15),
		(eq, "$g_talk_troop", "$enemy_commander"),
		(party_slot_eq, "$g_encountered_party", slot_party_type, 4),
		(play_sound, "snd_encounter_farmers")
	],
	"Please do not attack! We are just commoners, i beg of you - show mercy!", "attack_innocent_1",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 15),
		(eq, "$g_talk_troop", "$enemy_commander"),
		(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, 3),
		(party_slot_eq, "$g_encountered_party", slot_party_type, 2),
		(store_random_in_range, ":random_in_range_attack_comment_01_attack_comment_end", "str_attack_comment_01", "str_attack_comment_end"),
		(str_store_string, 43, ":random_in_range_attack_comment_01_attack_comment_end"),
		(play_sound, "snd_encounter_bandits")
	],
	"{s43}", "close_window",
	[
		(finish_mission),
		(assign, "$wm_target_party", "$g_encountered_party"),
		(jump_to_menu, "mnu_low_encounter")
	]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 15),
		(eq, "$g_talk_troop", "$enemy_commander"),
		(party_slot_eq, "$g_encountered_party", slot_party_type, 1),
		(store_random_in_range, ":random_in_range_attack_comment_01_attack_comment_end", "str_attack_comment_01", "str_attack_comment_end"),
		(try_begin),
			(eq, "$g_talk_troop_already_met", 0),
			(store_random_in_range, ":random_in_range_attack_comment_01_attack_comment_end", "str_enemy_meet_default", "str_enemy_meet_end"),
		(else_try),
			(troop_slot_ge, "$g_talk_troop", 26, 11),
			(try_begin),
				(troop_slot_eq, "$g_talk_troop", slot_troop_last_persuasion_time, 11),
				(store_random_in_range, ":random_in_range_attack_comment_01_attack_comment_end", "str_comment_you_defeated_me_enemy_chivalrous", "str_comment_you_defeated_me_enemy_end"),
			(else_try),
				(troop_slot_eq, "$g_talk_troop", slot_troop_last_persuasion_time, 12),
				(store_random_in_range, ":random_in_range_attack_comment_01_attack_comment_end", "str_comment_you_captured_my_castle_enemy_spiteful", "str_comment_you_captured_my_castle_enemy_end"),
			(else_try),
				(troop_slot_eq, "$g_talk_troop", slot_troop_last_persuasion_time, 13),
				(store_random_in_range, ":random_in_range_attack_comment_01_attack_comment_end", "str_comment_you_ran_from_me_enemy_spiteful", "str_comment_you_ran_from_me_enemy_end"),
			(try_end),
		(try_end),
		(str_store_string, 43, ":random_in_range_attack_comment_01_attack_comment_end"),
		#(play_sound, "snd_encounter_vaegirs_enemy")
	],
	"{s43}", "close_window",
	[
		(finish_mission),
		(assign, "$wm_target_party", "$g_encountered_party"),
		(jump_to_menu, "mnu_wm_attack_menu")
	]],

	[anyone, "start",
	[
		(is_between, "$g_talk_troop", "trp_temp_commander_fac_01", "trp_temp_commander_end")
	],
	"What do you want?", "temp_commander_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$qquest_type", 24),
		(eq, "$wm_talk_state", 4),
		(is_between, "$g_talk_troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
		(eq, "$g_talk_troop", "$qquest_target_troop")
	],
	"What are you doing here? Dont tell my wife. I will buy your silence.", "lord_misdoubt",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 1),
		(is_between, "$g_talk_troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
		(troop_slot_eq, "$g_talk_troop", slot_troop_cur_center, 2)
	],
	"I am in your debt for freeing me, {playername}.", "lord_prisoner_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 21),
		(is_between, "$g_talk_troop", "trp_tt_lord_01_00", "trp_tt_lord_end")
	],
	"Thank you for your inviation. What a nice mansion.", "lord_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 6),
		(is_between, "$g_talk_troop", "trp_tt_lord_01_00", "trp_tt_lord_end")
	],
	"This will be a great time, thank you.", "close_window",
	[
		(call_script, "script_molda_s_scene", 5, 0)
	]],

	[anyone, "start",
	[
		(is_between, "$g_talk_troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
		(eq, "$g_talk_troop", "$player_spouse")
	],
	"Yes, my wife?", "lord_talk",
	[]],

	[anyone, "start",
	[
		(is_between, "$g_talk_troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
		(ge, "$g_talk_troop_relation", 50),
		(eq, "$wm_talk_state", 5),
		(neq, "$g_talk_troop", "$player_spouse"),
		(neg|troop_slot_ge, "$g_talk_troop", 3, "trp_tt_lady_01_01"),
		(neg|troop_slot_ge, "trp_player", 3, "trp_tt_lord_01_00"),
		(eq, "$talk_troop_gender", 0),
		(eq, "$player_gender", 1),
		(store_random_in_range, ":random_in_range_0_8", 0, 8),
		(eq, ":random_in_range_0_8", 0)
	],
	"{playername}, I want to talk about our relationship.", "lord_propose_to_ply_1",
	[]],

	[anyone, "start",
	[
		(is_between, "$g_talk_troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
		(try_begin),
			(troop_slot_eq, "$g_talk_troop", 41, 3),
			(assign, ":value", "str_revengeful_lord_say_01"),
		(else_try),
			(eq, "$g_talk_troop_already_met", 0),
			(try_begin),
				(lt, "$g_talk_troop_faction_relation", 0),
				(assign, ":value", "str_unlike_first_meet_lord_say_01"),
			(else_try),
				(troop_slot_ge, "trp_player", 13, 75),
				(store_random_in_range, ":value", "str_comment_intro_famous_liege", "str_comment_intro_famous_end"),
			(else_try),
				(eq, "$player_noble", 1),
				(store_random_in_range, ":value", "str_comment_intro_noble_liege", "str_comment_intro_noble_end"),
			(else_try),
				(store_random_in_range, ":value", "str_comment_intro_common_liege", "str_comment_intro_common_end"),
			(try_end),
			(troop_get_slot, ":g_talk_troop_15", "$g_talk_troop", 15),
			(val_add, ":g_talk_troop_15", 1),
			(troop_set_slot, "$g_talk_troop", 15, ":g_talk_troop_15"),
		(else_try),
			(troop_slot_ge, "$g_talk_troop", 26, 1),
			(neg|troop_slot_ge, "$g_talk_troop", 26, 11),
			(try_begin),
				(troop_slot_eq, "$g_talk_troop", slot_troop_last_persuasion_time, 1),
				(neg|troop_slot_ge, "$g_talk_troop", 24, 3),
				(store_random_in_range, ":value", "str_battle_won_default", "str_battle_won_end"),
				(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 8),
			(else_try),
				(troop_slot_eq, "$g_talk_troop", slot_troop_last_persuasion_time, 1),
				(store_random_in_range, ":value", "str_comment_we_defeated_a_lord_unfriendly_spiteful", "str_comment_we_defeated_end"),
				(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 5),
			(else_try),
				(troop_slot_eq, "$g_talk_troop", slot_troop_last_persuasion_time, 2),
				(store_random_in_range, ":value", "str_comment_we_fought_in_siege_unfriendly_spiteful", "str_comment_we_fought_in_siege_default"),
				(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 5),
			(else_try),
				(troop_slot_eq, "$g_talk_troop", slot_troop_last_persuasion_time, 3),
				(store_random_in_range, ":value", "str_comment_you_abandoned_us_unfriendly_spiteful", "str_comment_you_abandoned_us_end"),
				(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -15),
			(else_try),
				(troop_slot_eq, "$g_talk_troop", slot_troop_last_persuasion_time, 4),
				(neg|troop_slot_ge, "$g_talk_troop", 24, 3),
				(store_random_in_range, ":value", "str_battle_won_grudging_default", "str_battle_won_grudging_end"),
				(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 10),
			(else_try),
				(troop_slot_eq, "$g_talk_troop", slot_troop_last_persuasion_time, 5),
				(neg|troop_slot_ge, "$g_talk_troop", 24, 3),
				(store_random_in_range, ":value", "str_battle_won_unfriendly_default", "str_battle_won_unfriendly_end"),
			(else_try),
				(troop_slot_eq, "$g_talk_troop", slot_troop_last_persuasion_time, 6),
				(store_random_in_range, ":value", "str_lord_derogatory_result", "str_lord_derogatory_end"),
				(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -10),
			(else_try),
				(troop_slot_eq, "$g_talk_troop", slot_troop_last_persuasion_time, 7),
				(store_random_in_range, ":value", "str_comment_our_king_granted_you_a_fief_allied_friendly", "str_comment_our_king_granted_you_a_fief_end"),
			(else_try),
				(troop_slot_eq, "$g_talk_troop", slot_troop_last_persuasion_time, 8),
				(store_random_in_range, ":value", "str_comment_you_renounced_your_alliegance_enemy_friendly", "str_comment_you_renounced_your_alliegance_end"),
				(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -10),
			(try_end),
			(troop_set_slot, "$g_talk_troop", slot_troop_last_persuasion_time, 0),
			(troop_set_slot, "$g_talk_troop", slot_troop_last_quest, 0),
		(else_try),
			(lt, "$g_talk_troop_faction_relation", 0),
			(assign, ":value", "str_dontlike_lord_say_01"),
			(try_begin),
				(eq, "$pre_battle_result_save", 2),
				(store_random_in_range, ":value", "str_comment_you_were_defeated_allied_friendly_spiteful", "str_comment_you_were_defeated_allied_end"),
				(assign, "$pre_battle_result_save", 0),
			(try_end),
		(else_try),
			(store_random_in_range, ":value", "str_lord_pre_comment_01", "str_lord_pre_comment_end"),
			(try_begin),
				(eq, "$pre_battle_result_save", 2),
				(store_random_in_range, ":value", "str_comment_we_were_defeated_unfriendly_spiteful", "str_comment_you_were_defeated_end"),
				(assign, "$pre_battle_result_save", 0),
			(try_end),
		(try_end),
		(str_store_string, 43, ":value")
	],
	"{s43}", "lord_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 0),
		(is_between, "$g_talk_troop", "trp_caravan_master2", "trp_covered_face_player_woman")
	],
	"Greetings.", "caravan_master_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 3),
		(is_between, "$g_talk_troop", "trp_farmer", "trp_town_walker_1"),
		(eq, "$wm_buying_drink_for_army", 0),
		(store_add, ":value", "$comp_rel_passsss", 3),
		(store_sub, reg3, ":value", 1),
		(store_sub, reg4, reg3, 1),
		(store_character_level, ":character_level_g_talk_troop", "$g_talk_troop"),
		(val_sub, ":character_level_g_talk_troop", 8),
		(val_mul, ":value", ":character_level_g_talk_troop"),
		(val_mul, ":value", 30),
		(assign, reg5, ":value")
	],
	"Do you have a need for mercenaries, {sir/madam}? {reg3?Me and {reg4?{reg3} of my mates:one of my mates} are:I am} looking for a master. We'll join you for {reg5} denars.", "tavern_mer_rec_1",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 4),
		(is_between, "$g_talk_troop", "trp_farmer", "trp_town_walker_1"),
		(eq, "$prison_guard_agent", "$g_talk_agent")
	],
	"Yes? What do you want?", "prison_guard_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 4),
		(is_between, "$g_talk_troop", "trp_farmer", "trp_town_walker_1"),
		(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
		(neq, "$wm_player_fac", ":faction_of_party_g_encountered_party")
	],
	"Greetings, stranger.", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 4),
		(is_between, "$g_talk_troop", "trp_farmer", "trp_town_walker_1"),
		(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
		(eq, "$wm_player_fac", ":faction_of_party_g_encountered_party")
	],
	"(The soldier stood to attention and saluted.)", "close_window",
	[
		(play_sound, "snd_man_victory")
	]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 5),
		(is_between, "$g_talk_troop", "trp_farmer", "trp_town_walker_1")
	],
	"(the soldier is staring straight ahead.)", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 1),
		(is_between, "$g_talk_troop", "trp_farmer", "trp_town_walker_1"),
		(str_store_troop_name, 15, "$g_sex_officer")
	],
	"{s15}-chan daisuki!!!  ", "close_window",
	[]],

	[anyone, "start",
	[
		(neq, "$wm_talk_state", 1),
		(neq, "$wm_talk_state", 5),
		(neq, "$wm_talk_state", 4),
		(is_between, "$g_talk_troop", "trp_farmer", "trp_town_walker_1")
	],
	"( The soldier stood to attention and saluted.)", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 1),
		(call_script, "script_wm_main_party_has_troop_sc", "$g_talk_troop"),
		(eq, "$wm_comp_continue", 1),
		(eq, "$g_talk_troop", "$g_sex_officer")
	],
	"(groan)", "close_window",
	[
		(try_begin),
			(call_script, "script_troop_type_sett", "$g_talk_troop"),
			(neq, "$troop_gender_type", 14),
			(play_sound, "snd_sex_female"),
		(else_try),
			(call_script, "script_troop_type_sett", "$g_talk_troop"),
			(eq, "$troop_gender_type", 14),
			(play_sound, "snd_sex_asian_female"),
		(try_end)
	]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 1),
		(eq, "$g_talk_troop", "$orphan_girl_troop_id"),
		(call_script, "script_wm_main_party_has_troop_sc", "$g_talk_troop"),
		(neq, "$wm_comp_continue", 1)
	],
	"Hi, {playername}", "orphan_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 1),
		(is_between, "$g_talk_troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(eq, "$player_gender", 0),
		(eq, "$g_talk_troop", "$player_spouse")
	],
	"Yes, my husband?", "member_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 1),
		(call_script, "script_wm_main_party_has_troop_sc", "$g_talk_troop"),
		(eq, "$wm_comp_continue", 1)
	],
	"Yes, {playername}?", "member_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_comp_id_standby", "$g_talk_troop")
	],
	"{playername}, i can't stand waiting much longer. To accept me formally, you will have to exclude the others.", "standby_talk",
	[]],

	[anyone, "start",
	[
		(call_script, "script_wm_main_party_has_troop_sc", "$g_talk_troop"),
		(eq, "$wm_comp_continue", 1)
	],
	"Keep going.", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$g_talk_troop_already_met", 1),
		(neq, "$g_talk_troop", "$player_spouse"),
		(this_or_next|is_between, "$g_talk_troop", "trp_npc1", "trp_kingdom_1_lord"),
		(is_between, "$g_talk_troop", "trp_tt_lady_ex_01", "trp_tt_lady_orphan_01"),
		(call_script, "script_wm_main_party_has_troop_sc", "$g_talk_troop"),
		(eq, "$wm_comp_continue", 0)
	],
	"I haven't seen you for a long time, what has happened?", "ex_lady_rejoin",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 3),
		(is_between, "$g_talk_troop", "trp_town_1_tavernkeeper", "trp_town_1_merchant")
	],
	"Good day dear {sir/madam}. How can I help you?", "tavernkeeper_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 3),
		(is_between, "$g_talk_troop", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin")
	],
	"Hi. Please tell me what you want to do.", "prostitute_talk",
	[
		(play_track, "track_calm_night_2", 2)
	]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 3),
		(is_between, "$g_talk_troop", "trp_tavern_minstrel_1", "trp_religionists_1")
	],
	"Greetings to you, this alcohol is manure.", "bard_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 3),
		(is_between, "$g_talk_troop", "trp_tavern_traveler_1", "trp_tavern_bookseller_1")
	],
	"Greetings, friend. I travel a lot all across the world and keep an open ear. I can provide you information that you might find useful.", "traveler_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 3),
		(is_between, "$g_talk_troop", "trp_ransom_broker_1", "trp_tavern_traveler_1")
	],
	"Greetings. If you have any prisoners, I will be happy to buy them off you.", "ransom_talk",
	[]],

	[anyone, "start",
	[
		(this_or_next|eq, "$wm_talk_state", 4),
		(eq, "$wm_talk_state", 20),
		(is_between, "$g_talk_troop", "trp_town_walker_1", "trp_tournament_master")
	],
	"Good day, {sir/madam}.", "walker_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 4),
		(is_between, "$g_talk_troop", "trp_town_1_armorer", "trp_town_1_weaponsmith")
	],
	"Good day, {sir/madam}.", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 4),
		(is_between, "$g_talk_troop", "trp_town_1_weaponsmith", "trp_town_1_tavernkeeper")
	],
	"Good day, {sir/madam}.", "close_window",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 4),
		(is_between, "$g_talk_troop", "trp_town_1_merchant", "trp_town_1_horse_merchant")
	],
	"Good day, {sir/madam}.", "goods_merchant_talk",
	[]],

	[anyone, "start",
	[
		(eq, "$wm_talk_state", 4),
		(is_between, "$g_talk_troop", "trp_town_1_horse_merchant", "trp_town_1_mayor")
	],
	"Good day, {sir/madam}.", "close_window",
	[]],

	[anyone, "start",
	[
		(is_between, "$g_talk_troop", "trp_sponsor_1", "trp_sponsor_end")
	],
	"Welcome to the academy, travelers.", "academy_pre_talk",
	[]],

	[trp_noble_woman, "start",
	[],
	"Who sent you? I will give you money, please do not hurt me! 2,000 denars? 5,000 denars? Yes, I'll give you 10,000 denars!", "insult_woman_mst_talk_1",
	[]],

	[anyone|plyr, "insult_woman_mst_talk_1",
	[],
	"[Insult] It is a message of the client. To be precise, my penis.", "insult_woman_mst_talk_2",
	[
		(play_sound, "snd_cryyy_female"),
		(call_script, "script_molda_s_scene", 19, 0)
	]],

	[anyone, "insult_woman_mst_talk_2",
	[],
	"[woman crying]", "insult_woman_mst_talk_3",
	[]],

	[anyone|plyr, "insult_woman_mst_talk_3",
	[],
	"[tear clothes]", "insult_woman_mst_talk_4",
	[
		(call_script, "script_molda_s_scene", 1, 0)
	]],

	[anyone, "insult_woman_mst_talk_4",
	[],
	"[woman crying]", "insult_woman_mst_talk_5",
	[]],

	[anyone|plyr, "insult_woman_mst_talk_5",
	[],
	"[Rape]", "close_window",
	[
		(assign, "$wm_quest_result", 1),
		(call_script, "script_wm_honor_change_diff", "trp_player", 2, 34),
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_male_p_fuck_rape")
	]],

	[anyone|plyr, "insult_woman_mst_talk_1",
	[],
	"Good. If you pay, you can keep your life.", "insult_woman_gold_1",
	[]],

	[anyone, "insult_woman_gold_1",
	[],
	"Thank you, I will leave immediately.", "close_window",
	[
		(assign, "$dark_quest_we_know", 1),
		(call_script, "script_wm_honor_change_diff", "trp_player", 5, 34),
		(store_mul, ":value", 100, 100),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
		(assign, "$wm_quest_result", 2),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_quest_menu")
	]],

	[anyone|plyr, "tavernkeeper_talk",
	[
		(eq, "$wm_quest_mission_anti_skip_menu", 1),
		(party_slot_eq, "$g_encountered_party", 15, 1)
	],
	"Please forgive me, This is a message from people with a grudge against you.", "tavernkeeper_qst_insult_tavern_master",
	[]],

	[anyone, "tavernkeeper_qst_insult_tavern_master",
	[],
	"What? What are you talking about? Oh no! Help!", "close_window",
	[
		(assign, "$wm_quest_result", 1),
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_male_p_fuck_rape")
	]],

	[trp_private_guard, "start",
	[],
	"I have nothing to say to you.", "close_window",
	[]],

	[trp_noble_man, "start",
	[
		(eq, "$player_gender", 1)
	],
	"Hmm. Acceptable body. First, suck my penis.", "woman_player_prosti_talk_1",
	[]],

	[anyone|plyr, "woman_player_prosti_talk_1",
	[],
	".........", "woman_player_prosti_talk_2",
	[
		(call_script, "script_molda_s_scene", 211, 0)
	]],

	[anyone, "woman_player_prosti_talk_2",
	[],
	" Oh...Ow!", "woman_player_prosti_talk_3",
	[]],

	[anyone|plyr, "woman_player_prosti_talk_3",
	[],
	"........ ", "woman_player_prosti_talk_4",
	[
		(call_script, "script_molda_s_scene", 211, 0)
	]],

	[anyone, "woman_player_prosti_talk_4",
	[],
	" Uhh!", "woman_player_prosti_talk_5",
	[
		(store_random_in_range, ":random_in_range_212_214", 212, 214),
		(call_script, "script_molda_s_scene", ":random_in_range_212_214", 0)
	]],

	[anyone|plyr, "woman_player_prosti_talk_5",
	[],
	"Uhh! Weird taste. Do you feel better now?", "woman_player_prosti_talk_6",
	[]],

	[anyone, "woman_player_prosti_talk_6",
	[],
	"Now shut up! Spread your legs! (hit) ", "woman_player_prosti_talk_7",
	[
		(play_sound, "snd_gbt_whip")
	]],

	[anyone|plyr, "woman_player_prosti_talk_7",
	[],
	"Ow!", "close_window",
	[
		(assign, "$wm_quest_result", 1),
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_female_p_fuck_prosti"),
		(store_random_in_range, ":random_in_range_0_100", 0, 100),
		(try_begin),
			(ge, ":random_in_range_0_100", 80),
			(call_script, "script_wm_troop_wound_disease_slot", "trp_player", 6),
		(else_try),
			(call_script, "script_wm_troop_wound_disease_slot", "trp_player", 1),
		(try_end)
	]],

	[trp_noble_man, "start",
	[
		(eq, "$player_gender", 0)
	],
	"Oh, finally! my prince charming has arrived!", "gay_noble_man_mst_talk_1",
	[]],

	[anyone|plyr, "gay_noble_man_mst_talk_1",
	[],
	"Do you want start now?", "gay_noble_man_mst_talk_2",
	[]],

	[anyone, "gay_noble_man_mst_talk_2",
	[],
	"Of course!", "close_window",
	[
		(assign, "$wm_quest_result", 1),
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_male_p_fuck_gay"),
		(store_random_in_range, ":random_in_range_0_100", 0, 100),
		(try_begin),
			(ge, ":random_in_range_0_100", 80),
			(call_script, "script_wm_troop_wound_disease_slot", "trp_player", 6),
		(else_try),
			(call_script, "script_wm_troop_wound_disease_slot", "trp_player", 1),
		(try_end)
	]],

	[anyone|plyr, "gay_noble_man_mst_talk_1",
	[],
	"I was mistaken. I'm out.", "gay_noble_man_mst_out",
	[]],

	[anyone, "gay_noble_man_mst_out",
	[],
	"Entering is your choice. However, once you have entered, you will not be allowed to leave on your own accord.", "close_window",
	[
		(assign, "$wm_quest_result", 1),
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_male_p_fuck_gay"),
		(store_random_in_range, ":random_in_range_0_100", 0, 100),
		(try_begin),
			(eq, ":random_in_range_0_100", 80),
			(call_script, "script_wm_troop_wound_disease_slot", "trp_player", 6),
		(else_try),
			(call_script, "script_wm_troop_wound_disease_slot", "trp_player", 1),
		(try_end)
	]],

	[trp_swadian_merchant, "start",
	[],
	"Nice to meet you. There are some questions, before taking up the main subject. Have you ever received a request from the scholar?", "mq_37_1",
	[]],

	[anyone|plyr, "mq_37_1",
	[],
	"If you're going to say that finding the fortress. it is yes.", "mq_37_2",
	[]],

	[anyone, "mq_37_2",
	[],
	"Have you ever met with the scholar since then?", "mq_37_3",
	[]],

	[anyone|plyr, "mq_37_3",
	[],
	"No. What happened to him?", "mq_37_4",
	[]],

	[anyone, "mq_37_4",
	[],
	"He died. and people who have received a request from that scholar also died. In my opinion, you have been caught up in something mighty dangerous.", "mq_37_5",
	[]],

	[anyone|plyr, "mq_37_5",
	[],
	"I've already been attacked by men in black clothes.", "mq_37_6",
	[]],

	[anyone, "mq_37_6",
	[],
	"If you're telling the truth, you are the first survivor. Do you have any inclination of who they might be?", "mq_37_7",
	[]],

	[anyone|plyr, "mq_37_7",
	[],
	"Nothing... Wait. if they were not disguised, they were probably muslims.", "mq_37_8",
	[]],

	[anyone, "mq_37_8",
	[],
	"It is too difficult to investigate. Either way, bee careful. There is no guarantee that they will not strike twice.", "mq_37_9",
	[]],

	[anyone|plyr, "mq_37_9",
	[],
	"I know. Good luck.", "close_window",
	[
		(assign, "$main_q_step", 38),
		(assign, "$main_q_day", 15),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return"),
		(jump_to_menu, "mnu_wm_pst_map_return")
	]],

	[trp_ex_npc_059, "start",
	[],
	"Our lord is watching over us. What are your intentions?", "pope_talk",
	[]],

	[trp_ex_npc_060, "start",
	[],
	"What are your intentions?", "pope_talk",
	[]],

	[trp_npc_18, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"I have been working as a mercenary. May i be of assistance?", "mq_30_1",
	[]],

	[anyone|plyr, "mq_30_1",
	[],
	"Yes, however that is a different problem.", "mq_30_2",
	[]],

	[anyone, "mq_30_2",
	[],
	"Different problem? if you have a grudge against me, i will say 'please forgive me'.", "mq_30_3",
	[]],

	[anyone|plyr, "mq_30_3",
	[],
	"I do not have any grudges against you. I merely want information about the horde of mountain bandits.", "mq_30_4",
	[]],

	[anyone, "mq_30_4",
	[],
	"If my guess is right, You have been chased by them. I understand. So what is your next plan?", "mq_30_5",
	[]],

	[anyone|plyr, "mq_30_5",
	[],
	"I want to destroy them all. I will not rest until there is not a single person left standing.", "mq_30_6",
	[]],

	[anyone, "mq_30_6",
	[],
	"If so, you should have a mercenary contract with me. Once the contract has been signed, i'll tell you the location of the bandits.", "mq_30_7",
	[]],

	[anyone|plyr, "mq_30_7",
	[],
	"I will do anything if you would help me.", "mq_30_8",
	[]],

	[anyone, "mq_30_8",
	[
		(assign, "$main_q_party", 0),
		(try_for_range, ":party", "p_pyongyang", "p_place_end"),
			(store_faction_of_party, ":faction_of_party_party", ":party"),
			(this_or_next|eq, ":faction_of_party_party", "$start_enemy_fac"),
			(party_slot_eq, ":party", slot_town_center, "$start_enemy_fac"),
			(try_begin),
				(eq, "$main_q_party", 0),
				(assign, "$main_q_party", ":party"),
			(else_try),
				(store_random_in_range, ":random_in_range_0_5", 0, 5),
				(eq, ":random_in_range_0_5", 0),
				(assign, "$main_q_party", ":party"),
			(try_end),
		(try_end),
		(str_store_party_name, 10, "$main_q_party")
	],
	"Good. Let's start soon. They are located in {s10}.", "close_window",
	[
		(assign, "$main_q_step", 31),
		(party_get_position, 11, "$main_q_party"),
		(map_get_land_position_around_position, 12, 11, 2),
		(assign, ":var_1", "p_ruin_dummy_5"),
		(party_set_position, ":var_1", 12),
		(party_set_icon, ":var_1", "icon_wm_town_barb_2"),
		(party_set_flags, ":var_1", 256, 0),
		(party_set_flags, ":var_1", 524288, 0),
		(party_set_flags, ":var_1", 16384, 1),
		(party_set_name, ":var_1", "str_mq_higma_fort_name"),
		(party_get_slot, ":main_q_party_town_center", "$main_q_party", slot_town_center),
		(party_set_slot, ":var_1", slot_town_center, ":main_q_party_town_center"),
		(call_script, "script_wm_comp_in_party_slot", "trp_npc_18")
	]],

	[trp_tt_lady_ex_01, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(party_slot_ge, "p_main_party", 28, 30000)
	],
	"Thank you for coming. my name is Gyewolhyang. Take a drink.", "ex_lady_01_join_1",
	[]],

	[trp_tt_lady_ex_01, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.) (need money 30000)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_01_join_1",
	[],
	"So... Let's take a drink.", "ex_lady_01_join_2",
	[]],

	[anyone|plyr, "ex_lady_01_join_1",
	[],
	"I don't like alcohol.", "close_window",
	[]],

	[anyone, "ex_lady_01_join_2",
	[],
	"(Cup filled with liquor. Time is running out. Had many conversations.)", "ex_lady_01_join_3",
	[]],

	[anyone, "ex_lady_01_join_3",
	[],
	"I'm sick of living here now. I feel trapped in a cage. It would be nice if someone would just take me away.", "ex_lady_01_join_4",
	[]],

	[anyone, "ex_lady_01_join_4",
	[],
	"Sounds silly, huh? Drink.", "ex_lady_01_join_5",
	[]],

	[anyone|plyr, "ex_lady_01_join_5",
	[],
	"(You grabbed her hand and stopped her.)", "ex_lady_01_join_6",
	[]],

	[anyone|plyr, "ex_lady_01_join_5",
	[],
	"(Pay for the drinks and leave.)", "close_window",
	[]],

	[anyone, "ex_lady_01_join_6",
	[],
	"'What are you doing?' (She said, as she pulls you along by your hand.)", "ex_lady_01_join_7",
	[]],

	[anyone, "ex_lady_01_join_7",
	[],
	"'Somebody help me! This guy is abducting me!' (She beckons from the door.)", "ex_lady_01_join_8",
	[]],

	[anyone|plyr, "ex_lady_01_join_8",
	[],
	"I may have exaggerated a little. Anyway, lets go.", "ex_lady_01_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_01_join_9",
	[],
	"Yay! Quickly.", "close_window",
	[]],

	[trp_tt_lady_ex_02, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(neg|troop_slot_ge, "trp_player", 13, -25)
	],
	"Hi! You seem to be the traveling sort.", "ex_lady_02_join_1",
	[]],

	[trp_tt_lady_ex_02, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.) (need honor -26)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_02_join_1",
	[],
	"That is right. Mercenaries, adventurers, merchants, whatever.", "ex_lady_02_join_2",
	[]],

	[anyone|plyr, "ex_lady_02_join_1",
	[],
	"What does it matter to you?", "close_window",
	[]],

	[anyone, "ex_lady_02_join_2",
	[],
	"Mercenary, I need a crew.", "ex_lady_02_join_3",
	[]],

	[anyone, "ex_lady_02_join_3",
	[],
	"I was a pirate. I was attacked by 'Red Beard' And lost everything.", "ex_lady_02_join_4",
	[]],

	[anyone, "ex_lady_02_join_4",
	[],
	"But I will rebuild. My skills have not rusted.", "ex_lady_02_join_5",
	[]],

	[anyone|plyr, "ex_lady_02_join_5",
	[],
	"It would be all that's needed to stop the pirates. You can be my first mate.", "ex_lady_02_join_6",
	[]],

	[anyone|plyr, "ex_lady_02_join_5",
	[],
	"I'm out.", "close_window",
	[]],

	[anyone, "ex_lady_02_join_6",
	[],
	"I did not retire. But right now i can't be a pirate.", "ex_lady_02_join_7",
	[]],

	[anyone, "ex_lady_02_join_7",
	[],
	"As you said, i might suit the position of first mate.", "ex_lady_02_join_8",
	[]],

	[anyone|plyr, "ex_lady_02_join_8",
	[],
	"Welcome, first mate.", "ex_lady_02_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_02_join_9",
	[],
	"Oh, yes. Well let's get going!", "close_window",
	[]],

	[trp_tt_lady_ex_03, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(troop_slot_ge, "trp_player", 13, 0)
	],
	"If you have something to say, Speak briefly. What do you want?", "ex_lady_03_join_1",
	[]],

	[trp_tt_lady_ex_03, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.)  (need honor 0)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_03_join_1",
	[],
	"There is nothing to say. Is there something bothering you?", "ex_lady_03_join_2",
	[]],

	[anyone|plyr, "ex_lady_03_join_1",
	[],
	"Nothing", "close_window",
	[]],

	[anyone, "ex_lady_03_join_2",
	[],
	"There are... a lot of things. ", "ex_lady_03_join_3",
	[]],

	[anyone, "ex_lady_03_join_3",
	[],
	"I am a fencing instructor. However, it was not meant to be. An accident occurred during training. An apprentice was killed while practicing with a trainee.", "ex_lady_03_join_4",
	[]],

	[anyone, "ex_lady_03_join_4",
	[],
	"I will never be able to go back.", "ex_lady_03_join_5",
	[]],

	[anyone|plyr, "ex_lady_03_join_5",
	[],
	"I need an instructor. Perhaps you could train my soldiers?", "ex_lady_03_join_6",
	[]],

	[anyone|plyr, "ex_lady_03_join_5",
	[],
	"It is a shame. But there is no time.", "close_window",
	[]],

	[anyone, "ex_lady_03_join_6",
	[],
	"I would be delighted to accept your offer.", "ex_lady_03_join_7",
	[]],

	[anyone, "ex_lady_03_join_7",
	[],
	"However, don't get any funny ideas. I am an instructor only.", "ex_lady_03_join_8",
	[]],

	[anyone|plyr, "ex_lady_03_join_8",
	[],
	"Sure. Welcome to the party. Instructor.", "ex_lady_03_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_03_join_9",
	[],
	"Thank you.", "close_window",
	[]],

	[trp_tt_lady_ex_04, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(neq, "$wm_player_fac", "fac_kingdom_35"),
		(troop_slot_ge, "trp_player", 13, 25)
	],
	"Nice to meet you. Could you please help me?", "ex_lady_04_join_1",
	[]],

	[trp_tt_lady_ex_04, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.) (need honor 25)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_04_join_1",
	[],
	"Help?, What are you saying?", "ex_lady_04_join_2",
	[]],

	[anyone|plyr, "ex_lady_04_join_1",
	[],
	"Sorry.", "close_window",
	[]],

	[anyone, "ex_lady_04_join_2",
	[],
	"Before you ask, I should introduce myself. My name is Diao chan. Adopted daughter of Minister Wang Yun.", "ex_lady_04_join_3",
	[]],

	[anyone, "ex_lady_04_join_3",
	[],
	"At the request of my father, i infiltraded Dong Zhuo's palace and seduced both him and his step-son Lu bu. I then convinced Lu Bu to assassinate Dong Zhuo and take the reins of his power, but Dong Zhuo's followers did not accept this. They are searching for me as we speak...", "ex_lady_04_join_4",
	[]],

	[anyone, "ex_lady_04_join_4",
	[],
	"They have cornered me here. I have nowhere left to run.", "ex_lady_04_join_5",
	[]],

	[anyone|plyr, "ex_lady_04_join_5",
	[],
	"We will protect you.", "ex_lady_04_join_6",
	[]],

	[anyone|plyr, "ex_lady_04_join_5",
	[],
	"My apologies, this is out of my depth. Best of luck to you.", "close_window",
	[]],

	[anyone, "ex_lady_04_join_6",
	[],
	"If you could save my life, I will do anything to repay your kindness.", "ex_lady_04_join_7",
	[]],

	[anyone, "ex_lady_04_join_7",
	[],
	"This is my only request.", "ex_lady_04_join_8",
	[]],

	[anyone|plyr, "ex_lady_04_join_8",
	[],
	"All right, you are hereby under my protection. My men and i will do our utmost to protect you.", "ex_lady_04_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop"),
		(call_script, "script_change_player_relation_with_troop", "trp_tt_lord_35_00", -50),
		(call_script, "script_change_player_relation_with_troop", "trp_tt_lord_35_00", -50),
		(call_script, "script_change_player_relation_with_troop", "trp_tt_lord_35_00", -50)
	]],

	[anyone, "ex_lady_04_join_9",
	[],
	"Thank you. Now let us hurry away before they arrive.", "close_window",
	[]],

	[trp_tt_lady_ex_05, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"Outsider! Are you just leaving?", "ex_lady_05_join_1",
	[]],

	[trp_tt_lady_ex_05, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_05_join_1",
	[],
	"What is the matter?", "ex_lady_05_join_2",
	[]],

	[anyone|plyr, "ex_lady_05_join_1",
	[],
	"I can't say.", "close_window",
	[]],

	[anyone, "ex_lady_05_join_2",
	[],
	"May i travel with you? I have little time, i will need an answer immediately.", "ex_lady_05_join_3",
	[]],

	[anyone, "ex_lady_05_join_3",
	[],
	"I want to escape this place immediately, before my parents discover my absence. My parents are the rulers of the Nanman tribes.", "ex_lady_05_join_4",
	[]],

	[anyone, "ex_lady_05_join_4",
	[],
	"I can fight as well as any man. We Nanman are warriors. ", "ex_lady_05_join_5",
	[]],

	[anyone|plyr, "ex_lady_05_join_5",
	[],
	"You'll have to prove your words. You're welcome to travel with us.", "ex_lady_05_join_6",
	[]],

	[anyone|plyr, "ex_lady_05_join_5",
	[],
	"You should stay at home.", "close_window",
	[]],

	[anyone, "ex_lady_05_join_6",
	[],
	"I won't let you down! I'll just need a moment to collect my belongings.", "ex_lady_05_join_7",
	[]],

	[anyone, "ex_lady_05_join_7",
	[],
	"(After a while) All done. Lets get out of here.", "ex_lady_05_join_8",
	[]],

	[anyone|plyr, "ex_lady_05_join_8",
	[],
	"After you.", "ex_lady_05_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_05_join_9",
	[],
	"I finally did it!", "close_window",
	[]],

	[trp_tt_lady_ex_06, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"Do you recruit soldiers?", "ex_lady_06_join_1",
	[]],

	[trp_tt_lady_ex_06, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_06_join_1",
	[],
	"Yes. Are you a mercenary? Do you know how to fight?", "ex_lady_06_join_2",
	[]],

	[anyone|plyr, "ex_lady_06_join_1",
	[],
	"No. My apologies.", "close_window",
	[]],

	[anyone, "ex_lady_06_join_2",
	[],
	"Do i know how to fight? I knew you wouldn't believe me. Most people dont.", "ex_lady_06_join_3",
	[]],

	[anyone, "ex_lady_06_join_3",
	[],
	"I am a shieldmaiden. People always say 'women are no good for fighting.' I am proof of their ignorance.", "ex_lady_06_join_4",
	[]],

	[anyone, "ex_lady_06_join_4",
	[],
	"So what do you think? Will you let me prove my words?", "ex_lady_06_join_5",
	[]],

	[anyone|plyr, "ex_lady_06_join_5",
	[],
	"There is no prejudice here, my lady. If it is fighting you want, you are most welcome to join us.", "ex_lady_06_join_6",
	[]],

	[anyone|plyr, "ex_lady_06_join_5",
	[],
	"Go home and stay there, where you belong.", "close_window",
	[]],

	[anyone, "ex_lady_06_join_6",
	[],
	"Fine.", "ex_lady_06_join_7",
	[]],

	[anyone, "ex_lady_06_join_7",
	[],
	"You'll see what i can do on the battlefield.", "ex_lady_06_join_8",
	[]],

	[anyone|plyr, "ex_lady_06_join_8",
	[],
	"Sure. Welcome aboard.", "ex_lady_06_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_06_join_9",
	[],
	"Thank you. I'm ready to leave when you are.", "close_window",
	[]],

	[trp_tt_lady_ex_07, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(troop_slot_ge, "trp_player", 13, 50)
	],
	"('An armor-clad woman is looking at you.)", "ex_lady_07_join_1",
	[]],

	[trp_tt_lady_ex_07, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.) (need honor 50)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_07_join_1",
	[],
	"(Speaks) Is there something i may help you with?", "ex_lady_07_join_2",
	[]],

	[anyone|plyr, "ex_lady_07_join_1",
	[],
	"(Quit)", "close_window",
	[]],

	[anyone, "ex_lady_07_join_2",
	[],
	"What kind of party do you lead? What is it you do?", "ex_lady_07_join_3",
	[]],

	[anyone, "ex_lady_07_join_3",
	[],
	"(The woman observes you) I seem to be mistaken. My apologies.", "ex_lady_07_join_4",
	[]],

	[anyone, "ex_lady_07_join_4",
	[],
	"I am being pursued. Your soldiers make me uneasy.", "ex_lady_07_join_5",
	[]],

	[anyone|plyr, "ex_lady_07_join_5",
	[],
	"I see that you are armed. If you are willing to fight with us, you may leave with us.", "ex_lady_07_join_6",
	[]],

	[anyone|plyr, "ex_lady_07_join_5",
	[],
	"I do not want to know. Best of luck to you.", "close_window",
	[]],

	[anyone, "ex_lady_07_join_6",
	[],
	"Really? We've just met, are you sure you will trust me just like that?", "ex_lady_07_join_7",
	[]],

	[anyone, "ex_lady_07_join_7",
	[],
	"Well you do not seem to be one of my pursuers. Either way i've no choice - i'll be in your care.", "ex_lady_07_join_8",
	[]],

	[anyone|plyr, "ex_lady_07_join_8",
	[],
	"Don't you worry. If your pursuers show up, they will have to go through us. But for now, let's get out of here - no point searching for trouble if we can avoid it.", "ex_lady_07_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_07_join_9",
	[],
	"Thank you.", "close_window",
	[]],

	[trp_tt_lady_ex_08, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(Scream) Help me! Help me! (A girl is being assaulted by a ruffian.)", "ex_lady_08_join_1",
	[]],

	[trp_tt_lady_ex_08, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_08_join_1",
	[],
	"(Attack)", "ex_lady_08_join_2",
	[]],

	[anyone|plyr, "ex_lady_08_join_1",
	[],
	"(Exit)", "close_window",
	[]],

	[anyone, "ex_lady_08_join_2",
	[],
	"(You knocked the drunkards out with ease.)", "ex_lady_08_join_3",
	[]],

	[anyone, "ex_lady_08_join_3",
	[],
	"Thank you. They are Juan Ferrero's men.", "ex_lady_08_join_4",
	[]],

	[anyone, "ex_lady_08_join_4",
	[],
	"This is not the first time they've attacked me. I need to find a way out of town before they lose their patience...", "ex_lady_08_join_5",
	[]],

	[anyone|plyr, "ex_lady_08_join_5",
	[],
	"Perhaps i may be of assistance. If you are willing to work for pay, you'd be welcome to travel with my army.", "ex_lady_08_join_6",
	[]],

	[anyone|plyr, "ex_lady_08_join_5",
	[],
	"It's a shame, but i have to leave. Good luck.", "close_window",
	[]],

	[anyone, "ex_lady_08_join_6",
	[],
	"Really? That is a most tempting offer.", "ex_lady_08_join_7",
	[]],

	[anyone, "ex_lady_08_join_7",
	[],
	"I'm not sure how i can be of assistance, but i will do my best.", "ex_lady_08_join_8",
	[]],

	[anyone|plyr, "ex_lady_08_join_8",
	[],
	"That's the spirit. Welcome.", "ex_lady_08_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_08_join_9",
	[],
	"I'll be outside in a minute.", "close_window",
	[]],

	[trp_tt_lady_ex_09, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"Greetings. My apologies, but i do not have time for a chat.", "ex_lady_09_join_1",
	[]],

	[trp_tt_lady_ex_09, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_09_join_1",
	[],
	"What's the matter? Perhaps i can help.", "ex_lady_09_join_2",
	[]],

	[anyone|plyr, "ex_lady_09_join_1",
	[],
	"(Exit)", "close_window",
	[]],

	[anyone, "ex_lady_09_join_2",
	[],
	"What nerve you've got!", "ex_lady_09_join_3",
	[]],

	[anyone, "ex_lady_09_join_3",
	[],
	"Have you ever heard the name Ali baba? I was his servant, Kahra mana.", "ex_lady_09_join_4",
	[]],

	[anyone, "ex_lady_09_join_4",
	[],
	"I have my freedom now. As i needed a bit of money, i went to the sesame cave. But it had been emptied! ", "ex_lady_09_join_5",
	[]],

	[anyone|plyr, "ex_lady_09_join_5",
	[],
	"Let us work together. We strive to make money!", "ex_lady_09_join_6",
	[]],

	[anyone|plyr, "ex_lady_09_join_5",
	[],
	"Right... I just remembered i have something urgent to do...", "close_window",
	[]],

	[anyone, "ex_lady_09_join_6",
	[],
	"Really now? A most welcome offer. I accept.", "ex_lady_09_join_7",
	[]],

	[anyone, "ex_lady_09_join_7",
	[],
	"I can fight. Perhaps some other things as well...", "ex_lady_09_join_8",
	[]],

	[anyone|plyr, "ex_lady_09_join_8",
	[],
	"Good. Welcome.", "ex_lady_09_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_09_join_9",
	[],
	"Thank you.", "close_window",
	[]],

	[trp_tt_lady_ex_10, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"Do you know shahrzad?", "ex_lady_10_join_1",
	[]],

	[trp_tt_lady_ex_10, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_10_join_1",
	[],
	"Shahrzad? Sorry, no.", "ex_lady_10_join_2",
	[]],

	[anyone|plyr, "ex_lady_10_join_1",
	[],
	"(Exit)", "close_window",
	[]],

	[anyone, "ex_lady_10_join_2",
	[],
	"It's pointless. I am tired of this, my sister can stay gone for all i care.", "ex_lady_10_join_3",
	[]],

	[anyone, "ex_lady_10_join_3",
	[],
	"Perhaps she'll be fine on her own.", "ex_lady_10_join_4",
	[]],

	[anyone, "ex_lady_10_join_4",
	[],
	"Or not. I do not care. So, what are you then?", "ex_lady_10_join_5",
	[]],

	[anyone|plyr, "ex_lady_10_join_5",
	[],
	"Warriors. Travelers, among other things... Perhaps we can help you look for your sister.", "ex_lady_10_join_6",
	[]],

	[anyone|plyr, "ex_lady_10_join_5",
	[],
	"I despise chatty women. Goodbye.", "close_window",
	[]],

	[anyone, "ex_lady_10_join_6",
	[],
	"I told you, i no longer care about her. Trying to find her is pointless.", "ex_lady_10_join_7",
	[]],

	[anyone, "ex_lady_10_join_7",
	[],
	"I do like the sound of that word, though... Travel. Whatever, as long as it doesnt involve looking for that lunatic.", "ex_lady_10_join_8",
	[]],

	[anyone|plyr, "ex_lady_10_join_8",
	[],
	"Good. Welcome.", "ex_lady_10_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_10_join_9",
	[],
	"Ugh, i can't wait to get away from this dreadful place.", "close_window",
	[]],

	[trp_tt_lady_ex_11, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"You there, traveler. Greetings. I want to leave the town immediately, and that would be simpler if i had a companion.", "ex_lady_11_join_1",
	[]],

	[trp_tt_lady_ex_11, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_11_join_1",
	[],
	"What's the urgency?", "ex_lady_11_join_2",
	[]],

	[anyone|plyr, "ex_lady_11_join_1",
	[],
	"(Ignore)", "close_window",
	[]],

	[anyone, "ex_lady_11_join_2",
	[],
	"My parents have sold me out! They've agreed to an arranged marriage.", "ex_lady_11_join_3",
	[]],

	[anyone, "ex_lady_11_join_3",
	[],
	"The suitor is part of the royal family. I just want to live an ordinary life, and last night i had terribly bad dreams.", "ex_lady_11_join_4",
	[]],

	[anyone, "ex_lady_11_join_4",
	[],
	"In my dreams, the country is invaded. The city is put to the torch and the invaders violate me. If i were to marry into the royal family, this is ever more likely to be my fate.", "ex_lady_11_join_5",
	[]],

	[anyone|plyr, "ex_lady_11_join_5",
	[],
	"Then come with us. We will take you far from here, and keep you safe.", "ex_lady_11_join_6",
	[]],

	[anyone|plyr, "ex_lady_11_join_5",
	[],
	"Who could possibly defeat the monarchy? This is the royal family, girl. You'll be a princess! Think of how pleasant life will be! Go now - It will certainly be a lot better than you imagine.", "close_window",
	[]],

	[anyone, "ex_lady_11_join_6",
	[],
	"Will you really? Oh, i don't know how to express my gratitude!", "ex_lady_11_join_7",
	[]],

	[anyone, "ex_lady_11_join_7",
	[],
	"I can cook. Perhaps a few other things, too.", "ex_lady_11_join_8",
	[]],

	[anyone|plyr, "ex_lady_11_join_8",
	[],
	"That's good enough. Let us be off before your family starts looking for you.", "ex_lady_11_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_11_join_9",
	[],
	"Thank you so much!", "close_window",
	[]],

	[trp_tt_lady_ex_12, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"Wait! A word, please! Hear me out!", "ex_lady_12_join_1",
	[]],

	[anyone|plyr, "ex_lady_12_join_1",
	[],
	"You want to talk? There's no need for words. Die!", "ex_lady_12_join_2",
	[]],

	[anyone, "ex_lady_12_join_2",
	[],
	"No! Stop! Please!", "ex_lady_12_join_3",
	[]],

	[anyone, "ex_lady_12_join_3",
	[],
	"I have failed the assassination i was ordered to. I am no longer in my organization.", "ex_lady_12_join_4",
	[]],

	[anyone, "ex_lady_12_join_4",
	[],
	"What this means is i am for hire, i suppose. I can work for you. Please.", "ex_lady_12_join_5",
	[]],

	[anyone|plyr, "ex_lady_12_join_5",
	[],
	"All right. I will grant you a second chance. But this is the only time. Remember that.", "ex_lady_12_join_6",
	[]],

	[anyone|plyr, "ex_lady_12_join_5",
	[],
	"A turncoat? Despicable. I'll let you leave with your life.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(change_screen_return)
	]],

	[anyone, "ex_lady_12_join_6",
	[],
	"Thank you, thank you! My blade belongs to you, and you only. I stake my life on this vow.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop"),
		(change_screen_return)
	]],

	[trp_tt_lady_ex_13, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(neq, "$wm_player_fac", "fac_kingdom_63"),
		(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
		(gt, ":party_size_wo_prisoners_main_party", 8000)
	],
	"You. Do you lead a company of mercenaries?", "ex_lady_13_join_1",
	[]],

	[trp_tt_lady_ex_13, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.) (need an army of 8000, and not of the Mori faction.)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_13_join_1",
	[],
	"Perhaps i do, if the purpose is right. Why do you require one?", "ex_lady_13_join_2",
	[]],

	[anyone|plyr, "ex_lady_13_join_1",
	[],
	"(Ignore)", "close_window",
	[]],

	[anyone, "ex_lady_13_join_2",
	[],
	"I am the last daughter of the Minura family. The Mori clan invaded our lands and wiped us off the map. Only i remain.", "ex_lady_13_join_3",
	[]],

	[anyone, "ex_lady_13_join_3",
	[],
	"I want vengeance. But i have no men to my name.", "ex_lady_13_join_4",
	[]],

	[anyone, "ex_lady_13_join_4",
	[],
	"In return for your aid, i am willing to do anything to repay you.", "ex_lady_13_join_5",
	[]],

	[anyone|plyr, "ex_lady_13_join_5",
	[],
	"If you are willing to cast aside your pride as a noble and live as one of us, your vengeance might be arranged.", "ex_lady_13_join_5_1",
	[]],

	[anyone|plyr, "ex_lady_13_join_5",
	[],
	"Go to war with a clan for the sake of one person's revenge? Your family is gone, girl. But you are not. Honor your family by making your survival matter.", "close_window",
	[]],

	[anyone, "ex_lady_13_join_5_1",
	[],
	"For the sake of revenge, i will do anything.", "ex_lady_13_join_5_2",
	[]],

	[anyone|plyr, "ex_lady_13_join_5_2",
	[],
	"Revenge seems rooted in your heart. A shame for someone so beautiful.", "ex_lady_13_join_5_3",
	[]],

	[anyone, "ex_lady_13_join_5_3",
	[],
	"My beauty and my life seeped away with the blood of my family. My only remaining desire is for revenge. Only with the last breath of the Mori will my heritage know peace. Only then can i rest, and mourn.", "ex_lady_13_join_6",
	[]],

	[anyone|plyr, "ex_lady_13_join_6",
	[],
	"You have suffered great injustice. Your words resonate within me, and your fury is ours. You have your army. It's time for the Mori to face their reckoning.", "ex_lady_13_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_13_join_9",
	[],
	"(She nearly smiles.) At last...", "close_window",
	[]],

	[trp_tt_lady_ex_14, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(neg|troop_slot_ge, "trp_player", 13, -25)
	],
	"Oh! My horse, it won't listen to me!", "ex_lady_14_join_1",
	[]],

	[trp_tt_lady_ex_14, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.) (need honor -26)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_14_join_1",
	[],
	"(Calm the horse)", "ex_lady_14_join_2",
	[]],

	[anyone|plyr, "ex_lady_14_join_1",
	[],
	"(Ignore)", "close_window",
	[]],

	[anyone, "ex_lady_14_join_2",
	[],
	"Oh, thank you. If you had not shown up, i might have been in peril.", "ex_lady_14_join_3",
	[]],

	[anyone, "ex_lady_14_join_3",
	[],
	"I am fleeing the war. My fiancée warned me by letter not to return home... They want my life. They are searching for me, even now.'", "ex_lady_14_join_4",
	[]],

	[anyone, "ex_lady_14_join_4",
	[],
	"I am getting ready to run, but i don't know where to go... I have never before left our estate on my own", "ex_lady_14_join_5",
	[]],

	[anyone|plyr, "ex_lady_14_join_5",
	[],
	"You may travel with us, my lady. We will keep you safe.", "ex_lady_14_join_6",
	[]],

	[anyone|plyr, "ex_lady_14_join_5",
	[],
	"How unfortunate for you. I wish you the best of luck, and i'll mislead your pursuers, should they ask for you.", "close_window",
	[]],

	[anyone, "ex_lady_14_join_6",
	[],
	"Can i, really? Oh, thank you so much!", "ex_lady_14_join_7",
	[]],

	[anyone, "ex_lady_14_join_7",
	[],
	"This is my first time leaving my homelands. I will need to prepare a few things.", "ex_lady_14_join_8",
	[]],

	[anyone|plyr, "ex_lady_14_join_8",
	[],
	"That will do, but we will have to leave soon. Dont take too long.", "ex_lady_14_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_14_join_9",
	[],
	"I will only bring the necessities. Thank you so much.", "close_window",
	[]],

	[trp_tt_lady_ex_15, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(party_slot_ge, "p_main_party", 28, 30000)
	],
	"Oh sir. What do you want.", "ex_lady_15_join_1",   # Please spare me having to do this one.
	[]],

	[trp_tt_lady_ex_15, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.) (need money 30000)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_15_join_1",
	[],
	"First, blow job.", "ex_lady_15_join_2",
	[]],

	[anyone|plyr, "ex_lady_15_join_1",
	[],
	"(Exit)", "close_window",
	[]],

	[anyone, "ex_lady_15_join_2",
	[],
	"Everyone likes this way.", "ex_lady_15_join_3",
	[
		(call_script, "script_molda_s_scene", 111, 0)
	]],

	[anyone, "ex_lady_15_join_3",
	[],
	"Your sperm is sweet. Erection of you was over. We could talk for a while.", "ex_lady_15_join_4",
	[
		(call_script, "script_molda_s_scene", 113, 0)
	]],

	[anyone, "ex_lady_15_join_4",
	[],
	"Last night, I had dreams of being the wife of the king. Funny story. isn't it?", "ex_lady_15_join_5",
	[]],

	[anyone|plyr, "ex_lady_15_join_5",
	[],
	"I might be the king. Come with me. Perhaps your dreams may come true.", "ex_lady_15_join_6",
	[]],

	[anyone|plyr, "ex_lady_15_join_5",
	[],
	"I would just fall asleep.", "close_window",
	[]],

	[anyone, "ex_lady_15_join_6",
	[],
	"Funny joke. but i go with you.", "ex_lady_15_join_7",
	[]],

	[anyone, "ex_lady_15_join_7",
	[],
	"It will be fun to follow you. more than life here.", "ex_lady_15_join_8",
	[]],

	[anyone|plyr, "ex_lady_15_join_8",
	[],
	"Good. Let's enjoy our time.", "ex_lady_15_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_15_join_9",
	[],
	"Haha.", "close_window",
	[]],

	[trp_tt_lady_ex_16, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(troop_slot_ge, "trp_player", 13, 25),
		(party_slot_ge, "p_main_party", 28, 30000)
	],
	"Townie. Why did you come here?", "ex_lady_16_join_1",
	[]],

	[trp_tt_lady_ex_16, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.) (need money 30000, honor 25)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_16_join_1",
	[],
	"I am a traveler. I go wherever my heart leads me.", "ex_lady_16_join_2",
	[]],

	[anyone|plyr, "ex_lady_16_join_1",
	[],
	"(Ignore)", "close_window",
	[]],

	[anyone, "ex_lady_16_join_2",
	[],
	"Oh, i wish i could be like you...", "ex_lady_16_join_3",
	[]],

	[anyone, "ex_lady_16_join_3",
	[],
	"I have lived here all my life, never seeing the outside world.", "ex_lady_16_join_4",
	[]],

	[anyone, "ex_lady_16_join_4",
	[],
	"But i've heard tales from travelers passing through, and dreamt of seeing it some day.", "ex_lady_16_join_5",
	[]],

	[anyone|plyr, "ex_lady_16_join_5",
	[],
	"Come with us. I can show you the world.", "ex_lady_16_join_6",
	[]],

	[anyone|plyr, "ex_lady_16_join_5",
	[],
	"The world is not only wonders and fairy tales. It can be a cruel and ugly place. You're better off staying here.", "close_window",
	[]],

	[anyone, "ex_lady_16_join_6",
	[],
	"Oh, but i can't. This is so sudden...", "ex_lady_16_join_7",
	[]],

	[anyone, "ex_lady_16_join_7",
	[],
	"No. I always keep putting it off. I may never get another opportunity like this. I would love to come with you!", "ex_lady_16_join_8",
	[]],

	[anyone|plyr, "ex_lady_16_join_8",
	[],
	"Glad to hear it. In that case, go pack your belongings. We'll be leaving very soon.", "ex_lady_16_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_16_join_9",
	[],
	"Never look back. That is what i'll tell myself from now on.", "close_window",
	[]],

	[trp_tt_lady_ex_17, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"Excuse me, I have a favor to ask.", "ex_lady_17_join_1",
	[]],

	[trp_tt_lady_ex_17, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_17_join_1",
	[],
	"Let's hear it.", "ex_lady_17_join_2",
	[]],

	[anyone|plyr, "ex_lady_17_join_1",
	[],
	"(Ignore)", "close_window",
	[]],

	[anyone, "ex_lady_17_join_2",
	[],
	"A few days ago my brother passed away.", "ex_lady_17_join_3",
	[]],

	[anyone, "ex_lady_17_join_3",
	[],
	"He was murdered. Someone who was visited him, an outsider, killed him in his home.", "ex_lady_17_join_4",
	[]],

	[anyone, "ex_lady_17_join_4",
	[],
	"They have already left. I need to chase them, find them, and kill them.", "ex_lady_17_join_5",
	[]],

	[anyone|plyr, "ex_lady_17_join_5",
	[],
	"I cannot promise anything, but if you come with us we may look for them in our travels.", "ex_lady_17_join_6",
	[]],

	[anyone|plyr, "ex_lady_17_join_5",
	[],
	"Then i wish you luck in your quest for vengeance. Now if you'll excuse me...", "close_window",
	[]],

	[anyone, "ex_lady_17_join_6",
	[],
	"Thank you. These weren't just anybody - it will be a challenge to track them down.", "ex_lady_17_join_7",
	[]],

	[anyone, "ex_lady_17_join_7",
	[],
	"That does not mean i'll give up. However long it takes, i'll find them.", "ex_lady_17_join_8",
	[]],

	[anyone|plyr, "ex_lady_17_join_8",
	[],
	"I hear you've set your resolve. Good. Then let us be off.", "ex_lady_17_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_17_join_9",
	[],
	"I have no reason to stay here anymore. Let's go.", "close_window",
	[]],

	[trp_tt_lady_ex_18, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(party_slot_ge, "p_main_party", 28, 30000)
	],
	"Nice to meet you. Sir. Is there anything you need?", "ex_lady_18_join_1",   # Please spare me having to do this one.
	[]],

	[trp_tt_lady_ex_18, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(She ignores you.) (need money 30000)", "close_window",
	[]],

	[anyone|plyr, "ex_lady_18_join_1",
	[],
	"Your body. Your hole.", "ex_lady_18_join_2",
	[]],

	[anyone|plyr, "ex_lady_18_join_1",
	[],
	"(Exit)", "close_window",
	[]],

	[anyone, "ex_lady_18_join_2",
	[],
	"Right, First enjoy my 'top hole'", "ex_lady_18_join_3",
	[
		(call_script, "script_molda_s_scene", 111, 0)
	]],

	[anyone, "ex_lady_18_join_3",
	[],
	"Oh, so many.", "ex_lady_18_join_4",
	[
		(call_script, "script_molda_s_scene", 112, 0)
	]],

	[anyone, "ex_lady_18_join_4",
	[],
	"Sir, do you need a dedicated prostitute, is not it? In fact, this place too harsh to me. so i wants to leave.", "ex_lady_18_join_5",
	[]],

	[anyone|plyr, "ex_lady_18_join_5",
	[],
	"If you can suck my dick for every day, may we go together.", "ex_lady_18_join_6",
	[]],

	[anyone|plyr, "ex_lady_18_join_5",
	[],
	"Heard everything. Bye.", "close_window",
	[]],

	[anyone, "ex_lady_18_join_6",
	[],
	"You liked my blow job, is it?", "ex_lady_18_join_7",
	[]],

	[anyone, "ex_lady_18_join_7",
	[],
	"I'll always suck. Promise.", "ex_lady_18_join_8",
	[]],

	[anyone|plyr, "ex_lady_18_join_8",
	[],
	"Fine. I'm appoint you as managers of my dick.", "ex_lady_18_join_9",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_18_join_9",
	[],
	"Haha.", "close_window",
	[]],

	[anyone|plyr, "ex_lady_rejoin",
	[],
	"Please rejoin us.", "ex_lady_rejoin_2",
	[]],

	[anyone, "ex_lady_rejoin_2",
	[
		(ge, "$g_talk_troop_relation", -15)
	],
	"I was hoping you would ask. Give me some time to collect my belongings.", "close_window",
	[
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "ex_lady_rejoin_2",
	[],
	"Now why would i want to do that? I left for a reason. Goodbye.", "close_window",
	[]],

	[anyone|plyr, "ex_lady_rejoin",
	[],
	"Nice to see you're well, now i'll be off.", "close_window",
	[]],

	[trp_npc1, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(troop_slot_ge, "trp_player", 13, 15)
	],
	"I am a seagull, circling the harbor...", "npc1_join_1",
	[]],

	[trp_npc1, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.) (honor 15)", "close_window",
	[]],

	[anyone|plyr, "npc1_join_1",
	[],
	"A seagull? What do you do?", "npc1_join_2",
	[]],

	[anyone|plyr, "npc1_join_1",
	[],
	"What are you saying, you blubbering drunkard? Go drool somewhere else.", "close_window",
	[]],

	[anyone, "npc1_join_2",
	[],
	"I am... I was a first mate. I recently split off from my crew.", "npc1_join_3",
	[]],

	[anyone, "npc1_join_3",
	[],
	"The admiral of our fleet was a man called Joan Ferrero. Joan Ferrero is a military commander as well as an adventurer.", "npc1_join_4",
	[]],

	[anyone, "npc1_join_4",
	[],
	"They decided to cast off the yoke of law. Piracy. I did not agree with robbing innocent men, so i bailed.", "npc1_join_5",
	[]],

	[anyone|plyr, "npc1_join_5",
	[],
	"How unusual. As it is, i lead a crew and hold a ship to my name. A ship lacking a first mate.", "npc1_join_6",
	[]],

	[anyone|plyr, "npc1_join_5",
	[],
	"That happens from time to time. Good luck finding employment.", "close_window",
	[]],

	[anyone, "npc1_join_6",
	[],
	"Really? As luck would have it, i am in dire need of a new job.", "npc1_join_7",
	[]],

	[anyone, "npc1_join_7",
	[],
	"I can assist you and your men with maneuvering the ship. With my help, you'll travel much faster, much safer. What do you say, captain?", "npc1_join_8",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc1_join_8",
	[],
	"Then welcome aboard, first mate.", "close_window",
	[]],

	[anyone|plyr, "npc1_join_8",
	[],
	"I'm afraid i can't afford that at the moment. I wish you good luck.", "close_window",
	[]],

	[trp_npc2, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(troop_slot_ge, "trp_player", 13, 25),
		(party_slot_ge, "p_main_party", 28, 16000)
	],
	"Give me your money. Let's work this out the easy way.", "npc2_join_1",  
	[]],

	[trp_npc2, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.) (honor 25) (money 16000)", "close_window",
	[]],

	[anyone|plyr, "npc2_join_1",
	[],
	"Cut yoff your dick and i'll give you the money. How's that?", "npc2_join_2",
	[]],

	[anyone|plyr, "npc2_join_1",
	[],
	"(Escaping)", "close_window",
	[]],

	[anyone, "npc2_join_2",
	[],
	"Well that'd be a fascinating proposal if i could live on without it. Today's business is a bust...", "npc2_join_3",
	[]],

	[anyone, "npc2_join_3",
	[],
	"My colleagues are in jail. I need a lot of money to bail them out.", "npc2_join_4",
	[]],

	[anyone, "npc2_join_4",
	[],
	"I've only one man left, so it seems an impossible achievment.", "npc2_join_5",
	[]],

	[anyone|plyr, "npc2_join_5",
	[],
	"I might be able to help you, should you contribute anything useful in return.", "npc2_join_6",
	[]],

	[anyone|plyr, "npc2_join_5",
	[],
	"And now you'll be joining your mates in prison.", "close_window",
	[]],

	[anyone, "npc2_join_6",
	[],
	"You spend big, and i'll fight for you. Without making myself a eunuch!", "npc2_join_7",
	[]],

	[anyone, "npc2_join_7",
	[
		(assign, reg3, 15000)
	],
	"I'll need {reg3} denars to pay the bail for my friends.", "npc2_join_8",
	[]],

	[anyone|plyr, "npc2_join_8",
	[],
	"Very well. Free your friends and return to our camp.", "close_window",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 15000, 34),
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc2_join_8",
	[],
	"Sorry. I can't afford that at the moment.", "close_window",
	[]],

	[trp_npc3, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"Sancho. Agh, where'd you run off to?", "npc3_join_1",
	[]],

	[trp_npc3, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.)", "close_window",
	[]],

	[anyone|plyr, "npc3_join_1",
	[],
	"I'm not Sancho.", "npc3_join_2",
	[]],

	[anyone|plyr, "npc3_join_1",
	[],
	"Apologies.", "close_window",
	[]],

	[anyone, "npc3_join_2",
	[],
	"Don't go for a stroll without telling me first! Lots of people need beating up.", "npc3_join_3",
	[]],

	[anyone, "npc3_join_3",
	[],
	"You're ever the slowpoke. Now let's go give them a beating!", "npc3_join_4",
	[]],

	[anyone, "npc3_join_4",
	[],
	"Now!", "npc3_join_5",
	[]],

	[anyone|plyr, "npc3_join_5",
	[],
	"Who? Where? Why do you want to beat them up?", "npc3_join_6",
	[]],

	[anyone|plyr, "npc3_join_5",
	[],
	"Crazy old man...", "close_window",
	[]],

	[anyone, "npc3_join_6",
	[],
	"Well that's up to me to decide, now isn't it? Now are we going to sit here and talk or are we going to go find a fight?", "npc3_join_7",
	[]],

	[anyone, "npc3_join_7",
	[],
	"Well? Now let's go already, Sancho.", "npc3_join_8",
	[]],

	[anyone|plyr, "npc3_join_8",
	[],
	"Again, i'm not Sancho. But very well, let's go.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc3_join_8",
	[],
	"Sure, go enjoy yourself. Goodbye.", "close_window",
	[]],

	[trp_npc4, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(troop_slot_ge, "trp_player", 13, 25),
		(party_slot_ge, "p_main_party", 28, 26000)
	],
	"Hello there. You seem clearly interested in my sword.", "npc4_join_1",
	[]],

	[trp_npc4, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.) (honor 25, money 26000)", "close_window",
	[]],

	[anyone|plyr, "npc4_join_1",
	[],
	"In fact, i am.", "npc4_join_2",
	[]],

	[anyone|plyr, "npc4_join_1",
	[],
	"Your what? Go bother someone else.", "close_window",
	[]],

	[anyone, "npc4_join_2",
	[],
	"As i was hunting in the forest, a giant clad in green armor came out of the woods. With naught a word he disappeared, leaving only this sword behind.", "npc4_join_3",
	[]],

	[anyone, "npc4_join_3",
	[],
	"This sword is huge, but very light. Only i can lift it.", "npc4_join_4",
	[]],

	[anyone, "npc4_join_4",
	[],
	"However, what is the use of a sword without a battle to wield it in? And so here i am, searching for a battlefield.", "npc4_join_5",
	[]],

	[anyone|plyr, "npc4_join_5",
	[],
	"Then by all means, join me. I am a person that creates battlefields.", "npc4_join_6",
	[]],

	[anyone|plyr, "npc4_join_5",
	[],
	"An interesting story. No doubt told by your ale. Goodbye.", "close_window",
	[]],

	[anyone, "npc4_join_6",
	[],
	"Good! But of course, i am a mercenary. I believe a contract with a wage is in order.", "npc4_join_7",
	[]],

	[anyone, "npc4_join_7",
	[
		(assign, reg3, 25000)
	],
	"Perhaps {reg3} denars would seem appropriate?", "npc4_join_8",
	[]],

	[anyone|plyr, "npc4_join_8",
	[],
	"Fair enough. Welcome to the fold.", "close_window",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 25000, 34),
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc4_join_8",
	[],
	"Sorry. I can't afford that at the moment.", "close_window",
	[]],

	[trp_npc5, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"What are you looking at?", "npc5_join_1",
	[]],

	[trp_npc5, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.)", "close_window",
	[]],

	[anyone|plyr, "npc5_join_1",
	[],
	"I am seeking comrades.", "npc5_join_2",
	[]],

	[anyone|plyr, "npc5_join_1",
	[],
	"Nothing. My apologies.", "close_window",
	[]],

	[anyone, "npc5_join_2",
	[],
	"I am incompetent. Talking to me is a waste of breath.", "npc5_join_3",
	[]],

	[anyone, "npc5_join_3",
	[],
	"I was a physician in the arena. Gladiators that survived the fights, i would patch them up.", "npc5_join_4",
	[]],

	[anyone, "npc5_join_4",
	[],
	"But one day the gladiators revolted. They killed their masters and escaped. So now what am i to do?", "npc5_join_5",
	[]],

	[anyone|plyr, "npc5_join_5",
	[],
	"I said i was seeking comrades. A doctor would always be welcome.", "npc5_join_6",
	[]],

	[anyone|plyr, "npc5_join_5",
	[],
	"I don't know. Best of luck to you.", "close_window",
	[]],

	[anyone, "npc5_join_6",
	[],
	"A mercenary band, you say? Travelers?", "npc5_join_7",
	[]],

	[anyone, "npc5_join_7",
	[],
	"Very well. Perhaps i can help train your recruits as well.", "npc5_join_8",
	[]],

	[anyone|plyr, "npc5_join_8",
	[],
	"Glad to hear it. Welcome to us, doctor.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc5_join_8",
	[],
	"A physician in a profession of death battles? How pointless. Farewell.", "close_window",
	[]],

	[trp_npc6, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(neq, "$wm_player_fac", "fac_kingdom_35"),
		(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
		(gt, ":party_size_wo_prisoners_main_party", 8000)
	],
	"You are a commander, are you not?", "npc6_join_1",
	[]],

	[trp_npc6, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.) (army 8000) (not Lubu faction)", "close_window",
	[]],

	[anyone|plyr, "npc6_join_1",
	[],
	"I just so happen to be.", "npc6_join_2",
	[]],

	[anyone|plyr, "npc6_join_1",
	[],
	"No, i'm not.", "close_window",
	[]],

	[anyone, "npc6_join_2",
	[],
	"I was once a general. A leader of men, like you.", "npc6_join_3",
	[]],

	[anyone, "npc6_join_3",
	[],
	"But one fateful day i was defeated. Stabbed in the back, i barely lived to tell the tale.", "npc6_join_4",
	[]],

	[anyone, "npc6_join_4",
	[],
	"I am only here due to the mystical healing arts of the very same people who brought about my defeat. Now i seek an answer to why they saved me.", "npc6_join_5",
	[]],

	[anyone|plyr, "npc6_join_5",
	[],
	"I cannot guarantee you answers, but i can offer you a position in my army. Officers are always practical.", "npc6_join_6",
	[]],

	[anyone|plyr, "npc6_join_5",
	[],
	"I'll leave you to your search.", "close_window",
	[]],

	[anyone, "npc6_join_6",
	[],
	"My old lord was murdered by his adopted son, Lu bu. Betrayed as repayment for giving him an upbringing, a home.", "npc6_join_7",
	[]],

	[anyone, "npc6_join_7",
	[],
	"To punish him, i will need an army. In the meantime your offer is graciously accepted.", "npc6_join_8",
	[]],

	[anyone|plyr, "npc6_join_8",
	[],
	"Welcome, in that case.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop"),
		(call_script, "script_change_player_relation_with_troop", "trp_tt_lord_35_00", -50),
		(call_script, "script_change_player_relation_with_troop", "trp_tt_lord_35_00", -50),
		(call_script, "script_change_player_relation_with_troop", "trp_tt_lord_35_00", -50)
	]],

	[anyone|plyr, "npc6_join_8",
	[],
	"My apologies. We do not accept defeat in my army. Death before dishonor.", "close_window",
	[]],

	[trp_npc7, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(eq, "$wm_player_fac", "fac_kingdom_1"),
		(troop_slot_ge, "trp_player", 13, 50),
		(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
		(ge, ":party_size_wo_prisoners_main_party", 9000)
	],
	"You are a commander of Joseon, are you not?", "npc7_join_1",
	[]],

	[trp_npc7, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.) (army 9000) (honor 50)", "close_window",
	[]],

	[anyone|plyr, "npc7_join_1",
	[],
	"Yes, i serve Korea.", "npc7_join_2",
	[]],

	[anyone|plyr, "npc7_join_1",
	[],
	"My apologies, you must have mistaken me for someone else.", "close_window",
	[]],

	[anyone, "npc7_join_2",
	[],
	"So do i. I am the commander of the civil defense force.", "npc7_join_3",
	[]],

	[anyone, "npc7_join_3",
	[],
	"Unfortunately, our police force has been defeated by the Muromachi shogunate. There are precious few of us left.", "npc7_join_4",
	[]],

	[anyone, "npc7_join_4",
	[],
	"Now i am looking for volunteers. New recruits. Any able hands.", "npc7_join_5",
	[]],

	[anyone|plyr, "npc7_join_5",
	[],
	"I cannot offer soldiers to your cause, but i can offer you a position at my side. Your knowledge is sure to be useful.", "npc7_join_6",
	[]],

	[anyone|plyr, "npc7_join_5",
	[],
	"Then i wish you luck. Fare well.", "close_window",
	[]],

	[anyone, "npc7_join_6",
	[],
	"Not quite what i set out for, but surely a much better opportunity.", "npc7_join_7",
	[]],

	[anyone, "npc7_join_7",
	[],
	"Too many innocents are being caught up in these petty squabbles. We must move with haste.", "npc7_join_8",
	[]],

	[anyone|plyr, "npc7_join_8",
	[],
	"By all means. Welcome to the army.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc7_join_8",
	[],
	"I am sorry. A police officer has no place in war. You steer clear of big battles and keep the citizens safe instead.", "close_window",  # Pathetic incompetent Yuki only got this far
	[]],

	[trp_npc9, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(troop_slot_ge, "trp_player", 13, 50)
	],
	"Nice to meet you. need a drink?", "npc9_join_1",
	[]],

	[trp_npc9, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.) (honor 50)", "close_window",
	[]],

	[anyone|plyr, "npc9_join_1",
	[],
	"Yes, in fact. Thank you.", "npc9_join_2",
	[]],

	[anyone|plyr, "npc9_join_1",
	[],
	"I'm fine, thank you.", "close_window",
	[]],

	[anyone, "npc9_join_2",
	[],
	"Good! Nothing's quite like drinking with friends!", "npc9_join_3",
	[]],

	[anyone, "npc9_join_3",
	[],
	"I'm a warrior. Recently, there hasn't been too much work for people like me.", "npc9_join_4",
	[]],

	[anyone, "npc9_join_4",
	[],
	"So all i can do is drink all day long. It's boring, i tell ya!'", "npc9_join_5",
	[]],

	[anyone|plyr, "npc9_join_5",
	[],
	"A real warrior, huh? I could always use men like you.", "npc9_join_6",
	[]],

	[anyone|plyr, "npc9_join_5",
	[],
	"I'll leave. Thank you for the drink.", "close_window",
	[]],

	[anyone, "npc9_join_6",
	[],
	"Oh, i like where this is going! I knew it the moment i saw you - like a mist of blood hanging all around you.", "npc9_join_7",
	[]],

	[anyone, "npc9_join_7",
	[],
	"I've been resting way too long. My sword arm needs practice. Allow me to loosen up under your command.", "npc9_join_8",
	[]],

	[anyone|plyr, "npc9_join_8",
	[],
	"I'll look forward to seeing you fight! Welcome aboard.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc9_join_8",
	[],
	"My apologies, i don't need more warriors as it is.", "close_window",
	[]],

	[trp_npc11, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"Greetings. It is nice to meet you, but it might be unwise of you to speak to me.", "npc11_join_1",
	[]],

	[trp_npc11, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.)", "close_window",
	[]],

	[anyone|plyr, "npc11_join_1",
	[],
	"And why would that be, friend?", "npc11_join_2",
	[]],

	[anyone|plyr, "npc11_join_1",
	[],
	"I suppose you are right. Good day.", "close_window",
	[]],

	[anyone, "npc11_join_2",
	[],
	"I am an exile.", "npc11_join_3",
	[]],

	[anyone, "npc11_join_3",
	[],
	"My tribe avoided all contact with outside civilization. I believed interacting with outsiders would be the wise course of action - the smart way to progress.", "npc11_join_4",
	[]],

	[anyone, "npc11_join_4",
	[],
	"My tribe did not see it the same way. They believe tradition is a virtue that must be upheld above all else. They saw me as a traitor, introducing ideas inspired by the outside world.", "npc11_join_5",
	[]],

	[anyone|plyr, "npc11_join_5",
	[],
	"So they exiled you as a traitor? You are better off without them. Come with us! We are travellers - with us you will see cultures aplenty.", "npc11_join_6",
	[]],

	[anyone|plyr, "npc11_join_5",
	[],
	"That is what you get for disrespecting tradition. Farewell.", "close_window",
	[]],

	[anyone, "npc11_join_6",
	[],
	"Really? You are an outsider, however. How do i know i can trust you?", "npc11_join_7",
	[]],

	[anyone, "npc11_join_7",
	[],
	"Then again, what does that matter? I am as good as an outsider myself. It is a most gracious offer i will not pass up - let me come with you.", "npc11_join_8",
	[]],

	[anyone|plyr, "npc11_join_8",
	[],
	"Welcome.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc11_join_8",
	[],
	"My apologies. We don't need traitors in our ranks.", "close_window",
	[]],

	[trp_npc12, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(troop_slot_ge, "trp_player", 13, 25)
	],
	"Greetings. Perhaps you could assist me in an urgent matter?", "npc12_join_1",
	[]],

	[trp_npc12, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.) (honor 25)", "close_window",
	[]],

	[anyone|plyr, "npc12_join_1",
	[],
	"Perhaps. What do you need?", "npc12_join_2",
	[]],

	[anyone|plyr, "npc12_join_1",
	[],
	"My apologies.", "close_window",
	[]],

	[anyone, "npc12_join_2",
	[],
	"I have heard news that Hua Tuo is dead.", "npc12_join_3",
	[]],

	[anyone, "npc12_join_3",
	[],
	"He was known as the master of medicine. He only ever took one apprentice to pass on his secrets to.", "npc12_join_4",
	[]],

	[anyone, "npc12_join_4",
	[],
	"That apprentice is me. As such, with his death i become a wanted man. I need to escape this place, fast.", "npc12_join_5",
	[]],

	[anyone|plyr, "npc12_join_5",
	[],
	"I understand. Then let us be on our way.", "npc12_join_6",
	[]],

	[anyone|plyr, "npc12_join_5",
	[],
	"And that is understandable. Your knowledge can help lots of people. Go back and pass it on.", "close_window",
	[]],

	[anyone, "npc12_join_6",
	[],
	"Thank you. In return i will do what i can to aid your army.", "npc12_join_7",
	[]],

	[anyone, "npc12_join_7",
	[],
	"I also have knowledge of field surgery. I won't be a hindrance to you.", "npc12_join_8",
	[]],

	[anyone|plyr, "npc12_join_8",
	[],
	"Then let's be on our way, doctor.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc12_join_8",
	[],
	"My apologies. This sounds like it might put us in peril.", "close_window",
	[]],

	[trp_npc13, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"You seem strong! I am impressed.", "npc13_join_1",
	[]],

	[anyone|plyr, "npc13_join_1",
	[],
	"You don't seem like a pushover yourself.", "npc13_join_2",
	[]],

	[anyone|plyr, "npc13_join_1",
	[],
	"Get out.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_quest_menu")
	]],

	[anyone, "npc13_join_2",
	[],
	"I have dueled many. Countless proud families have been humbled by my blade.", "npc13_join_3",
	[]],

	[anyone, "npc13_join_3",
	[],
	"Because of that, many hold grudges against me. It would seem i should go on a trip for a while.", "npc13_join_4",
	[]],

	[anyone, "npc13_join_4",
	[],
	"to avoid resentment? No. I'm not afraid of them. My concern is the lack of worthy opponents. The nobles are happy to talk behind my back, but no longer dare challenge me.", "npc13_join_5",
	[]],

	[anyone|plyr, "npc13_join_5",
	[],
	"If it's a fight you want, fight by my side. You'll have plenty of opponents.", "npc13_join_6",
	[]],

	[anyone|plyr, "npc13_join_5",
	[],
	"Count this time of peace a blessing.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_quest_menu")
	]],

	[anyone, "npc13_join_6",
	[],
	"I accept.", "npc13_join_7",
	[]],

	[anyone, "npc13_join_7",
	[],
	"Travel will do me good. I wonder how my sword will hold up in foreign lands.", "npc13_join_8",
	[]],

	[anyone|plyr, "npc13_join_8",
	[],
	"Then let us be on our way.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_quest_menu")
	]],

	[anyone|plyr, "npc13_join_8",
	[],
	"My apologies. A battlefield is no place for duels and glory.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_quest_menu")
	]],

	[trp_npc14, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"Before you kill me, i have a proposition for you.", "npc14_join_1",
	[]],

	[anyone|plyr, "npc14_join_1",
	[],
	"What proposition?", "npc14_join_2",
	[]],

	[anyone|plyr, "npc14_join_1",
	[],
	"I don't care.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(change_screen_return)
	]],

	[anyone, "npc14_join_2",
	[],
	"If you let me live, i can work for you.", "npc14_join_3",
	[]],

	[anyone, "npc14_join_3",
	[],
	"Assassination, espionage, sabotage...", "npc14_join_4",
	[]],

	[anyone, "npc14_join_4",
	[],
	"As a war lord, you will certainly have use of my skills.", "npc14_join_5",
	[]],

	[anyone|plyr, "npc14_join_5",
	[],
	"An assassin of my own... That does sound useful. I will give you a chance.", "npc14_join_6",
	[]],

	[anyone|plyr, "npc14_join_5",
	[],
	"I dont need turncoats in my army. I will let you leave with your life. Begone.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(change_screen_return)
	]],

	[anyone, "npc14_join_6",
	[],
	"Its a deal!", "npc14_join_7",
	[]],

	[anyone, "npc14_join_7",
	[],
	"You won't regret letting me live. I'll pay it back to you.", "npc14_join_8",
	[]],

	[anyone|plyr, "npc14_join_8",
	[],
	"I'll hold you to that. Welcome.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop"),
		(change_screen_return)
	]],

	[anyone|plyr, "npc14_join_8",
	[],
	"I changed my mind. You may go.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(change_screen_return)
	]],

	[trp_npc16, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"In fact, I avoided you. But now it seems impossible. Why do you waiting for me?", "npc16_join_1",
	[]],

	[anyone|plyr, "npc16_join_1",
	[],
	"I'm looking for a good Adviser.", "npc16_join_2",
	[]],

	[anyone|plyr, "npc16_join_1",
	[],
	"Sorry. You are different from what was expected.", "close_window",
	[]],

	[anyone, "npc16_join_2",
	[],
	"Adviser?  I've found what you want to me. The War adviser.", "npc16_join_3",
	[]],

	[anyone, "npc16_join_3",
	[],
	"You already have a great reputation. don't need to be greedy.", "npc16_join_4",
	[]],

	[anyone, "npc16_join_4",
	[],
	"Do you have any other plans?", "npc16_join_5",
	[]],

	[anyone|plyr, "npc16_join_5",
	[],
	"I would make a huge empire.", "npc16_join_6",
	[]],

	[anyone|plyr, "npc16_join_5",
	[],
	"You are different from what was expected.", "close_window",
	[]],

	[anyone, "npc16_join_6",
	[],
	"Are you serious? Of course, I agree with you to do so. Situation was split into smaller countries, some let us inspire pain to people.", "npc16_join_7",
	[]],

	[anyone, "npc16_join_7",
	[],
	"I know listening to the action you've been up to now. It would be a meaningful clearly able to fight by your side. I will leave you along.", "npc16_join_8",
	[]],

	[anyone|plyr, "npc16_join_8",
	[],
	"Thank you for me to understand my thoughts.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc16_join_8",
	[],
	"I am sorry. My opinion has changed.", "close_window",
	[]],

	[trp_npc_19, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(neq, "$wm_player_fac", "fac_kingdom_5"),
		(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
		(gt, ":party_size_wo_prisoners_main_party", 8000)
	],
	"Do not step in my circle.", "npc19_join_1",
	[]],

	[trp_npc_19, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.) (army 8000) (not roma faction)", "close_window",
	[]],

	[anyone|plyr, "npc19_join_1",
	[],
	"All right. I am sorry.", "npc19_join_2",
	[]],

	[anyone|plyr, "npc19_join_1",
	[],
	"Exits.", "close_window",
	[]],

	[anyone, "npc19_join_2",
	[],
	"I do not want to be disturbed, but there is no way.", "npc19_join_3",
	[]],

	[anyone, "npc19_join_3",
	[],
	"By Rome to attack this place, everything was ruined. Because rome is looking for me,  I should leave.", "npc19_join_4",
	[]],

	[anyone, "npc19_join_4",
	[],
	"Someday I'll take revenge to them.", "npc19_join_5",
	[]],

	[anyone|plyr, "npc19_join_5",
	[],
	"I can help you. Through an army.", "npc19_join_6",
	[]],

	[anyone|plyr, "npc19_join_5",
	[],
	"I heard well. Goodbye.", "close_window",
	[]],

	[anyone, "npc19_join_6",
	[],
	"Army? Is it possible you against the Roman army? ha.", "npc19_join_7",
	[]],

	[anyone, "npc19_join_7",
	[],
	"I do not even expect such a thing to you. But it is dangerous to leave me alone. Let's go together. I'm too old.", "npc19_join_8",
	[]],

	[anyone|plyr, "npc19_join_8",
	[],
	"Welcome.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc19_join_8",
	[],
	"I am sorry. My opinion has changed.", "close_window",
	[]],

	[trp_npc_21, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(troop_slot_ge, "trp_player", 13, 25)
	],
	"I think I want to borrow money to you. It is sufficient at 100,000 denar.", "npc21_join_1",
	[]],

	[trp_npc_21, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.) (honor 25)", "close_window",
	[]],

	[anyone|plyr, "npc21_join_1",
	[],
	"There is no such money to me.", "npc21_join_2",
	[]],

	[anyone|plyr, "npc21_join_1",
	[],
	"No. I'm not.", "close_window",
	[]],

	[anyone, "npc21_join_2",
	[],
	"While killing people so much, why there is no money to you?", "npc21_join_3",
	[]],

	[anyone, "npc21_join_3",
	[],
	"Without take money, Why do you kill people?", "npc21_join_4",
	[]],

	[anyone, "npc21_join_4",
	[],
	"It is not possible to understand. I know how to make money.  I will be the person you need. also I need you.", "npc21_join_5",
	[]],

	[anyone|plyr, "npc21_join_5",
	[],
	"Why do you need me?", "npc21_join_6",
	[]],

	[anyone|plyr, "npc21_join_5",
	[],
	"I heard well. Goodbye.", "close_window",
	[]],

	[anyone, "npc21_join_6",
	[],
	"Because, there is a possibility that touch a lot of money to people like you.", "npc21_join_7",
	[]],

	[anyone, "npc21_join_7",
	[],
	"And I can be to increase the money. If you do not like, go away.", "npc21_join_8",
	[]],

	[anyone|plyr, "npc21_join_8",
	[],
	"Making money is not bad. Welcome. ", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc21_join_8",
	[],
	"It was fun talking. Goodbye.", "close_window",
	[]],

	[trp_npc_23, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(troop_slot_ge, "trp_player", 13, 0)
	],
	"Please help me. The ship has been wrecked.", "npc_23_join_1",
	[]],

	[trp_npc_23, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.) (honor 0)", "close_window",
	[]],

	[anyone|plyr, "npc_23_join_1",
	[],
	"How long ago since you came here?", "npc_23_join_2",
	[]],

	[anyone|plyr, "npc_23_join_1",
	[],
	"No. I'm not.", "close_window",
	[]],

	[anyone, "npc_23_join_2",
	[],
	"A month. I have endured while eating straw or wood in it.", "npc_23_join_3",
	[]],

	[anyone, "npc_23_join_3",
	[],
	"I am a merchant. It was so long ago that merchant ships sunk.", "npc_23_join_4",
	[]],

	[anyone, "npc_23_join_4",
	[],
	"I ended now.", "npc_23_join_5",
	[]],

	[anyone|plyr, "npc_23_join_5",
	[],
	"to act with me is? I can help that you recover.", "npc_23_join_6",
	[]],

	[anyone|plyr, "npc_23_join_5",
	[],
	"I heard well. Goodbye.", "close_window",
	[]],

	[anyone, "npc_23_join_6",
	[],
	"God did not abandon me yet. You are my messenger of heaven?", "npc_23_join_7",
	[]],

	[anyone, "npc_23_join_7",
	[],
	"Of course, I will be at the mercy of your. I will recover by managing your funds.", "npc_23_join_8",
	[]],

	[anyone|plyr, "npc_23_join_8",
	[],
	"Welcome. Accountant.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc_23_join_8",
	[],
	"I am sorry. My opinion has changed.", "close_window",
	[]],

	[trp_npc_24, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"Here is really cold. But why did you come to a place like this?", "npc_24_join_1",
	[]],

	[trp_npc_24, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.)", "close_window",
	[]],

	[anyone|plyr, "npc_24_join_1",
	[],
	"I am looking for an excellent companion.", "npc_24_join_2",
	[]],

	[anyone|plyr, "npc_24_join_1",
	[],
	"Neglect", "close_window",
	[]],

	[anyone, "npc_24_join_2",
	[],
	"No one like that. Here, at least.", "npc_24_join_3",
	[]],

	[anyone, "npc_24_join_3",
	[],
	"There was a time when I was also through the travel like you. I found a place called vinland.", "npc_24_join_4",
	[]],

	[anyone, "npc_24_join_4",
	[],
	"However, it has been attacked by the local people there. We have finally escaped, has holed up here again.", "npc_24_join_5",
	[]],

	[anyone|plyr, "npc_24_join_5",
	[],
	"I think you miss the travel. Come with us.", "npc_24_join_6",
	[]],

	[anyone|plyr, "npc_24_join_5",
	[],
	"I heard well. Goodbye.", "close_window",
	[]],

	[anyone, "npc_24_join_6",
	[],
	"As a matter of fact, you are right.  I remember painful, but it would be better to grow old than of it is.", "npc_24_join_7",
	[]],

	[anyone, "npc_24_join_7",
	[],
	"I'll help in navigation and combat.", "npc_24_join_8",
	[]],

	[anyone|plyr, "npc_24_join_8",
	[],
	"Welcome. Adventurer.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc_24_join_8",
	[],
	"I am sorry. My opinion has changed.", "close_window",
	[]],

	[trp_npc_26, "start",
	[
		(eq, "$g_talk_troop_already_met", 0),
		(troop_slot_ge, "trp_player", 13, 50)
	],
	"What do you want? Are you a soldier?", "npc_26_join_1",
	[]],

	[trp_npc_26, "start",
	[
		(eq, "$g_talk_troop_already_met", 0)
	],
	"(He ignores you.) (honor 50)", "close_window",
	[]],

	[anyone|plyr, "npc_26_join_1",
	[],
	"You do not need to be vigilant.  It is a way just to pass.", "npc_26_join_2",
	[]],

	[anyone|plyr, "npc_26_join_1",
	[],
	"(Escaping)", "close_window",
	[]],

	[anyone, "npc_26_join_2",
	[],
	"Sorry to scare you.   I am afraid of the soldiers in the circumstances.", "npc_26_join_3",
	[]],

	[anyone, "npc_26_join_3",
	[],
	"You're a traveler. Then, you will help to me. I was a slave. Was a gladiator slave.", "npc_26_join_4",
	[]],

	[anyone, "npc_26_join_4",
	[],
	"During the rebellion of gladiators, and commanded the army, was beyond the Alps. However, I did not have anywhere where I settle.", "npc_26_join_5",
	[]],

	[anyone|plyr, "npc_26_join_5",
	[],
	"Next, are you going to leave?", "npc_26_join_6",
	[]],

	[anyone|plyr, "npc_26_join_5",
	[],
	"I heard well. Goodbye.", "close_window",
	[]],

	[anyone, "npc_26_join_6",
	[],
	"You are right. I am a person who does not suit farming.   I am still gladiator.", "npc_26_join_7",
	[]],

	[anyone, "npc_26_join_7",
	[],
	"If you're me accept me, I will kill off the many enemies. What are your thoughts?", "npc_26_join_8",
	[]],

	[anyone|plyr, "npc_26_join_8",
	[],
	"Without a doubt, we will welcome you. Gladiator.", "close_window",
	[
		(troop_set_slot, "$g_talk_troop", 15, 1),
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "npc_26_join_8",
	[],
	"It was fun talking. Goodbye.", "close_window",
	[]],

	[anyone, "start",
	[],
	"If you've seen this message, please report it as a bug with any information you have.", "close_window",
	[]],

	[anyone, "do_member_trade",
	[],
	"Anything else?", "member_talk",
	[]],

	[anyone|plyr, "member_talk",
	[],
	"What can you tell me about your skills?", "view_member_char_requested",
	[]],

	[anyone, "view_member_char_requested",
	[],
	"All right, let me tell you...", "do_member_view_char",
	[
		(change_screen_view_character)
	]],

	[anyone, "do_member_view_char",
	[],
	"Anything else?", "member_talk",
	[]],

	[anyone|plyr, "member_talk",
	[
		(eq, "$g_talk_troop", "$player_spouse"),
		(eq, "$wm_talk_state", 1),
		(eq, "$player_gender", 0),
		(eq, "$talk_troop_gender", 1),
		(call_script, "script_wm_main_party_has_troop_sc", "$g_talk_troop"),
		(neq, "$wm_comp_continue", 1)
	],
	"I want you to join my party", "spouse_join",
	[]],

	[anyone|plyr, "member_talk",
	[
		(eq, "$attemp_commu", 0)
	],
	"   How do you do these days?", "member_comp_relation_talk",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "member_comp_relation_talk",
	[
		(eq, "$comp_rel_passsss", 0)
	],
	"Im doing just fine.(Greeted appropriately.)", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 5)
	]],

	[anyone, "member_comp_relation_talk",
	[
		(eq, "$comp_rel_passsss", 1)
	],
	"Haha, How about you?(had a decent conversation.)", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 5)
	]],

	[anyone, "member_comp_relation_talk",
	[
		(eq, "$comp_rel_passsss", 2)
	],
	"just fine. You want to hear my story? (Talked for a long time.)", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 8)
	]],

	[anyone, "member_comp_relation_talk",
	[
		(eq, "$comp_rel_passsss", 3)
	],
	"There are rumors that funny.(laughed during a conversation.)", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 10)
	]],

	[anyone, "member_comp_relation_talk",
	[],
	"I can not talk right now.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -2)
	]],

	[anyone|plyr, "member_talk",
	[],
	"Sorry, I forgot. Can you remind me your role?", "member_bonus_explain",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_npc1")
	],
	"The chief mate. severe weather like storm, I will be able to handle this. I can ignore adverse at the sea.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_npc2")
	],
	"Range fighting. There are three sherwood bandits under my control. Little john, Will Scarlet, and Much the Miller's Son.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_npc3")
	],
	"I don't know!", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_npc4")
	],
	"Melee fighting. There are two vanguard under my control.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(this_or_next|eq, "$g_talk_troop", "trp_npc5"),
		(eq, "$g_talk_troop", "trp_tt_lady_ex_03")
	],
	"Training. I can handle doubled the soldiers.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_npc6")
	],
	"Charging. There are two Xiliangqibing under my control.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_npc7")
	],
	"Charging. There are four Uibyeong under my control.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_npc9")
	],
	"Melee/Range fighting. I will fight alone, it is sufficient by itself.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_npc11")
	],
	"Melee/Range fighting. There are two Avenger under my control.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_npc12")
	],
	"Medicine. We will be able to deal with injuries and illnesses.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_npc13")
	],
	"Melee fighting. My three disciples will fight with me. Yamamoto gengo jaemon, Delao magonojyo, Motomenoseuke", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_npc14")
	],
	"infiltration, I can open castle gate. and Melee/Range fighting. There are two Hashashin under my control.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_npc_19")
	],
	"Siege engineer, enemy will be damaged by my siege weapon.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(this_or_next|eq, "$g_talk_troop", "trp_npc_21"),
		(eq, "$g_talk_troop", "trp_npc_23")
	],
	"Accounting, I can increase the benefits of trade.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_npc_24")
	],
	"Melee/Range fighting. There are two Viking under my control. and Navigation, but i'm not good..", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_npc_26")
	],
	"Melee fighting. There are two Gladiator under my control. and Navigation, but i'm not good.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_01")
	],
	"You know!, What I need to say?", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_02")
	],
	"Melee/Range fighting. My four followers will fight with me.  and Navigation, but i'm not good.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_04")
	],
	"...Pardon?", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_05")
	],
	"Charging, I only need my elephant.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_06")
	],
	"Melee fighting, There are two Shield-Maiden under my control. ", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_07")
	],
	"Charging, There are two Chevalier under my control. ", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_08")
	],
	"Singing? sorry, I'm so helpless.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_09")
	],
	"Melee fighting. There are two Immortal under my control.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_10")
	],
	"Storytelling? What I need to say?", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_11")
	],
	"Hmm... nothing?", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_12")
	],
	"Free Espionage, Melee/Range fighting. My two Ninja will fight with me.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_13")
	],
	"Melee fighting. And two ashigaru will be backup.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_14")
	],
	"Nothing. however, Father sent the Servant for me. and my Servant will fight for me. you know? He like elephant riding. Fuckin elephant poop!", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_15")
	],
	"Sleeping. I'm so sleepy.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_16")
	],
	"Shopping. I think it is nice timing for money looting.", "member_talk",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34)
	]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_17")
	],
	"Melee fighting. and My two warrior will fight with me.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[
		(eq, "$g_talk_troop", "trp_tt_lady_ex_18")
	],
	"Blow job. haha I'm just kidding....maybe half is true.", "member_talk",
	[]],

	[anyone, "member_bonus_explain",
	[],
	"Hmm... Sorry. I need think about that.", "member_talk",
	[]],

	[anyone|plyr, "member_talk",
	[
		(is_between, "$g_talk_troop", "trp_npc1", "trp_kingdom_1_lord"),
		(ge, "$g_talk_troop_relation", 0)
	],
	"Can you guard me?", "member_guard_1",
	[]],

	[anyone, "member_guard_1",
	[],
	"Okay. I'll do it.", "close_window",
	[
		(assign, "$bodyguard_troop", "$g_talk_troop")
	]],

	[anyone|plyr, "member_talk",
	[
		(eq, "$talk_troop_gender", 1),
		(troop_is_hero, "$g_talk_troop"),
		(ge, "$g_talk_troop_relation", 0)
	],
	"Can you to follow me?", "member_eyecandy_1",
	[]],

	[anyone, "member_eyecandy_1",
	[],
	"Okay. I'll do it.", "close_window",
	[
		(assign, "$eyecandy_troop", "$g_talk_troop")
	]],

	[anyone|plyr, "member_talk",
	[
		(neg|troop_slot_ge, "trp_player", 3, "trp_tt_lady_01_01"),
		(neq, "$g_talk_troop", "$player_spouse"),
		(is_between, "$g_talk_troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(ge, "$g_talk_troop_relation", 25),
		(eq, "$player_gender", 0),
		(eq, "$attemp_commu", 0)
	],
	"Today I want to talk seriously about our relationship.", "marry_for_man_player_1",
	[]],

	[anyone, "marry_for_man_player_1",
	[],
	"(She listened to the story with eager attention.)", "marry_for_man_player_2",
	[]],

	[anyone|plyr, "marry_for_man_player_2",
	[],
	"I was thinking for a long time. Please marry me.", "member_marryme",
	[
		(call_script, "script_try_attemp_commu"),
		(troop_get_slot, ":g_talk_troop_player_order_object", "$g_talk_troop", slot_troop_player_order_object),
		(store_attribute_level, ":attribute_level_player_3", "trp_player", 3),
		(party_get_slot, ":main_party_29", "p_main_party", 29),
		(val_div, ":main_party_29", 37),
		(troop_get_slot, ":player_original_faction", "trp_player", slot_troop_original_faction),
		(val_div, ":player_original_faction", 37),
		(assign, ":var_5", 0),
		(try_for_range, ":party", "p_pyongyang", "p_place_end"),
			(party_slot_eq, ":party", slot_town_tavern, "trp_player"),
			(val_add, ":var_5", 1),
		(try_end),
		(try_begin),
			(eq, ":g_talk_troop_player_order_object", 11),
			(assign, ":value", 0),
			(assign, ":value_2", 75),
			(assign, ":value_3", -5),
			(assign, ":value_4", 15),
			(assign, ":value_5", 20),
			(assign, ":value_6", 20),
		(else_try),
			(eq, ":g_talk_troop_player_order_object", 12),
			(assign, ":value", 30000),
			(assign, ":value_2", 60),
			(assign, ":value_3", -5),
			(assign, ":value_4", -25),
			(assign, ":value_5", 30),
			(assign, ":value_6", 10),
		(else_try),
			(eq, ":g_talk_troop_player_order_object", 13),
			(assign, ":value", 40000),
			(assign, ":value_2", 50),
			(assign, ":value_3", 2),
			(assign, ":value_4", -100),
			(assign, ":value_5", 10),
			(assign, ":value_6", 10),
		(else_try),
			(eq, ":g_talk_troop_player_order_object", 14),
			(assign, ":value", 40000),
			(assign, ":value_2", 50),
			(assign, ":value_3", 4),
			(assign, ":value_4", -25),
			(assign, ":value_5", 5),
			(assign, ":value_6", 20),
		(else_try),
			(eq, ":g_talk_troop_player_order_object", 15),
			(assign, ":value", 10000),
			(assign, ":value_2", 90),
			(assign, ":value_3", 1),
			(assign, ":value_4", 75),
			(assign, ":value_5", 17),
			(assign, ":value_6", 30),
		(else_try),
			(assign, ":value", 30000),
			(assign, ":value_2", 75),
			(assign, ":value_3", 1),
			(assign, ":value_4", 10),
			(assign, ":value_5", 17),
			(assign, ":value_6", 15),
		(try_end),
		(str_clear, 40),
		(str_clear, 41),
		(str_clear, 42),
		(str_clear, 43),
		(str_clear, 44),
		(str_clear, 45),
		(str_clear, 46),
		(try_begin),
			(this_or_next|lt, "$g_talk_troop_relation", ":value_2"),
			(lt, "$met_time", ":value_6"),
			(str_store_string, 41, "str_marry_reject_rela"),
		(else_try),
			(le, ":player_original_faction", ":value_4"),
			(str_store_string, 41, "str_marry_reject_honor"),
		(else_try),
			(le, ":var_5", ":value_3"),
			(str_store_string, 41, "str_marry_reject_castle"),
		(else_try),
			(lt, ":attribute_level_player_3", ":value_5"),
			(str_store_string, 41, "str_marry_reject_charis"),
		(else_try),
			(lt, ":main_party_29", ":value"),
			(str_store_string, 41, "str_marry_reject_wealth"),
		(try_end),
		(str_store_string, 40, "str_marry_reject_result"),
		(try_begin),
			(this_or_next|lt, "$g_talk_troop_relation", ":value_2"),
			(this_or_next|lt, ":main_party_29", ":value"),
			(this_or_next|lt, ":var_5", ":value_3"),
			(this_or_next|lt, ":player_original_faction", ":value_4"),
			(this_or_next|lt, ":attribute_level_player_3", ":value_5"),
			(lt, "$met_time", ":value_6"),
			(assign, "$molda_marry_reject", 1),
		(else_try),
			(assign, "$molda_marry_reject", 0),
		(try_end)
	]],

	[anyone|plyr, "marry_for_man_player_2",
	[],
	"Sorry. I have no words for it.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -50)
	]],

	[anyone, "member_marryme",
	[
		(eq, "$molda_marry_reject", 1)
	],
	"{s40}", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -3)
	]],

	[anyone, "member_marryme",
	[],
	"I've waited to say that.", "member_marryme_2",
	[]],

	[anyone|plyr, "member_marryme_2",
	[],
	"If so, do not have to wait. We must immediately proceed to the wedding.", "member_marryme_3",
	[]],

	[anyone, "member_marryme_3",
	[],
	"My husband, I hearby pledge to be your wife, to stand with you in good times and bad. May the heavens smile upon us and bless us with children, livestock, and land.", "member_marryme_4",
	[]],

	[anyone|plyr, "member_marryme_4",
	[],
	"I pledge the same. Let us be husband and wife.", "member_marryme_5",
	[]],

	[anyone|plyr, "member_marryme_4",
	[],
	"Wait -- hold on... I'm not quite ready for this.", "close_window",
	[]],

	[anyone|plyr, "member_marryme_5",
	[],
	"now declare you and i to be husband and wife.", "close_window",
	[
		(assign, "$propose_target", 0),
		(call_script, "script_courtship_event_bride_marry_groom", "$g_talk_troop", "trp_player"),
		(play_track, "track_wedding", 2),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_wedding_menu")
	]],

	[anyone|plyr, "member_talk",
	[
		(neg|is_between, "$g_talk_troop", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin"),
		(try_begin),
			(eq, "$g_talk_troop", "$player_spouse"),
			(assign, ":value", -30),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_01"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_08"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_12"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_15"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_18"),
			(assign, ":value", 30),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_04"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_05"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_06"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_09"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_13"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_17"),
			(assign, ":value", 50),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_02"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_03"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_10"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_11"),
			(assign, ":value", 70),
		(else_try),
			(assign, ":value", 50),
		(try_end),
		(ge, "$g_talk_troop_relation", ":value"),
		(store_current_scene, ":current_scene"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_desert"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_snow"),
		(eq, ":current_scene", "scn_conv_camp_sea"),
		(eq, "$player_gender", 0),
		(eq, "$talk_troop_gender", 1),
		(eq, "$adult_content", 1)
	],
	"Dance for me.", "dance_camp_comp",
	[
		(assign, "$h_dancer_strip", 0)
	]],

	[anyone, "dance_camp_comp",
	[],
	"Haha. What kind of dancing do you want?", "dance_camp_comp_choose",
	[]],

	[anyone|plyr, "dance_camp_comp_choose",
	[],
	"Slow dance.", "dance_camp_comp",
	[
		(call_script, "script_molda_s_scene", 11, 1)
	]],

	[anyone|plyr, "dance_camp_comp_choose",
	[],
	"Usually dancing.", "dance_camp_comp",
	[
		(call_script, "script_molda_s_scene", 11, 2)
	]],

	[anyone|plyr, "dance_camp_comp_choose",
	[],
	"Ass shaking.", "dance_camp_comp",
	[
		(call_script, "script_molda_s_scene", 11, 3)
	]],

	[anyone|plyr, "dance_camp_comp_choose",
	[],
	"Erotic dance.", "dance_camp_comp",
	[
		(call_script, "script_molda_s_scene", 11, 4)
	]],

	[anyone|plyr, "dance_camp_comp_choose",
	[
		(eq, "$h_dancer_strip", 0)
	],
	"The weather is a little hot, isn't it?", "dance_camp_comp",
	[
		(call_script, "script_molda_s_scene", 11, 5),
		(assign, "$h_dancer_strip", 1)
	]],

	[anyone|plyr, "dance_camp_comp_choose",
	[
		(eq, "$h_dancer_strip", 1)
	],
	"Still hot, is not it?", "dance_camp_comp",
	[
		(call_script, "script_molda_s_scene", 11, 6),
		(assign, "$h_dancer_strip", 2)
	]],

	[anyone|plyr, "dance_camp_comp_choose",
	[],
	"[Observation mode]", "close_window",
	[
		(assign, "$sex_cam_on", 1)
	]],

	[anyone|plyr, "dance_camp_comp_choose",
	[],
	"Let's something else.", "close_window",
	[]],

	[anyone|plyr, "member_talk",
	[
		(is_between, "$g_talk_troop", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin"),
		(store_current_scene, ":current_scene"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_desert"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_snow"),
		(eq, ":current_scene", "scn_conv_camp_sea"),
		(eq, "$player_gender", 0),
		(eq, "$talk_troop_gender", 1),
		(eq, "$adult_content", 1)
	],
	"Dance for me.", "qua_dance_q",
	[
		(assign, "$h_dancer_strip", 0)
	]],

	[anyone, "qua_dance_q",
	[],
	"Haha. Let's be hot if the tip. ready?", "qua_dance_a",
	[]],

	[anyone|plyr, "qua_dance_a",
	[
		(call_script, "script_party_money_level_ge", "p_main_party", 100),
		(eq, "$wm_mo_continue", 1)
	],
	"Slow dance.", "qua_dance_q",
	[
		(call_script, "script_molda_s_scene", 11, 1),
		(call_script, "script_party_money_level_diff", "p_main_party", 100, 34)
	]],

	[anyone|plyr, "qua_dance_a",
	[
		(call_script, "script_party_money_level_ge", "p_main_party", 100),
		(eq, "$wm_mo_continue", 1)
	],
	"Usually dancing.", "qua_dance_q",
	[
		(call_script, "script_molda_s_scene", 11, 2),
		(call_script, "script_party_money_level_diff", "p_main_party", 100, 34)
	]],

	[anyone|plyr, "qua_dance_a",
	[
		(call_script, "script_party_money_level_ge", "p_main_party", 100),
		(eq, "$wm_mo_continue", 1)
	],
	"Ass shaking.", "qua_dance_q",
	[
		(call_script, "script_molda_s_scene", 11, 3),
		(call_script, "script_party_money_level_diff", "p_main_party", 100, 34)
	]],

	[anyone|plyr, "qua_dance_a",
	[
		(call_script, "script_party_money_level_ge", "p_main_party", 100),
		(eq, "$wm_mo_continue", 1)
	],
	"Erotic dance.", "qua_dance_q",
	[
		(call_script, "script_molda_s_scene", 11, 4),
		(call_script, "script_party_money_level_diff", "p_main_party", 100, 34)
	]],

	[anyone|plyr, "qua_dance_a",
	[
		(call_script, "script_party_money_level_ge", "p_main_party", 100),
		(eq, "$wm_mo_continue", 1),
		(eq, "$h_dancer_strip", 0)
	],
	"The weather is a little hot, isn't it?", "qua_dance_q",
	[
		(call_script, "script_molda_s_scene", 11, 5),
		(call_script, "script_party_money_level_diff", "p_main_party", 100, 34),
		(assign, "$h_dancer_strip", 1)
	]],

	[anyone|plyr, "qua_dance_a",
	[
		(call_script, "script_party_money_level_ge", "p_main_party", 100),
		(eq, "$wm_mo_continue", 1),
		(eq, "$h_dancer_strip", 1)
	],
	"Still hot, is not it?", "qua_dance_q",
	[
		(call_script, "script_molda_s_scene", 11, 6),
		(call_script, "script_party_money_level_diff", "p_main_party", 100, 34),
		(assign, "$h_dancer_strip", 2)
	]],

	[anyone|plyr, "qua_dance_a",
	[],
	"[Observation mode]", "close_window",
	[
		(assign, "$sex_cam_on", 1)
	]],

	[anyone|plyr, "qua_dance_a",
	[],
	"good bye", "close_window",
	[]],

	[anyone|plyr, "member_talk",
	[
		(store_current_scene, ":current_scene"),
		(neq, ":current_scene", "scn_ex_bedroom"),
		(is_between, "$g_talk_troop", "trp_npc1", "trp_kingdom_1_lord"),
		(eq, "$talk_troop_gender", 0),
		(eq, "$player_gender", 1),
		(eq, "$attemp_commu", 0),
		(eq, "$adult_content", 1)
	],
	"-I give you blowjob.", "member_blowjob_fe_plyr_1",
	[]],

	[anyone, "member_blowjob_fe_plyr_1",
	[],
	"Oh. What a sweetheart.", "member_blowjob_fe_plyr_2",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "member_blowjob_fe_plyr_2",
	[],
	".........", "member_blowjob_fe_plyr_3",
	[
		(call_script, "script_molda_s_scene", 211, 0)
	]],

	[anyone, "member_blowjob_fe_plyr_3",
	[],
	"  Oh....ow!", "member_blowjob_fe_plyr_4",
	[]],

	[anyone|plyr, "member_blowjob_fe_plyr_4",
	[],
	"........  ", "member_blowjob_fe_plyr_5",
	[
		(call_script, "script_molda_s_scene", 211, 0)
	]],

	[anyone, "member_blowjob_fe_plyr_5",
	[],
	"  Uhh!", "member_blowjob_fe_plyr_6",
	[
		(store_random_in_range, ":random_in_range_212_214", 212, 214),
		(call_script, "script_molda_s_scene", ":random_in_range_212_214", 0)
	]],

	[anyone|plyr, "member_blowjob_fe_plyr_6",
	[
		(eq, "$wm_talk_state", 1),
		(is_between, "$g_talk_troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
		(troop_slot_eq, "$g_talk_troop", slot_troop_cur_center, 2)
	],
	"Uhh!   Weird taste. You're feels better now?", "close_window",
	[
		(store_random_in_range, ":random_in_range_4_8", 4, 8),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", ":random_in_range_4_8"),
		(try_begin),
			(eq, "$blowjob_sp_skill", 1),
			(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 3),
		(try_end)
	]],

	[anyone|plyr, "member_blowjob_fe_plyr_6",
	[
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_cur_center, 2)
	],
	"Uhh! Weird taste. You're feels better now?", "member_talk",
	[
		(store_random_in_range, ":random_in_range_4_8", 4, 8),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", ":random_in_range_4_8"),
		(try_begin),
			(eq, "$blowjob_sp_skill", 1),
			(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 5),
		(try_end)
	]],

	[anyone|plyr, "member_talk",
	[
		(store_current_scene, ":current_scene"),
		(neq, ":current_scene", "scn_ex_bedroom"),
		(this_or_next|is_between, "$g_talk_troop", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin"),
		(is_between, "$g_talk_troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(eq, "$attemp_commu", 0),
		(eq, "$adult_content", 1)
	],
	"-If you has give me the blowjob gift. I feel better than now.", "member_blowjob",
	[]],

	[anyone, "member_blowjob",
	[
		(is_between, "$g_talk_troop", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin")
	],
	"That's my job.", "member_blowjob2",
	[
		(call_script, "script_molda_s_scene", 111, 0)
	]],

	[anyone, "member_blowjob",
	[
		(try_begin),
			(eq, "$g_talk_troop", "$player_spouse"),
			(assign, ":value", -30),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_01"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_12"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_15"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_18"),
			(assign, ":value", 0),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_02"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_04"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_06"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_08"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_09"),
			(assign, ":value", 30),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_03"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_05"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_10"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_17"),
			(assign, ":value", 45),
		(else_try),
			(assign, ":value", 60),
		(try_end),
		(ge, "$g_talk_troop_relation", ":value")
	],
	"Between you and me. I will give you a gift.", "member_blowjob2",
	[
		(call_script, "script_try_attemp_commu"),
		(call_script, "script_molda_s_scene", 111, 0)
	]],

	[anyone, "member_blowjob2",
	[],
	".....", "member_blowjob3",
	[
		(call_script, "script_molda_s_scene", 111, 0)
	]],

	[anyone|plyr, "member_blowjob3",
	[],
	"[Squirt cum on the face]", "member_blowjob_face",
	[]],

	[anyone|plyr, "member_blowjob3",
	[],
	"[Squirt cum in mouth]", "member_blowjob_mouth",
	[]],

	[anyone, "member_blowjob_face",
	[],
	" So you happy now? If you're a good boy, Would be nice you to wipe my face.", "member_talk",
	[
		(call_script, "script_molda_s_scene", 112, 0)
	]],

	[anyone, "member_blowjob_mouth",
	[],
	" Uhh. Shitty taste. So you happy now?", "member_talk",
	[
		(call_script, "script_molda_s_scene", 113, 0)
	]],

	[anyone, "member_blowjob",
	[],
	"What the fuck. Bent back and then suck yourself.", "member_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -3)
	]],

	[anyone|plyr, "member_talk",
	[
		(neg|is_between, "$g_talk_troop", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin"),
		(try_begin),
			(eq, "$g_talk_troop", "$player_spouse"),
			(assign, ":value", -30),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_01"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_08"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_12"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_15"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_18"),
			(assign, ":value", 20),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_04"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_05"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_06"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_09"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_13"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_17"),
			(assign, ":value", 40),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_02"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_03"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_10"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_11"),
			(assign, ":value", 70),
		(else_try),
			(assign, ":value", 60),
		(try_end),
		(ge, "$g_talk_troop_relation", ":value"),
		(store_current_scene, ":current_scene"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_desert"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_snow"),
		(eq, ":current_scene", "scn_conv_camp_sea"),
		(eq, "$player_gender", 0),
		(eq, "$talk_troop_gender", 1),
		(eq, "$adult_content", 1),
		(eq, "$attemp_commu", 0)
	],
	"-Come to my tent. Have something to talk.", "fuck_camp_comp_prepre",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "fuck_camp_comp_prepre",
	[
		(store_random_in_range, ":random_in_range_0_2", 0, 2),
		(eq, ":random_in_range_0_2", 0)
	],
	"Not now. My condition is too bad.", "close_window",
	[]],

	[anyone, "fuck_camp_comp_prepre",
	[],
	" I know what you're thinking.", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_fuck_process_normal")
	]],

	[anyone|plyr, "member_talk",
	[
		(neg|is_between, "$g_talk_troop", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin"),
		(try_begin),
			(eq, "$g_talk_troop", "$player_spouse"),
			(assign, ":value", -30),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_01"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_08"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_12"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_15"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_18"),
			(assign, ":value", 20),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_04"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_05"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_06"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_09"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_13"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_17"),
			(assign, ":value", 40),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_02"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_03"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_10"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_11"),
			(assign, ":value", 70),
		(else_try),
			(assign, ":value", 60),
		(try_end),
		(val_add, ":value", 20),
		(ge, "$g_talk_troop_relation", ":value"),
		(store_current_scene, ":current_scene"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_desert"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_snow"),
		(eq, ":current_scene", "scn_conv_camp_sea"),
		(eq, "$player_gender", 0),
		(eq, "$talk_troop_gender", 1),
		(eq, "$adult_content", 1),
		(eq, "$attemp_commu", 0),
		(troop_slot_eq, "$g_talk_troop", slot_troop_last_comment_time, 74),
		(is_between, "$2nd_sex_troop_id", "trp_npc1", "trp_tt_lady_end"),
		(neq, "$g_talk_troop", "$2nd_sex_troop_id"),
		(assign, ":value_2", 0),
		(try_for_agents, ":var_4"),
			(agent_is_alive, ":var_4"),
			(agent_get_troop_id, ":troop_id_var_4", ":var_4"),
			(neq, ":troop_id_var_4", "$g_talk_troop"),
			(eq, ":troop_id_var_4", "$2nd_sex_troop_id"),
			(assign, ":value_2", 1),
		(try_end),
		(eq, ":value_2", 1),
		(str_store_troop_name, 8, "$2nd_sex_troop_id")
	],
	"   - Come to my tent. we can try threesome with {s8}.", "man_ply_camp_three_some",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "man_ply_camp_three_some",
	[
		(store_random_in_range, ":random_in_range_0_2", 0, 2),
		(eq, ":random_in_range_0_2", 0)
	],
	"Sorry, My condition is too bad. ", "close_window",
	[]],

	[anyone, "man_ply_camp_three_some",
	[],
	" If you want, I can do.", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_troop_type_sett", "$2nd_sex_troop_id"),
		(try_begin),
			(gt, "$troop_gender_type", 10),
			(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_male_player_2girl_1man_threesome"),
		(else_try),
			(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_male_player_1girl_2man_threesome"),
		(try_end)
	]],

	[anyone|plyr, "member_talk",
	[
		(neg|is_between, "$g_talk_troop", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin"),
		(try_begin),
			(eq, "$g_talk_troop", "$player_spouse"),
			(assign, ":value", -30),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_01"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_08"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_12"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_15"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_18"),
			(assign, ":value", 20),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_04"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_05"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_06"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_09"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_13"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_17"),
			(assign, ":value", 40),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_02"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_03"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_10"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_11"),
			(assign, ":value", 70),
		(else_try),
			(assign, ":value", 60),
		(try_end),
		(val_add, ":value", 20),
		(ge, "$g_talk_troop_relation", ":value"),
		(store_current_scene, ":current_scene"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_desert"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_snow"),
		(eq, ":current_scene", "scn_conv_camp_sea"),
		(eq, "$talk_troop_gender", 1),
		(eq, "$adult_content", 1),
		(eq, "$attemp_commu", 0),
		(troop_slot_eq, "$g_talk_troop", slot_troop_last_comment_time, 74),
		(neq, "$g_talk_troop", "$2nd_sex_troop_id")
	],
	" -If i have tried threesome, you can do?", "man_ply_suggest_threesome",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "man_ply_suggest_threesome",
	[
		(store_random_in_range, ":random_in_range_0_2", 0, 2),
		(eq, ":random_in_range_0_2", 0)
	],
	"Threesome? No. I can't.", "close_window",
	[]],

	[anyone, "man_ply_suggest_threesome",
	[],
	"...If you want, i can.", "close_window",
	[
		(assign, "$2nd_sex_troop_id", "$g_talk_troop")
	]],

	[anyone|plyr, "member_talk",
	[
		(is_between, "$g_talk_troop", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin"),
		(store_current_scene, ":current_scene"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_desert"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_snow"),
		(eq, ":current_scene", "scn_conv_camp_sea"),
		(eq, "$player_gender", 0),
		(eq, "$talk_troop_gender", 1),
		(eq, "$adult_content", 1),
		(eq, "$attemp_commu", 0),
		(call_script, "script_party_money_level_ge", "p_main_party", 300),
		(eq, "$wm_mo_continue", 1)
	],
	" -Come to my tent. Have something to talk.", "qua_fuckchoose_tent",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "qua_fuckchoose_tent",
	[],
	"Fine. Prepare your wallet.", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_fuck_process_prosti")
	]],

	[anyone|plyr, "member_talk",
	[
		(store_current_scene, ":current_scene"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_desert"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_snow"),
		(eq, ":current_scene", "scn_conv_camp_sea"),
		(eq, "$talk_troop_gender", 0),
		(eq, "$player_gender", 1),
		(eq, "$adult_content", 1),
		(eq, "$attemp_commu", 0)
	],
	"  -Come to my tent. Have something to talk.", "fuck_camp_comp_for_girl_pre",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "fuck_camp_comp_for_girl_pre",
	[],
	"  I know what you're thinking.", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_fuck_process_normal")
	]],

	[anyone|plyr, "member_talk",
	[
		(store_current_scene, ":current_scene"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_desert"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_snow"),
		(eq, ":current_scene", "scn_conv_camp_sea"),
		(eq, "$talk_troop_gender", 0),
		(eq, "$player_gender", 1),
		(eq, "$adult_content", 1),
		(eq, "$attemp_commu", 0),
		(is_between, "$2nd_sex_troop_id", "trp_npc1", "trp_tt_lady_end"),
		(neq, "$g_talk_troop", "$2nd_sex_troop_id"),
		(assign, ":value", 0),
		(try_for_agents, ":var_3"),
			(agent_is_alive, ":var_3"),
			(agent_get_troop_id, ":troop_id_var_3", ":var_3"),
			(neq, ":troop_id_var_3", "$g_talk_troop"),
			(eq, ":troop_id_var_3", "$2nd_sex_troop_id"),
			(assign, ":value", 1),
		(try_end),
		(eq, ":value", 1),
		(str_store_troop_name, 8, "$2nd_sex_troop_id")
	],
	"   -Come to my tent. we can try threesome with {s8}.", "girl_ply_camp_three_some",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "girl_ply_camp_three_some",
	[],
	"I know what you're thinking.", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_troop_type_sett", "$2nd_sex_troop_id"),
		(try_begin),
			(gt, "$troop_gender_type", 10),
			(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_girl_player_2girl_1man_three_some"),
		(else_try),
			(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_girl_player_1girl_2man_three_some"),
		(try_end)
	]],

	[anyone|plyr, "member_talk",
	[
		(store_current_scene, ":current_scene"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_desert"),
		(this_or_next|eq, ":current_scene", "scn_conv_camp_snow"),
		(eq, ":current_scene", "scn_conv_camp_sea"),
		(eq, "$talk_troop_gender", 0),
		(eq, "$adult_content", 1),
		(eq, "$attemp_commu", 0),
		(neq, "$g_talk_troop", "$2nd_sex_troop_id")
	],
	"-If i have tried threesome, you can do?", "girl_ply_suggest_threesome",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "girl_ply_suggest_threesome",
	[],
	"Of course, why not?", "close_window",
	[
		(assign, "$2nd_sex_troop_id", "$g_talk_troop")
	]],

	[anyone|plyr, "member_talk",
	[
		(store_current_scene, ":current_scene"),
		(neq, ":current_scene", "scn_ex_bedroom"),
		(neq, "$g_talk_troop", "$g_sex_officer"),
		(call_script, "script_wm_main_party_has_troop_sc", "$g_talk_troop"),
		(eq, "$wm_comp_continue", 1),
		(eq, "$talk_troop_gender", 1),
		(eq, "$adult_content", 1),
		(neq, "$g_talk_troop", "$player_spouse")
	],
	"Give you a mission. You need have fuck with soldiers. to satisfy them.", "member_sexofficer_a",
	[]],

	[anyone, "member_sexofficer_a",
	[
		(is_between, "$g_talk_troop", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin")
	],
	"Okay. Okay. It is my mission. You must be command to soldiers. to them not become violent. I want to avoid being hurt...during fuck.", "member_talk",
	[
		(assign, "$g_sex_officer", "$g_talk_troop"),
		(assign, "$ass_agreed", 0),
		(str_clear, 33),
		(str_store_troop_name, 33, "$g_sex_officer"),
		(display_message, "str_sexofficername")
	]],

	[anyone, "member_sexofficer_a",
	[
		(try_begin),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_01"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_08"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_12"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_15"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_18"),
			(assign, ":value", 30),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_04"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_05"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_06"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_09"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_13"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_17"),
			(assign, ":value", 60),
		(else_try),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_02"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_03"),
			(this_or_next|eq, "$g_talk_troop", "trp_tt_lady_ex_10"),
			(eq, "$g_talk_troop", "trp_tt_lady_ex_11"),
			(assign, ":value", 100),
		(else_try),
			(assign, ":value", 100),
		(try_end),
		(ge, "$g_talk_troop_relation", ":value")
	],
	"You really want it, I can do that. You must be command to soldiers. to them not become violent. I want to avoid being hurt...during fuck.", "member_talk",
	[
		(assign, "$g_sex_officer", "$g_talk_troop"),
		(try_begin),
			(troop_slot_eq, "$g_sex_officer", slot_troop_last_persuasion_time, 1),
			(troop_set_slot, "$g_sex_officer", slot_troop_last_persuasion_time, 0),
			(display_message, "str_gbt_virgin", 0x00ff0000),
			(str_store_troop_name, 8, "$g_sex_officer"),
			(display_message, "str_gbt_virgin3", 0x00ff0000),
		(try_end),
		(assign, "$ass_agreed", 0),
		(str_clear, 33),
		(str_store_troop_name, 33, "$g_sex_officer"),
		(display_message, "str_sexofficername"),
		(try_begin),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_01"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -5),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_02"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -15),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_03"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -30),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_04"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -5),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_05"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -15),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_06"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -30),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_07"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -30),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_08"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -5),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_09"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -15),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_10"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -30),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_11"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -30),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_12"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -5),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_13"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -15),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_14"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -30),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_15"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -5),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_16"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -30),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_17"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -15),
		(else_try),
			(eq, "$g_sex_officer", "trp_tt_lady_ex_18"),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -5),
		(else_try),
			(call_script, "script_change_player_relation_with_troop", "$g_sex_officer", -30),
		(try_end)
	]],

	[anyone, "member_sexofficer_a",
	[],
	"No. I'm not. Why do you say that to me?", "member_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -10)
	]],

	[anyone|plyr, "member_talk",
	[
		(store_current_scene, ":current_scene"),
		(neq, ":current_scene", "scn_ex_bedroom"),
		(eq, "$g_talk_troop", "$g_sex_officer"),
		(neq, "$ass_agreed", 1),
		(eq, "$adult_content", 1)
	],
	"You are responsible for the morale of the soldiers. It is better to use the anus can handle a lot of men.", "member_ass_agree",
	[]],

	[anyone, "member_ass_agree",
	[],
	"Oh No! I do not use the anus.", "member_ass_agree_a",
	[]],

	[anyone|plyr, "member_ass_agree_a",
	[
		(call_script, "script_party_money_level_ge", "p_main_party", 1000),
		(eq, "$wm_mo_continue", 1)
	],
	"I'll give you money. Do you want it?", "member_ass_agree_b",
	[]],

	[anyone|plyr, "member_ass_agree_a",
	[],
	"Forget it if you do not want.", "member_talk",
	[]],

	[anyone, "member_ass_agree_b",
	[],
	"Okay. Okay. So now I'm twice as tired quickly.", "member_talk",
	[
		(assign, "$ass_agreed", 1),
		(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34),
		(display_message, "str_sexofficerass")
	]],

	[anyone|plyr, "member_talk",
	[
		(store_current_scene, ":current_scene"),
		(neq, ":current_scene", "scn_ex_bedroom"),
		(eq, "$g_talk_troop", "$g_sex_officer"),
		(eq, "$ass_agreed", 1)
	],
	"Now, do not allow anal sex. you'll shed a shit.", "member_ass_stops",
	[]],

	[anyone, "member_ass_stops",
	[],
	"I waited for you to say that.", "member_talk",
	[
		(assign, "$ass_agreed", 0)
	]],

	[anyone|plyr, "member_talk",
	[
		(store_current_scene, ":current_scene"),
		(neq, ":current_scene", "scn_ex_bedroom"),
		(eq, "$adult_content", 1),
		(eq, "$g_talk_troop", "$g_sex_officer")
	],
	"I need to see the status of your body.", "member_cunt_view",
	[]],

	[anyone, "member_cunt_view",
	[],
	"Hey. What are you doing now?", "member_cunt_mess_1",
	[
		(call_script, "script_molda_s_scene", 51, 0),
		(play_sound, "snd_womanscream02")
	]],

	[anyone, "member_cunt_mess_1",
	[
		(str_clear, 43)
	],
	"Vagina resilience : {reg43}/200. ^{s43}", "member_cunt_mess_2",
	[
		(call_script, "script_molda_s_scene", 51, 0)
	]],

	[anyone, "member_cunt_mess_2",
	[],
	"That's it?", "member_talk",
	[
		(call_script, "script_molda_s_scene", 52, 0)
	]],

	[anyone|plyr, "member_talk",
	[
		(neq, "$g_talk_troop", "$player_spouse"),
		(neg|is_between, "$g_talk_troop", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin"),
		(call_script, "script_wm_main_party_has_troop_sc", "$g_talk_troop"),
		(eq, "$wm_comp_continue", 1)
	],
	"We need to separate for a while.", "member_separate",
	[]],

	[anyone, "member_separate",
	[],
	"Oh really? Well, I'm not just going to wait around here. I'm going to go to the towns to look for work. Is that what you want?", "member_separate_confirm",
	[]],

	[anyone|plyr, "member_separate_confirm",
	[],
	"That's right. We need to part ways.", "member_separate_yes",
	[]],

	[anyone|plyr, "member_separate_confirm",
	[],
	"No, I'd rather have you at my side.", "do_member_trade",
	[]],

	[anyone, "member_separate_yes",
	[],
	"Well. I'll be off, then. Look me up if you need me.", "close_window",
	[
		(call_script, "script_wm_comp_separate", "$g_talk_troop")
	]],

	[anyone|plyr, "member_talk",
	[
		(eq, "$g_talk_troop", "$player_spouse"),
		(call_script, "script_wm_main_party_has_troop_sc", "$g_talk_troop"),
		(eq, "$wm_comp_continue", 1)
	],
	"This is unsafe for you. You should get back to our court.", "spouse_leave",
	[]],

	[anyone, "spouse_leave",
	[],
	"Are you sure, my love?", "spouse_leave_confirm",
	[]],

	[anyone|plyr, "spouse_leave_confirm",
	[],
	"Yes.", "close_window",
	[
		(call_script, "script_wm_comp_separate", "$g_talk_troop")
	]],

	[anyone|plyr, "spouse_leave_confirm",
	[],
	"No, I'd rather have you at my side.", "do_member_trade",
	[]],

	[anyone|plyr, "member_talk",
	[
		(is_between, "$g_talk_troop", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin"),
		(call_script, "script_wm_main_party_has_troop_sc", "$g_talk_troop"),
		(eq, "$wm_comp_continue", 1)
	],
	"This is unsafe for you. You should get back to your tavern.", "hore_leave",
	[]],

	[anyone, "hore_leave",
	[],
	"Are you sure?", "hore_leave_confirm",
	[]],

	[anyone|plyr, "hore_leave_confirm",
	[],
	"Yes.", "close_window",
	[
		(call_script, "script_wm_comp_separate", "$g_talk_troop")
	]],

	[anyone|plyr, "hore_leave_confirm",
	[],
	"No, I'd rather have you at my side.", "do_member_trade",
	[]],

	[anyone|plyr, "member_talk",
	[],
	"Never mind.", "close_window",
	[]],

	[anyone|plyr, "prostitute_talk",
	[
		(call_script, "script_party_money_level_ge", "p_main_party", 1000),
		(eq, "$wm_mo_continue", 1),
		(neg|is_between, "$wm_comp_id_1", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin"),
		(neg|is_between, "$wm_comp_id_2", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin"),
		(neg|is_between, "$wm_comp_id_3", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin"),
		(neg|is_between, "$wm_comp_id_4", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin"),
		(neg|is_between, "$wm_comp_id_5", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin"),
		(neg|is_between, "$wm_comp_id_standby", "trp_prostitute_1", "trp_kingdom_heroes_including_player_begin")
	],
	"I give you 1000 denars. Please to serve for our troops.", "prostitute_join",
	[]],

	[anyone, "prostitute_join",
	[],
	"Of course my lord!", "close_window",
	[
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop"),
		(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34)
	]],

	[anyone|plyr, "prostitute_talk",
	[
		(call_script, "script_party_money_level_ge", "p_main_party", 100),
		(eq, "$wm_mo_continue", 1),
		(eq, "$adult_content", 1)
	],
	"I'll give you the money. Blow job for me.", "prostitute_blow_job_1",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 100, 34)
	]],

	[anyone, "prostitute_blow_job_1",
	[],
	".........", "prostitute_blow_job_1_2",
	[
		(call_script, "script_molda_s_scene", 111, 0)
	]],

	[anyone, "prostitute_blow_job_1_2",
	[],
	".........", "prostitute_blow_job_2",
	[
		(call_script, "script_molda_s_scene", 111, 0)
	]],

	[anyone|plyr, "prostitute_blow_job_2",
	[],
	" [Squirt cum on the face]", "prostitute_blow_job_3_face",
	[]],

	[anyone|plyr, "prostitute_blow_job_2",
	[],
	" [Squirt cum in mouth]", "prostitute_blow_job_3_mouth",
	[]],

	[anyone, "prostitute_blow_job_3_face",
	[],
	"  Uhh. So you happy now?", "prostitute_talk",
	[
		(call_script, "script_molda_s_scene", 112, 0)
	]],

	[anyone, "prostitute_blow_job_3_mouth",
	[],
	"  Uhh....taste. So you happy now?", "prostitute_talk",
	[
		(call_script, "script_molda_s_scene", 113, 0)
	]],

	[anyone|plyr, "prostitute_talk",
	[
		(eq, "$player_gender", 0),
		(call_script, "script_party_money_level_ge", "p_main_party", 300),
		(eq, "$wm_mo_continue", 1),
		(eq, "$adult_content", 1)
	],
	"Let's play with me.", "qua_fuckchoose",
	[]],

	[anyone|plyr, "prostitute_talk",
	[
		(eq, "$adult_content", 1)
	],
	"Dance for me.", "qua_dance_q",
	[
		(assign, "$h_dancer_strip", 0)
	]],

	[anyone, "qua_fuckchoose",
	[],
	"Are you sure have enough money?", "qua_fuckchoose_style",
	[]],

	[anyone|plyr, "qua_fuckchoose_style",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 200, 34)
	],
	"(Pay 200 denars.) Open your groin. bitch!", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_fuck_process_prosti")
	]],

	[anyone|plyr, "qua_fuckchoose_style",
	[],
	"No. I cannot.", "close_window",
	[]],

	[anyone|plyr, "prostitute_talk",
	[],
	"I'm not interested. Farewell", "close_window",
	[]],

	[anyone|plyr, "standby_talk",
	[
		(this_or_next|eq, "$wm_comp_id_1", -1),
		(this_or_next|eq, "$wm_comp_id_2", -1),
		(this_or_next|eq, "$wm_comp_id_3", -1),
		(this_or_next|eq, "$wm_comp_id_4", -1),
		(eq, "$wm_comp_id_5", -1)
	],
	"Now you can join. welcome.", "standby_join",
	[]],

	[anyone, "standby_join",
	[],
	"Good.", "close_window",
	[
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "standby_talk",
	[],
	"All right, Please wait.", "close_window",
	[]],

	[anyone|plyr, "tavernkeeper_talk",
	[
		(eq, "$main_q_step", 75)
	],
	"Do you know about this symbol? [shows sword]", "mq_75_1",
	[]],

	[anyone, "mq_75_1",
	[
		(lt, "$comp_rel_passsss", 2),
		(party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 6)
	],
	"Oh, my God! This is symbol of hashashin! Why do you ask me this?", "mq_75_2",
	[]],

	[anyone, "mq_75_2",
	[],
	"No! They already know it! Run for your life!!", "close_window",
	[
		(assign, "$main_q_step", 76),
		(assign, "$main_q_day", 0)
	]],

	[anyone, "mq_75_1",
	[
		(party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 6)
	],
	"Are you gonna kill me? Get out of here! ", "close_window",
	[]],

	[anyone, "mq_75_1",
	[],
	"I don't know about that. in my opinion, arab peoples will know better than me about arab style sword.", "tavernkeeper_talk",
	[]],

	[anyone|plyr, "tavernkeeper_talk",
	[
		(eq, "$main_q_step", 1),
		(party_slot_eq, "$g_encountered_party", slot_town_center, "$kingdom_pick_start_faction")
	],
	"Hey. I know you. You lived next door to us.", "mq_1_1",
	[]],

	[anyone, "mq_1_1",
	[],
	"{playername}!!! oh my god! Never thought I'd see you!", "mq_1_2",
	[]],

	[anyone|plyr, "mq_1_2",
	[],
	"when i came back, our village has been already destroyed. There was nobody about.", "mq_1_3",
	[]],

	[anyone, "mq_1_3",
	[],
	"When all of the young man left the village,  our people was imprisoned by slave traders. They were waiting for a chance. We were being sold to the enemy , including your sister.", "mq_1_4",
	[]],

	[anyone|plyr, "mq_1_4",
	[],
	"What? how you came back here? where is my sister?", "mq_1_5",
	[]],

	[anyone, "mq_1_5",
	[
		(assign, "$main_q_party", 0),
		(try_for_range, ":party", "p_pyongyang", "p_place_end"),
			(store_faction_of_party, ":faction_of_party_party", ":party"),
			(eq, ":faction_of_party_party", "$start_enemy_fac"),
			(try_begin),
				(eq, "$main_q_party", 0),
				(assign, "$main_q_party", ":party"),
			(else_try),
				(store_random_in_range, ":random_in_range_0_5", 0, 5),
				(eq, ":random_in_range_0_5", 0),
				(assign, "$main_q_party", ":party"),
			(try_end),
		(try_end),
		(try_begin),
			(eq, "$main_q_party", 0),
			(try_for_range, ":party", "p_pyongyang", "p_place_end"),
				(party_slot_eq, ":party", slot_town_center, "$start_enemy_fac"),
				(try_begin),
					(eq, "$main_q_party", 0),
					(assign, "$main_q_party", ":party"),
				(else_try),
					(store_random_in_range, ":random_in_range_0_5", 0, 5),
					(eq, ":random_in_range_0_5", 0),
					(assign, "$main_q_party", ":party"),
				(try_end),
			(try_end),
		(try_end),
		(is_between, "$main_q_party", "p_pyongyang", "p_place_end"),
		(str_store_faction_name, 13, "$start_enemy_fac"),
		(str_store_party_name, 12, "$main_q_party")
	],
	"they usually sold slaves to town of {s13}. perhaps it is {s12}. {s12} is dangerous to you. you should be talk with lords of our country. he will help us.", "mq_1_6",
	[]],

	[anyone, "mq_1_5",
	[],
	"Sorry. I don't know. really. (main quest check fail)", "close_window",
	[]],

	[anyone|plyr, "mq_1_6",
	[],
	"Right. this job is need assistance of army. ", "close_window",
	[
		(assign, "$main_q_step", 2)
	]],

	[anyone|plyr, "tavernkeeper_talk",
	[
		(eq, "$qquest_type", 0),
		(party_slot_ge, "$g_encountered_party", 23, 1),
		(neg|party_slot_ge, "$g_encountered_party", 23, 3)
	],
	"Do you happen to have a job for me?", "tavernkeeper_quest",
	[]],

	[anyone|plyr, "tavernkeeper_talk",
	[
		(gt, "$qquest_type", 0),
		(eq, "$qquest_report_party", "$g_encountered_party"),
		(neq, "$qquest_progress", 1)
	],
	"Sorry. Please cancel the contract.", "tavernkeeper_quest_cancel",
	[]],

	[anyone, "tavernkeeper_quest_cancel",
	[],
	"Okay, then. It can't be helped. I'll find someone else.", "close_window",
	[
		(call_script, "script_qquest_initialize"),
		(play_sound, "snd_bad_drum"),
		(display_message, "str_questcancel")
	]],

	[anyone|plyr, "tavernkeeper_talk",
	[
		(eq, "$qquest_type", 1),
		(eq, "$qquest_target_party", "$g_encountered_party")
	],
	"I'm here to deliver alcohol.", "tavernkeeper_alcohol_end",
	[]],

	[anyone, "tavernkeeper_alcohol_end",
	[],
	"I was waiting for.. Well done!", "close_window",
	[
		(store_add, ":value", 1000, 1000),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
		(call_script, "script_qquest_initialize"),
		(play_sound, "snd_experience_gained"),
		(display_message, "str_questcomp"),
		(call_script, "script_town_relation_diff", "$g_encountered_party", 1)
	]],

	[anyone|plyr, "tavernkeeper_talk",
	[
		(eq, "$qquest_type", 2),
		(eq, "$qquest_report_party", "$g_encountered_party"),
		(eq, "$qquest_progress", 1),
		(str_store_party_name, 4, "$qquest_target_party")
	],
	"I found fugitive hiding at {s4} and gave him his punishment.", "tavernkeeper_headhunt_end",
	[]],

	[anyone, "tavernkeeper_headhunt_end",
	[],
	"Let me take the money, Thank you.", "close_window",
	[
		(store_add, ":value", 1000, 1000),
		(val_add, ":value", 500),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
		(call_script, "script_qquest_initialize"),
		(play_sound, "snd_experience_gained"),
		(call_script, "script_town_relation_diff", "$g_encountered_party", 1),
		(display_message, "str_questcomp")
	]],

	[anyone|plyr, "tavernkeeper_talk",
	[
		(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
		(gt, ":party_size_wo_prisoners_main_party", 2000),
		(eq, "$wm_buying_drink_for_army", 0)
	],
	"I'd like to buy me and my men a barrel of your best Alcohol.", "tavernkeeper_buy_drinks_troops",
	[]],

	[anyone, "tavernkeeper_buy_drinks_troops",
	[
		(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
		(store_div, "$temp", ":party_size_wo_prisoners_main_party", 10),
		(assign, reg5, "$temp"),
		(call_script, "script_party_money_level_ge", "p_main_party", "$temp")
	],
	"Of course, {my lord/my lady}. I reckon {reg5} denar should be enough for that. What should I tell the lads?", "tavernkeeper_buy_drinks_troops_2",
	[]],

	[anyone|plyr, "tavernkeeper_buy_drinks_troops_2",
	[
		(eq, "$wm_mo_continue", 1)
	],
	"The price is fair enough, let my men have at it.", "tavernkeeper_buy_drinks_troops_end",
	[
		(assign, "$wm_buying_drink_for_army", 72),
		(assign, reg9, "$wm_buying_drink_for_army"),
		(display_message, "str_tavern_cool_add", 0x00ffff00),
		(call_script, "script_party_money_level_diff", "p_main_party", "$temp", 34)
	]],

	[anyone, "tavernkeeper_buy_drinks_troops_end",
	[],
	"Don't worry {sir/madam}. Your men will enjoy their pints.", "tavernkeeper_pretalk",
	[
		(call_script, "script_moral_level_diff", "p_main_party", 10),
		(play_sound, "snd_man_victory")
	]],

	[anyone|plyr, "tavernkeeper_buy_drinks_troops_2",
	[],
	"Actually, cancel that order.", "tavernkeeper_pretalk",
	[]],

#####		##plus
#####  #blackjack
#####  ###Begin Blackjack
#####  [anyone|plyr,"tavernkeeper_talk",
#####   [],
#####   #"Play 'Blackjack'", "tavernkeeper_blackjack_1",[]],
#####   "Lets play Blackjack", "tavernkeeper_blackjack_1",[]],
#####  [anyone,"tavernkeeper_blackjack_1",
#####   [],
#####   #"What do you want?", "tavernkeeper_blackjack_2",[]],
#####   "Sure, I got some spare time.", "tavernkeeper_blackjack_2",[]],
#####  [anyone|plyr,"tavernkeeper_blackjack_2",
#####   [],
#####   "Start playing.", "tavernkeeper_blackjack_3",[]],
#####  [anyone,"tavernkeeper_blackjack_3",
#####   [
#####    (store_troop_gold,reg1,"trp_player"),#
#####    (ge,reg1,1),#
#####       ],
#####   "Ok.", "close_window",[
#####    (assign, "$black_jack",1),
#####    (assign, reg50, 0),#ßª
#####    (start_presentation, "prsnt_blackjack"),
#####    ]],
#####  [anyone,"tavernkeeper_blackjack_3",[],
#####   "You don't have enough money.", "tavernkeeper_blackjack_1",[]],
#####
#####  [anyone|plyr,"tavernkeeper_blackjack_2",
#####   [],
#####   "View Rules.", "tavernkeeper_blackjack_4",[]],
#####  [anyone,"tavernkeeper_blackjack_4",
#####   [],
#####   ####BlackJack Rules
#####   "The aim of the game is to accumulate a higher point total than the dealer, but without going over 21. You compute your score by adding the values of your individual cards, The cards 2 through 10 have their face value, J, Q, and K are worth 10 points each, and the Ace is worth either 1 or 11 points (player's choice). At the start of a blackjack game, the players and the dealer receive two cards each. The players' cards are normally dealt face up, while the dealer has one face down (called the hole card) and one face up. The best possible blackjack hand is an opening deal of an ace with any ten-point card. This is called a *blackjack*, or a natural 21, and the player holding this automatically wins unless the dealer also has a blackjack.", "tavernkeeper_blackjack_5",[]],
#####  [anyone,"tavernkeeper_blackjack_5",
#####   [],
#####   "The player can keep his hand as it is (stand) or take more cards from the deck (hit), one at a time, until either the player judges that the hand is strong enough to go up against the dealer's hand and stands, or until it goes over 21, in which case the player immediately loses (busts). Players can take as many cards as they like, as long as they don't bust, when all players have finished their actions, either decided to stand or busted, the dealer turns over his hidden hole card, If the dealer has a natural 21 (blackjack) with his two cards, he won't take any more cards. All players lose, except players who also have a blackjack, in which case it is a push - the bet is returned to the player.", "tavernkeeper_blackjack_1",[]],   
#####   #" Contrary to the player, though, the dealer's action is completely dictated by the rules. The dealer must hit if the value of the hand is lower than 17, otherwise the dealer will stand. If the dealer goes bust, all players who are left in the game win. Otherwise players with higher point totals than the dealer win, while players with lower totals than the dealer lose. For those with the same total as the dealer the result is a push: their stake is returned to them and they neither win nor lose. Players with a blackjack win a bet plus a bonus amount, which is normally equal to half their original wager. A blackjack hand beats any other hand, also those with a total value of 21 but with more cards. As described above, if the dealer has a blackjack, players with blackjack make a push, while all other players lose. ", "tavernkeeper_blackjack_1",[]],   
######   "At the start of a blackjack game, the players and the dealer receive two cards each. The players' cards are normally dealt face up, while the dealer has one face down (called the hole card) and one face up. The best possible blackjack hand is an opening deal of an ace with any ten-point card. This is called a *blackjack*, or a natural 21, and the player holding this automatically wins unless the dealer also has a blackjack. If a player and the dealer each have a blackjack, the result is a push for that player. If the dealer has a blackjack, all players not holding a blackjack lose.", "tavernkeeper_blackjack_1",[]],
#####   ###End blackjack rules
#####  [anyone|plyr,"tavernkeeper_blackjack_2",
#####   [],
#####   "Go back.", "tavernkeeper_pretalk",[]],
####### end plus
########End Blackjack
#####	### Three Cards ### Find the Lady ###
#####  [anyone|plyr,"tavernkeeper_talk",
#####   [],
#####   "Care to play 'Find the Lady?'", "tavern_tk_3cards",[]],
#####   
#####  [anyone,"tavern_tk_3cards",
#####   [
#####    (store_troop_gold,reg1,"trp_player"),#
#####    (ge,reg1,1),#
#####       ],
#####   "Ok. The rules are as simple as this: Find the Lady - you win , if not - you lose.", "close_window",
#####   [(assign, reg50, 0),
#####    (start_presentation, "prsnt_three_card"),]],
#####	
#####  [anyone,"tavern_tk_3cards",[],
#####   "You don't have enough money.", "close_window",[]],
#####
######## Three Cards ### Find the Lady ### END ###
######## Dice game ### Dice game ###
#####  [anyone|plyr,"tavernkeeper_talk",
#####   [],
#####   "Want to play a game of Dice?", "tavern_tk_dgame",[]],
#####   
#####  [anyone,"tavern_tk_dgame",
#####   [
#####    (store_troop_gold,reg1,"trp_player"),#
#####    (ge,reg1,1),#
#####       ],
#####   "Yes, lets play.", "close_window",
#####   [(assign, reg50, 0),
#####    (assign,"$g_gamble",0),
#####    (start_presentation, "prsnt_dices_game"),]],
#####	
#####  [anyone,"tavern_tk_3cards",[],
#####   "You don't have enough denars.", "close_window",[]],   
######## Dice game ### Dice game ### END ###
#####
#########Begin flip Coin OSP https://forums.taleworlds.com/index.php/topic,176440.0.html
#####  [anyone|plyr,"tavernkeeper_talk", [
#####      (store_current_hours,":cur_hours"),
#####      (val_sub, ":cur_hours", 6),
#####      (gt, ":cur_hours", "$gamble_last_time"),
#####      ], "I'd like to flip a coin with you.", "tavernkeeper_coin",[]],
#####
#####  [anyone,"tavernkeeper_coin", [
#####      ], "Alright. How much money do you want to lose?", "tavernkeeper_coin2",[]],
#####
#####  [anyone|plyr,"tavernkeeper_coin2", [
#####      (store_troop_gold, ":gold", "trp_player"),
#####      (ge,":gold",50),
#####      ], "50 Denars.", "tavernkeeper_coin3",[
#####          (assign, reg6, 50),]],
#####  [anyone|plyr,"tavernkeeper_coin2", [
#####      (store_troop_gold, ":gold", "trp_player"),
#####      (ge,":gold",100),
#####      ], "100 Denars.", "tavernkeeper_coin3",[
#####          (assign, reg6, 100),]],
#####  [anyone|plyr,"tavernkeeper_coin2", [
#####      (store_troop_gold, ":gold", "trp_player"),
#####      (ge,":gold",200),
#####      ], "200 Denars.", "tavernkeeper_coin3",[
#####          (assign, reg6, 200),]],
#####  [anyone|plyr,"tavernkeeper_coin2", [
#####      (store_troop_gold, ":gold", "trp_player"),
#####      (ge,":gold",500),
#####      ], "500 Denars.", "tavernkeeper_coin3",[
#####          (assign, reg6, 500),]],
#####  [anyone|plyr,"tavernkeeper_coin2", [
#####      (store_troop_gold, ":gold", "trp_player"),
#####      (ge,":gold",1000),
#####      ], "1000 Denars.", "tavernkeeper_coin3",[
#####          (assign, reg6, 1000),]],
#####  [anyone|plyr,"tavernkeeper_coin2", [
#####      (store_troop_gold, ":gold", "trp_player"),
#####      (ge,":gold",2000),
#####      ], "20000 Denars.", "tavernkeeper_coin3",[
#####          (assign, reg6, 2000),]],
#####  [anyone|plyr,"tavernkeeper_coin2", [
#####      ], "I can't afford it.", "tavernkeeper_coinn",[]],
#####
#####  [anyone,"tavernkeeper_coinn", [
#####      ], "Nevermind.", "tavernkeeper_talk",[]],
#####
#####  [anyone,"tavernkeeper_coin3", [
#####      ], "Okay. Head or tail?", "tavernkeeper_coin4",[]],
#####
#####  [anyone|plyr,"tavernkeeper_coin4", [
#####      ], "Head.", "tavernkeeper_coin5",[
#####          (str_store_string, s2, "@head"),
#####          (str_store_string, s3, "@tail"),]],
#####  [anyone|plyr,"tavernkeeper_coin4", [
#####      ], "Tail.", "tavernkeeper_coin5",[
#####          (str_store_string, s2, "@tail"),
#####          (str_store_string, s3, "@head"),]],
#####
#####  [anyone,"tavernkeeper_coin5", [
#####      ], "Well, here we go... (He flips the coin.)", "tavernkeeper_coin6",[
#####        (store_random_in_range, "$rand2", 0, 2),]],
#####
#####  [anyone,"tavernkeeper_coin6", [
#####       (eq,"$rand2",0),
#####      ], "Look, it's {s3}! Bad luck for you.", "tavernkeeper_coin6a",[]],
#####  [anyone,"tavernkeeper_coin6", [
#####       (eq,"$rand2",1),
#####      ], "Damn, it's {s2}... Here's your money.", "tavernkeeper_pretalk",[
#####          (troop_add_gold,"trp_player",reg6),
#####          (store_current_hours,":cur_hours"),
#####          (assign, "$gamble_last_time", ":cur_hours"),]],
#####
#####  [anyone|plyr,"tavernkeeper_coin6a", [
#####      ], "Here are your {reg6} Denars.", "tavernkeeper_pretalk",[
#####       (troop_remove_gold,"trp_player",reg6),
#####       (store_current_hours,":cur_hours"),
#####       (assign, "$gamble_last_time", ":cur_hours"),]],
#####
#########End flip coin OSP
	
	[anyone|plyr, "tavernkeeper_talk",
	[],
	"I guess I should leave now.", "close_window",
	[]],

	[anyone, "tavernkeeper_pretalk",
	[],
	"Anything else?", "tavernkeeper_talk",
	[]],

	[anyone|plyr, "walker_talk",
	[
		(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
		(eq, ":faction_of_party_g_encountered_party", "$main_q_faction"),
		(eq, "$main_q_step", 4)
	],
	"Do you know about the famous slave traders in this place?", "walker_mq_4_1",
	[]],

	[anyone, "walker_mq_4_1",
	[
		(gt, "$main_q_troop", 0)
	],
	"No. I never heard anything about that.", "close_window",
	[
		(try_begin),
			(neq, "$main_q_party", "$g_talk_agent"),
			(val_sub, "$main_q_troop", 1),
			(assign, "$main_q_party", "$g_talk_agent"),
		(try_end)
	]],

	[anyone, "walker_mq_4_1",
	[
		(assign, "$main_q_party", 0),
		(try_for_range, ":party", "p_pyongyang", "p_place_end"),
			(store_faction_of_party, ":faction_of_party_party", ":party"),
			(eq, ":faction_of_party_party", "$main_q_faction"),
			(try_begin),
				(eq, "$main_q_party", 0),
				(assign, "$main_q_party", ":party"),
			(else_try),
				(store_random_in_range, ":random_in_range_0_3", 0, 3),
				(eq, ":random_in_range_0_3", 0),
				(assign, "$main_q_party", ":party"),
			(try_end),
		(try_end),
		(try_begin),
			(eq, "$main_q_party", 0),
			(try_for_range, ":party", "p_pyongyang", "p_place_end"),
				(party_slot_eq, ":party", slot_town_center, "$main_q_party"),
				(try_begin),
					(eq, "$main_q_party", 0),
					(assign, "$main_q_party", ":party"),
				(else_try),
					(store_random_in_range, ":random_in_range_0_3", 0, 3),
					(eq, ":random_in_range_0_3", 0),
					(assign, "$main_q_party", ":party"),
				(try_end),
			(try_end),
		(try_end),
		(is_between, "$main_q_party", "p_pyongyang", "p_place_end"),
		(str_store_party_name, 12, "$main_q_party")
	],
	"Yes, i heard about that in {s12}. Ransom broker of the {s12} has known about it.", "walker_mq_4_2",
	[]],

	[anyone|plyr, "walker_mq_4_2",
	[],
	"I really appreciate that.", "close_window",
	[
		(assign, "$main_q_step", 5)
	]],

	[anyone, "walker_mq_4_1",
	[],
	" Sorry. I don't know. really. (main quest check fail)", "close_window",
	[]],

	[anyone|plyr, "walker_talk",
	[
		(eq, "$wm_quest_mission_anti_skip_menu", 1),
		(party_slot_eq, "$g_encountered_party", 15, 4),
		(eq, "$talk_troop_gender", 1)
	],
	"[Try kidnap] Mayor had looking for you. he was waiting in the woods.", "try_to_kidnap_sys",
	[]],

	[anyone, "try_to_kidnap_sys",
	[],
	"What? but...why?", "try_to_kidnap_sys_persue",
	[]],

	[anyone|plyr, "try_to_kidnap_sys_persue",
	[],
	"[Try persuasion] He talking about the your taxes.", "try_to_kidnap_sys_conclud",
	[]],

	[anyone|plyr, "try_to_kidnap_sys_persue",
	[],
	"Never mind.", "close_window",
	[]],

	[anyone, "try_to_kidnap_sys_conclud",
	[
		(store_random_in_range, ":random_in_range_0_10", 0, 10),
		(troop_get_slot, ":player_betrothal_time", "trp_player", slot_troop_betrothal_time),
		(val_add, ":random_in_range_0_10", ":player_betrothal_time"),
		(ge, ":random_in_range_0_10", 7)
	],
	"[Persuasion success] Really? I think we need going immediately.", "close_window",
	[
		(display_message, "str_kidnap_three", 0x00ffff00),
		(assign, "$wm_quest_result", 1),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_quest_menu")
	]],

	[anyone, "try_to_kidnap_sys_conclud",
	[],
	"[Persuasion fail] It cannot. You are lying.", "close_window",
	[
		(assign, "$wm_quest_result", 2),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_quest_menu")
	]],

	[anyone|plyr, "walker_talk",
	[
		(eq, "$adult_content", 1),
		(eq, "$player_gender", 0),
		(eq, "$talk_troop_gender", 1),
		(neq, "$last_talk_agent", "$g_talk_agent")
	],
	"Hey, listen. i have a good suggestion for you.", "walker_try_prosti_1",
	[]],

	[anyone, "walker_try_prosti_1",
	[],
	"Suggestion? what kind?", "walker_try_prosti_2",
	[]],

	[anyone|plyr, "walker_try_prosti_2",
	[
		(call_script, "script_party_money_level_ge", "p_main_party", 300),
		(eq, "$wm_mo_continue", 1)
	],
	"Suck my dick. and i'll give 300d to you.", "walker_try_prosti_blowjob_1",
	[]],

	[anyone, "walker_try_prosti_blowjob_1",
	[
		(store_random_in_range, ":random_in_range_0_4", 0, 4),
		(eq, ":random_in_range_0_4", 0)
	],
	"I...I... give me the money. right now.", "walker_try_prosti_blowjob_2",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 300, 34)
	]],

	[anyone, "walker_try_prosti_blowjob_2",
	[
		(agent_equip_item, "$g_talk_agent", 1399),
		(agent_set_stand_animation, "$g_talk_agent", "anim_blow_job"),
		(play_sound, "snd_blowjobbb")
	],
	".....", "walker_try_prosti_blowjob_3",
	[]],

	[anyone, "walker_try_prosti_blowjob_3",
	[
		(agent_equip_item, "$g_talk_agent", 1399),
		(agent_set_stand_animation, "$g_talk_agent", "anim_blow_job"),
		(play_sound, "snd_blowjobbb")
	],
	".....", "walker_try_prosti_blowjob_4",
	[]],

	[anyone|plyr, "walker_try_prosti_blowjob_4",
	[],
	"  [Squirt cum on the face]", "walker_try_prosti_blowjob_5",
	[
		(store_random_in_range, ":random_in_range_0_2", 0, 2),
		(try_begin),
			(eq, ":random_in_range_0_2", 0),
			(agent_equip_item, "$g_talk_agent", 1468),
		(else_try),
			(agent_equip_item, "$g_talk_agent", 1469),
		(try_end),
		(stop_all_sounds, 0),
		(play_sound, "snd_mansatis"),
		(agent_set_stand_animation, "$g_talk_agent", "anim_stand_lady"),
		(val_add, "$Sex_num_blow", 1)
	]],

	[anyone|plyr, "walker_try_prosti_blowjob_4",
	[],
	"  [Squirt cum in mouth]", "walker_try_prosti_blowjob_5",
	[
		(agent_equip_item, "$g_talk_agent", 1470),
		(stop_all_sounds, 0),
		(play_sound, "snd_swalloww"),
		(agent_set_stand_animation, "$g_talk_agent", "anim_stand_lady"),
		(val_add, "$Sex_num_blow", 1)
	]],

	[anyone, "walker_try_prosti_blowjob_5",
	[],
	"   Uhh. Shitty taste. So you happy now?", "walker_talk",
	[]],

	[anyone, "walker_try_prosti_blowjob_1",
	[],
	"Get out my sight. freak.", "close_window",
	[
		(assign, "$last_talk_agent", "$g_talk_agent")
	]],

	[anyone|plyr, "walker_try_prosti_2",
	[
		(call_script, "script_party_money_level_ge", "p_main_party", 1000),
		(eq, "$wm_mo_continue", 1)
	],
	"Follow me. i'll give 1000d to you.", "walker_try_prosti_fuck_1",
	[]],

	[anyone, "walker_try_prosti_fuck_1",
	[
		(store_random_in_range, ":random_in_range_0_4", 0, 4),
		(eq, ":random_in_range_0_4", 0)
	],
	"I...I... give me the money. right now.", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_male_p_fuck_civil_trade")
	]],

	[anyone, "walker_try_prosti_fuck_1",
	[],
	"Get out my sight. freak.", "close_window",
	[
		(assign, "$last_talk_agent", "$g_talk_agent")
	]],

	[anyone|plyr, "walker_try_prosti_2",
	[],
	"Never mind.", "close_window",
	[]],

	[anyone|plyr, "walker_talk",
	[
		(eq, "$adult_content", 1),
		(eq, "$player_gender", 1),
		(eq, "$talk_troop_gender", 0),
		(neq, "$last_talk_agent", "$g_talk_agent")
	],
	"Hey, handsome. i have a good suggestion for you.", "walker_fem_pl_prosti_1",
	[]],

	[anyone, "walker_fem_pl_prosti_1",
	[],
	"Suggestion? what kind?", "walker_fem_pl_prosti_2",
	[]],

	[anyone|plyr, "walker_fem_pl_prosti_2",
	[],
	"I'll give you blowjob. just pay to me 5 denar.", "walker_fem_pl_prosti_blow_job_1",
	[]],

	[anyone, "walker_fem_pl_prosti_blow_job_1",
	[
		(store_random_in_range, ":random_in_range_0_2", 0, 2),
		(eq, ":random_in_range_0_2", 0)
	],
	"5 denar? good. suck my dick!", "walker_fem_pl_prosti_blow_job_2",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 5, 87)
	]],

	[anyone|plyr, "walker_fem_pl_prosti_blow_job_2",
	[
		(call_script, "script_molda_s_scene", 211, 0)
	],
	".....", "walker_fem_pl_prosti_blow_job_3",
	[]],

	[anyone|plyr, "walker_fem_pl_prosti_blow_job_3",
	[
		(call_script, "script_molda_s_scene", 211, 0)
	],
	".....", "walker_fem_pl_prosti_blow_job_4",
	[]],

	[anyone, "walker_fem_pl_prosti_blow_job_4",
	[],
	"   Uhh!", "walker_fem_pl_prosti_blow_job_5",
	[
		(store_random_in_range, ":random_in_range_212_214", 212, 214),
		(call_script, "script_molda_s_scene", ":random_in_range_212_214", 0)
	]],

	[anyone|plyr, "walker_fem_pl_prosti_blow_job_5",
	[],
	"    Uhh. Shitty taste. So you happy now?", "walker_talk",
	[]],

	[anyone, "walker_fem_pl_prosti_blow_job_1",
	[],
	"Dirty whore. I have no interest in it.", "close_window",
	[
		(assign, "$last_talk_agent", "$g_talk_agent")
	]],

	[anyone|plyr, "walker_fem_pl_prosti_2",
	[],
	"Follow me. I'll give to you pleasure. just pay to me 10 denar.", "walker_fem_pl_try_prosti_fuck_1",
	[]],

	[anyone, "walker_fem_pl_try_prosti_fuck_1",
	[
		(store_random_in_range, ":random_in_range_0_2", 0, 2),
		(eq, ":random_in_range_0_2", 0)
	],
	"Are there any good places? Please guide me.", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_female_p_fuck_civil_prosti")
	]],

	[anyone, "walker_fem_pl_try_prosti_fuck_1",
	[],
	"Get out my sight.", "close_window",
	[
		(assign, "$last_talk_agent", "$g_talk_agent")
	]],

	[anyone|plyr, "walker_fem_pl_prosti_2",
	[],
	"Never mind.", "close_window",
	[]],

	[anyone|plyr, "walker_talk",
	[
		(is_between, "$g_encountered_party", "p_pyongyang", "p_place_end")
	],
	"Are there any rumors about your town owner?", "walker_talk_rumor",
	[]],

	[anyone, "walker_talk_rumor",
	[
		(party_get_slot, ":g_encountered_party_town_tavern", "$g_encountered_party", slot_town_tavern),
		(troop_get_slot, ":g_encountered_party_town_tavern_player_order_object", ":g_encountered_party_town_tavern", slot_troop_player_order_object),
		(str_store_troop_name, 6, ":g_encountered_party_town_tavern"),
		(store_random_in_range, ":random_in_range_0_3", 0, 3),
		(try_begin),
			(neg|is_between, ":g_encountered_party_town_tavern", "trp_tt_lord_01_00", "trp_tt_lord_end"),
			(store_random_in_range, ":random_in_range_walker_rumor_01_walker_rumor_end", "str_walker_rumor_01", "str_walker_rumor_end"),
		(else_try),
			(gt, ":random_in_range_0_3", 0),
			(store_random_in_range, ":random_in_range_walker_rumor_01_walker_rumor_end", "str_walker_rumor_01", "str_walker_rumor_end"),
		(else_try),
			(eq, ":g_encountered_party_town_tavern_player_order_object", 1),
			(assign, ":random_in_range_walker_rumor_01_walker_rumor_end", "str_gossip_about_character_martial"),
		(else_try),
			(eq, ":g_encountered_party_town_tavern_player_order_object", 2),
			(assign, ":random_in_range_walker_rumor_01_walker_rumor_end", "str_gossip_about_character_goodnatured"),
		(else_try),
			(eq, ":g_encountered_party_town_tavern_player_order_object", 3),
			(assign, ":random_in_range_walker_rumor_01_walker_rumor_end", "str_gossip_about_character_selfrighteous"),
		(else_try),
			(eq, ":g_encountered_party_town_tavern_player_order_object", 4),
			(assign, ":random_in_range_walker_rumor_01_walker_rumor_end", "str_gossip_about_character_upstanding"),
		(else_try),
			(eq, ":g_encountered_party_town_tavern_player_order_object", 5),
			(assign, ":random_in_range_walker_rumor_01_walker_rumor_end", "str_gossip_about_character_cunning"),
		(else_try),
			(assign, ":random_in_range_walker_rumor_01_walker_rumor_end", "str_gossip_about_character_default"),
		(try_end),
		(str_store_string, 43, ":random_in_range_walker_rumor_01_walker_rumor_end")
	],
	"{s43}", "walker_talk",
	[]],

	[anyone|plyr, "walker_talk",
	[],
	"Never mind.", "close_window",
	[]],

	[anyone|plyr, "goods_merchant_talk",
	[
		(eq, "$wm_steal_try", 0)
	],
	"[Try Pickpocket]", "try_to_steal_sys",
	[]],

	[anyone, "try_to_steal_sys",
	[
		(store_attribute_level, ":attribute_level_player_1", "trp_player", 1),
		(val_mul, ":attribute_level_player_1", 2),
		(try_begin),
			(gt, ":attribute_level_player_1", 80),
			(assign, ":attribute_level_player_1", 80),
		(try_end),
		(assign, reg8, ":attribute_level_player_1")
	],
	"(Probability : {reg8}%)", "try_to_steal_sys_2",
	[]],

	[anyone|plyr, "try_to_steal_sys_2",
	[
		(eq, "$wm_quest_mission_anti_skip_menu", 1),
		(party_slot_eq, "$g_encountered_party", 15, 3)
	],
	"[Steal Gem]", "close_window",
	[
		(call_script, "script_molda_town_steal")
	]],

	[anyone|plyr, "try_to_steal_sys_2",
	[],
	"[Pickpocket]", "close_window",
	[
		(call_script, "script_molda_town_steal")
	]],

	[anyone|plyr, "try_to_steal_sys_2",
	[],
	"[leave]", "close_window",
	[]],

	[anyone|plyr, "goods_merchant_talk",
	[],
	"Never mind.", "close_window",
	[]],

	[anyone, "academy_pre_talk",
	[
		(eq, "$main_q_step", 78)
	],
	"Welcome. what do you want?", "academy_mq_78_1",
	[]],

	[anyone|plyr, "academy_mq_78_1",
	[
		(party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 6)
	],
	"I'm looking for a book. It is associated with the location of hashashin base.", "academy_mq_78_2",
	[]],

	[anyone, "academy_mq_78_2",
	[
		(party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 6)
	],
	"I know much about the book. The title of the book is a desert fortress. but this book already sold many month ago.", "academy_mq_78_3",
	[]],

	[anyone|plyr, "academy_mq_78_3",
	[],
	"Desert fortress? are you sure?", "academy_mq_78_4",
	[]],

	[anyone, "academy_mq_78_4",
	[],
	"Yes. Do you need that book? You can obtain the new book after a few months.", "academy_mq_78_5",
	[]],

	[anyone|plyr, "academy_mq_78_5",
	[],
	"No, No. You've already helped me. Thanks!", "close_window",
	[
		(assign, "$main_q_step", 79),
		(display_message, "str_mq_1_79b", 0x00ffff00)
	]],

	[anyone, "academy_mq_78_2",
	[],
	"Sorry. I have never seen that book. in my opinion, arab scholars will know better than me about hashashin base.", "close_window",
	[]],

	[anyone, "academy_pre_talk",
	[
		(this_or_next|eq, "$main_q_step", 14),
		(eq, "$main_q_step", 15),
		(eq, "$main_q_party", "$g_encountered_party")
	],
	"Did you find fortress?", "academy_mq_15_1",
	[]],

	[anyone|plyr, "academy_mq_15_1",
	[],
	"I found alamut fortress. There is something difficult to access. ", "academy_mq_15_2",
	[]],

	[anyone, "academy_mq_15_2",
	[],
	"What do you mean exactly?", "academy_mq_15_3",
	[]],

	[anyone|plyr, "academy_mq_15_3",
	[],
	"In fact, I do not know. But I really got the feeling that someone hiding.", "academy_mq_15_4",
	[]],

	[anyone, "academy_mq_15_4",
	[],
	"I understand. As promised, I will give you the information. She have working at place called to 'triangular roof'. ", "academy_mq_15_5",
	[]],

	[anyone, "academy_mq_15_5",
	[],
	"Outlaws and nobles are often seen at this place. I think that place is most suspicious place of the world.", "academy_mq_15_6",
	[]],

	[anyone|plyr, "academy_mq_15_6",
	[],
	"Alright. I can break everything between my sister and me.", "academy_mq_15_7",
	[]],

	[anyone, "academy_mq_15_7",
	[],
	"Good luck. Perhaps you will be needing the luck.", "academy_mq_15_8",
	[]],

	[anyone|plyr, "academy_mq_15_8",
	[],
	"(I forgot about reporting of necklace. Probably not necessary.)", "close_window",
	[
		(assign, "$main_q_step", 16),
		(assign, "$main_q_party", "p_antioch"),
		(str_store_party_name, 10, "$main_q_party"),
		(display_message, "str_mq_1_16b"),
		(party_get_position, 11, "$main_q_party"),
		(map_get_land_position_around_position, 12, 11, 2),
		(assign, ":var_1", "p_ruin_dummy_5"),
		(party_set_position, ":var_1", 12),
		(party_set_icon, ":var_1", "icon_house_exn"),
		(party_set_flags, ":var_1", 256, 0),
		(party_set_flags, ":var_1", 524288, 0),
		(party_set_flags, ":var_1", 16384, 1),
		(party_set_name, ":var_1", "str_mq_1_16sp_name"),
		(party_get_slot, ":main_q_party_town_center", "$main_q_party", slot_town_center),
		(party_set_slot, ":var_1", slot_town_center, ":main_q_party_town_center")
	]],

	[anyone, "academy_pre_talk",
	[
		(eq, "$main_q_step", 12),
		(eq, "$main_q_party", "$g_encountered_party")
	],
	"Seems you have found a clue. ", "academy_mq_12_1",
	[]],

	[anyone|plyr, "academy_mq_12_1",
	[],
	"So, what is the next?", "academy_mq_12_2",
	[]],

	[anyone, "academy_mq_12_2",
	[],
	"Now, you should go to the location of the ruins. You must ensure that the ruins are present.", "academy_mq_12_3",
	[]],

	[anyone|plyr, "academy_mq_12_3",
	[],
	"Okay. But do not forget about our promise.", "academy_mq_12_4",
	[]],

	[anyone, "academy_mq_12_4",
	[],
	"When you get back, I will give you the information.", "close_window",
	[
		(assign, "$main_q_step", 13),
		(assign, "$main_q_faction", "p_ruin_dummy_4"),
		(init_position, 9),
		(set_fixed_point_multiplier, 1000),
		(position_set_x, 9, -323000),
		(position_set_y, 9, -138000),
		(party_set_position, "p_ruin_dummy_4", 9),
		(party_set_name, "p_ruin_dummy_4", "str_mq_1_13n")
	]],

	[anyone, "academy_pre_talk",
	[
		(eq, "$main_q_step", 11),
		(eq, "$main_q_party", "$g_encountered_party")
	],
	"You should find the clue from the book. Come back to have a clue.", "close_window",
	[]],

	[anyone, "academy_pre_talk",
	[
		(eq, "$main_q_step", 13),
		(eq, "$main_q_party", "$g_encountered_party")
	],
	"You should find the ruins. Then, come back.", "close_window",
	[]],

	[anyone, "academy_pre_talk",
	[
		(eq, "$main_q_step", 10),
		(eq, "$main_q_party", "$g_encountered_party")
	],
	" So, What do you want?", "academy_mq_10_1",
	[]],

	[anyone|plyr, "academy_mq_10_1",
	[],
	"I heard that you have been buying the slave from trade guild. I think one of that slave is my sister.", "academy_mq_10_2",
	[]],

	[anyone, "academy_mq_10_2",
	[],
	"It's a fact. Now I want to help you, but the situation is not good to me.", "academy_mq_10_3",
	[]],

	[anyone|plyr, "academy_mq_10_3",
	[],
	" what do you say? what is 'not good situation'?", "academy_mq_10_4",
	[]],

	[anyone, "academy_mq_10_4",
	[],
	"I don't want to claim ownership about your sister. As a matter of fact, She has been kidnapped by one of criminal group.", "academy_mq_10_5",
	[]],

	[anyone|plyr, "academy_mq_10_5",
	[],
	"So who are they?", "academy_mq_10_6",
	[]],

	[anyone, "academy_mq_10_6",
	[],
	"It is too dangerous. They are threatening me. If you want their information, I will demand reward to you about my risk.", "academy_mq_10_7",
	[]],

	[anyone|plyr, "academy_mq_10_7",
	[],
	"I agree. So what is your demand?", "academy_mq_10_8",
	[]],

	[anyone, "academy_mq_10_8",
	[],
	"It is important thing to me. A few years ago I had gotten any old book. The book referred old fortress, but i failed finding this place. ", "academy_mq_10_9",
	[]],

	[anyone, "academy_mq_10_9",
	[],
	"take this book. and you should find the library. you can studying in library, for finding clues of the fortress. If you find a clue, Come back to me.", "academy_mq_10_10",
	[]],

	[anyone|plyr, "academy_mq_10_10",
	[],
	"I'll be back soon.", "close_window",
	[
		(assign, "$main_q_step", 11),
		(troop_add_item, "trp_player", 1442, 0)
	]],

	[anyone, "academy_pre_talk",
	[
		(gt, "$ruin_qst_target_num", 0),
		(le, "$ruin_qst_remain_turn", 0),
		(eq, "$ruin_qst_giver_loc", "$g_encountered_party")
	],
	"You failed to discover. So, We should receive the money paid in advance. ", "academy_fail",
	[
		(call_script, "script_party_money_level_ge", "p_main_party", "$ruin_advance_money"),
		(try_begin),
			(neq, "$wm_mo_continue", 1),
			(display_message, "str_nomoney", 0x00ff0000),
			(call_script, "script_wm_honor_change_diff", "trp_player", 10, 34),
		(try_end),
		(call_script, "script_party_money_level_diff", "p_main_party", "$ruin_advance_money", 34),
		(call_script, "script_wm_honor_change_diff", "trp_player", 2, 34),
		(assign, "$ruin_qst_target_num", 0),
		(assign, "$ruin_qst_giver_loc", 0),
		(assign, "$ruin_qst_remain_turn", 0)
	]],

	[anyone|plyr, "academy_fail",
	[],
	"I'm really sorry about that.", "academy_fail_2",
	[]],

	[anyone, "academy_fail_2",
	[],
	"You need to take a break.", "close_window",
	[]],

	[anyone, "academy_pre_talk",
	[
		(gt, "$ruin_qst_target_num", 0),
		(eq, "$ruin_qst_giver_loc", "$g_encountered_party"),
		(party_slot_eq, "$ruin_qst_target_num", slot_party_ignore_player_until, 3)
	],
	"It is amazing. Finally, you've done it!", "academy_succ",
	[]],

	[anyone, "academy_pre_talk",
	[
		(gt, "$ruin_qst_target_num", 0),
		(eq, "$ruin_qst_giver_loc", "$g_encountered_party")
	],
	"We are waiting for the good news.", "close_window",
	[]],

	[anyone, "academy_pre_talk",
	[
		(gt, "$ruin_qst_target_num", 0),
		(neq, "$ruin_qst_giver_loc", "$g_encountered_party")
	],
	"You're already getting requests. Good luck.", "close_window",
	[]],

	[anyone, "academy_pre_talk",
	[],
	"What do you want?", "academy_talk",
	[]],

	[anyone|plyr, "academy_talk",
	[],
	"I need some help to find the ruins.", "academy_ruin_1",
	[]],

	[anyone|plyr, "academy_talk",
	[],
	"Nothing", "close_window",
	[]],

	[anyone, "academy_ruin_1",
	[
		(troop_slot_ge, "trp_player", 13, -25)
	],
	"We are sponsoring the ruins exploration certainly. Do you have any information?", "academy_ruin_2",
	[]],

	[anyone, "academy_ruin_1",
	[],
	"Sorry, Considering your credit. you will not be able to get job.", "close_window",
	[]],

	[anyone|plyr, "academy_ruin_2",
	[],
	"Nothing", "close_window",
	[]],

	[anyone|repeat_for_parties|plyr, "academy_ruin_2",
	[
		(store_repeat_object, ":repeat_object"),
		(is_between, ":repeat_object", "p_ruin_1", "p_ruin_end"),
		(this_or_next|party_slot_eq, ":repeat_object", slot_party_ignore_player_until, 1),
		(party_slot_eq, ":repeat_object", slot_party_ignore_player_until, 2),
		(str_store_party_name, 6, ":repeat_object")
	],
	"{s6}.", "academy_ruin_3",
	[
		(store_repeat_object, "$ruin_quest_target")
	]],

	[anyone, "academy_ruin_3",
	[
		(party_get_slot, ":ruin_quest_target_ai_state", "$ruin_quest_target", slot_party_ai_state),
		(try_begin),
			(eq, ":ruin_quest_target_ai_state", 1),
			(str_store_string, 7, "str_f_africa"),
		(else_try),
			(eq, ":ruin_quest_target_ai_state", 2),
			(str_store_string, 7, "str_f_east_orient"),
		(else_try),
			(eq, ":ruin_quest_target_ai_state", 3),
			(str_store_string, 7, "str_f_south_orient"),
		(else_try),
			(eq, ":ruin_quest_target_ai_state", 4),
			(str_store_string, 7, "str_f_arab"),
		(else_try),
			(eq, ":ruin_quest_target_ai_state", 5),
			(str_store_string, 7, "str_f_europe"),
		(else_try),
			(eq, ":ruin_quest_target_ai_state", 6),
			(str_store_string, 7, "str_f_battle"),
		(else_try),
			(eq, ":ruin_quest_target_ai_state", 7),
			(str_store_string, 7, "str_f_mystery"),
		(else_try),
			(eq, ":ruin_quest_target_ai_state", 8),
			(str_store_string, 7, "str_f_nature"),
		(else_try),
			(eq, ":ruin_quest_target_ai_state", 9),
			(str_store_string, 7, "str_f_new_world"),
		(try_end),
		(str_store_party_name, 6, "$ruin_quest_target"),
		(str_store_string, 8, "str_arcademy_norm"),
		(try_begin),
			(eq, "$g_talk_troop", "trp_sponsor_1"),
			(neq, ":ruin_quest_target_ai_state", 4),
			(str_store_string, 8, "str_arcademy_half"),
		(else_try),
			(eq, "$g_talk_troop", "trp_sponsor_2"),
			(neq, ":ruin_quest_target_ai_state", 1),
			(neq, ":ruin_quest_target_ai_state", 2),
			(neq, ":ruin_quest_target_ai_state", 3),
			(neq, ":ruin_quest_target_ai_state", 9),
			(str_store_string, 8, "str_arcademy_half"),
		(else_try),
			(eq, "$g_talk_troop", "trp_sponsor_3"),
			(neq, ":ruin_quest_target_ai_state", 2),
			(neq, ":ruin_quest_target_ai_state", 3),
			(neq, ":ruin_quest_target_ai_state", 7),
			(str_store_string, 8, "str_arcademy_half"),
		(else_try),
			(eq, "$g_talk_troop", "trp_sponsor_4"),
			(neq, ":ruin_quest_target_ai_state", 6),
			(str_store_string, 8, "str_arcademy_half"),
		(else_try),
			(eq, "$g_talk_troop", "trp_sponsor_5"),
			(neq, ":ruin_quest_target_ai_state", 5),
			(str_store_string, 8, "str_arcademy_half"),
		(else_try),
			(eq, "$g_talk_troop", "trp_sponsor_6"),
			(neq, ":ruin_quest_target_ai_state", 8),
			(str_store_string, 8, "str_arcademy_half"),
		(else_try),
			(eq, "$g_talk_troop", "trp_sponsor_7"),
			(neq, ":ruin_quest_target_ai_state", 7),
			(str_store_string, 8, "str_arcademy_half"),
		(try_end)
	],
	"{s8}", "academy_ruin_4",
	[]],

	[anyone|plyr, "academy_ruin_4",
	[],
	"I will surely find it. If there is enough time and money.", "academy_ruin_5",
	[]],

	[anyone|plyr, "academy_ruin_4",
	[],
	"Sorry. It seems little hard.", "close_window",
	[]],

	[anyone, "academy_ruin_5",
	[
		(party_get_slot, ":ruin_quest_target_ai_state", "$ruin_quest_target", slot_party_ai_state),
		(party_get_slot, ":ruin_quest_target_ai_object", "$ruin_quest_target", slot_party_ai_object),
		(party_get_slot, ":ruin_quest_target_ai_rationale", "$ruin_quest_target", slot_party_ai_rationale),
		(party_get_slot, ":ruin_quest_target_town_lord", "$ruin_quest_target", slot_town_lord),
		(try_begin),
			(eq, "$ruin_quest_target", "p_ruin_25"),
			(val_add, ":ruin_quest_target_ai_object", 30000),
		(try_end),
		(try_begin),
			(eq, "$g_talk_troop", "trp_sponsor_1"),
			(neq, ":ruin_quest_target_ai_state", 4),
			(val_div, ":ruin_quest_target_ai_object", 2),
			(val_div, ":ruin_quest_target_ai_rationale", 2),
		(else_try),
			(eq, "$g_talk_troop", "trp_sponsor_2"),
			(neq, ":ruin_quest_target_ai_state", 1),
			(neq, ":ruin_quest_target_ai_state", 2),
			(neq, ":ruin_quest_target_ai_state", 3),
			(neq, ":ruin_quest_target_ai_state", 9),
			(val_div, ":ruin_quest_target_ai_object", 2),
			(val_div, ":ruin_quest_target_ai_rationale", 2),
		(else_try),
			(eq, "$g_talk_troop", "trp_sponsor_3"),
			(neq, ":ruin_quest_target_ai_state", 2),
			(neq, ":ruin_quest_target_ai_state", 3),
			(neq, ":ruin_quest_target_ai_state", 7),
			(val_div, ":ruin_quest_target_ai_object", 2),
			(val_div, ":ruin_quest_target_ai_rationale", 2),
		(else_try),
			(eq, "$g_talk_troop", "trp_sponsor_4"),
			(neq, ":ruin_quest_target_ai_state", 6),
			(val_div, ":ruin_quest_target_ai_object", 2),
			(val_div, ":ruin_quest_target_ai_rationale", 2),
		(else_try),
			(eq, "$g_talk_troop", "trp_sponsor_5"),
			(neq, ":ruin_quest_target_ai_state", 5),
			(val_div, ":ruin_quest_target_ai_object", 2),
			(val_div, ":ruin_quest_target_ai_rationale", 2),
		(else_try),
			(eq, "$g_talk_troop", "trp_sponsor_6"),
			(neq, ":ruin_quest_target_ai_state", 8),
			(val_div, ":ruin_quest_target_ai_object", 2),
			(val_div, ":ruin_quest_target_ai_rationale", 2),
		(else_try),
			(eq, "$g_talk_troop", "trp_sponsor_7"),
			(neq, ":ruin_quest_target_ai_state", 7),
			(val_div, ":ruin_quest_target_ai_object", 2),
			(val_div, ":ruin_quest_target_ai_rationale", 2),
		(try_end),
		(try_begin),
			(party_slot_eq, "$ruin_quest_target", slot_party_ignore_player_until, 2),
			(val_div, ":ruin_quest_target_ai_object", 2),
		(try_end),
		(store_div, ":value", ":ruin_quest_target_ai_object", 2),
		(try_begin),
			(eq, "$r_player_class", 2),
			(val_mul, ":ruin_quest_target_ai_object", 2),
			(val_mul, ":value", 2),
		(try_end),
		(assign, reg11, ":ruin_quest_target_ai_object"),
		(assign, reg12, ":value"),
		(assign, reg13, ":ruin_quest_target_town_lord"),
		(assign, "$ruin_advance_money", ":value")
	],
	"If so, We give {reg12} denars in advance. If you success in {reg13} day, then you will receive {reg11} denars. Do you accept?", "academy_ruin_6",
	[]],

	[anyone|plyr, "academy_ruin_6",
	[],
	"Agree. You will not regret about this investment.", "academy_ruin_7",
	[
		(str_store_party_name, 11, "$ruin_quest_target"),
		(assign, "$ruin_qst_target_num", "$ruin_quest_target"),
		(assign, "$ruin_qst_giver_loc", "$g_encountered_party"),
		(party_get_slot, "$ruin_qst_remain_turn", "$ruin_qst_target_num", slot_town_lord),
		(call_script, "script_party_money_level_diff", "p_main_party", "$ruin_advance_money", 87)
	]],

	[anyone|plyr, "academy_ruin_6",
	[],
	"Sorry. It seems a little hard.", "close_window",
	[]],

	[anyone, "academy_ruin_7",
	[],
	"All right. We are looking forward to good news.", "close_window",
	[
		(try_begin),
			(eq, "$r_player_class", 2),
			(call_script, "script_adv_bonus_pos"),
		(try_end)
	]],

	[anyone|plyr, "academy_succ",
	[],
	"It was hard journey.", "academy_succ_2",
	[]],

	[anyone, "academy_succ_2",
	[],
	"All right. Take the promised reward. When we announced it, You will be famous.", "close_window",
	[
		(party_get_slot, ":ruin_qst_target_num_ai_object", "$ruin_qst_target_num", slot_party_ai_object),
		(try_begin),
			(eq, "$r_player_class", 2),
			(val_mul, ":ruin_qst_target_num_ai_object", 2),
		(try_end),
		(call_script, "script_party_money_level_diff", "p_main_party", ":ruin_qst_target_num_ai_object", 87),
		(set_show_messages, 0),
		(store_div, ":value", ":ruin_qst_target_num_ai_object", 2),
		(set_show_messages, 1),
		(call_script, "script_wm_after_battle_progress", ":value"),
		(party_get_slot, ":ruin_qst_target_num_ai_rationale", "$ruin_qst_target_num", slot_party_ai_rationale),
		(try_begin),
			(eq, "$r_player_class", 2),
			(val_mul, ":ruin_qst_target_num_ai_rationale", 2),
		(try_end),
		(call_script, "script_wm_honor_change_diff", "trp_player", ":ruin_qst_target_num_ai_rationale", 87),
		(val_add, "$adv_renown", ":ruin_qst_target_num_ai_rationale"),
		(val_mul, ":ruin_qst_target_num_ai_rationale", 50),
		(call_script, "script_adv_exp_diff", ":ruin_qst_target_num_ai_rationale", 87),
		(party_set_slot, "$ruin_qst_target_num", slot_party_ignore_player_until, 4),
		(assign, "$ruin_qst_target_num", 0),
		(assign, "$ruin_qst_giver_loc", 0),
		(assign, "$ruin_qst_remain_turn", 0)
	]],

	[anyone|plyr, "lord_talk",
	[
		(faction_slot_eq, "$g_talk_troop_faction", 1, "$g_talk_troop"),
		(assign, ":value", 0),
		(assign, ":value_2", 0),
		(try_begin),
			(eq, "$g_talk_troop_faction", "fac_kingdom_13"),
			(assign, ":value_2", 1),
		(else_try),
			(eq, "$start_age", 1184),
			(eq, "$g_talk_troop_faction", "fac_kingdom_26"),
			(assign, ":value_2", 1),
		(try_end),
		(try_begin),
			(is_between, "$wm_player_fac", "fac_kingdom_1", "fac_kingdoms_end"),
			(eq, "$g_talk_troop_faction", "$wm_player_fac"),
			(assign, ":value", 1),
		(else_try),
			(is_between, "$wm_player_fac", "fac_kingdom_1", "fac_kingdoms_end"),
			(faction_slot_eq, "$wm_player_fac", 1, "trp_player"),
			(assign, ":value", 1),
		(try_end),
		(eq, ":value_2", 1),
		(eq, ":value", 1)
	],
	" Your Majesty, we must declare the holy war.", "pope_holywar",
	[]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$main_q_step", 87),
		(this_or_next|eq, "$main_q_troop", 0),
		(eq, "$main_q_faction", 0),
		(neq, "$main_q_troop", "$g_talk_troop"),
		(neq, "$main_q_faction", "$g_talk_troop")
	],
	"[Try to persuade him for support]", "mq_lord_87_1",
	[]],

	[anyone, "mq_lord_87_1",
	[
		(eq, "$g_talk_troop_faction", "$wm_player_fac"),
		(faction_slot_eq, "$g_talk_troop_faction", 1, "trp_player")
	],
	"As you wish. My lord.", "mq_lord_87_2",
	[]],

	[anyone|plyr, "mq_lord_87_2",
	[],
	" Good. I will remember your effort.", "close_window",
	[
		(try_begin),
			(eq, "$main_q_troop", 0),
			(assign, "$main_q_troop", "$g_talk_troop"),
		(else_try),
			(assign, "$main_q_faction", "$g_talk_troop"),
		(try_end)
	]],

	[anyone, "mq_lord_87_1",
	[
		(ge, "$g_talk_troop_relation", 60)
	],
	"I can help you. my friend.", "mq_lord_87_2",
	[]],

	[anyone, "mq_lord_87_1",
	[],
	"Sorry, I can not help you.", "close_window",
	[]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$main_q_step", 82),
		(troop_get_slot, ":g_talk_troop_23", "$g_talk_troop", 23),
		(this_or_next|eq, ":g_talk_troop_23", 3),
		(eq, ":g_talk_troop_23", 1)
	],
	"What do you think about Hashashin?", "mq_lord_82_1",
	[]],

	[anyone, "mq_lord_82_1",
	[],
	"They are very dangerous group. everyone knows this fact. but they are afraid that they self would be assassination target.", "mq_lord_82_2",
	[]],

	[anyone|plyr, "mq_lord_82_2",
	[],
	"Are you thinking to fight with them?", "mq_lord_82_3",
	[]],

	[anyone, "mq_lord_82_3",
	[
		(troop_slot_eq, "$g_talk_troop", 23, 3)
	],
	"Not possible. Nobody want to fight against them.", "mq_lord_82_4",
	[]],

	[anyone|plyr, "mq_lord_82_4",
	[],
	"I understand your situation.", "close_window",
	[]],

	[anyone, "mq_lord_82_3",
	[],
	"Not possible.... Maybe the Knights Templar might be interested to them.", "mq_lord_82_end_1",
	[]],

	[anyone|plyr, "mq_lord_82_end_1",
	[],
	"Knights templar? Where can I find them?", "mq_lord_82_end_2",
	[]],

	[anyone, "mq_lord_82_end_2",
	[],
	"Their headquarters is in Cyprus.", "mq_lord_82_end_3",
	[]],

	[anyone|plyr, "mq_lord_82_end_3",
	[],
	"Thanks for your advice.", "close_window",
	[
		(assign, "$main_q_step", 83),
		(party_get_position, 11, "p_cyprus"),
		(map_get_land_position_around_position, 12, 11, 1),
		(assign, ":var_1", "p_ruin_dummy_3"),
		(party_set_position, ":var_1", 12),
		(party_set_icon, ":var_1", "icon_wm_town_euro_2"),
		(party_set_flags, ":var_1", 256, 0),
		(party_set_flags, ":var_1", 524288, 0),
		(party_set_flags, ":var_1", 16384, 1),
		(party_set_name, ":var_1", "str_cyprus_fort_n"),
		(party_get_slot, ":cyprus_town_center", "p_cyprus", slot_town_center),
		(party_set_slot, ":var_1", slot_town_center, ":cyprus_town_center")
	]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$main_q_step", 77),
		(troop_get_slot, ":g_talk_troop_guardian", "$g_talk_troop", slot_troop_guardian),
		(this_or_next|eq, ":g_talk_troop_guardian", "fac_kingdom_4"),
		(this_or_next|eq, ":g_talk_troop_guardian", "fac_kingdom_9"),
		(this_or_next|eq, ":g_talk_troop_guardian", "fac_kingdom_13"),
		(this_or_next|eq, ":g_talk_troop_guardian", "fac_kingdom_14"),
		(eq, ":g_talk_troop_guardian", "fac_kingdom_56")
	],
	"Do you know about hashashin?", "mq_lord_77_1",
	[]],

	[anyone, "mq_lord_77_1",
	[],
	"Vile fanatics, They have many enemies. They are infamous by assassination.", "mq_lord_77_2",
	[]],

	[anyone|plyr, "mq_lord_77_2",
	[],
	"How can I find their base?", "mq_lord_77_3",
	[]],

	[anyone, "mq_lord_77_3",
	[
		(lt, "$comp_rel_passsss", 2)
	],
	"Perhaps the book will be exist. it is will be associated with location of hashashin base.", "mq_lord_77_end",
	[]],

	[anyone|plyr, "mq_lord_77_end",
	[],
	"It is valuable information. Thanks.", "close_window",
	[
		(display_message, "str_mq_1_78b", 0x00ffff00),
		(assign, "$main_q_step", 78)
	]],

	[anyone, "mq_lord_77_3",
	[],
	"Unfortunately, I don't know about their base.", "mq_lord_77_4",
	[]],

	[anyone|plyr, "mq_lord_77_4",
	[],
	"Thanks. I must beg my leave.", "close_window",
	[]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$main_q_step", 2),
		(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
		(eq, ":faction_of_party_g_encountered_party", "$kingdom_pick_start_faction")
	],
	"my lord, Our citizens have been sold to slave traders. my little sister is one of them. we need assistance of army to rescue them.", "mq_lord_2_1",
	[]],

	[anyone, "mq_lord_2_1",
	[],
	"I understood. so, exactly where is?  In order to move the army , i need more detailed information.", "mq_lord_2_2",
	[]],

	[anyone|plyr, "mq_lord_2_2",
	[
		(neq, "$rt_marked_target", "$main_q_party")
	],
	"umm... sorry, I must beg my leave. (system: You need to set correctly 'map marker'.)", "close_window",
	[]],

	[anyone|plyr, "mq_lord_2_2",
	[
		(str_store_party_name, 12, "$main_q_party")
	],
	"slave traders are staying at the {s12}, can you help us?", "mq_lord_2_3",
	[]],

	[anyone, "mq_lord_2_3",
	[],
	"Our special army could be rescued them. we should wait until the results come out.", "mq_lord_2_4",
	[]],

	[anyone|plyr, "mq_lord_2_4",
	[],
	"I appreciate about your effort. my lord.", "close_window",
	[
		(assign, "$main_q_step", 3),
		(assign, "$main_q_day", 14)
	]],

	[anyone|plyr, "lord_talk",
	[
		(party_slot_eq, "$g_encountered_party", slot_party_type, 1),
		(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
		(neq, "$wm_player_fac", ":faction_of_party_g_encountered_party"),
		(neq, "$contract_fac", ":faction_of_party_g_encountered_party"),
		(store_random_in_range, ":random_in_range_attack_comment_01_attack_comment_end", "str_attack_comment_01", "str_attack_comment_end"),
		(str_store_string, 43, ":random_in_range_attack_comment_01_attack_comment_end")
	],
	"{s43}", "player_ambush_to_neutral_1",
	[]],

	[anyone|plyr, "lord_talk",
	[
		(gt, "$qquest_type", 0),
		(eq, "$qquest_report_troop", "$g_talk_troop"),
		(neq, "$qquest_progress", 1)
	],
	" Sorry. I cannot keep our appointment.", "lord_quest_cancel",
	[]],

	[anyone, "lord_quest_cancel",
	[],
	" Okay, then. It can't be helped. I'll find someone else.", "lord_talk",
	[
		(call_script, "script_qquest_initialize"),
		(play_sound, "snd_bad_drum"),
		(display_message, "str_questcancel"),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -3)
	]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$qquest_type", 22),
		(eq, "$qquest_target_troop", "$g_talk_troop"),
		(eq, "$qquest_progress", 0),
		(str_store_troop_name, 9, "$qquest_report_troop")
	],
	"I want you to take back your accusations against {s9}.", "lady_duel_req_end_1",
	[]],

	[anyone, "lady_duel_req_end_1",
	[],
	"What accusations? Everyone knows that she beds her stable boys and anyone else she can lay hands on while her husband is away. I merely repeat the words of many.", "lady_duel_req_end_2",
	[]],

	[anyone|plyr, "lady_duel_req_end_2",
	[],
	"You will recant these lies, sirrah, or prove them against my sword!", "lady_duel_req_end_3",
	[]],

	[anyone, "lady_duel_req_end_3",
	[],
	"You are challenging me to a duel? How droll! As you wish, {playername}, it will be good sport to bash your head in.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -15),
		(assign, "$wm_target_troop", "$g_talk_troop"),
		(try_begin),
			(is_between, "$g_encountered_party", "p_pyongyang", "p_place_end"),
			(call_script, "script_wm_finish_mission_menu_popup", "mnu_lord_talk_duel_menu_jump"),
		(else_try),
			(jump_to_menu, "mnu_lord_talk_duel_menu_jump"),
		(try_end)
	]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$qquest_type", 11),
		(eq, "$qquest_target_troop", "$g_talk_troop"),
		(str_store_troop_name, 9, "$qquest_report_troop")
	],
	"I bring a message from {s9}.", "lord_deliver_mess_end",
	[]],

	[anyone, "lord_deliver_mess_end",
	[],
	"Oh? Let me see that... Well, well, well! It was good of you to bring me this, {playername}. Take my seal as proof that I've received it, and give my regards to {s9} when you see him again.", "lord_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 5),
		(call_script, "script_change_player_relation_with_troop", "$qquest_report_troop", 5),
		(store_add, ":value", 1000, 1000),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
		(call_script, "script_qquest_initialize"),
		(play_sound, "snd_experience_gained"),
		(call_script, "script_town_relation_diff", "$g_encountered_party", 1),
		(display_message, "str_questcomp")
	]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$qquest_type", 13),
		(eq, "$qquest_progress", 1),
		(eq, "$qquest_report_troop", "$g_talk_troop")
	],
	"I defeated the enemy. we can celebrate together.", "lord_enemydefeat_end",
	[]],

	[anyone, "lord_enemydefeat_end",
	[],
	"Great! Your loyalty has been proven! praise the god!", "lord_talk",
	[
		(call_script, "script_wm_honor_change_diff", "trp_player", 5, 87),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 15),
		(store_mul, ":value", 1000, 15),
		(call_script, "script_wm_after_battle_progress", 1000),
		(call_script, "script_exp_reward_for_common_troop", 48),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
		(call_script, "script_qquest_initialize"),
		(play_sound, "snd_experience_gained"),
		(call_script, "script_town_relation_diff", "$g_encountered_party", 1),
		(display_message, "str_questcomp")
	]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$qquest_type", 14),
		(eq, "$qquest_progress", 1),
		(eq, "$qquest_report_troop", "$g_talk_troop")
	],
	"I was ambush the enemy. Everything was as planned.", "lord_warmonger_end",
	[]],

	[anyone, "lord_warmonger_end",
	[],
	" Great! You are a true patriot! Now it's war!", "lord_talk",
	[
		(call_script, "script_wm_honor_change_diff", "trp_player", 5, 34),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 45),
		(store_mul, ":value", 1000, 20),
		(call_script, "script_wm_after_battle_progress", 1000),
		(call_script, "script_exp_reward_for_common_troop", 72),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
		(call_script, "script_qquest_initialize"),
		(play_sound, "snd_experience_gained"),
		(call_script, "script_town_relation_diff", "$g_encountered_party", 1),
		(display_message, "str_questcomp")
	]],

	[anyone|plyr, "lord_talk",
	[
		(ge, "$g_talk_troop_faction_relation", 0),
		(eq, "$qquest_type", 0),
		(neq, "$g_talk_troop", "$player_spouse"),
		(troop_slot_ge, "$g_talk_troop", 20, 11),
		(neg|troop_slot_ge, "$g_talk_troop", 20, 15)
	],
	"  Do you happen to have a job for me?", "lord_quest",
	[]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$attemp_commu", 0),
		(ge, "$g_talk_troop_faction_relation", 0)
	],
	"I would like to talk about our religion.", "lord_relation_religion_talk",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lord_relation_religion_talk",
	[
		(troop_get_slot, ":player_23", "trp_player", 23),
		(troop_get_slot, ":g_talk_troop_23", "$g_talk_troop", 23),
		(neq, ":player_23", ":g_talk_troop_23")
	],
	"What? Our religion?", "lord_relation_religion_diff",
	[]],

	[anyone, "lord_relation_religion_diff",
	[],
	"I'm not have interest to pointless discussions.(Different Religion.)", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -5)
	]],

	[anyone, "lord_relation_religion_talk",
	[
		(this_or_next|eq, "$g_talk_troop_ego", 1),
		(eq, "$g_talk_troop_ego", 5)
	],
	"be honest, I don't like discussion.", "close_window",
	[]],

	[anyone, "lord_relation_religion_talk",
	[],
	"Not bad. I was bored until before you coming.", "lord_relation_religion_tal_2",
	[]],

	[anyone, "lord_relation_religion_tal_2",
	[],
	"[had a long talk]", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 7)
	]],

	[anyone|plyr, "lord_talk",
	[
		(ge, "$g_talk_troop_faction_relation", 0),
		(call_script, "script_party_money_level_ge", "p_main_party", 1000),
		(eq, "$wm_mo_continue", 1)
	],
	"I am honored to meet you. Please receive the my small gift. (Bribe)", "lord_bribe",
	[
		(store_random_in_range, "$temp_dice", 0, 100),
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lord_bribe",
	[
		(eq, "$g_talk_troop_ego", 2)
	],
	"i'm not interested your dirty money.", "lord_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -10)
	]],

	[anyone, "lord_bribe",
	[
		(ge, "$temp_dice", 50),
		(this_or_next|eq, "$g_talk_troop_ego", 1),
		(eq, "$g_talk_troop_ego", 5)
	],
	"Thank you. However, I want more money.", "lord_talk",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34),
		(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 15)
	]],

	[anyone, "lord_bribe",
	[
		(ge, "$temp_dice", 50)
	],
	"Your intention is suspected. however, Money is not guilty.", "lord_talk",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 1000, 34),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 10)
	]],

	[anyone, "lord_bribe",
	[],
	"Sorry. I need avoid unnecessary doubt.", "lord_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -5)
	]],

	[anyone|plyr, "lord_talk",
	[
		(ge, "$g_talk_troop_faction_relation", 0),
		(eq, "$attemp_commu", 0)
	],
	" How do you do these days?", "member_comp_relation_talk",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lord_talk",
	[
		(ge, "$g_talk_troop_faction_relation", 0)
	],
	"May I ask you a favor?, I want to practice fighting with you.", "lord_talk_duel_request_1",
	[
		(call_script, "script_rand_glob_dice")
	]],

	[anyone, "lord_talk_duel_request_1",
	[
		(ge, "$random_duel_offer", 65)
	],
	"Alright. It is okay for a while.", "close_window",
	[
		(assign, "$wm_target_troop", "$g_talk_troop"),
		(try_begin),
			(is_between, "$g_encountered_party", "p_pyongyang", "p_place_end"),
			(call_script, "script_wm_finish_mission_menu_popup", "mnu_lord_talk_duel_menu_jump"),
		(else_try),
			(jump_to_menu, "mnu_lord_talk_duel_menu_jump"),
		(try_end)
	]],

	[anyone, "lord_talk_duel_request_1",
	[
		(ge, "$random_duel_offer", 25)
	],
	"I'm in a hurry.  Maybe, some other time.", "close_window",
	[]],

	[anyone, "lord_talk_duel_request_1",
	[],
	"Don't borther me.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -1)
	]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$wm_talk_state", 5),
		(eq, "$g_talk_troop", "$player_spouse"),
		(eq, "$player_gender", 1),
		(eq, "$talk_troop_gender", 0),
		(eq, "$attemp_commu", 0),
		(eq, "$adult_content", 1)
	],
	"Hey, handsome. If you do not get bored?", "lord_husband_fuck_talk",
	[]],

	[anyone, "lord_husband_fuck_talk",
	[],
	"Bored. Go into the bedroom?", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_female_p_fuck_reln"),
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$g_talk_troop", "$player_spouse"),
		(eq, "$player_gender", 1),
		(eq, "$talk_troop_gender", 0),
		(eq, "$attemp_commu", 0),
		(eq, "$adult_content", 1)
	],
	"I give you blowjob.", "lord_husband_blowjob_1",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lord_husband_blowjob_1",
	[],
	"Oh. What a sweetheart.", "lord_husband_blowjob_2",
	[]],

	[anyone|plyr, "lord_husband_blowjob_2",
	[],
	".........", "lord_husband_blowjob_3",
	[
		(call_script, "script_molda_s_scene", 211, 0)
	]],

	[anyone, "lord_husband_blowjob_3",
	[],
	"Oh....ow!", "lord_husband_blowjob_4",
	[]],

	[anyone|plyr, "lord_husband_blowjob_4",
	[],
	"........   ", "lord_husband_blowjob_5",
	[
		(call_script, "script_molda_s_scene", 211, 0)
	]],

	[anyone, "lord_husband_blowjob_5",
	[],
	"    Uhh!", "lord_husband_blowjob_6",
	[
		(store_random_in_range, ":random_in_range_212_214", 212, 214),
		(call_script, "script_molda_s_scene", ":random_in_range_212_214", 0)
	]],

	[anyone|plyr, "lord_husband_blowjob_6",
	[],
	"Uhh! Weird taste. You're feels better now?", "lord_talk",
	[
		(store_random_in_range, ":random_in_range_5_8", 5, 8),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", ":random_in_range_5_8"),
		(try_begin),
			(eq, "$blowjob_sp_skill", 1),
			(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 5),
		(try_end)
	]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$wm_talk_state", 5),
		(ge, "$g_talk_troop_faction_relation", 0),
		(neg|faction_slot_eq, "$g_talk_troop_faction", 1, "trp_player"),
		(neq, "$g_talk_troop", "$player_spouse"),
		(eq, "$player_gender", 1),
		(eq, "$talk_troop_gender", 0),
		(eq, "$attemp_commu", 0),
		(store_current_scene, ":current_scene"),
		(neq, ":current_scene", "scn_ex_bedroom"),
		(eq, "$adult_content", 1)
	],
	"Hey, handsome. You got a minute?", "lord_for_girl_sex_try",
	[
		(assign, "$in_near_spouse", 0),
		(get_player_agent_no, ":player_agent_no"),
		(try_for_agents, ":var_2"),
			(neq, ":var_2", ":player_agent_no"),
			(agent_get_troop_id, ":troop_id_var_2", ":var_2"),
			(troop_slot_eq, "$g_talk_troop", slot_troop_state, ":troop_id_var_2"),
			(troop_slot_eq, ":troop_id_var_2", slot_troop_state, "$g_talk_troop"),
			(assign, "$in_near_spouse", 1),
		(try_end),
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lord_for_girl_sex_try",
	[
		(eq, "$in_near_spouse", 1)
	],
	"Whisper: You can't see my wife?", "lord_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -3)
	]],

	[anyone, "lord_for_girl_sex_try",
	[],
	"Do you have something to say to me. Lady?", "lord_for_girl_sex_choose",
	[]],

	[anyone|plyr, "lord_for_girl_sex_choose",
	[],
	"I give you blowjob.", "lord_blowjob_1",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lord_blowjob_1",
	[
		(store_random_in_range, ":random_in_range_0_10", 0, 10),
		(gt, ":random_in_range_0_10", 6)
	],
	"Oh. What a sweetheart.", "lord_blowjob_2",
	[]],

	[anyone, "lord_blowjob_1",
	[],
	"Not now.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -3)
	]],

	[anyone|plyr, "lord_blowjob_2",
	[],
	".........", "lord_blowjob_3",
	[
		(call_script, "script_molda_s_scene", 211, 0)
	]],

	[anyone, "lord_blowjob_3",
	[],
	"   Oh....ow!", "lord_blowjob_4",
	[]],

	[anyone|plyr, "lord_blowjob_4",
	[],
	"........    ", "lord_blowjob_5",
	[
		(call_script, "script_molda_s_scene", 211, 0)
	]],

	[anyone, "lord_blowjob_5",
	[],
	"     Uhh!", "lord_blowjob_6",
	[
		(store_random_in_range, ":random_in_range_212_214", 212, 214),
		(call_script, "script_molda_s_scene", ":random_in_range_212_214", 0)
	]],

	[anyone|plyr, "lord_blowjob_6",
	[],
	"Uhh! Weird taste. You're feels better now?", "lord_talk",
	[
		(store_random_in_range, ":random_in_range_5_8", 5, 8),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", ":random_in_range_5_8"),
		(try_begin),
			(eq, "$blowjob_sp_skill", 1),
			(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 5),
		(try_end)
	]],

	[anyone|plyr, "lord_for_girl_sex_choose",
	[],
	"We need to know each other. I want to get along with you.", "lord_for_girl_sex_relation",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lord_for_girl_sex_relation",
	[
		(store_random_in_range, ":random_in_range_0_10", 0, 10),
		(gt, ":random_in_range_0_10", 3)
	],
	"Good. I want to know about you.", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_female_p_fuck_reln")
	]],

	[anyone, "lord_for_girl_sex_relation",
	[],
	"Get out.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -3)
	]],

	[anyone|plyr, "lord_for_girl_sex_choose",
	[
		(neg|troop_slot_ge, "trp_player", 3, "trp_tt_lord_01_00")
	],
	"I give you blowjob. 250s in one shot?", "lord_bribe_blowjob_1",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lord_bribe_blowjob_1",
	[
		(store_random_in_range, ":random_in_range_0_10", 0, 10),
		(gt, ":random_in_range_0_10", 3)
	],
	"I will give it money. Suck my dick.", "lord_bribe_blowjob_2",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 250, 87)
	]],

	[anyone, "lord_bribe_blowjob_1",
	[],
	"Not now.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -2)
	]],

	[anyone|plyr, "lord_bribe_blowjob_2",
	[],
	".........", "lord_bribe_blowjob_3",
	[
		(call_script, "script_molda_s_scene", 211, 0)
	]],

	[anyone, "lord_bribe_blowjob_3",
	[],
	"    Oh....ow!", "lord_bribe_blowjob_4",
	[]],

	[anyone|plyr, "lord_bribe_blowjob_4",
	[],
	"........     ", "lord_bribe_blowjob_5",
	[
		(call_script, "script_molda_s_scene", 211, 0)
	]],

	[anyone, "lord_bribe_blowjob_5",
	[],
	"      Uhh!", "lord_bribe_blowjob_6",
	[
		(store_random_in_range, ":random_in_range_212_214", 212, 214),
		(call_script, "script_molda_s_scene", ":random_in_range_212_214", 0)
	]],

	[anyone|plyr, "lord_bribe_blowjob_6",
	[],
	"Uhh! Weird taste. You're feels better now?", "lord_talk",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 200, 87),
		(val_add, "$Meruru_num", 1),
		(try_begin),
			(eq, "$blowjob_sp_skill", 1),
			(call_script, "script_party_money_level_diff", "p_main_party", 200, 87),
		(try_end)
	]],

	[anyone|plyr, "lord_for_girl_sex_choose",
	[
		(neg|troop_slot_ge, "trp_player", 3, "trp_tt_lord_01_00")
	],
	"How about 500s in one shot? I am a girl selling Happiness.", "lord_for_girl_sex_get_money",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lord_for_girl_sex_get_money",
	[
		(store_random_in_range, ":random_in_range_0_10", 0, 10),
		(gt, ":random_in_range_0_10", 3)
	],
	"...Meet at a warehouse near.", "close_window",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 500, 87),
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_female_p_fuck_prosti")
	]],

	[anyone, "lord_for_girl_sex_get_money",
	[],
	"fuck off whore.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -2)
	]],

	[anyone|plyr, "lord_for_girl_sex_choose",
	[],
	"Nothing. sorry", "close_window",
	[]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$wm_talk_state", 5),
		(neq, "$g_talk_troop", "$player_spouse"),
		(eq, "$attemp_commu", 0),
		(eq, "$talk_troop_gender", 0),
		(eq, "$adult_content", 1)
	],
	"For our friendship, I have a suggestion.", "lord_comp_sex_trade",
	[
		(assign, "$in_near_spouse", 0),
		(get_player_agent_no, ":player_agent_no"),
		(try_for_agents, ":var_2"),
			(neq, ":var_2", ":player_agent_no"),
			(agent_get_troop_id, ":troop_id_var_2", ":var_2"),
			(troop_slot_eq, "$g_talk_troop", slot_troop_state, ":troop_id_var_2"),
			(troop_slot_eq, ":troop_id_var_2", slot_troop_state, "$g_talk_troop"),
			(assign, "$in_near_spouse", 1),
		(try_end),
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lord_comp_sex_trade",
	[
		(eq, "$in_near_spouse", 1)
	],
	"Whisper: You can't see my wife?", "lord_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -2)
	]],

	[anyone, "lord_comp_sex_trade",
	[],
	"What is your suggestion?", "lord_comp_sex_trade_choose",
	[]],

	[anyone|repeat_for_troops|plyr, "lord_comp_sex_trade_choose",
	[
		(store_repeat_object, ":repeat_object"),
		(is_between, ":repeat_object", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(neg|troop_slot_eq, "trp_player", slot_troop_state, ":repeat_object"),
		(call_script, "script_wm_main_party_has_troop_sc", ":repeat_object"),
		(eq, "$wm_comp_continue", 1),
		(str_store_troop_name, 1, ":repeat_object")
	],
	"{s1} will give you the Happiness.", "lord_comp_sex_trade_choos_2",
	[
		(store_repeat_object, "$g_sex_trade_comp_id")
	]],

	[anyone|plyr, "lord_comp_sex_trade_choose",
	[],
	"Never mind.", "close_window",
	[]],

	[anyone, "lord_comp_sex_trade_choos_2",
	[
		(troop_slot_eq, "$g_sex_trade_comp_id", slot_troop_player_order_object, 15),
		(this_or_next|eq, "$g_talk_troop_ego", 2),
		(this_or_next|eq, "$g_talk_troop_ego", 3),
		(this_or_next|eq, "$g_talk_troop_ego", 0),
		(eq, "$g_talk_troop_ego", 1)
	],
	"If this girl....I cannot resist.", "close_window",
	[
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_comp_trade_sex_scene")
	]],

	[anyone, "lord_comp_sex_trade_choos_2",
	[
		(troop_slot_eq, "$g_sex_trade_comp_id", slot_troop_player_order_object, 15),
		(this_or_next|eq, "$g_talk_troop_ego", 2),
		(this_or_next|eq, "$g_talk_troop_ego", 3),
		(this_or_next|eq, "$g_talk_troop_ego", 0),
		(eq, "$g_talk_troop_ego", 1)
	],
	"If this girl....I cannot resist.", "close_window",
	[
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_comp_trade_sex_scene")
	]],

	[anyone, "lord_comp_sex_trade_choos_2",
	[
		(troop_slot_eq, "$g_sex_trade_comp_id", slot_troop_player_order_object, 15),
		(this_or_next|eq, "$g_talk_troop_ego", 2),
		(this_or_next|eq, "$g_talk_troop_ego", 3),
		(this_or_next|eq, "$g_talk_troop_ego", 0),
		(eq, "$g_talk_troop_ego", 1)
	],
	"If this girl....I cannot resist.", "close_window",
	[
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_comp_trade_sex_scene")
	]],

	[anyone, "lord_comp_sex_trade_choos_2",
	[
		(troop_slot_eq, "$g_sex_trade_comp_id", slot_troop_player_order_object, 15),
		(this_or_next|eq, "$g_talk_troop_ego", 2),
		(this_or_next|eq, "$g_talk_troop_ego", 3),
		(this_or_next|eq, "$g_talk_troop_ego", 0),
		(eq, "$g_talk_troop_ego", 1)
	],
	"If this girl....I cannot resist.", "close_window",
	[
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_comp_trade_sex_scene")
	]],

	[anyone, "lord_comp_sex_trade_choos_2",
	[
		(troop_slot_eq, "$g_sex_trade_comp_id", slot_troop_player_order_object, 15),
		(this_or_next|eq, "$g_talk_troop_ego", 2),
		(this_or_next|eq, "$g_talk_troop_ego", 3),
		(this_or_next|eq, "$g_talk_troop_ego", 0),
		(eq, "$g_talk_troop_ego", 1)
	],
	"If this girl....I cannot resist.", "close_window",
	[
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_comp_trade_sex_scene")
	]],

	[anyone, "lord_comp_sex_trade_choos_2",
	[],
	"She is not my preference.", "close_window",
	[]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$g_talk_troop", "$player_spouse"),
		(lt, "$g_talk_troop_relation", -24),
		(eq, "$attemp_commu", 0)
	],
	"Between you and I almost ended. I want divorce.", "spouse_talk_divorce_random",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$g_talk_troop_faction", "$wm_player_fac"),
		(troop_slot_ge, "trp_player", 18, 11),
		(neg|faction_slot_eq, "$wm_player_fac", 1, "$g_talk_troop"),
		(neg|faction_slot_eq, "$wm_player_fac", 1, "trp_player"),
		(troop_slot_eq, "$g_talk_troop", slot_troop_leaded_party, 0)
	],
	"I want to have secret talk with you.", "lord_coup_1",
	[]],

	[anyone|plyr, "lord_talk",
	[
		(eq, "$g_talk_troop_faction", "$wm_player_fac"),
		(troop_slot_ge, "trp_player", 18, 11),
		(neg|faction_slot_eq, "$wm_player_fac", 1, "$g_talk_troop"),
		(neg|faction_slot_eq, "$wm_player_fac", 1, "trp_player"),
		(troop_slot_ge, "$g_talk_troop", 10, 1)
	],
	"[He is your supporter]", "lord_supporter_1",
	[]],

	[anyone, "lord_supporter_1",
	[],
	"Our plan has been going proceed?", "lord_supporter_2",
	[]],

	[anyone|plyr, "lord_supporter_2",
	[],
	"Yes. Please wait just a little more.", "lord_supporter_yes",
	[]],

	[anyone, "lord_supporter_yes",
	[],
	"We will not be able to wait long. Better get going.", "lord_talk",
	[]],

	[anyone|plyr, "lord_supporter_2",
	[],
	"No. Please forget about our plan.", "lord_supporter_no",
	[]],

	[anyone, "lord_supporter_no",
	[],
	"There is no choice. I will forget it.", "lord_talk",
	[
		(troop_set_slot, "$g_talk_troop", slot_troop_leaded_party, 0)
	]],

	[anyone, "lord_coup_1",
	[
		(lt, "$g_talk_troop_relation", 80)
	],
	"No. I need avoid unnecessary doubt.", "lord_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -5)
	]],

	[anyone, "lord_coup_1",
	[],
	"Secret? What are you talking about?", "lord_coup_2",
	[]],

	[anyone|plyr, "lord_coup_2",
	[],
	"Our country is becoming collapse. for protecting our civil, new government is required.", "lord_coup_persue_civil",
	[]],

	[anyone, "lord_coup_persue_civil",
	[
		(eq, "$g_talk_troop_ego", 2)
	],
	"What??", "lord_coup_persue_exposed",
	[]],

	[anyone, "lord_coup_persue_civil",
	[
		(this_or_next|eq, "$g_talk_troop_ego", 1),
		(eq, "$g_talk_troop_ego", 5)
	],
	"Civil? Why do you care about them? I'm not heard your words.", "lord_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -5)
	]],

	[anyone, "lord_coup_persue_civil",
	[
		(gt, "$random_succ_100_orand", 50),
		(store_random_in_range, ":random_in_range_political_philosophy_martial_political_philosophy_end", "str_political_philosophy_martial", "str_political_philosophy_end"),
		(str_store_string, 43, ":random_in_range_political_philosophy_martial_political_philosophy_end")
	],
	"{s43}. In fact, I'm thinking the same thing. At later date, I will help you.", "lord_talk",
	[
		(troop_set_slot, "$g_talk_troop", slot_troop_leaded_party, 25),
		(display_message, "str_comrade_add", 0x00ffff00),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 50),
		(call_script, "script_rand_glob_dice")
	]],

	[anyone, "lord_coup_persue_civil",
	[
		(store_random_in_range, ":random_in_range_talk_later_martial_talk_later_end", "str_talk_later_martial", "str_talk_later_end"),
		(str_store_string, 43, ":random_in_range_talk_later_martial_talk_later_end")
	],
	"{s43}", "lord_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -5)
	]],

	[anyone|plyr, "lord_coup_2",
	[],
	"I know that your ambition is enormous. if you help my achievement, the great rewards will follow to you.", "lord_coup_persue_ambition",
	[]],

	[anyone, "lord_coup_persue_ambition",
	[
		(eq, "$g_talk_troop_ego", 2)
	],
	"What??", "lord_coup_persue_exposed",
	[]],

	[anyone, "lord_coup_persue_ambition",
	[
		(this_or_next|eq, "$g_talk_troop_ego", 3),
		(this_or_next|eq, "$g_talk_troop_ego", 4),
		(eq, "$g_talk_troop_ego", 0)
	],
	"You're do not know about me. There is no ambition like that to me.", "lord_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -5)
	]],

	[anyone, "lord_coup_persue_ambition",
	[
		(gt, "$random_succ_100_srand", 50)
	],
	"You know well about me. Life is just once, If have a chance, I will help you.", "lord_talk",
	[
		(troop_set_slot, "$g_talk_troop", slot_troop_leaded_party, 25),
		(display_message, "str_comrade_add", 0x00ffff00),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 50)
	]],

	[anyone, "lord_coup_persue_ambition",
	[
		(store_random_in_range, ":random_in_range_talk_later_martial_talk_later_end", "str_talk_later_martial", "str_talk_later_end"),
		(str_store_string, 43, ":random_in_range_talk_later_martial_talk_later_end")
	],
	"{s43}", "lord_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -5)
	]],

	[anyone|plyr, "lord_coup_2",
	[],
	"Your achievements are not recognized in this country. I will help you.", "lord_coup_persue_hate",
	[]],

	[anyone, "lord_coup_persue_hate",
	[
		(eq, "$g_talk_troop_ego", 2)
	],
	"What??", "lord_coup_persue_exposed",
	[]],

	[anyone, "lord_coup_persue_hate",
	[
		(this_or_next|eq, "$g_talk_troop_ego", 1),
		(this_or_next|eq, "$g_talk_troop_ego", 4),
		(eq, "$g_talk_troop_ego", 0)
	],
	"There is no complaints about government like that to me.", "lord_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -5)
	]],

	[anyone, "lord_coup_persue_hate",
	[
		(gt, "$rand100_enemy_strategy", 50)
	],
	"You are right. Birds has sitting by selecting branch of tree. wise vassal is carefully choose the king. I will support you.", "lord_talk",
	[
		(troop_set_slot, "$g_talk_troop", slot_troop_leaded_party, 25),
		(display_message, "str_comrade_add", 0x00ffff00),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 50)
	]],

	[anyone, "lord_coup_persue_hate",
	[
		(store_random_in_range, ":random_in_range_talk_later_martial_talk_later_end", "str_talk_later_martial", "str_talk_later_end"),
		(str_store_string, 43, ":random_in_range_talk_later_martial_talk_later_end")
	],
	"{s43}", "lord_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -5)
	]],

	[anyone|plyr, "lord_coup_2",
	[],
	"Sorry. Forget about this.", "close_window",
	[]],

	[anyone, "lord_coup_persue_exposed",
	[],
	"I don't think so. This is a rebellion conspiracy. I exposed it all.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -99),
		(assign, ":var_1", "$wm_player_fac"),
		(call_script, "script_abondon_country_proceed", -99),
		(call_script, "script_init_main_party_core_slot"),
		(play_sound, "snd_lose_1"),
		(display_message, "str_coup_exposed", 0x00ff0000),
		(call_script, "script_set_player_relation_with_faction", ":var_1", -99),
		(change_screen_return)
	]],

	[anyone|plyr, "lord_talk",
	[
		(le, "$contract_time", 0),
		(neg|is_between, "$contract_fac", "fac_kingdom_1", "fac_kingdoms_end"),
		(neg|troop_slot_ge, "trp_player", 18, 11)
	],
	"I heard about that. your faction has recruiting mercenary leader.", "lord_talk_mercenary_1",
	[]],

	[anyone, "lord_talk_mercenary_1",
	[
		(set_show_messages, 0),
		(troop_get_slot, ":player_original_faction", "trp_player", slot_troop_original_faction),
		(val_div, ":player_original_faction", 37),
		(set_show_messages, 1),
		(lt, ":player_original_faction", 0)
	],
	"Right. however, Honesty, your reputation is bad. if i had Recommend you to candidate, maybe it is not accepted. (need honor)", "close_window",
	[]],

	[anyone, "lord_talk_mercenary_1",
	[
		(troop_get_slot, ":player_last_comment_slot", "trp_player", slot_troop_last_comment_slot),
		(lt, ":player_last_comment_slot", 2)
	],
	"Right. however, I think your lack of leadership is the problem. (need leadership 2)", "close_window",
	[]],

	[anyone, "lord_talk_mercenary_1",
	[
		(store_attribute_level, ":attribute_level_player_3", "trp_player", 3),
		(lt, ":attribute_level_player_3", 15)
	],
	"Right. however, I think your leadership is poor. (need charisma 15)", "close_window",
	[]],

	[anyone, "lord_talk_mercenary_1",
	[
		(store_character_level, ":character_level_player", "trp_player"),
		(lt, ":character_level_player", 15)
	],
	"Right. however, I think your lack of experience is the problem. (need level 15)", "close_window",
	[]],

	[anyone, "lord_talk_mercenary_1",
	[
		(assign, ":value", 0),
		(try_for_range, ":faction", "fac_kingdom_1", "fac_undeads"),
			(neq, ":faction", "$g_talk_troop_faction"),
			(store_relation, ":relation_faction_g_talk_troop_faction", ":faction", "$g_talk_troop_faction"),
			(lt, ":relation_faction_g_talk_troop_faction", 0),
			(assign, ":value", 1),
		(try_end),
		(eq, ":value", 0)
	],
	"Mercenaries, for what? our faction is peaceful.", "close_window",
	[]],

	[anyone, "lord_talk_mercenary_1",
	[],
	"Right. we need mercenaries to against enemy.", "lord_talk_mercenary_2",
	[]],

	[anyone, "lord_talk_mercenary_2",
	[],
	"So. if you have doing to lead our mercenaries, our faction will give money to you. don't worry about wage. we provide wage to you. during hundred days.", "lord_talk_mercenary_3",
	[]],

	[anyone|plyr, "lord_talk_mercenary_3",
	[],
	"I accept. it is honorable job.", "lord_talk_mercenary_4",
	[]],

	[anyone|plyr, "lord_talk_mercenary_3",
	[],
	"Sorry. it is hard to me.", "close_window",
	[]],

	[anyone, "lord_talk_mercenary_4",
	[],
	"Good. we need write contract paper right now........   Our faction have been ready for two thousand mercenaries. it isn't enough. you need recruit more mercenaries. for victory.", "close_window",
	[
		(call_script, "script_wm_mercenary_contract", "$g_talk_troop_faction")
	]],

	[anyone|plyr, "lord_talk",
	[
		(neg|is_between, "$contract_fac", "fac_kingdom_1", "fac_kingdoms_end"),
		(neg|troop_slot_ge, "trp_player", 18, 11)
	],
	"I hope join to your country. can you help me?", "lord_ask_enter_service",
	[]],

	[anyone, "lord_ask_enter_service",
	[
		(lt, "$g_talk_troop_faction_relation", 0)
	],
	"How dare you say such a thing? you are one of our enemy!", "close_window",
	[]],

	[anyone, "lord_ask_enter_service",
	[
		(call_script, "script_check_faction_lord_list15_number", "$g_talk_troop_faction"),
		(neq, "$wm_stp_continue", 1)
	],
	"We have a lot of generals already.", "close_window",
	[]],

	[anyone, "lord_ask_enter_service",
	[
		(lt, "$g_talk_troop_relation", 10)
	],
	"i don't know enough about you. (need relationship 10)", "close_window",
	[]],

	[anyone, "lord_ask_enter_service",
	[
		(set_show_messages, 0),
		(troop_get_slot, ":player_original_faction", "trp_player", slot_troop_original_faction),
		(val_div, ":player_original_faction", 37),
		(set_show_messages, 1),
		(lt, ":player_original_faction", 50)
	],
	"Honesty, your reputation is bad. if i had Recommend you to candidate, maybe it is not accepted. (need honor 50)", "close_window",
	[]],

	[anyone, "lord_ask_enter_service",
	[
		(troop_get_slot, ":player_last_comment_slot", "trp_player", slot_troop_last_comment_slot),
		(lt, ":player_last_comment_slot", 4)
	],
	"I think your lack of leadership is the problem. (need leadership 4)", "close_window",
	[]],

	[anyone, "lord_ask_enter_service",
	[
		(store_attribute_level, ":attribute_level_player_3", "trp_player", 3),
		(lt, ":attribute_level_player_3", 20)
	],
	"I think your leadership is poor. (need charisma 20)", "close_window",
	[]],

	[anyone, "lord_ask_enter_service",
	[
		(store_character_level, ":character_level_player", "trp_player"),
		(lt, ":character_level_player", 25)
	],
	"I think your lack of experience is the problem. (need level 25)", "close_window",
	[]],

	[anyone, "lord_ask_enter_service",
	[
		(this_or_next|eq, "$g_talk_troop_ego", 1),
		(eq, "$g_talk_troop_ego", 5),
		(store_mul, ":value", 1000, 10),
		(call_script, "script_party_money_level_ge", "p_main_party", ":value"),
		(neq, "$wm_mo_continue", 1)
	],
	"I think your lack of virtue is the problem. (he want money 10000)", "close_window",
	[]],

	[anyone, "lord_ask_enter_service",
	[
		(neq, "$g_talk_troop_ego", 1),
		(neq, "$g_talk_troop_ego", 5)
	],
	"I support the decide of you.", "join_faction",
	[]],

	[anyone, "lord_ask_enter_service",
	[
		(neq, "$g_talk_troop_ego", 1),
		(neq, "$g_talk_troop_ego", 5)
	],
	"I support the decide of you.", "join_faction",
	[]],

	[anyone, "join_faction",
	[],
	"Are you sure that you want join our faction?", "join_faction_2",
	[]],

	[anyone|plyr, "join_faction_2",
	[],
	"Yes, i am.", "join_faction_3",
	[]],

	[anyone|plyr, "join_faction_2",
	[],
	"Forgive me, I must give the matter more thought first...", "close_window",
	[]],

	[anyone, "join_faction_3",
	[],
	"Okay. i'll help you. you will receive small fief.", "join_faction_4",
	[]],

	[anyone|plyr, "join_faction_4",
	[
		(store_faction_of_troop, ":faction_of_troop_g_talk_troop", "$g_talk_troop"),
		(call_script, "script_ply_wayfarer_join_faction", ":faction_of_troop_g_talk_troop")
	],
	"Thank you. I don't forget about your grace.", "close_window",
	[]],

	[anyone|plyr, "lord_talk",
	[
		(troop_slot_ge, "trp_player", 18, 11),
		(neq, "$g_talk_troop_faction", "$wm_player_fac"),
		(neg|faction_slot_eq, "$wm_player_fac", 1, "trp_player"),
		(troop_slot_ge, "trp_player", 13, -10)
	],
	"I'd like to abandon my nation and join your country, are you able to assist me with that?", "lord_player_betray_1",
	[]],

	[anyone, "lord_player_betray_1",
	[
		(call_script, "script_check_faction_lord_list15_number", "$g_talk_troop_faction"),
		(neq, "$wm_stp_continue", 1)
	],
	"We have a lot of generals already.", "close_window",
	[]],

	[anyone, "lord_player_betray_1",
	[],
	"What? ha...haha!! Are you going to betray your country?", "lord_player_betray_2",
	[]],

	[anyone|plyr, "lord_player_betray_2",
	[],
	"Yes. I am.", "lord_player_betray_3",
	[]],

	[anyone|plyr, "lord_player_betray_2",
	[],
	"No. I'm just kidding.", "lord_player_betra_no",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -10),
		(call_script, "script_wm_honor_change_diff", "trp_player", 1, 34)
	]],

	[anyone, "lord_player_betra_no",
	[],
	"I never heard fucking joke like that.", "lord_talk",
	[]],

	[anyone, "lord_player_betray_3",
	[],
	"Okay. It is good news for our country. ", "lord_player_betray_4",
	[]],

	[anyone, "lord_player_betray_4",
	[],
	"Yes, yes, I can help you. except only one.  I cannot to defend you against blame.", "lord_player_betray_5",
	[]],

	[anyone|plyr, "lord_player_betray_5",
	[],
	"I'm already a traitor.", "lord_player_betray_6",
	[
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
			(try_end),
		(try_end),
		(assign, "$wm_player_fac", "$g_talk_troop_faction"),
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
		(assign, "$need_meeting_loose", 0)
	]],

	[anyone, "lord_player_betray_6",
	[],
	"Okay. at Last, I warn. Do not betray our country.", "close_window",
	[]],

	[anyone, "lord_propose_to_ply_1",
	[],
	"I was thinking for a long time. Please marry me.", "lord_propose_to_ply_2",
	[]],

	[anyone|plyr, "lord_propose_to_ply_2",
	[],
	"I've waited to say that.", "lord_propose_to_ply_3",
	[]],

	[anyone, "lord_propose_to_ply_3",
	[],
	"If so, do not have to wait. We must immediately proceed to the wedding.", "lord_propose_to_ply_4",
	[]],

	[anyone|plyr, "lord_propose_to_ply_4",
	[],
	"My husband, I hearby pledge to be your wife, to stand with you in good times and bad. May the heavens smile upon us and bless us with children, livestock, and land.", "lord_propose_to_ply_5",
	[]],

	[anyone, "lord_propose_to_ply_5",
	[],
	"I pledge the same. Let us be husband and wife.", "lord_propose_to_ply_6",
	[]],

	[anyone, "lord_propose_to_ply_6",
	[],
	"now declare you and i to be husband and wife.", "close_window",
	[
		(call_script, "script_courtship_event_bride_marry_groom", "trp_player", "$g_talk_troop"),
		(play_track, "track_wedding", 2),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_wedding_menu")
	]],

	[anyone|plyr, "marry_for_man_player_2",
	[],
	"Sorry. I have no words for it.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -50)
	]],

	[anyone|plyr, "lord_talk",
	[],
	" I must beg my leave.", "close_window",
	[
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", slot_party_type, 7),
			(jump_to_menu, "mnu_wm_pst_map_return"),
		(try_end)
	]],

	[anyone|plyr, "religionist_talk",
	[
		(try_begin),
			(eq, "$g_talk_troop", "trp_religionists_15"),
			(str_store_string, 8, "str_religion_title_1"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_42"),
			(str_store_string, 8, "str_religion_title_2"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_27"),
			(str_store_string, 8, "str_religion_title_3"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_34"),
			(str_store_string, 8, "str_religion_title_4"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_37"),
			(str_store_string, 8, "str_religion_title_5"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_23"),
			(str_store_string, 8, "str_religion_title_6"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_32"),
			(str_store_string, 8, "str_religion_title_7"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_31"),
			(str_store_string, 8, "str_religion_title_8"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_2"),
			(str_store_string, 8, "str_religion_title_9"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_22"),
			(str_store_string, 8, "str_religion_title_10"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_44"),
			(str_store_string, 8, "str_religion_title_11"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_43"),
			(str_store_string, 8, "str_religion_title_12"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_48"),
			(str_store_string, 8, "str_religion_title_13"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_45"),
			(str_store_string, 8, "str_religion_title_14"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_39"),
			(str_store_string, 8, "str_religion_title_15"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_47"),
			(str_store_string, 8, "str_religion_title_16"),
		(try_end),
		(eq, "$convert_possi", 0)
	],
	"I want to convert to {s8}.", "convert_1",
	[]],

	[anyone, "convert_1",
	[],
	"Are you sure? This is important thing. tell me the truth. You really want conversion?", "convert_2",
	[]],

	[anyone|plyr, "convert_2",
	[],
	"Yes. I really want.", "convert_3",
	[
		(try_begin),
			(eq, "$g_talk_troop", "trp_religionists_15"),
			(troop_set_slot, "trp_player", 23, 1),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_42"),
			(troop_set_slot, "trp_player", 23, 2),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_27"),
			(troop_set_slot, "trp_player", 23, 3),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_34"),
			(troop_set_slot, "trp_player", 23, 4),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_37"),
			(troop_set_slot, "trp_player", 23, 5),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_23"),
			(troop_set_slot, "trp_player", 23, 6),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_32"),
			(troop_set_slot, "trp_player", 23, 7),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_31"),
			(troop_set_slot, "trp_player", 23, 8),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_2"),
			(troop_set_slot, "trp_player", 23, 9),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_22"),
			(troop_set_slot, "trp_player", 23, 10),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_44"),
			(troop_set_slot, "trp_player", 23, 11),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_43"),
			(troop_set_slot, "trp_player", 23, 12),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_48"),
			(troop_set_slot, "trp_player", 23, 13),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_45"),
			(troop_set_slot, "trp_player", 23, 14),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_39"),
			(troop_set_slot, "trp_player", 23, 15),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_47"),
			(troop_set_slot, "trp_player", 23, 16),
		(try_end)
	]],

	[anyone|plyr, "convert_2",
	[],
	"Sorry. I can't afford that at the moment.", "close_window",
	[]],

	[anyone, "convert_3",
	[],
	"I believe your will. (He started a religious ceremony.) and now, you are one of follower.", "convert_4",
	[]],

	[anyone|plyr, "convert_4",
	[],
	"Thank you. You will not disappoint about me.", "close_window",
	[
		(try_begin),
			(eq, "$g_talk_troop", "trp_religionists_15"),
			(str_store_string, 8, "str_religion_title_1"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_42"),
			(str_store_string, 8, "str_religion_title_2"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_27"),
			(str_store_string, 8, "str_religion_title_3"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_34"),
			(str_store_string, 8, "str_religion_title_4"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_37"),
			(str_store_string, 8, "str_religion_title_5"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_23"),
			(str_store_string, 8, "str_religion_title_6"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_32"),
			(str_store_string, 8, "str_religion_title_7"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_31"),
			(str_store_string, 8, "str_religion_title_8"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_2"),
			(str_store_string, 8, "str_religion_title_9"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_22"),
			(str_store_string, 8, "str_religion_title_10"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_44"),
			(str_store_string, 8, "str_religion_title_11"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_43"),
			(str_store_string, 8, "str_religion_title_12"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_48"),
			(str_store_string, 8, "str_religion_title_13"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_45"),
			(str_store_string, 8, "str_religion_title_14"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_39"),
			(str_store_string, 8, "str_religion_title_15"),
		(else_try),
			(eq, "$g_talk_troop", "trp_religionists_47"),
			(str_store_string, 8, "str_religion_title_16"),
		(try_end),
		(assign, "$convert_possi", 3),
		(display_message, "str_convert_tip")
	]],

	[anyone|plyr, "religionist_talk",
	[],
	"  I must beg my leave.", "close_window",
	[]],

	[anyone|plyr, "lady_capture_1",
	[],
	"Of course you may leave.", "lady_capture_free",
	[]],

	[anyone, "lady_capture_free",
	[],
	"Thank you. my family also appreciate to you.", "close_window",
	[
		(call_script, "script_wm_player_relation_with_troop_family", "$g_talk_troop", 30),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 30),
		(call_script, "script_wm_honor_change_diff", "trp_player", 4, 87)
	]],

	[anyone|plyr, "lady_capture_1",
	[],
	"Write to your family, and ask them to hurry up with the ransom!", "lady_capture_ransom",
	#Potentional lord execution
	[]],

	[anyone, "lady_capture_ransom",
	[],
	"Thank you. I will write letter to the my family. right now.", "close_window",
	[
		(call_script, "script_wm_player_relation_with_troop_family", "$g_talk_troop", 5),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 5),
		(store_mul, ":value", 50, 100),
		(store_mul, ":value_2", 100, 100),
		(store_random_in_range, ":random_in_range_value_value_2", ":value", ":value_2"),
		(call_script, "script_party_money_level_diff", "p_main_party", ":random_in_range_value_value_2", 87)
	]],

	[anyone|plyr, "lady_capture_1",
	[
		(eq, "$adult_content", 1),
		(eq, "$player_gender", 0)
	],
	"Suck my dick! it is the payment for your free.", "lady_capture_bj_1",
	[]],

	[anyone, "lady_capture_bj_1",
	[],
	"What? I can not!", "lady_capture_bj_2",
	[]],

	[anyone|plyr, "lady_capture_bj_2",
	[],
	"I don't want to see blood. to act as I say.", "lady_capture_bj_3",
	[]],

	[anyone|plyr, "lady_capture_bj_2",
	[],
	"forget about it. you are free.", "close_window",
	[]],

	[anyone, "lady_capture_bj_3",
	[],
	"I will do as you command. Please do not kill me.", "lady_capture_bj_4",
	[
		(play_sound, "snd_cryyy_female")
	]],

	[anyone, "lady_capture_bj_4",
	[],
	".....", "lady_capture_bj_5",
	[
		(call_script, "script_molda_s_scene", 311, 0)
	]],

	[anyone, "lady_capture_bj_5",
	[],
	".....", "lady_capture_bj_6",
	[
		(call_script, "script_molda_s_scene", 311, 0)
	]],

	[anyone|plyr, "lady_capture_bj_6",
	[],
	"   [Squirt cum on the face]", "lady_capture_bj_6_face",
	[]],

	[anyone|plyr, "lady_capture_bj_6",
	[],
	"   [Squirt cum in mouth]", "lady_capture_bj_6_mouth",
	[]],

	[anyone, "lady_capture_bj_6_face",
	[],
	"(crying)", "lady_capture_bj_7",
	[
		(play_sound, "snd_cryyy_female"),
		(call_script, "script_molda_s_scene", 312, 0)
	]],

	[anyone, "lady_capture_bj_6_mouth",
	[],
	"(crying)", "lady_capture_bj_7",
	[
		(play_sound, "snd_cryyy_female"),
		(call_script, "script_molda_s_scene", 313, 0)
	]],

	[anyone|plyr, "lady_capture_bj_7",
	[],
	"Haha! good. please to notice to your family about this good news!", "lady_capture_bj_8",
	[]],

	[anyone, "lady_capture_bj_8",
	[],
	"No! I will not tell to anyone about it.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -99)
	]],

	[anyone|plyr, "lady_capture_1",
	[
		(gt, "$hidout_target_party", 0),
		(eq, "$adult_content", 1),
		(assign, ":var_1", 0),
		(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(troop_slot_eq, ":troop", slot_troop_leaded_party, 3),
			(val_add, ":var_1", 1),
		(try_end),
		(lt, ":var_1", 40)
	],
	"You are family of my enemy. and now you are my slave!", "lady_capture_slave_1",
	[]],

	[anyone, "lady_capture_slave_1",
	[],
	" No! please. I'm begging you for mercy", "lady_capture_slave_2",
	[]],

	[anyone|plyr, "lady_capture_slave_2",
	[],
	"I have no mercy. hey! soldiers! (She has dragged around like a dog.)", "lady_capture_slave_3",
	[
		(call_script, "script_wm_npc_family_set_revengeful", "$g_talk_troop"),
		(call_script, "script_wm_player_relation_with_troop_family", "$g_talk_troop", -99),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -99),
		(call_script, "script_wm_honor_change_diff", "trp_player", 15, 34),
		(play_sound, "snd_gbt_whip"),
		(play_sound, "snd_gbt_whip_hit"),
		(call_script, "script_slave_init_sett", "$g_talk_troop")
	]],

	[anyone|plyr, "lady_capture_slave_2",
	[],
	"Forget about it. you are free.", "close_window",
	[]],

	[anyone, "lady_capture_slave_3",
	[],
	" I damn you to hell! Our family will never forgive you!", "close_window",
	[]],

	[anyone|plyr, "lady_capture_1",
	[
		(eq, "$adult_content", 1),
		(eq, "$player_gender", 0),
		(troop_slot_ge, "$g_talk_troop", 3, "trp_tt_lord_01_00"),
		(neg|troop_slot_ge, "trp_player", 3, "trp_tt_lady_01_01")
	],
	" Forget about your husband. Now you will be my wife!", "lady_cap_marry_1",
	[]],

	[anyone|plyr, "lady_capture_1",
	[
		(eq, "$adult_content", 1),
		(eq, "$player_gender", 0),
		(neg|troop_slot_ge, "$g_talk_troop", 3, "trp_tt_lord_01_00"),
		(neg|troop_slot_ge, "trp_player", 3, "trp_tt_lady_01_01")
	],
	" Now you will be my wife!", "lady_cap_marry_1",
	[]],

	[anyone, "lady_cap_marry_1",
	[],
	" I cannot. I do not want to marry a cripple.", "lady_cap_marry_2",
	[]],

	[anyone|plyr, "lady_cap_marry_2",
	[],
	" I don't want to cutting off your neck. Obey my words. You are mine.", "lady_cap_marry_3",
	[
		(call_script, "script_wm_npc_family_set_revengeful", "$g_talk_troop"),
		(call_script, "script_wm_player_relation_with_troop_family", "$g_talk_troop", -99),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -99),
		(call_script, "script_courtship_event_bride_marry_groom", "$g_talk_troop", "trp_player"),
		(call_script, "script_wm_honor_change_diff", "trp_player", 15, 34)
	]],

	[anyone|plyr, "lady_cap_marry_2",
	[],
	"Forget about it. you are free.", "close_window",
	[]],

	[anyone, "lady_cap_marry_3",
	[
		(ge, "$random_succ_100_srand", 50)
	],
	" Please don't kill me.", "lady_cap_marry_4",
	[]],

	[anyone, "lady_cap_marry_3",
	[],
	" Noooooo!!", "lady_cap_marry_4",
	[]],

	[anyone|plyr, "lady_cap_marry_4",
	[],
	" Shut the fuck up. I'll teach you to act.", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_male_p_fuck_rape"),
		(assign, "$dark_quest_we_know", 1)
	]],

	[anyone|plyr, "lady_talk",
	[
		(gt, "$qquest_type", 0),
		(eq, "$qquest_report_troop", "$g_talk_troop"),
		(neq, "$qquest_progress", 1)
	],
	"  Sorry. I cannot keep our appointment.", "lady_quest_cancel",
	[]],

	[anyone, "lady_quest_cancel",
	[],
	"  Okay, then. It can't be helped. I'll find someone else.", "lady_talk",
	[
		(call_script, "script_qquest_initialize"),
		(play_sound, "snd_bad_drum"),
		(display_message, "str_questcancel"),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -3)
	]],

	[anyone|plyr, "lady_talk",
	[
		(eq, "$qquest_type", 32),
		(eq, "$qquest_report_troop", "$g_talk_troop"),
		(eq, "$qquest_progress", 1)
	],
	"  I have a good news.", "lord_lady_rescue_lord_end",
	[]],

	[anyone, "lord_lady_rescue_lord_end",
	[
		(str_store_troop_name, 8, "$qquest_target_troop")
	],
	"{playername}, you saved him! Thank you ever so much for rescuing my {s8}. Please, take this as some small repayment for your noble deed.", "lady_talk",
	[
		(call_script, "script_wm_after_battle_progress", 1000),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 35),
		(call_script, "script_wm_honor_change_diff", "trp_player", 4, 87),
		(store_mul, ":value", 1000, 10),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
		(call_script, "script_qquest_initialize"),
		(play_sound, "snd_experience_gained"),
		(call_script, "script_town_relation_diff", "$g_encountered_party", 1),
		(display_message, "str_questcomp")
	]],

	[anyone|plyr, "lady_talk",
	[
		(eq, "$qquest_type", 22),
		(eq, "$qquest_report_troop", "$g_talk_troop"),
		(eq, "$qquest_progress", 1)
	],
	" I have a good news.", "lord_lady_duel_req_end",
	[]],

	[anyone, "lord_lady_duel_req_end",
	[],
	"My dear {playername}, how joyous to see you again! I heard you gave that vile {s13} a well-deserved lesson. I hope he never forgets his humiliation. I've a reward for you, but I fear it's little compared to what you've done for me.", "lady_talk",
	[
		(call_script, "script_wm_after_battle_progress", 1000),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 35),
		(call_script, "script_wm_honor_change_diff", "trp_player", 4, 87),
		(store_mul, ":value", 1000, 10),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
		(call_script, "script_qquest_initialize"),
		(play_sound, "snd_experience_gained"),
		(call_script, "script_town_relation_diff", "$g_encountered_party", 1),
		(display_message, "str_questcomp")
	]],

	[anyone|plyr, "lady_talk",
	[
		(eq, "$qquest_type", 23),
		(eq, "$qquest_report_troop", "$g_talk_troop"),
		(eq, "$qquest_progress", 1),
		(str_store_troop_name, 13, "$qquest_target_troop")
	],
	"{s13} was knockdown. and her nurse's same.", "lord_lady_beat_end",
	[]],

	[anyone, "lord_lady_beat_end",
	[],
	"How joyous to see you again! I heard you gave that vile {s13} a well-deserved lesson. I hope she never forgets her humiliation. I've a reward for you, but I fear it's little compared to what you've done for me.", "lady_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 15),
		(call_script, "script_wm_honor_change_diff", "trp_player", 3, 34),
		(store_mul, ":value", 1000, 4),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
		(call_script, "script_qquest_initialize"),
		(play_sound, "snd_experience_gained"),
		(call_script, "script_town_relation_diff", "$g_encountered_party", 1),
		(display_message, "str_questcomp")
	]],

	[anyone|plyr, "lady_talk",
	[
		(eq, "$qquest_type", 24),
		(eq, "$qquest_report_troop", "$g_talk_troop"),
		(eq, "$qquest_progress", 1),
		(str_store_troop_name, 13, "$qquest_target_troop"),
		(str_store_troop_name, 14, "$qquest_target_faction")
	],
	"I came back. your husband {s13} has met with {s14}.", "lady_misdoubt_end_1",
	[]],

	[anyone, "lady_misdoubt_end_1",
	[],
	"Thank you for giving me the truth. From now on, I'll take care of it.", "lady_talk",
	[
		(store_random_in_range, ":random_in_range_0_10", 0, 10),
		(try_begin),
			(eq, ":random_in_range_0_10", 0),
			(call_script, "script_courtship_event_divorce", "$g_talk_troop", "$qquest_target_troop"),
		(try_end),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 15),
		(store_mul, ":value", 1000, 6),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
		(call_script, "script_qquest_initialize"),
		(play_sound, "snd_experience_gained"),
		(call_script, "script_town_relation_diff", "$g_encountered_party", 1),
		(display_message, "str_questcomp")
	]],

	[anyone|plyr, "lady_talk",
	[
		(eq, "$qquest_type", 24),
		(eq, "$qquest_report_troop", "$g_talk_troop"),
		(eq, "$qquest_progress", 2),
		(str_store_troop_name, 13, "$qquest_target_troop"),
		(str_store_troop_name, 14, "$qquest_target_faction")
	],
	"I had tracked him , there was nothing.", "lady_misdoubt_end_2",
	[]],

	[anyone, "lady_misdoubt_end_2",
	[],
	"Impossible. I'll take care of it by myself.", "lady_talk",
	[
		(store_mul, ":value", 1000, 1),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
		(call_script, "script_qquest_initialize"),
		(play_sound, "snd_experience_gained"),
		(display_message, "str_questcomp")
	]],

	[anyone|plyr, "lady_talk",
	[
		(this_or_next|eq, "$qquest_type", 21),
		(eq, "$qquest_type", 12),
		(eq, "$qquest_target_troop", "$g_talk_troop"),
		(str_store_troop_name, 9, "$qquest_report_troop")
	],
	"I have brought you a message from {s9}.", "lord_loveletter_end",
	[]],

	[anyone, "lord_loveletter_end",
	[],
	"Thank you so much!", "lady_talk",
	[
		(try_begin),
			(eq, "$qquest_type", 12),
			(store_random_in_range, ":random_in_range_0_20", 0, 20),
			(eq, ":random_in_range_0_20", 0),
			(call_script, "script_courtship_event_bride_marry_groom", "$qquest_target_troop", "$qquest_report_troop"),
			(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 25),
			(call_script, "script_change_player_relation_with_troop", "$qquest_report_troop", 50),
		(try_end),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 5),
		(call_script, "script_change_player_relation_with_troop", "$qquest_report_troop", 5),
		(store_add, ":value", 1000, 1000),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
		(call_script, "script_qquest_initialize"),
		(play_sound, "snd_experience_gained"),
		(call_script, "script_town_relation_diff", "$g_encountered_party", 1),
		(display_message, "str_questcomp")
	]],

	[anyone|plyr, "lady_talk",
	[
		(ge, "$g_talk_troop_faction_relation", 0),
		(eq, "$qquest_type", 0),
		(neq, "$g_talk_troop", "$player_spouse"),
		(troop_slot_ge, "$g_talk_troop", 20, 21),
		(neg|troop_slot_ge, "$g_talk_troop", 20, 25)
	],
	" Do you happen to have a job for me?", "lady_quest",
	[]],

	[anyone|plyr, "lady_talk",
	[
		(ge, "$g_talk_troop_faction_relation", 0),
		(eq, "$qquest_type", 0),
		(neq, "$g_talk_troop", "$player_spouse"),
		(assign, "$temp_num_01", 0),
		(assign, "$temp_num_02", 0),
		(assign, ":value", 0),
		(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
			(troop_slot_eq, ":troop", slot_troop_cur_center, 3),
			(call_script, "script_not_family_check", ":troop", "$g_talk_troop"),
			(eq, "$is_family", 1),
			(troop_get_slot, ":troop_present_at_event", ":troop", slot_troop_present_at_event),
			(is_between, ":troop_present_at_event", "p_pyongyang", "p_place_end"),
			(assign, ":value", 1),
			(assign, "$temp_num_01", ":troop"),
			(assign, "$temp_num_02", ":troop_present_at_event"),
		(try_end),
		(eq, ":value", 1),
		(gt, "$temp_num_01", 0),
		(gt, "$temp_num_02", 0)
	],
	" Why are you sad?", "lady_req_jailbreak_1",
	[]],

	[anyone|plyr, "lady_talk",
	[
		(eq, "$player_gender", 1),
		(eq, "$adult_content", 1),
		(neq, "$blowjob_sp_skill", 1),
		(eq, "$g_talk_troop", "trp_tt_lady_05_03")
	],
	"I heard your Blow job skill is very good.", "lady_cleo_oral_skill_1",
	[]],

	[anyone, "lady_cleo_oral_skill_1",
	[],
	"It's a fact. Everyone praise my oral sex skill.", "lady_cleo_oral_skill_2",
	[]],

	[anyone|plyr, "lady_cleo_oral_skill_2",
	[],
	"You can teach me this skill?", "lady_cleo_oral_skill_3",
	[]],

	[anyone, "lady_cleo_oral_skill_3",
	[
		(lt, "$g_talk_troop_relation", 70)
	],
	"Sorry. This skill, I will teach to my best friend.", "lady_talk",
	[]],

	[anyone, "lady_cleo_oral_skill_3",
	[],
	"You are my best friend. I will teach you.", "lady_talk",
	[
		(assign, "$blowjob_sp_skill", 1),
		(display_message, "str_art_bj1", 0x00ffff00),
		(display_message, "str_art_bj2", 0x00ffff00)
	]],

	[anyone|plyr, "lady_talk",
	[
		(eq, "$player_gender", 1),
		(eq, "$adult_content", 1),
		(neq, "$fuck_sp_skill", 1),
		(eq, "$g_talk_troop", "trp_tt_lady_ex_04")
	],
	"I heard your Vagina Fastening skill is very good.", "lady_diao_sex_skill_1",
	[]],

	[anyone, "lady_diao_sex_skill_1",
	[],
	"It's a fact. Everyone praise my sex skill.", "lady_diao_sex_skill_2",
	[]],

	[anyone|plyr, "lady_diao_sex_skill_2",
	[],
	"You can teach me this skill?", "lady_diao_sex_skill_3",
	[]],

	[anyone, "lady_diao_sex_skill_3",
	[
		(lt, "$g_talk_troop_relation", 70)
	],
	"Sorry. This skill, I will teach to my best friend.", "lady_talk",
	[]],

	[anyone, "lady_diao_sex_skill_3",
	[],
	"You are my best friend. I will teach you.", "lady_talk",
	[
		(assign, "$fuck_sp_skill", 1),
		(display_message, "str_art_puss1", 0x00ffff00),
		(display_message, "str_art_puss2", 0x00ffff00)
	]],

	[anyone|plyr, "lady_talk",
	[
		(neq, "$g_talk_troop", "$player_spouse")
	],
	"May I have the honor of knowing more about you, my lady?", "lady_backg_1",
	[]],

	[anyone, "lady_backg_1",
	[
		(str_clear, 6),
		(str_clear, 7),
		(str_clear, 8),
		(str_clear, 9),
		(str_clear, 10),
		(str_clear, 11),
		(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
			(try_begin),
				(troop_slot_eq, "$g_talk_troop", slot_troop_state, ":troop"),
				(str_store_troop_name, 11, ":troop"),
				(str_store_string, 8, "str_lady_backg_wife"),
			(else_try),
				(troop_slot_eq, "$g_talk_troop", slot_troop_last_talk_time, ":troop"),
				(str_store_troop_name, 11, ":troop"),
				(str_store_string, 9, "str_lady_backg_daughter"),
			(else_try),
				(troop_slot_eq, "$g_talk_troop", slot_troop_party_template, ":troop"),
				(str_store_troop_name, 11, ":troop"),
				(str_store_string, 10, "str_lady_backg_sister"),
			(try_end),
		(try_end),
		(try_for_range, ":troop_2", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(try_begin),
				(troop_slot_eq, ":troop_2", slot_troop_met, "$g_talk_troop"),
				(str_store_troop_name, 11, ":troop_2"),
				(str_store_string, 6, "str_lady_backg_mother"),
			(else_try),
				(troop_slot_eq, "$g_talk_troop", slot_troop_met, ":troop_2"),
				(str_store_troop_name, 11, ":troop_2"),
				(str_store_string, 7, "str_lady_backg_daughter"),
			(try_end),
		(try_end)
	],
	"{s8} {s6} {s7} {s9} {s10}", "lady_talk",
	[]],

	[anyone|plyr, "lady_talk",
	[
		(this_or_next|eq, "$wm_talk_state", 18),
		(eq, "$g_talk_troop", "$player_spouse"),
		(eq, "$attemp_commu", 0)
	],
	"I have something for you.", "lady_gift_1",
	[]],

	[anyone, "lady_gift_1",
	[],
	"What brings you here today?", "lady_gift_2",
	[]],

	[anyone|plyr, "lady_gift_2",
	[],
	"Sorry. nothing", "close_window",
	[]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_gift_2",
	[
		(player_has_item, 116),
		(str_store_item_name, 13, 116),
		(assign, "$temp", 116)
	],
	"Give a {s13} gift to her.", "lady_gift_3",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lady_gift_3",
	[],
	"oh {s13}? Thank you very much. I really appreciate for your kindness.", "lady_talk",
	[
		(try_begin),
			(eq, "$temp", 101),
			(assign, ":value", 15),
		(else_try),
			(eq, "$temp", 102),
			(assign, ":value", 8),
		(else_try),
			(eq, "$temp", 103),
			(assign, ":value", 8),
		(else_try),
			(eq, "$temp", 104),
			(assign, ":value", 8),
		(else_try),
			(eq, "$temp", 105),
			(assign, ":value", 8),
		(else_try),
			(eq, "$temp", 106),
			(assign, ":value", 7),
		(else_try),
			(eq, "$temp", 107),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 2),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 4),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 3),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 1),
			(party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 19),
			(assign, ":value", 10),
		(else_try),
			(eq, "$temp", 108),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 2),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 4),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 3),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 1),
			(party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 19),
			(assign, ":value", 10),
		(else_try),
			(eq, "$temp", 109),
			(assign, ":value", 15),
		(else_try),
			(eq, "$temp", 110),
			(assign, ":value", 15),
		(else_try),
			(eq, "$temp", 111),
			(assign, ":value", 15),
		(else_try),
			(eq, "$temp", 112),
			(assign, ":value", 8),
		(else_try),
			(eq, "$temp", 113),
			(assign, ":value", 10),
		(else_try),
			(eq, "$temp", 114),
			(assign, ":value", 10),
		(else_try),
			(eq, "$temp", 115),
			(assign, ":value", 15),
		(else_try),
			(eq, "$temp", 116),
			(assign, ":value", 15),
		(else_try),
			(assign, ":value", 8),
		(try_end),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", ":value")
	]],

	[anyone|plyr, "lady_talk",
	[
		(this_or_next|eq, "$wm_talk_state", 18),
		(eq, "$g_talk_troop", "$player_spouse"),
		(eq, "$attemp_commu", 0)
	],
	"  How do you do these days?", "member_comp_relation_talk",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_talk",
	[
		(neq, "$g_talk_troop", "$player_spouse"),
		(gt, "$g_talk_troop_relation", 49),
		(eq, "$wm_talk_state", 18),
		(eq, "$adult_content", 1),
		(eq, "$attemp_commu", 0),
		(eq, "$player_gender", 0)
	],
	"Whisper: Do you have time today night?", "lady_virgin_attem",
	[
		(assign, "$in_near_spouse", 0),
		(get_player_agent_no, ":player_agent_no"),
		(try_for_agents, ":var_2"),
			(neq, ":var_2", ":player_agent_no"),
			(agent_get_troop_id, ":troop_id_var_2", ":var_2"),
			(troop_slot_eq, "$g_talk_troop", slot_troop_state, ":troop_id_var_2"),
			(troop_slot_eq, ":troop_id_var_2", slot_troop_state, "$g_talk_troop"),
			(assign, "$in_near_spouse", 1),
		(try_end)
	]],

	[anyone|plyr, "lady_talk",
	[
		(eq, "$g_talk_troop", "$player_spouse"),
		(eq, "$wm_talk_state", 5),
		(eq, "$adult_content", 1),
		(eq, "$attemp_commu", 0),
		(eq, "$player_gender", 0)
	],
	"-Do you have time today night?", "lady_spouse",
	[]],

	[anyone, "lady_spouse",
	[
		(eq, "$g_talk_troop", "$player_spouse")
	],
	"Come to bedroom. honey", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_fuck_process_normal"),
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lady_virgin_attem",
	[
		(eq, "$in_near_spouse", 1)
	],
	"Whisper: You can't see my husband?", "lady_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -3),
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lady_virgin_attem",
	[
		(ge, "$g_talk_troop_relation", 50),
		(this_or_next|eq, "$g_talk_troop_ego", 14),
		(eq, "$g_talk_troop_ego", 13)
	],
	"(Whisper) Let's going outside first, and then we'll meet at secret place.", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_fuck_process_normal"),
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lady_virgin_attem",
	[
		(lt, "$g_talk_troop_relation", 75),
		(this_or_next|eq, "$g_talk_troop_ego", 11),
		(this_or_next|eq, "$g_talk_troop_ego", 12),
		(eq, "$g_talk_troop_ego", 15)
	],
	"I need to know more about you.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -3),
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lady_virgin_attem",
	[
		(ge, "$g_talk_troop_relation", 50),
		(this_or_next|eq, "$g_talk_troop_ego", 14),
		(eq, "$g_talk_troop_ego", 13)
	],
	"(Whisper) Let's going outside first, and then we'll meet at secret place.", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_fuck_process_normal"),
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lady_virgin_attem",
	[
		(lt, "$g_talk_troop_relation", 50),
		(this_or_next|eq, "$g_talk_troop_ego", 14),
		(eq, "$g_talk_troop_ego", 13)
	],
	"I need to know more about you.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -3),
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lady_virgin_attem",
	[],
	"We need to know more each other.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -3),
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lady_talk",
	[
		(call_script, "script_troop_type_sett", "$g_talk_troop"),
		(gt, "$troop_gender_type", 10),
		(eq, "$g_talk_troop", "$player_spouse")
	],
	"Don't you try to lie. You have a hidden lover. right?", "spouse_talk_relation_minus_1",
	[]],

	[anyone, "spouse_talk_relation_minus_1",
	[],
	"What?", "spouse_talk_relation_minus_2",
	[]],

	[anyone|plyr, "spouse_talk_relation_minus_2",
	[],
	"I want the right answer! (Assaulted Her)", "spouse_talk_relation_minus_3",
	[
		(play_sound, "snd_gbt_whip"),
		(play_sound, "snd_gbt_whip_hit"),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -20)
	]],

	[anyone|plyr, "spouse_talk_relation_minus_2",
	[],
	"It's a joke.", "close_window",
	[]],

	[anyone, "spouse_talk_relation_minus_3",
	[],
	"It's absurd. Why are you taking it out on me?", "spouse_talk_relation_minus_4",
	[]],

	[anyone|plyr, "spouse_talk_relation_minus_4",
	[],
	"Shut up bitch! Respect your husband!", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -20),
		(play_sound, "snd_cryyy_female")
	]],

	[anyone|plyr, "spouse_talk_relation_minus_4",
	[],
	"Enough.", "close_window",
	[]],

	[anyone|plyr, "lady_talk",
	[
		(eq, "$g_talk_troop", "$player_spouse"),
		(lt, "$g_talk_troop_relation", -24),
		(eq, "$attemp_commu", 0)
	],
	"Between you and I almost ended. I want divorce.", "spouse_talk_divorce_random",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "spouse_talk_divorce_random",
	[
		(store_random_in_range, ":random_in_range_0_2", 0, 2),
		(eq, ":random_in_range_0_2", 0)
	],
	"I can not. Do not tell me.", "close_window",
	[]],

	[anyone, "spouse_talk_divorce_random",
	[],
	"I agree. so, You'll need to prepare a lot of alimony huh?", "spouse_talk_divorce_choose1",
	[]],

	[anyone|plyr, "spouse_talk_divorce_choose1",
	[
		(store_mul, ":value", 1000, 15),
		(call_script, "script_party_money_level_ge", "p_main_party", ":value"),
		(eq, "$wm_mo_continue", 1)
	],
	"Alimony? Take everything. I don't want to meet you again.", "close_window",
	[
		(store_mul, ":value", 1000, 15),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 34),
		(call_script, "script_courtship_event_divorce", "$g_talk_troop", "trp_player"),
		(assign, "$Husband_first_time", 0)
	]],

	[anyone|plyr, "spouse_talk_divorce_choose1",
	[],
	"No. Just bullshit.", "close_window",
	[]],

	[anyone|plyr, "lady_talk",
	[
		(eq, "$g_talk_troop", "$player_spouse"),
		(eq, "$wm_talk_state", 5),
		(eq, "$player_gender", 0),
		(eq, "$talk_troop_gender", 1),
		(call_script, "script_wm_main_party_has_troop_sc", "$g_talk_troop"),
		(neq, "$wm_comp_continue", 1)
	],
	"I want you to join my party", "spouse_join",
	[]],

	[anyone, "spouse_join",
	[],
	"Of course my love!", "close_window",
	[
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone|plyr, "lady_talk",
	[
		(neg|troop_slot_ge, "trp_player", 3, "trp_tt_lord_01_00"),
		(neq, "$g_talk_troop", "$player_spouse"),
		(is_between, "$g_talk_troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(eq, "$wm_talk_state", 18),
		(ge, "$g_talk_troop_relation", 50),
		(eq, "$player_gender", 0),
		(eq, "$attemp_commu", 0)
	],
	"Today I want to talk seriously about our relationship.", "marry_for_man_player_1",
	[]],

	[anyone|plyr, "lady_talk",
	[],
	"   I must beg my leave.", "close_window",
	[]],

	[anyone|plyr, "lady_slave_prison",
	[
		(eq, "$player_gender", 0)
	],
	"Suck my dick! Slave!", "lady_slave_suck",
	[]],

	[anyone, "lady_slave_suck",
	[
		(this_or_next|eq, "$slave_attitude", 0),
		(eq, "$slave_attitude", 1)
	],
	"Fuck off dirty shit.", "lady_slave_suck_not",
	[]],

	[anyone|plyr, "lady_slave_suck_not",
	[],
	"[Whipped to her]", "lady_slave_whipped",
	[]],

	[anyone, "lady_slave_whipped",
	[],
	"!!!! Fuck!", "lady_slave_suck_yes",
	[
		(play_sound, "snd_gbt_whip"),
		(play_sound, "snd_gbt_whip_hit")
	]],

	[anyone|plyr, "lady_slave_suck_not",
	[],
	"[Leave]", "close_window",
	[]],

	[anyone, "lady_slave_suck_yes",
	[
		(this_or_next|eq, "$slave_attitude", 0),
		(eq, "$slave_attitude", 1)
	],
	"....", "lady_slave_suck_bite",
	[
		(call_script, "script_molda_s_scene", 111, 0)
	]],

	[anyone, "lady_slave_suck_yes",
	[],
	"....", "lady_slave_suck_yes_2",
	[
		(call_script, "script_molda_s_scene", 111, 0)
	]],

	[anyone|plyr, "lady_slave_suck_bite",
	[],
	"Oh....ow!....Argh !!!! my penis!", "lady_slave_suck_bite_1",
	[
		(play_sound, "snd_man_die"),
		(call_script, "script_wm_troop_wound_disease_slot", "trp_player", 3)
	]],

	[anyone, "lady_slave_suck_bite_1",
	[],
	"Hahahaha!!", "lady_slave_suck_bite_2",
	[]],

	[anyone|plyr, "lady_slave_suck_bite_2",
	[],
	"This fucking bitch!! I'll kill you!", "close_window",
	[
		(agent_set_team, "$g_talk_agent", 2),
		(agent_add_relation_with_agent, "$g_talk_agent", "$bt_player_agent", -1),
		(agent_ai_set_aggressiveness, "$g_talk_agent", 199),
		(try_for_agents, ":var_1"),
			(agent_get_troop_id, ":troop_id_var_1", ":var_1"),
			(neq, ":var_1", "$g_talk_agent"),
			(neq, ":var_1", "$bt_player_agent"),
			(neq, ":troop_id_var_1", "trp_hideout_warder"),
			(agent_start_running_away, ":var_1"),
		(try_end)
	]],

	[anyone|plyr, "lady_slave_suck_yes_2",
	[],
	"     Oh....ow!", "lady_slave_suck_yes_3",
	[]],

	[anyone, "lady_slave_suck_yes_3",
	[],
	"........      ", "lady_slave_suck_yes_4",
	[
		(call_script, "script_molda_s_scene", 111, 0)
	]],

	[anyone|plyr, "lady_slave_suck_yes_4",
	[],
	"    [Squirt cum on the face]", "lady_slave_suck_face",
	[]],

	[anyone|plyr, "lady_slave_suck_yes_4",
	[],
	"    [Squirt cum in mouth]", "lady_slave_suck_mouth",
	[]],

	[anyone, "lady_slave_suck_face",
	[],
	"!!!", "lady_slave_suck_after",
	[
		(call_script, "script_molda_s_scene", 112, 0)
	]],

	[anyone, "lady_slave_suck_mouth",
	[],
	"!!!", "lady_slave_suck_after",
	[
		(call_script, "script_molda_s_scene", 113, 0)
	]],

	[anyone, "lady_slave_suck_after",
	[
		(troop_get_slot, "$slave_attitude", "$g_talk_troop", slot_troop_age_appearance),
		(try_begin),
			(eq, "$slave_attitude", 5),
			(str_store_string, 11, "str_slave_state_5"),
			(str_store_string, 12, "str_slave_aftersuck_5"),
		(else_try),
			(eq, "$slave_attitude", 4),
			(str_store_string, 11, "str_slave_state_4"),
			(str_store_string, 12, "str_slave_aftersuck_4"),
		(else_try),
			(eq, "$slave_attitude", 3),
			(str_store_string, 11, "str_slave_state_3"),
			(str_store_string, 12, "str_slave_aftersuck_3"),
		(else_try),
			(eq, "$slave_attitude", 2),
			(str_store_string, 11, "str_slave_state_2"),
			(str_store_string, 12, "str_slave_aftersuck_2"),
		(else_try),
			(eq, "$slave_attitude", 1),
			(str_store_string, 11, "str_slave_state_1"),
			(str_store_string, 12, "str_slave_aftersuck_1"),
		(else_try),
			(eq, "$slave_attitude", 0),
			(str_store_string, 11, "str_slave_state_0"),
			(str_store_string, 12, "str_slave_aftersuck_0"),
		(try_end)
	],
	"({s11}) {s12}", "lady_slave_prison",
	[]],

	[anyone, "lady_slave_suck",
	[
		(this_or_next|eq, "$slave_attitude", 2),
		(eq, "$slave_attitude", 3)
	],
	"I know. there is no other choice.", "lady_slave_suck_yes",
	[]],

	[anyone, "lady_slave_suck",
	[],
	"Yes. my master.", "lady_slave_suck_yes",
	[]],

	[anyone|plyr, "lady_slave_prison",
	[
		(eq, "$player_gender", 0)
	],
	"Follow me. I want to talking with you.", "lady_slave_fuck",
	[]],

	[anyone, "lady_slave_fuck",
	[
		(this_or_next|eq, "$slave_attitude", 0),
		(eq, "$slave_attitude", 1)
	],
	"What the fucking talk? I'm not fool.", "lady_slave_fuck_no",
	[]],

	[anyone|plyr, "lady_slave_fuck_no",
	[],
	"[Whipped to her]", "lady_slave_fuck_whip",
	[]],

	[anyone, "lady_slave_fuck_whip",
	[],
	"!!!! Fuck!", "close_window",
	[
		(play_sound, "snd_gbt_whip"),
		(play_sound, "snd_gbt_whip_hit")
	]],

	[anyone|plyr, "lady_slave_fuck_no",
	[],
	"[Leave]", "close_window",
	[]],

	[anyone, "lady_slave_fuck",
	[
		(this_or_next|eq, "$slave_attitude", 2),
		(eq, "$slave_attitude", 3)
	],
	"......", "lady_slave_fuck_yes",
	[]],

	[anyone, "lady_slave_fuck",
	[],
	"Yes. my master.", "lady_slave_fuck_yes",
	[]],

	[anyone, "lady_slave_fuck_yes",
	[],
	"(You have going out with her)", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_male_p_fuck_rape")
	]],

	[anyone|plyr, "lady_slave_prison",
	[
		(eq, "$player_gender", 0),
		(troop_slot_ge, "$g_talk_troop", 3, 1),
		(neg|troop_slot_ge, "trp_player", 3, 1),
		(neq, "$slave_attitude", 0),
		(neq, "$slave_attitude", 1)
	],
	"  Forget about your husband. Now you will be my wife!", "lady_slavmarry_1",
	[]],

	[anyone|plyr, "lady_slave_prison",
	[
		(eq, "$player_gender", 0),
		(neg|troop_slot_ge, "$g_talk_troop", 3, 1),
		(neg|troop_slot_ge, "trp_player", 3, 1),
		(neq, "$slave_attitude", 0),
		(neq, "$slave_attitude", 1)
	],
	"  Now you will be my wife!", "lady_slavmarry_1",
	[]],

	[anyone, "lady_slavmarry_1",
	[
		(this_or_next|eq, "$slave_attitude", 2),
		(eq, "$slave_attitude", 3)
	],
	"  I cannot. I do not want to marry a cripple.", "lady_slavmarry_2",
	[]],

	[anyone, "lady_slavmarry_1",
	[],
	"Yes. I'm yours.", "lady_slavmarry_yes",
	[
		(call_script, "script_courtship_event_bride_marry_groom", "$g_talk_troop", "trp_player"),
		(call_script, "script_wm_honor_change_diff", "trp_player", 5, 34)
	]],

	[anyone|plyr, "lady_slavmarry_yes",
	[],
	"Good.", "close_window",
	[
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_wedding_menu")
	]],

	[anyone|plyr, "lady_slavmarry_2",
	[],
	"  I don't want to cutting off your neck. Obey my words. You are mine.", "lady_slavmarry_3",
	[]],

	[anyone|plyr, "lady_slavmarry_2",
	[],
	"Forget about it.", "close_window",
	[]],

	[anyone, "lady_slavmarry_3",
	[
		(ge, "$random_succ_100_srand", 50)
	],
	"  Please don't kill me.", "lady_slavmarry_4",
	[]],

	[anyone, "lady_slavmarry_3",
	[],
	"  Noooooo!!", "lady_slavmarry_4",
	[]],

	[anyone|plyr, "lady_slavmarry_4",
	[],
	"  Shut the fuck up. I'll teach you to act.", "close_window",
	[
		(call_script, "script_wm_npc_family_set_revengeful", "$g_talk_troop"),
		(call_script, "script_wm_player_relation_with_troop_family", "$g_talk_troop", -99),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -99),
		(call_script, "script_courtship_event_bride_marry_groom", "$g_talk_troop", "trp_player"),
		(call_script, "script_wm_honor_change_diff", "trp_player", 15, 34),
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_male_p_fuck_rape")
	]],

	[anyone|plyr, "lady_slave_prison",
	[
		(gt, "$brothel_target_party", 0),
		(this_or_next|eq, "$brothel_member_1", 0),
		(this_or_next|eq, "$brothel_member_2", 0),
		(this_or_next|eq, "$brothel_member_3", 0),
		(this_or_next|eq, "$brothel_member_4", 0),
		(this_or_next|eq, "$brothel_member_5", 0),
		(this_or_next|eq, "$brothel_member_6", 0),
		(eq, "$brothel_member_7", 0),
		(neq, "$brothel_member_1", "$g_talk_troop"),
		(neq, "$brothel_member_2", "$g_talk_troop"),
		(neq, "$brothel_member_3", "$g_talk_troop"),
		(neq, "$brothel_member_4", "$g_talk_troop"),
		(neq, "$brothel_member_5", "$g_talk_troop"),
		(neq, "$brothel_member_6", "$g_talk_troop"),
		(neq, "$brothel_member_7", "$g_talk_troop")
	],
	"I think you have the talent of prostitution. Get out and earn money for me.", "lady_slave_prostitution",
	[]],

	[anyone, "lady_slave_prostitution",
	[
		(this_or_next|eq, "$slave_attitude", 0),
		(eq, "$slave_attitude", 1)
	],
	"Fuck off. Disgusting monster. I'm never surrender to you.", "close_window",
	[]],

	[anyone, "lady_slave_prostitution",
	[
		(this_or_next|eq, "$slave_attitude", 2),
		(eq, "$slave_attitude", 3),
		(try_begin),
			(eq, "$brothel_member_1", 0),
			(assign, "$brothel_member_1", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_2", 0),
			(assign, "$brothel_member_2", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_3", 0),
			(assign, "$brothel_member_3", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_4", 0),
			(assign, "$brothel_member_4", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_5", 0),
			(assign, "$brothel_member_5", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_6", 0),
			(assign, "$brothel_member_6", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_7", 0),
			(assign, "$brothel_member_7", "$g_talk_troop"),
		(try_end),
		(str_store_troop_name, 8, "$g_talk_troop"),
		(display_message, "str_slave_move_brothel")
	],
	"There is no other choice.", "close_window",
	[
		(agent_fade_out, "$g_talk_agent")
	]],

	[anyone, "lady_slave_prostitution",
	[
		(eq, "$slave_attitude", 4),
		(try_begin),
			(eq, "$brothel_member_1", 0),
			(assign, "$brothel_member_1", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_2", 0),
			(assign, "$brothel_member_2", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_3", 0),
			(assign, "$brothel_member_3", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_4", 0),
			(assign, "$brothel_member_4", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_5", 0),
			(assign, "$brothel_member_5", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_6", 0),
			(assign, "$brothel_member_6", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_7", 0),
			(assign, "$brothel_member_7", "$g_talk_troop"),
		(try_end),
		(str_store_troop_name, 8, "$g_talk_troop"),
		(display_message, "str_slave_move_brothel")
	],
	"Yes. my master.", "close_window",
	[
		(agent_fade_out, "$g_talk_agent")
	]],

	[anyone, "lady_slave_prostitution",
	[
		(try_begin),
			(eq, "$brothel_member_1", 0),
			(assign, "$brothel_member_1", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_2", 0),
			(assign, "$brothel_member_2", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_3", 0),
			(assign, "$brothel_member_3", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_4", 0),
			(assign, "$brothel_member_4", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_5", 0),
			(assign, "$brothel_member_5", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_6", 0),
			(assign, "$brothel_member_6", "$g_talk_troop"),
		(else_try),
			(eq, "$brothel_member_7", 0),
			(assign, "$brothel_member_7", "$g_talk_troop"),
		(try_end),
		(str_store_troop_name, 8, "$g_talk_troop"),
		(display_message, "str_slave_move_brothel")
	],
	"Haha good! fuck me! fuck me harder! please!", "close_window",
	[
		(agent_fade_out, "$g_talk_agent")
	]],

	[anyone|plyr, "lady_slave_prison",
	[
		(gt, "$nakepit_target_party", 0),
		(this_or_next|eq, "$nakepit_member_1", 0),
		(this_or_next|eq, "$nakepit_member_2", 0),
		(this_or_next|eq, "$nakepit_member_3", 0),
		(eq, "$nakepit_member_4", 0),
		(neq, "$nakepit_member_1", "$g_talk_troop"),
		(neq, "$nakepit_member_2", "$g_talk_troop"),
		(neq, "$nakepit_member_3", "$g_talk_troop"),
		(neq, "$nakepit_member_4", "$g_talk_troop"),
		(store_attribute_level, ":attribute_level_g_talk_troop_0", "$g_talk_troop", 0),
		(lt, ":attribute_level_g_talk_troop_0", 10),
		(store_attribute_level, ":attribute_level_g_talk_troop_1", "$g_talk_troop", 1),
		(lt, ":attribute_level_g_talk_troop_1", 10)
	],
	"You will become good fighter. So, go to the 'fight pit' and earn money for me.", "lady_slave_fightpit",
	[]],

	[anyone, "lady_slave_fightpit",
	[
		(eq, "$slave_attitude", 0)
	],
	"Fuck off. I'm never surrender to you.", "close_window",
	[]],

	[anyone, "lady_slave_fightpit",
	[
		(this_or_next|eq, "$slave_attitude", 1),
		(this_or_next|eq, "$slave_attitude", 2),
		(eq, "$slave_attitude", 3),
		(try_begin),
			(eq, "$nakepit_member_1", 0),
			(assign, "$nakepit_member_1", "$g_talk_troop"),
		(else_try),
			(eq, "$nakepit_member_2", 0),
			(assign, "$nakepit_member_2", "$g_talk_troop"),
		(else_try),
			(eq, "$nakepit_member_3", 0),
			(assign, "$nakepit_member_3", "$g_talk_troop"),
		(else_try),
			(eq, "$nakepit_member_4", 0),
			(assign, "$nakepit_member_4", "$g_talk_troop"),
		(try_end),
		(str_store_troop_name, 8, "$g_talk_troop"),
		(display_message, "str_slave_move_fightpit")
	],
	"There is no other choice.", "close_window",
	[
		(agent_fade_out, "$g_talk_agent")
	]],

	[anyone, "lady_slave_prostitution",
	[
		(eq, "$slave_attitude", 4),
		(try_begin),
			(eq, "$nakepit_member_1", 0),
			(assign, "$nakepit_member_1", "$g_talk_troop"),
		(else_try),
			(eq, "$nakepit_member_2", 0),
			(assign, "$nakepit_member_2", "$g_talk_troop"),
		(else_try),
			(eq, "$nakepit_member_3", 0),
			(assign, "$nakepit_member_3", "$g_talk_troop"),
		(else_try),
			(eq, "$nakepit_member_4", 0),
			(assign, "$nakepit_member_4", "$g_talk_troop"),
		(try_end),
		(str_store_troop_name, 8, "$g_talk_troop"),
		(display_message, "str_slave_move_fightpit")
	],
	"Yes. my master.", "close_window",
	[
		(agent_fade_out, "$g_talk_agent")
	]],

	[anyone, "lady_slave_fightpit",
	[
		(try_begin),
			(eq, "$nakepit_member_1", 0),
			(assign, "$nakepit_member_1", "$g_talk_troop"),
		(else_try),
			(eq, "$nakepit_member_2", 0),
			(assign, "$nakepit_member_2", "$g_talk_troop"),
		(else_try),
			(eq, "$nakepit_member_3", 0),
			(assign, "$nakepit_member_3", "$g_talk_troop"),
		(else_try),
			(eq, "$nakepit_member_4", 0),
			(assign, "$nakepit_member_4", "$g_talk_troop"),
		(try_end),
		(str_store_troop_name, 8, "$g_talk_troop"),
		(display_message, "str_slave_move_fightpit")
	],
	"Haha....Fight?!", "close_window",
	[
		(agent_fade_out, "$g_talk_agent")
	]],

	[anyone|plyr, "lady_slave_prison",
	[
		(eq, "$hideout_build_torture", 1),
		(this_or_next|eq, "$torture_troop_1", 0),
		(this_or_next|eq, "$torture_troop_2", 0),
		(eq, "$torture_troop_3", 0),
		(neq, "$torture_troop_1", "$g_talk_troop"),
		(neq, "$torture_troop_2", "$g_talk_troop"),
		(neq, "$torture_troop_3", "$g_talk_troop")
	],
	"My soldiers will teach to you about good attitude.", "lady_slave_torture",
	[]],

	[anyone, "lady_slave_torture",
	[
		(this_or_next|eq, "$slave_attitude", 0),
		(eq, "$slave_attitude", 1),
		(try_begin),
			(eq, "$torture_troop_1", 0),
			(assign, "$torture_troop_1", "$g_talk_troop"),
		(else_try),
			(eq, "$torture_troop_2", 0),
			(assign, "$torture_troop_2", "$g_talk_troop"),
		(else_try),
			(eq, "$torture_troop_3", 0),
			(assign, "$torture_troop_3", "$g_talk_troop"),
		(try_end),
		(str_store_troop_name, 8, "$g_talk_troop"),
		(display_message, "str_slave_move_torture"),
		(play_sound, "snd_gbt_whip"),
		(play_sound, "snd_gbt_whip_hit")
	],
	"Disgusting monster. I'm never surrender to you.", "close_window",
	[
		(agent_fade_out, "$g_talk_agent")
	]],

	[anyone, "lady_slave_torture",
	[
		(this_or_next|eq, "$slave_attitude", 4),
		(this_or_next|eq, "$slave_attitude", 2),
		(eq, "$slave_attitude", 3),
		(try_begin),
			(eq, "$torture_troop_1", 0),
			(assign, "$torture_troop_1", "$g_talk_troop"),
		(else_try),
			(eq, "$torture_troop_2", 0),
			(assign, "$torture_troop_2", "$g_talk_troop"),
		(else_try),
			(eq, "$torture_troop_3", 0),
			(assign, "$torture_troop_3", "$g_talk_troop"),
		(try_end),
		(str_store_troop_name, 8, "$g_talk_troop"),
		(display_message, "str_slave_move_torture"),
		(play_sound, "snd_gbt_whip"),
		(play_sound, "snd_gbt_whip_hit")
	],
	"Oh no. Please Have mercy!", "close_window",
	[
		(agent_fade_out, "$g_talk_agent")
	]],

	[anyone, "lady_slave_torture",
	[
		(try_begin),
			(eq, "$torture_troop_1", 0),
			(assign, "$torture_troop_1", "$g_talk_troop"),
		(else_try),
			(eq, "$torture_troop_2", 0),
			(assign, "$torture_troop_2", "$g_talk_troop"),
		(else_try),
			(eq, "$torture_troop_3", 0),
			(assign, "$torture_troop_3", "$g_talk_troop"),
		(try_end),
		(str_store_troop_name, 8, "$g_talk_troop"),
		(display_message, "str_slave_move_torture")
	],
	"Haha good! fuck me! fuck me harder! please!", "close_window",
	[
		(agent_fade_out, "$g_talk_agent")
	]],

	[anyone|plyr, "lady_slave_prison",
	[],
	"I'll make you more comfortably. From now you are dancer for my guests.", "lady_slave_dancer",
	[]],

	[anyone, "lady_slave_dancer",
	[
		(this_or_next|eq, "$slave_attitude", 0),
		(eq, "$slave_attitude", 1)
	],
	"Fuck off. I never dance for you.", "close_window",
	[]],

	[anyone, "lady_slave_dancer",
	[
		(this_or_next|eq, "$slave_attitude", 2),
		(eq, "$slave_attitude", 3),
		(assign, "$wm_slave_dancer", "$g_talk_troop"),
		(str_store_troop_name, 8, "$g_talk_troop"),
		(display_message, "str_slave_move_dancer", 0x0000ff00),
		(agent_fade_out, "$g_talk_agent")
	],
	"I understand. There is no other choice.", "close_window",
	[]],

	[anyone, "lady_slave_dancer",
	[
		(assign, "$wm_slave_dancer", "$g_talk_troop"),
		(str_store_troop_name, 8, "$g_talk_troop"),
		(display_message, "str_slave_move_dancer", 0x0000ff00),
		(agent_fade_out, "$g_talk_agent")
	],
	"Yes, my master.", "close_window",
	[]],

	[anyone|plyr, "lady_slave_prison",
	[],
	"Write to your family, and ask them to hurry up with the ransom!", "lady_slave_prison_ransom_1",
	#Potentional lord execution
	[]],

	[anyone, "lady_slave_prison_ransom_1",
	[],
	"What? it is any kind of joke?", "lady_slave_prison_ransom_2",
	[]],

	[anyone|plyr, "lady_slave_prison_ransom_2",
	[],
	"Wow. you are so smart. yes it is joke.", "lady_slave_prison_ransom_2a",
	[]],

	[anyone, "lady_slave_prison_ransom_2a",
	[],
	"I'll kill you! fucking monster!", "close_window",
	[
		(agent_set_team, "$g_talk_agent", 2),
		(agent_add_relation_with_agent, "$g_talk_agent", "$bt_player_agent", -1),
		(agent_ai_set_aggressiveness, "$g_talk_agent", 199),
		(try_for_agents, ":var_1"),
			(agent_get_troop_id, ":troop_id_var_1", ":var_1"),
			(neq, ":var_1", "$g_talk_agent"),
			(neq, ":var_1", "$bt_player_agent"),
			(neq, ":troop_id_var_1", "trp_hideout_warder"),
			(agent_start_running_away, ":var_1"),
		(try_end)
	]],

	[anyone|plyr, "lady_slave_prison_ransom_2",
	[],
	"It is not a joke.", "lady_slave_prison_ransom_2b",
	[]],

	[anyone, "lady_slave_prison_ransom_2b",
	[],
	"I will write letter to the my family. right now.", "close_window",
	[
		(store_mul, ":value", 50, 100),
		(store_mul, ":value_2", 100, 100),
		(store_random_in_range, ":random_in_range_value_value_2", ":value", ":value_2"),
		(call_script, "script_party_money_level_diff", "p_main_party", ":random_in_range_value_value_2", 87),
		(call_script, "script_slave_freedom_execute", "$g_talk_troop"),
		(agent_fade_out, "$g_talk_agent")
	]],

	[anyone|plyr, "lady_slave_prison",
	[],
	"You will need praising my merciful. you are free now.", "lady_slave_free_1",
	[]],

	[anyone, "lady_slave_free_1",
	[],
	"What? it is any kind of joke?", "lady_slave_free_2",
	[]],

	[anyone|plyr, "lady_slave_free_2",
	[],
	"Wow. you are so smart. yes it is joke.", "lady_slave_free_2a",
	[]],

	[anyone, "lady_slave_free_2a",
	[],
	"I'll kill you! fucking monster!", "close_window",
	[
		(agent_set_team, "$g_talk_agent", 2),
		(agent_add_relation_with_agent, "$g_talk_agent", "$bt_player_agent", -1),
		(agent_ai_set_aggressiveness, "$g_talk_agent", 199),
		(try_for_agents, ":var_1"),
			(agent_get_troop_id, ":troop_id_var_1", ":var_1"),
			(neq, ":var_1", "$g_talk_agent"),
			(neq, ":var_1", "$bt_player_agent"),
			(neq, ":troop_id_var_1", "trp_hideout_warder"),
			(agent_start_running_away, ":var_1"),
		(try_end)
	]],

	[anyone|plyr, "lady_slave_free_2",
	[],
	"It is not a joke. you are free.", "lady_slave_free_2b",
	[]],

	[anyone, "lady_slave_free_2b",
	[],
	"Oh my god. I can't believe that! you...you... alright. (she seems to be patient about anger) I need to first get out of here.", "close_window",
	[
		(call_script, "script_slave_freedom_execute", "$g_talk_troop"),
		(agent_fade_out, "$g_talk_agent")
	]],

	[anyone|plyr, "lady_slave_prison",
	[],
	"[Leave]", "close_window",
	[]],

	[anyone|plyr, "hideout_warder_1",
	[],
	"weather is too hot. every slave need to take off clothes except underwear.", "hideout_warder_underwear",
	[]],

	[anyone, "hideout_warder_underwear",
	[],
	"Yes. today is too hot. I've done as you wish.", "close_window",
	[
		(try_for_agents, ":var_1"),
			(agent_is_alive, ":var_1"),
			(agent_get_troop_id, ":troop_id_var_1", ":var_1"),
			(try_begin),
				(is_between, ":troop_id_var_1", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(call_script, "script_molda_body_hand_set", ":troop_id_var_1", 1, ":var_1"),
			(try_end),
		(try_end)
	]],

	[anyone|plyr, "hideout_warder_1",
	[],
	"I want to watching my slave's body. Do not misunderstand. I'm just check about my slaves health.", "hideout_warder_nake",
	[]],

	[anyone, "hideout_warder_nake",
	[],
	"I completely agree with you. How could exist such a good opinion?", "close_window",
	[
		(try_for_agents, ":var_1"),
			(agent_is_alive, ":var_1"),
			(agent_get_troop_id, ":troop_id_var_1", ":var_1"),
			(try_begin),
				(is_between, ":troop_id_var_1", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(call_script, "script_molda_body_hand_set", ":troop_id_var_1", 0, ":var_1"),
			(try_end),
		(try_end)
	]],

	[anyone|plyr, "hideout_warder_1",
	[],
	"My slaves need to exercise. like dance. freely.", "hideout_warder_dance_notsame",
	[]],

	[anyone, "hideout_warder_dance_notsame",
	[],
	"I agree with you. exercise. good.", "close_window",
	[
		(try_for_agents, ":var_1"),
			(agent_is_alive, ":var_1"),
			(agent_get_troop_id, ":troop_id_var_1", ":var_1"),
			(troop_slot_ge, ":troop_id_var_1", 19, 3),
			(try_begin),
				(is_between, ":troop_id_var_1", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(store_random_in_range, ":random_in_range_0_4", 0, 4),
				(try_begin),
					(eq, ":random_in_range_0_4", 0),
					(agent_set_stand_animation, ":var_1", "anim_dancer_1"),
				(else_try),
					(eq, ":random_in_range_0_4", 1),
					(agent_set_stand_animation, ":var_1", "anim_dancer_2"),
				(else_try),
					(eq, ":random_in_range_0_4", 2),
					(agent_set_stand_animation, ":var_1", "anim_dancer_3"),
				(else_try),
					(agent_set_stand_animation, ":var_1", "anim_dancer_4"),
				(try_end),
			(try_end),
		(try_end)
	]],

	[anyone|plyr, "hideout_warder_1",
	[],
	"Every slave's health was weaken. therefore they need to exercise. example, like dance.", "hideout_warder_dance_same",
	[]],

	[anyone, "hideout_warder_dance_same",
	[],
	"I agree with you. exercise. good.", "close_window",
	[
		(store_random_in_range, ":random_in_range_0_4", 0, 4),
		(try_for_agents, ":var_2"),
			(agent_is_alive, ":var_2"),
			(agent_get_troop_id, ":troop_id_var_2", ":var_2"),
			(troop_slot_ge, ":troop_id_var_2", 19, 3),
			(try_begin),
				(is_between, ":troop_id_var_2", "trp_tt_lady_01_01", "trp_tt_lady_end"),
				(try_begin),
					(eq, ":random_in_range_0_4", 0),
					(agent_set_stand_animation, ":var_2", "anim_dancer_1"),
				(else_try),
					(eq, ":random_in_range_0_4", 1),
					(agent_set_stand_animation, ":var_2", "anim_dancer_2"),
				(else_try),
					(eq, ":random_in_range_0_4", 2),
					(agent_set_stand_animation, ":var_2", "anim_dancer_3"),
				(else_try),
					(agent_set_stand_animation, ":var_2", "anim_dancer_4"),
				(try_end),
			(try_end),
		(try_end)
	]],

	[anyone|plyr, "hideout_warder_1",
	[],
	"I'll leave.", "close_window",
	[]],

	[anyone, "hideout_torturer_1",
	[],
	"What can i help?", "hideout_torturer_2",
	[]],

	[anyone|repeat_for_troops|plyr, "hideout_torturer_2",
	[
		(store_repeat_object, ":repeat_object"),
		(is_between, ":repeat_object", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(troop_slot_eq, ":repeat_object", slot_troop_leaded_party, 3),
		(this_or_next|eq, ":repeat_object", "$torture_troop_1"),
		(this_or_next|eq, ":repeat_object", "$torture_troop_2"),
		(eq, ":repeat_object", "$torture_troop_3"),
		(str_store_troop_name, 1, ":repeat_object")
	],
	"How's {s1} doing?", "hideout_torturer_troop_info",
	[
		(store_repeat_object, "$temp")
	]],

	[anyone, "hideout_torturer_troop_info",
	[
		(troop_get_slot, "$slave_attitude", "$temp", slot_troop_age_appearance),
		(try_begin),
			(eq, "$slave_attitude", 5),
			(str_store_string, 11, "str_slave_state_5"),
			(str_store_string, 12, "str_slave_torture_5"),
		(else_try),
			(eq, "$slave_attitude", 4),
			(str_store_string, 11, "str_slave_state_4"),
			(str_store_string, 12, "str_slave_torture_4"),
		(else_try),
			(eq, "$slave_attitude", 3),
			(str_store_string, 11, "str_slave_state_3"),
			(str_store_string, 12, "str_slave_torture_3"),
		(else_try),
			(eq, "$slave_attitude", 2),
			(str_store_string, 11, "str_slave_state_2"),
			(str_store_string, 12, "str_slave_torture_2"),
		(else_try),
			(eq, "$slave_attitude", 1),
			(str_store_string, 11, "str_slave_state_1"),
			(str_store_string, 12, "str_slave_torture_1"),
		(else_try),
			(eq, "$slave_attitude", 0),
			(str_store_string, 11, "str_slave_state_0"),
			(str_store_string, 12, "str_slave_torture_0"),
		(try_end)
	],
	"({s11}) {s12}", "hideout_torturer_choose",
	[]],

	[anyone|plyr, "hideout_torturer_choose",
	[
		(this_or_next|eq, "$torture_room_stave", "$temp"),
		(this_or_next|eq, "$torture_room_gangbang", "$temp"),
		(this_or_next|eq, "$torture_room_corpse", "$temp"),
		(this_or_next|eq, "$torture_room_cage", "$temp"),
		(eq, "$torture_room_beat", "$temp")
	],
	"Stop work about her.", "hideout_torturer_done",
	[
		(try_begin),
			(eq, "$torture_room_stave", "$temp"),
			(assign, "$torture_room_stave", 0),
		(else_try),
			(eq, "$torture_room_gangbang", "$temp"),
			(assign, "$torture_room_gangbang", 0),
		(else_try),
			(eq, "$torture_room_corpse", "$temp"),
			(assign, "$torture_room_corpse", 0),
		(else_try),
			(eq, "$torture_room_cage", "$temp"),
			(assign, "$torture_room_cage", 0),
		(else_try),
			(eq, "$torture_room_beat", "$temp"),
			(assign, "$torture_room_beat", 0),
		(try_end)
	]],

	[anyone|plyr, "hideout_torturer_choose",
	[
		(eq, "$torture_room_stave", 0),
		(neq, "$torture_room_stave", "$temp"),
		(neq, "$torture_room_gangbang", "$temp"),
		(neq, "$torture_room_corpse", "$temp"),
		(neq, "$torture_room_cage", "$temp"),
		(neq, "$torture_room_beat", "$temp")
	],
	"Do not give food to her. only water permitted. and we need the smell by cooked pork.", "hideout_torturer_done",
	[
		(assign, "$torture_room_stave", "$temp")
	]],

	[anyone|plyr, "hideout_torturer_choose",
	[
		(eq, "$torture_room_gangbang", 0),
		(neq, "$torture_room_stave", "$temp"),
		(neq, "$torture_room_gangbang", "$temp"),
		(neq, "$torture_room_corpse", "$temp"),
		(neq, "$torture_room_cage", "$temp"),
		(neq, "$torture_room_beat", "$temp")
	],
	"I'll give to her the punishment. Gangbang her.", "hideout_torturer_done",
	[
		(assign, "$torture_room_gangbang", "$temp"),
		(try_begin),
			(troop_slot_eq, "$temp", slot_troop_last_persuasion_time, 1),
			(troop_set_slot, "$temp", slot_troop_last_persuasion_time, 0),
			(display_message, "str_gbt_virgin", 0x00ff0000),
			(str_store_troop_name, 8, "$temp"),
			(display_message, "str_gbt_virgin3", 0x00ff0000),
		(try_end)
	]],

	[anyone|plyr, "hideout_torturer_choose",
	[
		(eq, "$torture_room_corpse", 0),
		(neq, "$torture_room_stave", "$temp"),
		(neq, "$torture_room_gangbang", "$temp"),
		(neq, "$torture_room_corpse", "$temp"),
		(neq, "$torture_room_cage", "$temp"),
		(neq, "$torture_room_beat", "$temp")
	],
	"Use same room with the corpse.", "hideout_torturer_done",
	[
		(assign, "$torture_room_corpse", "$temp")
	]],

	[anyone|plyr, "hideout_torturer_choose",
	[
		(eq, "$torture_room_cage", 0),
		(neq, "$torture_room_stave", "$temp"),
		(neq, "$torture_room_gangbang", "$temp"),
		(neq, "$torture_room_corpse", "$temp"),
		(neq, "$torture_room_cage", "$temp"),
		(neq, "$torture_room_beat", "$temp")
	],
	"Put to the cage.", "hideout_torturer_done",
	[
		(assign, "$torture_room_cage", "$temp")
	]],

	[anyone|plyr, "hideout_torturer_choose",
	[
		(eq, "$torture_room_beat", 0),
		(neq, "$torture_room_stave", "$temp"),
		(neq, "$torture_room_gangbang", "$temp"),
		(neq, "$torture_room_corpse", "$temp"),
		(neq, "$torture_room_cage", "$temp"),
		(neq, "$torture_room_beat", "$temp")
	],
	"Use the club.", "hideout_torturer_done",
	[
		(assign, "$torture_room_beat", "$temp")
	]],

	[anyone|plyr, "hideout_torturer_choose",
	[
		(neq, "$torture_room_stave", "$temp"),
		(neq, "$torture_room_gangbang", "$temp"),
		(neq, "$torture_room_corpse", "$temp"),
		(neq, "$torture_room_cage", "$temp"),
		(neq, "$torture_room_beat", "$temp")
	],
	"She need send back to the prison.", "hideout_torturer_done",
	[
		(try_begin),
			(eq, "$torture_troop_1", "$temp"),
			(assign, "$torture_troop_1", 0),
		(else_try),
			(eq, "$torture_troop_2", "$temp"),
			(assign, "$torture_troop_2", 0),
		(else_try),
			(eq, "$torture_troop_3", "$temp"),
			(assign, "$torture_troop_3", 0),
		(try_end),
		(str_store_troop_name, 8, "$temp"),
		(display_message, "str_slave_move_prison")
	]],

	[anyone|plyr, "hideout_torturer_choose",
	[],
	"I want to talking about another slave.", "hideout_torturer_1",
	[]],

	[anyone, "hideout_torturer_done",
	[],
	"As your wish.", "close_window",
	[
		(assign, "$restart_cur_mission", 1),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_ply_hideout")
	]],

	[anyone|plyr, "hideout_torturer_2",
	[],
	"I'll leave.", "close_window",
	[]],

	[anyone|plyr, "hideout_chef_1",
	[
		(eq, "$wm_buying_drink_for_army", 0)
	],
	"I'd like to buy me and my men a barrel of your best Alcohol.", "hideout_chef_buy_drink",
	[]],

	[anyone, "hideout_chef_buy_drink",
	[],
	"Of course, {my lord/my lady}.", "close_window",
	[
		(assign, "$wm_buying_drink_for_army", 72),
		(assign, reg9, "$wm_buying_drink_for_army"),
		(display_message, "str_tavern_cool_add", 0x00ffff00),
		(call_script, "script_moral_level_diff", "p_main_party", 10),
		(play_sound, "snd_man_victory")
	]],

	[anyone|plyr, "hideout_chef_1",
	[],
	"I'll leave.", "close_window",
	[]],

	[anyone, "brothel_manager",
	[],
	"What can i help?", "brothel_manager_2",
	[]],

	[anyone|repeat_for_troops|plyr, "brothel_manager_2",
	[
		(store_repeat_object, ":repeat_object"),
		(is_between, ":repeat_object", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(troop_slot_eq, ":repeat_object", slot_troop_leaded_party, 3),
		(this_or_next|eq, ":repeat_object", "$brothel_member_1"),
		(this_or_next|eq, ":repeat_object", "$brothel_member_2"),
		(this_or_next|eq, ":repeat_object", "$brothel_member_3"),
		(this_or_next|eq, ":repeat_object", "$brothel_member_4"),
		(this_or_next|eq, ":repeat_object", "$brothel_member_5"),
		(this_or_next|eq, ":repeat_object", "$brothel_member_6"),
		(eq, ":repeat_object", "$brothel_member_7"),
		(str_store_troop_name, 1, ":repeat_object")
	],
	"How's {s1} doing?", "brothel_manager_3",
	[
		(store_repeat_object, "$temp")
	]],

	[anyone, "brothel_manager_3",
	[
		(troop_get_slot, "$slave_attitude", "$temp", slot_troop_age_appearance),
		(try_begin),
			(eq, "$slave_attitude", 5),
			(str_store_string, 11, "str_slave_state_5"),
			(str_store_string, 12, "str_slave_torture_5"),
		(else_try),
			(eq, "$slave_attitude", 4),
			(str_store_string, 11, "str_slave_state_4"),
			(str_store_string, 12, "str_slave_torture_4"),
		(else_try),
			(eq, "$slave_attitude", 3),
			(str_store_string, 11, "str_slave_state_3"),
			(str_store_string, 12, "str_slave_torture_3"),
		(else_try),
			(eq, "$slave_attitude", 2),
			(str_store_string, 11, "str_slave_state_2"),
			(str_store_string, 12, "str_slave_torture_2"),
		(else_try),
			(eq, "$slave_attitude", 1),
			(str_store_string, 11, "str_slave_state_1"),
			(str_store_string, 12, "str_slave_torture_1"),
		(else_try),
			(eq, "$slave_attitude", 0),
			(str_store_string, 11, "str_slave_state_0"),
			(str_store_string, 12, "str_slave_torture_0"),
		(try_end)
	],
	"({s11}) {s12}", "brothel_manager_4",
	[]],

	[anyone|plyr, "brothel_manager_4",
	[],
	"She need send back to the prison.", "brothel_manager_5",
	[
		(try_begin),
			(eq, "$brothel_member_1", "$temp"),
			(assign, "$brothel_member_1", 0),
		(else_try),
			(eq, "$brothel_member_2", "$temp"),
			(assign, "$brothel_member_2", 0),
		(else_try),
			(eq, "$brothel_member_3", "$temp"),
			(assign, "$brothel_member_3", 0),
		(else_try),
			(eq, "$brothel_member_4", "$temp"),
			(assign, "$brothel_member_4", 0),
		(else_try),
			(eq, "$brothel_member_1", "$temp"),
			(assign, "$brothel_member_1", 0),
		(else_try),
			(eq, "$brothel_member_5", "$temp"),
			(assign, "$brothel_member_5", 0),
		(else_try),
			(eq, "$brothel_member_6", "$temp"),
			(assign, "$brothel_member_6", 0),
		(else_try),
			(eq, "$brothel_member_7", "$temp"),
			(assign, "$brothel_member_7", 0),
		(try_end),
		(str_store_troop_name, 8, "$temp"),
		(display_message, "str_slave_move_prison")
	]],

	[anyone, "brothel_manager_5",
	[],
	"As your wish.", "close_window",
	[]],

	[anyone|plyr, "brothel_manager_4",
	[],
	"I want to talking about another slave.", "brothel_manager",
	[]],

	[anyone|plyr, "brothel_manager_2",
	[],
	"I'll leave.", "close_window",
	[]],

	[anyone, "nakepit_manager",
	[
		(gt, "$bet_troop_no", 0),
		(eq, "$pit_fight_begin", 0)
	],
	"Sorry. I need to declare to fight.", "close_window",
	[]],

	[anyone, "nakepit_manager",
	[
		(eq, "$pit_fight_begin", 1),
		(eq, "$pit_fight_winner_no", 0)
	],
	"Sorry. the fight is proceeding.", "close_window",
	[]],

	[anyone, "nakepit_manager",
	[
		(eq, "$pit_fight_begin", 1),
		(eq, "$pit_fight_winner_no", "$bet_troop_no"),
		(ge, "$bet_money_to_pit", 50)
	],
	"Congratulations. Your fighter is winner!", "close_window",
	[
		(store_mul, ":value", "$bet_money_to_pit", 4),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
		(assign, "$bet_money_to_pit", 0)
	]],

	[anyone, "nakepit_manager",
	[
		(eq, "$pit_fight_begin", 1),
		(neq, "$pit_fight_winner_no", "$bet_troop_no")
	],
	"Haha, unfortunately, your fighter was knockdown.", "close_window",
	[]],

	[anyone, "nakepit_manager",
	[
		(eq, "$pit_fight_begin", 1),
		(eq, "$bet_money_to_pit", 0)
	],
	"Have a good day.", "close_window",
	[]],

	[anyone, "nakepit_manager",
	[],
	"Do you wanna bet? ", "nakepit_manager_2",
	[]],

	[anyone|plyr, "nakepit_manager_2",
	[
		(eq, "$g_encountered_party", "p_nakepit_party")
	],
	"I want taking about my slave. ", "nakepit_manager_slave_list_1",
	[]],

	[anyone, "nakepit_manager_slave_list_1",
	[],
	"Okay.", "nakepit_manager_slave_list_2",
	[]],

	[anyone|repeat_for_troops|plyr, "nakepit_manager_slave_list_2",
	[
		(store_repeat_object, ":repeat_object"),
		(is_between, ":repeat_object", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(troop_slot_eq, ":repeat_object", slot_troop_leaded_party, 3),
		(this_or_next|eq, ":repeat_object", "$nakepit_member_1"),
		(this_or_next|eq, ":repeat_object", "$nakepit_member_2"),
		(this_or_next|eq, ":repeat_object", "$nakepit_member_3"),
		(eq, ":repeat_object", "$nakepit_member_4"),
		(str_store_troop_name, 1, ":repeat_object")
	],
	"How's {s1} doing?", "nakepit_manager_slave_list_3",
	[
		(store_repeat_object, "$temp")
	]],

	[anyone, "nakepit_manager_slave_list_3",
	[
		(troop_get_slot, "$slave_attitude", "$temp", slot_troop_age_appearance),
		(try_begin),
			(eq, "$slave_attitude", 5),
			(str_store_string, 11, "str_slave_state_5"),
			(str_store_string, 12, "str_slave_fightpit_5"),
		(else_try),
			(eq, "$slave_attitude", 4),
			(str_store_string, 11, "str_slave_state_4"),
			(str_store_string, 12, "str_slave_fightpit_4"),
		(else_try),
			(eq, "$slave_attitude", 3),
			(str_store_string, 11, "str_slave_state_3"),
			(str_store_string, 12, "str_slave_fightpit_3"),
		(else_try),
			(eq, "$slave_attitude", 2),
			(str_store_string, 11, "str_slave_state_2"),
			(str_store_string, 12, "str_slave_fightpit_2"),
		(else_try),
			(eq, "$slave_attitude", 1),
			(str_store_string, 11, "str_slave_state_1"),
			(str_store_string, 12, "str_slave_fightpit_1"),
		(else_try),
			(eq, "$slave_attitude", 0),
			(str_store_string, 11, "str_slave_state_0"),
			(str_store_string, 12, "str_slave_fightpit_0"),
		(try_end)
	],
	"({s11}) {s12}", "nakepit_manager_slave_list_4",
	[]],

	[anyone|plyr, "nakepit_manager_slave_list_4",
	[],
	"She need send back to the prison.", "nakepit_manager_back_prison",
	[
		(try_begin),
			(eq, "$nakepit_member_1", "$temp"),
			(assign, "$nakepit_member_1", 0),
		(else_try),
			(eq, "$nakepit_member_2", "$temp"),
			(assign, "$nakepit_member_2", 0),
		(else_try),
			(eq, "$nakepit_member_3", "$temp"),
			(assign, "$nakepit_member_3", 0),
		(else_try),
			(eq, "$nakepit_member_4", "$temp"),
			(assign, "$nakepit_member_4", 0),
		(try_end),
		(str_store_troop_name, 8, "$temp"),
		(display_message, "str_slave_move_prison")
	]],

	[anyone, "nakepit_manager_back_prison",
	[],
	"As your wish.", "close_window",
	[]],

	[anyone|plyr, "nakepit_manager_slave_list_4",
	[],
	"I want to talking about another thing.", "nakepit_manager",
	[]],

	[anyone|plyr, "nakepit_manager_slave_list_2",
	[],
	"I want to talking about another thing.", "nakepit_manager",
	[]],

	[anyone|plyr, "nakepit_manager_2",
	[
		(eq, "$bet_already", 0),
		(call_script, "script_party_money_level_ge", "p_main_party", 50),
		(eq, "$wm_mo_continue", 1)
	],
	"Yes I want spend some money. (bet 50d)", "nakepit_manager_bet",
	[
		(assign, "$bet_money_to_pit", 50)
	]],

	[anyone|plyr, "nakepit_manager_2",
	[
		(eq, "$bet_already", 0),
		(call_script, "script_party_money_level_ge", "p_main_party", 250),
		(eq, "$wm_mo_continue", 1)
	],
	"Yes I want spend some money. (bet 250d)", "nakepit_manager_bet",
	[
		(assign, "$bet_money_to_pit", 250)
	]],

	[anyone|plyr, "nakepit_manager_2",
	[
		(eq, "$bet_already", 0),
		(call_script, "script_party_money_level_ge", "p_main_party", 500),
		(eq, "$wm_mo_continue", 1)
	],
	"Yes I want spend some money. (bet 500d)", "nakepit_manager_bet",
	[
		(assign, "$bet_money_to_pit", 500)
	]],

	[anyone|plyr, "nakepit_manager_2",
	[
		(eq, "$bet_already", 0),
		(call_script, "script_party_money_level_ge", "p_main_party", 1000),
		(eq, "$wm_mo_continue", 1)
	],
	"Yes I want spend some money. (bet 1000d)", "nakepit_manager_bet",
	[
		(assign, "$bet_money_to_pit", 1000)
	]],

	[anyone, "nakepit_manager_bet",
	[],
	"Who can be winner? what is your think?", "nakepit_manager_bet_choose",
	[]],

	[anyone|plyr, "nakepit_manager_bet_choose",
	[],
	"Red Shield", "nakepit_manager_bet_okay",
	[
		(assign, "$bet_troop_no", "$pit_fighter_1"),
		(call_script, "script_party_money_level_diff", "p_main_party", "$bet_money_to_pit", 34),
		(assign, "$bet_already", 72),
		(assign, reg9, "$bet_already"),
		(display_message, "str_fight_pit_bet_cool_add", 0x00ffff00)
	]],

	[anyone|plyr, "nakepit_manager_bet_choose",
	[],
	"Red and Black Shield", "nakepit_manager_bet_okay",
	[
		(assign, "$bet_troop_no", "$pit_fighter_2"),
		(call_script, "script_party_money_level_diff", "p_main_party", "$bet_money_to_pit", 34),
		(assign, "$bet_already", 72),
		(assign, reg9, "$bet_already"),
		(display_message, "str_fight_pit_bet_cool_add", 0x00ffff00)
	]],

	[anyone|plyr, "nakepit_manager_bet_choose",
	[],
	"Black Shield", "nakepit_manager_bet_okay",
	[
		(assign, "$bet_troop_no", "$pit_fighter_3"),
		(call_script, "script_party_money_level_diff", "p_main_party", "$bet_money_to_pit", 34),
		(assign, "$bet_already", 72),
		(assign, reg9, "$bet_already"),
		(display_message, "str_fight_pit_bet_cool_add", 0x00ffff00)
	]],

	[anyone|plyr, "nakepit_manager_bet_choose",
	[],
	"Yellow Shield", "nakepit_manager_bet_okay",
	[
		(assign, "$bet_troop_no", "$pit_fighter_4"),
		(call_script, "script_party_money_level_diff", "p_main_party", "$bet_money_to_pit", 34),
		(assign, "$bet_already", 72),
		(assign, reg9, "$bet_already"),
		(display_message, "str_fight_pit_bet_cool_add", 0x00ffff00)
	]],

	[anyone|plyr, "nakepit_manager_bet_choose",
	[],
	"Never mind", "close_window",
	[]],

	[anyone, "nakepit_manager_bet_okay",
	[],
	"Good choice. the fight begin soon.", "close_window",
	[]],

	[anyone|plyr, "nakepit_manager_2",
	[],
	"I'll leave.", "close_window",
	[]],

	[anyone|plyr, "bath_manager",
	[
		(call_script, "script_party_money_level_ge", "p_main_party", 1),
		(eq, "$wm_mo_continue", 1)
	],
	"Milk. please.", "bath_manager_milk",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 1, 34)
	]],

	[anyone, "bath_manager_milk",
	[],
	"Thanks!", "close_window",
	[
		(play_sound, "snd_swalloww")
	]],

	[anyone|plyr, "bath_manager",
	[],
	"Nothing.", "close_window",
	[]],

	[anyone|plyr, "lord_ntr_1",
	[],
	"Yes, yes. congratulations.", "lord_ntr_2",
	[]],

	[anyone, "lord_ntr_2",
	[
		(play_sound, "snd_gbt_whip"),
		#(play_sound, "snd_man_hit")
	],
	"Shut your mouth. you can't speak without my permit.", "lord_ntr_3",
	[]],

	[anyone, "lord_ntr_3",
	[],
	"Oh. my lady. I meet you today first time.", "lord_ntr_4",
	[]],

	[anyone, "lord_ntr_4",
	[],
	"I assume that you, as a man of honor. me and my husband will be set free soon. right?", "lord_ntr_5",
	[
		(set_conversation_speaker_troop, "$meeting_add_troop_no")
	]],

	[anyone, "lord_ntr_5",
	[],
	"Me and my husband will be set free soon. right?", "lord_ntr_6",
	[
		(set_conversation_speaker_troop, "$meeting_add_troop_no")
	]],

	[anyone, "lord_ntr_6",
	[],
	"You assume wrong, my lady!", "lord_ntr_7",
	[]],

	[anyone, "lord_ntr_7",
	[],
	"What?! What infamy is this?", "lord_ntr_8",
	[
		(set_conversation_speaker_troop, "$meeting_add_troop_no")
	]],

	[anyone, "lord_ntr_8",
	[],
	"Infamy? Infamy? I'll show to you the 'real infamy'.", "lord_ntr_9",
	[]],

	[anyone, "lord_ntr_9",
	[],
	"!!!!!", "lord_ntr_10",
	[
		(play_sound, "snd_gbt_whip"),
		(play_sound, "snd_gbt_whip_hit"),
		(set_conversation_speaker_troop, "$meeting_add_troop_no")
	]],

	[anyone, "lord_ntr_10",
	[],
	"Suck my dick! if not, i will kill your husband.", "lord_ntr_11",
	[]],

	[anyone|plyr, "lord_ntr_11",
	[],
	"No!!!!", "lord_ntr_12",
	[]],

	[anyone, "lord_ntr_12",
	[],
	"What?", "lord_ntr_13",
	[
		(set_conversation_speaker_troop, "$meeting_add_troop_no")
	]],

	[anyone, "lord_ntr_13",
	[],
	"I already had command to you!", "lord_ntr_14",
	[
		(play_sound, "snd_gbt_whip"),
		(play_sound, "snd_gbt_whip_hit")
	]],

	[anyone|plyr, "lord_ntr_14",
	[],
	"Do not listen! I would rather die!", "lord_ntr_15",
	[]],

	[anyone, "lord_ntr_15",
	[],
	"If i do, you will release husband?", "lord_ntr_16",
	[
		(set_conversation_speaker_troop, "$meeting_add_troop_no")
	]],

	[anyone, "lord_ntr_16",
	[],
	"Haha. I promise.", "lord_ntr_17",
	[]],

	[anyone, "lord_ntr_17",
	[],
	".....", "lord_ntr_18",
	[
		(set_conversation_speaker_troop, "$meeting_add_troop_no"),
		(try_for_agents, ":var_1"),
			(agent_get_troop_id, ":troop_id_var_1", ":var_1"),
			(eq, ":troop_id_var_1", "$meeting_add_troop_no"),
			(agent_equip_item, ":var_1", 1399),
			(agent_set_stand_animation, ":var_1", "anim_blow_job"),
			(play_sound, "snd_blowjobbb"),
		(try_end)
	]],

	[anyone|plyr, "lord_ntr_18",
	[],
	"No!!", "lord_ntr_19",
	[]],

	[anyone, "lord_ntr_19",
	[],
	"Haha! good!", "lord_ntr_20",
	[]],

	[anyone, "lord_ntr_20",
	[],
	".....", "lord_ntr_21",
	[
		(set_conversation_speaker_troop, "$meeting_add_troop_no"),
		(try_for_agents, ":var_1"),
			(agent_get_troop_id, ":troop_id_var_1", ":var_1"),
			(eq, ":troop_id_var_1", "$meeting_add_troop_no"),
			(agent_equip_item, ":var_1", 1399),
			(agent_set_stand_animation, ":var_1", "anim_blow_job"),
			(play_sound, "snd_blowjobbb"),
		(try_end)
	]],

	[anyone, "lord_ntr_21",
	[],
	"Ug!", "lord_ntr_22",
	[
		(set_conversation_speaker_troop, "$meeting_add_troop_no"),
		(try_for_agents, ":var_1"),
			(agent_get_troop_id, ":troop_id_var_1", ":var_1"),
			(eq, ":troop_id_var_1", "$meeting_add_troop_no"),
			(store_random_in_range, ":random_in_range_0_2", 0, 2),
			(try_begin),
				(eq, ":random_in_range_0_2", 0),
				(agent_equip_item, ":var_1", 1468),
			(else_try),
				(agent_equip_item, ":var_1", 1469),
			(try_end),
			(stop_all_sounds, 0),
			(play_sound, "snd_mansatis"),
			(agent_set_stand_animation, ":var_1", "anim_stand_lady"),
		(try_end)
	]],

	[anyone, "lord_ntr_22",
	[],
	"You had promised. release my husband.", "lord_ntr_23",
	[
		(set_conversation_speaker_troop, "$meeting_add_troop_no")
	]],

	[anyone, "lord_ntr_23",
	[
		(troop_slot_ge, "$g_talk_troop", 3, "trp_tt_lady_01_01")
	],
	"Yes yes. I'll do that.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -99)
	]],

	[anyone, "lord_ntr_23",
	[],
	"Yes yes. I'll do that. however, you will follow with me.", "lord_ntr_24",
	[]],

	[anyone, "lord_ntr_24",
	[],
	"What? what's that means?", "lord_ntr_25",
	[
		(set_conversation_speaker_troop, "$meeting_add_troop_no")
	]],

	[anyone, "lord_ntr_25",
	[],
	"You are my loot. and now you are my spouse!", "lord_ntr_26",
	[]],

	[anyone|plyr, "lord_ntr_26",
	[],
	"I will kill you!", "lord_ntr_27",
	[]],

	[anyone, "lord_ntr_27",
	[],
	"No. you can't.", "lord_ntr_28",
	[
		(play_sound, "snd_gbt_whip"),
		#(play_sound, "snd_man_hit")
	]],

	[anyone, "lord_ntr_28",
	[
		(str_store_troop_name, 8, "trp_player")
	],
	"{s8}!", "lord_ntr_29",
	[
		(set_conversation_speaker_troop, "$meeting_add_troop_no")
	]],

	[anyone, "lord_ntr_29",
	[],
	"Stop! hey, soldiers! we will leave this place!", "lord_ntr_30",
	[
		(play_sound, "snd_gbt_whip"),
		(play_sound, "snd_gbt_whip_hit")
	]],

	[anyone, "lord_ntr_30",
	[
		(str_store_troop_name, 8, "trp_player")
	],
	"{s8}!", "lord_ntr_31",
	[
		(set_conversation_speaker_troop, "$meeting_add_troop_no")
	]],

	[anyone|plyr, "lord_ntr_31",
	[],
	"Nooooooo!!!", "close_window",
	[
		(stop_all_sounds, 0),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -99),
		(call_script, "script_wm_comp_separate", "$meeting_add_troop_no"),
		(call_script, "script_courtship_event_bride_marry_groom", "$meeting_add_troop_no", "$g_talk_troop"),
		(assign, "$meeting_add_troop_no", 0)
	]],

	[anyone|plyr, "female_ply_raped_1",
	[],
	"Yes, yes. congratulations.", "female_ply_raped_2",
	[]],

	[anyone, "female_ply_raped_2",
	[],
	"Congratulation? Haha. you can't imagine what happens next.", "female_ply_raped_3",
	[]],

	[anyone|plyr, "female_ply_raped_3",
	[],
	"What?", "close_window",
	[
		(assign, "$mt_action_on", 1),
		(assign, "$g_sex_troop_id", "$g_talk_troop"),
		(assign, "$need_rope_body", 1),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_mt_female_p_fuck_rape")
	]],

	[anyone|plyr, "traveler_talk",
	[
		(eq, "$main_q_step", 62)
	],
	"do you know about catholic kingdom of africa?", "mq_62_1",
	[]],

	[anyone, "mq_62_1",
	[],
	"Yes, maybe it is existed near massawa.", "mq_62_2",
	[]],

	[anyone|plyr, "mq_62_2",
	[],
	" Thank you very much.", "close_window",
	[
		(party_set_flags, "p_tradeport97", 256, 0),
		(assign, "$main_q_step", 63)
	]],

	[anyone|plyr, "traveler_talk",
	[
		(this_or_next|eq, "$main_q_step", 52),
		(eq, "$main_q_step", 53)
	],
	"Have you heard about 'Prester John'?", "mq_52_1",
	[]],

	[anyone, "mq_52_1",
	[
		(eq, "$g_encountered_party", "p_tola"),
		(eq, "$main_q_step", 53)
	],
	"I don't know about 'Prester John'. but I know about the warlord of Nestorian Christian.", "mq_52_a1",
	[]],

	[anyone|plyr, "mq_52_a1",
	[],
	"That warlord is who?", "mq_52_a2",
	[]],

	[anyone, "mq_52_a2",
	[],
	"Ong khan of Khereid. He is one of powerful warlord of meadows.", "mq_52_a3",
	[]],

	[anyone|plyr, "mq_52_a3",
	[],
	"Thank you very much. I must talk with him.", "mq_52_a4",
	[]],

	[anyone, "mq_52_a4",
	[
		(this_or_next|eq, "$start_age", 0),
		(eq, "$start_age", 1184)
	],
	"  Good luck.", "close_window",
	[
		(assign, "$main_q_step", 54),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_main_quest_menu")
	]],

	[anyone, "mq_52_a4",
	[],
	"Unfortunately, that is Impossible.", "mq_52_a5",
	[]],

	[anyone|plyr, "mq_52_a5",
	[],
	" what? why?", "mq_52_a6",
	[]],

	[anyone, "mq_52_a6",
	[],
	"He was dead four centuries ago. Now christians no one here.", "mq_52_a7",
	[]],

	[anyone|plyr, "mq_52_a7",
	[],
	"...All my efforts turned out to have been wasted.", "close_window",
	[
		(assign, "$main_q_step", 55),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_main_quest_menu")
	]],

	[anyone, "mq_52_1",
	[
		(party_slot_eq, "$g_encountered_party", slot_town_claimed_by_player, 10),
		(neq, "$g_encountered_party", "p_tola")
	],
	"I know, I know. I heard that believers of strange religions live in Tola.", "mq_52_22",
	[
		(assign, "$main_q_step", 53),
		(assign, "$main_q_party", "p_tola")
	]],

	[anyone|plyr, "mq_52_22",
	[],
	"Great! this information is really valuable.", "close_window",
	[]],

	[anyone, "mq_52_1",
	[],
	"I have heard that. Location? I don't know. Someone said that it is located Africa. another said that it is located more east. In my opinion, nomads may know about it.", "mq_52_33",
	[]],

	[anyone|plyr, "mq_52_33",
	[],
	"Good. thanks", "close_window",
	[]],

	[anyone|plyr, "traveler_talk",
	[
		(eq, "$main_q_step", 29),
		(neq, "$main_q_party", "$g_encountered_party")
	],
	"[Explain to him about the bandits]", "mq_29_1",
	[]],

	[anyone, "mq_29_1",
	[
		(ge, "$random_duel_offer", 75),
		(party_get_slot, ":g_encountered_party_town_center", "$g_encountered_party", slot_town_center),
		(assign, "$main_q_party", 0),
		(try_for_range, ":party", "p_pyongyang", "p_place_end"),
			(party_slot_eq, ":party", slot_town_center, ":g_encountered_party_town_center"),
			(try_begin),
				(eq, "$main_q_party", 0),
				(assign, "$main_q_party", ":party"),
			(else_try),
				(store_random_in_range, ":random_in_range_0_5", 0, 5),
				(eq, ":random_in_range_0_5", 0),
				(assign, "$main_q_party", ":party"),
			(try_end),
		(try_end),
		(is_between, "$main_q_party", "p_pyongyang", "p_place_end"),
		(str_store_party_name, 12, "$main_q_party")
	],
	"I heard about them from man of mercenary. If it isn't too late, he is in {s12}. His name is Gale.", "mq_29_2",
	[]],

	[anyone|plyr, "mq_29_2",
	[],
	"Thank you. I have to find him.", "close_window",
	[
		(assign, "$main_q_step", 30)
	]],

	[anyone, "mq_29_1",
	[],
	"I understand about those bastards. however i don't have any information.", "close_window",
	[
		(assign, "$main_q_party", "$g_encountered_party"),
		(call_script, "script_rand_glob_dice")
	]],

	[anyone|plyr, "traveler_talk",
	[],
	"Maybe then , you know about the ruins to come out in this book?", "traveler_talk_book_1",
	[]],

	[anyone|plyr, "traveler_talk",
	[],
	"Goodbye.", "close_window",
	[]],

	[anyone, "traveler_talk_book_1",
	[],
	"What book are you talking about?", "traveler_talk_book_2",
	[]],

	[anyone|plyr, "traveler_talk_book_2",
	[],
	"Nothing.", "close_window",
	[]],

	[anyone|repeat_for_parties|plyr, "traveler_talk_book_2",
	[
		(store_repeat_object, ":repeat_object"),
		(is_between, ":repeat_object", 1081, 1252),
		(player_has_item, ":repeat_object"),
		(str_store_item_name, 6, ":repeat_object")
	],
	"{s6}.", "traveler_talk_book_3",
	[
		(store_repeat_object, "$temp")
	]],

	[anyone, "traveler_talk_book_3",
	[
		(ge, "$random_succ_100_orand", 60),
		(store_sub, ":value", "$temp", 1081),
		(val_add, ":value", "str_r_name_001"),
		(str_store_string, 8, ":value")
	],
	"Hmm.. The name of the ruins in this book, probably [{s8}].  I don't know anymore.", "traveler_talk_book_4",
	[]],

	[anyone, "traveler_talk_book_3",
	[],
	"Oh dear. I don't know well.", "close_window",
	[]],

	[anyone|plyr, "traveler_talk_book_4",
	[],
	"It would be a helpful. Thank you.", "close_window",
	[]],

	[anyone|plyr, "temp_commander_talk",
	[
		(party_slot_eq, "$g_encountered_party", slot_party_type, 1),
		(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
		(neq, "$wm_player_fac", ":faction_of_party_g_encountered_party"),
		(neq, "$contract_fac", ":faction_of_party_g_encountered_party"),
		(store_random_in_range, ":random_in_range_attack_comment_01_attack_comment_end", "str_attack_comment_01", "str_attack_comment_end"),
		(str_store_string, 43, ":random_in_range_attack_comment_01_attack_comment_end")
	],
	"{s43}", "player_ambush_to_neutral_1",
	[]],

	[anyone|plyr, "temp_commander_talk",
	[],
	"Nevermind.", "close_window",
	[
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", slot_party_type, 7),
			(jump_to_menu, "mnu_wm_pst_map_return"),
		(try_end)
	]],

	[anyone, "player_ambush_to_neutral_1",
	[
		(store_random_in_range, ":random_in_range_unprovoked_attack_default_unprovoked_attack_end", "str_unprovoked_attack_default", "str_unprovoked_attack_end"),
		(str_store_string, 43, ":random_in_range_unprovoked_attack_default_unprovoked_attack_end"),
		(try_begin),
			(party_slot_eq, "$g_encountered_party", slot_party_type, 4),
			(str_store_string, 43, "str_innocent_comment"),
		(try_end)
	],
	"{s43}.", "player_ambush_to_neutral_2",
	[]],

	[anyone|plyr, "player_ambush_to_neutral_2",
	[],
	"Don't worry about that, I will have a lot to do with your spoils, prepare to die!", "close_window",
	[
		(call_script, "script_player_ambush_respond_sett", "$g_encountered_party"),
		(assign, "$wm_target_party", "$g_encountered_party"),
		(store_party_size_wo_prisoners, ":party_size_wo_prisoners_g_encountered_party", "$g_encountered_party"),
		(try_begin),
			(lt, ":party_size_wo_prisoners_g_encountered_party", 200),
			(jump_to_menu, "mnu_low_encounter"),
		(else_try),
			(jump_to_menu, "mnu_wm_attack_menu"),
		(try_end)
	]],

	[anyone|plyr, "player_ambush_to_neutral_2",
	[
		(eq, "$innocent_pay", 0),
		(party_slot_eq, "$g_encountered_party", slot_party_type, 4)
	],
	"I think maybe some of money can change current situation.", "attack_innocent_money",
	[]],

	[anyone|plyr, "player_ambush_to_neutral_2",
	[],
	"Sorry. I must have been out of my mind.", "close_window",
	[
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", slot_party_type, 7),
			(jump_to_menu, "mnu_wm_pst_map_return"),
		(try_end)
	]],

	[anyone|plyr, "caravan_master_talk",
	[
		(party_slot_eq, "$g_encountered_party", slot_party_type, 4),
		(store_faction_of_party, ":faction_of_party_g_encountered_party", "$g_encountered_party"),
		(neq, "$wm_player_fac", ":faction_of_party_g_encountered_party"),
		(neq, "$contract_fac", ":faction_of_party_g_encountered_party"),
		(store_random_in_range, ":random_in_range_attack_comment_01_attack_comment_end", "str_attack_comment_01", "str_attack_comment_end"),
		(str_store_string, 43, ":random_in_range_attack_comment_01_attack_comment_end")
	],
	"{s43}", "player_ambush_to_neutral_1",
	[]],

	[anyone|plyr, "caravan_master_talk",
	[],
	"Show me what you have for trading.", "caravan_master_trade",
	[]],

	[anyone, "caravan_master_trade",
	[],
	"As you wish.", "close_window",
	[
		(jump_to_menu, "mnu_trade_caravan_field")
	]],

	[anyone|plyr, "caravan_master_talk",
	[],
	"Goodbye.", "close_window",
	[
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", slot_party_type, 7),
			(jump_to_menu, "mnu_wm_pst_map_return"),
		(try_end)
	]],

	[anyone|plyr, "attack_innocent_1",
	[
		(store_random_in_range, ":random_in_range_attack_comment_01_attack_comment_end", "str_attack_comment_01", "str_attack_comment_end"),
		(str_store_string, 43, ":random_in_range_attack_comment_01_attack_comment_end")
	],
	"{s43}", "close_window",
	[
		(finish_mission),
		(assign, "$wm_target_party", "$g_encountered_party"),
		(store_party_size_wo_prisoners, ":party_size_wo_prisoners_g_encountered_party", "$g_encountered_party"),
		(try_begin),
			(lt, ":party_size_wo_prisoners_g_encountered_party", 200),
			(jump_to_menu, "mnu_low_encounter"),
		(else_try),
			(jump_to_menu, "mnu_wm_attack_menu"),
		(try_end)
	]],

	[anyone|plyr, "attack_innocent_1",
	[
		(eq, "$innocent_pay", 0)
	],
	"I think maybe some of money can change current situation.", "attack_innocent_money",
	[]],

	[anyone, "attack_innocent_money",
	[],
	"I'll give the money to you. Now we can go?", "close_window",
	[
		(assign, "$innocent_pay", 72),
		(assign, reg9, "$innocent_pay"),
		(display_message, "str_innocent_pay_cool_add", 0x00ffff00),
		(store_random_in_range, ":random_in_range_500_1000", 500, 1000),
		(val_add, ":random_in_range_500_1000", 500),
		(call_script, "script_party_money_level_diff", "p_main_party", ":random_in_range_500_1000", 87),
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", slot_party_type, 7),
			(jump_to_menu, "mnu_wm_pst_map_return"),
		(try_end)
	]],

	[anyone|plyr, "attack_innocent_1",
	[],
	"Get out of my sight.", "close_window",
	[
		(try_begin),
			(neg|party_slot_eq, "$g_encountered_party", slot_party_type, 7),
			(jump_to_menu, "mnu_wm_pst_map_return"),
		(try_end)
	]],

	[anyone|plyr, "lord_captured_1", #Lord execution
	[
		(neq, "$g_talk_troop", "$player_spouse")
	],
	"You're not going anywhere. You'll be my prisoner now!", "freed_hero_answer_1",
	[
		(store_conversation_troop, ":conversation_troop"),
		(party_force_add_prisoners, "p_main_party", ":conversation_troop", 1),
		(troop_set_slot, ":conversation_troop", slot_troop_cur_center, 2)
	]],

	[anyone, "freed_hero_answer_1",
	[],
	"Damn you. You will regret this.", "close_window",
	[]],

	[anyone|plyr, "lord_captured_1",
	[],
	"I demand a ransom to your country. This is my greatest mercy.", "lord_captured_ransom",
	[]],

	[anyone, "lord_captured_ransom",
	[],
	"Yes, yes, you're wise man. now you became rich. and i got freedom. it is perfectly fair!", "close_window",
	[
		(store_random_in_range, ":random_in_range_3000_7000", 3000, 7000),
		(call_script, "script_party_money_level_diff", "p_main_party", ":random_in_range_3000_7000", 87)
	]],

	[anyone|plyr, "lord_captured_1",
	[],
	"Of course, you can return to homeland.", "lord_captured_release",
	[]],

	[anyone, "lord_captured_release",
	[
		(store_random_in_range, ":random_in_range_prisoner_released_default_prisoner_released_end", "str_prisoner_released_default", "str_prisoner_released_end"),
		(str_store_string, 43, ":random_in_range_prisoner_released_default_prisoner_released_end")
	],
	"{s43}", "close_window",
	[
		(call_script, "script_wm_honor_change_diff", "trp_player", 4, 87),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 15)
	]],

	[anyone|plyr, "mq_46_1",
	[],
	"What happened in your village?", "mq_46_2",
	[]],

	[anyone, "mq_46_2",
	[],
	"That place was occupied by group of deserters. There are deserters of the much larger number than in fortress.", "mq_46_3",
	[]],

	[anyone|plyr, "mq_46_3",
	[],
	"I can sweep them for you. my lady", "mq_46_4",
	[]],

	[anyone|plyr, "mq_46_3",
	[],
	"You are lucky today. Murder is my hobby.", "mq_46_4",
	[]],

	[anyone, "mq_46_4",
	[],
	"Oh. Can you help our village? Thank you so much.", "close_window",
	[
		(assign, "$main_q_step", 47),
		(party_get_position, 11, "p_main_party"),
		(map_get_land_position_around_position, 12, 11, 2),
		(assign, ":var_1", "p_ruin_dummy_5"),
		(party_set_position, ":var_1", 12),
		(party_set_icon, ":var_1", "icon_wm_town_euro_1"),
		(party_set_flags, ":var_1", 256, 0),
		(party_set_flags, ":var_1", 524288, 0),
		(party_set_flags, ":var_1", 16384, 1),
		(str_store_troop_name, 14, "$main_q_troop"),
		(party_set_name, ":var_1", "str_mq_lady_vill"),
		(party_get_slot, ":last_visit_town_town_center", "$last_visit_town", slot_town_center),
		(party_set_slot, ":var_1", slot_town_center, ":last_visit_town_town_center")
	]],

	[anyone|plyr, "lady_rescue_1",
	[],
	"Of course my lady. I will escort you for safely.", "lady_resc_escort",
	[]],

	[anyone, "lady_resc_escort",
	[],
	"I really appreciate to you.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 40),
		(call_script, "script_wm_honor_change_diff", "trp_player", 2, 87),
		(assign, "$wm_quest_result", 1),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_quest_menu")
	]],

	[anyone|plyr, "lady_rescue_1",
	[
		(gt, "$hidout_target_party", 0),
		(eq, "$adult_content", 1),
		(neq, "$g_talk_troop_faction", "$wm_player_fac"),
		(assign, ":var_1", 0),
		(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(troop_slot_eq, ":troop", slot_troop_leaded_party, 3),
			(val_add, ":var_1", 1),
		(try_end),
		(lt, ":var_1", 40)
	],
	"I have a hobby of collecting female slaves. and now you are my slave!", "lady_resc_slave_1",
	[]],

	[anyone, "lady_resc_slave_1",
	[],
	"  No! please. I'm begging you for mercy", "lady_resc_slave_2",
	[]],

	[anyone|plyr, "lady_resc_slave_2",
	[],
	"I have no mercy. (She has dragged around like a dog.)", "lady_resc_slave_3",
	[
		(call_script, "script_wm_npc_family_set_revengeful", "$g_talk_troop"),
		(call_script, "script_wm_player_relation_with_troop_family", "$g_talk_troop", -99),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -99),
		(call_script, "script_wm_honor_change_diff", "trp_player", 15, 34),
		(play_sound, "snd_gbt_whip"),
		(play_sound, "snd_gbt_whip_hit"),
		(call_script, "script_slave_init_sett", "$g_talk_troop")
	]],

	[anyone, "lady_resc_slave_3",
	[],
	"  I damn you to hell! Our family will never forgive you!", "close_window",
	[
		(assign, "$wm_quest_result", 2),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_quest_menu")
	]],

	[anyone|plyr, "lady_rescue_1",
	[
		(eq, "$adult_content", 1),
		(eq, "$player_gender", 0),
		(troop_slot_ge, "$g_talk_troop", 3, "trp_tt_lord_01_00"),
		(neg|troop_slot_ge, "trp_player", 3, "trp_tt_lady_01_01")
	],
	"   Forget about your husband. Now you will be my wife!", "lady_resc_marry_1",
	[]],

	[anyone|plyr, "lady_rescue_1",
	[
		(eq, "$adult_content", 1),
		(eq, "$player_gender", 0),
		(neg|troop_slot_ge, "$g_talk_troop", 3, "trp_tt_lord_01_00"),
		(neg|troop_slot_ge, "trp_player", 3, "trp_tt_lady_01_01")
	],
	"   Now you will be my wife!", "lady_resc_marry_1",
	[]],

	[anyone, "lady_resc_marry_1",
	[],
	"   I cannot. I do not want to marry a cripple.", "lady_resc_marry_2",
	[]],

	[anyone|plyr, "lady_resc_marry_2",
	[],
	"   I don't want to cutting off your neck. Obey my words. You are mine.", "lady_resc_marry_3",
	[
		(call_script, "script_wm_npc_family_set_revengeful", "$g_talk_troop"),
		(call_script, "script_wm_player_relation_with_troop_family", "$g_talk_troop", -99),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -99),
		(call_script, "script_courtship_event_bride_marry_groom", "$g_talk_troop", "trp_player"),
		(call_script, "script_wm_honor_change_diff", "trp_player", 15, 34)
	]],

	[anyone, "lady_resc_marry_3",
	[
		(ge, "$random_succ_100_srand", 50)
	],
	"   Please don't kill me.", "lady_resc_marry_4",
	[]],

	[anyone, "lady_resc_marry_3",
	[],
	"   Noooooo!!", "lady_resc_marry_4",
	[]],

	[anyone|plyr, "lady_resc_marry_4",
	[],
	"   Shut the fuck up. I'll teach you to act.", "close_window",
	[
		(assign, "$wm_quest_result", 2),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_quest_menu")
	]],

	[anyone|plyr, "bard_talk",
	[
		(eq, "$adult_content", 1),
		(eq, "$player_gender", 0),
		(assign, "$pst_target_no", 0),
		(party_get_slot, ":g_encountered_party_town_center", "$g_encountered_party", slot_town_center),
		(call_script, "script_temp_save_number11_initialize"),
		(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
			(eq, ":faction_of_troop_troop", ":g_encountered_party_town_center"),
			(troop_slot_eq, ":troop", slot_troop_last_persuasion_time, 1),
			(neg|troop_slot_eq, ":troop", slot_troop_leaded_party, 3),
			(neg|troop_slot_eq, "trp_player", slot_troop_state, ":troop"),
			(call_script, "script_temp_save_number11_inject", ":troop"),
		(try_end),
		(call_script, "script_temp_save_number11_choice_rand"),
		(try_begin),
			(is_between, "$wm_target_number11", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(assign, "$pst_target_no", "$wm_target_number11"),
		(try_end),
		(is_between, "$pst_target_no", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(str_store_troop_name, 8, "$pst_target_no")
	],
	"Is there something interesting?", "bard_quest_1",
	[]],

	[anyone, "bard_quest_1",
	[],
	"Of course. There is one of the interesting facts, lady {s8} of this country is still called 'virgin'.", "bard_quest_2",
	[]],

	[anyone, "bard_quest_2",
	[],
	"I want to know the truth of this lady. However , I do not want to fall in danger. I need find other trustworthy person.", "bard_quest_3",
	[]],

	[anyone, "bard_quest_3",
	[],
	"So , are you interested in this job? I prepared a great reward.", "bard_quest_4",
	[]],

	[anyone|plyr, "bard_quest_4",
	[],
	"I can try. I will not come back until destroy the hymen of {s8}. Having expectations!", "bard_quest_5",
	[]],

	[anyone, "bard_quest_5",
	[],
	"Haha. You are the man!", "close_window",
	[
		(assign, "$bard_quest_target", "$pst_target_no"),
		(assign, "$bard_quest_party", "$g_encountered_party"),
		(assign, "$bard_quest_state", 1)
	]],

	[anyone|plyr, "bard_quest_4",
	[],
	"i'm not a flirt. Goodbye.", "close_window",
	[]],

	[anyone|plyr, "bard_talk",
	[
		(eq, "$bard_quest_party", "$g_encountered_party"),
		(eq, "$bard_quest_state", 1)
	],
	"I came in order to cancel your suggestions.", "bard_quest_cancel",
	[]],

	[anyone|plyr, "bard_quest_cancel",
	[],
	"Alright, I understand you..", "close_window",
	[
		(assign, "$bard_quest_target", 0),
		(assign, "$bard_quest_party", 0),
		(assign, "$bard_quest_state", 0)
	]],

	[anyone|plyr, "bard_talk",
	[
		(eq, "$bard_quest_party", "$g_encountered_party"),
		(eq, "$bard_quest_state", 2),
		(str_store_troop_name, 8, "$bard_quest_target")
	],
	"I have checked! lady {s8} was a real virgin.", "bard_quest_succ",
	[]],

	[anyone|plyr, "bard_quest_succ",
	[],
	"Oh my god! It is just a joke. However , I will give you a reward.", "close_window",
	[
		(call_script, "script_adv_exp_diff", 1000, 87),
		(assign, "$bard_quest_target", 0),
		(assign, "$bard_quest_party", 0),
		(assign, "$bard_quest_state", 0)
	]],

	[anyone|plyr, "bard_talk",
	[],
	"Goodbye.", "close_window",
	[]],

	[anyone, "tavernkeeper_quest",
	[
		(party_slot_eq, "$g_encountered_party", slot_town_merchant, 1),
		(call_script, "script_temp_save_number11_initialize"),
		(try_for_range, ":party", "p_pyongyang", "p_place_end"),
			(neq, ":party", "$g_encountered_party"),
			(store_faction_of_party, ":faction_of_party_party", ":party"),
			(store_relation, ":relation_faction_of_party_party_wm_player_fac", ":faction_of_party_party", "$wm_player_fac"),
			(ge, ":relation_faction_of_party_party_wm_player_fac", 0),
			(store_distance_to_party_from_party, ":distance_to_party_from_party_party_g_encountered_party", ":party", "$g_encountered_party"),
			(is_between, ":distance_to_party_from_party_party_g_encountered_party", 80, 150),
			(call_script, "script_temp_save_number11_inject", ":party"),
		(try_end),
		(call_script, "script_temp_save_number11_choice_rand"),
		(is_between, "$wm_target_number11", "p_pyongyang", "p_place_end"),
		(str_store_party_name, 4, "$wm_target_number11"),
		(assign, reg8, 2000)
	],
	"I have a cargo of Alcohol that needs to be delivered to the tavern in {s4}. If you can take 10 units of Alcohol to {s4} in 10 days, you may earn {reg8} denars. What do you say?", "tavernkeeper_alcohol",
	[]],

	[anyone|plyr, "tavernkeeper_alcohol",
	[],
	"Alright. I will make the delivery.", "close_window",
	[
		(assign, "$qquest_type", 1),
		(assign, "$qquest_progress", 0),
		(assign, "$qquest_report_party", "$g_encountered_party"),
		(assign, "$qquest_report_troop", 0),
		(assign, "$qquest_target_party", "$wm_target_number11"),
		(assign, "$qquest_target_troop", 0),
		(assign, "$qquest_target_faction", 0),
		(assign, "$qquest_time_day", 10),
		(play_sound, "snd_quest_taken"),
		(display_message, "str_questget", 0x00ffff00),
		(party_set_slot, "$g_encountered_party", slot_town_merchant, 0)
	]],

	[anyone|plyr, "tavernkeeper_alcohol",
	[],
	"I am afraid I can't carry all that cargo now.", "close_window",
	[]],

	[anyone, "tavernkeeper_quest",
	[
		(party_slot_eq, "$g_encountered_party", slot_town_merchant, 2),
		(call_script, "script_temp_save_number11_initialize"),
		(try_for_range, ":party", "p_pyongyang", "p_place_end"),
			(neq, ":party", "$g_encountered_party"),
			(store_faction_of_party, ":faction_of_party_party", ":party"),
			(store_relation, ":relation_faction_of_party_party_wm_player_fac", ":faction_of_party_party", "$wm_player_fac"),
			(ge, ":relation_faction_of_party_party_wm_player_fac", 0),
			(store_distance_to_party_from_party, ":distance_to_party_from_party_party_g_encountered_party", ":party", "$g_encountered_party"),
			(is_between, ":distance_to_party_from_party_party_g_encountered_party", 25, 100),
			(call_script, "script_temp_save_number11_inject", ":party"),
		(try_end),
		(call_script, "script_temp_save_number11_choice_rand"),
		(is_between, "$wm_target_number11", "p_pyongyang", "p_place_end"),
		(str_store_party_name, 4, "$wm_target_number11"),
		(assign, reg8, 2500)
	],
	"I have something you could help with, an issue with the lawless villain.  He murdered one of innocent men and has been on the run from his judgment ever since. Guild put a bounty of {reg8} denars on his head. Friends of the murdered man reckon that this assassin may have taken refuge with his kinsmen at {s4}. You might be able to hunt him down and give him what he deserves, and claim the bounty for yourself.", "tavernkeeper_headhunt",
	[]],

	[anyone|plyr, "tavernkeeper_headhunt",
	[],
	"Then I will hunt him down and execute the law.", "close_window",
	[
		(assign, "$qquest_type", 2),
		(assign, "$qquest_progress", 0),
		(assign, "$qquest_report_party", "$g_encountered_party"),
		(assign, "$qquest_report_troop", 0),
		(assign, "$qquest_target_party", "$wm_target_number11"),
		(assign, "$qquest_target_troop", 0),
		(assign, "$qquest_target_faction", 0),
		(assign, "$qquest_time_day", 15),
		(play_sound, "snd_quest_taken"),
		(display_message, "str_questget", 0x00ffff00),
		(party_set_slot, "$g_encountered_party", slot_town_merchant, 0)
	]],

	[anyone|plyr, "tavernkeeper_headhunt",
	[],
	"I am too busy to go after him at the moment.", "close_window",
	[]],

	[plyr|trp_fugitive, "fugitive_1",
	[],
	"I am looking for a murderer. You fit his description.", "fugitive_2",
	[]],

	[plyr|trp_fugitive, "fugitive_1",
	[],
	"Nothing. Sorry to trouble you.", "close_window",
	[]],

	[trp_fugitive, "fugitive_2",
	[],
	"I don't understand, {sir/madam}. I never killed anyone. I think you've got the wrong man.", "fugitive_3",
	[]],

	[plyr|trp_fugitive, "fugitive_3",
	[],
	"Then drop your weapon. If you are innocent, you have nothing to fear. We'll go now and talk to your neighbours, and if they verify your story, I'll go on my way.", "fugitive_4",
	[]],

	[anyone, "fugitive_4",
	[],
	"I'm not going anywhere, friend. You're going to have to fight for your silver, today.", "fugitive_5",
	[]],

	[plyr|trp_fugitive, "fugitive_5",
	[],
	"No problem. I really just need your head, anyway.", "fugitive_fight_start",
	[]],

	[plyr|trp_fugitive, "fugitive_5",
	[],
	"I come not for money, but to execute the law!", "fugitive_fight_start",
	[]],

	[plyr|trp_fugitive, "fugitive_5",
	[],
	"Alas, that you cannot be made to see reason.", "fugitive_fight_start",
	[]],

	[anyone, "fugitive_fight_start",
	[],
	"Die, dog!", "close_window",
	[
		(set_party_battle_mode),
		(try_for_agents, ":var_1"),
			(agent_get_troop_id, ":troop_id_var_1", ":var_1"),
			(eq, ":troop_id_var_1", "trp_fugitive"),
			(agent_set_team, ":var_1", 4),
			(agent_ai_set_aggressiveness, ":var_1", 199),
			(agent_set_is_alarmed, ":var_1", 1),
		(try_end)
	]],

	[anyone, "tavernkeeper_quest",
	[],
	" Unfortunately, There is no job to for you.", "tavernkeeper_talk",
	[]],

	[anyone, "lord_quest",
	[
		(troop_slot_eq, "$g_talk_troop", slot_troop_does_not_give_quest, 11),
		(call_script, "script_temp_save_number11_initialize"),
		(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
			(neq, ":troop", "$g_talk_troop"),
			(call_script, "script_not_family_check", ":troop", "trp_player"),
			(eq, "$is_family", 0),
			(neg|troop_slot_eq, ":troop", slot_troop_leaded_party, 3),
			(troop_get_slot, ":troop_love_interest_3", ":troop", slot_troop_love_interest_3),
			(is_between, ":troop_love_interest_3", "p_pyongyang", "p_place_end"),
			(neq, ":troop_love_interest_3", "$g_encountered_party"),
			(store_faction_of_party, ":faction_of_party_troop_love_interest_3", ":troop_love_interest_3"),
			(store_relation, ":relation_faction_of_party_troop_love_interest_3_wm_player_fac", ":faction_of_party_troop_love_interest_3", "$wm_player_fac"),
			(ge, ":relation_faction_of_party_troop_love_interest_3_wm_player_fac", 0),
			(store_distance_to_party_from_party, ":distance_to_party_from_party_troop_love_interest_3_g_encountered_party", ":troop_love_interest_3", "$g_encountered_party"),
			(is_between, ":distance_to_party_from_party_troop_love_interest_3_g_encountered_party", 70, 150),
			(call_script, "script_temp_save_number11_inject", ":troop"),
		(try_end),
		(call_script, "script_temp_save_number11_choice_rand"),
		(is_between, "$wm_target_number11", "trp_tt_lord_01_00", "trp_tt_lord_end"),
		(str_store_troop_name, 13, "$wm_target_number11"),
		(troop_get_slot, ":troop_love_interest_3", "$wm_target_number11", slot_troop_love_interest_3),
		(str_store_party_name, 4, ":troop_love_interest_3")
	],
	"I need to send a letter to {s13} who should be currently at {s4}. If you will be heading towards there, would you deliver it to him? The letter needs to be in his hands in 15 days.", "lord_deliver_mess",
	[]],

	[anyone|plyr, "lord_deliver_mess",
	[],
	"Certainly, I intend to pass by {s4} and it would be no trouble.", "lord_deliver_mess_accept",
	[
		(assign, "$qquest_type", 11),
		(assign, "$qquest_progress", 0),
		(assign, "$qquest_report_party", 0),
		(assign, "$qquest_report_troop", "$g_talk_troop"),
		(assign, "$qquest_target_party", 0),
		(assign, "$qquest_target_troop", "$wm_target_number11"),
		(assign, "$qquest_target_faction", 0),
		(assign, "$qquest_time_day", 15),
		(play_sound, "snd_quest_taken"),
		(display_message, "str_questget", 0x00ffff00),
		(troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 0)
	]],

	[anyone, "lord_deliver_mess_accept",
	[],
	"I appreciate it, {playername}. Here's the letter, and a small sum to cover your travel expenses. Give my regards to {s13} when you see him.", "lord_talk",
	[]],

	[anyone|plyr, "lord_deliver_mess",
	[],
	"I doubt I'll be seeing {s13} anytime soon. You'd best send it with someone else.", "lord_deliver_mess_reject",
	[]],

	[anyone, "lord_deliver_mess_reject",
	[],
	"Ah, all right then. Well, I am sure I will find someone else.", "lord_talk",
	[]],

	[anyone, "lord_quest",
	[
		(troop_slot_eq, "$g_talk_troop", slot_troop_does_not_give_quest, 12),
		(neg|troop_slot_ge, "$g_talk_troop", 3, "trp_tt_lady_01_01"),
		(call_script, "script_temp_save_number11_initialize"),
		(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(store_faction_of_troop, ":faction_of_troop_troop", ":troop"),
			(eq, ":faction_of_troop_troop", "$g_talk_troop_faction"),
			(neg|troop_slot_ge, ":troop", 3, "trp_tt_lord_01_00"),
			(call_script, "script_not_family_check", ":troop", "$g_talk_troop"),
			(eq, "$is_family", 0),
			(call_script, "script_not_family_check", ":troop", "trp_player"),
			(eq, "$is_family", 0),
			(neg|troop_slot_eq, ":troop", slot_troop_leaded_party, 3),
			(call_script, "script_temp_save_number11_inject", ":troop"),
		(try_end),
		(call_script, "script_temp_save_number11_choice_rand"),
		(is_between, "$wm_target_number11", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(str_store_troop_name, 13, "$wm_target_number11"),
		(troop_get_slot, ":wm_target_number11_betrothed", "$wm_target_number11", slot_troop_betrothed),
		(str_store_party_name, 4, ":wm_target_number11_betrothed")
	],
	" I need to send a letter to {s13} who should be currently at {s4}. If you will be heading towards there, would you deliver it to her? The letter needs to be in her hands in 15 days.", "lord_loveletter",
	[]],

	[anyone|plyr, "lord_loveletter",
	[],
	" Certainly, I intend to pass by {s4} and it would be no trouble.", "lord_loveletter_accept",
	[
		(assign, "$qquest_type", 12),
		(assign, "$qquest_progress", 0),
		(assign, "$qquest_report_party", 0),
		(assign, "$qquest_report_troop", "$g_talk_troop"),
		(assign, "$qquest_target_party", 0),
		(assign, "$qquest_target_troop", "$wm_target_number11"),
		(assign, "$qquest_target_faction", 0),
		(assign, "$qquest_time_day", 15),
		(play_sound, "snd_quest_taken"),
		(display_message, "str_questget", 0x00ffff00),
		(troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 0)
	]],

	[anyone, "lord_loveletter_accept",
	[],
	" I appreciate it, {playername}. Here's the letter, and a small sum to cover your travel expenses. Give my regards to {s13} when you see him.", "lord_talk",
	[]],

	[anyone|plyr, "lord_loveletter",
	[],
	" I doubt I'll be seeing {s13} anytime soon. You'd best send it with someone else.", "lord_loveletter_reject",
	[]],

	[anyone, "lord_loveletter_reject",
	[],
	" Ah, all right then. Well, I am sure I will find someone else.", "lord_talk",
	[]],

	[anyone, "lord_quest",
	[
		(neq, "$g_talk_troop_ego", 4),
		(neq, "$g_talk_troop_ego", 5),
		(troop_slot_eq, "$g_talk_troop", slot_troop_does_not_give_quest, 13),
		(eq, "$g_talk_troop_faction", "$wm_player_fac"),
		(store_party_size_wo_prisoners, ":party_size_wo_prisoners_main_party", "p_main_party"),
		(gt, ":party_size_wo_prisoners_main_party", 4000),
		(assign, ":value", 0),
		(try_for_range, ":faction", "fac_kingdom_1", "fac_kingdoms_end"),
			(store_relation, ":relation_faction_wm_player_fac", ":faction", "$wm_player_fac"),
			(lt, ":relation_faction_wm_player_fac", 0),
			(assign, ":value", 1),
		(try_end),
		(eq, ":value", 1)
	],
	"You know, our country has in the middle of war. If you do not handle the enemy troops , many citizens will die. If if you repel the enemy , I 'll give to compensate.", "lord_enemydefeat",
	[]],

	[anyone|plyr, "lord_enemydefeat",
	[],
	"I have my army.  I will protect citizens from enemies.", "lord_enemydefeat_accept",
	[
		(assign, "$qquest_type", 13),
		(assign, "$qquest_progress", 0),
		(assign, "$qquest_report_party", 0),
		(assign, "$qquest_report_troop", "$g_talk_troop"),
		(assign, "$qquest_target_party", 0),
		(assign, "$qquest_target_troop", 0),
		(assign, "$qquest_target_faction", 0),
		(assign, "$qquest_time_day", 45),
		(play_sound, "snd_quest_taken"),
		(display_message, "str_questget", 0x00ffff00),
		(troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 0)
	]],

	[anyone, "lord_enemydefeat_accept",
	[],
	"I believe your patriotism. and I look forward to good news.", "lord_talk",
	[]],

	[anyone|plyr, "lord_enemydefeat",
	[],
	"My army is not prepared. I need more time.", "lord_enemydefeat_reject",
	[]],

	[anyone, "lord_enemydefeat_reject",
	[],
	"Time is always short. I am disappointed.", "lord_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -5)
	]],

	[anyone, "lord_quest",
	[
		(neq, "$g_talk_troop_ego", 4),
		(neq, "$g_talk_troop_ego", 2),
		(neq, "$g_talk_troop_ego", 3),
		(troop_slot_eq, "$g_talk_troop", slot_troop_does_not_give_quest, 14),
		(eq, "$g_talk_troop_faction", "$wm_player_fac"),
		(neg|faction_slot_eq, "$wm_player_fac", 1, "trp_player"),
		(neg|faction_slot_eq, "$wm_player_fac", 1, "$g_talk_troop"),
		(call_script, "script_temp_save_number11_initialize"),
		(try_for_range, ":party", "p_pyongyang", "p_place_end"),
			(neq, ":party", "$g_encountered_party"),
			(store_faction_of_party, ":faction_of_party_party", ":party"),
			(neq, "$g_talk_troop_faction", ":faction_of_party_party"),
			(store_relation, ":relation_faction_of_party_party_wm_player_fac", ":faction_of_party_party", "$wm_player_fac"),
			(ge, ":relation_faction_of_party_party_wm_player_fac", 0),
			(store_distance_to_party_from_party, ":distance_to_party_from_party_party_g_encountered_party", ":party", "$g_encountered_party"),
			(is_between, ":distance_to_party_from_party_party_g_encountered_party", 10, 70),
			(is_between, ":faction_of_party_party", "fac_kingdom_1", "fac_kingdoms_end"),
			(call_script, "script_temp_save_number11_inject", ":faction_of_party_party"),
		(try_end),
		(call_script, "script_temp_save_number11_choice_rand"),
		(is_between, "$wm_target_number11", "fac_kingdom_1", "fac_kingdoms_end"),
		(str_store_faction_name, 13, "$wm_target_number11")
	],
	"This peace with {s13} ill suits me, {playername}. We've let those swine have their way for far too long. Now they get stronger with each passing and their arrogance knows no bounds. I say, we must wage war on them before it's too late! Unfortunately, some of the bleeding hearts among our realm's lords are blocking a possible declaration of war. Witless cowards with no stomach for blood.", "lord_warmonger_1",
	[]],

	[anyone|plyr, "lord_warmonger_1",
	[],
	"You are right, {s65}, but what can we do?", "lord_warmonger_2",
	[]],

	[anyone|plyr, "lord_warmonger_1",
	[],
	"I disagree, sir. It is better that there be peace.", "lord_warmonger_reject",
	[]],

	[anyone, "lord_warmonger_2",
	[
		(str_store_faction_name, 14, "$g_talk_troop_faction")
	],
	"Ah, 'tis good to hear someone who understands! As a matter of fact, there is something we can do, {playername}. A little bit of provocation... If one of our war parties managed to enter their territory and Amubsh one of their 'Army' or 'Traders', and perhaps left behind a little token or two of the {s14}, they would have ample cause to declare war on us. And then, well, even the cowards among us must rise to defend themselves. So what do you say? Are you interested?", "lord_warmonger_3",
	[]],

	[anyone|plyr, "lord_warmonger_3",
	[],
	"An excellent plan. Count me in.", "lord_warmonger_accept",
	[
		(assign, "$qquest_type", 14),
		(assign, "$qquest_progress", 0),
		(assign, "$qquest_report_party", 0),
		(assign, "$qquest_report_troop", "$g_talk_troop"),
		(assign, "$qquest_target_party", 0),
		(assign, "$qquest_target_troop", 0),
		(assign, "$qquest_target_faction", "$wm_target_number11"),
		(assign, "$qquest_time_day", 45),
		(play_sound, "snd_quest_taken"),
		(display_message, "str_questget", 0x00ffff00),
		(troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 0)
	]],

	[anyone, "lord_warmonger_accept",
	[],
	"Very good! A raid on a caravan, or, if you can't manage that, an attack on one of their villages, should do the trick. Now, good luck and good hunting. Go set the borders aflame!", "lord_talk",
	[]],

	[anyone|plyr, "lord_warmonger_3",
	[],
	"I don't like this. Find yourself someone else to take the blame for your schemes.", "lord_warmonger_reject",
	[]],

	[anyone, "lord_warmonger_reject",
	[],
	"Hm. As you wish, {playername}.  I thought you had some fire in you, but it seems I was wrong.", "lord_talk",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -5)
	]],

	[anyone, "lord_quest",
	[],
	"Unfortunately, There is no job to for you.", "lord_talk",
	[]],

	[anyone, "lady_req_jailbreak_1",
	[
		(str_store_troop_name, 8, "$temp_num_01"),
		(str_store_party_name, 9, "$temp_num_02")
	],
	"Oh, I fear I may never see my {s8}, again... He is a prisoner in the dungeon of {s9}. We have tried to negotiate his ransom, but it has been set too high. We can never hope to raise that much money without selling everything we own, and God knows {s8} would rather spend his life in prison than make us destitute. Instead I came up with a plan to get him out of there, but it requires someone to make a great sacrifice, and so far my pleas have fallen on deaf ears...", "lady_req_jailbreak_2",
	[]],

	[anyone|plyr, "lady_req_jailbreak_2",
	[],
	"As you wish it, {s65}, it shall be done.", "lady_mission_accepted",
	[]],

	[anyone|plyr, "lady_req_jailbreak_2",
	[],
	"{s66}, I fear I cannot help you right now.", "lady_mission_rejected",
	[]],

	[anyone, "lady_mission_accepted",
	[],
	"You are a true {gentleman/lady}, {playername}. Thank you so much for helping me", "close_window",
	[
		(assign, "$qquest_type", 32),
		(assign, "$qquest_progress", 0),
		(assign, "$qquest_report_party", 0),
		(assign, "$qquest_report_troop", "$g_talk_troop"),
		(assign, "$qquest_target_party", "$temp_num_02"),
		(assign, "$qquest_target_troop", "$temp_num_01"),
		(assign, "$qquest_target_faction", 0),
		(assign, "$qquest_time_day", 20),
		(play_sound, "snd_quest_taken"),
		(display_message, "str_questget", 0x00ffff00),
		(troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 0)
	]],

	[anyone, "lady_mission_rejected",
	[],
	"You'll not help a woman in need? You should be ashamed, {playername}... Please leave me, I have some important embroidery to catch up.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -3)
	]],

	[anyone, "lady_quest",
	[
		(troop_slot_eq, "$g_talk_troop", slot_troop_does_not_give_quest, 21),
		(call_script, "script_temp_save_number11_initialize"),
		(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(neq, ":troop", "$g_talk_troop"),
			(call_script, "script_not_family_check", ":troop", "$g_talk_troop"),
			(eq, "$is_family", 0),
			(call_script, "script_not_family_check", ":troop", "trp_player"),
			(eq, "$is_family", 0),
			(neg|troop_slot_eq, ":troop", slot_troop_leaded_party, 3),
			(troop_get_slot, ":troop_betrothed", ":troop", slot_troop_betrothed),
			(is_between, ":troop_betrothed", "p_pyongyang", "p_place_end"),
			(neq, ":troop_betrothed", "$g_encountered_party"),
			(store_faction_of_party, ":faction_of_party_troop_betrothed", ":troop_betrothed"),
			(store_relation, ":relation_faction_of_party_troop_betrothed_wm_player_fac", ":faction_of_party_troop_betrothed", "$wm_player_fac"),
			(ge, ":relation_faction_of_party_troop_betrothed_wm_player_fac", 0),
			(store_distance_to_party_from_party, ":distance_to_party_from_party_troop_betrothed_g_encountered_party", ":troop_betrothed", "$g_encountered_party"),
			(is_between, ":distance_to_party_from_party_troop_betrothed_g_encountered_party", 70, 150),
			(call_script, "script_temp_save_number11_inject", ":troop"),
		(try_end),
		(call_script, "script_temp_save_number11_choice_rand"),
		(is_between, "$wm_target_number11", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(str_store_troop_name, 13, "$wm_target_number11"),
		(troop_get_slot, ":troop_betrothed", "$wm_target_number11", slot_troop_betrothed),
		(str_store_party_name, 4, ":troop_betrothed")
	],
	"  I need to send a letter to {s13} who should be currently at {s4}. If you will be heading towards there, would you deliver it to her? The letter needs to be in her hands in 15 days.", "lady_messenger",
	[]],

	[anyone|plyr, "lady_messenger",
	[],
	"  Certainly, I intend to pass by {s4} and it would be no trouble.", "lady_messenger_accept",
	[
		(assign, "$qquest_type", 21),
		(assign, "$qquest_progress", 0),
		(assign, "$qquest_report_party", 0),
		(assign, "$qquest_report_troop", "$g_talk_troop"),
		(assign, "$qquest_target_party", 0),
		(assign, "$qquest_target_troop", "$wm_target_number11"),
		(assign, "$qquest_target_faction", 0),
		(assign, "$qquest_time_day", 15),
		(play_sound, "snd_quest_taken"),
		(display_message, "str_questget", 0x00ffff00),
		(troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 0)
	]],

	[anyone, "lady_messenger_accept",
	[],
	"  I appreciate it, {playername}. Here's the letter, and a small sum to cover your travel expenses. Give my regards to {s13} when you see him.", "lady_talk",
	[]],

	[anyone|plyr, "lady_messenger",
	[],
	"  I doubt I'll be seeing {s13} anytime soon. You'd best send it with someone else.", "lady_messenger_reject",
	[]],

	[anyone, "lady_messenger_reject",
	[],
	"  Ah, all right then. Well, I am sure I will find someone else.", "lady_talk",
	[]],

	[anyone, "lady_quest",
	[
		(troop_slot_eq, "$g_talk_troop", slot_troop_does_not_give_quest, 22),
		(call_script, "script_temp_save_number11_initialize"),
		(try_for_range, ":troop", "trp_tt_lord_01_00", "trp_tt_lord_end"),
			(neq, ":troop", "$g_talk_troop"),
			(call_script, "script_not_family_check", ":troop", "$g_talk_troop"),
			(eq, "$is_family", 0),
			(call_script, "script_not_family_check", ":troop", "trp_player"),
			(eq, "$is_family", 0),
			(troop_get_slot, ":troop_love_interest_3", ":troop", slot_troop_love_interest_3),
			(is_between, ":troop_love_interest_3", "p_pyongyang", "p_place_end"),
			(neq, ":troop_love_interest_3", "$g_encountered_party"),
			(store_faction_of_party, ":faction_of_party_troop_love_interest_3", ":troop_love_interest_3"),
			(neg|faction_slot_eq, ":faction_of_party_troop_love_interest_3", 1, ":troop"),
			(store_relation, ":relation_faction_of_party_troop_love_interest_3_wm_player_fac", ":faction_of_party_troop_love_interest_3", "$wm_player_fac"),
			(ge, ":relation_faction_of_party_troop_love_interest_3_wm_player_fac", 0),
			(store_distance_to_party_from_party, ":distance_to_party_from_party_troop_love_interest_3_g_encountered_party", ":troop_love_interest_3", "$g_encountered_party"),
			(is_between, ":distance_to_party_from_party_troop_love_interest_3_g_encountered_party", 30, 130),
			(call_script, "script_temp_save_number11_inject", ":troop"),
		(try_end),
		(call_script, "script_temp_save_number11_choice_rand"),
		(is_between, "$wm_target_number11", "trp_tt_lord_01_00", "trp_tt_lord_end"),
		(str_store_troop_name, 13, "$wm_target_number11")
	],
	"Dear {playername}, you are kind to ask, but you know little of my troubles and I can't possibly ask you to throw yourself into danger on my behalf. My family has made certain enemies, {playername}. One of the most insidious is {s13}. He is going around making terrible accusations against me, impugning my honour at every turn! Because he cannot harm my husband directly, he is using me as a target to try and stain our name. You should hear the awful things he's said! I only wish there was someone brave enough to make him recant his slander, but {s13} is a very fine swordsman, and he's widely feared...", "lady_duel_req",
	[]],

	[anyone|plyr, "lady_duel_req",
	[],
	"I fear him not, {s65}. I will make him take back his lies.", "lady_duel_req_accept",
	[
		(assign, "$qquest_type", 22),
		(assign, "$qquest_progress", 0),
		(assign, "$qquest_report_party", 0),
		(assign, "$qquest_report_troop", "$g_talk_troop"),
		(assign, "$qquest_target_party", 0),
		(assign, "$qquest_target_troop", "$wm_target_number11"),
		(assign, "$qquest_target_faction", 0),
		(assign, "$qquest_time_day", 15),
		(play_sound, "snd_quest_taken"),
		(display_message, "str_questget", 0x00ffff00),
		(troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 0)
	]],

	[anyone, "lady_duel_req_accept",
	[],
	"Oh! I can't ask that of you, {playername}, but... I would be forever indebted to you, and you are so sure. It would mean so much if you would defend my honour. Thank you a thousand times, all my prayers and my favour go with you.", "lady_talk",
	[]],

	[anyone|plyr, "lady_duel_req",
	[],
	"If he's that dangerous, perhaps maybe it would be better to ignore him...", "lady_duel_req_reject",
	[]],

	[anyone, "lady_duel_req_reject",
	[],
	"Oh... Perhaps you're right, {playername}.  I should let go of these silly childhood ideas of chivalry and courage. {Men/People} are not like that,  not anymore. Good day to you.", "lady_talk",
	[]],

	[anyone, "lady_quest",
	[
		(troop_slot_eq, "$g_talk_troop", slot_troop_does_not_give_quest, 23),
		(neq, "$g_talk_troop_faction", "fac_kingdom_50"),
		(neq, "$g_talk_troop_ego", 12),
		(neq, "$g_talk_troop_ego", 15),
		(call_script, "script_temp_save_number11_initialize"),
		(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(neq, ":troop", "$g_talk_troop"),
			(call_script, "script_not_family_check", ":troop", "$g_talk_troop"),
			(eq, "$is_family", 0),
			(call_script, "script_not_family_check", ":troop", "trp_player"),
			(eq, "$is_family", 0),
			(neg|troop_slot_eq, ":troop", slot_troop_leaded_party, 3),
			(troop_get_slot, ":troop_betrothed", ":troop", slot_troop_betrothed),
			(is_between, ":troop_betrothed", "p_pyongyang", "p_place_end"),
			(neq, ":troop_betrothed", "$g_encountered_party"),
			(store_faction_of_party, ":faction_of_party_troop_betrothed", ":troop_betrothed"),
			(store_relation, ":relation_faction_of_party_troop_betrothed_wm_player_fac", ":faction_of_party_troop_betrothed", "$wm_player_fac"),
			(ge, ":relation_faction_of_party_troop_betrothed_wm_player_fac", 0),
			(store_distance_to_party_from_party, ":distance_to_party_from_party_troop_betrothed_g_encountered_party", ":troop_betrothed", "$g_encountered_party"),
			(is_between, ":distance_to_party_from_party_troop_betrothed_g_encountered_party", 40, 130),
			(call_script, "script_temp_save_number11_inject", ":troop"),
		(try_end),
		(call_script, "script_temp_save_number11_choice_rand"),
		(is_between, "$wm_target_number11", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(str_store_troop_name, 13, "$wm_target_number11"),
		(troop_get_slot, ":troop_betrothed", "$wm_target_number11", slot_troop_betrothed),
		(str_store_party_name, 4, ":troop_betrothed")
	],
	"{s13} is damn bitch. That bitch told bad rumor about me to everyone. I will teach her that who is now prostitute. She is now staying in a villa near {s4}. Covering your face and slap her face.", "lady_beat",
	[]],

	[anyone|plyr, "lady_beat",
	[],
	"Interesting. I always want slap the women.", "lady_beat_accept",
	[
		(assign, "$qquest_type", 23),
		(assign, "$qquest_progress", 0),
		(assign, "$qquest_report_party", 0),
		(assign, "$qquest_report_troop", "$g_talk_troop"),
		(assign, "$qquest_target_party", 0),
		(assign, "$qquest_target_troop", "$wm_target_number11"),
		(assign, "$qquest_target_faction", 0),
		(assign, "$qquest_time_day", 15),
		(play_sound, "snd_quest_taken"),
		(display_message, "str_questget", 0x00ffff00),
		(troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 0),
		(troop_get_slot, ":wm_target_number11_betrothed", "$wm_target_number11", slot_troop_betrothed),
		(party_relocate_near_party, "p_for_quest_villa", ":wm_target_number11_betrothed", 2),
		(party_set_icon, "p_for_quest_villa", "icon_house_exn"),
		(party_set_flags, "p_for_quest_villa", 256, 0),
		(party_set_flags, "p_for_quest_villa", 16384, 1),
		(str_store_troop_name, 13, "$wm_target_number11"),
		(str_store_string, 14, "str_s13svilla"),
		(party_set_name, "p_for_quest_villa", 14),
		(store_faction_of_party, ":faction_of_party_wm_target_number11_betrothed", ":wm_target_number11_betrothed"),
		(party_set_slot, "p_for_quest_villa", slot_town_center, ":faction_of_party_wm_target_number11_betrothed")
	]],

	[anyone, "lady_beat_accept",
	[],
	"Good. This is your perfect job.", "lady_talk",
	[]],

	[anyone|plyr, "lady_beat",
	[],
	"I'm not a bully.", "lady_beat_reject",
	[]],

	[anyone, "lady_beat_reject",
	[],
	"   Ah, all right then. Well, I am sure I will find someone else.", "lady_talk",
	[]],

	[anyone, "lady_quest",
	[
		(troop_slot_eq, "$g_talk_troop", slot_troop_does_not_give_quest, 24),
		(neq, "$g_talk_troop_faction", "fac_kingdom_50"),
		(troop_slot_ge, "$g_talk_troop", 3, "trp_tt_lord_01_00"),
		(call_script, "script_temp_save_number11_initialize"),
		(try_for_range, ":troop", "trp_tt_lady_01_01", "trp_tt_lady_end"),
			(neq, ":troop", "$g_talk_troop"),
			(call_script, "script_not_family_check", ":troop", "$g_talk_troop"),
			(eq, "$is_family", 0),
			(call_script, "script_not_family_check", ":troop", "trp_player"),
			(eq, "$is_family", 0),
			(neg|troop_slot_eq, ":troop", slot_troop_leaded_party, 3),
			(troop_get_slot, ":troop_betrothed", ":troop", slot_troop_betrothed),
			(is_between, ":troop_betrothed", "p_pyongyang", "p_place_end"),
			(neq, ":troop_betrothed", "$g_encountered_party"),
			(store_faction_of_party, ":faction_of_party_troop_betrothed", ":troop_betrothed"),
			(store_relation, ":relation_faction_of_party_troop_betrothed_wm_player_fac", ":faction_of_party_troop_betrothed", "$wm_player_fac"),
			(ge, ":relation_faction_of_party_troop_betrothed_wm_player_fac", 0),
			(store_distance_to_party_from_party, ":distance_to_party_from_party_troop_betrothed_g_encountered_party", ":troop_betrothed", "$g_encountered_party"),
			(is_between, ":distance_to_party_from_party_troop_betrothed_g_encountered_party", 40, 130),
			(call_script, "script_temp_save_number11_inject", ":troop"),
		(try_end),
		(call_script, "script_temp_save_number11_choice_rand"),
		(is_between, "$wm_target_number11", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(str_store_troop_name, 13, "$wm_target_number11"),
		(troop_get_slot, ":troop_betrothed", "$wm_target_number11", slot_troop_betrothed),
		(str_store_party_name, 4, ":troop_betrothed"),
		(troop_get_slot, ":g_talk_troop_state", "$g_talk_troop", slot_troop_state),
		(str_store_troop_name, 14, ":g_talk_troop_state")
	],
	"My husband {s14} has seems to meet another woman. You have to keep track of the husband, please find the site that meet two people. My husband often go to {s4}.", "lady_misdoubt",
	[]],

	[anyone|plyr, "lady_misdoubt",
	[],
	"All right. I can resolve this problem.", "lady_misdoubt_accept",
	[
		(assign, "$qquest_type", 24),
		(assign, "$qquest_progress", 0),
		(assign, "$qquest_report_party", 0),
		(assign, "$qquest_report_troop", "$g_talk_troop"),
		(troop_get_slot, ":wm_target_number11_betrothed", "$wm_target_number11", slot_troop_betrothed),
		(assign, "$qquest_target_party", ":wm_target_number11_betrothed"),
		(troop_get_slot, ":g_talk_troop_state", "$g_talk_troop", slot_troop_state),
		(assign, "$qquest_target_troop", ":g_talk_troop_state"),
		(assign, "$qquest_target_faction", "$wm_target_number11"),
		(assign, "$qquest_time_day", 15),
		(play_sound, "snd_quest_taken"),
		(display_message, "str_questget", 0x00ffff00),
		(troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 0)
	]],

	[anyone, "lady_misdoubt_accept",
	[],
	"Go to the '{s4} street'. and track him. I really want to know truth.", "lady_talk",
	[]],

	[anyone|plyr, "lady_misdoubt",
	[],
	"Sorry, I'm not a tracker.", "lady_misdoubt_reject",
	[]],

	[anyone, "lady_misdoubt_reject",
	[],
	"  Well, I am sure I will find someone else.", "lady_talk",
	[]],

	[anyone|plyr, "lord_misdoubt",
	[],
	"Well. Give me the money. Maybe I should prepare the perfect lie for your wife.", "lord_misdoubt_lie",
	[]],

	[anyone, "lord_misdoubt_lie",
	[],
	"Good. Do not betray me. Here's the Money.", "close_window",
	[
		(store_mul, ":value", 1000, 3),
		(call_script, "script_party_money_level_diff", "p_main_party", ":value", 87),
		(assign, "$qquest_progress", 2),
		(play_sound, "snd_bad_drum"),
		(display_message, "str_questfail", 0x00ffff00),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return")
	]],

	[anyone|plyr, "lord_misdoubt",
	[],
	"Sorry, sir. I will not betray your wife.", "lord_misdoubt_truth",
	[]],

	[anyone, "lord_misdoubt_truth",
	[],
	"Damn you. You'll pay for this.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$qquest_target_faction", -5),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -15),
		(assign, "$qquest_progress", 1),
		(play_sound, "snd_quest_succeeded"),
		(display_message, "str_questsucc", 0x00ffff00),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return")
	]],

	[anyone, "lady_quest",
	[],
	"  Unfortunately, There is no job to for you.", "lady_talk",
	[]],

	[anyone|plyr, "ransom_talk",
	[
		(eq, "$main_q_step", 5),
		(eq, "$main_q_party", "$g_encountered_party")
	],
	"I have a question about the slave you have bought.", "broker_mq_5_1",
	[]],

	[anyone, "broker_mq_5_1",
	[],
	"I cannot say anything about my old slaves. Even if you brought to me the [Fish], I will not say anything.", "close_window",
	[
		(assign, "$main_q_step", 6)
	]],

	[anyone|plyr, "ransom_talk",
	[
		(eq, "$main_q_step", 6),
		(eq, "$main_q_party", "$g_encountered_party"),
		(player_has_item, 97)
	],
	" I have a question about the slave you have bought. and i have gift for you.", "broker_mq_6_1",
	[]],

	[anyone, "broker_mq_6_1",
	[],
	"i can't saying anything about that! (he threw to me a book.)", "broker_mq_6_2",
	[]],

	[anyone|plyr, "broker_mq_6_2",
	[],
	" Aw!!", "close_window",
	[
		(troop_remove_item, "trp_player", 97),
		(assign, "$main_q_step", 7),
		(party_get_position, 11, "$main_q_party"),
		(map_get_land_position_around_position, 12, 11, 2),
		(assign, ":var_1", "p_ruin_dummy_5"),
		(party_set_position, ":var_1", 12),
		(party_set_icon, ":var_1", "icon_wm_town_barb_2"),
		(party_set_flags, ":var_1", 256, 0),
		(party_set_flags, ":var_1", 524288, 0),
		(party_set_flags, ":var_1", 16384, 1),
		(party_set_name, ":var_1", "str_mq_higma_fort_name"),
		(party_get_slot, ":main_q_party_town_center", "$main_q_party", slot_town_center),
		(party_set_slot, ":var_1", slot_town_center, ":main_q_party_town_center"),
		(dialog_box, "str_mq_1_6", "str_box_note")
	]],

	[anyone|plyr, "ransom_talk",
	[
		(store_num_regular_prisoners, reg0),
		(ge, reg0, 1)
	],
	"Then you'd better bring your purse. I have got prisoners to sell.", "ransom_broker_sell_prisoners_2",
	[
		(assign, ":var_1", 0),
		(party_get_num_prisoner_stacks, ":num_prisoner_stacks_main_party", "p_main_party"),
		(try_for_range, ":localvariable", 0, ":num_prisoner_stacks_main_party"),
			(party_prisoner_stack_get_troop_id, ":party_prisoner_stack_troop_id_main_party_localvariable", "p_main_party", ":localvariable"),
			(neg|troop_is_hero, ":party_prisoner_stack_troop_id_main_party_localvariable"),
			(party_prisoner_stack_get_size, ":party_prisoner_stack_size_main_party_localvariable", "p_main_party", ":localvariable"),
			(gt, ":party_prisoner_stack_size_main_party_localvariable", 0),
			(store_character_level, ":character_level_party_prisoner_stack_troop_id_main_party_localvariable", ":party_prisoner_stack_troop_id_main_party_localvariable"),
			(store_mul, ":value", ":character_level_party_prisoner_stack_troop_id_main_party_localvariable", 2),
			(val_mul, ":value", ":party_prisoner_stack_size_main_party_localvariable"),
			(val_add, ":var_1", ":value"),
		(try_end),
		(remove_regular_prisoners, "p_main_party"),
		(call_script, "script_party_money_level_diff", "p_main_party", ":var_1", 87)
	]],

	[anyone, "ransom_broker_sell_prisoners_2",
	[],
	"I will be staying here for a few days. Let me know if you need my services.", "close_window",
	[]],

	[anyone|plyr, "ransom_talk",
	[],
	"Not this time. Good-bye.", "close_window",
	[]],

	[anyone|plyr, "lord_prisoner_talk",
	[
		(eq, "$attemp_commu", 0),
		(eq, "$adult_content", 1)
	],
	"  Don't hate me. I have a gift for you.", "lord_prisoner_compbj_pre",
	[]],

	[anyone, "lord_prisoner_compbj_pre",
	[],
	"What?", "lord_prisoner_compbj_0",
	[]],

	[anyone|repeat_for_troops|plyr, "lord_prisoner_compbj_0",
	[
		(store_repeat_object, ":repeat_object"),
		(is_between, ":repeat_object", "trp_tt_lady_01_01", "trp_tt_lady_end"),
		(neg|troop_slot_eq, "trp_player", slot_troop_state, ":repeat_object"),
		(call_script, "script_wm_main_party_has_troop_sc", ":repeat_object"),
		(eq, "$wm_comp_continue", 1),
		(call_script, "script_troop_get_player_relation", ":repeat_object"),
		(assign, ":var_2", reg0),
		(try_begin),
			(this_or_next|eq, ":repeat_object", "trp_tt_lady_ex_01"),
			(this_or_next|eq, ":repeat_object", "trp_tt_lady_ex_12"),
			(this_or_next|eq, ":repeat_object", "trp_tt_lady_ex_15"),
			(eq, ":repeat_object", "trp_tt_lady_ex_18"),
			(assign, ":value", 0),
		(else_try),
			(this_or_next|eq, ":repeat_object", "trp_tt_lady_ex_02"),
			(this_or_next|eq, ":repeat_object", "trp_tt_lady_ex_04"),
			(this_or_next|eq, ":repeat_object", "trp_tt_lady_ex_06"),
			(this_or_next|eq, ":repeat_object", "trp_tt_lady_ex_08"),
			(eq, ":repeat_object", "trp_tt_lady_ex_09"),
			(assign, ":value", 30),
		(else_try),
			(this_or_next|eq, ":repeat_object", "trp_tt_lady_ex_03"),
			(this_or_next|eq, ":repeat_object", "trp_tt_lady_ex_05"),
			(this_or_next|eq, ":repeat_object", "trp_tt_lady_ex_10"),
			(eq, ":repeat_object", "trp_tt_lady_ex_17"),
			(assign, ":value", 45),
		(else_try),
			(assign, ":value", 60),
		(try_end),
		(ge, ":var_2", ":value"),
		(str_store_troop_name, 1, ":repeat_object")
	],
	"  {s1} will give you the Happiness.", "lord_prisoner_compbj_1",
	[
		(store_repeat_object, "$temp")
	]],

	[anyone|plyr, "lord_prisoner_compbj_0",
	[],
	"Nevermind", "close_window",
	[]],

	[anyone, "lord_prisoner_compbj_1",
	[],
	"ha! I cannot reject your favor.", "lord_prisoner_compbj_2",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone, "lord_prisoner_compbj_2",
	[],
	".......", "lord_prisoner_compbj_3",
	[
		(set_conversation_speaker_troop, "$temp"),
		(call_script, "script_molda_s_scene", 511, 0)
	]],

	[anyone, "lord_prisoner_compbj_3",
	[],
	" Oh....ow!", "lord_prisoner_compbj_4",
	[]],

	[anyone, "lord_prisoner_compbj_4",
	[],
	".......", "lord_prisoner_compbj_5",
	[
		(set_conversation_speaker_troop, "$temp"),
		(call_script, "script_molda_s_scene", 511, 0)
	]],

	[anyone, "lord_prisoner_compbj_5",
	[],
	"       Uhh!", "lord_prisoner_compbj_6",
	[
		(store_random_in_range, ":random_in_range_512_514", 512, 514),
		(call_script, "script_molda_s_scene", ":random_in_range_512_514", 0)
	]],

	[anyone, "lord_prisoner_compbj_6",
	[],
	" Uhh!   Weird taste. You're feels better now?", "close_window",
	[
		(set_conversation_speaker_troop, "$temp"),
		(store_random_in_range, ":random_in_range_3_6", 3, 6),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", ":random_in_range_3_6")
	]],

	[anyone|plyr, "lord_prisoner_talk",
	[
		(eq, "$talk_troop_gender", 0),
		(eq, "$player_gender", 1),
		(eq, "$attemp_commu", 0),
		(eq, "$adult_content", 1)
	],
	" Don't hate me. I give you blowjob.", "lord_prisoner_blowjob",
	[]],

	[anyone, "lord_prisoner_blowjob",
	[],
	"What? You're really a whore bitch.", "member_blowjob_fe_plyr_2",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "lord_prisoner_talk",
	[],
	" I demand a ransom to your country. This is my greatest mercy.", "lord_prisoner_ransom",
	[]],

	[anyone, "lord_prisoner_ransom",
	[],
	" Yes, yes, you're wise man. now you became rich. and i got freedom. it is perfectly fair!", "close_window",
	[
		(store_random_in_range, ":random_in_range_3000_7000", 3000, 7000),
		(call_script, "script_party_money_level_diff", "p_main_party", ":random_in_range_3000_7000", 87),
		(troop_set_slot, "$g_talk_troop", slot_troop_cur_center, 0),
		(party_remove_prisoners, "p_main_party", "$g_talk_troop", 1),
		(finish_mission)
	]],

	[anyone|plyr, "lord_prisoner_talk",
	[],
	" You can return to homeland.", "lord_prisoner_release",
	[]],

	[anyone, "lord_prisoner_release",
	[
		(store_random_in_range, ":random_in_range_prisoner_released_default_prisoner_released_end", "str_prisoner_released_default", "str_prisoner_released_end"),
		(str_store_string, 43, ":random_in_range_prisoner_released_default_prisoner_released_end")
	],
	"{s43}", "close_window",
	[
		(call_script, "script_wm_honor_change_diff", "trp_player", 3, 87),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 10),
		(troop_set_slot, "$g_talk_troop", slot_troop_cur_center, 0),
		(party_remove_prisoners, "p_main_party", "$g_talk_troop", 1),
		(finish_mission)
	]],

	[anyone|plyr, "lord_prisoner_talk",
	[],
	" SHUT UP! [Whipped to him]", "lord_prisoner_whip",
	[
		(play_sound, "snd_gbt_whip"),
		#(play_sound, "snd_man_hit")
	]],

	[anyone, "lord_prisoner_whip",
	[],
	" Damn you. You'll pay for this.", "close_window",
	[
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -20),
		(call_script, "script_troop_get_player_relation", "$g_talk_troop"),
		(assign, ":var_1", reg0),
		(try_begin),
			(lt, ":var_1", -80),
			(troop_set_slot, "$g_talk_troop", 41, 3),
			(str_store_troop_name, 3, "$g_talk_troop"),
			(dialog_box, "str_revengeful_set", "str_box_note"),
		(try_end)
	]],

	[anyone|plyr, "lord_prisoner_talk",
	[],
	" Not this time.", "close_window",
	[]],

	[anyone|plyr, "tavern_mer_rec_1",
	[
		(store_add, ":value", "$comp_rel_passsss", 3),
		(store_character_level, ":character_level_g_talk_troop", "$g_talk_troop"),
		(val_sub, ":character_level_g_talk_troop", 8),
		(val_mul, ":value", ":character_level_g_talk_troop"),
		(val_mul, ":value", 30),
		(assign, reg5, ":value"),
		(call_script, "script_party_money_level_ge", "p_main_party", reg5),
		(eq, "$wm_mo_continue", 1)
	],
	"All right. I will hire all of you. Here is {reg5} denars.", "tavern_mer_rec_2",
	[
		(store_add, ":value", "$comp_rel_passsss", 3),
		(call_script, "script_new_troop_add_sc", "$g_talk_troop", ":value"),
		(call_script, "script_party_money_level_diff", "p_main_party", reg5, 34),
		(assign, "$wm_buying_drink_for_army", 168),
		(assign, reg9, "$wm_buying_drink_for_army"),
		(display_message, "str_tavern_cool_add", 0x00ffff00)
	]],

	[anyone, "tavern_mer_rec_2",
	[],
	"You will not be disappointed {sir/madam}. You will not find better warriors in near.", "close_window",
	[]],

	[anyone|plyr, "tavern_mer_rec_1",
	[],
	"That sounds good. But I can't afford to hire any more men right now.", "close_window",
	[]],

	[anyone|plyr, "prison_guard_talk",
	[],
	"I want to speak with a prisoner.", "prison_guard_visit_prison",
	[]],

	[anyone|plyr, "prison_guard_talk",
	[],
	"Never mind.", "close_window",
	[]],

	[anyone, "prison_guard_visit_prison",
	[],
	"You need to get permission from the lord to talk to prisoners.", "prison_guard_visit_prison_2",
	[]],

	[anyone|plyr, "prison_guard_visit_prison_2",
	[],
	"All right then. I'll try that.", "close_window",
	[]],

	[anyone|plyr, "prison_guard_visit_prison_2",
	[],
	"Come on now. I thought you were the boss here.", "prison_guard_visit_prison_3",
	[]],

	[anyone, "prison_guard_visit_prison_3",
	[],
	"He-heh. You got that right. Still, I can't let you into the prison.", "prison_guard_visit_prison_4",
	[]],

	[anyone|plyr, "prison_guard_visit_prison_4",
	[],
	"All right then. I'll leave now.", "close_window",
	[]],

	[anyone|plyr, "prison_guard_visit_prison_4",
	[
		(call_script, "script_party_money_level_ge", "p_main_party", 1500),
		(eq, "$wm_mo_continue", 1)
	],
	"I found a purse with 1500 denars a few paces away. I reckon it belongs to you.", "prison_guard_visit_prison_5",
	[]],

	[anyone, "prison_guard_visit_prison_5",
	[],
	"Ah! I was looking for this all day. How good of you to bring it back {sir/madam}.Well, now that I know what an honest {man/lady} you are, there can be no harm in letting you inside for a look. Go in.... Just so you know, though -- I'll be hanging onto the keys, in case you were thinking about undoing anyone's chains.", "close_window",
	[
		(call_script, "script_party_money_level_diff", "p_main_party", 1500, 34),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_jailbreak_enter")
	]],

	[anyone|plyr, "prison_guard_visit_prison_4",
	[],
	"Give me the keys to the cells -- now!", "prison_guard_visit_break",
	[]],

	[anyone, "prison_guard_visit_break",
	[],
	"Help! Help! Prison break!", "close_window",
	[
		(try_for_agents, ":var_1"),
			(agent_is_human, ":var_1"),
			(agent_is_alive, ":var_1"),
			(agent_get_troop_id, ":troop_id_var_1", ":var_1"),
			(is_between, ":troop_id_var_1", "trp_farmer", "trp_town_walker_1"),
			(agent_set_team, ":var_1", 4),
			(agent_set_is_alarmed, ":var_1", 1),
			(agent_ai_set_aggressiveness, ":var_1", 199),
		(try_end)
	]],

	[anyone|plyr, "orphan_talk",
	[
		(lt, "$orphan_grown_count", 240)
	],
	"I have to say about your training.", "orphan_study",
	[]],

	[anyone, "orphan_study",
	[],
	"I want to play a little more. What is today training?", "orphan_study_list",
	[]],

	[anyone|plyr, "orphan_study_list",
	[],
	"Navermind.", "close_window",
	[]],

	[anyone|plyr, "orphan_study_list",
	[],
	"Weapon master (Skill+1, It is important)", "orphan_study_react",
	[
		(assign, "$orphan_train_type", 27)
	]],

	[anyone|plyr, "orphan_study_list",
	[],
	"Sword fighting (Str+1, Melee proficiency)", "orphan_study_react",
	[
		(assign, "$orphan_train_type", 1)
	]],

	[anyone|plyr, "orphan_study_list",
	[],
	"Range weapon (Agi+1, Range proficiency)", "orphan_study_react",
	[
		(assign, "$orphan_train_type", 2)
	]],

	[anyone|plyr, "orphan_study_list",
	[],
	"Makeup (Cha+1, Appearance improve)", "orphan_study_react",
	[
		(assign, "$orphan_train_type", 3)
	]],

	[anyone|plyr, "orphan_study_list",
	[],
	"Power strike (Skill+1)", "orphan_study_react",
	[
		(assign, "$orphan_train_type", 35)
	]],

	[anyone|plyr, "orphan_study_list",
	[],
	"Riding (Skill+1)", "orphan_study_react",
	[
		(assign, "$orphan_train_type", 24)
	]],

	[anyone|plyr, "orphan_study_list",
	[],
	"Power draw (Skill+1)", "orphan_study_react",
	[
		(assign, "$orphan_train_type", 33)
	]],

	[anyone|plyr, "orphan_study_list",
	[],
	"Ironflesh (Skill+1)", "orphan_study_react",
	[
		(assign, "$orphan_train_type", 36)
	]],

	[anyone|plyr, "orphan_study_list",
	[],
	"Horse archery (Skill+1)", "orphan_study_react",
	[
		(assign, "$orphan_train_type", 23)
	]],

	[anyone|plyr, "orphan_study_list",
	[],
	"Athletics (Skill+1)", "orphan_study_react",
	[
		(assign, "$orphan_train_type", 25)
	]],

	[anyone|plyr, "orphan_study_list",
	[],
	"Shield (Skill+1)", "orphan_study_react",
	[
		(assign, "$orphan_train_type", 26)
	]],

	[anyone|plyr, "orphan_study_list",
	[],
	"Power throw (Skill+1)", "orphan_study_react",
	[
		(assign, "$orphan_train_type", 34)
	]],

	[anyone, "orphan_study_react",
	[],
	"Boring. (system: selected skill or state is grown one time per a week.)", "orphan_talk",
	[]],

	[anyone|plyr, "orphan_talk",
	[],
	" What can you tell me about your skills?", "orphan_char_requested",
	[]],

	[anyone, "orphan_char_requested",
	[],
	"All right, let me tell you...", "orphan_view_char",
	[
		(change_screen_view_character)
	]],

	[anyone, "orphan_view_char",
	[],
	"Anything else?", "orphan_talk",
	[]],

	[anyone|plyr, "orphan_talk",
	[
		(eq, "$attemp_commu", 0)
	],
	"How do you do these days?", "member_comp_relation_talk",
	[
		(call_script, "script_try_attemp_commu")
	]],

	[anyone|plyr, "orphan_talk",
	[
		(player_has_item, 1432),
		(ge, "$orphan_grown_count", 200)
	],
	"Can you eat this herb? It is good for your health.", "orphan_bigboobherb",
	[]],

	[anyone, "orphan_bigboobherb",
	[],
	"Whoops ! It tastes like snot.", "orphan_talk",
	[
		(try_begin),
			(troop_get_slot, ":orphan_girl_troop_id_last_quest_betrayed", "$orphan_girl_troop_id", slot_troop_last_quest_betrayed),
			(lt, ":orphan_girl_troop_id_last_quest_betrayed", 16),
			(val_add, ":orphan_girl_troop_id_last_quest_betrayed", 1),
			(troop_set_slot, "$orphan_girl_troop_id", slot_troop_last_quest_betrayed, ":orphan_girl_troop_id_last_quest_betrayed"),
			(display_message, "str_bodychannnn"),
		(try_end),
		(troop_remove_item, "$orphan_girl_troop_id", 1432)
	]],

	[anyone|plyr, "orphan_talk",
	[
		(player_has_item, 1431),
		(ge, "$orphan_grown_count", 200)
	],
	" Can you eat this herb? It is good for your health.", "orphan_smallboobherb",
	[]],

	[anyone, "orphan_smallboobherb",
	[],
	" Whoops ! It tastes like snot.", "orphan_talk",
	[
		(try_begin),
			(troop_get_slot, ":orphan_girl_troop_id_last_quest_betrayed", "$orphan_girl_troop_id", slot_troop_last_quest_betrayed),
			(gt, ":orphan_girl_troop_id_last_quest_betrayed", 1),
			(val_sub, ":orphan_girl_troop_id_last_quest_betrayed", 1),
			(troop_set_slot, "$orphan_girl_troop_id", slot_troop_last_quest_betrayed, ":orphan_girl_troop_id_last_quest_betrayed"),
			(display_message, "str_bodychannnn"),
		(try_end),
		(troop_remove_item, "$orphan_girl_troop_id", 1431)
	]],

	[anyone|plyr, "orphan_talk",
	[
		(ge, "$orphan_grown_count", 240),
		(this_or_next|eq, "$wm_comp_id_1", -1),
		(this_or_next|eq, "$wm_comp_id_2", -1),
		(this_or_next|eq, "$wm_comp_id_3", -1),
		(this_or_next|eq, "$wm_comp_id_4", -1),
		(eq, "$wm_comp_id_5", -1)
	],
	"You are an adult now. Help my job.", "orphan_join",
	[
		(call_script, "script_wm_comp_in_party_slot", "$g_talk_troop")
	]],

	[anyone, "orphan_join",
	[],
	"Okay. I can fight well!", "close_window",
	[]],

	[anyone|plyr, "orphan_talk",
	[],
	"We need to separate.", "orphan_disable",
	[]],

	[anyone, "orphan_disable",
	[],
	"Why? I have something wrong? why?", "orphan_confirm",
	[]],

	[anyone|plyr, "orphan_confirm",
	[],
	"Sorry. I deluded that.", "close_window",
	[]],

	[anyone|plyr, "orphan_confirm",
	[],
	"Good bye. forever", "close_window",
	[
		(assign, "$orphan_girl_troop_id", -1),
		(call_script, "script_wm_honor_change_diff", "trp_player", 10, 34),
		(play_sound, "snd_cryyy_female"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return")
	]],

	[anyone|plyr, "orphan_talk",
	[],
	"Good bye.", "close_window",
	[]],

	[anyone|plyr, "pope_talk",
	[],
	"Your Majesty, we must declare the holy war.", "pope_holywar",
	[]],

	[anyone, "pope_holywar",
	[
		(is_between, "$rt_marked_target", "p_pyongyang", "p_place_end"),
		(store_faction_of_party, ":faction_of_party_rt_marked_target", "$rt_marked_target"),
		(faction_get_slot, ":faction_of_party_rt_marked_target_27", ":faction_of_party_rt_marked_target", 27),
		(troop_get_slot, ":g_talk_troop_23", "$g_talk_troop", 23),
		(assign, ":value", 1),
		(try_begin),
			(eq, ":faction_of_party_rt_marked_target_27", ":g_talk_troop_23"),
			(assign, ":value", 0),
		(else_try),
			(eq, ":g_talk_troop_23", 4),
			(eq, ":faction_of_party_rt_marked_target_27", 5),
			(assign, ":value", 0),
		(try_end),
		(eq, ":value", 1)
	],
	"The Holywar. What is object about your holy war?", "pope_holywar_list",
	[]],

	[anyone, "pope_holywar",
	[],
	"What is your object? (system: You need to set correctly 'map marker'.)", "close_window",
	[]],

	[anyone|plyr, "pope_holywar_list",
	[
		(store_faction_of_party, ":faction_of_party_rt_marked_target", "$rt_marked_target"),
		(faction_get_slot, ":faction_of_party_rt_marked_target_27", ":faction_of_party_rt_marked_target", 27),
		(str_store_party_name, 8, "$rt_marked_target"),
		(str_store_faction_name, 9, ":faction_of_party_rt_marked_target"),
		(store_add, ":value", ":faction_of_party_rt_marked_target_27", "str_religion_title_0"),
		(str_store_string, 10, ":value")
	],
	"The {s8} of {s9}, they are believe {s10}.", "pope_holywar_repond",
	[]],

	[anyone|plyr, "pope_holywar_list",
	[],
	"Nevermind. ", "close_window",
	[]],

	[anyone, "pope_holywar_repond",
	[
		(troop_get_slot, ":player_23", "trp_player", 23),
		(neg|troop_slot_eq, "$g_talk_troop", 23, ":player_23")
	],
	"What? are you crazy? but you are heretic! (system: Your religion are different.", "close_window",
	[]],

	[anyone, "pope_holywar_repond",
	[
		(this_or_next|eq, "$g_talk_troop", "trp_ex_npc_059"),
		(eq, "$g_talk_troop", "trp_ex_npc_060"),
		(neg|faction_slot_eq, "$wm_player_fac", 1, "trp_player")
	],
	"The important thing should be talk with the king. but you are not.(system: 'faction leader' only can suggest to pope(or tenno).", "close_window",
	[]],

	[anyone, "pope_holywar_repond",
	[
		(set_show_messages, 0),
		(faction_get_slot, ":wm_player_fac_culture", "$wm_player_fac", slot_faction_culture),
		(val_div, ":wm_player_fac_culture", 23),
		(set_show_messages, 1),
		(lt, ":wm_player_fac_culture", 19000)
	],
	"Your kingdom did devote to the religion? I don't think so.(system: holywar require culture point 19000.)", "close_window",
	[]],

	[anyone, "pope_holywar_repond",
	[],
	"I understand. We will make a decision In association with other countries.", "close_window",
	[
		(call_script, "script_culture_point_diff", "$wm_player_fac", 19000, 34),
		(troop_get_slot, ":g_talk_troop_23", "$g_talk_troop", 23),
		(assign, "$holy_war_religion_att", ":g_talk_troop_23"),
		(store_faction_of_party, ":faction_of_party_rt_marked_target", "$rt_marked_target"),
		(faction_get_slot, ":faction_of_party_rt_marked_target_27", ":faction_of_party_rt_marked_target", 27),
		(assign, "$holy_war_religion_def", ":faction_of_party_rt_marked_target_27"),
		(assign, "$holy_war_target_party", "$rt_marked_target"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_pst_holywar")
	]],

	[anyone|plyr, "pope_talk",
	[],
	"    I must beg my leave.", "close_window",
	[]],

	[anyone|plyr, "sister_talk",
	[
		(eq, "$main_q_step", 16)
	],
	"Finally I found you.", "mq_16_2",
	[]],

	[anyone, "mq_16_2",
	[],
	"Is it really you? Oh my god.", "mq_16_3",
	[]],

	[anyone|plyr, "mq_16_3",
	[],
	"We don't have much time now. We must get out of here right now.", "mq_16_4",
	[]],

	[anyone, "mq_16_4",
	[],
	"I know... Watch your back!", "close_window",
	[
		(assign, "$main_q_step", 17),
		(mission_disable_talk),
		(add_visitors_to_current_scene, 22, "trp_raid_bandit_boss", 2)
	]],

	[anyone|plyr, "sister_talk",
	[
		(eq, "$main_q_step", 44)
	],
	"I am glad to see you in good health. my sister.", "mq_44_2",
	[]],

	[anyone, "mq_44_2",
	[],
	"What? is it really you? Oh my god.", "mq_44_3",
	[]],

	[anyone|plyr, "mq_44_3",
	[],
	"Follow me. We can escape to the window.", "mq_44_4",
	[]],

	[anyone, "mq_44_4",
	[],
	"No, I don't want to leave here", "mq_44_5",
	[]],

	[anyone|plyr, "mq_44_5",
	[],
	"What are you talking about? have you had any problems?", "mq_44_6",
	[]],

	[anyone, "mq_44_6",
	[],
	"I am no longer a slave. The owner of this mansion is my husband.", "mq_44_7",
	[]],

	[anyone|plyr, "mq_44_7",
	[],
	"Are you serious? You have really thought that slave buyer as your husband?", "mq_44_8",
	[]],

	[anyone, "mq_44_8",
	[],
	"If you have conversation with him, you can understand about me.", "mq_44_9",
	[]],

	[anyone|plyr, "mq_44_9",
	[],
	"Enough! Stop this foolish bullshit right now. You should be following me.", "mq_44_10",
	[]],

	[anyone, "mq_44_10",
	[],
	"Please have a talk with him. He's not a bad person.", "mq_44_11",
	[]],

	[anyone|plyr, "mq_44_11",
	[],
	" Enough!", "mq_44_12",
	[]],

	[anyone, "mq_44_12",
	[],
	"Please, give me a chance to explain. oh, I don't want to harm you.", "mq_44_13",
	[
		(set_conversation_speaker_troop, "trp_vaegir_merchant")
	]],

	[anyone|plyr, "mq_44_13",
	[],
	"!!Who are you?", "mq_44_14",
	[]],

	[anyone, "mq_44_14",
	[],
	"I'm owner of this mansion, and Duke of Bavaria.", "mq_44_15",
	[
		(set_conversation_speaker_troop, "trp_vaegir_merchant")
	]],

	[anyone|plyr, "mq_44_15",
	[],
	"and master of my sister?", "mq_44_16",
	[]],

	[anyone, "mq_44_16",
	[],
	"I am not the master of her.", "mq_44_17",
	[
		(set_conversation_speaker_troop, "trp_vaegir_merchant")
	]],

	[anyone, "mq_44_17",
	[],
	"he is my husband. Please have a talk with him.", "mq_44_18",
	[]],

	[anyone, "mq_44_18",
	[],
	"I'll tell you everything.", "mq_44_19",
	[
		(set_conversation_speaker_troop, "trp_vaegir_merchant")
	]],

	[anyone, "mq_44_19",
	[],
	"[He began to explain about himself. He had bought her as a slave. But he gave to the freedom. After that, He began speech, About how much he love her.]", "mq_44_20",
	[
		(set_conversation_speaker_troop, "trp_vaegir_merchant")
	]],

	[anyone, "mq_44_20",
	[],
	"[You were staring at your sister. You can feel that she is also sincere.]", "mq_44_21",
	[]],

	[anyone|plyr, "mq_44_21",
	[],
	"Yet I can not afford it. anyway, I will leave alone today.", "mq_44_22",
	[]],

	[anyone, "mq_44_22",
	[],
	"   {playername}!!", "mq_44_23",
	[]],

	[anyone|plyr, "mq_44_23",
	[],
	"When my thought is organized, I will come back here.", "mq_44_24",
	[]],

	[anyone, "mq_44_24",
	[],
	"You are always welcome. {playername}", "close_window",
	[
		(set_conversation_speaker_troop, "trp_vaegir_merchant"),
		(assign, "$main_q_step", 45),
		(assign, "$main_q_day", 60),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return"),
		(jump_to_menu, "mnu_wm_pst_map_return")
	]],

	[anyone|plyr, "sister_talk",
	[
		(eq, "$main_q_step", 50)
	],
	"You now seems like to wife of nobility. Seriously, do you satisfy to this situation?", "mq_50_2",
	[]],

	[anyone, "mq_50_2",
	[],
	"Of course. I know, you can't understand me. But this is the truth.", "mq_50_3",
	[]],

	[anyone, "mq_50_3",
	[],
	"That's what I'm saying.", "mq_50_4",
	[
		(set_conversation_speaker_troop, "trp_vaegir_merchant")
	]],

	[anyone, "mq_50_4",
	[],
	"[For 5 hours, You had talk with this couple. And you were aware the fact that you cannot persuade sister.]", "mq_50_5",
	[
		(set_conversation_speaker_troop, "trp_vaegir_merchant")
	]],

	[anyone|plyr, "mq_50_5",
	[],
	"I can't help it. Congratulations on your marriage.", "mq_50_6",
	[]],

	[anyone, "mq_50_6",
	[],
	"  {playername}!!", "mq_50_7",
	[]],

	[anyone|plyr, "mq_50_7",
	[],
	"[You wanted to leave something for her. And you reminded the necklace picked up at the desert fortress.] Please receive this necklace as a wedding gift. ", "mq_50_8",
	[]],

	[anyone, "mq_50_8",
	[],
	"Thank you {playername}!! ", "mq_50_9",
	[]],

	[anyone|plyr, "mq_50_9",
	[],
	"I'll leave. if you have some happening, just sending letter to me.", "close_window",
	[
		(assign, "$main_q_step", 51),
		(assign, "$main_q_day", 30),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return"),
		(jump_to_menu, "mnu_wm_pst_map_return")
	]],

	[anyone|plyr, "sister_talk",
	[
		(eq, "$g_encountered_party", "p_ruin_dummy_3"),
		(ge, "$main_q_step", 51)
	],
	"I'm very well. How are you doing? ", "sis_ord_talk",
	[]],

	[anyone, "sis_ord_talk",
	[],
	"I'm pretty good, too.", "close_window",
	[
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return")
	]],

	[anyone|plyr, "mainq_48_1",
	[],
	"Welcome. This trip will not be bored.", "close_window",
	[
		(assign, "$main_q_step", 49),
		(party_set_flags, "p_ruin_dummy_5", 256, 1),
		(call_script, "script_wm_comp_in_party_slot", "$main_q_troop"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return")
	]],

	[anyone|plyr, "mainq_20_1",
	[],
	"What? what are you talking about?", "mainq_20_2",
	[]],

	[anyone, "mainq_20_2",
	[],
	"Of course, they are slave traders. Your sister has captivated to them.", "mainq_20_3",
	[]],

	[anyone, "mainq_20_3",
	[],
	"We haven't much time. follow me, I can track them. ", "mainq_20_4",
	[]],

	[anyone|plyr, "mainq_20_4",
	[],
	"(I have suspicion about him. but I followed his back.)", "close_window",
	[
		(assign, "$main_q_step", 21),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_main_quest_menu")
	]],

	[anyone, "temp_talker",
	[
		(eq, "$main_q_step", 32)
	],
	"Thank you for letting me liberation from hell.", "mainq_32_1",
	[
		(set_conversation_speaker_troop, "$main_q_troop")
	]],

	[anyone|plyr, "mainq_32_1",
	[],
	"Where is your hometown? I can take you there.", "mainq_32_2",
	[]],

	[anyone, "mainq_32_2",
	[],
	"My hometown was completely destroyed. This place was my hometown in past.", "mainq_32_3",
	[
		(set_conversation_speaker_troop, "$main_q_troop")
	]],

	[anyone|plyr, "mainq_32_3",
	[],
	"You may have other choice....You can travel with us!", "mainq_32_4",
	[]],

	[anyone, "mainq_32_4",
	[],
	"I am a useless woman. If you do not mind, I will gladly join to your party.", "mainq_32_5",
	[
		(set_conversation_speaker_troop, "$main_q_troop")
	]],

	[anyone|plyr, "mainq_32_5",
	[],
	"I respect your choice. welcome.", "close_window",
	[
		(assign, "$main_q_step", 33),
		(assign, "$main_q_day", 60),
		(call_script, "script_wm_comp_in_party_slot", "$main_q_troop"),
		(party_set_flags, "p_ruin_dummy_5", 256, 1),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return"),
		(jump_to_menu, "mnu_wm_pst_map_return")
	]],

	[anyone, "temp_talker",
	[
		(eq, "$main_q_step", 86)
	],
	"Is there any good news? {playername}.", "mainq_86_1",
	[
		(set_conversation_speaker_troop, "trp_ex_npc_057")
	]],

	[anyone|plyr, "mainq_86_1",
	[],
	"I have found Shroud of Jesus. At least they believe so.", "mainq_86_2",
	[]],

	[anyone, "mainq_86_2",
	[],
	"Good. and now, my troops be freed from the stupid mission. Finally I can help you.", "mainq_86_3",
	[
		(set_conversation_speaker_troop, "trp_ex_npc_057")
	]],

	[anyone|plyr, "mainq_86_3",
	[],
	"Now I'll prepare the army.", "mainq_86_4",
	[]],

	[anyone, "mainq_86_4",
	[],
	"Wait. Our troops are still small-scale. we need more support of others.", "mainq_86_5",
	[
		(set_conversation_speaker_troop, "trp_ex_npc_057")
	]],

	[anyone|plyr, "mainq_86_5",
	[],
	"Others? Who can help us?", "mainq_86_6",
	[]],

	[anyone, "mainq_86_6",
	[],
	"Everything hinges on you. You should be talking with warlords. If you are friend of them, they will help you.", "mainq_86_7",
	[
		(set_conversation_speaker_troop, "trp_ex_npc_057")
	]],

	[anyone, "mainq_86_7",
	[],
	"Or give money to them. then you can borrow the army from them.", "mainq_86_8",
	[
		(set_conversation_speaker_troop, "trp_ex_npc_057")
	]],

	[anyone|plyr, "mainq_86_8",
	[],
	"I understood. I'm going right away.", "close_window",
	[
		(assign, "$main_q_step", 87),
		(assign, "$main_q_troop", 0),
		(assign, "$main_q_faction", 0),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return"),
		(jump_to_menu, "mnu_wm_pst_map_return")
	]],

	[anyone, "temp_talker",
	[
		(eq, "$main_q_step", 83)
	],
	"Welcome. I've been heard your name {playername}. So what happened?", "mainq_83_1",
	[
		(set_conversation_speaker_troop, "trp_ex_npc_057")
	]],

	[anyone|plyr, "mainq_83_1",
	[],
	"I heard that knights templar had fight against to hashashins.", "mainq_83_2",
	[]],

	[anyone, "mainq_83_2",
	[],
	"Of course. They are one of our enemies. But to be honest, We don't have any intend to attack them now.", "mainq_83_3",
	[
		(set_conversation_speaker_troop, "trp_ex_npc_057")
	]],

	[anyone|plyr, "mainq_83_3",
	[],
	"Is there any other way? I must destroy them.", "mainq_83_4",
	[]],

	[anyone, "mainq_83_4",
	[],
	"We are now busy at finding the relics of Jesus. If you help us, the time may be shortened.", "mainq_83_5",
	[
		(set_conversation_speaker_troop, "trp_ex_npc_057")
	]],

	[anyone|plyr, "mainq_83_5",
	[],
	"what is the relics of Jesus? How can this old thing has still existed?", "mainq_83_6",
	[]],

	[anyone, "mainq_83_6",
	[],
	"I think it's a fake. But people do not care whether if it is a fake or real. We just need a outsider who can find it for persuasively.", "mainq_83_7",
	[
		(set_conversation_speaker_troop, "trp_ex_npc_057")
	]],

	[anyone|plyr, "mainq_83_7",
	[],
	"I understand that what you want. what is next?", "mainq_83_8",
	[]],

	[anyone, "mainq_83_8",
	[],
	"According to our research, This is rumored to be near Genoa.", "mainq_83_9",
	[
		(set_conversation_speaker_troop, "trp_ex_npc_057")
	]],

	[anyone|plyr, "mainq_83_9",
	[],
	"If i have succeeded to finding it, Can you promised me the military support?", "mainq_83_10",
	[]],

	[anyone, "mainq_83_10",
	[],
	"Hashashin is one of our enemy. We will fight against them.", "mainq_83_11",
	[
		(set_conversation_speaker_troop, "trp_ex_npc_057")
	]],

	[anyone|plyr, "mainq_83_11",
	[],
	"Good. I must beg my leave. Grand master.", "close_window",
	[
		(assign, "$main_q_step", 84),
		(assign, "$main_q_faction", "p_ruin_dummy_2"),
		(init_position, 9),
		(set_fixed_point_multiplier, 1000),
		(position_set_x, 9, 126000),
		(position_set_y, 9, -244000),
		(party_set_position, "p_ruin_dummy_2", 9),
		(party_set_name, "p_ruin_dummy_2", "str_hidden_cathedral"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return"),
		(jump_to_menu, "mnu_wm_pst_map_return")
	]],

	[anyone, "temp_talker",
	[
		(eq, "$main_q_step", 72)
	],
	"{playername}!!  I am the servant of your sister. Our mansion has under attack!!", "mainq_72_1",
	[
		(set_conversation_speaker_troop, "trp_khergit_merchant")
	]],

	[anyone|plyr, "mainq_72_1",
	[],
	"Where is my sister? Who are these attackers?", "mainq_72_2",
	[]],

	[anyone, "mainq_72_2",
	[],
	"I'm really sorry about that.  I don't know whether about she happened. They are looked like to the Arab armies.", "mainq_72_3",
	[
		(set_conversation_speaker_troop, "trp_khergit_merchant")
	]],

	[anyone|plyr, "mainq_72_3",
	[],
	"Where is her husband now?", "mainq_72_4",
	[]],

	[anyone, "mainq_72_4",
	[],
	"Duke was killed during the battle. He requested me before he dies. He requested me before him die, try to asking help from you.", "mainq_72_5",
	[
		(set_conversation_speaker_troop, "trp_khergit_merchant")
	]],

	[anyone|plyr, "mainq_72_5",
	[],
	"Enough! I will be going there right now.", "close_window",
	[
		(assign, "$main_q_step", 73),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return")
	]],

	[anyone, "temp_talker",
	[
		(eq, "$main_q_step", 70)
	],
	"{playername}!! They are coming! we need attack them Immediately!", "mainq_70_1",
	[
		(set_conversation_speaker_troop, "trp_swadian_merchant")
	]],

	[anyone|plyr, "mainq_70_1",
	[],
	"What? Who are they?", "mainq_70_2",
	[]],

	[anyone, "mainq_70_2",
	[],
	"Arab armies! I had to track them. and They are tracking you. we must attack them Immediately!", "mainq_70_3",
	[
		(set_conversation_speaker_troop, "trp_swadian_merchant")
	]],

	[anyone, "mainq_70_3",
	[],
	"[I have suspicious to his intentions, related about man who tried to say to me before.]", "mainq_70_4",
	[
		(set_conversation_speaker_troop, "trp_swadian_merchant")
	]],

	[anyone|plyr, "mainq_70_4",
	[],
	"No. I will not engage them. Because I don't know exactly about their intention.", "mainq_70_5",
	[]],

	[anyone, "mainq_70_5",
	[],
	"What?...I understood. take care.", "close_window",
	[
		(set_conversation_speaker_troop, "trp_swadian_merchant"),
		(assign, "$main_q_step", 71),
		(assign, "$main_q_day", 60),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return"),
		(jump_to_menu, "mnu_wm_pst_map_return")
	]],

	[anyone, "temp_talker",
	[
		(eq, "$main_q_step", 69)
	],
	"You...", "mainq_69_1",
	[
		(set_conversation_speaker_troop, "trp_ww_a_5_2")
	]],

	[anyone, "mainq_69_1",
	[],
	"[That moment, Arrows has flown to the man. and this arrows had penetrate heart of man.]", "mainq_69_2",
	[
		(play_sound, "snd_sea_bow_shoot"),
		(set_conversation_speaker_troop, "trp_ww_a_5_2")
	]],

	[anyone, "mainq_69_2",
	[],
	"Are you ok? This man has tried to kill you!", "mainq_69_3",
	[
		(set_conversation_speaker_troop, "trp_swadian_merchant")
	]],

	[anyone|plyr, "mainq_69_3",
	[],
	"I'm okay. why you here?", "mainq_69_4",
	[]],

	[anyone, "mainq_69_4",
	[],
	"I've been tracking this man. He is suspected of killing a scholar.", "mainq_69_5",
	[
		(set_conversation_speaker_troop, "trp_swadian_merchant")
	]],

	[anyone|plyr, "mainq_69_5",
	[],
	"but he seemed to saying to me. I'm a little confused.", "mainq_69_6",
	[]],

	[anyone, "mainq_69_6",
	[],
	"Please calm down. I'll investigate more this man.", "close_window",
	[
		(set_conversation_speaker_troop, "trp_swadian_merchant"),
		(assign, "$main_q_step", 70),
		(assign, "$main_q_day", 30),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return"),
		(jump_to_menu, "mnu_wm_pst_map_return")
	]],

	[anyone, "temp_talker",
	[
		(eq, "$main_q_step", 60)
	],
	"Welcome my hero! I heard that you had destroyed all the beggars.", "mainq_60_1",
	[
		(set_conversation_speaker_troop, "trp_temporary_minister")
	]],

	[anyone|plyr, "mainq_60_1",
	[],
	"I'm just interested in the reward.", "mainq_60_2a",
	[]],

	[anyone, "mainq_60_2a",
	[],
	"Of course! I will be your ardent supporter.", "close_window",
	[
		(set_conversation_speaker_troop, "trp_temporary_minister"),
		(call_script, "script_party_money_level_diff", "p_main_party", 10000, 87),
		(assign, "$main_q_step", 61),
		(assign, "$main_q_day", 60),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return"),
		(jump_to_menu, "mnu_wm_pst_map_return")
	]],

	[anyone|plyr, "mainq_60_1",
	[],
	"I have the question of one thing.", "mainq_60_2b",
	[]],

	[anyone, "mainq_60_2b",
	[],
	"[You had to question about the brides.] They are serfs. That's just a common level.", "mainq_60_3b",
	[
		(set_conversation_speaker_troop, "trp_temporary_minister")
	]],

	[anyone|plyr, "mainq_60_3b",
	[],
	"[Cuts his neck.]", "mainq_60_4a",
	[]],

	[anyone|plyr, "mainq_60_4a",
	[],
	"[it will be cause of some problems. But your behavior is very faster than you think.]", "close_window",
	[
		(play_sound, "snd_man_die"),
		(call_script, "script_wm_honor_change_diff", "trp_player", 35, 87),
		(assign, "$main_q_step", 61),
		(assign, "$main_q_day", 60),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return"),
		(jump_to_menu, "mnu_wm_pst_map_return")
	]],

	[anyone|plyr, "mainq_60_3b",
	[],
	"I do not care about it. where is my money?", "mainq_60_4b",
	[]],

	[anyone, "mainq_60_4b",
	[],
	" Of course! I will be your ardent supporter.", "close_window",
	[
		(set_conversation_speaker_troop, "trp_temporary_minister"),
		(call_script, "script_wm_honor_change_diff", "trp_player", 10, 34),
		(call_script, "script_party_money_level_diff", "p_main_party", 50000, 87),
		(assign, "$main_q_step", 61),
		(assign, "$main_q_day", 60),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_wm_pst_map_return"),
		(jump_to_menu, "mnu_wm_pst_map_return")
	]],

	[anyone, "temp_talker",
	[
		(eq, "$main_q_step", 59)
	],
	"You son of a bitch, You cannot hide these things forever.", "mainq_59_1",
	[
		(set_conversation_speaker_troop, "trp_rebels_fort_leader")
	]],

	[anyone|plyr, "mainq_59_1",
	[],
	"I don't have to hide. What are you talking about?", "mainq_59_2",
	[]],

	[anyone, "mainq_59_2",
	[],
	"What? haha! you are just stupid puppet.", "mainq_59_3",
	[
		(set_conversation_speaker_troop, "trp_rebels_fort_leader")
	]],

	[anyone, "mainq_59_3",
	[],
	"The world listen to my words! the crazy landowner have robbed virginity of every bride!", "mainq_59_4",
	[
		(set_conversation_speaker_troop, "trp_rebels_fort_leader")
	]],

	[anyone, "mainq_59_4",
	[],
	"[It was his last words. His serious wounds had pushing himself into the death.]", "close_window",
	[
		(assign, "$main_q_step", 60),
		(set_conversation_speaker_troop, "trp_rebels_fort_leader"),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_main_quest_menu")
	]],

	[anyone, "temp_talker",
	[
		(eq, "$main_q_step", 54)
	],
	"Welcome {playername}", "mainq_54_1",
	[
		(set_conversation_speaker_troop, "trp_tt_lord_22_00")
	]],

	[anyone|plyr, "mainq_54_1",
	[],
	"I'm honored to see you. Great khan.", "mainq_54_2",
	[]],

	[anyone, "mainq_54_2",
	[],
	"I heard that you got the question about my religion.", "mainq_54_3",
	[
		(set_conversation_speaker_troop, "trp_tt_lord_22_00")
	]],

	[anyone|plyr, "mainq_54_3",
	[],
	"Yes. I'm looking for the kingdom of the prester john. If my assumption is correct, you are the prester john.", "mainq_54_4",
	[]],

	[anyone, "mainq_54_4",
	[],
	"Prester john? Haha. It is not bad to my new nickname. yes, I'm nestorian christian. however, my nomadic tribe has not christians. How can this be called by kingdom of christians? It's a complete nonsense.", "mainq_54_5",
	[
		(set_conversation_speaker_troop, "trp_tt_lord_22_00")
	]],

	[anyone, "mainq_54_5",
	[],
	"Nevertheless, I can move my troops to help the Christians. But I wouldn't do that. My real enemy has exist in the meadows.", "mainq_54_6",
	[
		(set_conversation_speaker_troop, "trp_tt_lord_22_00")
	]],

	[anyone|plyr, "mainq_54_6",
	[],
	"I understand you. Thank you for the conversation.", "close_window",
	[
		(assign, "$main_q_step", 55),
		(call_script, "script_wm_finish_mission_menu_popup", "mnu_main_quest_menu")
	]],

	[anyone|plyr, "mq_95_1",
	[],
	"So, that was that all things are false? Why me? Why you killed my sister ?", "mq_95_2",
	[]],

	[anyone, "mq_95_2",
	[],
	"I'm not. It is true that the hashashin armies that attacked us.", "mq_95_3",
	[]],

	[anyone|plyr, "mq_95_3",
	[],
	"and the cause of attack, it is you. right?", "mq_95_4",
	[]],

	[anyone, "mq_95_4",
	[],
	"Wow. You really become smarter! we cannot avoid to fight! Right?", "close_window",
	[
		(mission_disable_talk),
		(try_for_agents, ":value"),
			(agent_get_troop_id, ":troop_id_value", ":value"),
			(eq, ":troop_id_value", "trp_vaegir_merchant"),
			(agent_set_team, ":value", 1),
			(agent_ai_set_aggressiveness, ":value", 199),
		(try_end),
		(team_set_relation, 0, 1, -1),
		(try_for_agents, ":value"),
			(agent_is_alive, ":value"),
			(agent_is_human, ":value"),
			(agent_set_is_alarmed, ":value", 1),
		(try_end)
	]],

	[anyone|plyr, "mq_94_1",
	[],
	"How did you survive?", "mq_94_2",
	[]],

	[anyone, "mq_94_2",
	[],
	"Kill him! Kill him!", "close_window",
	[
		(mission_disable_talk),
		(try_for_agents, ":value"),
			(agent_get_troop_id, ":troop_id_value", ":value"),
			(eq, ":troop_id_value", "trp_cru_5_m"),
			(agent_set_team, ":value", 2),
			(agent_ai_set_aggressiveness, ":value", 199),
		(try_end),
		(team_set_relation, 0, 2, -1),
		(try_for_agents, ":value"),
			(agent_is_alive, ":value"),
			(agent_is_human, ":value"),
			(agent_set_is_alarmed, ":value", 1),
		(try_end)
	]],

	[anyone, "member_chat",
	[
		(eq, "$g_talk_troop", "trp_army_size_troop")
	],
	"(System: This is the representation about your army size)", "close_window",
	[]],

	[anyone, "member_chat",
	[],
	"Your orders {sir/madam}?", "regular_member_talk",
	[]],

	[anyone|plyr, "regular_member_talk",
	[],
	"Tell me about yourself", "view_regular_char_requested",
	[]],

	[anyone, "view_regular_char_requested",
	[],
	"Aye {sir/madam}. Let me tell you all there is to know about me.", "do_regular_member_view_char",
	[
		(change_screen_view_character)
	]],

	[anyone, "do_regular_member_view_char",
	[],
	"Anything else?", "regular_member_talk",
	[]],

	[anyone|plyr, "regular_member_talk",
	[],
	"Nothing. Keep moving.", "close_window",
	[]],

	[anyone|plyr, "prisoner_chat",
	[],
	"Do not try running away or trying something stupid. I will be watching you.", "prisoner_chat_2",
	[]],

	[anyone, "prisoner_chat_2",
	[
		(troop_is_hero, "$g_talk_troop")
	],
	"Ha!, You'll pay for this.", "close_window",
	[]],

	[anyone, "prisoner_chat_2",
	[],
	"No, I swear I won't.", "close_window",
	[]],


	
]