from fantasy_football_autodraft import EspnBrowser
from espn_secret import EspnSecret
import time

def current_url():
    browser = EspnBrowser()

    browser.open_page('https://www.espn.com.co')
    time.sleep(3)

    browser.login_espn(EspnSecret.email_espn, EspnSecret.password_espn)
    time.sleep(18)

    browser.search_nav_bar()
    time.sleep(3)

    browser.search_fantasy_link()
    time.sleep(3)

    browser.click_mock_draft_now()
    time.sleep(3)

    browser.click_join_league()
    time.sleep(3)

    browser.click_join_public_league()
    time.sleep(3)

    browser.click_join_a_league()
    time.sleep(3)

    browser.login_espn(EspnSecret.email_espn, EspnSecret.password_espn)
    time.sleep(2)

    browser.click_join_this_league()
    time.sleep(3)

    browser.click_edit_pre_draft_rankings()
    time.sleep(3)

    # Obtener la URL final
    final_url = browser.get_current_url()


    return final_url

if __name__ == '__main__':
    url_final = current_url()
    print(f"La URL final del draft es: {url_final}")
