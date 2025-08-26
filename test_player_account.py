from playwright.sync_api import sync_playwright
import requests
import pytest

# MMORPG Player Account API Testing
BASE_URL = "https://api.example-game.com/v1"

def test_player_balance_query():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://game.example.com/login")
        page.fill("#username", "test_user")
        page.fill("#password", "secure123")
        page.click("#login-btn")
        assert page.is_visible("#dashboard")  # Verify login success

        # API Test: Query player balance
        response = requests.get(f"{BASE_URL}/player/balance?user_id=test_user")
        assert response.status_code == 200
        assert response.json()["balance"] >= 0  # Check valid balance
        browser.close()

def test_invalid_user():
    response = requests.get(f"{BASE_URL}/player/balance?user_id=invalid_user")
    assert response.status_code == 404  # Expect error for invalid user
