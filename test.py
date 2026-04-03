from playwright.sync_api import sync_playwright, expect


def test_turkish_char_fix():
    test_data = [
        {"input": "iste gidiyorum", "expected": "işte gidiyorum"},
        {"input": "bir sey demeden", "expected": "bir şey demeden"},
        {"input": "arkami donmeden", "expected": "arkamı dönmeden"},
        {"input": "sikayet etmeden", "expected": "şikayet etmeden"},
        {"input": "hicbir sey almadan", "expected": "hiçbir şey almadan"},
        
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://turkcekarakter.com/")

        original_text_box = page.locator("#orijinalMetinTextArea")
        result_text_box = page.locator("#duzenlenmisMetinTextArea")

        for test_case in test_data:
            original_text_box.clear()
            original_text_box.fill(test_case["input"])

            page.get_by_role("button", name="İşlem Seçimi").click()
            page.get_by_text("Türkçe Harfleri Düzelt", exact=True).click()

            expect(result_text_box).to_have_value(test_case["expected"])

            page.get_by_role("button", name="Başa Dön").click()

        browser.close()


def test_turkish_char_fix_2():
    test_data = [
        {"input": "her bir adimda", "expected": "her bir adımda"},
        {"input": "pismanlik kalbimde", "expected": "pişmanlık kalbimde"},
        {"input": "yuruyorum sanki", "expected": "yürüyorum sanki"},
        {"input": "senin yaninda", "expected": "senin yanında"},
        {"input": "sesin uzaklasir", "expected": "sesin uzaklaşır"},
        {"input": "ne kusluk var ne", "expected": "ne küslük var ne"},
        
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://turkcekarakter.com/")

        original_text_box = page.locator("#orijinalMetinTextArea")
        result_text_box = page.locator("#duzenlenmisMetinTextArea")

        for test_case in test_data:
            original_text_box.clear()
            original_text_box.fill(test_case["input"])

            page.get_by_role("button", name="İşlem Seçimi").click()
            page.get_by_text("Türkçe Harfleri Düzelt", exact=True).click()

            expect(result_text_box).to_have_value(test_case["expected"])

            page.get_by_role("button", name="Başa Dön").click()

        browser.close()