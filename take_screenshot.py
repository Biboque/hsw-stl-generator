from playwright.sync_api import sync_playwright
import os

html_file_path = os.path.abspath(r'G:\Users\Babique\Downloads\BABIQUES-HSW-GENERATOR\V1\test\BABIQUES-HSW-GENERATOR-v1.3.4.html')
file_url = f'file://{html_file_path}'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    page.goto(file_url)
    page.screenshot(path='screenshot.png', full_page=True)
    browser.close()

print("Screenshot taken!")