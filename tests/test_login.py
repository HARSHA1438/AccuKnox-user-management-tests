from playwright.sync_api import Page
import time

class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_menu = page.locator("a[href='/web/index.php/admin/viewAdminModule']")
        self.add_button = page.locator("button:has-text('Add')")
        self.username_field = page.locator("input[placeholder='Username']")
        self.user_role_dropdown = page.locator("label:has-text('User Role') >> .. div[role='combobox']")
        self.status_dropdown = page.locator("label:has-text('Status') >> .. div[role='combobox']")
        self.employee_name_field = page.locator("input[placeholder='Type for hints...']")
        self.password_field = page.locator("input[type='password']").nth(0)
        self.confirm_password_field = page.locator("input[type='password']").nth(1)
        self.save_button = page.locator("button:has-text('Save')")
        self.search_username = page.locator("div input[placeholder='Username']")
        self.search_button = page.locator("button:has-text('Search')")
        self.edit_icon = page.locator("i.bi-pencil-fill").first
        self.delete_icon = page.locator("i.bi-trash").first
        self.confirm_delete = page.locator("button:has-text('Yes, Delete')")
    
    def go_to_admin(self):
        self.admin_menu.click()

    def add_user(self, username, employee_name, password):
        self.add_button.click()
        self.user_role_dropdown.click()
        self.page.locator("div[role='option']:has-text('Admin')").click()

        self.employee_name_field.fill(employee_name)
        time.sleep(1)  # Give dropdown time to load
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        self.status_dropdown.click()
        self.page.locator("div[role='option']:has-text('Enabled')").click()

        self.username_field.fill(username)
        self.password_field.fill(password)
        self.confirm_password_field.fill(password)
        self.save_button.click()

    def search_user(self, username):
        self.search_username.fill(username)
        self.search_button.click()

    def edit_user(self, new_username):
        self.edit_icon().click()
        self.username_field.fill(new_username)
        self.save_button.click()

    def delete_user(self):
        self.delete_icon().click()
        self.confirm_delete.click()