Mount&Blade Module System

For getting documentation and the latest version of the module system check out:

www.taleworlds.com/mb_module_system.html

Modifications by Lav:

  * It is possible to add items with modifiers to troop inventories. For example,
    [(itm_item1, imod_rusty), itm_item2] will add rusty "itm_item1" and regular
    "itm_item2". This is a slightly modified version of The_dragon's code from
    http://forums.taleworlds.com/index.php/topic,309179.msg7331722.html#msg7331722

  * Temporary *.pyc files are no longer generated during compilation and won't
    clutter the folder in case of a failed compilation attempt.

  * Info page references "ip_*" are now correctly recognized by module system
    compiler and will not throw an "Unrecognized tag" error.

  * New 1.165 operations (try_for_prop_instances) and (try_for_players) are now
    correctly identified as "depth-increasing" operations.

  * Modifications to "header_common.py" enable numeric, string and position
    registers up to reg127, s127 and pos127 respectively. Note that numeric and
    string registers with indexes of 100 and higher cannot be used in string
    substitutions.

  * Modifications to "header_item_modifiers.py" to include information on item
    modifier hardcoded game effects and make imodbit_* constants more readable.

  * Various modifications to "header_items.py":

    * Item weight can now go up to 4096 kg with very high precision. Note that
      the game engine will round displayed weight to nearest 0.1 anyway.

    * Item other parameters will no longer overflow into hit_points field,
      resulting in items with ridiculously high HP value (which is usually
      meaningless and harmless though).

    * Item max_ammo value can now go up to 65535 (compared to vanilla 255).

  * Modifications to "header_skills.py" get rid of uncomprehensibly big numbers
    and extend knows_* constants to include skill levels up to 15.

  * Modifications to "header_troops.py" provide attribute constants for
    attributes in [3..64) range (upper value not included).

  * Modifications to "header_triggers.py" to provide more detailed information
    on triggers parameters.

  * File "header_operations.py" has been completely replaced with properly
    documented version.

  * Added a small tweak to "module_info.py" which will provide a trailing slash
    to export_dir constant if it doesn't have one. Also provided several
    commented possible values for export_dir setting.

  * All inconsistent code that was found by W.R.E.C.K. compiler in Native
    sources has been fixed while preserving full savegame-compatibility with
    vanilla Native. A number of strings that had been incorrectly named have
    been fixed. Duplicate copies of items and strings have been renamed with
    the "_DUPLICATE" suffix.
