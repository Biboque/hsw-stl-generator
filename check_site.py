from playwright.sync_api import sync_playwright
import os

html_file_path = r'G:\Users\Babique\Downloads\BABIQUES-HSW-GENERATOR\V1\test\BABIQUES-HSW-GENERATOR-v1.3.4.html'
file_url = f'file://{html_file_path.replace(os.sep, "/")}'

console_logs = []
errors = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})

    def handle_console_message(msg):
        log_entry = f"[{msg.type}] {msg.text}"
        console_logs.append(log_entry)
        print(log_entry)
        if msg.type == 'error':
            errors.append(log_entry)

    page.on("console", handle_console_message)

    try:
        page.goto(file_url)
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(2000)  # Wait a bit for JS to initialize

        # Check if key elements exist
        sidebar = page.locator('#sidebar')
        canvas = page.locator('#canvas-container')
        hud = page.locator('#hud')

        elements_present = {
            'sidebar': sidebar.count() > 0,
            'canvas': canvas.count() > 0,
            'hud': hud.count() > 0
        }

        print(f"Elements present: {elements_present}")

        # Try to get some stats
        hex_count = page.locator('#hexCount').text_content() if page.locator('#hexCount').count() > 0 else 'N/A'
        print(f"Initial hex count: {hex_count}")

        # Take a verification screenshot
        page.screenshot(path='site_check.png', full_page=True)

    except Exception as e:
        errors.append(f"Exception: {str(e)}")
        print(f"Error during check: {e}")

    browser.close()

# Save logs
with open('console.log', 'w') as f:
    f.write('\n'.join(console_logs))

print(f"\nCheck completed. {len(console_logs)} console messages, {len(errors)} errors.")
if errors:
    print("Errors found:")
    for err in errors:
        print(f"  {err}")
else:
    print("No errors detected.")
