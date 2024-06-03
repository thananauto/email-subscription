import re, pytest
from playwright.sync_api import Page, expect

from read_csv import get_file_data, conf


@pytest.mark.parametrize("site", get_file_data())
def test_subscribe(page: Page, site):
    url = site.strip()
    page.goto(f'https://{url}', wait_until='domcontentloaded')
    # hardwait for all scenarios to be laaded
    page.wait_for_timeout(10000)

    email_button = page.get_by_role('textbox', name=re.compile(r"mail", re.IGNORECASE))
    email_button1 = page.get_by_placeholder(re.compile(r"mail", re.IGNORECASE))
    # get the list email textbox in homepage itself
    final_textbox = [*email_button.all(), *email_button1.all()]   
    textbox = wait_for_textbox_visible(text_box=final_textbox)
    expect(textbox).to_be_visible()
   
   # fill firstname and last name if it required
    names(page, 'firstname', 'lastname')

    # click the subscribe
    page.wait_for_timeout(2000)
    # Subscribe button is in form of different text and types
    subscribe_btn = page.get_by_role('button', name=re.compile(r"(subscribe)", re.IGNORECASE))
    join_btn = page.get_by_role('button', name=re.compile(r"(join)", re.IGNORECASE))
    signup_button = page.get_by_role('button', name=re.compile(r"(sign up|sign me)", re.IGNORECASE))
    submit_button = page.get_by_role('button', name=re.compile(r"(submit)", re.IGNORECASE))
    subscribe_link = page.get_by_role('link', name=re.compile(r"(subscribe)", re.IGNORECASE))
    subscribe_activate = page.get_by_role('button', name=re.compile(r"(activate)", re.IGNORECASE))
    subscribe_offer = page.get_by_role('button', name=re.compile(r"(offer)", re.IGNORECASE))
    go_button = page.get_by_role('button', name=re.compile(r"(go)", re.IGNORECASE))
    off_button = page.get_by_role('button', name=re.compile(r"(off)", re.IGNORECASE))
    discount_button = page.get_by_role('button', name=re.compile(r"(discount|in)", re.IGNORECASE))
    coupon_code_button = page.get_by_role('button', name=re.compile(r"(coupon|code)", re.IGNORECASE))
   
    submit_cls = page.locator('.submit')
    final_btn = [ *subscribe_btn.all(), * join_btn.all(), * subscribe_link.all(),
                *signup_button.all(), *submit_button.all(),*subscribe_offer.all(),
                *subscribe_activate.all(),*go_button.all(), *off_button.all(),
                * discount_button.all(), *submit_cls.all(), *coupon_code_button.all() ]
    
    clicked_btn = wait_for_button_visible(buttons=final_btn)
    assert clicked_btn == True

    page.wait_for_timeout(2000)


def wait_for_button_visible(buttons):
     for item in buttons:
        try:
            item.click()
            return True
        except:
             print("An exception occurred")
    
    
    

def wait_for_textbox_visible(text_box):
      for item in text_box:
        try:
         
            item.click(timeout=1000)
            item.scroll_into_view_if_needed()
            email = conf()['email_Address']
            item.fill(email)
            return item
        except:
             print("An exception occurred")

def names(page, firstName, lastname):
    first = page.get_by_role('textbox', name=re.compile(r"(first)", re.IGNORECASE))
    last = page.get_by_role('textbox', name=re.compile(r"(last)", re.IGNORECASE))
  
    if(first.count()>0):
        first.fill(firstName)

    if(last.count()>0):
        last.fill(lastname)


def attemp_1_test_subscribe(page: Page, site):
    page.goto(f'https://{site}')

    email_button = page.get_by_role('textbox', name=re.compile(r"mail", re.IGNORECASE))
    email_button.scroll_into_view_if_needed()
    
    # set the email text field 
    email_button.evaluate("(node) => {node.value='test@email.com'}", 5)
    subsctibe = page.get_by_role('button', name=re.compile(r"(subscribe)", re.IGNORECASE))

    #click the subscribe or submit button
    subsctibe.evaluate("(node) => {node.click()}", 2)
    assert subsctibe.is_visible() == True