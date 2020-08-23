# coding=utf-8
def auto_check_in(stuid, pwd, debug = 1, show = 0):
    import time # delay
    
    try:
        from selenium import webdriver
    except:
        print("Please run \"pip install selenium\" to install the selenium package")
        driver.quit()
        return 0
    else:
        if debug ==1 :print("Detected selenium part...")
    
    if show==0:
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome("chromedriver", options=chrome_options)
    else:
        driver = webdriver.Chrome("chromedriver")
    
    driver.get("https://ehall.neu.edu.cn/infoplus/form/JKXXSB/start")
    if debug == 1:print("Waiting for 3 seconds..")
    time.sleep(8)

    try:
        driver.find_element_by_xpath('/html/body/div[2]/div/form/div/div[1]/input[1]').send_keys(str(stuid))
        driver.find_element_by_xpath("/html/body/div[2]/div/form/div/div[1]/input[2]").send_keys(str(pwd))
        driver.find_element_by_xpath("/html/body/div[2]/div/form/div/div[1]/span/input").click()
        if debug==1 :print("Loging in...")
        time.sleep(1)
        try:
            driver.find_element_by_xpath('/html/body/div/main/div/form/div[1]/table/tbody/tr/td[1]/div/div/div/label[1]/span[1]/span').click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div/main/div/form/div[3]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]/span[1]/span').click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div/main/div/form/div[4]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]/span[1]/span').click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div/main/div/form/div[6]/button/span').click()
            time.sleep(3)
        except:
            if debug==1 :print("Failed to jump...")
            driver.quit()
            return 0
        else:
            if debug==1 : print("Jumping...")

    except:
        print("Error...\nExiting...")
        if debug==1 :print("The page has been changed...\nThe programming do not be useful until it has been updated...")
        return 0
    else:
        if debug==1 : print("Submitting...")

    try:
        text = driver.find_element_by_xpath('/html/body/div/main/div/div/div/div/div[1]').text
    except:
        print("Error happens!\nFailed to check in...\nexiting")
        return 0
    else:
        print("return:", text)
    driver.quit()
    return 1
