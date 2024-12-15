from playwright.sync_api import Page


def get_news(page: Page, itercount: int):
    page.wait_for_load_state("networkidle")
    news_feed = page.locator("div.SoaBEf").all()

    for news in news_feed:
        title = news.locator("div.n0jPhd").inner_text()
        print(f"title: {title}")

        news.click()
        page.wait_for_load_state("domcontentloaded", timeout=50000)

        section_exist = page.locator("section").count() > 0
        article_exist = page.locator("article").count() > 0

        if section_exist:
            content = "\n\n".join(page.locator("section").all_inner_texts())
        elif article_exist:
            content = "\n\n".join(page.locator("article").all_inner_texts())
        else:
            content = "\n\n".join(page.locator("div").all_inner_texts())

        save_to_md(f"news{itercount}.md", content)

        itercount += 1

        page.go_back()

    return itercount


def go_to_next_page(page: Page):
    next_button = page.get_by_role("link", name="Next")

    if next_button.is_visible():
        page.wait_for_load_state("domcontentloaded")
        next_button.click()
        page.wait_for_load_state("domcontentloaded")
        return True
    return False


def save_to_md(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"content saved to {filename}")


def test_get_started_link(page: Page):
    itercount = 0
    page.goto("https://google.co.id/")

    search_element = page.get_by_title("Search")
    # put your keyword here and uncomment the code below
    search_element.fill("bencana megathrust")
    # search_element.press("Enter")

    # page.wait_for_load_state("domcontentloaded")
    # news_section = page.get_by_role("link", name="News", exact=True)
    # news_section.click()

    # for i in range(2):
    #     itercount = get_news(page, itercount)
    #     if not go_to_next_page(page):
    #         print("No more pages or unable to navigate to the next page.")
    #         break
