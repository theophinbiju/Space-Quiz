from flask import Flask,render_template,request, session
app = Flask(__name__)
app.config["SECRET_KEY"]="Hello"



@app.route("/theo")
def theo():
    return render_template("Quiz.html")

@app.route("/new")
def new():
    user_option = request.args['lang']
    correct_answer = 'python'
    message = ''
    if user_option == correct_answer:
        message = 'correct answer'
    else:
        message = 'wrong answer'

    return render_template('Quiz.html',output=message)


@app.route("/square")
def square():
    session["Location"]="Sharjah"
    return render_template('Practice/square.html')

@app.route("/square2")
def square2():
    product = int(request.args.get('square'))
    squared = product**2

    return render_template('square.html', squared=squared)

@app.route("/Table")
def table():
    return render_template('tables.html')

@app.route("/Table2")
def table2():
    multiply=[1,2,3,4,5,6,7,8,9,10]
    times=[]
    number = int(request.args.get('number'))
    for i in multiply:
        times.append(number*i)

    return render_template('tables.html', times=times)



@app.route("/Space")
@app.route("/")
def space():
    session.clear()
    return render_template('Space_home.html')

@app.route("/Space2")
def space2():
    return render_template('descriptive/descriptive.html')    

@app.route("/Space3")
def space3():
    score = session.get('user_score',0)
    answer = ['Black Hole', 'Black hole', 'black Hole', 'black hole', 'BLACK HOLE']
    input = request.args.get('black')

    if input in answer:
        score = score+10
        session['user_score']=score
        print(score)
        #session={'user_score':10}
        return render_template('descriptive/correct.html')
        
    else:
        score = score-5
        session['user_score']=score
        #session={'user_score':-5}
        return render_template('descriptive/wrong.html')


@app.route('/Space1a')
def space1a():
    return render_template('descriptive/descriptive2.html') 

@app.route('/Space1b')
def space1b():
    answer1 = ['Moon', 'moon', 'MOON']
    input1 = request.args.get('moon')
    score = session.get('user_score',0)

    if input1 in answer1:
        score = score+10
        session['user_score']=score
        return render_template('descriptive/correct2.html')
        
    else:
        score = score-5
        session['user_score']=score
        return render_template('descriptive/wrong2.html')
        


@app.route('/Space2a')
def space2a():
    return render_template('descriptive/descriptive3.html') 

@app.route('/Space2b')
def space2b():
    answer2 = ['Hydra', 'hydra', 'HYDRA']
    input2 = request.args.get('hydra')
    score = session.get('user_score',0)

    if input2 in answer2:
        score = score+10
        session['user_score']=score
        return render_template('descriptive/correct3.html')
        
    else:
        score = score-5
        session['user_score']=score
        return render_template('descriptive/wrong3.html')        


@app.route('/Space3a')
def space3a():
    return render_template('descriptive/descriptive4.html')

@app.route('/Space3b')
def space3b():
    answer3 = ['76 Years', '76 YEARS', '76 years', '76', 'Seventy Six Years' 'Seventy six years', 'SEVENTY SIX YEARS', 'seventy six years']
    input3 = request.args.get('76')
    score = session.get('user_score',0)

    if input3 in answer3:
        score = score+10
        session['user_score']=score
        return render_template('descriptive/correct4.html')
        
    else:
        score = score-5
        session['user_score']=score
        return render_template('descriptive/wrong4.html')
        

@app.route('/Space4a')
def space4a():
    return render_template('descriptive/descriptive5.html')

@app.route('/Space4b')
def space4b():
    answer4 = ['Mars', 'MARS', 'mars']
    input4 = request.args.get('mars')
    score = session.get('user_score',0)

    if input4 in answer4:
        score = score+10
        session['user_score']=score
        return render_template('descriptive/correct5.html')
        
    else:
        score = score-5
        session['user_score']=score
        return render_template('descriptive/wrong5.html')
        


@app.route('/Space5a')
def space5a():
    return render_template('descriptive/descriptive6.html')

@app.route('/Space5b')
def space5b():
    answer5 = ['Supernova', 'SUPERNOVA', 'supernova', 'Super Nova', 'SUPER NOVA', 'super nova']
    input5 = request.args.get('nova')
    score = session.get('user_score',0)

    if input5 in answer5:
        score = score+10
        session['user_score']=score
        return render_template('descriptive/correct6.html')
        
    else:
        score = score-5
        session['user_score']=score
        return render_template('descriptive/wrong6.html')
        


@app.route('/scores')
def scores():
    score=session.get('user_score',0)
    if score<=10:
        return render_template('try_again.html')

    else:
        return render_template('great_job.html') 



@app.route('/Choice')
def choice():
    return render_template('multiple_choice/multiple.html')

@app.route('/Choice2')
def choice2():
    user_option = request.args.get('opt')
    correct = 'black'
    score = session.get('user_score',0)
    print(score)

    if user_option == correct:
        score = score+10
        session['user_score']=score
        return render_template('multiple_choice/correct_1.html')

    else:
        score = score-5
        session['user_score']=score
        return render_template('multiple_choice/wrong_1.html')  

@app.route('/Choice2a')
def choice2a():
    return render_template('multiple_choice/multiple2.html')

@app.route('/Choice2b')
def choice2b():
    user_option = request.args.get('opt')
    correct = 'moon'
    score = session.get('user_score',0)

    if user_option == correct:
        score = score+10
        session['user_score']=score
        return render_template('multiple_choice/correct_2.html')

    else:
        score = score-5
        session['user_score']=score
        return render_template('multiple_choice/wrong_2.html') 

