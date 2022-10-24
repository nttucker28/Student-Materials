import pytest
import json
import Staff
import System
import User
import Professor

username = 'calyam'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
course = 'cloud_computing'
assignment = 'assignment1'
profUser = 'goggins'
profPass = 'augurrox'

#Tests if the program can handle a wrong username
#Test1
def test_login(grading_system):
    username = 'thtrhg'
    password =  'fhjhjdhjdfh'
    grading_system.login(username,password)

#Test2
def test_check_password(grading_system):
    test = grading_system.check_password(username,password)
    test2 = grading_system.check_password(username,'#yeet')
    test3 = grading_system.check_password(username,'#YEET')
    if test == test3 or test2 == test3:
        assert False
    if test != test2:
        assert False


#Test3
def test_change_grade(grading_system):
    score = 85
    grading_system.login(profUser, profPass)
    grading_system.usr.change_grade('hdjsr7', 'cloud_computing', 'assignment1', score)
    grades = grading_system.usr.check_grades("hdjsr7", "cloud_computing")
    print(grades)
    if grades[0] != score:
        assert False

#Test4
def test_create_assignment(grading_system):
    grading_system.login(profUser, profPass)
    grading_system.usr.create_assignment('new_assignment', '10/31/22', 'cloud_computing')
    assignment == grading_system.usr.all_courses['cloud_computing']['assignments']['new_assignment']['due_date']
    if assignment == '10/31/22':
        assert True
    else:
        assert False


#Test5
def test_add_student(grading_system):
    grading_system.login(profUser, profPass)
    grading_system.usr.add_student('hdjsr7', 'comp_sci')
    try:
        grading_system.login('hdjsr7', 'pass1234')
        grading_system.usr.check_grades("comp_sci")
    except:
        assert False
    else:
        assert True

#Test6
def test_drop_student(grading_system):
    grading_system.login(profUser, profPass)
    grading_system.usr.drop_student('yted91', 'cloud_computing')
    try:
        grading_system.login('yted91', 'imoutofpasswordnames')
        grading_system.usr.check_grades("cloud_computing")
    except:
        assert True
    else:
        assert False


#Test7
def test_submit_assignment(grading_system):
    grading_system.login('hdsrj7', 'pass1234')
    grading_system.usr.submit_assignment('cloud_computing', 'assignment1', 'submission', '10/23/22')
    submitted = grading_system.usr.courses['cloud_computing']['assignment1']['submission_date']
    if submitted == '10/23/22':
        assert True
    else:
        assert False


#Test8
def test_check_ontime(grading_system):
    grading_system.login('hdsrj7', 'pass1234')
    ontime = grading_system.usr.check_ontime('10/23/22', '1/3/20')
    if (ontime):
        assert False

#Test9
def test_check_grades(grading_system):
    grading_system.login('hdsrj7', 'pass1234')
    grades = grading_system.usr.check_grades('cloud_computing')
    if grades[0][1] == grading_system.usr.users['hdsrj7']['courses']['cloud_computing']['assignment1']['grade']:
        assert True
    

#Test10
def test_view_assignments(grading_system):
    grading_system.login('akend3', '123454321')
    assignments = grading_system.usr.view_assignments('comp_sci')
    for assignment in assignments:
        if assignment[0] == 'new_assignment':
            assert True
    else:
        assert False


#Test11
def test_in_course(grading_system):
    grading_system.login('akend3', '123454321')
    if 'cloud_computing' not in grading_system.usr.users['akend3']['courses']:
        assert False

#Test12
def test_has_TA(grading_system):
    grading_system.login(profUser, profPass)
    TA = grading_system.usr.courses['databases']['ta']
    if TA == 'cmhbf5':
        assert True
    else:
        assert False

#Test13
def test_check_course(grading_system):
    grading_system.login(profUser, profPass)
    if 'stats' not in grading_system.usr.courses:
        assert False
    else:
        assert True

#Test14
def test_course_needs_professor(grading_system):
    grading_system.login(profUser, profPass)
    if grading_system.usr.courses['databases']['professor'] != 'none':
        assert False
    else:
        assert True

#Test15
def test_is_failing(grading_system):
    grading_system.login('akend3', '123454321')
    grades = grading_system.usr.check_grades('comp_sci')
    for grade in grades:
        if grade[0][1] < 60:
            assert True
    else:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
