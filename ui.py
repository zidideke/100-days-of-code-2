from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"



class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain): #quiz_brain: QuizBrain this means you showing the type of data you want passed in which is a quizBrain
        self.quiz =quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.score_label=Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Something",width=280, font=("Arial", 15, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50) # the pad here will give more space on the up yaxis

        self.check_img=PhotoImage(file="true.png")
        self.cross_img=PhotoImage(file="false.png")

        self.check_button=Button(image= self.check_img, highlightthickness=0, command=self.true_button)
        self.check_button.grid(column=0, row=2)

        self.cross_button=Button(image= self.cross_img, highlightthickness=0,command=self.false_button)
        self.cross_button.grid(column=1, row=2)

        self.get_next_question() #call here because outside of the mainloop won't execute untill the window is closed

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white") #when placed here the background will remain white
        if self.quiz.still_has_questions():   #this checks for unanswered questions
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text= "You've reached the end of quiz ")
            self.cross_button.config(state= "disabled")  #disables button from being pressed when the quiz ends
            self.check_button.config(state= "disabled")

    def true_button(self):
        is_right=self.quiz.check_answer("True") #wheb the function is called it checks the check_answer and if corrects returns true
        self.give_feedback(is_right)

    def false_button(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:                    #if is_right is true
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

