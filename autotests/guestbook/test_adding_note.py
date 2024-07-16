import pytest
from autotests.pages.guestbook_page import GuestbookPage
from autotests.utils import wait_of_element_located


@pytest.mark.parametrize("note", ["test note"])
def test_add_note_to_guestbook(driver, note):
    guestbook_page = GuestbookPage(driver)
    guestbook_page.add_note_to_guestbook(note)
    new_note = wait_of_element_located(driver, "/html/body/table[2]/tbody/tr/td[3]/center/table/tbody/tr[2]/td[2]")
    assert note in new_note.text
