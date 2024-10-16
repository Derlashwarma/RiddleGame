class FiniteStateMachine:
    def __init__(self, initial_state, states):
        self.state = initial_state
        self.states = states
        self.previous_state = []

    def transition(self, answer):
        current_state = self.states[self.state]

        if answer in current_state['on']:
            self.previous_state.append(self.state)
            self.state = current_state['on'][answer]
            print(f"Transitioning to {self.state}")
        else:
            if self.previous_state:
                self.state = self.previous_state.pop()
                print(f"Wrong!!!! going back to state {self.state}")
            else:
                print('Staying in the first riddle lol')


    def get_current_riddle(self):
        return self.states[self.state]['riddle']

    def is_game_over(self):
        return self.state == 'win'

states = {
    'riddle1': {
        'riddle': 'I have a head and a tail but no body. What am I?',
        'on': {
            'coin': 'riddle2'
        }
    },
    'riddle2': {
        'riddle': 'The more you take, the more you leave behind. What am I?',
        'on': {
            'footsteps': 'riddle3'
        }
    },
    'riddle3': {
        'riddle': 'I am tall when I am young and short when I am old. What am I?',
        'on': {
            'candle': 'riddle4'
        }
    },
    'riddle4': {
        'riddle': 'What gets wetter as it dries?',
        'on': {
            'towel': 'riddle5'
        }
    },
    'riddle5':{
        'riddle':'What has hands but cannot clap?',
        'on':{
            'clock': 'win'
        }
    },
    'win': {
        'riddle': 'Congratulations, you successfuly escaped JOJO\'s RIDDLE DUNGEON!'
    }
}

riddle_game = FiniteStateMachine('riddle1', states)

def play_riddle_game():
    print('Welcome to JOJO\'s RIDDLE DUNGEON! Answer all the riddles to ESCAPE.')
    while not riddle_game.is_game_over():
        current_riddle = riddle_game.get_current_riddle()
        answer = input(current_riddle + " ")  
        riddle_game.transition(answer)

    print(riddle_game.get_current_riddle())

play_riddle_game()