@app.route('/Choice3a')
def choice3a():
    return render_template('multiple_choice/multiple3.html')

@app.route('/Choice3b')
def choice3b():
    user_option = request.args.get('opt')
    correct = 'hydra'
    score = session.get('user_score',0)

    if user_option == correct:
        score = score+10
        session['user_score']=score
        return render_template('multiple_choice/correct_3.html')

    else:
        score = score-5
        session['user_score']=score
        return render_template('multiple_choice/wrong_3.html') 

@app.route('/Choice4a')
def choice4a():
    return render_template('multiple_choice/multiple4.html')

@app.route('/Choice4b')
def choice4b():
    user_option = request.args.get('opt')
    correct = 'seven'
    score = session.get('user_score',0)

    if user_option == correct:
        score = score+10
        session['user_score']=score
        return render_template('multiple_choice/correct_4.html')

    else:
        score = score-5
        session['user_score']=score
        return render_template('multiple_choice/wrong_4.html') 

@app.route('/Choice5a')
def choice5a():
    return render_template('multiple_choice/multiple5.html')

@app.route('/Choice5b')
def choice5b():
    user_option = request.args.get('opt')
    correct = 'mons'
    score = session.get('user_score',0)

    if user_option == correct:
        score = score+10
        session['user_score']=score
        return render_template('multiple_choice/correct_5.html')

    else:
        score = score-5
        session['user_score']=score
        return render_template('multiple_choice/wrong_5.html')  

@app.route('/Choice6a')
def choice6a():
    return render_template('multiple_choice/multiple6.html')

@app.route('/Choice6b')
def choice6b():
    user_option = request.args.get('opt')
    correct = 'super'
    score = session.get('user_score',0)

    if user_option == correct:
        score = score+10
        session['user_score']=score
        return render_template('multiple_choice/correct_6.html')

    else:
        score = score-5
        session['user_score']=score
        return render_template('multiple_choice/wrong_6.html')  


@app.route('/Lightning')
def lightning():
    return render_template('Lightning.html')

@app.route('/Lightning_quiz')
def quiz():
    return render_template('Lightning_quiz.html')   

@app.route('/Lightning_quiz_2')
def quiz2():
    return render_template('Lightning_quiz2.html')

@app.route('/Lightning_quiz_3')
def quiz3():
    return render_template('Lightning_quiz3.html')

@app.route('/Verify')
def verify():
    user_opt = request.args.get('opt')
    correct_opt = 'opt4'
    output=''
    if user_opt == correct_opt:
        output = 'CORRECT ANSWER'

    else:
        output = 'WRONG ANSWER'

    return render_template('Lightning_quiz.html', output=output) 

@app.route('/Verify_2')
def verify_2():
    user_opt = request.args.get('opt')
    correct_opt = 'opt2'
    output=''
    if user_opt == correct_opt:
        output = 'CORRECT ANSWER'

    else:
        output = 'WRONG ANSWER'

    return render_template('Lightning_quiz2.html', output=output) 

@app.route('/Verify_3')
def verify_3():
    user_opt = request.args.get('opt')
    correct_opt = 'opt2'
    output=''
    if user_opt == correct_opt:
        output = 'CORRECT ANSWER'

    else:
        output = 'WRONG ANSWER'

    return render_template('Lightning_quiz3.html', output=output)      


@app.route('/Lower', methods = ['GET'])
def lower():
    return render_template('Practice/lower_detect.html')

@app.route('/Lower_detect', methods = ['POST'])
def lower_det():
    user_opt = request.form.get('word')
    lowercase_letter = 0
    for i in user_opt:
        if i.islower():
            lowercase_letter = lowercase_letter+1
    output = lowercase_letter 
    return render_template('Practice/lower_detect.html', output=output) 


@app.route('/Countries')
def countries():
    countries_list=["India","America","Canada","New Zealand","Zimbabwe","Congo"]
    return render_template('Practice/countries.html', countries=countries_list)      


users=["Theophin", "Sam", "Johan", "Samjon", "John"]

@app.route('/Register_Page')
def Register_Page():
    return render_template("Registration_Page/Registration.html")

@app.route('/Register', methods = ['POST'])
def Register():
    full_name = request.form.get('full_name')
    print(full_name,350)
    birth = request.form.get('DOB')
    email = request.form.get('email')
    password = request.form.get('pass')
    pass_len = len(password)
    message = ''
    message1 = ''

    if not (full_name or birth  or email or password):
        message = "Please fill in your details"

    else:    
        if full_name in users:
            message = "You are already signed in"
            
        else:
            if pass_len<8:
                message1 = "You need minimum 8 characters for a password"
            else:
                message = "Login Successful"   


    return render_template("Registration_Page/Registration.html", message=message, message1=message1)


@app.route('/Shipping')
def Shipping():
    return render_template("Practice/Shipping.html")

@app.route('/Shipping_Check')
def Shipping_Check():
    weight = int(request.args.get('weight'))
    cost = 0

    if weight == 20:
        cost = 10*weight
    elif weight>=10 and weight<20:
        cost = 12*weight
    elif weight>=1 and weight<10: 
        cost = 14*weight 
    elif weight<1:
        cost = "Your Package Will Be Sent For Free :)"
    elif weight>20:
        cost = "Sorry, weight should be below 20kg"

    return render_template("Practice/Shipping.html", cost=cost)    


if __name__=='__main__':
    app.run(debug=True)