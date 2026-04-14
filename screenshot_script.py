from playwright.sync_api import sync_playwright
import os

html_file_path = r'G:\Users\Babique\Downloads\BABIQUES-HSW-GENERATOR\V1\test\BABIQUES-HSW-GENERATOR-v1.3.4.html'
file_url = f'file://{html_file_path.replace(os.sep, "/")}'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    page.goto(file_url)
    page.wait_for_load_state('networkidle')
    page.screenshot(path='screenshot.png', full_page=True)
    browser.close()

print('Screenshot taken!')
