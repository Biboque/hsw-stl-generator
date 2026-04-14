from playwright.sync_api import sync_playwright

url = 'file:///G:/Users/Babique/Downloads/BABIQUES-HSW-GENERATOR/V1/test/BABIQUES-HSW-GENERATOR-v1_3_44.html'

console_logs = []
errors = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    def handle_console_message(msg):
        console_logs.append(f"[{msg.type}] {msg.text}")
        print(f"Console: [{msg.type}] {msg.text}")
        if msg.type == 'error':
            errors.append(msg.text)

    page.on("console", handle_console_message)

    page.goto(url)
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(2000)  # Wait a bit more for JS to run

    browser.close()

if errors:
    print("Errors found:")
    for err in errors:
        print(err)
else:
    print("No console errors detected.")