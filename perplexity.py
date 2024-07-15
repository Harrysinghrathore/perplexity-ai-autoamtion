# try:
import requests
from bs4 import BeautifulSoup
# import lxml
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
import pickle
drive = Driver(uc=True, headed=True)


drive.get('https://www.perplexity.ai/')
# drive.
time.sleep(2)
drive.delete_all_cookies()
time.sleep(2)
cookies = pickle.load(open('cookies.pkl', 'rb'))
for cookie in cookies:
    cookie['domain'] = '.perplexity.ai'
    try:
        drive.add_cookie(cookie)
    except Exception as e:
        print('hfds cookie', e)
        # pass
        print(cookie)
# time.sleep(5)
drive.get('https://www.perplexity.ai/')
time.sleep(3)






# driver.delete_all_cookies()
# drive.get('https://www.perplexity.ai/')
# drive.get(asd)
# time.sleep(130so)
# login_btn_perpex = drive.find_element(By.XPATH,'/html/body/div/main/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/button')
# login_btn_perpex.click()
# email_inpu_perplex = drive.find_element(By.XPATH, '/html/body/div/main/div[3]/div/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/input')
# email_inpu_perplex.send_keys('admin@runningnosedr.com')
# continue_with_email_btn = drive.find_element(By.XPATH, '/html/body/div/main/div[3]/div/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/button/div/div')
# continue_with_email_btn.click()
# time.sleep(100)
# pickle.dump(drive.get_cookies(), open('cookiesperplex.pkl', 'wb'))
try:

    new_thread_btn = drive.find_element(By.XPATH, '/html/body/div/main/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]')
    new_thread_btn.click()
    time.sleep(3)
    print('th')
    focus_button = drive.find_element(By.CSS_SELECTOR,
                                      '#__next > main > div.fixed.bottom-0.left-0.right-0.top-0.z-30.flex.items-center.justify-center > div > div > div > div > span > div > div > div.bg-background.dark\:bg-offsetDark.flex.rounded-l-lg.col-start-1.row-start-2.-ml-2 > div:nth-child(1) > span > button')
    focus_button.click()
    time.sleep(4)
    print('foc')
    academic = drive.find_element(By.XPATH, '/html/body/div/main/div[3]/div/div/div/div/div/div[2]/div/div/div[1]')
    academic.click()
    time.sleep(4)
    file_input = drive.find_element(By.XPATH,
                                    '//*[@id="__next"]/main/div[3]/div/div/div/div/span/div/div/div[1]/div[2]/input')
    # file_input.send_keys('/Users/maweni/Desktop/Perplexity/Sample of MCQ´s.pdf')
    file_input.send_keys('/home/harshwardhan-singh-r/Downloads/Sample of MCQ´s.pdf')
    time.sleep(2)

    inp = drive.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div/div/div/div/span/div/div/textarea')

    inp.send_keys(f"the most important thing is give me only one statement like this and follow the pattern which is mentioned in this statement, Task Instructions: 1. Rewrite the Question: Rewrite the provided question to imitate the format used in the EBEORL-HNS examination. Make them more challenging than they currently are, at the level of an attending otolaryngologist, creating new plausible distractors. Refer to the attached PDF for examples of past questions to ensure the format is consistent. 2. Identify the Subspecialty: At the top of the question, indicate the Otolaryngology subspecialty it belongs to. The options are: Embryology, Research, Microbiology, Physiology, Anatomy, Rhinology, Otology, Paediatric ENT, Laryngology, Facial Plastics, Head and Neck. 3. Identify the Correct Answer: Clearly state the correct answer to the rewritten question. 4. Expand the Explanation: Enhance the explanation to make it more insightful and helpful for learners. This should include: - A detailed and thorough explanation of the answer. - Links to further reading materials that are relevant and reliable. Ensure that the links are present and work. - Additional aspects or concepts related to the question that will aid candidates in their understanding and preparation. Question: [Insert rewritten question here with plausible distractors] Subspecialty: [Insert relevant subspecialty here] Correct Answer: [Insert correct answer here with the option alphabet in front of the answer like a, b, c,d,e,f] Explanation:  [Insert detailed and thorough explanation of the answer here] Further Reading: [Insert links to relevant and reliable reading materials here] Additional Concepts: [Insert additional aspects or related concepts here]. Which advanced hearing aid feature is particularly effective in enhancing speech recognition in noisy environments by focusing on the direction of the sound source?, options are")
    # print(f"{task_instruction} {question} {explanation} {final_options}")
    # inp.send_keys('most important thing is give me only one statement like this and follow the pattern which is mentioned in this statement, Task Instructions: 1. Rewrite the Question: Rewrite the provided question to imitate the format used in the EBEORL-HNS examination. Make them more challenging than they currently are, at the level of an attending otolaryngologist, creating new plausible distractors. Refer to the attached PDF for examples of past questions to ensure the format is consistent. 2. Identify the Subspecialty: At the top of the question, indicate the Otolaryngology subspecialty it belongs to. The options are: Embryology, Research, Microbiology, Physiology, Anatomy, Rhinology, Otology, Paediatric ENT, Laryngology, Facial Plastics, Head and Neck. 3. Identify the Correct Answer: Clearly state the correct answer to the rewritten question. 4. Expand the Explanation: Enhance the explanation to make it more insightful and helpful for learners. This should include: - A detailed and thorough explanation of the answer. - Links to further reading materials that are relevant and reliable. Ensure that the links are present and work. - Additional aspects or concepts related to the question that will aid candidates in their understanding and preparation. <div><div class="prose dark:prose-invert inline leading-normal break-words min-w-0 [word-break:break-word]"><span>Question: [question here]</span><span><br></span><span> </span><span>a.[options here]</span><span><br></span><span> b. [options here]</span><span><br></span><span> c. [options here]</span><span><br></span><span> d. [options here]</span><span><br></span><span> e. [options here]</span><span class="mt-md block"></span> <span>Subspecialty: [subspecialty here]</span><span class="mt-md block"></span> <span>Correct Answer: d. [correct answer here]</span><span class="mt-md block"></span> <span>Explanation:</span><span><br></span><span> [explanation here]</span><span class="mt-md block"></span> <span>Further Reading:</span> <ul class="list-disc pl-8"> <li>[reading here]</li> <li [readings here]</li> </ul> <span>Additional Concepts:</span> <ul> <li> [additional concepts here] </li> <li>[additional concepts here]</li> <li>[additional concepts here]</li> </ul></div></div> Which hearing aid option is considered most suitable for a patient who requires high levels of amplification and has issues with feedback? CIC hearing aid Open-fit BTE hearing aid Analogue ITE hearing aid Bodyworn hearing aid BAHA'
    # )
    time.sleep(2)
    print('inp')
    try:
        entre = drive.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div/div/div/div/span/div/div/div[2]/button')
        entre.click()
    except:
        print('no need')




    time.sleep(40)






    while True:
        # time.sleep(3)
        try:
            if 'Share' not in drive.get_page_source():
                time.sleep(3)
                raise Exception("Sorry, no numbers below zero")
            else:
                total_answers = (BeautifulSoup(drive.get_page_source(), 'html.parser').select_one('.prose'))
            break
        except:
            print('not there')
            pass
        time.sleep(3)
    its = []
    print('start')
    all_spans = []
    print(total_answers)

    soup = total_answers
    # Extracting question
    # if '<h2 class="mb-2 mt-6 text-lg first:mt-3">Question:</h2>' not in
    question_span = soup.find('span', string='Question:')
    # try:
    if question_span:
        # Find the next non-empty span element containing the question text
        next_span = question_span.find_next_sibling('span')
        while next_span and not next_span.get_text(strip=True):
            next_span = next_span.find_next_sibling('span')

        if next_span:
            question = next_span.get_text(strip=True)
            print(question)
        else:
            question = ("Question text not found.ris")
    else:
        # question = ("Question text not found.tw")
        # print("Question label not found.")
        question_span = soup.find('h2', string='Question:')
        if question_span:
            # Find the next non-empty span element containing the question text
            next_span = question_span.find_next_sibling('span')
            while next_span and not next_span.get_text(strip=True):
                next_span = next_span.find_next_sibling('span')

            if next_span:
                question = next_span.get_text(strip=True)
                print(question)
            else:
                question = ("Question text not found.ris")
        else:
            question =' not found '
    # except:


    # Extracting subspecialty

    if soup.find('span', string='Subspecialty:').find_next('span').get_text(strip=True) if soup.find('span', string='Subspecialty:') else None:
        subspecialty = soup.find('span', string='Subspecialty:').find_next('span').get_text(strip=True) if soup.find('span',
                                                                                                                     string='Subspecialty:') else None
    else:
        subspecialty = soup.find('h2', string='Subspecialty:').find_next('span').get_text(strip=True) if soup.find('h2',
                                                                                                                   string='Subspecialty:') else None
    # Extracting correct answer
    if soup.find('span', string='Correct Answer:').find_next('span').get_text(strip=True) if soup.find('span', string='Correct Answer:') else None:
        correct_answer = soup.find('span', string='Correct Answer:').find_next('span').get_text(strip=True) if soup.find('span', string='Correct Answer:') else None
    else:
        correct_answer = soup.find('h2', string='Correct Answer:').find_next('span').get_text(strip=True) if soup.find(
            'h2', string='Correct Answer:') else None
    # # Extracting explanation

    explanation_span = soup.find('span', string='Explanation:')

    # Extract the text from the next sibling span (skipping empty spans)

    if explanation_span:
        explanation_text = ''
        next_sibling = explanation_span.find_next_sibling('span')
        while next_sibling and next_sibling.text.strip() == '':
            next_sibling = next_sibling.find_next_sibling('span')

        # Once a non-empty sibling is found, accumulate its text and subsequent non-empty sibling texts
        while next_sibling and next_sibling.text.strip() != '':
            explanation_text += next_sibling.text.strip() + ' '
            next_sibling = next_sibling.find_next_sibling('span')

        explanation = explanation_text.strip()
    else:
        explanation_span = soup.find('span', string='Explanation:')

        # If the span is found, navigate to the next non-empty sibling span and collect text
        if explanation_span:
            explanation_text = ''
            next_sibling = explanation_span.find_next_sibling('span')
            while next_sibling and next_sibling.text.strip() == '':
                next_sibling = next_sibling.find_next_sibling('span')

            # Once a non-empty sibling is found, accumulate its text and subsequent non-empty sibling texts
            while next_sibling and next_sibling.text.strip() != '':
                explanation_text += next_sibling.text.strip() + ' '
                next_sibling = next_sibling.find_next_sibling('span')

            explanation = explanation_text.strip()
        else:
            explanation_span = soup.find('h2', string='Explanation:')

            # If the span is found, navigate to the next non-empty sibling span and collect text
            if explanation_span:
                explanation_text = ''
                next_sibling = explanation_span.find_next_sibling('span')
                while next_sibling and next_sibling.text.strip() == '':
                    next_sibling = next_sibling.find_next_sibling('span')

                # Once a non-empty sibling is found, accumulate its text and subsequent non-empty sibling texts
                while next_sibling and next_sibling.text.strip() != '':
                    explanation_text += next_sibling.text.strip() + ' '
                    next_sibling = next_sibling.find_next_sibling('span')
                explanation = explanation_text.strip()

                print("Explanation:", explanation_text.strip())
            else:
                explanation = 'none'


    # import pdb
    # pdb.set_trace()

    additional_concepts = []


    # Find the span with strong tag containing "Additional Concepts:"
    additional_concepts_span = soup.find('span', string='Additional Concepts:')

    # Navigate to the ul tag following the span
    if additional_concepts_span:
        ul_tag = additional_concepts_span.find_next('ul', class_='list-disc')
        if ul_tag:
            # Save the HTML of Additional Concepts section as a variable
            additional_concepts_html = str(ul_tag)

            # Extract all text from the saved HTML
            additional_concepts_text = ul_tag.get_text(separator='\n', strip=True)
            additional_concepts = additional_concepts_text

    else:
        additional_concepts_span = soup.find('h2', string='Additional Concepts:')
        if additional_concepts_span:
            ul_tag = additional_concepts_span.find_next('ul', class_='list-disc')
            if ul_tag:
                # Save the HTML of Additional Concepts section as a variable
                additional_concepts_html = str(ul_tag)

                # Extract all text from the saved HTML
                additional_concepts_text = ul_tag.get_text(separator='\n', strip=True)
                additional_concepts = additional_concepts_text
    # Create the dictionary
    further_reading_links = []
    further_reading_items = soup.find('span', string='Further Reading:').find_next('ul').find_all('a') if soup.find('span', string='Further Reading:') else []
    if further_reading_items:
        for item in further_reading_items:
            further_reading_links.append(item['href'])
    else:
        further_reading_items = soup.find('h2', string='Further Reading:').find_next('ul').find_all('a') if soup.find(
            'h2', string='Further Reading:') else []
        if further_reading_items:
            for item in further_reading_items:
                further_reading_links.append(item['href'])
    extracted_info = {
        'Question': question,
        'Subspecialty': subspecialty,
        'Correct Answer': correct_answer,
        'Explanation': explanation,
        'Further Reading': further_reading_links,
        'Additional Concepts': additional_concepts
    }
    print(extracted_info)
    time.sleep(4)
    # adder = Driver(uc=True, headed=True)

except Exception as e:
    print(e)
    time.sleep(10000)


