from selenium import webdriver
import time

driver = webdriver.Chrome()

def test_login_page():
    driver.get('http://www.skillgun.com')
    time.sleep(5)

    mobile = driver.find_element('id','ContentPlaceHolder1_tbPhoneNumber')
    mobile.send_keys('number')
    time.sleep(5)

    email = driver.find_element('id','ContentPlaceHolder1_tbEmail')
    email.send_keys('email id')
    time.sleep(3)

    password = driver.find_element('id','ContentPlaceHolder1_tbPassword')
    password.send_keys('password')
    time.sleep(3)

    check_box = driver.find_element('xpath','//*[@id="lblPolicyAgreement"]')
    check_box.click()
    time.sleep(10)

    login = driver.find_element('xpath','//*[@id="ContentPlaceHolder1_btnLogin"]')
    login.click()
    time.sleep(5)

    assert 'Home' in driver.current_url

def test_skillgun_profilesetting():

    profile = driver.find_element('xpath', '//*[@id="content"]/div/div/div/div/div/div/strong/strong/div[3]/div[3]/a')
    profile.click()

    time.sleep(5)

    assert 'ProfileSetting' in driver.current_url

def test_skillgun_editcontacts():
    edit = driver.find_element('id', 'ContentPlaceHolder1_hlEditContact')
    edit.click()

    time.sleep(5)

    assert 'EditContactDetails' in driver.current_url

def test_skillgun_editingcontacts():
    whatsapp_number=driver.find_element('id','ContentPlaceHolder1_RadioButtonList1_0')
    whatsapp_number.click()


    cur_add_line = driver.find_element('id', 'ContentPlaceHolder1_tbCALine1')
    cur_add_line.clear()  # first remove the current address data
    cur_add_line.send_keys('HSR LAYOUT')

    cur_city = driver.find_element('id', 'ContentPlaceHolder1_tbCACity')
    cur_city.clear()
    cur_city.send_keys('Bengaluru')

    cur_state = driver.find_element('id', 'ContentPlaceHolder1_ddlCAState')
    cur_state.send_keys('Karnataka')

    save = driver.find_element('id', 'ContentPlaceHolder1_btnSubmit')
    save.click()

    time.sleep(5)
    # assert 'Bengaluru' in cur_city.text
    driver.back()

def test_skillgun_editeducational_details():
    education_details = driver.find_element('id','ContentPlaceHolder1_hlEditEducational')
    education_details.click()
    assert 'EducationDetails' in driver.current_url

def test_skillgun_editing_educational_details():
    school_name = driver.find_element('id','schoolname')
    school_name.send_keys('School name')

    year_of_passing = driver.find_element('id','sslc_yop')
    year_of_passing.send_keys('enter of SSC year of passing')

    ssc_percentage = driver.find_element('id','sslc_perc')
    ssc_percentage.send_keys('enter SSC percentage')

    diploma_college_name = driver.find_element('id','diploma_college')
    diploma_college_name.send_keys('enter your college name')

    diploma_year_of_passing = driver.find_element('id','diploma_yop')
    diploma_year_of_passing.send_keys('enter your diploma yop')

    diploma_percentage = driver.find_element('id','diploma_perc')
    diploma_percentage.send_keys('enter your percentage')

    diploma_specialization = driver.find_element('id','diploma_specialization')
    diploma_specialization.send_keys('enter your specialization ')

    college_name = driver.find_element('id','ug_college')
    college_name.send_keys('enter your college name')

    degree = driver.find_element('id','')
    degree.send_keys('enter your degree')

    ug_specialization = driver.find_element('id','')
    ug_specialization.send_keys('enter specialization')

    ug_yop = driver.find_element('id','')
    ug_yop.send_keys('enter your yop')

    ug_percentage = driver.find_element('id','')
    ug_percentage.send_keys('enter your percentage')

    driver.back()

def test_upload_resume():
    update = driver.find_element('id','ContentPlaceHolder1_hlUploadResume')
    update.click()

    assert 'UploadResume' in driver.current_url

def test_uploading_resume():
    browse_resume = driver.find_element('id','ContentPlaceHolder1_btnBrowse')
    browse_resume.click() # browse the resume in your pc to update existing resume

    upload_resume = driver.find_element('id','ContentPlaceHolder1_btnUpload')
    upload_resume.click() # click on upload button to update resume you selected from your pc

    driver.back()

def test_skillgun_profilesetting():
    go_to_home = driver.find_element('xpath','//*[@id="content"]/div[1]/div[1]/div/div/div/div[1]/div[10]/a')
    go_to_home.click()

    assert 'Home' in driver.current_url

def test_logout():
    logout = driver.find_element('xpath','//*[@id="ContentPlaceHolder1_btnLogout"]')
    logout.click()
