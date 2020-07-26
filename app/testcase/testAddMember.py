from app.page.app import App


class TestAddMember:
    def test_add_member_success(self):
        App().start().goto_contact().goto_add_member().add_member()
