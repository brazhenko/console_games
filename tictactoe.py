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

    def make_turn(self):
        if self.turn_counts % 2 == 1:
            print('Играют: ООО')
            sell = int(input())
            if 0<sell<9 and self.turn_positions[sell] == ' ':
                self.turn_positions[sell] = 'O'
                self.turn_counts += 1

        else:
            print('Играют: XXX')
            sell = int(input())
            if 0<=sell<9 and self.turn_positions[sell] == ' ':
                self.turn_positions[sell] = 'X'
                self.turn_counts += 1

    def field_print(self, a=turn_positions):
        print('''
		   ___________
		  |0  |1  |2  |
		  | {} | {} | {} |
		  |___|___|___|
		  |3  |4  |5  |
		  | {} | {} | {} |
		  |___|___|___|
		  |6  |7  |8  |
		  | {} | {} | {} |
		  |___|___|___|		  
				'''.format
                                   (a[0], a[1], a[2],
                                   a[3], a[4], a[5],
                                   a[6], a[7], a[8])
              )



def main():
    x = Field()
    x.field_print()
    print('Играем в крестики нолики. Для хода введите номер клетки.')
    while x.is_game_finished()[1] == False:
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        x.make_turn()
        x.field_print()
    print(x.is_game_finished()[0])
    input('Игра закончена. Нажмите любую клавишу для выхода')
main()