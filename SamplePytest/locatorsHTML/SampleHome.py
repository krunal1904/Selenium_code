def einfochips_logo(): return "//img[@class='mk-sticky-logo']"
def Eic_header(i): return "(//span[text()='" + i + "'])[1]"
def Eic_hower(): return "(//span[text()='Domains'])[1]"
def Eic_click(): return "(//span[text()='Semiconductor'])[1]"
def Eic_link(): return "https://www.einfochips.com/domains/semiconductor/"
def Eic_title(): return "Semiconductor Design Services | ASIC/FPGA Design Services"
def Eic_scroll(s):
    if s == 'a':
        return "//h2[text()='Subscribe to Newsletter']"
    if s == 'k':
        return "(//span[contains(.,' Connect')])[3]"
    if s == 'p':
        return "//span[text()='Championing']"

def Eic_plc(): return "//input[@name='email']"
def Eic_plc_name(): return "Business Email"
def Eic_form(k) :
    if k == 'c':
        return "//a[@href='/contact-us/']"
    if k == 'n':
        return "//input[@name='Name']"
    if k == 'e':
        return "//input[@name='email-834']"
    if k == 'num':
        return "//input[@name='tel-224']"
    if k == 'com':
        return "//input[@name='Company']"
    if k == 'comm':
        return "//textarea[@name='textarea-584']"


def form_data(a):
    if a == 'name':
        return 'krunal prajapati'
    if a == 'email':
        return 'krunal.prajapati@einfochips.com'
    if a == 'number':
        return '6353367484'
    if a == 'company':
        return 'einfochips'
    if a == 'comments':
        return 'NA'

def Eic_dropdown(): return "//select[@name='menu-151']"

def Eic_spec(j): return f"(//div[@class='wpb_column vc_column_container vc_col-sm-2'])[{j}]"  # xpath = '//*[@id="w1"]/div[%s]/div/div[2]/h3' % i
                                                                                                      # xpath = '//*[@id="w1"]/div[{}]/div/div[2]/h3'.format(i)
                                                                                                      # xpath = f'//*[@id="w1"]/div[{i}]/div/div[2]/h3'

def Eic_check_src(v):
    if v == 'b':
        return "//img[@alt='Aerospace']"
    if v == 'a':
        return "(//span[text()='Aerospace'])[3]"
