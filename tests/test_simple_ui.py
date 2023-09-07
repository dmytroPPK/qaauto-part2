def test_check_title(driver):
    driver.get("https://google.com.ua")
    assert "Google" in driver.title


def test_check_search(driver):
    word = "wombat"
    driver.get(f"https://www.google.com.ua/search?q={word}")
    source = driver.page_source
    assert word in source
