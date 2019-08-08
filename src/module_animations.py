from header_common import *
from header_animations import *

####################################################################################################################
#  There are two animation arrays (one for human and one for horse). Each animation in these arrays contains the following fields:
#  1) Animation id (string): used for referencing animations in other files. The prefix anim_ is automatically added before each animation-id .
#  2) Animation flags: could be anything beginning with acf_ defined in header_animations.py
#  3) Animation master flags: could be anything beginning with amf_ defined in header_animations.py
#  4) Animation sequences (list).
#  4.1) Duration of the sequence.
#  4.2) Name of the animation resource.
#  4.3) Beginning frame of the sequence within the animation resource.
#  4.4) Ending frame of the sequence within the animation resource.
#  4.5) Sequence flags: could be anything beginning with arf_ defined in header_animations.py
# 
####################################################################################################################

#plan : 
# basic movement : walk ride etc. 0 -20000
#  on_foot  : 0     - 10000
#  horse    : 10000 - 20000
# combat         :                20000 - 40000
# fall           :                4000 - 70000
# act            : misc.          70000 - ...

amf_priority_jump           = 2
amf_priority_ride           = 2
amf_priority_continue       = 1
amf_priority_attack         = 10
amf_priority_cancel         = 12
amf_priority_defend         = 14
amf_priority_defend_parry   = amf_priority_defend + 1
amf_priority_throw          = amf_priority_defend + 1
amf_priority_blocked        = amf_priority_defend_parry
amf_priority_parried        = amf_priority_defend_parry
amf_priority_kick           = 33
amf_priority_jump_end       = 33
amf_priority_reload         = 60
amf_priority_mount          = 64
amf_priority_equip          = 70
amf_priority_rear           = 74
amf_priority_striked        = 80
amf_priority_fall_from_horse= 81
amf_priority_die            = 95



horse_move = 10000
combat     = 20000
defend     = 35000
blow       = 40000

attack_parried_duration = 0.6
attack_blocked_duration = 0.3
attack_blocked_duration_thrust = attack_blocked_duration + 0.3
attack_parried_duration_thrust = attack_parried_duration + 0.1
defend_parry_duration_1 = 0.6
defend_parry_duration_2 = 0.6
defend_parry_duration_3 = 0.8
ready_durn     = 0.35
defend_duration = 0.75
defend_keep_duration = 2.0
cancel_duration = 0.25

blend_in_defense = arf_blend_in_3
blend_in_ready = arf_blend_in_6
blend_in_release = arf_blend_in_5
blend_in_parry = arf_blend_in_5
blend_in_parried = arf_blend_in_3


blend_in_walk = arf_blend_in_3
blend_in_continue = arf_blend_in_1

#### Animations begin here

# All of the animations are hardcoded. You can edit the individual sequences, resources or times. But each
# animation must stay at the same position, otherwise the game won't run properly. If you want to add a new animation,
# you can change both the ids and values of the animations which are named as unused_human_anim_???
# and unused_horse_anim_??? (??? = any number). You must not change used animations' ids.

