class Field(object):
    turn_positions = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ']
    turn_counts = 0

    def is_game_finished(self, a=turn_positions, i=turn_counts):
        if a[0] == a[1] == a[2] == 'X' \
            or a[3] == a[4] == a[5] == 'X' \
            or a[6] == a[7] == a[8] == 'X' \
            or a[0] == a[3] == a[6] == 'X' \
            or a[1] == a[4] == a[7] == 'X' \
            or a[2] == a[5] == a[8] == 'X' \
            or a[0] == a[4] == a[8] == 'X' \
            or a[2] == a[4] == a[6] == 'X':
            return 'Крестики выиграли', True
        elif a[0] == a[1] == a[2] == 'O' \
            or a[3] == a[4] == a[5] == 'O' \
            or a[6] == a[7] == a[8] == 'O' \
            or a[0] == a[3] == a[6] == 'O' \
            or a[1] == a[4] == a[7] == 'O' \
            or a[2] == a[5] == a[8] == 'O' \
            or a[0] == a[4] == a[8] == 'O' \
            or a[2] == a[4] == a[6] == 'O':
            return 'Нолики выиграли', True
        elif i==9:
            return 'Ничья', True
        else:
            return '', False






    def field_print(self, a=turn_positions):
        print('''
		   ___________
		  |   |   |   |
		  | {} | {} | {} |
		  |___|___|___|
		  |   |   |   |
		  | {} | {} | {} |
		  |___|___|___|
		  |   |   |   |
		  | {} | {} | {} |
		  |___|___|___|		  
						'''.format(a[0], a[1], a[2],
                                   a[3], a[4], a[5],
                                   a[6], a[7], a[8]))


x = Field()
x.field_print()
