from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = '#2F4F4F'
FONT = ('Arial', 16, 'italic')


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('QuizBrain')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_block = Label(text=f'Score: 0',
                                 font=FONT, fg='white',
                                 bg=THEME_COLOR)
        self.score_block.grid(column=1, row=0)

        self.question_block = Canvas(height=250, width=300, bg='white')
        self.question_text = self.question_block.create_text(
            150, 125,
            text='Question',
            font=FONT,
            width=280)
        self.question_block.grid(column=0, row=1, columnspan=2, pady=30)

        true_img = PhotoImage(file='./images/true.png')
        self.true_btn = Button(image=true_img,
                               highlightthickness=0,
                               command=self.true_click)
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file='./images/false.png')
        self.false_btn = Button(image=false_img,
                                highlightthickness=0,
                                command=self.false_click)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score_block.config(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
        self.question_block.config(bg='white')

        if self.quiz.still_has_question():
            q_text = self.quiz.next_question()
            self.question_block.itemconfig(self.question_text, text=q_text)
        else:
            self.question_block.itemconfig(self.question_text, text='The end of Quiz')
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')



    def true_click(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_click(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.question_block.config(bg='#3CB371')
        else:
            self.question_block.config(bg='#DC143C')

        self.window.after(1000, self.get_next_question)