animations = [
# ["stand", 0, amf_client_prediction,
 #  [3.0, "anim_human", 50, 52, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],








































































































































































































































































































































































































































































































 #  [3.0, "anim_human", 60, 62, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.75],


















 #  [3.0, "anim_human", 70, 72, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































 #  [3.0, "anim_human", 80, 82, arf_use_stand_progress|arf_cyclic|arf_two_handed_blade, 0, (0, 0, 0), 0.5],




































 #],



 ["stand", 0, amf_client_prediction, #Try using amf_client_owner_prediction for server side instead
   [11.0, "stand_man", 0, 315, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [11.0, "new_stand_man", 0, 314, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [45.0, "lord_listen", 0, 962, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [11.0, "stand_man", 0, 315, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [65.0, "lord_sant2", 0, 1400, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [60.0, "lord_sant2", 1400, 2550, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [60.0, "lord_sant2", 2550, 3601, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [11.0, "new_stand_man", 0, 314, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [11.0, "stand_man", 0, 315, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 ],
 
 ["stand_man", 0, amf_client_prediction, #Try using amf_client_owner_prediction for server side instead
   [11.0, "stand_man", 0, 315, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [11.0, "new_stand_man", 0, 314, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [45.0, "lord_listen", 0, 962, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [11.0, "stand_man", 0, 315, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [65.0, "lord_sant2", 0, 1400, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [60.0, "lord_sant2", 1400, 2550, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [60.0, "lord_sant2", 2550, 3601, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [10.0, "lord_stand", 0, 111, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [11.0, "new_stand_man", 0, 314, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [11.0, "stand_man", 0, 315, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 
 ],
 ["stand_player_first_person", 0, amf_client_prediction, #Try using amf_client_owner_prediction for server side instead
   [3.5, "anim_human", 90, 100, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [3.5, "anim_human", 110, 120, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 ],
 ["jump", acf_enforce_lowerbody, amf_priority_jump|amf_play|amf_client_prediction|amf_continue_to_next,
##   [1.09, "jump", 22, 48, arf_blend_in_1],
   [1.0, "jump", 22, 46, arf_blend_in_1],
##   [0.8, "anim_human", 270, 272, arf_blend_in_4],
 ],
 ["jump_loop", acf_enforce_lowerbody, amf_priority_jump|amf_play|amf_client_prediction,
##   [0.8, "jump_loop", 0, 30, arf_blend_in_2|arf_cyclic],
   [0.5, "jump_loop", 0, 14, arf_blend_in_3|arf_cyclic],
 ],
 ["jump_end", acf_enforce_lowerbody, amf_priority_jump_end|amf_play|amf_client_prediction,
##   [0.1, "jump", 48, 55, arf_blend_in_1],
   [0.3, "jump", 48, 55, arf_blend_in_2],
 ],
 ["jump_end_hard", acf_enforce_lowerbody, amf_priority_jump_end|amf_play|amf_client_prediction,
##   [0.8, "jump_end_hard", 29, 54, arf_blend_in_1],
   [0.6, "jump_end_hard", 36, 54, arf_blend_in_1],
 ],
 ["stand_unarmed", 0, amf_client_prediction,
   [8, "noweapon_cstance", 0, 100, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 ],
 #["stand_single", 0, amf_client_prediction,
  # [9.0, "sword_loop01", 0, 200, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
# ],




 #hispania 1200




 ["stand_single", 0, amf_client_prediction,
   [15.0, "sword_loop01", 0, 200, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [17.0, "sword_loop02", 0, 100, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 #  [13.0, "sword_loop03", 0, 100, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [15.0, "sword_loop04", 0, 100, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [14.0, "sword_loop05", 0, 200, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [12.0, "sword_loop06", 0, 100, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 #  [20.0, "sword_loop08", 0, 200, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 #  [12.0, "sword_loop09", 0, 100, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 #  [12.0, "sword_loop10", 0, 100, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   
 #  [15.0, "staff_cstance_new", 0, 59, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],



    ],
 
# ["stand_greatsword", 0, amf_client_prediction,
 #  [6.0, "greatsword_cstance", 0, 91, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],  
# ],




 #hispania 1200




 ["stand_greatsword", 0, amf_client_prediction,
   [8.0, "greatsword_cstance", 0, 85, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [8.0, "crouch_greatsword_cstance", 0, 170, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [8.0, "pike_loop01", 0, 99, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [8.0, "greatsword_cstance", 0, 85, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [15.0, "staff_cstance_new", 0, 59, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [8.0, "pike_loop02", 0, 99, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [8.0, "pike_loop03", 0, 134, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
 ],







 
# ["stand_staff", 0, amf_client_prediction,
  # [2.0, "staff_cstance", 0, 60, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],  
# ],




#hispania 1200




 ["stand_staff", 0, amf_client_prediction, 
   [8.0, "staff_cstance", 0, 60, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [15.0, "pike_loop01", 0, 99, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0],
  # [4.0, "stand_staff_rot_left", 0, 60, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [15.0, "pike_loop02", 0, 99, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0],
  # [4.0, "stand_staff_rot_right", 0, 60, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [15.0, "crouch_staff_cstance", 0, 120, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [15.0, "staff_cstance_new", 0, 59, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [8.0, "pike_loop03", 0, 134, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],




    ],
 
 ["stand_crossbow", 0, amf_client_prediction,
   [8.0, "staff_cstance", 0, 60, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [8.0, "staff_cstance", 0, 60, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [4.0, "stand_staff_rot_right", 0, 60, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [8.0, "staff_cstance", 0, 60, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
   [4.0, "stand_staff_rot_left", 0, 60, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],
 ],


 
 ["turn_right", acf_enforce_lowerbody, amf_play|amf_client_prediction,
   [0.95, "stand_man", 0, 30, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25], #TODO
 ],
 ["turn_left", acf_enforce_lowerbody, amf_play|amf_client_prediction,
   [0.95, "stand_man", 0, 30, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25], #TODO
 ],
 ["turn_right_single", acf_enforce_lowerbody, amf_play|amf_client_prediction,
    [0.95, "turn_man_onehanded", 0, 23, arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["turn_left_single", acf_enforce_lowerbody, amf_play|amf_client_prediction,
   [0.95, "turn_man_onehanded", 30, 53, arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["turn_right_staff", acf_enforce_lowerbody, amf_play|amf_client_prediction,
   [0.95, "turn_man_staff", 0, 20, arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["turn_left_staff", acf_enforce_lowerbody, amf_play|amf_client_prediction,
   [0.95, "turn_man_staff", 30, 50, arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["turn_right_greatsword", acf_enforce_lowerbody, amf_play|amf_client_prediction,
   [0.95, "turn_man_greatsword", 0, 20, arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["turn_left_greatsword", acf_enforce_lowerbody, amf_play|amf_client_prediction,
   [0.95, "turn_man_greatsword", 30, 50, arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["prepare_kick_0", acf_enforce_lowerbody, amf_priority_kick|amf_play|amf_client_prediction|amf_continue_to_next,
   [0.05, "kick_rightleg", 10, 12, arf_blend_in_3],
 ],
 ["prepare_kick_1", acf_enforce_lowerbody, amf_priority_kick|amf_play|amf_client_prediction|amf_continue_to_next,
   [0.05, "kick_rightleg", 12, 12, arf_blend_in_3],
 ],
 ["prepare_kick_2", acf_enforce_lowerbody, amf_priority_kick|amf_play|amf_client_prediction|amf_continue_to_next, 
   [0.05, "kick_rightleg", 12, 12, arf_blend_in_3],
 ],
 ["prepare_kick_3", acf_enforce_lowerbody, amf_priority_kick|amf_play|amf_client_prediction|amf_continue_to_next, #Doghotel begin
   [0.05, "kick_rightleg", 12, 12, arf_blend_in_3],
 ],
 ["kick_right_leg", acf_enforce_lowerbody, amf_priority_kick|amf_play|amf_client_prediction, #Doghotel end
##   [1.09, "jump", 22, 48, arf_blend_in_1],
   [0.7, "kick_rightleg", 12, 33, arf_blend_in_1],
 ],
 ["kick_left_leg", acf_enforce_lowerbody, amf_priority_kick|amf_play|amf_client_prediction,
##   [1.09, "jump", 22, 48, arf_blend_in_1],
   [0.7, "kick_rightleg", 12, 33, arf_blend_in_1],
 ],
 ["run_forward", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [0.8, "anim_human", 7000, 7040, arf_use_walk_progress|arf_cyclic|blend_in_walk,pack2f(0.4,0.9)], 
   [0.8, "run_man_forward", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
# ["run_forward_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [0.8, "anim_human", 7000, 7040, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9)], 
#   [0.8, "run_normal", 0, 12, arf_use_walk_progress|arf_cyclic|blend_in_walk,pack2f(0.4,0.9)], 
 #  [0.8, "run_man_forward_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
# ],




#hispania 1200




 ["run_forward_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.8, "run_man_forward_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_sword_1", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
   [0.8, "run_sword_2", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
   [0.8, "run_sword_3", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
   [0.8, "run_man_forward_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_sword_4", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
   [0.8, "run_sword_5", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
   [0.8, "run_sword_6", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
   [0.8, "run_sword_7", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 #  [0.8, "run_sword_8", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],




 #




 #  [0.8, "run_man_forward_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],




 
 #["run_forward_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [0.8, "anim_human", 7100, 7140, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
##   [0.8, "run_greatsword", 0, 22, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 #  [0.8, "run_forward_staff", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
# ],




#hispania 1200



 ["run_forward_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction, #musket
  
  [0.8, "run_forward_staff", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
  [0.8, "run_pike_2", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 # [0.8, "run_pike_3", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
  [0.8, "run_forward_staff", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
  [0.8, "run_forward_staff", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],




 
# ["run_forward_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [0.8, "anim_human", 7200, 7240, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
##   [0.8, "run_greatsword", 0, 22, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
#   [0.8, "run_forward_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
# ],




 #hispania 1200




 ["run_forward_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_forward_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
  [0.8, "run_pike_2", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
  [0.8, "run_pike_3", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
  [0.8, "run_pike_4", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],    
  [0.8, "run_forward_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
  [0.8, "run_forward_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
  [0.8, "run_forward_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],








 
 ["run_forward_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.8, "run_forward_hips_right", 0, 22, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.8, "run_forward_hips_left", 0, 22, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
##   [0.8, "run_normal", 0, 22, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
##   [0.8, "run_man_right", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_man_forward_right", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
##   [0.8, "run_crossright_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_man_forward_right_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_right_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
##   [0.8, "run_crossright_staff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_man_forward_right_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_right_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
##   [0.8, "run_crossright_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_man_forward_right_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.8, "run_forward_right_hips_right", 0, 22, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.8, "run_forward_right_hips_left", 0, 19, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
##   [0.8, "run_normal", 0, 22, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
##   [0.8, "run_man_left", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_man_forward_left", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
##   [0.8, "run_crossleft_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_man_forward_left_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_left_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
##   [0.8, "run_crossleft_staff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_man_forward_left_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_left_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
##   [0.8, "run_crossleft_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_man_forward_left_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.6, "run_forward_left_hips_right", 0, 19, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.8, "run_forward_left_hips_left", 0, 22, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_backward", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.7, "run_backward", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [1.0, "anim_human", 7040, 7000, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [0.7, "run_backward", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [1.0, "anim_human", 7140, 7100, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [0.7, "run_backward_staff", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [1.0, "anim_human", 7240, 7200, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [0.7, "run_backward_twohanded", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.7, "run_backward_hips_right", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.7, "run_backward_hips_left", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [1.0, "anim_human", 7040, 7000, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
##   [1.0, "run_man_forward", 24, 0, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
   [0.7, "run_backward_right", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [1.0, "anim_human", 7040, 7000, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [0.7, "run_backward_right", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_right_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [1.0, "anim_human", 7140, 7100, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [0.7, "run_backward_staff_right", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_right_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [1.0, "anim_human", 7240, 7200, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [0.7, "run_backward_twohanded_right", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.7, "run_backward_right_hips_right", 0, 19, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.7, "run_backward_right_hips_left", 0, 22, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [1.0, "anim_human", 7040, 7000, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
##   [1.0, "run_man_forward", 24, 0, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
   [0.7, "run_backward_left", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [1.0, "anim_human", 7040, 7000, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [0.7, "run_backward_left", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_left_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [1.0, "anim_human", 7140, 7100, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [0.7, "run_backward_staff_left", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_left_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [1.0, "anim_human", 7240, 7200, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [0.7, "run_backward_twohanded_left", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.7, "run_backward_left_hips_right", 0, 22, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.7, "run_backward_left_hips_left", 0, 19, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [0.8, "anim_human", 9000, 9020, arf_use_walk_progress|arf_cyclic|blend_in_walk,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
##   [0.8, "run_right_normal", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
   [0.8, "run_man_right", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["run_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [0.8, "run_right_onehanded", 0, 12, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
##   [0.8, "run_right_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
   [0.8, "run_man_right_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["run_right_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [0.8, "run_right_greatsword", 0, 12, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
##   [0.8, "run_right_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
   [0.8, "run_man_right_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["run_right_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [0.8, "run_right_staff", 0, 12, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
##   [0.8, "run_right_staff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
   [0.8, "run_man_right_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["run_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.8, "run_man_right_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["run_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.8, "run_right_hips_left", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["run_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [0.8, "anim_human", 9500, 9520, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
##   [0.8, "run_left_normal", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
   [0.8, "run_man_left", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
 ],
 ["run_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [0.8, "run_left_onehanded", 0, 12, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
   [0.8, "run_man_left_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
 ],
 ["run_left_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [0.8, "anim_human", 9500, 9520, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
#   [0.8, "run_left_greatsword", 0, 12, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
##   [0.8, "run_left_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
   [0.8, "run_man_left_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
 ],
 ["run_left_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [0.8, "run_left_staff", 0, 12, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
##   [0.8, "run_left_staff", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
   [0.8, "run_man_left_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
 ],
 ["run_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.8, "run_left_hips_right", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
 ],
 ["run_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.8, "run_man_left_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
 ],
  ["walk_forward", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [1.0, "anim_human", 6000, 6020, arf_walk,pack2f(0.4,0.9)],
   [1.0, "man_walk", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [1.0, "anim_human", 6000, 6020, arf_walk,pack2f(0.4,0.9)],
   [1.0, "man_walk", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
##   [1.0, "anim_human", 6100, 6120, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [1.0, "man_walk_staff", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
##   [1.0, "anim_human", 6200, 6220, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [1.0, "man_walk_greatsword", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_forward_hips_right", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_forward_hips_left", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
##   [1.0, "anim_human", 6020, 6000, arf_phase_odd|arf_walk,pack2f(0.4,0.9)],
##   [1.0, "anim_human", 6020, 6000, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
##   [1.0, "man_walk", 32, 0, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [1.0, "walk_backward", 0, 30, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
#   [1.0, "anim_human", 6000, 6020, arf_walk,pack2f(0.4,0.9)],
   [1.0, "man_walk", 32, 0, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
##   [1.0, "anim_human", 6120, 6100, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [1.0, "man_walk_staff", 32, 0, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
##   [1.0, "anim_human", 6220, 6200, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [1.0, "man_walk_greatsword", 32, 0, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_backward_hips_right", 0, 30, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_backward_hips_left", 0, 30, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
["walk_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_right_normal", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_right_onehanded_r", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_right_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_right_greatsword_r", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_right_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_right_staff_r", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_right_staff_r", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_right_hips_left", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_left_normal", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_left_onehanded_r", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_left_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_left_greatsword", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_left_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_left_staff", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_left_hips_right", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_left_staff", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossright_normal", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_forward_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossright_onehanded", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_forward_right_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossright_greatsword", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_forward_right_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossright_staff", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_forward_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_forward_right_hips_right", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_forward_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_forward_right_hips_left", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_forward_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossleft_normal", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossleft_onehanded", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_left_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossleft_greatsword", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_left_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossleft_staff", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_forward_left_hips_right", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_forward_left_hips_left", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossright_normal", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_backward_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossright_onehanded", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_backward_left_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossright_greatsword", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_backward_left_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossright_staff", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_backward_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_backward_left_hips_right", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_backward_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_backward_left_hips_left", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_backward_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossleft_normal", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossleft_onehanded", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_right_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossleft_greatsword", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_right_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_crossleft_staff", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_backward_right_hips_right", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [1.0, "walk_backward_right_hips_left", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ###Backup before AI Crouching begin
# ["walk_forward_crouch", acf_enforce_lowerbody, 0,
#   [1.7, "low_walk", 0, 48, arf_use_walk_progress,pack2f(0.4,0.9)],
# ],
# ["stand_to_crouch", acf_enforce_lowerbody, 0,
#   [1.3, "crouch_down", 0, 50,  arf_blend_in_1, 0, (0.0,0,0.0)],
# ],
# ["crouch_to_stand", acf_enforce_lowerbody, 0,
#   [1.0, "crouch_down", 56, 91,  arf_blend_in_1, 0, (0.0,0,0.0)],
# ],
###Backup before AI Crouching, END
###Add AI Crouching
["walk_forward_crouch", acf_enforce_lowerbody, amf_priority_continue|amf_use_cycle_period|amf_client_prediction,
   # DUNDE :
   #[1.7, "low_walk", 0, 48, arf_use_walk_progress,pack2f(0.4,0.9)],
   [1.7, "low_walk", 0, 48, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0]],
 ["stand_to_crouch", acf_enforce_lowerbody, amf_priority_continue|amf_client_prediction|amf_keep,
   [1.0, "crouch_down", 0, 81,  arf_blend_in_1, 0, (0.0,0,0.0)]],
 ["crouch_to_stand", acf_enforce_lowerbody, amf_priority_continue|amf_client_prediction|amf_play,
   [1.0, "crouch_down", 154, 185, arf_blend_in_1, 0, (0.0,0,0.0)]],
###END Add AI Crouching
 ["ride_0", acf_enforce_lowerbody, amf_client_prediction,
  ## [10.0, "anim_human", horse_move+2000, horse_move+2100, arf_cyclic],
  # [3.0, "anim_human_02", 600, 644, arf_cyclic],
##   [37.0, "stand_onhorse", 0, 1110, arf_cyclic],
##   [22.0, "stand_onhorse_sword", 0, 671, arf_cyclic],
   [15.0, "stand_onhorse", 0, 456, arf_cyclic],
  ],
 ["ride_1", acf_enforce_lowerbody | acf_synch_with_horse, amf_client_prediction,
   [1.0, "anim_human_02", 0, 31, arf_cyclic],
 ],








#hispania 1200 jinetes 

 ["lancer_ride_1", acf_enforce_lowerbody | acf_synch_with_horse, amf_client_prediction|amf_priority_ride|amf_play,

##   [0.8, "anim_human", horse_move+210, horse_move+250, arf_cyclic |  arf_blend_in_16],
   [20.0, "lancer_ride1", 0, 31, arf_cyclic],
   # [20.0, "lancer_ride1_kite", 0, 31, arf_cyclic],
   [20.0, "lancer_ride1", 0, 31, arf_cyclic],
  ],
 
 ["lancer_charge_parried",acf_enforce_lowerbody, amf_priority_parried|amf_use_weapon_speed|amf_play,
   [1.0, "anim_human", horse_move+210, horse_move+220, arf_blend_in_32],
  
 ],
 ["ride_2", acf_enforce_lowerbody | acf_synch_with_horse, amf_client_prediction,
   [20.8, "anim_human_02", 50, 69, arf_cyclic],
   # [20.0, "ride_one_handed_2", 1, 19, arf_cyclic],
   [20.8, "anim_human_02", 50, 69, arf_cyclic],
   #[20.8, "newanim_ride_2", 1, 19, arf_cyclic],
 ],
 ["ride_3", acf_enforce_lowerbody | acf_synch_with_horse, amf_client_prediction,
   [20.6, "anim_human_02", 100, 116, arf_cyclic],
  # [20.6, "newanim_ride_3", 0, 16, arf_cyclic],
   # [20.8, "ride_one_handed_3", 1, 16, arf_cyclic],
  # [20.6, "anim_human_02", 100, 116, arf_cyclic],
 #  [20.6, "ride_one_handed_5", 2, 17, arf_cyclic],
   
 ],
 ["ride_4", acf_enforce_lowerbody | acf_synch_with_horse, amf_client_prediction,
   [20.5, "anim_human_02", 150, 165, arf_cyclic|arf_blend_in_32],
 #  [20.0, "newanim_ride_4", 1, 15, arf_cyclic|arf_blend_in_32],
 #  [20.0, "ride_1", 1, 15, arf_cyclic|arf_blend_in_32],
#   [20.5, "anim_human_02", 150, 165, arf_cyclic|arf_blend_in_32],
 #  [20.0, "ride_2", 1, 15, arf_cyclic|arf_blend_in_32],
   # [20.5, "ride_one_handed_4", 1, 14, arf_cyclic|arf_blend_in_32],
   [20.5, "anim_human_02", 150, 165, arf_cyclic|arf_blend_in_32],
  # [20.5, "new_ride_4a", 0, 15, arf_cyclic|arf_blend_in_32],
   [20.5, "new_ride_4c", 0, 15, arf_cyclic|arf_blend_in_32],
  # [20.5, "anim_human_02", 150, 165, arf_cyclic|arf_blend_in_32],
  # [20.5, "new_ride_4d", 0, 15, arf_cyclic|arf_blend_in_32],
   [20.5, "new_ride_4e", 0, 15, arf_cyclic|arf_blend_in_32],
   [20.5, "anim_human_02", 150, 165, arf_cyclic|arf_blend_in_32],
 #  [2.0, "ride_4", 1, 15, arf_cyclic|arf_blend_in_32],
 ],
  
# ["lancer_ride_4",  acf_enforce_lowerbody | acf_synch_with_horse | acf_rot_vertical_sword|acf_anim_length(100), 0,
#   [0.5, "anim_human", horse_move+610, horse_move+650, arf_cyclic | arf_blend_in_128], 
# ],

 ["lancer_ride_4",  acf_enforce_lowerbody | acf_synch_with_horse | acf_rot_vertical_sword|acf_anim_length(30), amf_rider_rot_couched_lance|amf_client_prediction|amf_priority_ride|amf_play,
   [0.5, "lancer_ride4", 0, 15, arf_cyclic | arf_blend_in_128], 

 ],

#hispania 1200
 ["lancer_ride_4_no_shield",  acf_enforce_lowerbody | acf_synch_with_horse | acf_rot_vertical_sword|acf_anim_length(30), amf_use_cycle_period|amf_rider_rot_couched_lance|amf_client_prediction|amf_priority_ride|amf_play,
   [0.5, "lancer_ride4_no_shield", 0, 15, arf_cyclic | arf_blend_in_128], 

   [0.5, "lancer_ride4_no_shield_1", 0, 15, arf_cyclic | arf_blend_in_128], 
   [0.5, "lancer_ride4_no_shield_2", 0, 15, arf_cyclic | arf_blend_in_128], 
 ],

 
 ["ride_rear", acf_enforce_lowerbody|acf_ignore_slope, amf_priority_mount|amf_play|amf_client_prediction,
##   [1.4, "anim_human", horse_move+820, horse_move+837,  arf_blend_in_16],
##   [2.4, "anim_human", horse_move+820, horse_move+837,  arf_blend_in_16],
   [1.7, "anim_human_02", 265, 297,  arf_blend_in_8],
 ],
 ["ride_spur", acf_enforce_lowerbody, amf_play|amf_priority_jump,
   [0.3, "anim_human", horse_move+860, horse_move+865,  arf_blend_in_8],
 ],
 ["ride_jump", acf_enforce_lowerbody, amf_client_prediction,
## [1.6, "anim_human_02", 400, 420,  arf_blend_in_16],
   [1.6, "anim_human_02", 205, 222,  arf_blend_in_4],#|arf_end_pos_0_25],
 ],
 ["ride_jump_end", acf_enforce_all, amf_client_prediction,
## [0.1, "anim_human", horse_move+935, horse_move+940,  arf_blend_in_16], 
## [0.3, "anim_human_02", 420, 424,  arf_blend_in_16],
   [0.1, "anim_human_02", 222, 224,  arf_blend_in_16],
 ],
 ["ride_turn_right", acf_enforce_lowerbody | acf_synch_with_horse, amf_client_prediction,
   [1.0, "anim_human_02", 500, 533, arf_cyclic],
 ],
 ["ride_turn_left", acf_enforce_lowerbody | acf_synch_with_horse, amf_client_prediction,
   [1.0, "anim_human_02", 450, 483, arf_cyclic], 
 ],
 
 ["mount_horse", acf_enforce_all, amf_priority_mount|amf_play|amf_client_prediction,


   [1.3, "anim_human", horse_move+1003, horse_move+1045,  arf_blend_in_1, 0, (0.0,0,0.0)],
 ],
 ["dismount_horse", acf_enforce_lowerbody|acf_displace_position, amf_priority_mount|amf_play|amf_accurate_body|amf_client_prediction,
   [1.1, "anim_human", horse_move+1103, horse_move+1145,  arf_blend_in_1, 0, (-0.5,0,0)],
 ],
 ["lancer_ride_0", acf_enforce_lowerbody, amf_priority_ride|amf_play|amf_client_prediction,
##   [4.0, "anim_human", horse_move + 5000, horse_move + 5057, arf_lancer|arf_cyclic],
   [43.0, "stand_onhorse_staff", 0, 1300, arf_lancer|arf_cyclic],
 ],
 ["equip_default", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.6, "equip_arms", 206, 221, arf_blend_in_0],
 ],
 ["unequip_default", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "equip_arms", 207, 200, arf_blend_in_0],
 ],
 ["equip_sword", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.8, "equip_sword", 0, 27, arf_blend_in_0],
 ],
 ["unequip_sword", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "equip_sword", 6, 0, arf_blend_in_0],
 ],
 ["equip_greatsword", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [1.2, "draw_greatsword", 0, 35, arf_blend_in_0],
 ],
 ["unequip_greatsword", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "draw_greatsword", 10, 0, arf_blend_in_0],
 ],
 ["equip_axe_left_hip", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.8, "draw_axe", 0, 16, arf_blend_in_0],
 ],
 ["unequip_axe_left_hip", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "draw_axe", 6, 0, arf_blend_in_0],
 ],
 ["equip_crossbow", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [1.2, "equip_greataxe", 0, 20, arf_blend_in_0],
 ],
 ["unequip_crossbow", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "equip_greataxe", 10, 0, arf_blend_in_0],
 ],
 ["equip_spear", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.8, "equip_arms", 17, 34, arf_blend_in_0],
 ],
 ["unequip_spear", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "equip_arms", 15, 10, arf_blend_in_0],
 ],
 ["equip_dagger_front_left", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.8, "equip_arms", 253, 276, arf_blend_in_0],
 ],
 ["unequip_dagger_front_left", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.2, "equip_arms", 254, 250, arf_blend_in_0],
 ],
 ["equip_dagger_front_right", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.8, "equip_arms", 305, 333, arf_blend_in_0],
 ],
 ["unequip_dagger_front_right", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.4, "equip_arms", 306, 300, arf_blend_in_0],
 ],
 ["equip_axe_back", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [1.0, "equip_greataxe", 0, 17, arf_blend_in_0],
 ],
 ["unequip_axe_back", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "equip_greataxe", 7, 0, arf_blend_in_0],
 ],
 ["equip_revolver_right", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.6, "equip_arms", 352, 365, arf_blend_in_0],
 ],
 ["unequip_revolver_right", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "equip_arms", 354, 350, arf_blend_in_0],
 ],
 ["equip_pistol_front_left", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
##   [0.6, "anim_human", combat+30, combat+45, arf_blend_in_0],
   [0.8, "equip_arms", 253, 276, arf_blend_in_0],
 ],
 ["unequip_pistol_front_left", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
##   [0.3, "anim_human", combat+10, combat+0, arf_blend_in_0],
   [0.2, "equip_arms", 254, 250, arf_blend_in_0],
 ],
 ["equip_katana", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.8, "anim_human", combat+30, combat+45, arf_blend_in_0],
 ],
 ["unequip_katana", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "anim_human", combat+10, combat+0, arf_blend_in_0],
 ],
 ["equip_wakizashi", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.8, "anim_human", combat+30, combat+45, arf_blend_in_0],
 ],
 ["unequip_wakizashi", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "anim_human", combat+10, combat+0, arf_blend_in_0],
 ],
 ["equip_shield", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.8, "equip_arms", 68, 84, arf_blend_in_0],
 ],
 ["unequip_shield", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.4, "equip_arms", 62, 50, arf_blend_in_0],
 ],
 ["equip_bow_back", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.7, "equip_arms", 161, 179, arf_blend_in_0],
 ],
 ["unequip_bow_back", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "equip_arms", 163, 150, arf_blend_in_0],
 ],
 ["equip_bow_left_hip", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.7, "equip_arms", 110, 148, arf_blend_in_0],
 ],
 ["unequip_bow_left_hip", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "equip_arms", 115, 108, arf_blend_in_0],
 ],
 ["cancel_attack_onehanded", 0, amf_priority_cancel|amf_use_weapon_speed|amf_use_inertia|amf_play|amf_rider_rot_thrust,
   [cancel_duration, "sword_loop01", 10, 11, arf_blend_in_8],
 ],
 ["cancel_attack_twohanded", 0, amf_priority_cancel|amf_use_weapon_speed|amf_use_inertia|amf_play|amf_rider_rot_thrust,
   [cancel_duration, "greatsword_cstance", 10, 11, arf_blend_in_8],
 ],
 ["cancel_attack_polearm", 0, amf_priority_cancel|amf_use_weapon_speed|amf_use_inertia|amf_play|amf_rider_rot_thrust,
   [cancel_duration, "staff_cstance", 10, 11, arf_blend_in_8],
 ],
#TODO: ready bow, release javelin and reload crossbow should have the same time 
# duration and controlled via weapon speed.
 ["ready_bow", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_bow,
   [1.5, "anim_human", combat+500, combat+530, blend_in_ready|arf_make_custom_sound, pack2f(0.14, 0.44)],
   [1.5, "anim_archery", 16, 133, blend_in_ready|arf_make_custom_sound, pack2f(0.14, 0.44)],
 ],
 ["release_bow", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_bow,
   [0.3, "anim_human", combat+530, combat+532, arf_blend_in_2],
   [0.3, "anim_archery", 133, 174, arf_blend_in_2],
 ],
 #not used
 ["ready_bow_mounted", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_bow,
   [1.5, "anim_human", combat+800, combat+830, blend_in_ready|arf_make_custom_sound, pack2f(0.10, 0.40)],
 ],
 #not used
 ["release_bow_mounted", acf_rot_vertical_bow|acf_anim_length(100), amf_rider_rot_bow,
   [0.3, "anim_human", combat+830, combat+832, arf_blend_in_2],
 ],
 ["ready_crossbow", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_crossbow,
   [1.5, "anim_human", combat+1300, combat+1320, blend_in_ready],
 ],
 ["release_crossbow", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_crossbow,
   [0.2, "anim_human", combat+1330, combat+1331, arf_blend_in_1],
 ],
  ["reload_crossbow", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
    [1, "anim_human", 21700, 21750, arf_blend_in_8|arf_make_custom_sound, pack2f(0.94, 0.4), (0, 0, 0), 0],
    [1.5, "crossbow_reload_pavise", 0, 158, arf_blend_in_8|arf_make_custom_sound, pack2f(0.94, 0.4), (0, 0, 0), 0],
  ],
 ["reload_crossbow_horseback", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
   [1.6, "anim_human", combat+1800, combat+1877, arf_blend_in_8|arf_make_custom_sound, pack2f(0.27, 0.94)], 
 ],
 ["ready_javelin", acf_rot_vertical_bow, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_throw,
   [0.6, "throw_javelin2", 0, 30, blend_in_ready],
 ],
 ["release_javelin", acf_rot_vertical_bow, amf_priority_throw|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_throw,
   [0.9, "throw_javelin2", 55, 100, arf_blend_in_0],
 ],
 ["ready_throwing_knife", acf_rot_vertical_bow, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_throw,
   [0.6, "throw_knife", 10, 30, blend_in_ready],
 ],
 ["release_throwing_knife", acf_rot_vertical_bow, amf_priority_throw|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_throw,
   [0.9, "throw_knife", 30, 70, arf_blend_in_0],
 ],
 ["ready_throwing_axe", acf_rot_vertical_bow, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_throw,
##   [0.3, "throw_axe", 0, 40, blend_in_ready],
   [0.6, "throwing_axe", 7, 23, blend_in_ready],
 ],
 ["release_throwing_axe", acf_rot_vertical_bow, amf_priority_throw|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_throw,
##   [0.9, "throw_axe", 40, 90, arf_blend_in_0],
   [0.9, "throwing_axe", 23, 60, arf_blend_in_0],
 ],
 ["ready_stone", acf_rot_vertical_bow, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_throw,
####   [0.3, "anim_human", combat+2200, combat+2210, blend_in_ready],
##   [0.7, "throw_stone", 0, 21, blend_in_ready],
   [0.6, "throwing_stone", 0, 20, blend_in_ready],
 ],
 ["release_stone", acf_rot_vertical_bow, amf_priority_throw|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_throw,
####   [1.0, "anim_human", combat+2210, combat+2225, arf_blend_in_0],
##   [1.0, "throw_stone", 21, 54, arf_blend_in_0],
   [0.9, "throwing_stone", 20, 65, arf_blend_in_0],
 ],
 ["ready_pistol", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_pistol,
   [0.3, "anim_human", combat+2500, combat+2515, arf_blend_in_8],
 ],
 ["release_pistol", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_pistol,
   [0.3, "anim_human", combat+2520, combat+2527, arf_blend_in_1],
 ],
 ["reload_pistol", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
   [2.0, "anim_human", combat+2650, combat+2860, arf_blend_in_8],
 ],
 ["ready_musket", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_crossbow,
   [1.5, "anim_human", combat+1300, combat+1320, blend_in_ready],
 ],
 ["release_musket", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_crossbow,
   [0.2, "anim_human", combat+1330, combat+1331, arf_blend_in_1],
 ],
 ["reload_musket", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
   [2.0, "anim_human", combat+2650, combat+2860, arf_blend_in_8],
 ],








 ["ready_swingright_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_swing_right,
   [ready_durn, "right_swing", 0, 15, blend_in_ready], 
 ],
 ["release_swingright_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right,
   [0.5, "right_swing", 15, 41, blend_in_release], 
 ],
 ["release_swingright_fist_continue", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right,
   [0.5, "right_swing", 15, 41, blend_in_release], 
 ],
 ["blocked_swingright_fist", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right,
   [attack_blocked_duration, "anim_human", combat+4013, combat+4008, blend_in_parry], 
 ],
 ["parried_swingright_fist", 0, amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right,
   [attack_parried_duration, "anim_human", combat+4013, combat+4008, blend_in_parry], 
 ],



 ["ready_swingleft_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_swing_left,
   [ready_durn, "anim_human", combat+4300, combat+4300, blend_in_ready], 
 ],
 ["release_swingleft_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left,
   [0.5, "anim_human", combat+4300, combat+4335, blend_in_release], 
 ],
 ["release_swingleft_fist_continue", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left,
   [0.5, "anim_human", combat+4300, combat+4335, blend_in_release], 
 ],
 ["blocked_swingleft_fist", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left,
   [attack_blocked_duration, "anim_human", combat+4313, combat+4308, blend_in_parry], 
 ],
 ["parried_swingleft_fist", 0, amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left,
   [attack_parried_duration, "anim_human", combat+4313, combat+4308, blend_in_parry], 
 ],








 ["ready_direct_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_thrust,
   [ready_durn, "direct_fist", 0, 16, blend_in_ready], 
 ],
 ["release_direct_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
   [0.5, "direct_fist", 17, 36, blend_in_release], 
 ],
 ["release_direct_fist_continue", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
   [0.5, "direct_fist", 17, 36, blend_in_release], 
 ],
 ["blocked_direct_fist", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
   [attack_blocked_duration, "anim_human", combat+4613, combat+4608, blend_in_parry], 
 ],
 ["parried_direct_fist", 0, amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
   [attack_parried_duration, "anim_human", combat+4613, combat+4608, blend_in_parry], 
 ],
 ["ready_uppercut_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_thrust,
   [ready_durn, "uppercut", 0, 17, blend_in_ready], 
 ],
 ["release_uppercut_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
   [0.5, "uppercut", 17, 34, blend_in_release], 
 ],
 ["release_uppercut_fist_continue", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
   [0.5, "uppercut", 17, 34, blend_in_release], 
 ],
 ["blocked_uppercut_fist", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
   [attack_blocked_duration, "anim_human", combat+4913, combat+4908, blend_in_parry], 
 ],
 ["parried_uppercut_fist", 0, amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
   [attack_parried_duration, "anim_human", combat+4913, combat+4908, blend_in_parry], 
 ],




 ["ready_slashright_twohanded", acf_right_cut|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
##   [ready_durn, "anim_human", combat+5700, combat+5710, blend_in_ready], 
##   [ready_durn, "slashright_twohanded", 5, 20, blend_in_ready], 
##   [ready_durn, "slashright_twohanded", 10, 16, blend_in_ready], 
   [ready_durn, "slashright_twohanded", 10, 18, blend_in_ready], 
 ],
 ["release_slashright_twohanded", acf_right_cut|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
##   [0.62, "anim_human", combat+5710, combat+5740, blend_in_release], 
##   [0.62, "slashright_twohanded", 20, 51, blend_in_release], 
##   [0.62, "slashright_twohanded", 16, 40, blend_in_release], 
   [0.61, "slashright_twohanded", 18, 38, blend_in_release], 
 ],
 ["release_slashright_twohanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
##   [0.3, "slashright_twohanded", 45, 61, blend_in_continue], 
   [0.5, "slashright_twohanded", 38, 61, blend_in_continue], 
 ],
 ["blocked_slashright_twohanded",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_blocked|amf_use_weapon_speed|amf_play,
   [attack_blocked_duration, "anim_human", combat+5725, combat+5720, blend_in_parry], 
 ],
 ["parried_slashright_twohanded",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_parried|amf_use_weapon_speed|amf_play,
   [attack_parried_duration, "anim_human", combat+5725, combat+5720, blend_in_parry], 
 ],
 ["ready_slashleft_twohanded", acf_right_cut|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
   [ready_durn, "slashleft_twohanded", 12, 16, blend_in_ready], 
 ],
 ["release_slashleft_twohanded", acf_right_cut|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
   [0.61, "slashleft_twohanded", 16, 38, blend_in_release], 
 ],
 ["release_slashleft_twohanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
   [0.5, "slashleft_twohanded", 38, 52, blend_in_continue], 
 ],
 ["blocked_slashleft_twohanded",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_blocked|amf_use_weapon_speed|amf_play,
   [attack_blocked_duration, "anim_human", combat+6425, combat+6420, blend_in_parry], 
 ],
 ["parried_slashleft_twohanded",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_parried|amf_use_weapon_speed|amf_play,
   [attack_parried_duration, "anim_human", combat+6425, combat+6420, blend_in_parry], 
 ],
 ["ready_thrust_twohanded", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
   [ready_durn, "anim_human", combat+6000, combat+6010, blend_in_ready], 
 ],
 ["release_thrust_twohanded", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
   [0.61, "anim_human", combat+6010, combat+6031, blend_in_release], 
 ],
 ["release_thrust_twohanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
   [0.1, "anim_human", combat+6031, combat+6040, blend_in_continue], 
 ],
 ["blocked_thrust_twohanded", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play,
   [attack_blocked_duration_thrust, "anim_human", combat+6015, combat+6016, blend_in_parry], 
 ],
 ["parried_thrust_twohanded", 0, amf_priority_parried|amf_use_weapon_speed|amf_play,
   [attack_parried_duration_thrust, "anim_human", combat+6015, combat+6016, blend_in_parry], 
 ],
 ["ready_overswing_twohanded", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
   [ready_durn, "attacks_twohanded_overswing", 11, 26, blend_in_ready],
 ],
 ["release_overswing_twohanded", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
   [0.61, "attacks_twohanded_overswing", 26, 55, blend_in_release],
 ],
 ["release_overswing_twohanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
   [0.5, "attacks_twohanded_overswing", 55, 66, blend_in_continue],
 ],
 ["blocked_overswing_twohanded", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play,
   [attack_blocked_duration, "anim_human", combat+6215, combat+6212, blend_in_parry], 
 ],
 ["parried_overswing_twohanded", 0, amf_priority_parried|amf_use_weapon_speed|amf_play,
   [attack_parried_duration, "anim_human", combat+6215, combat+6212, blend_in_parry], 
 ],
 ["ready_thrust_onehanded",   acf_thrust|acf_rot_vertical_sword|acf_anim_length(100)|acf_enforce_rightside, amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction|amf_rider_rot_thrust,
##   [ready_durn, "anim_human", combat+8500, combat+8510, blend_in_ready], 
   [ready_durn, "attacks_thrust_onehanded", 5, 13, blend_in_ready], 
 ],
 ["release_thrust_onehanded", acf_thrust|acf_rot_vertical_sword|acf_anim_length(100)|acf_enforce_rightside, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust|amf_continue_to_next,
##   [0.61, "anim_human", combat+8510, combat+8540, blend_in_release], 
   [0.62, "attacks_thrust_onehanded", 12, 32, blend_in_release], 
 ],
 ["release_thrust_onehanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust|amf_client_owner_prediction,
   [0.3, "attacks_thrust_onehanded", 32, 54, blend_in_continue], 
 ],
 ["blocked_thrust_onehanded", acf_enforce_rightside, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
   [attack_blocked_duration_thrust, "anim_human", combat+8515, combat+8513, blend_in_parry], 
 ],
 ["parried_thrust_onehanded", acf_enforce_rightside, amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
   [attack_parried_duration_thrust, "anim_human", combat+8515, combat+8513, blend_in_parry], 
 ],
  ["ready_thrust_onehanded_horseback",   acf_thrust|acf_rot_vertical_sword|acf_anim_length(100)|acf_enforce_rightside, amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction|amf_rider_rot_thrust,
##   [ready_durn, "anim_human", combat+8500, combat+8510, blend_in_ready], 
##   [ready_durn, "attacks_thrust_onehanded", 0, 16, blend_in_ready], 
   [ready_durn, "attacks_thrust_onehanded", 5, 13, blend_in_ready], 
 ],
 ["release_thrust_onehanded_horseback", acf_thrust|acf_rot_vertical_sword|acf_anim_length(100)|acf_enforce_rightside, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust|amf_continue_to_next,
##   [0.61, "anim_human", combat+8510, combat+8540, blend_in_release], 
##   [0.9, "attacks_thrust_onehanded", 16, 54, blend_in_release], 
   [0.62, "attacks_thrust_onehanded", 12, 32, blend_in_release], 
 ],
 ["release_thrust_onehanded_horseback_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust|amf_client_owner_prediction,
##   [0.1, "attacks_thrust_onehanded", 54, 54, blend_in_continue], 
   [0.3, "attacks_thrust_onehanded", 32, 54, blend_in_continue], 
 ],
 ["blocked_thrust_onehanded_horseback", acf_enforce_rightside, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
   [attack_blocked_duration_thrust, "anim_human", combat+8515, combat+8513, blend_in_parry], 
 ],
 ["parried_thrust_onehanded_horseback", acf_enforce_rightside, amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
   [attack_parried_duration_thrust, "anim_human", combat+8515, combat+8513, blend_in_parry], 
 ],




 ["ready_thrust_onehanded_lance",   acf_thrust|acf_rot_vertical_sword|acf_anim_length(100)|acf_enforce_rightside, amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction|amf_rider_rot_thrust,
##   [ready_durn, "anim_human", combat+9500, combat+9508, blend_in_ready], 
   [ready_durn, "thrust_onehanded_lance_hb", 5, 8, blend_in_ready], 
 ],
 ["release_thrust_onehanded_lance", acf_thrust|acf_rot_vertical_sword|acf_anim_length(100)|acf_enforce_rightside, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust|amf_continue_to_next,
##   [0.62, "anim_human", combat+9507, combat+9530, blend_in_release], 
   [0.62, "thrust_onehanded_lance_hb", 8, 33, blend_in_release], 
 ],
 ["release_thrust_onehanded_lance_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust|amf_client_owner_prediction,
##   [0.1, "anim_human", combat+9530, combat+9540, blend_in_continue], 
   [0.1, "thrust_onehanded_lance_hb", 33, 45, blend_in_continue], 
 ],
 ["blocked_thrust_onehanded_lance", acf_enforce_rightside, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
   [attack_blocked_duration_thrust, "anim_human", combat+9515, combat+9513, blend_in_parry], 
 ],
 ["parried_thrust_onehanded_lance", acf_enforce_rightside, amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
   [attack_parried_duration_thrust, "anim_human", combat+9515, combat+9513, blend_in_parry], 
 ],
 ["ready_slashright_onehanded", acf_right_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
####   [ready_durn, "anim_human", combat+8800, combat+8810, blend_in_ready], 
##   [ready_durn, "attacks_single_righttoleft", 8, 16, blend_in_ready], 
##   [ready_durn, "attacks_single_righttoleft", 5, 10, blend_in_ready], 
   [ready_durn, "attacks_single_righttoleft", 2, 5, blend_in_ready], 
 ],
 ["release_slashright_onehanded", acf_right_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
####   [0.6, "anim_human", combat+8810, combat+8840, blend_in_release], 
##   [0.6, "attacks_single_righttoleft", 16, 37, blend_in_release], 
##   [0.6, "attacks_single_righttoleft", 10, 26, blend_in_release], 
   [0.6, "attacks_single_righttoleft", 5, 28, blend_in_release], 
 ],
 ["release_slashright_onehanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
##   [0.4, "attacks_single_righttoleft", 37, 49, blend_in_continue], 
##   [0.4, "attacks_single_righttoleft", 26, 43, blend_in_continue], 
   [0.4, "attacks_single_righttoleft", 28, 44, blend_in_continue], 
 ],
 ["blocked_slashright_onehanded", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play,
##   [attack_parried_duration, "anim_human", combat+8820, combat+8815, blend_in_parry], 
   [attack_blocked_duration, "parry_single_righttoleft", 0, 14, blend_in_parry], 
 ],
 ["parried_slashright_onehanded", 0, amf_priority_parried|amf_use_weapon_speed|amf_play,
##   [attack_parried_duration, "anim_human", combat+8820, combat+8815, blend_in_parry], 
   [attack_parried_duration, "parry_single_righttoleft", 0, 14, blend_in_parry], 
 ],
## ["ready_slashright_onehanded", acf_left_cut|acf_rot_vertical|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction,
##   [ready_durn, "attacks_single", 200, 220, blend_in_ready], 
## ],
## ["release_slashright_onehanded", acf_left_cut|acf_rot_vertical|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play,
##   [0.6, "attacks_single", 220, 245, blend_in_release], 
## ],
## ["parry_slashright_onehanded", 0, amf_priority_parried|acf_rot_vertical|amf_use_weapon_speed|amf_play,
##   [attack_parried_duration, "attacks_single", 230, 225, blend_in_parry], 
## ],




 ["ready_slashleft_onehanded", acf_left_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
##   [ready_durn, "anim_human", combat+9100, combat+9110, blend_in_ready], 
##   [ready_durn, "attacks_single_lefttoright", 9, 19, blend_in_ready], 
##   [ready_durn, "attacks_single_lefttoright", 12, 21, blend_in_ready], 
   [ready_durn, "attacks_single_lefttoright", 4, 11, blend_in_ready], 
 ],
 ["release_slashleft_onehanded", acf_left_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
##   [0.6, "anim_human", combat+9110, combat+9140, blend_in_release], 
##   [0.61, "attacks_single_lefttoright", 19, 43, blend_in_release], 
##   [0.61, "attacks_single_lefttoright", 21, 40, blend_in_release], 
   [0.61, "attacks_single_lefttoright", 11, 29, blend_in_release], 
 ],
 ["release_slashleft_onehanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
##   [0.4, "attacks_single_lefttoright", 43, 56, blend_in_continue],
##   [0.4, "attacks_single_lefttoright", 40, 50, blend_in_continue],
   [0.4, "attacks_single_lefttoright", 29, 43, blend_in_continue],
 ],
 ["blocked_slashleft_onehanded", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play,
##   [attack_blocked_duration, "anim_human", combat+9120, combat+9115, blend_in_parry], 
   [attack_blocked_duration, "parry_single_lefttoright", 0, 75, blend_in_parry], 
 ],
 ["parried_slashleft_onehanded", 0, amf_priority_parried|amf_use_weapon_speed|amf_play,
##   [attack_parried_duration, "anim_human", combat+9120, combat+9115, blend_in_parry], 
   [attack_parried_duration, "parry_single_lefttoright", 0, 75, blend_in_parry], 
 ],
 ["ready_overswing_onehanded", acf_overswing|acf_enforce_rightside, amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction|amf_rider_rot_overswing,
##   [ready_durn, "anim_human", combat+9300, combat+9305, blend_in_ready], 
##   [ready_durn, "attacks_single_overswing", 2, 16, blend_in_ready], 
   [ready_durn, "attacks_single_overswing", 5, 16, blend_in_ready], 
 ],
 ["release_overswing_onehanded", acf_overswing|acf_enforce_rightside, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_overswing|amf_continue_to_next,
##   [0.6, "anim_human", combat+9305, combat+9342, blend_in_release], 
##   [0.6, "attacks_single_overswing", 16, 35, blend_in_release], 
   [0.6, "attacks_single_overswing", 16, 37, blend_in_release], 
 ],
 ["release_overswing_onehanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_rider_rot_overswing|amf_client_owner_prediction,
   [0.2, "attacks_single_overswing", 37, 40, blend_in_continue],
 ],
 ["blocked_overswing_onehanded", acf_enforce_rightside, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_overswing,
   [attack_blocked_duration, "anim_human", combat+9315, combat+9310, blend_in_parry], 
 ],
 ["parried_overswing_onehanded", acf_enforce_rightside, amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_overswing,
   [attack_parried_duration, "anim_human", combat+9315, combat+9310, blend_in_parry], 
 ],
 ["ready_slash_horseback_right", acf_right_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction|amf_rider_rot_swing_right,
##   [ready_durn, "anim_human", combat+10100, combat+10110, blend_in_ready], 
##   [ready_durn, "single_r_l_horse", 100, 112, blend_in_ready], 
##   [ready_durn, "attacks_single_righttoleft_horseback", 8, 16, blend_in_ready], 
   [ready_durn, "attacks_single_righttoleft_horseback", 8, 17, blend_in_ready], 
 ],
 ["release_slash_horseback_right", acf_right_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right|amf_continue_to_next,
##   [0.6, "anim_human", combat+10110, combat+10140, blend_in_release], 
#   [1.0, "single_r_l_horse", 112, 144, blend_in_release], 
##   [0.6, "attacks_single_righttoleft_horseback", 16, 38, blend_in_release], 
   [0.7, "attacks_single_righttoleft_horseback", 17, 39, blend_in_release], 
  ],
 ["release_slash_horseback_right_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right|amf_client_owner_prediction,
   [0.4, "attacks_single_righttoleft_horseback", 39, 54, blend_in_continue],
  ],
 ["blocked_slash_horseback_right",acf_rot_vertical_sword|acf_anim_length(100), amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right,
#   [attack_blocked_duration, "anim_human", combat+10120, combat+10115, blend_in_parry], 
   [attack_blocked_duration, "parry_single_righttoleft", 0, 14, blend_in_parry], 
 ],
 ["parried_slash_horseback_right",acf_rot_vertical_sword|acf_anim_length(100), amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right,
#   [attack_parried_duration, "anim_human", combat+10120, combat+10115, blend_in_parry], 
   [attack_parried_duration, "parry_single_righttoleft", 0, 14, blend_in_parry], 
 ],
 ["ready_slash_horseback_left", acf_left_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction|amf_rider_rot_swing_left,
#   [ready_durn, "anim_human", combat+10400, combat+10410, blend_in_ready], 
#   [ready_durn, "anim_human", combat+9100, combat+9110, blend_in_ready], 
   [ready_durn, "attacks_single_lefttoright_horseback", 7, 21, blend_in_ready], 
 ],
 ["release_slash_horseback_left", acf_left_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left|amf_continue_to_next,
#   [0.6, "anim_human", combat+10410, combat+10440, blend_in_release], 
#   [0.6, "anim_human", combat+9110, combat+9140, blend_in_release], 
   [0.7, "attacks_single_lefttoright_horseback", 21, 43, blend_in_release], 
 ],
 ["release_slash_horseback_left_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left|amf_client_owner_prediction,
   [0.3, "attacks_single_lefttoright_horseback", 43, 51, blend_in_continue],
 ],
 ["blocked_slash_horseback_left",acf_rot_vertical_sword|acf_anim_length(100), amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left,
#   [attack_blocked_duration, "anim_human", combat+10420, combat+10415, blend_in_parry], 
   [attack_blocked_duration, "parry_single_lefttoright", 0, 75, blend_in_parry], 
 ],
 ["parried_slash_horseback_left",acf_rot_vertical_sword|acf_anim_length(100), amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left,
#   [attack_parried_duration, "anim_human", combat+10420, combat+10415, blend_in_parry], 
   [attack_parried_duration, "parry_single_lefttoright", 0, 75, blend_in_parry], 
 ],




["ready_slash_horseback_polearm_right", acf_right_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction|amf_rider_rot_swing_right,
   [ready_durn, "attacks_staff_righttoleft", 6, 16, blend_in_ready], 
 ],
 ["release_slash_horseback_polearm_right", acf_right_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right|amf_continue_to_next,
   [0.7, "attacks_staff_righttoleft", 16, 40, blend_in_release], 
  ],
 ["release_slash_horseback_polearm_right_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right|amf_client_owner_prediction,
   [0.4, "attacks_staff_righttoleft", 40, 48, blend_in_continue],
  ],
 ["blocked_slash_horseback_polearm_right",acf_rot_vertical_sword|acf_anim_length(100), amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right,
   [attack_blocked_duration, "anim_human", combat+7915, combat+7913, arf_blend_in_2], 
 ],
 ["parried_slash_horseback_polearm_right",acf_rot_vertical_sword|acf_anim_length(100), amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right,
   [attack_blocked_duration, "anim_human", combat+7915, combat+7913, arf_blend_in_2], 
 ],
 ["ready_slash_horseback_polearm_left", acf_left_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction|amf_rider_rot_swing_left,
   [ready_durn, "attacks_staff_lefttoright", 10, 16, blend_in_ready], 
 ],
 ["release_slash_horseback_polearm_left", acf_left_cut|acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left|amf_continue_to_next,
   [0.7, "attacks_staff_lefttoright", 16, 41, blend_in_release], 
 ],
 ["release_slash_horseback_polearm_left_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left|amf_client_owner_prediction,
   [0.3, "attacks_staff_lefttoright", 41, 55, blend_in_continue],
 ],
 ["blocked_slash_horseback_polearm_left",acf_rot_vertical_sword|acf_anim_length(100), amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left,
   [attack_blocked_duration, "anim_human", combat+7615, combat+7613, arf_blend_in_2], 
 ],
 ["parried_slash_horseback_polearm_left",acf_rot_vertical_sword|acf_anim_length(100), amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left,
   [attack_blocked_duration, "anim_human", combat+7615, combat+7613, arf_blend_in_2], 
 ],

 ["ready_overswing_staff", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
  [ready_durn, "attacks_staff_uptodown", 9, 26, blend_in_ready],
 ],
 ["release_overswing_staff", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
  [0.6, "attacks_staff_uptodown", 26, 61, blend_in_release],
 ],
 ["release_overswing_staff_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,


  [0.3, "attacks_staff_uptodown", 61, 68, blend_in_continue],
 ],
 ["blocked_overswing_staff", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play,
   [attack_blocked_duration, "anim_human", combat+7017, combat+7014, arf_blend_in_2], 
 ],
 ["parried_overswing_staff", 0, amf_priority_parried|amf_use_weapon_speed|amf_play,
   [attack_parried_duration, "anim_human", combat+7017, combat+7014, arf_blend_in_2], 
 ],
 ["ready_thrust_staff", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
   [ready_durn, "attacks_staff_thrust", 14, 21, blend_in_ready],
 ],
 ["release_thrust_staff", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play,
   [0.6, "attacks_staff_thrust", 21, 40, blend_in_release], 
 ],
 ["release_thrust_staff_continue", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
   [0.6, "attacks_staff_thrust", 40, 58, blend_in_release], 
 ],
 ["blocked_thrust_staff", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_blocked|amf_use_weapon_speed|amf_play,
   [attack_blocked_duration_thrust, "anim_human", combat+7316, combat+7313, arf_blend_in_2], 
#   [attack_blocked_duration, "thrust_staff", 102, 97, arf_blend_in_2], 
 ],
 ["parried_thrust_staff", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_parried|amf_use_weapon_speed|amf_play,
   [attack_parried_duration_thrust, "anim_human", combat+7316, combat+7313, arf_blend_in_2], 
#   [attack_parried_duration, "thrust_staff", 102, 97, arf_blend_in_2], 
 ],
##                            
## ["ready_overswing_staff_overhead", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
##   [ready_durn, "attacks_staff_thrust_overhead", 6, 21, blend_in_ready], 
## ],
## ["release_overswing_staff_overhead", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
##   [0.6, "attacks_staff_thrust_overhead", 21, 43, blend_in_release], 
## ],
## ["release_overswing_staff_overhead_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
##   [0.3, "attacks_staff_thrust_overhead", 43, 50, blend_in_continue],
## ],
## ["blocked_overswing_staff_overhead", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play,
##   [attack_blocked_duration, "anim_human", combat+7017, combat+7014, arf_blend_in_2], 
## ],
## ["parried_overswing_staff_overhead", 0, amf_priority_parried|amf_use_weapon_speed|amf_play,
##   [attack_parried_duration, "anim_human", combat+7017, combat+7014, arf_blend_in_2], 
## ],
## ["ready_thrust_staff_overhead", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
##   [ready_durn, "javelin_thrust_overhead", 14, 30, blend_in_ready],
## ],
## ["release_thrust_staff_overhead", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play,
##   [0.6, "javelin_thrust_overhead", 55, 78, blend_in_release], 
## ],
## ["release_thrust_staff_overhead_continue", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
##   [0.6, "javelin_thrust_overhead", 78, 95, blend_in_release], 
## ],
## ["blocked_thrust_staff_overhead", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_blocked|amf_use_weapon_speed|amf_play,
##   [attack_blocked_duration_thrust, "anim_human", combat+7316, combat+7313, arf_blend_in_2], 
## ],
## ["parried_thrust_staff_overhead", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_parried|amf_use_weapon_speed|amf_play,
##   [attack_parried_duration_thrust, "anim_human", combat+7316, combat+7313, arf_blend_in_2], 
## ],

 ["ready_slashleft_staff",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,


##   [ready_durn, "anim_human", combat+7600, combat+7610, blend_in_ready], 
##   [ready_durn, "attacks_staff_lefttoright", 6, 20, blend_in_ready], 
   [ready_durn, "attacks_staff_lefttoright", 10, 16, blend_in_ready], 
 ],
 ["release_slashleft_staff",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
##   [0.6, "anim_human", combat+7610, combat+7640, arf_blend_in_0], 
##   [0.6, "attacks_staff_lefttoright", 20, 48, arf_blend_in_0], 
   [0.6, "attacks_staff_lefttoright", 16, 44, blend_in_release], 
 ],
 ["release_slashleft_staff_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
   [0.3, "attacks_staff_lefttoright", 44, 55, blend_in_continue], 
 ],
 ["blocked_slashleft_staff",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_blocked|amf_use_weapon_speed|amf_play,
   [attack_blocked_duration, "anim_human", combat+7615, combat+7613, arf_blend_in_2], 
 ],
 ["parried_slashleft_staff",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_parried|amf_use_weapon_speed|amf_play,
   [attack_parried_duration, "anim_human", combat+7615, combat+7613, arf_blend_in_2], 
 ],
 ["ready_slashright_staff",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
##   [ready_durn, "anim_human", combat+7900, combat+7910, blend_in_ready], 
##   [ready_durn, "attacks_staff_righttoleft", 3, 18, blend_in_ready], 
   [ready_durn, "attacks_staff_righttoleft", 6, 16, blend_in_ready], 
 ],
 ["release_slashright_staff",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
##   [0.6, "anim_human", combat+7910, combat+7940, arf_blend_in_0], 
##   [0.6, "attacks_staff_righttoleft", 18, 48, arf_blend_in_0], 
   [0.6, "attacks_staff_righttoleft", 16, 40, blend_in_release], 
 ],
 ["release_slashright_staff_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
   [0.4, "attacks_staff_righttoleft", 40, 48, blend_in_continue],  
 ],
 ["blocked_slashright_staff",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_blocked|amf_use_weapon_speed|amf_play,
   [attack_blocked_duration, "anim_human", combat+7915, combat+7913, arf_blend_in_2], 
 ],
 ["parried_slashright_staff",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_parried|amf_use_weapon_speed|amf_play,
   [attack_parried_duration, "anim_human", combat+7915, combat+7913, arf_blend_in_2], 
 ],















  ["defend_fist", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_duration, "anim_human", combat+4950, combat+4960, blend_in_defense], 
 ],
 ["defend_fist_keep", 0, amf_rider_rot_defend|amf_priority_defend|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_keep_duration, "anim_human", combat+4950, combat+4960, arf_blend_in_2|arf_cyclic], 
 ],
 ["defend_fist_parry_1", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_1, "anim_human", combat+4962, combat+4970, arf_blend_in_0], 
 ],
 ["defend_fist_parry_2", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_2, "anim_human", combat+4962, combat+4970, arf_blend_in_0], 
 ],
 ["defend_fist_parry_3", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_3, "anim_human", combat+4962, combat+4970, arf_blend_in_0], 
 ],
["defend_shield_forward", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_rider_rot_shield|amf_client_owner_prediction,
   [defend_duration, "defend_shield_forward", 6, 25, blend_in_defense], 
  ],
["defend_shield_up", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_rider_rot_shield|amf_client_owner_prediction,
   [defend_duration, "defend_shield_up", 1, 27, blend_in_defense], 
  ],
["defend_shield_right", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_rider_rot_shield|amf_client_owner_prediction,
   [defend_duration, "defend_shield_right", 5, 26, blend_in_defense], 
  ],
["defend_shield_left", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_rider_rot_shield|amf_client_owner_prediction,
   [defend_duration, "defend_shield_left", 5, 26, blend_in_defense], 
  ],




 ["defend_shield", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_rider_rot_shield|amf_client_owner_prediction,
 #  [defend_duration, "anim_human", defend+105, defend+120, blend_in_defense], 
#   [defend_duration, "defend_shield_parry_all", 5, 26, blend_in_defense], 
   [defend_duration, "defend_shield_up", 1, 17, blend_in_defense], 
  ],
 ["defend_shield_keep", acf_parallels_for_look_slope|acf_anim_length(100), amf_rider_rot_shield|amf_priority_defend|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_keep_duration, "anim_human", defend+118, defend+120, arf_blend_in_4|arf_cyclic], 
 ],
 ["defend_shield_parry_1", acf_parallels_for_look_slope|acf_anim_length(100), amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_shield,
   [defend_parry_duration_1, "anim_human", defend+121, defend+130, arf_blend_in_1], 
 ],
 ["defend_shield_parry_2", acf_parallels_for_look_slope|acf_anim_length(100), amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_shield,
   [defend_parry_duration_2, "anim_human", defend+121, defend+130, arf_blend_in_1], 
 ],
 ["defend_shield_parry_3", acf_parallels_for_look_slope|acf_anim_length(100), amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_shield,
   [defend_parry_duration_3, "anim_human", defend+121, defend+130, arf_blend_in_1], 
 ],
 ["defend_forward_greatsword", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
#   [defend_duration, "anim_human", defend+310, defend+320, blend_in_defense], 
   [defend_duration, "defend_twohanded", 0, 20, blend_in_defense], 
 ],
 ["defend_forward_greatsword_keep", 0, amf_priority_defend|amf_use_defend_speed|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
#   [2.0, "anim_human", defend+320, defend+320, arf_blend_in_3|arf_cyclic], 
   [defend_keep_duration, "defend_twohanded", 170, 170, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_forward_greatsword_parry_1", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
#   [0.3, "anim_human", defend+320, defend+330, arf_blend_in_1], 
   [0.6, "defend_twohanded", 350, 367, arf_blend_in_1], 
 ],
 ["defend_forward_greatsword_parry_2", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
#   [0.3, "anim_human", defend+320, defend+330, arf_blend_in_1], 
   [0.6, "defend_twohanded", 350, 367, arf_blend_in_1], 
 ],
 ["defend_forward_greatsword_parry_3", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
#   [0.3, "anim_human", defend+320, defend+330, arf_blend_in_1], 
   [0.6, "defend_twohanded", 350, 367, arf_blend_in_1], 
 ],
 ["defend_up_twohanded", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_duration, "anim_human", defend+403, defend+410, blend_in_defense], 
 ],
 ["defend_up_twohanded_keep", 0, amf_priority_defend|amf_use_defend_speed|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_keep_duration, "anim_human", defend+410, defend+410, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_up_twohanded_parry_1", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_1, "anim_human", defend+411, defend+418, arf_blend_in_1], 
 ],
 ["defend_up_twohanded_parry_2", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_2, "anim_human", defend+411, defend+418, arf_blend_in_1], 
 ],
 ["defend_up_twohanded_parry_3", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_3, "anim_human", defend+411, defend+418, arf_blend_in_1], 
 ],
 ["defend_right_twohanded", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_duration, "anim_human", defend+510, defend+520, blend_in_defense], 
 ],
 ["defend_right_twohanded_keep", 0, amf_priority_defend|amf_use_defend_speed|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_keep_duration, "anim_human", defend+520, defend+520, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_right_twohanded_parry_1", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_1, "anim_human", defend+521, defend+528, arf_blend_in_1], 
 ],
 ["defend_right_twohanded_parry_2", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_2, "anim_human", defend+521, defend+528, arf_blend_in_1], 
 ],
 ["defend_right_twohanded_parry_3", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_3, "anim_human", defend+521, defend+528, arf_blend_in_1], 
 ],
 ["defend_left_twohanded", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_duration, "anim_human", defend+610, defend+620, blend_in_defense], 
 ],
 ["defend_left_twohanded_keep", 0, amf_priority_defend|amf_use_defend_speed|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_keep_duration, "anim_human", defend+620, defend+620, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_left_twohanded_parry_1", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_1, "anim_human", defend+620, defend+630, arf_blend_in_1], 
 ],
 ["defend_left_twohanded_parry_2", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_2, "anim_human", defend+620, defend+630, arf_blend_in_1], 
 ],
 ["defend_left_twohanded_parry_3", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_3, "anim_human", defend+620, defend+630, arf_blend_in_1], 
 ],
 ["defend_forward_onehanded", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
##   [defend_duration, "defend_onehanded", 8, 15, blend_in_defense], 
   [defend_duration, "defend_forward_onehanded", 20, 41, blend_in_defense], 
#   [defend_duration, "parry_attack_thrust_onehanded", 20, 32, arf_blend_in_1], 
 ],
 ["defend_forward_onehanded_keep", 0, amf_priority_defend|amf_use_defend_speed|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
#   [2.0, "anim_human", defend+1020, defend+1020, arf_blend_in_3|arf_cyclic], 
   [5.0, "defend_onehanded", 15, 70, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_forward_onehanded_parry_1", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
#   [0.3, "anim_human", defend+1021, defend+1030, arf_blend_in_1], 
   [defend_parry_duration_1, "defend_onehanded", 75, 85, arf_blend_in_1], 
##   [defend_parry_duration_1, "defend_forward_onehanded_parry", 11, 18, arf_blend_in_1], 
 ],
 ["defend_forward_onehanded_parry_2", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
#   [0.3, "anim_human", defend+1021, defend+1030, arf_blend_in_1], 
   [defend_parry_duration_2, "defend_onehanded", 75, 85, arf_blend_in_1], 
##   [defend_parry_duration_2, "defend_forward_onehanded_parry", 53, 67, arf_blend_in_1], 
 ],
 ["defend_forward_onehanded_parry_3", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
#   [0.3, "anim_human", defend+1021, defend+1030, arf_blend_in_1], 
   [defend_parry_duration_3, "defend_onehanded", 75, 85, arf_blend_in_1], 
##   [defend_parry_duration_3, "defend_forward_onehanded_parry", 91, 110, arf_blend_in_1], 
 ],
 ["defend_up_onehanded", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
##   [defend_duration, "anim_human", defend+1110, defend+1120, blend_in_defense], 
   [defend_duration, "defend_up_onehanded", 9, 25, blend_in_defense], 
#   [defend_duration, "parry_attack_overswing_onehanded", 7, 19, blend_in_release], 
 ],
 ["defend_up_onehanded_keep", 0, amf_priority_defend|amf_use_defend_speed|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
##   [defend_keep_duration, "anim_human", defend+1120, defend+1120, arf_blend_in_3|arf_cyclic], 
   [2.8, "defend_up_onehanded_keep", 1, 87, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_up_onehanded_parry_1", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_1, "anim_human", defend+1121, defend+1130, arf_blend_in_1], 
##   [defend_parry_duration_1, "defend_up_onehanded_parry", 13, 19, arf_blend_in_1], 
 ],
 ["defend_up_onehanded_parry_2", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_2, "anim_human", defend+1121, defend+1130, arf_blend_in_1], 
##   [defend_parry_duration_2, "defend_up_onehanded_parry", 46, 52, arf_blend_in_1], 
 ],
 ["defend_up_onehanded_parry_3", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_3, "anim_human", defend+1121, defend+1130, arf_blend_in_1], 
##   [defend_parry_duration_3, "defend_up_onehanded_parry", 86, 109, arf_blend_in_1], 
 ],
 ["defend_right_onehanded", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
##   [defend_duration, "anim_human", defend+1210, defend+1220, blend_in_defense], 
   [defend_duration, "defend_right_onehanded", 14, 31, blend_in_defense], 
#   [defend_duration, "parry_attack_slashright_onehanded", 9, 22, arf_blend_in_1], 
 ],
 ["defend_right_onehanded_keep", 0, amf_priority_defend|amf_use_defend_speed|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
##   [defend_keep_duration, "anim_human", defend+1220, defend+1220, arf_blend_in_5|arf_cyclic], 
   [2.5, "defend_right_onehanded_keep", 0, 79, arf_blend_in_5|arf_cyclic], 
 ],
 ["defend_right_onehanded_parry_1", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_1, "anim_human", defend+1221, defend+1230, arf_blend_in_1], 
##   [defend_parry_duration_1, "defend_right_onehanded_parry", 4, 10, arf_blend_in_1], 
 ],
 ["defend_right_onehanded_parry_2", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_2, "anim_human", defend+1221, defend+1230, arf_blend_in_1], 
##   [defend_parry_duration_2, "defend_right_onehanded_parry", 38, 47, arf_blend_in_1], 
 ],
 ["defend_right_onehanded_parry_3", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_3, "anim_human", defend+1221, defend+1230, arf_blend_in_1], 
##   [defend_parry_duration_3, "defend_right_onehanded_parry", 80, 96, arf_blend_in_1], 
 ],
 ["defend_left_onehanded", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
##   [defend_duration, "anim_human", defend+1310, defend+1320, blend_in_defense], 
   [defend_duration, "defend_left_onehanded", 12, 28, blend_in_defense], 
 #  [defend_duration, "parry_attack_slashleft_onehanded", 11, 24, blend_in_ready], 
 ],
 ["defend_left_onehanded_keep", 0, amf_priority_defend|amf_use_defend_speed|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
##   [defend_keep_duration, "anim_human", defend+1320, defend+1320, arf_blend_in_3|arf_cyclic], 
   [2.2, "defend_left_onehanded_keep", 1, 71, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_left_onehanded_parry_1", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_1, "anim_human", defend+1321, defend+1330, arf_blend_in_1], 
##   [defend_parry_duration_1, "defend_left_onehanded_parry", 4, 13, arf_blend_in_1], 
 ],
 ["defend_left_onehanded_parry_2", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_2, "anim_human", defend+1321, defend+1330, arf_blend_in_1], 
##   [defend_parry_duration_2, "defend_left_onehanded_parry", 30, 40, arf_blend_in_1], 
 ],
 ["defend_left_onehanded_parry_3", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_3, "anim_human", defend+1321, defend+1330, arf_blend_in_1], 
##   [defend_parry_duration_3, "defend_left_onehanded_parry", 58, 90, arf_blend_in_1], 
 ],
 ["defend_forward_staff", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
#   [pole_defend_duration, "anim_human", defend+2010, defend+2020, blend_in_defense], 
   [defend_duration, "defend_staff", 0, 5, blend_in_defense], 
 ],
 ["defend_forward_staff_keep", 0, amf_priority_defend|amf_use_defend_speed|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
#   [2.0, "anim_human", defend+2020, defend+2020, arf_blend_in_3|arf_cyclic], 
#   [4.0, "defend_staff", 0, 45, arf_blend_in_3|arf_cyclic], 
   [defend_keep_duration, "defend_staff", 5, 5, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_forward_staff_parry_1", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
#   [0.3, "anim_human", defend+2021, defend+2030, arf_blend_in_1], 
   [0.6, "defend_staff", 56, 70, arf_blend_in_1], 
 ],
 ["defend_forward_staff_parry_2", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
#   [0.3, "anim_human", defend+2021, defend+2030, arf_blend_in_1], 
   [0.6, "defend_staff", 56, 70, arf_blend_in_1], 
 ],
 ["defend_forward_staff_parry_3", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
#   [0.3, "anim_human", defend+2021, defend+2030, arf_blend_in_1], 
   [0.6, "defend_staff", 56, 70, arf_blend_in_1], 
 ],
 ["defend_up_staff", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_duration, "anim_human", defend+2110, defend+2120, blend_in_defense], 
 ],
 ["defend_up_staff_keep", 0, amf_priority_defend|amf_use_defend_speed|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_keep_duration, "anim_human", defend+2120, defend+2120, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_up_staff_parry_1", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_1, "anim_human", defend+2121, defend+2130, arf_blend_in_1], 
 ],
 ["defend_up_staff_parry_2", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_2, "anim_human", defend+2121, defend+2130, arf_blend_in_1], 
 ],
 ["defend_up_staff_parry_3", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_3, "anim_human", defend+2121, defend+2130, arf_blend_in_1], 
 ],
 ["defend_right_staff", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_duration, "anim_human", defend+2210, defend+2220, blend_in_defense], 
 ],
 ["defend_right_staff_keep", 0, amf_priority_defend|amf_use_defend_speed|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_keep_duration, "anim_human", defend+2220, defend+2220, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_right_staff_parry_1", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_1, "anim_human", defend+2221, defend+2230, arf_blend_in_1], 
 ],
 ["defend_right_staff_parry_2", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_2, "anim_human", defend+2221, defend+2230, arf_blend_in_1], 
 ],
 ["defend_right_staff_parry_3", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_3, "anim_human", defend+2221, defend+2230, arf_blend_in_1], 
 ],
 ["defend_left_staff", 0, amf_play|amf_restart|amf_priority_defend|amf_use_defend_speed|amf_use_inertia|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_duration, "anim_human", defend+2310, defend+2320, blend_in_defense], 
 ],
 ["defend_left_staff_keep", 0, amf_priority_defend|amf_use_defend_speed|amf_keep|amf_rider_rot_defend|amf_client_owner_prediction,
   [defend_keep_duration, "anim_human", defend+2320, defend+2320, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_left_staff_parry_1", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_1, "anim_human", defend+2321, defend+2330, arf_blend_in_1], 
 ],
 ["defend_left_staff_parry_2", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_2, "anim_human", defend+2321, defend+2330, arf_blend_in_1], 
 ],
 ["defend_left_staff_parry_3", 0, amf_priority_defend_parry|amf_play|amf_restart|amf_rider_rot_defend,
   [defend_parry_duration_3, "anim_human", defend+2321, defend+2330, arf_blend_in_1], 
 ],

 
 ["strike_head_left", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,

   [0.5, "strikes", 55, 71, arf_blend_in_3], 
 ],
 ["strike_head_right", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.5, "strikes", 4, 19, arf_blend_in_3], 
 ],
 ["strike_head_front", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.5, "strikes", 180, 198, arf_blend_in_3], 
 ],
 ["strike_head_back", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.6, "strikes_back", 4, 25, arf_blend_in_3], 
 ],
 ["strike_chest_left", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.5, "strikes", 706, 724, arf_blend_in_3], 
 ],
 ["strike_chest_right", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.6, "strikes", 487, 512, arf_blend_in_3], 
 ],
 ["strike_chest_front", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.6, "strikes", 881, 905, arf_blend_in_3], 
 ],
 ["strike_chest_back", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.5, "strikes_back", 401, 418, arf_blend_in_3], 
 ],
 ["strike_abdomen_left", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.58, "strikes", 1425, 1444, arf_blend_in_3], 
 ],
 ["strike_abdomen_right", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.6, "strikes", 1168, 1188, arf_blend_in_3], 
 ],
 ["strike_abdomen_front", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.6, "strikes", 1618, 1640, arf_blend_in_3], 
 ],
 ["strike_abdomen_back", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.53, "strikes_back", 886, 904, arf_blend_in_3], 
 ],
 ["strike_legs_left", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.55, "strikes", 2284, 2305, arf_blend_in_3], 
 ],
 ["strike_legs_right", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.56, "strikes", 1999, 2020, arf_blend_in_3], 
 ],
 ["strike_legs_front", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.56, "strikes", 2655, 2676, arf_blend_in_3], 
 ],
 ["strike_legs_back", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.5, "strikes_back", 1120, 1137, arf_blend_in_3], 

 ],

 ["strike2_head_left", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,


   [0.5, "strikes", 55, 71, arf_blend_in_3], 
 ],
 ["strike2_head_right",acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.5, "strikes", 4, 19, arf_blend_in_3], 
 ],
 ["strike2_head_front",acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.5, "strikes", 180, 198, arf_blend_in_3], 
 ],
 ["strike2_head_back", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
#   [0.6, "strikes_back", 4, 25, arf_blend_in_3], 
   [0.55, "strikes_back", 4, 25, arf_blend_in_3], 
 ],
 ["strike2_chest_left", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.5, "strikes", 706, 724, arf_blend_in_3], 
 ],
 ["strike2_chest_right", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
#   [0.6, "strikes", 487, 512, arf_blend_in_3], 
   [0.55, "strikes", 487, 512, arf_blend_in_3], 
 ],
 ["strike2_chest_front", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
#   [0.6, "strikes", 881, 905, arf_blend_in_3], 
   [0.55, "strikes", 881, 905, arf_blend_in_3], 
 ],
 ["strike2_chest_back",acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.5, "strikes_back", 401, 418, arf_blend_in_3], 
 ],
 ["strike2_abdomen_left", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.55, "strikes", 1425, 1444, arf_blend_in_3], 
 ],
 ["strike2_abdomen_right", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
#   [0.6, "strikes", 1168, 1188, arf_blend_in_3], 
   [0.55, "strikes", 1168, 1188, arf_blend_in_3], 
 ],
 ["strike2_abdomen_front", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
#   [0.6, "strikes", 1618, 1640, arf_blend_in_3], 
   [0.55, "strikes", 1618, 1640, arf_blend_in_3], 
 ],
 ["strike2_abdomen_back", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.53, "strikes_back", 886, 904, arf_blend_in_3], 
 ],
 ["strike2_legs_left", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.55, "strikes", 2284, 2305, arf_blend_in_3], 
 ],
 ["strike2_legs_right", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.56, "strikes", 1999, 2020, arf_blend_in_3], 
 ],
 ["strike2_legs_front", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.56, "strikes", 2655, 2676, arf_blend_in_3], 
 ],
 ["strike2_legs_back", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.5, "strikes_back", 1120, 1137, arf_blend_in_3], 
 ],



 ["strike3_head_left", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.9 * 1.1, "strikes3_head", 107, 146, arf_blend_in_3], 
 ],
 ["strike3_head_right",acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.9 * 1.0, "strikes3_head", 208, 251, arf_blend_in_3], 
 ],
 ["strike3_head_front",acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.9 * 1.0, "strikes3_head", 14, 48, arf_blend_in_3], 
 ],
 ["strike3_head_back", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.9 * 1.0, "strikes3_head", 309, 346, arf_blend_in_3],
 ],
 ["strike3_chest_left", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.9 * 1.0, "strikes3_chest", 61, 97, arf_blend_in_3],
 ],
 ["strike3_chest_right", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.9, "strikes3_chest", 108, 145, arf_blend_in_3], 
 ],
 ["strike3_chest_front", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.8, "strikes3_chest", 3, 27, arf_blend_in_3], 
 ],
## ["strike3_chest_back",acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
##   [1.3, "strikes3_chest", 264, 310, arf_blend_in_3], 
## ],
 ["strike3_abdomen_left", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.9 * 1.0, "strikes3_abdomen", 105, 150, arf_blend_in_3, 0, (0, -0.0, 0.0)], 
 ],
 ["strike3_abdomen_right", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.9, "strikes3_abdomen", 63, 98, arf_blend_in_3, 0, (0, 0.0, 0.0)], 
 ],
 ["strike3_abdomen_front", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.9 * 1.0, "strikes3_abdomen", 4, 43, arf_blend_in_3,  0, (0, 0.0, 0.0)],
 ],
 ["strike3_abdomen_back", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.9 * 1.2, "strikes3_abdomen_back", 0, 53, arf_blend_in_3], 
 ],
## ["strike3_legs_left", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
##   [0.6, "strikes", 2284, 2305, arf_blend_in_3], 
## ],
## ["strike3_legs_right", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
##   [0.7, "strikes", 1999, 2020, arf_blend_in_3], 
## ],
## ["strike3_legs_front", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
##   [0.7, "strikes", 2655, 2676, arf_blend_in_3], 
## ],
## ["strike3_legs_back", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
##   [0.8, "strikes_back", 1120, 1144, arf_blend_in_3], 
## ],

## ["strike_head_front_left", 0, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,


##   [0.55, "anim_human", blow+0, blow+10, arf_blend_in_3], 
## ],
 ["strike_head_front_left_reloc", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.6,  "strike_frontal", 0, 37, arf_blend_in_3], 
#   [0.6,  "anim_human", blow+5200, blow+5220, arf_blend_in_3], 
 ],


#hispania 1200 muertes
 
  ["fall_face_hold", acf_enforce_all|acf_align_with_ground|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_keep|amf_client_prediction,
   [2.2, "death_face", 8, 60, arf_blend_in_16|arf_make_custom_sound, pack2f(0.5, 0.0), (0,0,0), 0.6],



   [1.2, "death_new5", 5, 103, arf_blend_in_16|arf_make_custom_sound, pack2f(0.3, 0.0), (0,0,0), 0.5],

  

 ],
 ["fall_chest_front", acf_enforce_all|acf_align_with_ground|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_keep|amf_client_prediction,
   [1.0, "death_chest", 4, 37, arf_blend_in_16|arf_make_custom_sound, pack2f(0.9, 0.0), (0,0,0), 0.5],


 #  [1.0, "new_death_7", 1, 199, arf_blend_in_16|arf_make_custom_sound, pack2f(0.9, 0.0), (0,0,0), 0.5],
   [1.0, "new_death_7", 1, 199, arf_blend_in_16|arf_make_custom_sound, pack2f(0.47, 0.82), (0,0,0), 1.8],
   [2.0, "new_death_10", 0, 54, arf_blend_in_16|arf_make_custom_sound, pack2f(0.9, 0.0), (0,0,0), 0.5],
   [2.0, "new_death_fall", 0, 60, arf_blend_in_16|arf_make_custom_sound, pack2f(0.9, 0.0), (0,0,0), 0.5],
  
  
 ],
 ["fall_abdomen_hold_front", acf_enforce_all|acf_align_with_ground|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_keep|amf_client_prediction,
   [2.7, "death_abdomen", 5, 96, arf_blend_in_16|arf_make_custom_sound, pack2f(0.4, 0.0), (0,0,0), 0.5],
   [4.7, "wounded_leg_right_fall", 1, 44, arf_blend_in_16|arf_make_custom_sound, pack2f(0.4, 0.0), (0,0,0), 0.5],
 ],
 ["fall_head_front", acf_enforce_all|acf_align_with_ground|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_keep|amf_client_prediction,
   [2.0, "new_death_9", 0, 60, arf_blend_in_16|arf_make_custom_sound, pack2f(0.9, 0.0), (0,0,0), 0.5],
   [1.2, "anim_human", blow+100, blow+138, arf_blend_in_16|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 0.8], 
 ],
 ["fall_right_front", acf_enforce_all|acf_align_with_ground|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_keep|amf_client_prediction,
   [2.0, "death2", 0, 53, arf_blend_in_16|arf_make_custom_sound, pack2f(0.65, 0.0), (0,0,0), 1.0], 
   [2.7, "new_death_8", 0, 14, arf_blend_in_16|arf_make_custom_sound, pack2f(0.65, 0.0), (0,0,0), 1.0], 
 
 ],
 ["fall_body_back", acf_enforce_all|acf_align_with_ground|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_keep|amf_client_prediction,
   [2.7, "death", 0, 83, arf_blend_in_16|arf_make_custom_sound, pack2f(0.47, 0.82), (0,0,0), 1.8],
   [2.0, "new_death_crawl", 1, 109, arf_blend_in_16|arf_make_custom_sound, pack2f(0.47, 0.82), (0,0,0), 1.8], 
   [1.0, "death_new4", 10, 84, arf_blend_in_16|arf_make_custom_sound, pack2f(0.47, 0.82), (0,0,0), 1.8], 
   [2.0, "death", 0, 83, arf_blend_in_16|arf_make_custom_sound, pack2f(0.47, 0.82), (0,0,0), 1.8],
   [2.0, "new_death_crawl", 1, 109, arf_blend_in_16|arf_make_custom_sound, pack2f(0.47, 0.82), (0,0,0), 1.8], 
 ],
## ["fall_rider_head_front", acf_enforce_all,
##   [2.2, "anim_human", blow+200, blow+275, arf_blend_in_3], 
## ],
 ["fall_rider_right_forward", acf_enforce_all|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_keep|amf_client_prediction,
   [2.2, "anim_human", blow+200, blow+275, arf_blend_in_3|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 0.3], 
##   [2.2, "fall_rider_right_forward", 0, 68, arf_blend_in_3|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 0.3], 
 ],
 ["fall_rider_right", acf_enforce_all|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_keep|amf_client_prediction,
   [2.2, "anim_human", blow+200, blow+275, arf_blend_in_3|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 0.3], 
##   [1.9, "fall_rider_right", 0, 57, arf_blend_in_3|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 0.3], 
 ],
 ["fall_rider_left", acf_enforce_all|acf_lock_camera, amf_priority_die|amf_accurate_body|amf_keep|amf_client_prediction,
   [2.2, "anim_human", blow+200, blow+275, arf_blend_in_3|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 0.3], 
##   [1.9, "fall_rider_left", 0, 56, arf_blend_in_3|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 0.3], 
 ],
## ["rider_fall_in_place", acf_enforce_lowerbody, amf_priority_fall_from_horse|amf_play|amf_client_prediction,
##   [3.8, "anim_human", blow + 1000, blow + 1075, arf_blend_in_16|arf_make_custom_sound, pack2f(0.0, 0.0), (0,0,0), 0.5], 
## ],
 ["rider_fall_right", acf_enforce_all|acf_displace_position, amf_priority_fall_from_horse|amf_play|amf_accurate_body|amf_client_prediction,
   [2.5, "anim_human_02", 350, 382,  arf_blend_in_8, 0, (0.8,-1.8,0), 0.5],
 ],
 ["rider_fall_roll", acf_enforce_all|acf_displace_position, amf_priority_fall_from_horse|amf_play|amf_accurate_body|amf_client_prediction,
   [2.5, "anim_human", blow+ 2000, blow+2084,  arf_blend_in_8, 0, (0.0,0.0,0), 1.0],
 ],
 ["strike_chest_front_stop", acf_enforce_all, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [0.4, "anim_human", blow+5000, blow+5010, arf_blend_in_3], 
 ],
 ["strike_fall_back_rise", acf_enforce_lowerbody|acf_align_with_ground, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [1.7, "anim_human", blow+5400, blow+5453, arf_blend_in_2|arf_make_custom_sound, pack2f(0.4, 0.0), (0,0,0), 0.5],
 ],
 ["strike_fall_back_rise_upper", acf_align_with_ground, amf_priority_striked|amf_play|amf_accurate_body|amf_restart,
   [1.44, "anim_human", blow+5400, blow+5445, arf_blend_in_2], 
 ],


 ["cheer", 0, amf_play|amf_priority_mount,
##   [2.5, "anim_human", 70000, 70045, arf_blend_in_5], 
##   [3.0, "anim_human", 70100, 70150, arf_blend_in_5],
   [6.0, "man_cheer", 0, 185, arf_blend_in_5],
   [3.0, "man_cheer", 200, 289, arf_blend_in_5],

   [4.5, "man_cheer", 300, 437, arf_blend_in_5],
   [5.5, "man_cheer", 450, 617, arf_blend_in_5],
 ],

 ["cheer_stand", arf_cyclic, amf_play|amf_priority_mount,
   [31.5, "man_cheer", 650, 1597, arf_blend_in_5],   

 ],

 ["stand_townguard", 0, 0,
   [79.0, "stand_guardsman", 0, 2397, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],

 ],
 ["stand_lady", 0, 0,
   [29.0, "lady_stand", 0, 863, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 ],
 ["stand_lord", 0, 0,
   [45.0, "lord_listen", 0, 962, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [10.0, "lord_stand", 0, 111, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [65.0, "lord_sant2", 0, 1400, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [10.0, "lord_stand", 0, 111, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [60.0, "lord_sant2", 1400, 2550, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [60.0, "lord_sant2", 2550, 3601, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [10.0, "lord_stand", 0, 111, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 ],

 ["dance", 0, 0,
   [20.0, "anim_human", 0, 387, arf_blend_in_5], 
#   [10.0, "anim_human_temp", 0, 10, arf_blend_in_5], 
 ],
 ["pose_1", 0, 0,
   [3.0, "poses", 0, 0, arf_cyclic],
 ],
 ["pose_2", 0, 0,
   [3.0, "poses", 2, 2, arf_cyclic],
 ],
 ["pose_3", 0, 0,
   [3.0, "poses", 4, 4, arf_cyclic],
 ],
 ["pose_4", 0, 0,
   [3.0, "poses", 6, 6, arf_cyclic],
 ],
 ["pose_5", 0, 0,
   [3.0, "poses", 8, 8, arf_cyclic],

 ],








 
 ### Unused human animations start from here.

 ["wedding_guest", 0, amf_play|amf_priority_die,
  [30.0, "wedding_guest", 0, 906, arf_cyclic]],
 
 ["wedding_guest_notr", 0, amf_play|amf_priority_die,
  [32.0, "wedding_guest_notr", 0, 962, arf_cyclic]],


 ["wedding_guest_woman", 0, amf_play|amf_priority_die,
  [27.5, "wedding_guest_woman", 0, 825, arf_cyclic]],


 ["wedding_dad_stairs", 0, amf_play|amf_priority_die|amf_start_instantly,
  [10.0, "wedding_dad_stairs", 0, 300, arf_blend_in_0]],


 ["wedding_dad_walk", 0, amf_play|amf_priority_die|amf_start_instantly,
  [4.5, "wedding_dad_walk", 0, 134, arf_blend_in_0]],
 
 ["wedding_bride_stairs", 0, amf_play|amf_priority_die|amf_start_instantly,
  [10.0, "wedding_bride_stairs", 0, 300, arf_blend_in_0]],


 ["wedding_bride_walk", 0, amf_play|amf_priority_die|amf_start_instantly,
  [4.5, "wedding_bride_walk", 0, 134, arf_blend_in_0]],


 ["wedding_groom_wait", 0, amf_play|amf_priority_die|amf_start_instantly|amf_keep,
  [10.0, "wedding_groom_last", 0, 2, arf_blend_in_0]],


 ["wedding_groom_last", 0, amf_play|amf_priority_die|amf_start_instantly|amf_keep,
  [10.0, "wedding_groom_last", 0, 300, arf_blend_in_0]],


 ["wedding_dad_last", 0, amf_play|amf_priority_die|amf_start_instantly|amf_keep,
  [10.0, "wedding_dad_last", 0, 300, arf_blend_in_0]],


 ["wedding_bride_last", 0, amf_play|amf_priority_die|amf_start_instantly|amf_keep,
  [10.0, "wedding_bride_last", 0, 300, arf_blend_in_0]],


 ["equip_bayonet", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "equip_musket", 5, 13, arf_blend_in_0],
 ],
 ["unequip_bayonet", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "equip_musket", 5, 13, arf_blend_in_0],
 ],
 





["crouch_unarmed", 0, amf_client_prediction,
   [11.0, "crouch_stand_man", 0, 315, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 ],
 ["crouch_single", 0, amf_client_prediction,
   [11.0, "crouch_stand_man", 0, 315, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 ],
 ["crouch_greatsword", 0, amf_client_prediction,
   [6.0, "crouch_greatsword_cstance", 0, 170, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],  
 ],
 ["crouch_staff", 0, amf_client_prediction,
   [5.0, "crouch_staff_cstance", 0, 120, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],  
 ],
 ["crouch_crossbow", 0, amf_client_prediction,
   [2.0, "staff_cstance", 0, 60, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],  
 ],
 ["crouch_ready_pistol", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_pistol,
   [0.3, "crouch_fire_pistol", 1, 12, blend_in_ready],
 ],
 ["crouch_release_pistol", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_pistol,
   [0.3, "crouch_fire_pistol", 12, 21, arf_blend_in_1],
 ],
 ["reload_musket_full", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
   [2.5, "man_reload", 0, 340, arf_stick_item_to_left_hand|arf_blend_in_3],
 ],
 ["reload_musket_two_third", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
   [1.7, "man_reload", 110, 340, arf_stick_item_to_left_hand|arf_blend_in_3],
 ],
 ["reload_musket_one_third", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
   [0.6, "man_reload", 270, 340, arf_stick_item_to_left_hand|arf_blend_in_3],
 ],
 ["crouch_pike", 0, amf_client_prediction,
   [3.3, "crouch_staff_cstance_attack", 0, 100, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],  
 ],
 ["crouch_pike_recover", 0, amf_priority_parried|amf_use_weapon_speed|amf_play,
   [1.2, "crouch_staff_cstance_attack", 105, 137, arf_blend_in_3, 0, (0, 0, 0), 0.0],  
 ],
 ["ready_overswing_spear", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
	[ready_durn, "spear_thrust_overhead", 0, 20, blend_in_ready],
 ],
 ["release_overswing_spear", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
 	[0.6, "spear_thrust_overhead", 20, 41, blend_in_release],
 ],
 ["release_overswing_spear_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
   [0.3, "spear_thrust_overhead", 41, 52, arf_blend_in_2],
 ],
 ["parried_overswing_spear", 0, amf_priority_parried|amf_use_weapon_speed|amf_play,
   [0.3, "spear_thrust_overhead", 26, 22, arf_blend_in_2],
 ],
 ["blocked_overswing_spear", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play,
  [0.3, "spear_thrust_overhead", 26, 22, arf_blend_in_2],
],
 ["reload_pistol_half", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
   [1.2, "reload_pistol_new", 125, 250, arf_blend_in_3],
 ],
 ["ready_overswing_musket", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
  [ready_durn, "musket_upper_swing", 12, 24, blend_in_ready],
 ],
 ["release_overswing_musket", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
  [0.55, "musket_upper_swing", 24, 40, blend_in_release],
 ],
 ["release_overswing_musket_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
  [0.4, "musket_upper_swing", 40, 48, arf_blend_in_2],
 ],
 ["parried_overswing_musket", 0, amf_priority_parried|amf_use_weapon_speed|amf_play,
  [attack_parried_duration, "musket_upper_swing", 34, 30, blend_in_parry],
 ],
 ["blocked_overswing_musket", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play,
  [attack_blocked_duration, "musket_upper_swing", 34, 30, blend_in_parry],
 ],
 ["ready_thrust_musket", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
  [ready_durn, "musket_thrust_forward", 1, 19, blend_in_ready],
 ],
 ["release_thrust_musket", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
  [0.9, "musket_thrust_forward", 19, 50, blend_in_release],
 ],
 ["release_thrust_musket_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
  [0.2, "musket_thrust_forward", 50, 54, arf_blend_in_2],
 ],
 ["parried_thrust_musket", 0, amf_priority_parried|amf_use_weapon_speed|amf_play,
   [attack_parried_duration, "musket_thrust_forward_parry", 1, 9, arf_blend_in_2],
 ],
 ["blocked_thrust_musket", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play,
  [attack_blocked_duration, "musket_thrust_forward_parry", 1, 9, arf_blend_in_2],
 ],
 ["equip_pistol_melee", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "equip_pistol", 0, 10, arf_blend_in_0],
 ],
 ["unequip_pistol_melee", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
   [0.3, "equip_pistol", 0, 10, arf_blend_in_0],
 ],
# ["unused_human_anim_44", 0, 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_45", 0, 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_46", 0, 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_47", 0, 0, [1.0, "anim_human", 0, 1, 0]],
#BEGIN Before AI Crouching backup
# ["unused_human_anim_48", 0, 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_49", 0, 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_50", 0, 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_51", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 #END Before AI crouching Backup
 #Begin AI Crouching Code
	["fall_head_front_legshot", acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[0.55, "strikes", 2284, 2305, arf_blend_in_3]
	],

	["taunt", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_client_prediction|amf_play,
		[3.0, "taunt_1h_s3", 5, 90, arf_blend_in_1]
	],

	["pevic_thrust", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_client_prediction|amf_play,
		[2.0, "pelvic_thrust", 90, 165, arf_blend_in_1

]
	],

	["howl", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_client_prediction|amf_play,
		[4.5, "man_cheer", 0, 185, arf_blend_in_1],
		[4.5, "man_cheer", 200, 289, arf_blend_in_1],
		[4.5, "man_cheer", 300, 437, arf_blend_in_1],
		[4.5, "man_cheer", 450, 617, arf_blend_in_1]
	]
,

	["tekst", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_client_prediction|amf_play,
		[3.0, "tekst", 1, 10, arf_blend_in_1
]
	],

	["fatigues1", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_client_prediction|amf_play
,
		[3.0, "taunt", 5, 90, arf_blend_in_1]
	],


	["dancer_1", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.5, "dancer_1", 0, 24, arf_cyclic|arf_use_stand_progress

]
	],

	["dancer_2", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.5, "dancer_2", 0, 19, arf_cyclic|arf_use_stand_progress

]
	],

	["dancer_3", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.5, "dancer_3", 0, 19, arf_cyclic|arf_use_stand_progress

]
	],

	["dancer_4", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.5, "dancer_4", 0, 18, arf_cyclic|arf_use_stand_progress

]
	],

	["female_fucker", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.0, "female_fucker", 0, 10, arf_cyclic|arf_use_stand_progress

]
	],

	["female_fucker_1", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.0, "female_fucker_1", 0, 10, arf_cyclic|arf_use_stand_progress

]
	],

	["female_fucker_2", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.0, "female_fucker_2", 0, 10, arf_cyclic|arf_use_stand_progress

]
	],

	["fuck_female", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.0, "fuck_female", 0, 9, arf_cyclic|arf_use_stand_progress

]
	],

	["fuck_female_1", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.5, "fuck_female_1", 0, 9, arf_cyclic|arf_use_stand_progress

]
	],

	["fuck_female_2", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.5, "fuck_female_2", 0, 9, arf_cyclic|arf_use_stand_progress

]
	],

	["fuck_female_orgasm", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.5, "fuck_female_orgasm", 0, 9, arf_cyclic|arf_use_stand_progress

]
	],

	["fuck_male", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.0, "fuck_male", 0, 9, arf_cyclic|arf_use_stand_progress

]
	],

	["fuck_male_1", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.5, "fuck_male_1", 0, 9, arf_cyclic|arf_use_stand_progress

]
	],

	["fuck_male_orgasm", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.5, "fuck_male_orgasm", 0, 9, arf_cyclic|arf_use_stand_progress

]
	],

	["male_fucked", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.0, "male_fucked", 0, 10, arf_cyclic|arf_use_stand_progress

]
	],

	["curtsey", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[2.5, "curtsey", 0, 40, arf_cyclic|arf_use_stand_progress

]
	],

	["drunk_cheers", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[30.0, "drunk_cheers", 0, 9, arf_cyclic|arf_use_stand_progress

]
	],

	["freeze_hold", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[30.0, "curtsey", 0, 4, arf_cyclic|arf_use_stand_progress

]
	],

	["blow_job", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[1.0, "fuck_female_blow", 0, 9, arf_cyclic|arf_use_stand_progress

]
	],

	["female_cum", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[10.0, "female_cum", 0, 10, arf_cyclic|arf_use_stand_progress

]
	],

	["male_masterb", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[0.7, "male_masterb", 0, 5, arf_cyclic|arf_use_stand_progress

]
	],

	["female_masturb", acf_enforce_all, amf_priority_kick|amf_priority_jump_end|amf_play,
		[0.4, "female_masturb", 0, 4, arf_cyclic|arf_use_stand_progress
		#Dismemberment DMK
##	  ["handchop", 0, amf_priority_striked|amf_play,
#    [1.5, "strikes", 55, 71, arf_blend_in_3],
#  ], #here
#  ["armchop", 0, amf_priority_striked|amf_play,
#    [1.6, "strikes", 2284, 2305, arf_blend_in_3],
#  ], #here make sure unused anims are right
#  
#  #
#Dismemberment DMK
]
],
 ["unused_human_anim_76", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_77", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_78", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_79", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_80", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_81", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_82", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_83", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_84", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_85", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_86", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_87", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_88", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_89", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_90", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_91", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_92", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_93", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_94", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_95", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_96", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_97", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_98", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_99", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_100", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 #ENVFIX ANIMATION FIX#
	["shield_bash", acf_align_with_ground|acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[1.5, "defend_shield_parry_all", 1, 50, arf_blend_in_3],
		[1.5, "defend_shield_right", 1, 50, arf_blend_in_3],
		[1.5, "defend_shield_left", 1, 50, arf_blend_in_3],
		[1.5, "defend_shield_right", 1, 50, arf_blend_in_3]

	],

	["shield_strike", acf_align_with_ground|acf_enforce_all, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[1.0, "anim_human", 45000, 45010, arf_blend_in_3|arf_make_custom_sound],
		[1.7, "anim_human", 45400, 45453, arf_blend_in_2|arf_make_custom_sound],
		[1.44, "anim_human", 45400, 45445, arf_blend_in_2|arf_make_custom_sound]
	],

	["spearwall_hold", acf_align_with_ground|acf_enforce_all|acf_thrust, amf_priority_striked|amf_accurate_body|amf_play|amf_restart,
		[4.0, "anim_human", 27310, 27310, arf_blend_in_6]

	],

	["sit_drink", acf_enforce_all, amf_accurate_body,
		[3.0, "sit_drink", 0, 2, arf_cyclic, 0, (0.0, 0.0, 0.0), 0.25]
	],

































































































































































































































































































































































































































































































































































































































































































































































































	#ENVFIX END ANIMATION FIX
 ["horse_stand", 0, amf_client_prediction,
##   [5.0, "anim_horse", 1000, 1044, arf_cyclic],


##   [3.0, "anim_horse", 600, 644, arf_cyclic], 
   [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],


   [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   [1.5, "anim_horse", 644, 688, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],


   [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   [1.5, "anim_horse", 688, 732, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],


   [3.5, "anim_horse", 732, 820, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],


   [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   [2.5, "anim_horse", 820, 908, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
 ],
 ["horse_pace_1", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
     [1.0, "anim_horse", 0, 31, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.25,0.42,0.75,0.92), (0, 0, 0), 0.25], 


 ],
 ["horse_pace_2", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
[0.8, "anim_horse", 50, 69, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.15,0.16,0.65,0.66), (0, 0, 0), 0.9],
 ],
 ["horse_pace_3", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.6, "anim_horse", 100, 116, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.93,0.95,0.35,0.42), (0, 0, 0), 0.6],


 ],
 ["horse_pace_4", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
   [0.5, "anim_horse", 150, 165, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.4,0.31,0.79,0.94), (0, 0, 0), 0.2],
 ],
 ["horse_walk_backward", acf_enforce_lowerbody, amf_client_prediction,
   [1.9, "anim_horse", 31, 0, arf_cyclic|arf_use_inv_walk_progress|arf_make_walk_sound,pack4f(0.07,0.13,0.56,0.63), (0, 0, 0), 0.0],



 ],
 ["horse_rear", acf_enforce_lowerbody | acf_ignore_slope, amf_priority_rear|amf_play,
#   [1.4, "anim_horse_temp", 1, 10,  arf_blend_in_1],
##   [2.5, "anim_horse", 505, 580,  arf_blend_in_8],
   [1.7, "anim_horse", 265, 297,  arf_blend_in_8],

 ],
 ["horse_jump", acf_enforce_lowerbody, amf_priority_jump|amf_play|amf_client_prediction,
   [1.6, "anim_horse", 205, 222,  arf_blend_in_4], #|arf_end_pos_0_25],
 ],
 ["horse_jump_end", acf_enforce_lowerbody, amf_priority_jump_end|amf_play|amf_client_prediction,
   [0.1, "anim_horse", 222,  224,  arf_blend_in_8],
 ],

 ["horse_turn_right", 0, amf_client_prediction,
   [1.0, "anim_horse", 500, 533, arf_blend_in_4|arf_cyclic], 
 ],
 ["horse_turn_left", 0, amf_client_prediction,
   [1.0, "anim_horse", 450, 483, arf_blend_in_4|arf_cyclic],
 ],
 ["horse_turn_right_head", 0, amf_client_prediction,
   [1.0, "anim_horse", 500, 533, arf_blend_in_4|arf_cyclic], 
 ],
 ["horse_turn_left_head", 0, amf_client_prediction,
   [1.0, "anim_horse", 450, 483, arf_blend_in_4|arf_cyclic],
 ],
 ["horse_slow", 0, amf_client_prediction, #not used anymore?
   [3.0, "anim_horse", 0, 31,arf_cyclic], 
   [1.5, "anim_horse", 0, 31, arf_cyclic], 
 ],
 ["horse_fall_in_place", acf_enforce_all|acf_align_with_ground, amf_priority_striked|amf_keep|amf_client_prediction,
   [4.0, "anim_horse", 0, 38, arf_blend_in_16|arf_make_custom_sound, pack2f(0.0, 0.0)], 
 ],
 ["horse_fall_right", acf_enforce_all|acf_align_with_ground, amf_priority_striked|amf_keep|amf_client_prediction,
   [1.75, "anim_horse", 350, 375,  arf_blend_in_8|arf_make_custom_sound, pack2f(0.6, 0.0), (0, 0, 0), 0.5],
 ],
 ["horse_fall_roll", acf_enforce_all|acf_align_with_ground, amf_priority_striked|amf_keep|amf_client_prediction,
   [2.5, "anim_horse", 400, 428,  arf_blend_in_8|arf_make_custom_sound, pack2f(0.3, 0.0), (0, 0, 0), 1.8],
 ],
 ### Unused horse animations start from here.
 	["process_fuck_base", 0, 0,
		[3.0, "process_fuck_base", 0, 0, arf_cyclic
]
	],

	["process_fuck_stand_1", 0, 0,
		[3.0, "process_fuck_stand_1", 0, 0, arf_cyclic
]
	],

	["process_fuck_01_0", 0, 0,
		[3.0, "process_fuck_01", 0, 0, arf_cyclic
]
	],

	["process_fuck_01_1", 0, 0,
		[3.0, "process_fuck_01_1", 0, 0, arf_cyclic
]
	],

	["process_fuck_01_2", 0, 0,
		[3.0, "process_fuck_01_2", 0, 0, arf_cyclic
]
	],

	["process_fuck_01_3", 0, 0,
		[3.0, "process_fuck_01_3", 0, 0, arf_cyclic
]
	],

	["process_fuck_01_4", 0, 0,
		[3.0, "process_fuck_01_4", 0, 0, arf_cyclic
]
	],

	["process_fuck_01_5", 0, 0,
		[3.0, "process_fuck_01_5", 0, 0, arf_cyclic
]
	],

	["process_fuck_02", 0, 0,
		[3.0, "process_fuck_02", 0, 0, arf_cyclic
]
	],

	["process_fuck_03", 0, 0,
		[3.0, "process_fuck_03", 0, 0, arf_cyclic
]
	],

	["process_fuck_04", 0, 0,
		[3.0, "process_fuck_04", 0, 0, arf_cyclic
]
	],

	["process_fuck_05", 0, 0,
		[3.0, "process_fuck_05", 0, 0, arf_cyclic
]
	],
 ["unused_horse_anim_13", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_14", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_15", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_16", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_17", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_18", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_19", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_20", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_21", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_22", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_23", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_24", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_25", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_26", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_27", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_28", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_29", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_30", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_31", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_32", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_33", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_34", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_35", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_36", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_37", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_38", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_39", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_40", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_41", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_42", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_43", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_44", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_45", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_46", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_47", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_48", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_49", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_50", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_51", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_52", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_53", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_54", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_55", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_56", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_57", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_58", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_59", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_60", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_61", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_62", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_63", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_64", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_65", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_66", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_67", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_68", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_69", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_70", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_71", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_72", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_73", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_74", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_75", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_76", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_77", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_78", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_79", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_80", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_81", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_82", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_83", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_84", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_85", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_86", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_87", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_88", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_89", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_90", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_91", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_92", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_93", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_94", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_95", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_96", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_97", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_98", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_99", 0, 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_100", 0, 0, [1.0, "anim_horse", 0, 1, 0]],

 #taverna hispania1200 Daedalus / Slawomir of Aaarrghh
 ["sitting_drinking_low", acf_enforce_all, amf_priority_die|amf_play,
	[20.0, "dedal_sitting_drinking_low", 0, 311, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],],
 ["sitting_low", acf_enforce_all, amf_priority_die|amf_keep,
	[18.0, "dedal_sitting_low", 3, 301, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],],
 ["lute_sitting", acf_enforce_all, amf_priority_die|amf_play,
	[2.05, "dedal_lute_sitting", 3, 7, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],],
 ["lute_standing", acf_enforce_all, amf_priority_die|amf_play,
	[2.05, "dedal_lute_standing", 3, 7, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],],
 ["lyre_sitting", acf_enforce_all, amf_priority_die|amf_play,
	[2.05, "dedal_lyre_sitting", 3, 7, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],],
 ["lyre_standing", acf_enforce_all, amf_priority_die|amf_play,
	[2.05, "dedal_lyre_standing", 3, 7, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],],





]