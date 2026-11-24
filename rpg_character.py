full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):
    if type(name) != str:
        return 'The character name should be a string.'
    if name == '':
        return 'The character should have a name.'
    if len(name) > 10:
        return 'The character name is too long.'
    if  ' ' in name:
        return 'The character name should not contain spaces.'
    stats = [strength, intelligence, charisma]
    if any(type(s) != int for s in stats):
        return 'All stats should be integers.'
    if any(s < 1 for s in stats):
        return 'All stats should be less than 1'
    if any(s > 4 for s in stats):
        return 'All stats should be more than 4'
    if sum(stats) != 7:
        return 'The character should start with 7 points'
    str_line = 'STR ' + full_dot * strength + empty_dot * (10 - strength)
    int_line = 'INT ' + full_dot * intelligence + empty_dot * (10 - intelligence)
    cha_line = 'CHA ' + full_dot * charisma + empty_dot * (10 - charisma)
    return '\n'.join([name, str_line, int_line, cha_line])
print('ren', 4, 2, 1)