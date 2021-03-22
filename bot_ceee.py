from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import sys

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(
    executable_path=r'C:\Users\Samsung\Desktop\geckodriver.exe',
    options=options)
driver.get(
    'https://www.ceee.com.br/prj_pc_Desligamento/faces/DesligProgramado.xhtml')
wait = WebDriverWait(driver, 40)

numero_xpath_rua = range(1, 81)
numero_rua = range(1, 81)


def selecao(exp_sel, sel_poa, cidade_sel):
    try:
        expandir_selecao = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, exp_sel))).click()
        time.sleep(2)
        selecao_poa = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, sel_poa))).click()
        time.sleep(3)
        cidade_selecionada = driver.find_element_by_xpath(cidade_sel)
        if cidade_selecionada.text != "PORTO ALEGRE":
            print("Porto Alegre não foi selecionada.")
            driver.quit()
            return sys.exit()
    except TimeoutException:
        print("Link fora do ar ou elementos não foram encontrados no tempo determinado.")
        driver.quit()
        return sys.exit()


def ruas(number, body_pattern, rua_x, date, hour, rua_y):
    for x in number:
        try:
            rua = driver.find_element_by_xpath(body_pattern + str(x) + rua_x)
            for item in lista_rua:
                if item in rua.text:
                    print(r'***************************************')
                    data = driver.find_element_by_xpath(
                        body_pattern + str(x) + date)
                    hora = driver.find_element_by_xpath(
                        body_pattern + str(x) + hour)
                    for y in numero_rua:
                        try:
                            nome_rua = driver.find_element_by_xpath(
                                body_pattern + str(x) + rua_y + str(y) + "]")
                            if item in nome_rua.text:
                                print(
                                    data.text, hora.text, nome_rua.text, sep='\n')
                                break
                        except NoSuchElementException:
                            break
                    print(r'***************************************')
        except NoSuchElementException:
            print('Fim da análise')
            driver.quit()
            break


# DICIONÁRIO XPATH
xpath = {
    "body_pattern": r"/html/body/div[2]/div[3]/div/div/ul/li[",
    "date": r"]/span[1]",
    "hour": r"]/span[2]",
    "exp_sel": r"/html/body/div[2]/div[2]/div/form/div/div/div[3]/span",
    "sel_poa": r"/html/body/div[5]/div/ul/li[55]",
    "rua_x": r"]/table/tbody/tr[4]/td[2]",
    "cidade_selecionada": r'//*[@id="j_idt14:municipio_label"]',
    "rua_y": r"]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/div/div/ul/li["
}

# LISTA DAS RUAS
lista_rua = [
    'MARGARIDA',
    'FURRIEL',
    'JOAO CAETANO',
    'RAIMUNDO CORREA',
    'KOSERITZ',
    'BAGE',
    'LAGEADO',
    'FELIX DA CUNHA',
    'EDUARDO CHARTIER',
    'COUFAL',
    'CARLOS BARBOSA',
    'CIRO GAVIÃO',
    'JURUA',
    'ITAJAI',
    'LAURINDO',
    'TEREZINHA',
    'MORENO LOUREIRO',
    'MEIRELLES',
    'FRANCISCO TREIN']

# CHAMANDO AS FUNÇÕES
selecao(
        xpath["exp_sel"],
        xpath["sel_poa"], 
        xpath["cidade_selecionada"])
        
ruas(
    numero_xpath_rua,
    xpath["body_pattern"],
    xpath["rua_x"],
    xpath["date"],
    xpath["hour"],
    xpath["rua_y"])
