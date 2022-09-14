import keyboard as kb

rec = kb.record(until="escape")
seq = kb.get_typed_strings(rec)
print("".join (seq))
trent alexander